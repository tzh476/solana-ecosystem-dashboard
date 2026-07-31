#!/usr/bin/env python3
"""Generate a Solana ecosystem snapshot, report, and standalone dashboard.

The script is intentionally dependency-free so it can run in a clean Python
environment. It favors public, reproducible sources and records fetch errors
inside the snapshot instead of failing the entire report.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import math
import os
import pathlib
import signal
import statistics
import urllib.error
import urllib.request
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
SNAPSHOT_PATH = DATA_DIR / "solana_snapshot.json"
REPORT_PATH = ROOT / "report.md"
DASHBOARD_PATH = ROOT / "dashboard.html"

SOLANA_RPC = os.environ.get("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
COINGECKO_PRICE = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=solana&vs_currencies=usd&include_24hr_change=true"
)
DEFILLAMA_CHAINS = "https://api.llama.fi/v2/chains"
DEFILLAMA_SOL_PRICE = "https://coins.llama.fi/prices/current/coingecko:solana"
FETCH_DEADLINE_SECONDS = int(os.environ.get("FETCH_DEADLINE_SECONDS", "18"))


class FetchDeadlineExceeded(TimeoutError):
    """Raised when a data source exceeds the per-source wall-clock deadline."""


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()


def post_json(url: str, payload: dict[str, Any], timeout: int = 8) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "content-type": "application/json",
            "user-agent": "solana-ecosystem-dashboard/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_json(url: str, timeout: int = 8) -> Any:
    req = urllib.request.Request(url, headers={"user-agent": "solana-ecosystem-dashboard/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def rpc(method: str, params: list[Any] | None = None) -> dict[str, Any]:
    payload = {"jsonrpc": "2.0", "id": method, "method": method}
    if params is not None:
        payload["params"] = params
    return post_json(SOLANA_RPC, payload)


def safe_fetch(label: str, fn) -> tuple[Any | None, str | None]:
    def deadline_handler(_signum, _frame) -> None:
        raise FetchDeadlineExceeded(f"{label} exceeded {FETCH_DEADLINE_SECONDS}s")

    previous_handler = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, deadline_handler)
    signal.setitimer(signal.ITIMER_REAL, FETCH_DEADLINE_SECONDS)
    try:
        return fn(), None
    except (
        urllib.error.URLError,
        urllib.error.HTTPError,
        TimeoutError,
        json.JSONDecodeError,
        OSError,
        RuntimeError,
    ) as exc:
        return None, f"{label}: {type(exc).__name__}: {exc}"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)


def pct(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return numerator / denominator * 100


def compact_number(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    value = float(value)
    for suffix, scale in [("T", 1e12), ("B", 1e9), ("M", 1e6), ("K", 1e3)]:
        if abs(value) >= scale:
            return f"{value / scale:.2f}{suffix}"
    return f"{value:,.2f}" if not value.is_integer() else f"{int(value):,}"


def build_snapshot() -> dict[str, Any]:
    errors: list[str] = []
    fetched_at = utc_now()

    def fetch_rpc(method: str, params: list[Any] | None = None) -> Any:
        response = rpc(method, params)
        if "error" in response:
            raise RuntimeError(response["error"])
        return response.get("result")

    health, err = safe_fetch("getHealth", lambda: fetch_rpc("getHealth"))
    if err:
        errors.append(err)

    epoch_info, err = safe_fetch("getEpochInfo", lambda: fetch_rpc("getEpochInfo"))
    if err:
        errors.append(err)

    performance_samples, err = safe_fetch(
        "getRecentPerformanceSamples", lambda: fetch_rpc("getRecentPerformanceSamples", [24])
    )
    if err:
        errors.append(err)

    vote_accounts, err = safe_fetch("getVoteAccounts", lambda: fetch_rpc("getVoteAccounts"))
    if err:
        errors.append(err)

    supply, err = safe_fetch(
        "getSupply",
        lambda: fetch_rpc("getSupply", [{"excludeNonCirculatingAccountsList": True}]),
    )
    if err:
        errors.append(err)

    price_payload, err = safe_fetch("CoinGecko SOL price", lambda: get_json(COINGECKO_PRICE))
    if err:
        errors.append(err)

    fallback_price_payload = None
    if not (price_payload or {}).get("solana"):
        fallback_price_payload, err = safe_fetch(
            "DeFiLlama SOL price fallback", lambda: get_json(DEFILLAMA_SOL_PRICE)
        )
        if err:
            errors.append(err)

    chain_payload, err = safe_fetch("DeFiLlama chains", lambda: get_json(DEFILLAMA_CHAINS))
    if err:
        errors.append(err)

    samples = performance_samples or []
    sample_tps = []
    sample_slot_ms = []
    for sample in samples:
        seconds = sample.get("samplePeriodSecs") or 0
        tx = sample.get("numTransactions") or 0
        slots = sample.get("numSlots") or 0
        if seconds:
            sample_tps.append(tx / seconds)
        if slots:
            sample_slot_ms.append(seconds / slots * 1000)

    validators_current = (vote_accounts or {}).get("current") or []
    validators_delinquent = (vote_accounts or {}).get("delinquent") or []
    total_validators = len(validators_current) + len(validators_delinquent)
    current_stake = sum(v.get("activatedStake", 0) for v in validators_current)
    top_stakes = sorted((v.get("activatedStake", 0) for v in validators_current), reverse=True)
    top10_stake = sum(top_stakes[:10])

    coingecko = (price_payload or {}).get("solana") or {}
    fallback_sol = ((fallback_price_payload or {}).get("coins") or {}).get("coingecko:solana") or {}
    solana_chain = None
    if isinstance(chain_payload, list):
        for row in chain_payload:
            if str(row.get("name", "")).lower() == "solana":
                solana_chain = row
                break

    epoch_progress = None
    if epoch_info:
        epoch_progress = pct(epoch_info.get("slotIndex", 0), epoch_info.get("slotsInEpoch", 0))

    metrics = {
        "network": {
            "health": health,
            "epoch": (epoch_info or {}).get("epoch"),
            "absolute_slot": (epoch_info or {}).get("absoluteSlot"),
            "block_height": (epoch_info or {}).get("blockHeight"),
            "transaction_count": (epoch_info or {}).get("transactionCount"),
            "epoch_progress_pct": epoch_progress,
            "avg_tps_24_samples": statistics.fmean(sample_tps) if sample_tps else None,
            "latest_tps": sample_tps[0] if sample_tps else None,
            "avg_slot_time_ms_24_samples": statistics.fmean(sample_slot_ms) if sample_slot_ms else None,
            "latest_slot_time_ms": sample_slot_ms[0] if sample_slot_ms else None,
        },
        "validators": {
            "active": len(validators_current),
            "delinquent": len(validators_delinquent),
            "delinquent_pct": pct(len(validators_delinquent), total_validators),
            "top10_stake_pct": pct(top10_stake, current_stake),
        },
        "economics": {
            "sol_usd": coingecko.get("usd") or fallback_sol.get("price"),
            "sol_usd_24h_change_pct": coingecko.get("usd_24h_change"),
            "tvl_usd": (solana_chain or {}).get("tvl"),
            "stablecoins_usd": (solana_chain or {}).get("stablecoins"),
        },
        "supply": (supply or {}).get("value") if isinstance(supply, dict) else None,
    }

    anomalies = []
    latest_tps = metrics["network"]["latest_tps"]
    avg_slot_ms = metrics["network"]["avg_slot_time_ms_24_samples"]
    delinquent_pct = metrics["validators"]["delinquent_pct"]
    price_change = metrics["economics"]["sol_usd_24h_change_pct"]
    if latest_tps is not None and latest_tps < 1000:
        anomalies.append({"severity": "watch", "metric": "latest_tps", "message": "Latest TPS is below 1,000."})
    if avg_slot_ms is not None and avg_slot_ms > 700:
        anomalies.append({"severity": "watch", "metric": "avg_slot_time_ms", "message": "Average slot time is above 700 ms."})
    if delinquent_pct is not None and delinquent_pct > 5:
        anomalies.append({"severity": "watch", "metric": "validator_delinquency", "message": "Validator delinquency is above 5%."})
    if price_change is not None and abs(price_change) > 8:
        anomalies.append({"severity": "info", "metric": "sol_price_24h", "message": "SOL moved more than 8% over 24h."})
    if metrics["economics"]["tvl_usd"] is None:
        anomalies.append({"severity": "info", "metric": "tvl", "message": "DeFiLlama TVL was unavailable in this run."})
    if errors:
        anomalies.append({"severity": "info", "metric": "data_fetch", "message": "One or more data sources returned errors."})

    return {
        "generated_at": fetched_at,
        "sources": {
            "solana_rpc": SOLANA_RPC,
            "coingecko_price": COINGECKO_PRICE,
            "defillama_sol_price_fallback": DEFILLAMA_SOL_PRICE,
            "defillama_chains": DEFILLAMA_CHAINS,
        },
        "metrics": metrics,
        "samples": {
            "recent_performance": samples,
        },
        "anomalies": anomalies,
        "errors": errors,
    }


def render_report(snapshot: dict[str, Any]) -> str:
    m = snapshot["metrics"]
    n = m["network"]
    v = m["validators"]
    e = m["economics"]
    rows = [
        ("Network health", n["health"]),
        ("Epoch", n["epoch"]),
        ("Epoch progress", f"{n['epoch_progress_pct']:.2f}%" if n["epoch_progress_pct"] is not None else "n/a"),
        ("Absolute slot", compact_number(n["absolute_slot"])),
        ("Block height", compact_number(n["block_height"])),
        ("Transactions processed", compact_number(n["transaction_count"])),
        ("Latest TPS", compact_number(n["latest_tps"])),
        ("Average TPS, last 24 samples", compact_number(n["avg_tps_24_samples"])),
        ("Average slot time, last 24 samples", f"{n['avg_slot_time_ms_24_samples']:.0f} ms" if n["avg_slot_time_ms_24_samples"] is not None else "n/a"),
        ("Active validators", compact_number(v["active"])),
        ("Delinquent validators", compact_number(v["delinquent"])),
        ("Delinquent validator ratio", f"{v['delinquent_pct']:.2f}%" if v["delinquent_pct"] is not None else "n/a"),
        ("Top 10 validator stake share", f"{v['top10_stake_pct']:.2f}%" if v["top10_stake_pct"] is not None else "n/a"),
        ("SOL price", f"${e['sol_usd']:.2f}" if e["sol_usd"] is not None else "n/a"),
        ("SOL 24h change", f"{e['sol_usd_24h_change_pct']:.2f}%" if e["sol_usd_24h_change_pct"] is not None else "n/a"),
        ("Solana TVL", f"${compact_number(e['tvl_usd'])}" if e["tvl_usd"] is not None else "n/a"),
    ]

    lines = [
        "# Solana Ecosystem Auto-Updating Report",
        "",
        f"Generated: `{snapshot['generated_at']}`",
        "",
        "## Executive Summary",
        "",
        "This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.",
        "",
        "## Metrics",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
    ]
    for name, value in rows:
        lines.append(f"| {name} | {value} |")

    lines.extend(["", "## Anomaly Flags", ""])
    if snapshot["anomalies"]:
        for item in snapshot["anomalies"]:
            lines.append(f"- **{item['severity']} / {item['metric']}**: {item['message']}")
    else:
        lines.append("- No threshold-based anomalies detected in this run.")

    lines.extend([
        "",
        "## Automation Notes",
        "",
        "- The same script refreshes JSON, Markdown, and HTML outputs.",
        "- Solana RPC data covers live chain health, epoch, recent performance, validators, and supply.",
        "- CoinGecko and DeFiLlama provide economic context outside the validator/runtime layer.",
        "- Thresholds are intentionally simple and visible so reviewers can tune them without reverse-engineering the pipeline.",
        "",
        "## Source URLs",
        "",
    ])
    for label, url in snapshot["sources"].items():
        lines.append(f"- {label}: {url}")
    if snapshot["errors"]:
        lines.extend(["", "## Fetch Errors", ""])
        for err in snapshot["errors"]:
            lines.append(f"- {err}")
    return "\n".join(lines) + "\n"


def render_dashboard(snapshot: dict[str, Any]) -> str:
    data = json.dumps(snapshot, ensure_ascii=False)
    escaped = html.escape(data)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Solana Ecosystem Dashboard</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #07110f;
      --panel: #101c19;
      --panel2: #132923;
      --line: #25443d;
      --text: #ecfff8;
      --muted: #9bb8ae;
      --accent: #8ef9c4;
      --warn: #ffd166;
      --bad: #ff7d7d;
    }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: radial-gradient(circle at top left, #16352d, var(--bg) 40%);
      color: var(--text);
    }}
    main {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 32px 20px 56px;
    }}
    header {{
      display: flex;
      justify-content: space-between;
      gap: 24px;
      align-items: flex-end;
      border-bottom: 1px solid var(--line);
      padding-bottom: 22px;
      margin-bottom: 24px;
    }}
    h1, h2 {{ margin: 0; letter-spacing: 0; }}
    h1 {{ font-size: 32px; line-height: 1.1; }}
    h2 {{ font-size: 17px; margin-bottom: 14px; }}
    .muted {{ color: var(--muted); }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px;
    }}
    .card {{
      background: linear-gradient(180deg, var(--panel), var(--panel2));
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
      min-height: 92px;
    }}
    .label {{
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .08em;
    }}
    .value {{
      margin-top: 10px;
      font-size: 28px;
      font-weight: 720;
      white-space: nowrap;
    }}
    section {{ margin-top: 24px; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      overflow: hidden;
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    th, td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--line);
      text-align: left;
    }}
    th {{ color: var(--muted); font-weight: 600; background: #0e1917; }}
    tr:last-child td {{ border-bottom: 0; }}
    .pill {{
      display: inline-flex;
      align-items: center;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 5px 10px;
      margin: 4px 6px 4px 0;
      color: var(--muted);
      background: #0d1715;
      font-size: 13px;
    }}
    .ok {{ color: var(--accent); }}
    .warn {{ color: var(--warn); }}
    .bad {{ color: var(--bad); }}
    pre {{
      overflow: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      background: #07100f;
      color: #c9ffe7;
      max-height: 320px;
    }}
    @media (max-width: 880px) {{
      header {{ display: block; }}
      .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 520px) {{
      .grid {{ grid-template-columns: 1fr; }}
      .value {{ font-size: 24px; }}
    }}
  </style>
</head>
<body>
<main>
  <header>
    <div>
      <p class="muted">Auto-updating public-data snapshot</p>
      <h1>Solana Ecosystem Dashboard</h1>
    </div>
    <div class="muted">Generated <span id="generated"></span></div>
  </header>

  <section class="grid" id="cards"></section>

  <section>
    <h2>Anomaly Flags</h2>
    <div id="anomalies"></div>
  </section>

  <section>
    <h2>Metric Table</h2>
    <table>
      <thead><tr><th>Metric</th><th>Value</th><th>Layer</th></tr></thead>
      <tbody id="metrics"></tbody>
    </table>
  </section>

  <section>
    <h2>Data Sources</h2>
    <div id="sources"></div>
  </section>

  <section>
    <h2>Machine-Readable Snapshot</h2>
    <pre id="raw"></pre>
  </section>
</main>
<script id="snapshot" type="application/json">{escaped}</script>
<script>
const snapshot = JSON.parse(document.getElementById('snapshot').textContent);
const m = snapshot.metrics;
const compact = (value) => {{
  if (value === null || value === undefined || Number.isNaN(value)) return 'n/a';
  const abs = Math.abs(Number(value));
  if (abs >= 1e12) return (value / 1e12).toFixed(2) + 'T';
  if (abs >= 1e9) return (value / 1e9).toFixed(2) + 'B';
  if (abs >= 1e6) return (value / 1e6).toFixed(2) + 'M';
  if (abs >= 1e3) return (value / 1e3).toFixed(2) + 'K';
  return Number(value).toLocaleString(undefined, {{ maximumFractionDigits: 2 }});
}};
const pct = (value) => value === null || value === undefined ? 'n/a' : Number(value).toFixed(2) + '%';
const ms = (value) => value === null || value === undefined ? 'n/a' : Number(value).toFixed(0) + ' ms';
document.getElementById('generated').textContent = snapshot.generated_at;

const cards = [
  ['Network health', m.network.health || 'n/a', 'runtime'],
  ['Latest TPS', compact(m.network.latest_tps), 'performance'],
  ['Avg slot time', ms(m.network.avg_slot_time_ms_24_samples), 'performance'],
  ['Epoch progress', pct(m.network.epoch_progress_pct), 'runtime'],
  ['Active validators', compact(m.validators.active), 'validators'],
  ['Delinquent validators', pct(m.validators.delinquent_pct), 'validators'],
  ['SOL price', m.economics.sol_usd ? '$' + Number(m.economics.sol_usd).toFixed(2) : 'n/a', 'markets'],
  ['TVL', m.economics.tvl_usd ? '$' + compact(m.economics.tvl_usd) : 'n/a', 'markets'],
];
document.getElementById('cards').innerHTML = cards.map(([label, value, layer]) => `
  <article class="card"><div class="label">${{label}}</div><div class="value">${{value}}</div><div class="muted">${{layer}}</div></article>
`).join('');

const rows = [
  ['Epoch', m.network.epoch, 'runtime'],
  ['Absolute slot', compact(m.network.absolute_slot), 'runtime'],
  ['Block height', compact(m.network.block_height), 'runtime'],
  ['Transactions processed', compact(m.network.transaction_count), 'runtime'],
  ['Average TPS, 24 samples', compact(m.network.avg_tps_24_samples), 'performance'],
  ['Latest TPS', compact(m.network.latest_tps), 'performance'],
  ['Average slot time, 24 samples', ms(m.network.avg_slot_time_ms_24_samples), 'performance'],
  ['Latest slot time', ms(m.network.latest_slot_time_ms), 'performance'],
  ['Active validators', compact(m.validators.active), 'validators'],
  ['Delinquent validators', compact(m.validators.delinquent), 'validators'],
  ['Delinquent validator ratio', pct(m.validators.delinquent_pct), 'validators'],
  ['Top 10 validator stake share', pct(m.validators.top10_stake_pct), 'validators'],
  ['SOL 24h change', pct(m.economics.sol_usd_24h_change_pct), 'markets'],
  ['Stablecoins', m.economics.stablecoins_usd ? '$' + compact(m.economics.stablecoins_usd) : 'n/a', 'markets'],
];
document.getElementById('metrics').innerHTML = rows.map(([name, value, layer]) => `<tr><td>${{name}}</td><td>${{value}}</td><td>${{layer}}</td></tr>`).join('');

document.getElementById('anomalies').innerHTML = snapshot.anomalies.length
  ? snapshot.anomalies.map(a => `<span class="pill ${{a.severity === 'watch' ? 'warn' : 'ok'}}">${{a.severity}} / ${{a.metric}}: ${{a.message}}</span>`).join('')
  : '<span class="pill ok">No threshold-based anomalies detected</span>';

document.getElementById('sources').innerHTML = Object.entries(snapshot.sources)
  .map(([name, url]) => `<span class="pill">${{name}}: <a href="${{url}}" target="_blank" rel="noreferrer" style="color:var(--accent);margin-left:6px;">source</a></span>`)
  .join('');
document.getElementById('raw').textContent = JSON.stringify(snapshot, null, 2);
</script>
</body>
</html>
"""


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    snapshot = build_snapshot()
    SNAPSHOT_PATH.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    REPORT_PATH.write_text(render_report(snapshot), encoding="utf-8")
    DASHBOARD_PATH.write_text(render_dashboard(snapshot), encoding="utf-8")
    print(f"Wrote {SNAPSHOT_PATH}")
    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {DASHBOARD_PATH}")


if __name__ == "__main__":
    main()

# Submission Draft

## Link

Live dashboard: https://tzh476.github.io/solana-ecosystem-dashboard/

Repository: https://github.com/tzh476/solana-ecosystem-dashboard

## Short Description

I built an auto-updating Solana ecosystem report and interactive dashboard. It pulls live data from Solana JSON-RPC, CoinGecko, and DeFiLlama, then generates a machine-readable JSON snapshot, a Markdown report, and a dark-theme HTML dashboard.

## What Is Automated

- Network health, epoch progress, slot, block height, and transaction count from Solana RPC.
- Recent performance samples with computed TPS and slot time.
- Validator active/delinquent counts and stake concentration metrics.
- SOL price and 24-hour price movement from CoinGecko.
- Solana TVL, stablecoin supply, and 24-hour DEX volume from DeFiLlama.
- Simple anomaly flags for low TPS, slow slot time, validator delinquency, price moves, and TVL source availability.
- Per-source failures remain visible in every generated output instead of silently presenting stale values as live data.
- GitHub Actions refreshes the generated outputs every six hours; the workflow can also be run manually for an auditable fresh snapshot.

## Files

- `data/solana_snapshot.json`
- `report.md`
- `dashboard.html`
- `fetch_solana_dashboard.py`

## Owner Action Needed

If the Superteam form requires accepting Terms of Use or confirming eligibility, the account owner must complete that action directly.

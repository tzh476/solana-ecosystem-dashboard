# Submission Draft

## Link

Use the hosted or repository link to `dashboard.html` once published.

## Short Description

I built an auto-updating Solana ecosystem report and interactive dashboard. It pulls live data from Solana JSON-RPC, CoinGecko, and DeFiLlama, then generates a machine-readable JSON snapshot, a Markdown report, and a dark-theme HTML dashboard.

## What Is Automated

- Network health, epoch progress, slot, block height, and transaction count from Solana RPC.
- Recent performance samples with computed TPS and slot time.
- Validator active/delinquent counts and stake concentration metrics.
- SOL price and 24-hour price movement from CoinGecko.
- Solana TVL from DeFiLlama.
- Simple anomaly flags for low TPS, slow slot time, validator delinquency, price moves, and TVL source availability.

## Files

- `data/solana_snapshot.json`
- `report.md`
- `dashboard.html`
- `fetch_solana_dashboard.py`

## Owner Action Needed

If the Superteam form requires accepting Terms of Use or confirming eligibility, the account owner must complete that action directly.

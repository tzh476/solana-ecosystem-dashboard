# Solana Ecosystem Auto-Updating Dashboard

Submission package for the Superteam Canada bounty:
https://earn.superteam.fun/listing/develop-solana-ecosystem-auto-updating-report-and-interactive-dashboard

## What This Produces

- `data/solana_snapshot.json`: machine-readable snapshot from public APIs.
- `report.md`: human-readable ecosystem report with metric notes and anomaly flags.
- `dashboard.html`: standalone dark-theme interactive dashboard.

## Data Sources

- Solana mainnet-beta JSON-RPC:
  - `getHealth`
  - `getEpochInfo`
  - `getRecentPerformanceSamples`
  - `getVoteAccounts`
  - `getSupply`
- CoinGecko simple price API for SOL price and 24h change.
- DeFiLlama Coins as a SOL price fallback when CoinGecko is unavailable.
- DeFiLlama chain TVL endpoint for Solana TVL.

## Run

```bash
python3 fetch_solana_dashboard.py
```

To use a different public or private Solana RPC endpoint:

```bash
SOLANA_RPC_URL=https://solana-rpc.publicnode.com python3 fetch_solana_dashboard.py
```

The script intentionally uses only Python standard-library modules. It writes all outputs into this directory and can be run repeatedly to refresh the report.

Each source has a wall-clock deadline so one slow API cannot block the whole report. Failed sources are recorded in the JSON snapshot, Markdown report, and dashboard anomaly section.

## Submission Notes

This artifact is not submitted yet. Superteam final submission may require agreeing to Terms of Use or other account-side declarations; that step must be performed by the account owner.

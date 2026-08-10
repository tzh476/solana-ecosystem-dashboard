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
- DeFiLlama chain, stablecoin-history, and DEX-volume endpoints for Solana TVL, stablecoin supply, and 24h DEX volume.

## Run

```bash
python3 fetch_solana_dashboard.py
```

To use a different public or private Solana RPC endpoint:

```bash
SOLANA_RPC_URL=https://solana-rpc.publicnode.com python3 fetch_solana_dashboard.py
```

The script intentionally uses only Python standard-library modules. It writes all outputs into this directory and can be run repeatedly to refresh the report.

Independent third-party sources are fetched concurrently with a bounded HTTP timeout, while calls to the same public Solana RPC stay ordered to avoid rate-limit failures. Failed sources are recorded in the JSON snapshot, Markdown report, and dashboard anomaly section.

The dashboard is intentionally a generated static artifact: run the script locally or from any scheduler, then publish the resulting JSON, Markdown, and HTML together. This keeps the live-data provenance reviewable and avoids API keys, embedded credentials, or browser-only state.

The included GitHub Actions workflow also refreshes these generated files every six hours and can be run manually from the Actions tab.

## Submission Notes

This artifact is not submitted yet. Superteam final submission may require agreeing to Terms of Use or other account-side declarations; that step must be performed by the account owner.

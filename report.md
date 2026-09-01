# Solana Ecosystem Auto-Updating Report

Generated: `2026-09-01T21:01:47+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1026 |
| Epoch progress | 66.74% |
| Absolute slot | 443.52M |
| Block height | 421.57M |
| Transactions processed | 544.24B |
| Latest TPS | 4.47K |
| Average TPS, last 24 samples | 4.28K |
| Average slot time, last 24 samples | 316 ms |
| Active validators | 678 |
| Delinquent validators | 16 |
| Delinquent validator ratio | 2.31% |
| Top 10 validator stake share | 24.18% |
| SOL price | $100.05 |
| SOL 24h change | -3.54% |
| Solana TVL | $5.72B |
| Stablecoin supply | $15.91B |
| DEX volume, 24h | $2.50B |

## Anomaly Flags

- No threshold-based anomalies detected in this run.

## Automation Notes

- The same script refreshes JSON, Markdown, and HTML outputs.
- Solana RPC data covers live chain health, epoch, recent performance, validators, and supply.
- CoinGecko and DeFiLlama provide price, TVL, stablecoin-supply, and DEX-volume context outside the validator/runtime layer.
- Independent external sources fetch concurrently with per-request timeouts; calls to one public RPC stay ordered to avoid rate-limit failures.
- Thresholds are intentionally simple and visible so reviewers can tune them without reverse-engineering the pipeline.

## Source URLs

- solana_rpc: https://api.mainnet-beta.solana.com
- coingecko_price: https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true
- defillama_sol_price_fallback: https://coins.llama.fi/prices/current/coingecko:solana
- defillama_chains: https://api.llama.fi/v2/chains
- defillama_solana_dex_volume: https://api.llama.fi/overview/dexs/solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- defillama_solana_stablecoins: https://stablecoins.llama.fi/stablecoincharts/Solana

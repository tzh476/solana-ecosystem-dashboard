# Solana Ecosystem Auto-Updating Report

Generated: `2026-10-22T21:34:37+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1065 |
| Epoch progress | 25.38% |
| Absolute slot | 460.19M |
| Block height | 438.22M |
| Transactions processed | 563.29B |
| Latest TPS | 1.70K |
| Average TPS, last 24 samples | 2.32K |
| Average slot time, last 24 samples | 212 ms |
| Active validators | 655 |
| Delinquent validators | 21 |
| Delinquent validator ratio | 3.11% |
| Top 10 validator stake share | 24.46% |
| SOL price | $103.69 |
| SOL 24h change | -4.25% |
| Solana TVL | $5.87B |
| Stablecoin supply | $16.08B |
| DEX volume, 24h | $2.27B |

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

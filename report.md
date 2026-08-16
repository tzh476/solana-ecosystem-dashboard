# Solana Ecosystem Auto-Updating Report

Generated: `2026-08-16T06:58:24+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1017 |
| Epoch progress | 57.83% |
| Absolute slot | 439.59M |
| Block height | 417.64M |
| Transactions processed | 538.61B |
| Latest TPS | 2.83K |
| Average TPS, last 24 samples | 2.84K |
| Average slot time, last 24 samples | 414 ms |
| Active validators | 688 |
| Delinquent validators | 9 |
| Delinquent validator ratio | 1.29% |
| Top 10 validator stake share | 24.40% |
| SOL price | $75.33 |
| SOL 24h change | -0.06% |
| Solana TVL | $4.81B |
| Stablecoin supply | $15.94B |
| DEX volume, 24h | $1.23B |

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

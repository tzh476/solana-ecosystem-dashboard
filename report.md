# Solana Ecosystem Auto-Updating Report

Generated: `2026-09-09T04:40:56+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1031 |
| Epoch progress | 30.17% |
| Absolute slot | 445.52M |
| Block height | 423.57M |
| Transactions processed | 546.58B |
| Latest TPS | 3.74K |
| Average TPS, last 24 samples | 3.62K |
| Average slot time, last 24 samples | 317 ms |
| Active validators | 676 |
| Delinquent validators | 11 |
| Delinquent validator ratio | 1.60% |
| Top 10 validator stake share | 24.25% |
| SOL price | $104.01 |
| SOL 24h change | 0.59% |
| Solana TVL | $5.96B |
| Stablecoin supply | $16.57B |
| DEX volume, 24h | $2.58B |

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

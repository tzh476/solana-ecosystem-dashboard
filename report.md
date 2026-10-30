# Solana Ecosystem Auto-Updating Report

Generated: `2026-10-30T22:18:11+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1072 |
| Epoch progress | 80.18% |
| Absolute slot | 463.45M |
| Block height | 441.47M |
| Transactions processed | 564.53B |
| Latest TPS | 1.77K |
| Average TPS, last 24 samples | 1.57K |
| Average slot time, last 24 samples | 215 ms |
| Active validators | 667 |
| Delinquent validators | 24 |
| Delinquent validator ratio | 3.47% |
| Top 10 validator stake share | 24.79% |
| SOL price | $95.50 |
| SOL 24h change | -1.29% |
| Solana TVL | $5.40B |
| Stablecoin supply | $15.38B |
| DEX volume, 24h | $2.30B |

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

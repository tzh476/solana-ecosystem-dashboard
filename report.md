# Solana Ecosystem Auto-Updating Report

Generated: `2026-11-17T20:53:57+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1089 |
| Epoch progress | 52.49% |
| Absolute slot | 470.67M |
| Block height | 448.69M |
| Transactions processed | 567.15B |
| Latest TPS | 1.99K |
| Average TPS, last 24 samples | 1.91K |
| Average slot time, last 24 samples | 216 ms |
| Active validators | 661 |
| Delinquent validators | 5 |
| Delinquent validator ratio | 0.75% |
| Top 10 validator stake share | 24.77% |
| SOL price | $72.80 |
| SOL 24h change | 1.85% |
| Solana TVL | $4.72B |
| Stablecoin supply | $14.25B |
| DEX volume, 24h | $1.48B |

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

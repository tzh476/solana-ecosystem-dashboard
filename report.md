# Solana Ecosystem Auto-Updating Report

Generated: `2026-10-09T22:37:26+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1053 |
| Epoch progress | 30.27% |
| Absolute slot | 455.03M |
| Block height | 433.06M |
| Transactions processed | 558.09B |
| Latest TPS | 4.95K |
| Average TPS, last 24 samples | 5.01K |
| Average slot time, last 24 samples | 218 ms |
| Active validators | 674 |
| Delinquent validators | 6 |
| Delinquent validator ratio | 0.88% |
| Top 10 validator stake share | 24.63% |
| SOL price | $109.19 |
| SOL 24h change | -0.96% |
| Solana TVL | $6.18B |
| Stablecoin supply | $16.31B |
| DEX volume, 24h | $2.64B |

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

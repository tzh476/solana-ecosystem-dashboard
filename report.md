# Solana Ecosystem Auto-Updating Report

Generated: `2026-11-09T22:20:04+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1082 |
| Epoch progress | 13.63% |
| Absolute slot | 467.48M |
| Block height | 445.50M |
| Transactions processed | 565.96B |
| Latest TPS | 1.83K |
| Average TPS, last 24 samples | 1.71K |
| Average slot time, last 24 samples | 215 ms |
| Active validators | 657 |
| Delinquent validators | 41 |
| Delinquent validator ratio | 5.87% |
| Top 10 validator stake share | 24.62% |
| SOL price | $86.37 |
| SOL 24h change | -0.29% |
| Solana TVL | $5.09B |
| Stablecoin supply | $14.98B |
| DEX volume, 24h | $1.04B |

## Anomaly Flags

- **watch / validator_delinquency**: Validator delinquency is above 5%.

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

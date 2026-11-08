# Solana Ecosystem Auto-Updating Report

Generated: `2026-11-08T22:03:09+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1081 |
| Epoch progress | 19.37% |
| Absolute slot | 467.08M |
| Block height | 445.09M |
| Transactions processed | 565.82B |
| Latest TPS | 2.71K |
| Average TPS, last 24 samples | 2.51K |
| Average slot time, last 24 samples | 214 ms |
| Active validators | 661 |
| Delinquent validators | 36 |
| Delinquent validator ratio | 5.16% |
| Top 10 validator stake share | 24.66% |
| SOL price | $86.15 |
| SOL 24h change | -3.32% |
| Solana TVL | $5.22B |
| Stablecoin supply | $15.07B |
| DEX volume, 24h | $917.44M |

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

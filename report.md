# Solana Ecosystem Auto-Updating Report

Generated: `2026-11-14T17:59:36+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1086 |
| Epoch progress | 62.10% |
| Absolute slot | 469.42M |
| Block height | 447.44M |
| Transactions processed | 566.69B |
| Latest TPS | 1.78K |
| Average TPS, last 24 samples | 1.94K |
| Average slot time, last 24 samples | 215 ms |
| Active validators | 661 |
| Delinquent validators | 38 |
| Delinquent validator ratio | 5.44% |
| Top 10 validator stake share | 24.75% |
| SOL price | $72.71 |
| SOL 24h change | -9.02% |
| Solana TVL | $4.78B |
| Stablecoin supply | $14.14B |
| DEX volume, 24h | $1.56B |

## Anomaly Flags

- **watch / validator_delinquency**: Validator delinquency is above 5%.
- **info / sol_price_24h**: SOL moved more than 8% over 24h.

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

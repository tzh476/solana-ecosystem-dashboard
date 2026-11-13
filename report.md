# Solana Ecosystem Auto-Updating Report

Generated: `2026-11-13T06:42:41+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1085 |
| Epoch progress | 25.49% |
| Absolute slot | 468.83M |
| Block height | 446.85M |
| Transactions processed | 566.47B |
| Latest TPS | 1.66K |
| Average TPS, last 24 samples | 1.82K |
| Average slot time, last 24 samples | 215 ms |
| Active validators | 655 |
| Delinquent validators | 44 |
| Delinquent validator ratio | 6.29% |
| Top 10 validator stake share | 23.73% |
| SOL price | $79.89 |
| SOL 24h change | -3.44% |
| Solana TVL | $4.93B |
| Stablecoin supply | $14.29B |
| DEX volume, 24h | $1.51B |

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

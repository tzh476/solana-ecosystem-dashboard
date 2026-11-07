# Solana Ecosystem Auto-Updating Report

Generated: `2026-11-07T12:58:47+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1079 |
| Epoch progress | 90.95% |
| Absolute slot | 466.52M |
| Block height | 444.54M |
| Transactions processed | 565.65B |
| Latest TPS | 1.07K |
| Average TPS, last 24 samples | 1.25K |
| Average slot time, last 24 samples | 214 ms |
| Active validators | 660 |
| Delinquent validators | 36 |
| Delinquent validator ratio | 5.17% |
| Top 10 validator stake share | 24.72% |
| SOL price | $89.67 |
| SOL 24h change | -0.50% |
| Solana TVL | $5.24B |
| Stablecoin supply | $14.76B |
| DEX volume, 24h | $1.48B |

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

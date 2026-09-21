# Solana Ecosystem Auto-Updating Report

Generated: `2026-09-21T21:58:18+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1039 |
| Epoch progress | 77.55% |
| Absolute slot | 449.18M |
| Block height | 427.22M |
| Transactions processed | 551.09B |
| Latest TPS | 4.77K |
| Average TPS, last 24 samples | 4.76K |
| Average slot time, last 24 samples | 268 ms |
| Active validators | 675 |
| Delinquent validators | 15 |
| Delinquent validator ratio | 2.17% |
| Top 10 validator stake share | 24.28% |
| SOL price | $119.18 |
| SOL 24h change | 8.52% |
| Solana TVL | $6.49B |
| Stablecoin supply | $15.84B |
| DEX volume, 24h | $2.80B |

## Anomaly Flags

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

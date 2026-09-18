# Solana Ecosystem Auto-Updating Report

Generated: `2026-09-18T20:53:52+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1037 |
| Epoch progress | 49.32% |
| Absolute slot | 448.20M |
| Block height | 426.24M |
| Transactions processed | 549.93B |
| Latest TPS | 5.50K |
| Average TPS, last 24 samples | 4.72K |
| Average slot time, last 24 samples | 268 ms |
| Active validators | 676 |
| Delinquent validators | 12 |
| Delinquent validator ratio | 1.74% |
| Top 10 validator stake share | 24.28% |
| SOL price | $113.55 |
| SOL 24h change | 12.31% |
| Solana TVL | $6.27B |
| Stablecoin supply | $15.65B |
| DEX volume, 24h | $2.59B |

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

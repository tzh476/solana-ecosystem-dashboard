# Solana Ecosystem Auto-Updating Report

Generated: `2026-09-13T11:50:39+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1034 |
| Epoch progress | 1.79% |
| Absolute slot | 446.70M |
| Block height | 424.74M |
| Transactions processed | 548.02B |
| Latest TPS | 3.30K |
| Average TPS, last 24 samples | 3.42K |
| Average slot time, last 24 samples | 315 ms |
| Active validators | 677 |
| Delinquent validators | 12 |
| Delinquent validator ratio | 1.74% |
| Top 10 validator stake share | 24.39% |
| SOL price | $99.72 |
| SOL 24h change | -2.25% |
| Solana TVL | $5.84B |
| Stablecoin supply | $16.46B |
| DEX volume, 24h | $1.69B |

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

# Solana Ecosystem Auto-Updating Report

Generated: `2026-08-28T11:22:29+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1023 |
| Epoch progress | 90.81% |
| Absolute slot | 442.33M |
| Block height | 420.38M |
| Transactions processed | 542.71B |
| Latest TPS | 3.56K |
| Average TPS, last 24 samples | 3.41K |
| Average slot time, last 24 samples | 364 ms |
| Active validators | 688 |
| Delinquent validators | 10 |
| Delinquent validator ratio | 1.43% |
| Top 10 validator stake share | 24.28% |
| SOL price | $106.55 |
| SOL 24h change | 1.82% |
| Solana TVL | $5.93B |
| Stablecoin supply | $16.32B |
| DEX volume, 24h | $3.70B |

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

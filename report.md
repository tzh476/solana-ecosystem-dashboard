# Solana Ecosystem Auto-Updating Report

Generated: `2026-09-02T21:02:22+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1027 |
| Epoch progress | 30.24% |
| Absolute slot | 443.79M |
| Block height | 421.84M |
| Transactions processed | 544.56B |
| Latest TPS | 3.36K |
| Average TPS, last 24 samples | 3.78K |
| Average slot time, last 24 samples | 314 ms |
| Active validators | 675 |
| Delinquent validators | 20 |
| Delinquent validator ratio | 2.88% |
| Top 10 validator stake share | 24.33% |
| SOL price | $99.69 |
| SOL 24h change | -0.35% |
| Solana TVL | $5.68B |
| Stablecoin supply | $15.78B |
| DEX volume, 24h | $2.17B |

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

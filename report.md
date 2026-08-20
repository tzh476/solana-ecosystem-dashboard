# Solana Ecosystem Auto-Updating Report

Generated: `2026-08-20T07:05:48+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1019 |
| Epoch progress | 50.54% |
| Absolute slot | 440.43M |
| Block height | 418.48M |
| Transactions processed | 539.89B |
| Latest TPS | 3.02K |
| Average TPS, last 24 samples | 2.99K |
| Average slot time, last 24 samples | 417 ms |
| Active validators | 688 |
| Delinquent validators | 8 |
| Delinquent validator ratio | 1.15% |
| Top 10 validator stake share | 24.38% |
| SOL price | $85.79 |
| SOL 24h change | 11.52% |
| Solana TVL | $5.20B |
| Stablecoin supply | $16.26B |
| DEX volume, 24h | $2.79B |

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

# Solana Ecosystem Auto-Updating Report

Generated: `2026-11-01T13:22:37+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1074 |
| Epoch progress | 32.25% |
| Absolute slot | 464.11M |
| Block height | 442.13M |
| Transactions processed | 564.71B |
| Latest TPS | 966.10 |
| Average TPS, last 24 samples | 1.66K |
| Average slot time, last 24 samples | 215 ms |
| Active validators | 662 |
| Delinquent validators | 34 |
| Delinquent validator ratio | 4.89% |
| Top 10 validator stake share | 24.95% |
| SOL price | $94.94 |
| SOL 24h change | -0.80% |
| Solana TVL | $5.43B |
| Stablecoin supply | $15.43B |
| DEX volume, 24h | $953.37M |

## Anomaly Flags

- **watch / latest_tps**: Latest TPS is below 1,000.

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

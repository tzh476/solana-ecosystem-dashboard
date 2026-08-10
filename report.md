# Solana Ecosystem Auto-Updating Report

Generated: `2026-08-10T02:47:47+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1014 |
| Epoch progress | 62.75% |
| Absolute slot | 438.32M |
| Block height | 416.37M |
| Transactions processed | 536.71B |
| Latest TPS | 3.12K |
| Average TPS, last 24 samples | 3.40K |
| Average slot time, last 24 samples | 422 ms |
| Active validators | 691 |
| Delinquent validators | 7 |
| Delinquent validator ratio | 1.00% |
| Top 10 validator stake share | 24.39% |
| SOL price | $76.76 |
| SOL 24h change | 1.17% |
| Solana TVL | $4.84B |

## Anomaly Flags

- No threshold-based anomalies detected in this run.

## Automation Notes

- The same script refreshes JSON, Markdown, and HTML outputs.
- Solana RPC data covers live chain health, epoch, recent performance, validators, and supply.
- CoinGecko and DeFiLlama provide economic context outside the validator/runtime layer.
- Thresholds are intentionally simple and visible so reviewers can tune them without reverse-engineering the pipeline.

## Source URLs

- solana_rpc: https://api.mainnet-beta.solana.com
- coingecko_price: https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true
- defillama_sol_price_fallback: https://coins.llama.fi/prices/current/coingecko:solana
- defillama_chains: https://api.llama.fi/v2/chains

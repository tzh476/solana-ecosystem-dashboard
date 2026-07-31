# Solana Ecosystem Auto-Updating Report

Generated: `2026-07-31T16:05:17+00:00`

## Executive Summary

This report combines live network, validator, market, and TVL signals into a repeatable snapshot. The dashboard can be regenerated with one command and emits the same data as JSON for downstream automation.

## Metrics

| Metric | Value |
| --- | ---: |
| Network health | ok |
| Epoch | 1010 |
| Epoch progress | 15.63% |
| Absolute slot | 436.39M |
| Block height | 414.44M |
| Transactions processed | 533.96B |
| Latest TPS | 4.03K |
| Average TPS, last 24 samples | 3.65K |
| Average slot time, last 24 samples | 423 ms |
| Active validators | 692 |
| Delinquent validators | 12 |
| Delinquent validator ratio | 1.70% |
| Top 10 validator stake share | 24.47% |
| SOL price | $73.05 |
| SOL 24h change | n/a |
| Solana TVL | $4.75B |

## Anomaly Flags

- **info / data_fetch**: One or more data sources returned errors.

## Automation Notes

- The same script refreshes JSON, Markdown, and HTML outputs.
- Solana RPC data covers live chain health, epoch, recent performance, validators, and supply.
- CoinGecko and DeFiLlama provide economic context outside the validator/runtime layer.
- Thresholds are intentionally simple and visible so reviewers can tune them without reverse-engineering the pipeline.

## Source URLs

- solana_rpc: https://solana-rpc.publicnode.com
- coingecko_price: https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true
- defillama_sol_price_fallback: https://coins.llama.fi/prices/current/coingecko:solana
- defillama_chains: https://api.llama.fi/v2/chains

## Fetch Errors

- getSupply: TimeoutError: The read operation timed out
- CoinGecko SOL price: URLError: <urlopen error timed out>

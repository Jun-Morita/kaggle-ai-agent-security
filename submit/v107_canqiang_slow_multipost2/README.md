# v107_canqiang_slow_multipost2

High-risk / high-return slow-row density test.

- Source: `submit/v102_canqiang_ea_b_exact`
- Change: `SLOW_MULTIPOST_N=1 -> 2`
- Strategy: keep the proven live validation-fill / replay-safe sizing baseline, but ask the latency-classified slow Harmony row to execute two forged `http.post` endpoints per candidate.
- Risk: replay cost may rise enough to blank/timeout. Upside exists only if the slow row reliably records more than one scored exfil event per returned candidate.

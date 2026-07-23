# v105_canqiang_ea_b_safe975

Small replay-safe margin push from the current best v102 canqiang EA-B transfer.

- Source: `canqiang/aiagsec-ea-b-0721`
- Public source score: `88.560`
- Previous repo result: `v102 = 87.435`
- Attack SHA-256 prefix: `67af80e2c31e`
- Strategy: keep the v102 live validation-fill and latency split, changing only `REPLAY_SAFE_FRAC` from `0.97` to `0.975`.
- Rationale: Silver boundary was `87.705` on 2026-07-23, so only a few additional successful single-post candidates are needed.
- Submission note: slightly higher timeout risk than v104, but much lower risk than the failed broad rewrites.
- Submission ref: `54928618` (pending as of 2026-07-23 22:13 JST)

# exp127_v123_rsf978_recheck

## Hypothesis

`v122` proved that the `v123` single-post Harmony-frame family can complete at
`REPLAY_SAFE_FRAC=0.978` and score `91.170`. Rechecking that known-safe boundary
samples hosted replay variance while retaining the replay envelope and all
high-value mechanics from the active `v123` baseline.

## Base and Change

- Base: `submit/v123_v121_exact_rerun`
- Only change: `REPLAY_SAFE_FRAC=0.975 -> 0.978`
- Preserve the payload, candidate construction, `FRAME_TEMPLATE`,
  `SPLIT_CLASSIFY_N=6`, `PROBE_HOPS=0`, and `SLOW_MULTIPOST_N=1`.

## Validation

- `python3 -m py_compile`: passed.
- SDK `validate redteam`: passed.
- Deterministic 60-second smoke: completed; expected score `0.00`.
- Notebook JSON is valid and emits the identical `attack.py`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v127-rsf978-recheck` version 1.
- Competition submission ref: `55182814`.
- Status: pending Kaggle evaluation as of 2026-08-02.
- Attack SHA-256: `3d5bc0fced00` (identical to scored `v122`).

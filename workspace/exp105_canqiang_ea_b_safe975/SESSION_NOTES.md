# v105_canqiang_ea_b_safe975

## Hypothesis

The current best v102 score is only `0.270` below the observed Top 5% boundary. A small replay-safe fraction increase may add enough successful single-post candidates to cross that line while preserving most of v102's timeout safety.

## Source

- `submit/v102_canqiang_ea_b_exact`
- `canqiang/aiagsec-ea-b-0721`
- Public source score: `88.560`
- Repo result before this run: `v102 = 87.435`

## Implementation

- Submit directory: `submit/v105_canqiang_ea_b_safe975`
- Kernel: `junichiromorita/ai-agent-security-v105-canqiang-eab-safe975`
- Attack SHA-256 prefix: `67af80e2c31e`
- Only attack change: `REPLAY_SAFE_FRAC = 0.97` -> `0.975`.

## Validation

- `py_compile`: passed.
- Notebook JSON preflight: writes `attack.py`, writes `submission.csv`, calls `JEDAttackInferenceServer`.
- SDK `validate redteam`: passed.
- Hosted output check: `attack.py` and `submission.csv` present.
- Deterministic smoke: not run, to avoid spending time in the long live-fill loop.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v105-canqiang-eab-safe975` version 1.
- Competition submission ref: `54928618`.
- Status as of 2026-07-23 22:13 JST: pending.

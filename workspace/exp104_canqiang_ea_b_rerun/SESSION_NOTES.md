# v104_canqiang_ea_b_rerun

## Hypothesis

The Silver boundary is within normal hosted variance of the proven canqiang EA-B profile. Re-running the exact v102 code can recover the public source upper tail without increasing timeout risk.

## Source

- `submit/v102_canqiang_ea_b_exact`
- `canqiang/aiagsec-ea-b-0721`
- Public source score: `88.560`
- Repo result before this run: `v102 = 87.435`

## Implementation

- Submit directory: `submit/v104_canqiang_ea_b_rerun`
- Kernel: `junichiromorita/ai-agent-security-v104-canqiang-eab-rerun`
- Attack SHA-256 prefix: `3867ef52aa19`
- No attack-code changes from v102.

## Validation

- `py_compile`: passed.
- Notebook JSON preflight: writes `attack.py`, writes `submission.csv`, calls `JEDAttackInferenceServer`.
- SDK `validate redteam`: passed.
- Hosted output check: `attack.py` and `submission.csv` present.
- Deterministic smoke: not run, to avoid spending time in the long live-fill loop.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v104-canqiang-eab-rerun` version 1.
- Competition submission ref: `54928588`.
- Status as of 2026-07-23 22:11 JST: pending.

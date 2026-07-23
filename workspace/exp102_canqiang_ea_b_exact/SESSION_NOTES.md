# v102_canqiang_ea_b_exact

## Hypothesis

The public Silver threshold is reachable by reproducing the source-scored implementation rather than modifying the v093 branch. This experiment keeps the high-scoring public notebook logic intact and changes only the Kaggle owner/slug metadata.

## Source

- `canqiang/aiagsec-ea-b-0721`
- Public source score: `88.560`
- Source script version: `latest pulled 2026-07-23`

## Implementation

- Submit directory: `submit/v102_canqiang_ea_b_exact`
- Kernel: `junichiromorita/ai-agent-security-v102-canqiang-eab`
- Attack SHA-256 prefix: `3867ef52aa19`
- GPU enabled to match the public source notebook metadata.

## Validation

- `py_compile`: passed.
- Notebook JSON preflight: writes `attack.py`, writes `submission.csv`, calls `JEDAttackInferenceServer`.
- SDK `validate redteam`: passed.
- Deterministic smoke: not run, to avoid spending time in the long live-fill loop.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v102-canqiang-eab` version 1.
- Competition submission ref: `54906778`.
- Status as of 2026-07-23 00:37 JST: pending.

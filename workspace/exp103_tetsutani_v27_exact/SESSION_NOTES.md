# v103_tetsutani_v27_exact

## Hypothesis

The public Silver threshold is reachable by reproducing the source-scored implementation rather than modifying the v093 branch. This experiment keeps the high-scoring public notebook logic intact and changes only the Kaggle owner/slug metadata.

## Source

- `tetsutani/ai-agent-sec-adaptive-uniform-three-probe-race version 27`
- Public source score: `88.515`
- Source script version: `336810494`

## Implementation

- Submit directory: `submit/v103_tetsutani_v27_exact`
- Kernel: `junichiromorita/ai-agent-security-v103-tetsutani-v27`
- Attack SHA-256 prefix: `4b22bc66dade`
- GPU enabled to match the public source notebook metadata.

## Validation

- `py_compile`: passed.
- Notebook JSON preflight: writes `attack.py`, writes `submission.csv`, calls `JEDAttackInferenceServer`.
- SDK `validate redteam`: passed.
- Deterministic smoke: not run, to avoid spending time in the long live-fill loop.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v103-tetsutani-v27` version 1.
- Competition submission ref: `54906782`.
- Status as of 2026-07-23 00:37 JST: pending.

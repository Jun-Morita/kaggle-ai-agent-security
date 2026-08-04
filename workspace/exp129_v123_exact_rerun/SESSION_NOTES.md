# exp129_v123_exact_rerun

## Hypothesis

`v123` is the current public best at `91.890`, while byte-identical reruns have
shown large hosted variance. Another exact rerun is the lowest-risk way to sample
the upper tail and defend the public Silver position.

## Base and Change

- Base: `submit/v123_v121_exact_rerun`
- Change: none. This is an exact rerun under a new Kaggle kernel slug.

## Validation

- `python3 -m py_compile`: passed.
- Notebook JSON is valid and emits the identical `attack.py`.
- SDK `validate redteam`: passed.
- Deterministic 60-second smoke: completed; expected score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v129-v123-rerun` version 1.
- Competition submission ref: `55211416`.
- Status: complete.
- Public LB: `85.770` as of 2026-08-05.
- Result: large hosted down-draw from the byte-identical `v123=91.890`; do not
  promote.
- Attack SHA-256: `00fcdb1a2916`.

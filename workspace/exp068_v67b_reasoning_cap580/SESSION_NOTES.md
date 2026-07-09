# exp068 V67b Reasoning Cap580

## Hypothesis

`v067` was a close transfer of the public v67b reasoning-suppression preset but
completed with a blank public score. Since the notebook actively verifies and
keeps collecting until the deadline, the reasoning-suppression prompt may have
allowed too many candidates to be returned, causing replay-side no-score.

This variant keeps the v67b prompt and active verifier but caps returned
candidates at `580`, near the current high-scoring single-hop equivalent range.

## Implementation

- Submission directory: `submit/v068_v67b_reasoning_cap580/`
- Notebook source:
  `submit/v068_v67b_reasoning_cap580/ai-agent-security-v67b-cap580.ipynb`
- Changes from `v067`:
  - `while len(cands) < 2000:` -> `while len(cands) < 580:`
  - `return cands[:2000]` -> `return cands[:580]`

## Validation

- Notebook structure check passed.
- Extracted `attack.py` compiled successfully.
- SDK validate passed on extracted `attack.py`.
- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v068-v67b-reasoning-cap580` version 1.
- Hosted output contains `attack.py` and `submission.csv`.

## Result

- Submitted as ref `54426167`; complete with blank public score as of 2026-07-08.
- Notebook hash: `659e0f013bf0`.
- Hosted `attack.py` hash: `3a71dc4eea10`.

Treat this as no-score / `Submission Format Error` class. The simple hard cap of
`580` did not fix the v67b reasoning-suppression transfer, so the issue is not
only uncontrolled candidate count.

# exp069 V67b Unconditional Serve

## Hypothesis

`v067` and `v068` were close transfers of the public v67b reasoning-suppression
preset but completed with blank public scores. `v068` capped returned candidates
at `580`, so the failure is not explained by candidate count alone.

The successful `v063` notebook calls `JEDAttackInferenceServer().serve()`
unconditionally, while `v067` and `v068` only call it when
`KAGGLE_IS_COMPETITION_RERUN` is set. This variant keeps the `v068` attack logic
and cap, but restores unconditional `serve()` to test the submission-entry
hypothesis.

## Implementation

- Submission directory: `submit/v069_v67b_unconditional_serve/`
- Notebook source:
  `submit/v069_v67b_unconditional_serve/ai-agent-security-v67b-cap580.ipynb`
- Changes from `v068`:
  - remove the `KAGGLE_IS_COMPETITION_RERUN` conditional around
    `JEDAttackInferenceServer().serve()`
  - keep `while len(cands) < 580`
  - keep `return cands[:580]`

## Validation

- Notebook JSON check passed.
- Generated `attack.py` compiled during notebook build-cell execution.
- SDK validate passed on generated `attack.py`.
- Deterministic smoke completed in about `42.2s` with score `0.00`.
- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v069-v67b-unconditional-serve` version 1.
- Hosted output contains `attack.py` and `submission.csv`.
- Hosted `attack.py` hash is `3a71dc4eea10`, matching `v068`.

## Result

- Submitted as ref `54440860`; complete with blank public score as of 2026-07-08.
- Notebook hash: `d930a3747eb7`.
- Hosted `attack.py` hash: `3a71dc4eea10`.

Treat as no-score / `Submission Format Error` class. This result rejects the
simple entrypoint-only explanation: unconditional `serve()` did not rescue the
v67b reasoning-suppression transfer.

# exp177_replay_costcoef0975

## Hypothesis

`v169` improved the post-refresh best by setting `REPLAY_COST_COEF=0.95`, but
`v172` and `v174` showed that the `Say OK.` branch collapses when combined with
replay-cost optimism. This variant returns to the proven `Then say OK.` anchor
and tests a safer midpoint, `REPLAY_COST_COEF=0.975`, to reduce underfill without
crossing as far into replay-risk territory as `0.95` / `0.925`.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Confirmed base public score: `89.685`

## Change

- Keep `Then say OK.` plain/frame templates.
- Keep `REPLAY_SAFE_FRAC=0.985`.
- Change only:
  - `REPLAY_COST_COEF=0.95`
  - to `REPLAY_COST_COEF=0.975`

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v177_replay_costcoef0975/attack.py`: passed.
- `python3 -m json.tool submit/v177_replay_costcoef0975/kernel-metadata.json`: passed.
- Notebook first-cell parity with `attack.py`: passed.
- SDK validate: passed.
- Attack SHA-256: `c0ad53ba4863`
- Hosted output check: `submission.csv` downloaded from kernel version 1, but
  `attack.py` was missing.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v177-replay-costcoef0975`
- Version: 1
- Competition submission ref: `55771451`
- Status: complete with blank public score as of 2026-08-25.

## Failure Analysis

This was an output-defect no-score, so the `REPLAY_COST_COEF=0.975` attack idea
was not actually evaluated. The notebook first cell lost the
`%%writefile /kaggle/working/attack.py` wrapper during local notebook/attack
sync, so the hosted kernel emitted `submission.csv` but did not emit the required
`attack.py`.

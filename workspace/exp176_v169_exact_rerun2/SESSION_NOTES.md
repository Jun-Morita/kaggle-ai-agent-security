# exp176_v169_exact_rerun2

## Hypothesis

`v169_replay_costcoef095` remains the current confirmed post-refresh best at
public `89.685`. The 2026-08-25 top-10% boundary is `89.910`, so an additional
exact rerun is a reasonable low-risk variance sample while more experimental
variants are pending.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Confirmed base public score: `89.685`

## Change

- Exact rerun of `v169`.
- Only the Kaggle kernel id/title changed.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v176_v169_exact_rerun2/attack.py`: passed.
- `python3 -m json.tool submit/v176_v169_exact_rerun2/kernel-metadata.json`: passed.
- Notebook first-cell parity with `attack.py`: passed.
- `sha256sum` confirmed `attack.py` is byte-identical to `v169`.
- SDK validate: passed.
- Hosted output check: `submission.csv` downloaded from kernel version 1, but
  `attack.py` was missing.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v176-v169-exact-rerun2`
- Version: 1
- Competition submission ref: `55771449`
- Status: complete with blank public score as of 2026-08-25.

## Failure Analysis

This was an output-defect no-score, not a valid `v169` variance readout. The
notebook first cell lost the `%%writefile /kaggle/working/attack.py` wrapper
during local notebook/attack sync, so the hosted kernel emitted
`submission.csv` but did not emit the required `attack.py`.

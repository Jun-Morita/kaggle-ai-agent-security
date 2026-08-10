# exp133_v123_exact_rerun

## Hypothesis

Re-submit the v123 exact attack body to sample hosted evaluation variance and keep a high-public-score candidate for the final selection pool.

## Changes

- Copied `submit/v123_v121_exact_rerun`.
- Changed only Kaggle kernel metadata to `ai-agent-security-v133-v123-rerun`.
- Kept `attack.py` unchanged from v123.

## Validation

- `python3 -m py_compile submit/v133_v123_exact_rerun/attack.py`
- Notebook writefile cell matches `attack.py`.
- `aicomp_sdk.cli.main validate redteam submit/v133_v123_exact_rerun/attack.py` passed.

## Submission

- Prepared locally.
- Codex-side Kaggle submission command was blocked by approval review after user approval, so manual execution is required.

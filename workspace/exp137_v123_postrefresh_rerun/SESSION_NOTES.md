# exp137_v123_postrefresh_rerun

## Hypothesis

`v135=56.340` showed that simple static breadth is not enough after the 2026-08-05 evaluator refresh. Re-submit the byte-identical `v123` live validation-fill attack to get a clean post-refresh baseline for the old best family.

## Changes

- Copied `submit/v123_v121_exact_rerun`.
- Changed only Kaggle kernel metadata to `ai-agent-security-v137-v123-postrefresh`.
- Kept `attack.py` byte-identical to `v123`; SHA-256 prefix `00fcdb1a2916`.

## Validation

- `python3 -m py_compile submit/v137_v123_postrefresh_rerun/attack.py` passed.
- Notebook writefile cell matches `attack.py`.
- `aicomp_sdk.cli.main validate redteam submit/v137_v123_postrefresh_rerun/attack.py` passed.

## Submission

- Submitted on 2026-08-11.
- Kernel: `junichiromorita/ai-agent-security-v137-v123-postrefresh` version 1.
- Submission ref: `55418639`.
- Status after submission: `PENDING`.

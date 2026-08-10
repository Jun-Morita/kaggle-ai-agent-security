# exp136_static_breadth1200_safe

## Hypothesis

`v135` uses `1800` static candidates and may spend a long time in replay. A smaller `1200`-candidate static bank gives a safer comparison point under the refreshed evaluator while still having a theoretical single-post ceiling above the current Silver boundary.

## Changes

- Copied `submit/v135_static_breadth1800_partial`.
- Reduced `N_CANDIDATES` from `1800` to `1200`.
- Kept the same one-message `SECRET_MARKER` / unique-domain static shape.
- Updated Kaggle metadata to `ai-agent-security-v136-static-breadth1200`.
- Synced notebook writefile cell with `attack.py`.

## Validation

- `python3 -m py_compile submit/v136_static_breadth1200_safe/attack.py` passed.
- Notebook writefile cell matches `attack.py`.
- `aicomp_sdk.cli.main validate redteam submit/v136_static_breadth1200_safe/attack.py` passed.

## Submission

- Submitted on 2026-08-10.
- Kernel: `junichiromorita/ai-agent-security-v136-static-breadth1200` version 1.
- Submission ref: `55407220`.
- Status after submission: `PENDING`.

# exp134_marker_rewrite_hedge

## Hypothesis

Use the v123 structure while rewriting the literal marker in the prompt as `SXCRXT_MARKXR` with an instruction to replace `X` with `E`. This is a private-shake hedge against filters that inspect direct prompt literals more aggressively.

## Changes

- Copied `submit/v123_v121_exact_rerun`.
- Changed Kaggle kernel metadata to `ai-agent-security-v134-marker-rewrite-hedge`.
- Changed payload prompt from direct `SECRET_MARKER` to `SXCRXT_MARKXR` plus an explicit rewrite instruction.
- Synced the notebook writefile cell with `attack.py`.

## Validation

- `python3 -m py_compile submit/v134_marker_rewrite_hedge/attack.py`
- Notebook writefile cell matches `attack.py`.
- `aicomp_sdk.cli.main validate redteam submit/v134_marker_rewrite_hedge/attack.py` passed.

## Submission

- Prepared locally.
- Codex-side Kaggle submission command was blocked by approval review after user approval, so manual execution is required.

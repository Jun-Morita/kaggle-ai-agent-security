# exp161_v148_exact_rerun

Date: 2026-08-21

## Hypothesis

The current best family has material hosted variance. A byte-equivalent rerun of
`v148=88.245` may catch a better draw without changing the proven primitive.

## Source

- Base: `submit/v148_replaysafe_postrefresh_push`
- Output candidate: `submit/v161_v148_exact_rerun`

## Change

- No `attack.py` behavioral change versus `v148`.
- New Kaggle kernel slug only.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v161_v148_exact_rerun/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v161_v148_exact_rerun/attack.py`

## Submission

- Submitted 2026-08-21.
- Kernel: `junichiromorita/ai-agent-security-v161-v148-exact-rerun` v1
- Submission ref: `55669672`
- Result: complete, public `80.370` as of 2026-08-22
- Readout: byte-equivalent rerun landed far below `v148=88.245`; rerun-only is
  not a reliable Silver path.

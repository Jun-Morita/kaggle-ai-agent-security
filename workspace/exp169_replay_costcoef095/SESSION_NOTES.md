# exp169_replay_costcoef095

Date: 2026-08-23

## Hypothesis

Terminal compactness variants (`v166`-`v168`) explore one narrow axis. This
high-risk / high-return branch instead pushes replay sizing. `v163=88.920` may
be leaving a few successful candidates on the table if the replay cost estimate
is conservative. Reducing `REPLAY_COST_COEF` from `1.0` to `0.95` lets the live
fill keep more candidates while preserving the proven `v163` prompt wording.

## Source

- Base: `submit/v163_fastfirst_terminal_short`
- Output candidate: `submit/v169_replay_costcoef095`

## Change

- Keep `TEMPLATE`, `FRAME_TEMPLATE`, fastest-first ordering, and
  `REPLAY_SAFE_FRAC=0.985`.
- Change only:
  - `REPLAY_COST_COEF=1.0`
  - to `REPLAY_COST_COEF=0.95`

## Risk

- If hosted replay is already at the true boundary, this can over-return and
  lose score through timeout / replay truncation.
- If the current coefficient is conservative, this can add enough successful
  single-post findings to close part of the medal gap.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v169_replay_costcoef095/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v169_replay_costcoef095/attack.py`
- Attack SHA-256: `40dc80e8bdcd`

## Submission

- Submitted 2026-08-23.
- Kaggle kernel: `junichiromorita/ai-agent-security-v169-replay-costcoef095` v1
- Competition submission ref: `55702321`
- Status: pending as of 2026-08-23 09:35 JST

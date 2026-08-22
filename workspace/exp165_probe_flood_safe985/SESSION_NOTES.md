# exp165_probe_flood_safe985

Date: 2026-08-22

## Hypothesis

The public `probe-and-flood-strategy` uses `REPLAY_SAFE_FRAC=0.99`, but this repo
has strong negative evidence against pushing that knob (`v150=76.815` and
`v162=78.795`). A safety pair at `0.985` may keep the probe-and-flood template
structure while avoiding the replay-safe overshoot.

## Source

- Base: `submit/v164_probe_flood_exact`
- Output candidate: `submit/v165_probe_flood_safe985`

## Change

- Single knob:
  - `REPLAY_SAFE_FRAC=0.99`
  - to `REPLAY_SAFE_FRAC=0.985`

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v165_probe_flood_safe985/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v165_probe_flood_safe985/attack.py`

## Submission

- Submitted 2026-08-22.
- Kaggle kernel: `junichiromorita/ai-agent-security-v165-probe-flood-safe985` v1
- Competition submission ref: `55684828`
- Status: pending as of 2026-08-22 15:23 JST

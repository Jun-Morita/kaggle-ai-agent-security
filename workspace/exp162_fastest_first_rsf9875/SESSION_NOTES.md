# exp162_fastest_first_rsf9875

Date: 2026-08-21

## Hypothesis

`v150` showed `REPLAY_SAFE_FRAC=0.99` is too aggressive, while `v148=0.985`
remains the best confirmed value. Combining `v159`'s fastest-first ordering with
a midpoint `REPLAY_SAFE_FRAC=0.9875` may gain a few extra successful candidates
while preserving enough prefix quality under partial replay scoring.

## Source

- Base: `submit/v159_fastest_first_rsf985`
- Output candidate: `submit/v162_fastest_first_rsf9875`

## Change

- Preserve fastest-first ordering from `v159`.
- Change `REPLAY_SAFE_FRAC=0.985 -> 0.9875`.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v162_fastest_first_rsf9875/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v162_fastest_first_rsf9875/attack.py`

## Submission

- Submitted 2026-08-21.
- Kernel: `junichiromorita/ai-agent-security-v162-fastfirst-rsf9875` v1
- Submission ref: `55669708`
- Result: complete, public `78.795` as of 2026-08-22
- Readout: midpoint `REPLAY_SAFE_FRAC=0.9875` regressed badly; do not push
  beyond `0.985` in this family.

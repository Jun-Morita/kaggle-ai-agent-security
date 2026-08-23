# exp166_terminal_say_ok_direct

Date: 2026-08-22

## Hypothesis

`v163_fastfirst_terminal_short=88.920` improved over `v159=87.570` by changing
only the terminal phrase from `Then answer OK only.` to `Then say OK.`. A further
minimal contraction to `Say OK.` may improve replay throughput without repeating
the failed full terminal removal pattern from older branches.

## Source

- Base: `submit/v163_fastfirst_terminal_short`
- Output candidate: `submit/v166_terminal_say_ok_direct`

## Change

- Keep fastest-first ordering and `REPLAY_SAFE_FRAC=0.985`.
- Change terminal wording only:
  - `Then say OK.`
  - to `Say OK.`
- Apply the same terminal change to `FRAME_TEMPLATE`.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v166_terminal_say_ok_direct/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v166_terminal_say_ok_direct/attack.py`
- Attack SHA-256: `e399e259048b`

## Submission

- Submitted 2026-08-22.
- Kaggle kernel: `junichiromorita/ai-agent-security-v166-terminal-say-ok` v1
- Competition submission ref: `55693088`
- Status: pending as of 2026-08-22 23:31 JST

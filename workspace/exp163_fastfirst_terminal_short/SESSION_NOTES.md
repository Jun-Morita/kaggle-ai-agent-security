# exp163_fastfirst_terminal_short

Date: 2026-08-22

## Hypothesis

Discussion on 2026-08-21 raised prompt-language / compactness as a replay
throughput lever. A low-risk way to test this without repeating the failed
full-frame-shortening pattern from `v146` is to keep `v159` intact and shorten
only the terminal answer instruction.

## Source

- Base: `submit/v159_fastest_first_rsf985`
- Output candidate: `submit/v163_fastfirst_terminal_short`

## Change

- Keep fastest-first ordering and `REPLAY_SAFE_FRAC=0.985`.
- Change terminal wording only:
  - `Then answer OK only.`
  - to `Then say OK.`
- Apply the same terminal change to `FRAME_TEMPLATE`.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v163_fastfirst_terminal_short/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v163_fastfirst_terminal_short/attack.py`

## Submission

- Submitted 2026-08-22.
- Kernel: `junichiromorita/ai-agent-security-v163-fastfirst-terminal-short` v1
- Submission ref: `55679512`
- Status: complete as of 2026-08-22
- Public LB: `88.920`

## Readout

- New confirmed post-refresh best, improving over `v148=88.245` by `+0.675`.
- Compact terminal wording is a real positive lever.
- The result is still below the 2026-08-22 public top-10% boundary `89.550` by
  `0.630` and below the top-5% boundary `91.710` by `2.790`.

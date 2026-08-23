# exp168_terminal_ok_only

Date: 2026-08-23

## Hypothesis

`v163_fastfirst_terminal_short=88.920` showed that shorter terminal wording can
improve replay throughput. `OK.` is the aggressive version: it minimizes the
terminal suffix while retaining an explicit answer token.

## Source

- Base: `submit/v163_fastfirst_terminal_short`
- Output candidate: `submit/v168_terminal_ok_only`

## Change

- Keep fastest-first ordering and `REPLAY_SAFE_FRAC=0.985`.
- Change terminal wording only:
  - `Then say OK.`
  - to `OK.`
- Apply the same terminal change to `FRAME_TEMPLATE`.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v168_terminal_ok_only/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v168_terminal_ok_only/attack.py`
- Attack SHA-256: `728bdd348cf1`

## Submission

- Submitted 2026-08-23.
- Kaggle kernel: `junichiromorita/ai-agent-security-v168-terminal-ok-only` v1
- Competition submission ref: `55701939`
- Status: pending as of 2026-08-23 09:13 JST

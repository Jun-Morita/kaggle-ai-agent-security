# exp171_sayok_router

## Hypothesis

`v166_terminal_say_ok_direct` completed with public `89.235`, improving over
`v163=88.920`. The `Say OK.` terminal contraction is therefore a confirmed
positive lever. This experiment keeps the `v163`/`v166` scoring primitive and
uses a lighter adaptive router centered on `Say OK.`.

## Base

- Base implementation: `submit/v170_adaptive_terminal_router`
- Confirmed static anchor: `v166_terminal_say_ok_direct=89.235`
- Current top-10% boundary on 2026-08-23: `89.640`
- Current public top-5% / Silver proxy: `91.800`

## Change

- Keep live validation-fill, fastest-first ordering, `REPLAY_SAFE_FRAC=0.985`,
  `REPLAY_COST_COEF=1.0`, and single-hop `http.post` with `SECRET_MARKER`.
- Route among four terminal templates using the existing six classification
  probes:
  - plain `Say OK.`
  - Harmony-frame `Say OK.`
  - plain `Then say OK.`
  - Harmony-frame `Then say OK.`
- Selection rule is unchanged from `v170`: maximize live fired count, then break
  ties by lower elapsed time per fired candidate.

## Risk

- The six-probe router can still be noisy.
- If static `v167` or `v168` later outperforms `v166`, this arm set may be too
  conservative.
- This submission does not change replay-cost sizing; `v169` remains the separate
  sizing probe.

## Validation

- `python3 -m py_compile submit/v171_sayok_router/attack.py`: passed.
- `python3 -m json.tool submit/v171_sayok_router/kernel-metadata.json`: passed.
- Notebook first-cell parity with `attack.py`: passed.
- SDK validate:
  `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v171_sayok_router/attack.py`
  passed.
- SDK deterministic smoke:
  `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main test redteam submit/v171_sayok_router/attack.py --budget-s 60 --agent deterministic`
  completed in 76.4s with 0 findings, as expected for this deterministic local
  agent.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v171-sayok-router` v1.
- Competition submission ref: `55715068`.
- Status at submission time: pending.
- Remaining daily submissions after submit: `1`.

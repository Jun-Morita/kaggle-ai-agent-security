# exp159_fastest_first_rsf985

Date: 2026-08-21

## Hypothesis

The post-refresh public best `v148=88.245` may be losing value when replay only
scores an early slice of the returned candidate list. If live elapsed time is a
reasonable proxy for replay cost, returning the fired candidates fastest-first
should increase the score accumulated before any replay-side budget cutoff.

## Source

- Base: `submit/v148_replaysafe_postrefresh_push`
- Output candidate: `submit/v159_fastest_first_rsf985`

## Change

- Preserve `v148`'s live validation-fill, template race, `REPLAY_SAFE_FRAC=0.985`,
  payload, and guardrail assumptions.
- Store fired candidates as `(elapsed, idx, AttackCandidate)`.
- Sort returned candidates by `(elapsed, idx)` before returning from `run()`.

## Rationale

Kaggle discussion on 2026-08-21 suggests that very large returned sets may only
have the first roughly `200-250` candidates effectively scored. The best current
family is already a single-post throughput strategy, so returned-candidate order
is a cheap, local optimization surface.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v159_fastest_first_rsf985/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v159_fastest_first_rsf985/attack.py`

## Submission

- Submitted 2026-08-21.
- Kernel: `junichiromorita/ai-agent-security-v159-fastest-first-rsf985` v1
- Submission ref: `55669483`
- Result: complete, public `87.570` as of 2026-08-22
- Readout: fastest-first ordering did not improve over `v148=88.245`; live
  elapsed sorting is not a reliable replay-value proxy.

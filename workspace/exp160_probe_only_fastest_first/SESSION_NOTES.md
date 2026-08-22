# exp160_probe_only_fastest_first

Date: 2026-08-21

## Hypothesis

The `v148` classifier probes may create early replay candidates that are not the
best use of a partially-scored candidate prefix. Treating classification as
probe-only, then returning only post-classification fired candidates fastest-first,
may improve the leading scored slice even if it sacrifices up to the first six
successful probe candidates.

## Source

- Base: `submit/v148_replaysafe_postrefresh_push`
- Output candidate: `submit/v160_probe_only_fastest_first`

## Change

- Preserve `v148`'s template race and `REPLAY_SAFE_FRAC=0.985`.
- Do not append fired candidates while `classifying` is true.
- Store post-classification fired candidates as `(elapsed, idx, AttackCandidate)`.
- Sort returned candidates by `(elapsed, idx)`.

## Rationale

This is a higher-risk companion to `v159`. It tests whether the leaderboard is
more sensitive to candidate prefix quality than to retaining every live-fired
candidate. If `v160` beats `v159`, future variants should spend a small probe
budget but keep the replay list as homogeneous and low-latency as possible.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v160_probe_only_fastest_first/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v160_probe_only_fastest_first/attack.py`

## Submission

- Submitted 2026-08-21.
- Kernel: `junichiromorita/ai-agent-security-v160-probe-only-fastfirst` v1
- Submission ref: `55669526`
- Result: complete, public `87.885` as of 2026-08-22
- Readout: probe-only fastest-first stayed below `v148=88.245`; classification
  probes are not the binding issue.

# exp175_v169_exact_rerun

## Hypothesis

`v169_replay_costcoef095` is the current confirmed post-refresh best at public
`89.685`, while the 2026-08-25 top-10% boundary is `89.910`. Hosted variance is
large enough that an exact rerun can plausibly recover the small `+0.225` gap
without taking on new mechanism risk.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Confirmed base public score: `89.685`

## Change

- Exact rerun of `v169`.
- Only the Kaggle kernel id/title changed.
- `attack.py` and notebook attack cell are intended to remain identical to
  `v169`.

## Risk

- Same-code reruns can underperform substantially under hosted variance.
- This does not target the larger public Silver/top-5% gap directly; it is a
  top-10 recovery / stable-best sampling attempt.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v175_v169_exact_rerun/attack.py`: passed.
- `python3 -m json.tool submit/v175_v169_exact_rerun/kernel-metadata.json`: passed.
- `sha256sum` confirmed `attack.py` and notebook are byte-identical to `v169`.
- SDK validate: passed.
- Hosted output check: `attack.py` and `submission.csv` downloaded from kernel
  version 1.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v175-v169-exact-rerun`
- Version: 1
- Competition submission ref: `55769525`
- Status: complete as of 2026-08-26.
- Public score: `73.620`

## Result

The exact rerun landed far below `v169=89.685`. Treat this as hosted
variance/timing evidence against relying on rerun-only submissions for the
public top-10% / Silver gap.

# exp164_probe_flood_exact

Date: 2026-08-22

## Hypothesis

The newly updated public notebook `adhirajjagtap/probe-and-flood-strategy` reports
public `88.695`, slightly above the repo best `v148=88.245`. A near-exact
transfer may recover that small improvement and provide a fresh baseline for the
post-`v159` negative results.

## Source

- Public Code: `adhirajjagtap/probe-and-flood-strategy`
- Cached notebook:
  `data/notebooks/ai-agent-security-multi-step-tool-attacks/adhirajjagtap_probe-and-flood-strategy/probe-and-flood-strategy.ipynb`
- Output candidate: `submit/v164_probe_flood_exact`

## Change

- Extracted the notebook's `attack.py`.
- Preserved the attack logic.
- Changed the notebook write target from relative `attack.py` to
  `/kaggle/working/attack.py` for consistency with this repo's submission
  wrapper.

## Validation

- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v164_probe_flood_exact/attack.py`
- Notebook cell 0 matches `attack.py`.
- `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v164_probe_flood_exact/attack.py`

## Submission

- Submitted 2026-08-22.
- Kaggle kernel: `junichiromorita/ai-agent-security-v164-probe-flood-exact` v1
- Competition submission ref: `55684830`
- Status: pending as of 2026-08-22 15:23 JST

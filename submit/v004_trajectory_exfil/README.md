# v004 Trajectory Exfil

High-score attempt based on the public `17-1-eda-agent-security-trajectory-search` notebook, ported into this repository's stable script-kernel wrapper.

This version focuses on the strongest observed public approach:

- exfil calibration across payload, prompt wording, and endpoint count;
- domain-diverse callback hosts, because score cells vary by host more than URL path;
- payload bank: `TOKEN=admin123`, `SECRET_API_KEY=sk_live_test`, `PASSWORD=test123`, `SECRET_MARKER`;
- bounded fill up to `180` returned candidates when the active model verifies at least one finding;
- roughly 80% exfil fill and 20% confused-deputy fill in static/fallback behavior;
- tiny source-action lottery only, avoiding broad public-guardrail-blocked destructive sweeps.

The submission wiring is the same as `v001-v003`: `attack.py` writes `/kaggle/working/attack.py`, writes placeholder `/kaggle/working/submission.csv`, disables GPU, and serves the competition inference gateway.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v004_trajectory_exfil/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v004_trajectory_exfil/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v004_trajectory_exfil

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v004-trajectory-exfil \
  -v <version> \
  -f submission.csv \
  -m "v004 trajectory exfil"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v004-trajectory-exfil`
- Version: `1`
- Submission ref: `53637051`
- Status: `PENDING` after repeated CLI checks on 2026-06-13
- Public score: pending
- Local deterministic smoke score: `0.00`

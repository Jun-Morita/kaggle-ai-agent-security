# v007 Fast Aggressive Fill

Fast aggressive-fill variant based on `v006_trajectory_exfil_multipost` and the public `AI Agent 25.205` notebook.

This version is a hedge while `v006` is still running. It keeps the strong public-LB lesson from `v005` and the `AI Agent` notebook: return a full set of domain-diverse exfil candidates, but avoid the heavy active-search profile.

Key settings:

- `RETURN_TARGET_CANDIDATES = 300`
- `MAX_VERIFIED_CANDIDATES = 120`
- `SEARCH_FRACTION = 0.18`
- `MAX_SEARCH_S = 360.0`
- endpoint calibration counts `(1, 2)`
- `ENDPOINTS_PER_MSG = 2`
- fill payload is naked `sk_live_test`
- static / empty fallback also fills to 300 candidates

The expected use case is not to replace `v006` if the multi-post multiplier works. It is a runtime-safer backup that should preserve much of the v005/vAI-Agent public score shape while hedging private guardrails with `sk_live_test`.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v007_fast_aggressive_fill/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v007_fast_aggressive_fill/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v007_fast_aggressive_fill

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v007-fast-aggressive-fill \
  -v <version> \
  -f submission.csv \
  -m "v007 fast aggressive fill"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v007-fast-aggressive-fill`
- Version: `1`
- Submission ref: `53660670`
- Script version: `327051929`
- Status: `Notebook Timeout`
- Public score: none
- Local deterministic smoke score: `0.00`

Interpretation:

- The 300-candidate fast-fill hedge did not finish in hosted evaluation.
- Treat this as another runtime failure for repeated-post prompt families at high returned-candidate counts, not as evidence that the underlying single-post v005 approach stopped working.

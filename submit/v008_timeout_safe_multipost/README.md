# v008 Timeout-Safe Multipost

Timeout-safe multipost variant copied from `workspace/exp007_v008_parameterized/attack.py`.

This version reacts to the `v006_trajectory_exfil_multipost` timeout. It keeps the multi-post prompt family, but reduces the returned-candidate count enough that the hosted replay should have a better chance to finish.

Key settings:

- `RETURN_TARGET_CANDIDATES = 96`
- `MAX_VERIFIED_CANDIDATES = 80`
- `STATIC_FALLBACK_CANDIDATES = 96`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 96`
- `SEARCH_FRACTION = 0.12`
- `MAX_SEARCH_S = 240.0`
- endpoint calibration counts `(2, 3)`
- `ENDPOINTS_PER_MSG = 4`
- fill payload is naked `sk_live_test`

Expected interpretation:

- if hosted models reproduce 4 posts per finding, public score can exceed v005 despite only 96 candidates;
- if hosted models average 1-2 posts per finding, this will underperform v005 but still measures timeout-safe multipost viability;
- if it times out, multipost replay cost is too high even at small candidate counts.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v008_timeout_safe_multipost/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v008_timeout_safe_multipost/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v008_timeout_safe_multipost

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v008-timeout-safe-multipost \
  -v <version> \
  -f submission.csv \
  -m "v008 timeout safe multipost"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v008-timeout-safe-multipost`
- Version: `1`
- Submission ref: `53671096`
- Script version: pending
- Status: `PENDING` as of 2026-06-14 20:14 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 11.2s
- Static `env=None` return count: `96`

# v011 Single Breadth 500

High-risk / high-reward single-hop breadth variant based on the public `Replay-Dense Exfiltration Boundary Search` notebook.

This version keeps the replay-dense single-endpoint design from `v010`, but switches from `guide16_single_600` to the more aggressive `single_breadth_500` profile.

Key settings:

- `SEARCH_PROFILE = "single_breadth_500"`
- `RETURN_TARGET_CANDIDATES = 500`
- `MIN_RETURN_CANDIDATES = 360`
- `MAX_VERIFIED_CANDIDATES = 80`
- `STATIC_FALLBACK_CANDIDATES = 500`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 120`
- `SEARCH_FRACTION = 0.12`
- `MAX_SEARCH_S = 240.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 600`

Expected interpretation:

- if it completes, public score can exceed v010 and has a theoretical single-post ceiling near `45`;
- if it times out while v010 completes, the safe boundary is closer to `400` effective single-hop findings;
- if both timeout, returned candidate count is still too high even with single-hop replay.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v011_single_breadth_500/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v011_single_breadth_500/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v011_single_breadth_500

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v011-single-breadth-500 \
  -v <version> \
  -f submission.csv \
  -m "v011 single breadth 500"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v011-single-breadth-500`
- Version: `1`
- Submission ref: `53711101`
- Script version: pending
- Status: `PENDING` as of 2026-06-15 21:49 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 13.1s
- Static `env=None` return count: `500`

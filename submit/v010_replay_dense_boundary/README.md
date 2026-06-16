# v010 Replay-Dense Boundary

Replay-hop-light exfil breadth attempt based on the public `Replay-Dense Exfiltration Boundary Search` notebook.

This version reacts to the v009 timeout. Instead of using multi-endpoint prompts or a long search phase, it returns many single-endpoint candidates with `max_tool_hops` effectively capped at `1`.

Key settings:

- `SEARCH_PROFILE = "guide16_single_600"`
- `RETURN_TARGET_CANDIDATES = 600`
- `MIN_RETURN_CANDIDATES = 400`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 300`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 400`

Expected interpretation:

- if it completes near public `36`, the runtime bottleneck was replay-hop load rather than returned candidate count alone;
- if it times out, even 400-600 single-hop candidates are too heavy and the next attempt should reduce the minimum return target;
- if it completes far below v005, the exact public notebook environment or candidate ordering is not transferring.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v010_replay_dense_boundary/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v010_replay_dense_boundary/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v010_replay_dense_boundary

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v010-replay-dense-boundary \
  -v <version> \
  -f submission.csv \
  -m "v010 replay dense boundary"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v010-replay-dense-boundary`
- Version: `1`
- Submission ref: `53710139`
- Script version: pending
- Status: `COMPLETE` as of 2026-06-16
- Public score: `36.000`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 5.5s
- Static `env=None` return count: `300`

# v014 Replay Dense classic500

Runtime-safe replay-dense attempt after v012/v013 completed with blank public scores.

This version uses `guide20_classic500`, keeping short single-hop messages while backing off the forced lower-bound count from guide22's `580`/`640` to `500`.

Key settings:

- `SEARCH_PROFILE = "guide20_classic500"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 500`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.78`
- `MUTATION_SEED_LIMIT = 0`

Expected interpretation:

- if it completes near or above v010, `500` is inside the hosted runtime envelope;
- if it no-scores, the safe floor is closer to v010's effective `400`;
- if it scores below v010, prompt/model balance matters more than count.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v014_replay_dense_classic500/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v014_replay_dense_classic500/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v014_replay_dense_classic500

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v014-replay-dense-classic500 \
  -v <version> \
  -f submission.csv \
  -m "v014 replay dense classic500"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v014-replay-dense-classic500`
- Version: `1`
- Submission ref: `53775306`
- Status: `PENDING` as of 2026-06-17 21:21 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.6s
- Static `env=None` return count: `400`

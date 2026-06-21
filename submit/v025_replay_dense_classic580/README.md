# v025 Replay Dense classic580

High-risk boundary probe after v019 reached public `51.300`.

This version preserves the v019 `classic570` shape and raises only `MIN_RETURN_CANDIDATES` from `570` to `580`.

Key settings:

- `SEARCH_PROFILE = "classic580"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 580`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.84`
- `MUTATION_SEED_LIMIT = 0`

Expected interpretation:

- if it completes at scale, expected public score is `52.200`;
- if it no-scores, the safe classic boundary is likely below 580;
- if it lands near v019, the higher floor did not convert into extra validated findings.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v025_replay_dense_classic580/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v025_replay_dense_classic580/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v025_replay_dense_classic580

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v025-replay-dense-classic580 \
  -v <version> \
  -f submission.csv \
  -m "v025 replay dense classic580"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v025-replay-dense-classic580`
- Version: `1`
- Submission ref: `53881541`
- Status: `PENDING` as of 2026-06-20 21:21 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.3s
- Static `env=None` return count: `400`

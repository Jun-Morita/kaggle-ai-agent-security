# v017 Replay Dense classic540

Controlled public-LB attempt after v014 became current best at public `45.000`.

This version uses `guide20_classic540`. It keeps v014/v016's profile family and raises the lower-bound return floor to `540`.

Key settings:

- `SEARCH_PROFILE = "guide20_classic540"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 540`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.8`
- `MUTATION_SEED_LIMIT = 0`

Expected interpretation:

- if it completes near `48.6`, the `540` floor is inside the hosted runtime envelope;
- if it no-scores, `540` is beyond the safe boundary and v014/v016 should guide future tuning;
- if it stays near `45.000`, the higher floor did not convert into extra validated findings.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v017_replay_dense_classic540/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v017_replay_dense_classic540/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v017_replay_dense_classic540

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v017-replay-dense-classic540 \
  -v <version> \
  -f submission.csv \
  -m "v017 replay dense classic540"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v017-replay-dense-classic540`
- Version: `1`
- Submission ref: `53788043`
- Status: `COMPLETE` as of 2026-06-18 21:02 JST
- Public score: `48.600`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 7.4s
- Static `env=None` return count: `400`

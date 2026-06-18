# v018 Replay Dense classic560

Controlled public-upside attempt after v017 reached public `48.600`.

This version adds a custom `classic560` profile, preserving the v017 shape while raising `MIN_RETURN_CANDIDATES` from `540` to `560`.

Key settings:

- `SEARCH_PROFILE = "classic560"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 560`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.82`
- `MUTATION_SEED_LIMIT = 0`

Expected interpretation:

- if it completes near `50.4`, the 560 floor is inside the hosted runtime envelope;
- if it no-scores, v017's 540 floor is close to the stable boundary;
- if it lands near `48.6`, the higher floor did not convert into extra validated findings.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v018_replay_dense_classic560/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v018_replay_dense_classic560/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v018_replay_dense_classic560

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v018-replay-dense-classic560 \
  -v <version> \
  -f submission.csv \
  -m "v018 replay dense classic560"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v018-replay-dense-classic560`
- Version: `1`
- Submission ref: `53808088`
- Status: `PENDING` as of 2026-06-18 21:31 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.6s
- Static `env=None` return count: `400`

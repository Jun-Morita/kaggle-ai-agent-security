# v015 Replay Dense n800

Safe backup submission while v014 is pending.

This version uses `guide18_n800`. It stays close to the proven v010 boundary by keeping `MIN_RETURN_CANDIDATES = 400`, while increasing `RETURN_TARGET_CANDIDATES` and `STATIC_FALLBACK_CANDIDATES` relative to v010.

Key settings:

- `SEARCH_PROFILE = "guide18_n800"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 400`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 40`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 400`
- `MUTATION_SEED_LIMIT = 3`

Expected interpretation:

- if it completes above v010, target/static count can be raised safely while the lower bound stays at 400;
- if it lands near v010, the v010 boundary is already close to optimal for this runtime path;
- if it no-scores, target/static count also affects hosted replay/runtime risk.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v015_replay_dense_n800/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v015_replay_dense_n800/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v015_replay_dense_n800

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v015-replay-dense-n800 \
  -v <version> \
  -f submission.csv \
  -m "v015 replay dense n800"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v015-replay-dense-n800`
- Version: `1`
- Submission ref: `53775486`
- Status: `PENDING` as of 2026-06-17 21:28 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 7.5s
- Static `env=None` return count: `400`

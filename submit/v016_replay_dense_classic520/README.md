# v016 Replay Dense classic520

Controlled public-LB attempt after v014 became the current best with public `45.000`.

This version uses `guide20_classic520`. It keeps v014's profile shape and raises only the lower-bound return floor from `500` to `520`.

Key settings:

- `SEARCH_PROFILE = "guide20_classic520"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 520`
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

- if it completes near `46.8`, the `520` floor is inside the hosted runtime envelope;
- if it no-scores, v014's `500` floor is close to the safe limit;
- if it stays near `45.000`, the floor increase did not translate cleanly into extra validated findings.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v016_replay_dense_classic520/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v016_replay_dense_classic520/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v016_replay_dense_classic520

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v016-replay-dense-classic520 \
  -v <version> \
  -f submission.csv \
  -m "v016 replay dense classic520"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v016-replay-dense-classic520`
- Version: `1`
- Submission ref: `53787950`
- Status: `COMPLETE` with blank public score as of 2026-06-18 21:02 JST
- Public score: none; treat as no-score / evaluator timeout
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 7.4s
- Static `env=None` return count: `400`

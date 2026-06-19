# v019 Replay Dense classic570

High-upside boundary probe after v017 reached public `48.600`.

This version adds a custom `classic570` profile, preserving the v017 shape while raising `MIN_RETURN_CANDIDATES` from `540` to `570`.

Key settings:

- `SEARCH_PROFILE = "classic570"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 570`
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

- it completed near `51.3`, so the usable boundary is just below guide22's failed `580+` range;
- if it no-scores, the safe boundary is likely between 560 and 570;
- if it lands near v017, the higher floor did not convert into extra validated findings.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v019_replay_dense_classic570/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v019_replay_dense_classic570/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v019_replay_dense_classic570

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v019-replay-dense-classic570 \
  -v <version> \
  -f submission.csv \
  -m "v019 replay dense classic570"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v019-replay-dense-classic570`
- Version: `1`
- Submission ref: `53808128`
- Status: `COMPLETE` as of 2026-06-19 19:47 JST
- Public score: `51.300`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.7s
- Static `env=None` return count: `400`

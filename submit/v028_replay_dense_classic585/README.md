# v028 Replay Dense classic585

Boundary probe after `v025_replay_dense_classic580` completed at public `52.200`.

This version preserves the successful `classic580` shape and raises only `MIN_RETURN_CANDIDATES` from `580` to `585`.

Key settings:

- `SEARCH_PROFILE = "classic585"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 585`
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

- if it completes at scale, expected public score is `52.650`;
- if it no-scores, the safe classic boundary is likely around `580-585`;
- if it lands near `v025`, the higher floor did not convert into extra validated findings.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v028_replay_dense_classic585/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v028_replay_dense_classic585/attack.py \
  --budget-s 60 --agent deterministic
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v028-replay-dense-classic585`
- Version: `1`
- Submission ref: `53913061`
- Status: `PENDING` as of 2026-06-21 21:28 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.6s
- Static `env=None` return count: `400`

# v029 Replay Dense classic590

Higher-risk boundary probe after `v025_replay_dense_classic580` completed at public `52.200`.

This version preserves the successful `classic580` shape and raises only `MIN_RETURN_CANDIDATES` from `580` to `590`.

Key settings:

- `SEARCH_PROFILE = "classic590"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 590`
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

- if it completes at scale, expected public score is `53.100`;
- if it no-scores while `v028` succeeds, the safe classic boundary is likely `585-590`;
- if it no-scores together with `v028`, fall back to `v025` as the current safe public baseline.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v029_replay_dense_classic590/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v029_replay_dense_classic590/attack.py \
  --budget-s 60 --agent deterministic
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v029-replay-dense-classic590`
- Version: `1`
- Submission ref: `53913086`
- Status: `PENDING` as of 2026-06-21 21:29 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.4s
- Static `env=None` return count: `400`

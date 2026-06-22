# v030 Replay Dense classic600

Higher-risk boundary probe after `v029_replay_dense_classic590` completed at public `53.100`.

This version preserves the successful `classic590` shape and raises only `MIN_RETURN_CANDIDATES` from `590` to `600`.

Key settings:

- `SEARCH_PROFILE = "classic600"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 600`
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

- if it completes at scale, expected public score is `54.000`;
- if it no-scores while `v029` succeeded, the safe classic boundary is likely `590-600`;
- if it completes, consider only cautious follow-up increments after checking runtime behavior.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v030_replay_dense_classic600/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v030_replay_dense_classic600/attack.py \
  --budget-s 60 --agent deterministic
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v030-replay-dense-classic600`
- Version: `1`
- Submission ref: `53946466`
- Status: `PENDING` as of 2026-06-22 21:50 JST
- Public score: pending
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.6s
- Static `env=None` return count: `400`

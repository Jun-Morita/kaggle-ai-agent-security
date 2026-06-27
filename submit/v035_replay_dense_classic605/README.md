# v035 Replay Dense classic605

Insurance boundary probe after `v030_replay_dense_classic600` completed at public `54.000` and while `v034_replay_dense_classic610` is pending.

This version preserves the successful `classic600` shape and raises only `MIN_RETURN_CANDIDATES` from `600` to `605`.

Key settings:

- `SEARCH_PROFILE = "classic605"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 605`
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

- if it completes at scale, expected public score is `54.450`;
- if `v034` no-scores but this completes, the practical boundary is likely `605-610`;
- if both complete, continue only cautious classic increments.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v035_replay_dense_classic605/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v035_replay_dense_classic605/attack.py \
  --budget-s 60 --agent deterministic
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v035-replay-dense-classic605`
- Version: `1`
- Submission ref: `53990711`
- Status: `COMPLETE` as of 2026-06-25
- Public score: `0.540`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.3s
- Static `env=None` return count: `400`

Notes:

- Expected score was `54.450`, but hosted public LB was only `0.540`.
- Hosted output contained `attack.py` and `submission.csv`; the hosted `attack.py` hash matched the local file.
- Treat this as a failed boundary probe.

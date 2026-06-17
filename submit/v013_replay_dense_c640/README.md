# v013 Replay Dense c640

High-risk / high-return public-LB attempt based on the same `AI Agent: Replay-Dense Exfiltration` attack template used by v012.

This version uses `guide22_c640`. It intentionally changes only the selected profile and repository wrapper metadata from v012.

Key settings:

- `SEARCH_PROFILE = "guide22_c640"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 640`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 80`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.9`
- `MUTATION_SEED_LIMIT = 0`

Expected interpretation:

- if it completes and validates close to 640 single-hop EXFIL findings, public score can exceed v012;
- if it times out or falls below v012, `MIN_RETURN_CANDIDATES = 640` is beyond the stable hosted boundary;
- this is not a private-LB hedge.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v013_replay_dense_c640/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v013_replay_dense_c640/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v013_replay_dense_c640

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v013-replay-dense-c640 \
  -v <version> \
  -f submission.csv \
  -m "v013 replay dense c640"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v013-replay-dense-c640`
- Version: `1`
- Submission ref: `53745360`
- Status: `COMPLETE` with blank public score as of 2026-06-17 20:57 JST
- Public score: none; treat as no-score / timeout
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 8.5s
- Static `env=None` return count: `400`

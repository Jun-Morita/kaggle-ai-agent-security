# v012 Replay Dense c580

Public-LB attempt based on `AI Agent: Replay-Dense Exfiltration` public score `52.2`.

This version ports the `guide22_c580` profile and keeps the reference settings unchanged except for this repository's script-kernel wrapper.

Key settings:

- `SEARCH_PROFILE = "guide22_c580"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 580`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 80`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.88`
- `MUTATION_SEED_LIMIT = 0`

Expected interpretation:

- if it completes near public `52.2`, the lower-bound count and shorter messages transferred;
- if it lands near v010 `36.000`, the public reference has hidden notebook/environment advantages or our wrapper changes candidate ordering;
- if it times out, `MIN_RETURN_CANDIDATES = 580` is too aggressive for our hosted runtime.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache   PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks   uv run python -m aicomp_sdk.cli.main validate redteam submit/v012_replay_dense_c580/attack.py

UV_CACHE_DIR=/tmp/uv-cache   PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks   uv run python -m aicomp_sdk.cli.main test redteam submit/v012_replay_dense_c580/attack.py   --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache   uv run kaggle kernels push -p submit/v012_replay_dense_c580

UV_CACHE_DIR=/tmp/uv-cache   uv run kaggle competitions submit   ai-agent-security-multi-step-tool-attacks   -k junichiromorita/ai-agent-security-v012-replay-dense-c580   -v <version>   -f submission.csv   -m "v012 replay dense c580"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v012-replay-dense-c580`
- Version: `1`
- Submission ref: `53744896`
- Status: `COMPLETE` with blank public score as of 2026-06-17 20:57 JST
- Public score: none; treat as no-score / timeout
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 7.8s
- Static `env=None` return count: `400`

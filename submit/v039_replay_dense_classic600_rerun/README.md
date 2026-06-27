# v039 Replay Dense classic600 Rerun

Post-update control rerun of the current confirmed best submission,
`v030_replay_dense_classic600`.

This version intentionally keeps the `v030` `attack.py` byte-for-byte identical
at creation time. The goal is to determine whether the successful `classic600`
shape still scores under the 2026-06-25 evaluator update.

Key inherited settings:

- `SEARCH_PROFILE = "classic600"`
- `MIN_RETURN_CANDIDATES = 600`
- `RETURN_TARGET_CANDIDATES = 800`
- `MAX_VERIFIED_CANDIDATES = 60`
- endpoint calibration counts `(1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- static env-none path returns `400`

Interpretation:

- if this scores near `54.000`, `v030` remains viable under the updated evaluator;
- if this collapses or no-scores, the old best is pre-update only and strategy
  should pivot to smaller post-update-scoring shapes such as v038/JED.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v039_replay_dense_classic600_rerun/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v039_replay_dense_classic600_rerun/attack.py \
  --budget-s 60 --agent deterministic
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v039-classic600-rerun`
- Kernel version: `1`
- Submission ref: `54042220`
- Status: `COMPLETE` as of 2026-06-25
- Public score: `0.540`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 6.3s
- Static return count: `400`

Notes:

- `attack.py` matches `v030` exactly, but the post-update public score is only
  `0.540` instead of `54.000`.
- Treat the old `classic600` high score as a pre-update result that no longer
  reproduces under the current evaluator.

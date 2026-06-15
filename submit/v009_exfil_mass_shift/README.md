# v009 Exfil Mass Shift

High-expectation mass-fill attempt based on the public `AI Agent Security - V2 Exfil Mass Shift` notebook.

This version keeps the stable v005 script-kernel wrapper and ports only the public notebook's higher-scale search profile and candidate ordering. It is deliberately not based on v006-v008 multipost prompts.

Key settings:

- `RETURN_TARGET_CANDIDATES = 360`
- `MAX_VERIFIED_CANDIDATES = 760`
- `STATIC_FALLBACK_CANDIDATES = 120`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 40`
- `SEARCH_FRACTION = 0.38`
- `MAX_SEARCH_S = 980.0`
- endpoint calibration counts `(1, 2, 4, 8)`
- `ENDPOINTS_PER_MSG = 8`
- `DEFAULT_MAX_HOPS = 8`
- score-sorted mass exfil fill with top-12 active combos and top-18 fill combos

Expected interpretation:

- if it completes, score should mainly reflect more single-post/domain-diverse exfil candidates than v005;
- if it times out, 360 returned candidates are beyond this account's hosted runtime envelope and the next step should be a midpoint such as 330 candidates;
- if it scores below v005 while completing, the public notebook's wrapper or exact prompt surface likely matters more than the simple parameter shift.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v009_exfil_mass_shift/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v009_exfil_mass_shift/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v009_exfil_mass_shift

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v009-exfil-mass-shift \
  -v <version> \
  -f submission.csv \
  -m "v009 exfil mass shift"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v009-exfil-mass-shift`
- Version: `1`
- Submission ref: `53687643`
- Script version: `327223458`
- Status: `Notebook Timeout`
- Public score: none
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 23.4s
- Static `env=None` return count: `120`

Interpretation:

- The public 32.71 mass-shift settings did not fit this hosted runtime envelope.
- Since `v005` completed at 300 candidates and `v009` timed out at 360 candidates, the next candidate-count experiment should use a midpoint or reduce search time before scaling returned candidates again.

# v003 Broad Prompt Bank

Score-improvement candidate that mixes `baseline-solution-4-900` style broad prompt banks into the working `v002` attack.

This version keeps the proven script-kernel submission wiring:

- `attack.py` is the Kaggle script entrypoint;
- GPU is disabled;
- `/kaggle/working/attack.py` is written;
- placeholder `/kaggle/working/submission.csv` is written for Kaggle's output check.

Attack changes:

- preserves the `v002` neutral URL exfil core;
- expands exfil payload patterns to `TOKEN=admin123`, `PASSWORD=test123`, and `SECRET_API_KEY=sk_live_test`;
- adds direct destructive-write probes;
- adds confused-deputy prompts that avoid explicit `send`, `email`, and `upload` wording;
- adds `snapshot()` / `restore()` branching for untrusted setup + follow-up prompts;
- mutates successful single-turn findings if time remains.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v003_broad_prompt_bank/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v003_broad_prompt_bank/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v003_broad_prompt_bank

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v003-broad-prompt-bank \
  -v <version> \
  -f submission.csv \
  -m "v003 broad prompt bank"
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v003-broad-prompt-bank`
- Version: `1`
- Submission ref: `53625867`
- Status: `PENDING` after repeated CLI checks on 2026-06-13
- Public score: pending
- Local deterministic smoke score: `0.00`

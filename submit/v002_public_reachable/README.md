# v002 Public Reachable

First score-improvement candidate after the working `v001` submission path.

This submission keeps the proven script-kernel wiring from `v001` and changes only the attack logic. The attack uses a fast verify-and-keep loop:

- try a small set of public fixture / untrusted-content probes;
- calibrate direct `http.post` exfil prompts;
- batch multiple neutral collector URLs per message to increase tool-call cell diversity;
- try a small confused-deputy message set;
- return a small exfil fallback only if the active environment produced no local findings.

The main expected scoring lift is from `EXFILTRATION`. The untrusted probes are intentionally cheap and retained only if the active environment actually fires predicates.

## Local Validation

From the repository root:

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v002_public_reachable/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v002_public_reachable/attack.py \
  --budget-s 60 --agent deterministic
```

## Kaggle Push

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v002_public_reachable
```

After the pushed kernel succeeds, submit the completed version:

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v002-public-reachable \
  -v <version> \
  -f submission.csv \
  -m "v002 public reachable"
```

Record the result in `submit/SUBMISSIONS.md` and `submit/submissions.csv`.

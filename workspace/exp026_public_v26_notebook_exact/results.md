# exp026 Results

## 2026-06-20

Candidate:

```text
submit/v026_public_v26_notebook_exact/agi-ai-agent-security.ipynb
```

Checks:

```bash
PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam \
  workspace/exp026_public_v26_notebook_exact/public_v26_attack.py
```

Result:

- Reference attack compile: passed
- SDK validate for reference attack: passed
- SDK deterministic smoke test: completed in about 16.5s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/public_v26_attack_20260620_212243.json`
- Static reference attack `env=None` return count: `208`
- Static total user messages: `624`
- Static message length min/mean/max: `32 / 38.0 / 41`
- Kaggle kernel: `junichiromorita/ai-agent-security-v026-public-v26-notebook-exact`
- Kaggle kernel version: `2`
- Kaggle submission ref: `53883538`
- Kaggle status: `PENDING` as of 2026-06-20 22:32 JST
- Kaggle public score: pending

Notes:

- This is not a script-kernel wrapper submission.
- Version 1 with GPU enabled was rejected by `CreateCodeSubmission`: `Submission not allowed: Your Notebook cannot use P100 GPUs in this competition.`
- Version 2 disables GPU and skips normal-run Qwen validation while preserving the generated attack shape and competition rerun server cell.
- Version 2 output generated `attack.py`, `submission.csv`, and skipped Qwen validation as intended.

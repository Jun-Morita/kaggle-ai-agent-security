# Attack Submission Template

Template for Kaggle **AI Agent Security - Multi-Step Tool Attacks** submissions.

```text
submit/v001_baseline/
├─ README.md
├─ attack.py
├─ submission.py
└─ kernel-metadata.json
```

## Files

- `attack.py`: source of the submitted `AttackAlgorithm`.
- `submission.py`: Kaggle script kernel entrypoint. It copies `attack.py` to `/kaggle/working/attack.py`, imports the competition gateway, and starts `JEDAttackInferenceServer`.
- `kernel-metadata.json`: Kaggle kernel metadata. Set `id` to your Kaggle username and desired slug before pushing.

## Local Validation

From the repository root:

```bash
PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v001_baseline/attack.py

PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v001_baseline/attack.py \
  --budget-s 60 --agent deterministic
```

Use `--env gym` with `evaluate redteam` for public-path parity once the local SDK dependencies are ready.

## Kaggle Push

```bash
uv run kaggle kernels push -p submit/v001_baseline
uv run kaggle kernels status your-kaggle-username/ai-agent-security-v001-baseline
```

Record each push and submission in `submit/SUBMISSIONS.md` and `submit/submissions.csv`.

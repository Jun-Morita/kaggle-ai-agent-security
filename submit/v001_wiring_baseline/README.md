# v001 Wiring Baseline

First Kaggle submission candidate for **AI Agent Security - Multi-Step Tool Attacks**.

Purpose: keep the submission wiring fixed and easy to validate before improving attack quality. This baseline is expected to be low-score; use it to confirm `attack.py` generation, SDK validation, local smoke test, and Kaggle kernel push flow.

```text
submit/v001_wiring_baseline/
├─ README.md
├─ attack.py
└─ kernel-metadata.json
```

## Files

- `attack.py`: Kaggle script kernel entrypoint and source of the submitted `AttackAlgorithm`. When run as a script, it copies itself to `/kaggle/working/attack.py`, writes a placeholder `/kaggle/working/submission.csv` for Kaggle's pre-submit output check, imports the competition gateway, and starts `JEDAttackInferenceServer`.
- `kernel-metadata.json`: Kaggle kernel metadata. Set `id` to your Kaggle username and desired slug before pushing.

## Local Validation

From the repository root:

```bash
PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v001_wiring_baseline/attack.py

PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v001_wiring_baseline/attack.py \
  --budget-s 60 --agent deterministic
```

Use `--env gym` with `evaluate redteam` for public-path parity once the local SDK dependencies are ready.

## Kaggle Push

```bash
uv run kaggle kernels push -p submit/v001_wiring_baseline
uv run kaggle kernels status your-kaggle-username/ai-agent-security-v001-wiring-baseline
```

## Competition Submit

UI submit may fail with `Could not find provided output file attack.py` even when the Output tab shows `attack.py`. Use CLI submission for the completed kernel version:

```bash
uv run kaggle competitions submit \
  ai-agent-security-multi-step-tool-attacks \
  -k junichiromorita/ai-agent-security-v001-wiring-baseline \
  -v 6 \
  -f submission.csv \
  -m "v001 wiring baseline"
```

This consumes a daily submission slot. This baseline is only for wiring confirmation and is expected to score 0.

Record each push and submission in `submit/SUBMISSIONS.md` and `submit/submissions.csv`.

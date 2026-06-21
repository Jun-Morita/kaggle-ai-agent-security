# v026 Public V26 notebook exact

Different-path test after `v022` and `v023` no-scored through the script-kernel wrapper.

This submission copies the actual public Kaggle notebook:

```text
boristown/agi-ai-agent-security
```

The goal is to test whether the public `56.25` result depends on notebook execution path, GPU/model-source metadata, or the public notebook's exact competition-rerun server cell rather than only the generated `AttackCandidate` logic.

Key settings:

- kernel type: notebook
- GPU: disabled for competition compatibility
- internet: disabled
- normal-run Qwen validation: skipped by default
- kernel source: `pilkwang/ai-agent-replay-dense-exfiltration`
- notebook version from pulled public kernel: `V26`
- generated attack shape: `208` candidates / `624` user messages
- each candidate: `web.search` then two short `POST ... body=TOKEN=admin123` messages

Expected interpretation:

- if it scores near public `56.25`, the earlier v022/v023 failures were likely submission-path or metadata transfer issues;
- if it no-scores, the public notebook is not directly transferable, and the repo should return to the confirmed classic family.
- version 1 with GPU enabled was rejected by the competition submit API because P100 GPUs are not allowed for this competition; version 2 disables GPU and skips normal-run Qwen validation while preserving the generated attack shape.

## Local Checks

The generated attack from the public kernel output is saved for reference at:

```text
workspace/exp026_public_v26_notebook_exact/public_v26_attack.py
```

Validate that file with:

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam workspace/exp026_public_v26_notebook_exact/public_v26_attack.py
```

## Kaggle

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p submit/v026_public_v26_notebook_exact
```

Then submit the completed kernel version as a code submission using `submission.csv`.

## Result

- Kernel: `junichiromorita/ai-agent-security-v026-public-v26-notebook-exact`
- Version: `2`
- Submission ref: `53883538`
- Status: `PENDING` as of 2026-06-20 22:32 JST
- Public score: pending
- Reference attack deterministic smoke score: `0.00`
- Reference attack deterministic smoke runtime: about 16.5s
- Static reference attack return count: `208`

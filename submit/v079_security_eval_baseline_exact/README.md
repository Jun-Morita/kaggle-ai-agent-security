# v079 Security Eval Baseline Exact

Exact-form transfer of the public `Security Eval Baseline` notebook.

## Strategy

- Single-post `SECRET_MARKER` live validation fill.
- Keep only successful marker-bearing `http.post` traces.
- Preserve the source runtime controls: `MARGIN_S=46.0`, `SLOWEST0=25.0`,
  `SLOWEST_MULT=1.35`, `FILL_BUDGET_FRAC=0.97`, and `HARD_N_CAP=2000`.

## Source And Compatibility Changes

- Source: `references/raw/notebooks/security-eval-baseline.ipynb`
- Attack logic changes: none.
- The first direct public-notebook push was rejected by Kaggle with
  `SaveKernel` HTTP 400. The Notebook therefore uses the already accepted v077
  execution wrapper while embedding the source `ATTACK_CODE` byte-for-byte.
- Kernel metadata disables GPU and Internet for competition compatibility.
- The wrapper writes `/kaggle/working/attack.py` and a normal-run placeholder
  `submission.csv` before serving the official inference gateway on rerun.

## Status

Submitted as Kaggle Kernel version 1.

- Kernel: `junichiromorita/ai-agent-security-v079-security-eval-base`
- Submission ref: `54609871`
- Status: `PENDING`
- SDK validation, source-attack equivalence, and hosted-output hash verification:
  passed.

The original Kernel slug exceeded Kaggle's 50-character limit. The submitted
slug is shortened to `ai-agent-security-v079-security-eval-base`; this does not
change the experiment directory or attack code.

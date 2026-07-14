# exp079 Security Eval Baseline Exact

## Hypothesis

The public `Security Eval Baseline` score of `62.720` improves upon v077's
`61.775` by preserving strict successful-event filtering while expanding the
live-fill deadline from 95% to 97% of the documented generation budget.

## Implementation

- Submission: `submit/v079_security_eval_baseline_exact/`
- Source: `references/raw/notebooks/security-eval-baseline.ipynb`
- Attack logic changes: none.
- The source Notebook form was rejected by the Kaggle Kernel API with
  `SaveKernel` HTTP 400. Use the v077 wrapper, which has already produced a
  valid Kaggle competition submission, while embedding the source attack code
  byte-for-byte.
- Compatibility change: use the v077 Notebook execution wrapper and disable
  GPU and Internet in its existing metadata.

## Validation Plan

- Confirm the Notebook's embedded `ATTACK_CODE` exactly matches this extracted
  attack source.
- Run syntax, SDK contract validation, and output-wrapper preflight.
- Confirm Kaggle hosted output contains both `attack.py` and `submission.csv`.

## Decision

Submit as an independent exact transfer. Do not combine it with v078's
result-only event signal or add an unvalidated tail in the first evaluation.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v079-security-eval-base` v1
- Submission ref: `54609871`
- Status: complete; public LB `61.965` as of 2026-07-13.
- Hosted source attack hash: `1962cc45072d`

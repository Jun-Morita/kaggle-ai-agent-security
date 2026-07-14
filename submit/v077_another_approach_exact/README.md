# v077 Another Approach Exact

Exact-form transfer of the public `AI Agent Sec | Another Approach` notebook.

## Strategy

- Use the same live-validation single-post primitive as v076.
- Keep only candidate traces containing `http.post` with `SECRET_MARKER` data.
- Preserve its distinct runtime control: `MARGIN_S=45.0`, with
  `SLOWEST0=25.0`, `SLOWEST_MULT=1.35`, `FILL_BUDGET_FRAC=0.95`, and
  `HARD_N_CAP=2000` unchanged.

## Source And Compatibility Changes

- Source: `references/raw/notebooks/ai-agent-sec-another-approach.ipynb`
- Attack logic change: none.
- Notebook metadata is changed only to disable GPU and Internet.
- The original normal-run placeholder `submission.csv` is retained.

## Status

Submitted as Kaggle Kernel version 1.

- Kernel: `junichiromorita/ai-agent-security-v077-another-approach-exact`
- Submission ref: `54556032`
- Status: complete; public score `61.775`
- Python syntax, SDK validation, and Notebook preflight: passed.
- Hosted output: `attack.py` and a four-row `submission.csv` confirmed;
  generated `attack.py` SHA-256 is `5b8d4f71864c`.

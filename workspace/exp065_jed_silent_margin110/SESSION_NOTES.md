# exp065 JED Silent Margin 1.10

## Hypothesis

`v063` scored `52.430` with the public JED silent notebook form and a
`slowest_s * 1.2` deadline guard. Reducing the guard to `1.1` may allow more
verified candidates to be collected before the deadline while preserving the
same compact prompt and notebook execution form.

## Implementation

- Submission directory: `submit/v065_jed_silent_margin110/`
- Notebook source: `submit/v065_jed_silent_margin110/jed-silent-margin110.ipynb`
- Only attack-logic change: `slowest_s * 1.2` -> `slowest_s * 1.1`
- GPU and internet disabled.

## Result

- SDK validate passed on the extracted `attack.py`.
- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v065-jed-silent-margin110` version 1.
- Hosted output contains `attack.py` and `submission.csv`.
- Submitted as ref `54396186`.
- Completed with blank public score as of 2026-07-07. Treat as no-score /
  `Submission Format Error` class.
- Reducing the deadline guard multiplier from `1.2` to `1.1` was too risky in
  this active-verifier notebook form.
- Notebook hash: `c10bcf4e0095`.
- Hosted `attack.py` hash: `ded1e15773ab`.

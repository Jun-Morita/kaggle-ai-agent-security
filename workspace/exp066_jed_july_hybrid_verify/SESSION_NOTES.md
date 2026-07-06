# exp066 JED July Hybrid Verify

## Hypothesis

`v063` active verified collection scored `52.430`, while `v064` direct July Safe
fill scored `49.500`. A mostly-JED active verifier with a small direct-prompt
share may preserve the stronger compact path while adding prompt diversity that
could help one model row or private behavior.

## Implementation

- Submission directory: `submit/v066_jed_july_hybrid_verify/`
- Notebook source: `submit/v066_jed_july_hybrid_verify/jed-july-hybrid-verify.ipynb`
- Every fourth probe uses the July Safe direct `http.post` prompt.
- Other probes use the proven JED silent prompt.
- `slowest_s * 1.2` deadline guard and active `eval_predicates` filtering are
  preserved.

## Result

- SDK validate passed on the extracted `attack.py`.
- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v066-jed-july-hybrid-verify` version 1.
- Hosted output contains `attack.py` and `submission.csv`.
- Submitted as ref `54396216`.
- Completed with blank public score as of 2026-07-07. Treat as no-score /
  `Submission Format Error` class.
- This result argues against mixing the July Safe direct prompt into the active
  verifier at a 25% ratio.
- Notebook hash: `6bd4789b38b3`.
- Hosted `attack.py` hash: `335cbf6fadc7`.

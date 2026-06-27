# exp045 Omega multipost2 N120

## Hypothesis

`SECRET_MARKER` revived the exfil path post-update. A smaller multipost probe may
increase score per returned candidate without crossing the N330/N350 replay
boundary.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v045-multipost2-n120` v1
- Submission ref: `54102209`
- Public LB: none; complete with blank public score as of 2026-06-27
- Local deterministic score: `0.00`
- Local deterministic runtime: about 8.5s
- Static return count: `120`
- Notes: py_compile, ruff, SDK validate, and deterministic smoke passed.
- Interpretation: no-score / replay timeout. Do not revive multipost without a
  lower-cost proof.

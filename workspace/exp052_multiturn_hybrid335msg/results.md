# exp052 Multiturn hybrid335msg

## Hypothesis

Three-message `AttackCandidate` chains may replay more efficiently than the same
number of separate single-message candidates. This tests a v043-sized
tool-intent budget with fewer candidates.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v052-multiturn-hybrid335msg` v1
- Submission ref: `54212725`
- Public LB: blank / no-score as of 2026-07-01
- Local deterministic score: `0.00`
- Local deterministic runtime: about 15.8s
- Static return count: `215`
- Static user-message count: `335`
- Notes: py_compile, ruff, SDK validate, deterministic smoke, kernel push, and competition submit passed. Treat result as no-score / replay timeout; `335` user messages in this shape are too heavy.

# exp053 Multiturn conservative250msg

## Hypothesis

A lower-count three-turn exfil probe can establish whether multi-turn
compression works before pushing the full v043-sized message budget.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v053-mt250` v1
- Submission ref: `54212740`
- Public LB: `21.500` as of 2026-07-01
- Local deterministic score: `0.00`
- Local deterministic runtime: about 11.3s
- Static return count: `150`
- Static user-message count: `250`
- Notes: py_compile, ruff, SDK validate, deterministic smoke, kernel push, and competition submit passed. Initial kernel push failed with the longer slug; `v053-mt250` succeeded. Multi-turn compression scored but did not beat the current post-update best `v043=30.170`.

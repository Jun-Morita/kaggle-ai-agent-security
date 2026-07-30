# exp117 v110 rerun

Hypothesis: hosted replay variance may lift an exact rerun of the repo-best v110 above 88.605 without changing timeout risk.

Change: copied `submit/v110_kaiwalya_classify6` and changed only Kaggle kernel slug/title metadata.

Validation:

- notebook JSON: passed
- `python3 -m py_compile submit/v117_v110_rerun/attack.py`: passed
- SDK validate redteam: passed

Submission:

- Kernel: `junichiromorita/ai-agent-security-v117-v110-rerun` version 1
- Competition submission ref: `55086859`
- Result: complete, public `88.200` as of 2026-07-30

Interpretation:

- Below original `v110=88.605`, so it does not replace the current best.
- Still high-88, so byte-identical replay variance remains meaningful but the v110 family is stable.

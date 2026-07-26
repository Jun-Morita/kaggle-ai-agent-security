# exp112_classify6_rerun

## Hypothesis

`v110` reached the repo best public score (`88.605`) and is within about seven clean single-post findings of the 2026-07-26 Silver boundary. Discussion `728947` reports high hosted replay variance for byte-identical submissions, so an exact rerun has positive expected value without adding timeout risk.

## Implementation

- Submission dir: `submit/v112_classify6_rerun`
- Baseline: `v110_kaiwalya_classify6`
- Attack: exact rerun of the `SPLIT_CLASSIFY_N=6` single-post `SECRET_MARKER` live validation-fill family
- Code changes from `v110`: none, except Kaggle kernel slug/title

## Validation

- `python3 -m json.tool submit/v112_classify6_rerun/ai-agent-security-solution-v9.ipynb`: passed
- `python3 -m py_compile submit/v112_classify6_rerun/attack.py`: passed
- `aicomp validate redteam submit/v112_classify6_rerun/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v112-classify6-rerun` version 1
- Competition submission ref: `54992796`
- Status: pending as of 2026-07-26 14:47 JST
- Note: Kaggle API now rejects code submissions with `-f attack.py`; this was submitted successfully with `-f submission.csv`, while the kernel output contains both `attack.py` and `submission.csv`.

# exp113_classify5_boundary

## Hypothesis

`v110` showed that reducing `SPLIT_CLASSIFY_N` from `8` to `6` improves throughput, while `v109` showed that `4` is too aggressive and can fail with Kaggle `incorrect format`. `5` is the remaining boundary rung: it may recover one more classification interaction while staying closer to the scoring `v110` behavior.

## Implementation

- Submission dir: `submit/v113_classify5_boundary`
- Baseline: `v110_kaiwalya_classify6`, public `88.605`
- Attack: same single-post `SECRET_MARKER` live validation-fill family
- Change: `SPLIT_CLASSIFY_N=6 -> 5`

## Validation

- `python3 -m json.tool submit/v113_classify5_boundary/ai-agent-security-solution-v9.ipynb`: passed
- `python3 -m py_compile submit/v113_classify5_boundary/attack.py`: passed
- `aicomp validate redteam submit/v113_classify5_boundary/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v113-classify5` version 1
- Competition submission ref: `54992805`
- Status: complete as of 2026-07-27
- Public LB: `87.390`
- Note: Kaggle API now rejects code submissions with `-f attack.py`; this was submitted successfully with `-f submission.csv`, while the kernel output contains both `attack.py` and `submission.csv`.
- Readout: `SPLIT_CLASSIFY_N=5` avoided format error but underperformed `v110=88.605`, so further classification reduction is not currently supported.

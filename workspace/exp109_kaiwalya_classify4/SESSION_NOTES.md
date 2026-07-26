# exp109_kaiwalya_classify4

## Hypothesis

The current best family is latency-bound. Reducing the initial latency-classification sample count from `8` to `4` may reclaim a few successful single-post candidates without changing the payload, replay-safe sizing, or multipost behavior.

## Implementation

- Submission dir: `submit/v109_kaiwalya_classify4`
- Source notebook: `references/raw/notebooks/kaiwalya-ai-agent-security-solution/v009__scriptVersionId-337445891/source.ipynb`
- Baseline: `v106_kaiwalya_solution_v9_exact`, public `88.110`
- Attack: live validation-fill / replay-safe single-hop `SECRET_MARKER`
- Change: `SPLIT_CLASSIFY_N=8 -> 4`

## Validation

- `python3 -m py_compile submit/v109_kaiwalya_classify4/attack.py`: passed
- `aicomp validate redteam submit/v109_kaiwalya_classify4/attack.py`: passed

## Result

- Kernel: `junichiromorita/ai-agent-security-v109-classify4` version 1
- Competition submission ref: `54967528`
- Status: complete with Kaggle `incorrect format` error as of 2026-07-25
- Public LB: blank

## Failure Analysis

- Hosted kernel status is `COMPLETE`.
- Hosted output contains both `attack.py` and placeholder `submission.csv`.
- Hosted `attack.py` SHA-256 matches local: `a2b817d72b8c8bf845bef58a2caaf815de37b7a7b02c943ace1e959369579723`.
- Kaggle API error description: generated submission file has incorrect format.
- Since `v106` with the same notebook wrapper scored `88.110`, this is not a wrapper or missing-output issue.
- The only attack-code change is `SPLIT_CLASSIFY_N=8 -> 4`. Treat this as negative evidence for reducing the latency classification sample this far; the change likely made one hosted model branch unsafe enough that the rerun gateway did not emit a valid scored submission.

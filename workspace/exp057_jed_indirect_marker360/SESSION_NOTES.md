# exp057 JED Indirect Marker N360

## Hypothesis

The `jed-indirect-marker360` public notebook reports a materially higher public
score than our current post-update best. It appears to use the same indirect
fixture-page mechanism as the 300-candidate variant, only scaled to 360 unique
one-message candidates.

## Risk

The upside is higher, but the recent Submission Format Error series suggests we
should treat larger candidate counts carefully. This version remains single-hop
and search-free, so its risk should mainly be replay/evaluator boundary rather
than attack-generation runtime.

## Implementation

- Submission directory: `submit/v057_jed_indirect_marker360/`
- Static 360 candidates.
- Wrapper mirrors `v056` and starts the JED server only during competition rerun.

## Local validation

- `uv run ruff check submit/v057_jed_indirect_marker360/attack.py`: passed
- `aicomp_sdk.cli.main validate redteam`: passed
- deterministic smoke: `0.00`, about 23.8s, 360 static candidates

## Result

- Kernel `junichiromorita/ai-agent-security-v057-jed-indirect-marker360` version 1 pushed and completed.
- Hosted output includes `attack.py` and `submission.csv`.
- Kaggle CLI competition registration initially failed when using `-f attack.py`.
- Submitted with `-f submission.csv` as ref `54325987`; status `PENDING` as of 2026-07-04.

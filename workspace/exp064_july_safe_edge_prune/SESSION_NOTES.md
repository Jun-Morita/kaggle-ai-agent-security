# exp064 July Safe Edge Prune

## Hypothesis

The public `LB51.255 July Safe: Edge Prune` notebook improves on our current
post-update best `v059=45.585` by using per-model deadline-aware single-hop
candidate fill rather than a fixed or probe-sized candidate count.

The key transfer risk is runtime. The public notebook intentionally avoids the
recently failing K2 / burst / multihop branches and changes only the deadline
safety margin to `MARGIN_S = 44.0`.

## Implementation

- Submission directory: `submit/v064_july_safe_edge_prune/`
- Notebook source:
  `submit/v064_july_safe_edge_prune/lb51-255-july-safe-edge-prune.ipynb`
- Close copy from:
  `references/raw/notebooks/lb51-255-july-safe-edge-prune.ipynb`
- Kernel type: notebook
- GPU: disabled
- Internet: disabled

## Validation

- Notebook copied from the reviewed public raw notebook.
- Public notebook already writes `/kaggle/working/attack.py`.
- Public notebook writes placeholder `submission.csv` outside competition rerun.

## Result

- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v064-july-safe-edge-prune` version 1.
- Hosted output contains `attack.py` and `submission.csv`.
- Submitted as ref `54365420`; completed at public `49.500` as of
  2026-07-06.
- Strong score, but below `v063=52.430`; active verified collection is
  currently a better path than unfiltered deadline-aware fill.
- Notebook hash: `4dfd8accb725`.
- Hosted `attack.py` hash: `281a11a213fa`.

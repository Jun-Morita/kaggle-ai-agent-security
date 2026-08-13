# exp145_dimong4_v16_exact

## Hypothesis

The public `dimong4/ai-agent-security` v16 branch combines `REPLAY_SAFE_FRAC=0.975`, `SPLIT_CLASSIFY_N=8`, and a shorter slow-row Harmony frame. It may be more stable under the post-refresh evaluator than the current `v140=87.705` template-race branch and different enough from pending Nikita `v143/v144` to provide useful exploration.

## Source

- Kernel: `dimong4/ai-agent-security`
- Version: `16`
- scriptVersionId: `339219173`
- Archived public LB: `89.100`
- Downloaded source: `/tmp/kaggle-aas-dimong4/v016__scriptVersionId-339219173/source.ipynb`

## Implementation

- Copied source notebook to `submit/v145_dimong4_v16_exact/source.ipynb`.
- Extracted embedded `src` to `submit/v145_dimong4_v16_exact/attack.py`.
- Added private Kaggle kernel metadata with competition source.

## Notes

- `fetch_kernel_score.py` reported `90.09`, but version archive selected v16 with numeric public `89.100`; treat `89.100` as the verified score for this exact source.
- Key differences from `v140`:
  - `SPLIT_CLASSIFY_N = 8` instead of `6`
  - no 3+3 template race
  - shorter `FRAME_TEMPLATE`
- Key differences from `v143`:
  - `REPLAY_SAFE_FRAC = 0.975` instead of `0.98`
  - shorter `FRAME_TEMPLATE`

## Expected Readout

- If `v145 > v140`, short-frame `SPLIT_CLASSIFY_N=8` is a useful post-refresh branch.
- If `v145 <= v140`, prefer the `v140` template-race lineage unless `v143/v144` beat it.

## Submission

- 2026-08-13: pushed kernel `junichiromorita/ai-agent-security-v145-dimong4-v16` version 2.
- Submitted to competition as ref `55482945` with message `v145 dimong4 v16 exact`.
- Status: pending as of 2026-08-13 12:23 JST snapshot.

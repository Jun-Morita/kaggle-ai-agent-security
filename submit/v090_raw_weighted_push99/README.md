# v090 Raw Weighted Push99

Independent high-upside branch from `v087`.

## Strategy

- Close transfer of the `pilkwang` / `liubaby` raw-weighted public source.
- Push replay-safe sizing to `REPLAY_SAFE=0.99`.
- Select templates by measured raw-per-second.
- Keep a larger template bank than R1-011.

## Source

- Experiment: `workspace/exp090_raw_weighted_push99/`
- Public reference: `liubabyvstone/ai-security-pilkwang-v3`
- Same source hash observed in:
  `pilkwang/ai-agent-v3-1-2-single-post-exfiltration`
- Raw notebook:
  `references/raw/notebooks/ai-security-pilkwang-v3-20260717.ipynb`
- Source hash: `e13fc4b9ea5b`

## Status

Submitted to Kaggle.

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.
- Kernel: `junichiromorita/ai-agent-security-v090-raw-weighted-push99`
- Competition submission ref: `54781620`
- Status: complete with blank public score as of 2026-07-18
- Diagnosis: likely replay failure. The larger template bank and raw-per-second
  selection increased variance relative to the five-template public 84.87
  notebook.

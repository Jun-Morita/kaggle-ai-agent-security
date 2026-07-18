# v089 R1-011 Push99

High-upside follow-up to `v087`.

## Strategy

- Close transfer of current public R1-011.
- Push replay-safe sizing to `REPLAY_SAFE=0.99`.
- Use `PROBE_REPS=5` and `MIN_FIRE_RATE=0.2`.
- Estimate fill cost from successful firing probe latencies.

## Source

- Experiment: `workspace/exp089_r1_011_push99/`
- Public reference: `yusuketogashi/ai-agent-sec-another-approach`
- Raw notebook:
  `references/raw/notebooks/ai-agent-sec-another-approach-20260717.ipynb`
- Source hash: `a3e9d3a7190e`

## Status

Submitted to Kaggle.

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.
- Kernel: `junichiromorita/ai-agent-security-v089-r1-011-push99`
- Competition submission ref: `54781615`
- Status: complete with blank public score as of 2026-07-18
- Diagnosis: likely replay failure. The later public 84.87 notebook keeps the
  same five-template `REPLAY_SAFE=0.99` shape but estimates fill cost from all
  selected probe latencies, not successful-fire latencies only.

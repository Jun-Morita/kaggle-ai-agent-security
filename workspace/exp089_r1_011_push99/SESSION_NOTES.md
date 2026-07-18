# exp089 R1-011 Push99

## Hypothesis

`v087` scored public `76.950` with the R1-008 replay-safe single-message
family. The current public R1-011 source pushes the same family harder while
using successful-fire latency for fill sizing.

## Source

- Public Code: `yusuketogashi/ai-agent-sec-another-approach`
- Pulled: 2026-07-17
- Extracted source hash: `a3e9d3a7190e`
- Saved raw notebook:
  `references/raw/notebooks/ai-agent-sec-another-approach-20260717.ipynb`

## Implementation

Close source transfer of current R1-011:

- `REPLAY_SAFE = 0.99`
- `PROBE_REPS = 5`
- `MIN_FIRE_RATE = 0.2`
- removes `call_syntax` relative to `v087`
- estimates fill cost from successful firing probe latencies

## Expected Outcome

This is the direct high-upside continuation of `v087`. It spends more of the
replay budget than `v087`, so it can score higher if hosted timing is favorable,
but it also has higher no-score risk.

## Validation

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v089-r1-011-push99` version 1
- Competition submission ref: `54781615`
- Status: complete with blank public score as of 2026-07-18
- Diagnosis: likely replay failure. The public 84.87 five-template notebook
  uses all selected probe latencies for `fill_unit`; this experiment used
  successful-fire latencies only, likely underestimating replay cost and
  returning too many candidates.

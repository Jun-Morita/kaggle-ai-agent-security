# exp128_template_race

## Hypothesis

The active family uses six plain-template trials to classify a model as fast or
slow using a fixed latency threshold, then chooses either the plain or Harmony
frame. Reusing the same six trials as a balanced, per-model template race may
choose the lower elapsed-time-per-success frame directly and improve successful
candidate throughput without increasing the replay budget.

## Base and Change

- Base: `submit/v123_v121_exact_rerun`
- Keep the payload, one-post candidate shape, candidate cap, replay-safe fraction,
  warm-up, and all replay sizing unchanged.
- Replace the six plain latency-classification trials with three plain and three
  Harmony-frame trials.
- Choose the remaining frame by observed total elapsed time per successful post.

## Validation

- `python3 -m py_compile`: passed.
- SDK `validate redteam`: passed.
- Deterministic 60-second smoke: completed; expected score `0.00`.
- Notebook JSON is valid and emits the identical `attack.py`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v128-template-race` version 1.
- Competition submission ref: `55182815`.
- Status: complete.
- Public LB: `89.505` as of 2026-08-03.
- Attack SHA-256: `a04933506595`.
- Result: tied `v125=89.505` and underperformed `v123=91.890`; the template
  race did not recover enough throughput to defend Silver.
- Risk: template selection can choose the wrong branch under noisy early probes,
  but it does not widen the known replay envelope.

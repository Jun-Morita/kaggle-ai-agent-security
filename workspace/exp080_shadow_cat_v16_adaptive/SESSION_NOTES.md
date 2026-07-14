# exp080 Shadow Cat V16 Adaptive

## Hypothesis

v076 submitted the supplied Shadow Cat v15 single-post source and scored
`54.740`. The currently public source is v16, whose adaptive multi-post probe
can amortize interaction overhead while reverting to v15 single-post fill if
the live distinct-domain yield is weak. The public Notebook reports `63.650`.

## Implementation

- Submission: `submit/v080_shadow_cat_v16_adaptive/`
- Source: current `lucifer19/shadow-cat-firewall` pulled on 2026-07-12.
- Source attack SHA-256: `499ed856821c`.
- Attack logic changes: none.
- Compatibility-only change: use v077's accepted execution wrapper and CPU /
  no-Internet Kernel metadata.

## Validation Plan

- Verify the source attack, extracted experiment source, and generated
  Notebook attack content match exactly.
- Run syntax, SDK validation, and wrapper preflight.
- Verify Kaggle output artifacts before the competition submission.

## Risk

The source begins multi-post collection and uses one interaction per candidate.
Although it has an early adaptive revert, replay cost can rise when multi-post
continues. Keep this as an independent high-upside public-score test rather
than a replacement for the v077 single-post baseline.

## Result

- Public LB: `42.870` as of 2026-07-13.
- The adaptive multi-post branch did not preserve the single-post baseline in
  this evaluation. Keep the result as negative evidence against this branch.

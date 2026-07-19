# v096 Density Ladder Margin150

## Strategy

- Controlled upside variant of `v095_adaptive_density_ladder_exact`.
- Changes only the attack-generation reserve from `MARGIN_S = 180.0` to `150.0`.
- Keeps `REPLAY_SAFE = 0.99`, replay charge, exact URL matching, holdout confirmation, rolling fallback, and all arm definitions unchanged.
- Goal: beat the public `86.175` notebook if the exact source was leaving generation time unused before filling the replay ledger.

## Source

- Parent: `submit/v095_adaptive_density_ladder_exact/`
- Public reference: `tetsutani/ai-agent-security-adaptive-tool-call-throughput-se`
- Baseline to beat: `v093_edgefill_v27_safe982`, public `84.600`.

## Status

- Validation passed: `py_compile`, SDK `validate`, deterministic SDK smoke, notebook format validation.
- Kaggle kernel: `junichiromorita/ai-agent-security-v096-density-margin150` version 1.
- Competition submission: ref `54831468`, status `PENDING` as of 2026-07-19 22:08 JST.

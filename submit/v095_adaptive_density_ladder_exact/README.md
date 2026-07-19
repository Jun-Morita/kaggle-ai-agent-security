# v095 Adaptive Density Ladder Exact

## Strategy

- Exact port of `tetsutani/ai-agent-security-adaptive-tool-call-throughput-se`.
- Public reference score: `86.175`.
- Adaptive score-density ladder across one-call, two-call, and three-call `SECRET_MARKER` exfiltration forms.
- Uses exact URL matching, holdout confirmation, rolling fallback, and conservative replay ledger.

## Source

- Experiment: `workspace/exp095_adaptive_density_ladder_exact/`
- Extracted source: `/tmp/aas-kernel-analysis-20260719/tetsutani_attack.py`
- Source attack SHA-256 prefix: `a57847310bfd`
- Baseline to beat: `v093_edgefill_v27_safe982`, public `84.600`.

## Status

- Validation passed: `py_compile`, SDK `validate`, deterministic SDK smoke, notebook format validation.
- Kaggle kernel: `junichiromorita/ai-agent-security-v095-density-ladder` version 1.
- Competition submission: ref `54831375`, status `PENDING` as of 2026-07-19 22:03 JST.

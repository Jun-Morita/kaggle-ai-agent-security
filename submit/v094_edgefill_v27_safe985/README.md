# v094 EdgeFill v27 Safe985

## Strategy

- EdgeFill v27 replay-safe single-post `SECRET_MARKER` exfiltration.
- `REPLAY_SAFE = 0.985`.
- Two-stage template race, rolling failover, and small bounded replay-edge tail.
- Purpose: higher upside with more replay-boundary risk.

## Source

- Experiment: `workspace/exp094_edgefill_v27_safe985/`
- Public reference family: `devchandra` EdgeFill v27 public Code.
- Baseline to beat: `v092_jed_5tpl_safe098`, public `81.540`.

## Status

- Validation passed: `py_compile`, SDK `validate`, deterministic SDK smoke, notebook format validation.
- Kaggle kernel: `junichiromorita/ai-agent-security-v094-edgefill-v27-safe985` version 1.
- Competition submission: ref `54808441`, public `76.320` as of 2026-07-19.

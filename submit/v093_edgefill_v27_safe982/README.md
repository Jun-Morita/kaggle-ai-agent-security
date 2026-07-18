# v093 EdgeFill v27 Safe982

## Strategy

- EdgeFill v27 replay-safe single-post `SECRET_MARKER` exfiltration.
- `REPLAY_SAFE = 0.982`.
- Two-stage template race, rolling failover, and small bounded replay-edge tail.
- Purpose: balanced silver attempt close to v092 safety.

## Source

- Experiment: `workspace/exp093_edgefill_v27_safe982/`
- Public reference family: `devchandra` EdgeFill v27 public Code.
- Baseline to beat: `v092_jed_5tpl_safe098`, public `81.540`.

## Status

- Validation passed: `py_compile`, SDK `validate`, deterministic SDK smoke, notebook format validation.
- Kaggle kernel: `junichiromorita/ai-agent-security-v093-edgefill-v27-safe982` version 1.
- Competition submission: ref `54808421`, status `PENDING` as of 2026-07-18 22:09 JST.

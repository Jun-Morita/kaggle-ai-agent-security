# exp092 JED 5 Templates Safe098

## Hypothesis

The public five-template `REPLAY_SAFE=0.99` notebook is high scoring but sits
near the replay boundary. A safety pair at `REPLAY_SAFE=0.98` may preserve most
of the score while reducing blank-score risk.

## Source

- Base: `workspace/exp091_jed_5tpl_exact099/attack.py`
- Public reference: `assiaben/jed-attack-5-templates-aggressive-replay-0-99`
- Base `attack_code` hash: `97a839b8755`

## Implementation

Single-knob variant:

- `REPLAY_SAFE = 0.99` -> `0.98`
- All templates, probe settings, latency sizing, and wrapper behavior unchanged.

## Validation

Pending.

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v092-jed-5tpl-safe098` version 1
- Competition submission ref: `54794174`
- Status: complete as of 2026-07-18
- Public score: `81.540`
- Result: current confirmed best; lowering `REPLAY_SAFE` to `0.98` beat
  `v087=76.950` by `+4.590` and beat exact `v091=73.935`.

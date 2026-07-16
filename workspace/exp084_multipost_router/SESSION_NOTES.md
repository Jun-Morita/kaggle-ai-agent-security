# exp084 Multipost Router

## Hypothesis

The single-post live-fill plateau around `61-64` suggests a structural lever is
needed for silver-zone attempts. Public `tensorliu/jed-attack-improved-nb`
proposes per-model routing:

- fast row: keep one-post bare template
- slow row: request multiple `http.post` events per candidate to amortize fixed
  per-candidate replay overhead

This is high risk because earlier multi-post attempts in this repo
underperformed or timed out, but it is one of the few public approaches that
explicitly attacks the score plateau.

## Implementation

- Source: `tensorliu/jed-attack-improved-nb`
- Extracted from notebook `ATTACK_PY_B64` into
  `workspace/exp084_multipost_router/attack.py`.
- Preserved parameters from the public source:
  - `_POSTS_SLOW = 3`
  - `_FILL_FRAC = 0.85`
  - `_MARGIN_S = 60.0`
  - `_SLOWEST0 = 30.0`
  - `_SLOWEST_MULT = 1.5`
  - `_PROBE_K = 8`
  - `_FAST_THR = 17.0`

## Risk

High.

- Multi-post has been negative in this repo historically.
- The approach depends on hosted model behavior and per-model latency routing.
- It may no-score if replay/generation gets too slow.

## Validation

- SDK `validate redteam` passed.
- Deterministic smoke completed with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v084-multipost-router` v1
- Submission ref: `54689110`
- Status: `COMPLETE` as of 2026-07-15.
- Public LB: blank / no-score.

## Result

The submission completed with blank public score. Treat as no-score / evaluator
failure. The profile is likely outside the current replay/runtime envelope.

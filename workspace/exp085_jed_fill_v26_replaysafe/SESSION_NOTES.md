# exp085 JED Fill v26 Replay Safe

## Hypothesis

Recent no-score submissions suggest the active bottleneck is replay timeout, not
local syntax or SDK compatibility. Public `pengwang91/jed-fill-v26-replaysafe`
directly addresses that by capping returned candidates using measured replay
cost rather than simply filling the attack-generation budget.

## Implementation

- Source: `pengwang91/jed-fill-v26-replaysafe`
- Extraction: decoded `_ATTACK_B64` from the public notebook.
- Preserved key settings:
  - `REPLAY_SAFE = 0.90`
  - `REPLAY_BUDGET_S = 9000.0`
  - `MARGIN_S = 60.0`
  - `MARGIN_MULT = 1.35`
  - `SLOWEST0 = 24.0`
  - `PROBE_REPS = 2`
  - `MIN_FIRE_RATE = 1.0`
- Candidate selection uses proven templates and sums measured live latencies to
  keep the returned set under a replay cost cap.

## Risk

Medium. The approach is designed to avoid replay timeout, but it still depends
on hosted latency matching the search-time proxy closely enough.

## Validation

- SDK validate passed.
- Deterministic smoke passed with score `0.00`.
- Notebook embedded source hash matched `workspace/exp085_jed_fill_v26_replaysafe/attack.py`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v085-jed-v26-safe` version 1
- Competition submission ref: `54726743`
- Status: complete
- Public LB: `63.495` as of 2026-07-16
- Outcome: current confirmed best; improves over `v079=61.965` by `+1.530`.

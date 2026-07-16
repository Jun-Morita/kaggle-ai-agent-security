# exp086 JED Fill v26 Safe85

## Hypothesis

`v085` follows the public replay-safe notebook with `REPLAY_SAFE=0.90`. Because
the current grader is unstable and no-score failures are common, this paired
submission lowers the returned replay-cost cap to `0.85`.

## Implementation

- Base: `workspace/exp085_jed_fill_v26_replaysafe/attack.py`
- Only logic change:
  - `REPLAY_SAFE = 0.90` -> `REPLAY_SAFE = 0.85`

## Risk

Lower timeout risk than `v085`, with lower public-score ceiling because fewer
candidates may be returned.

## Validation

- SDK validate passed.
- Deterministic smoke passed with score `0.00`.
- Notebook embedded source hash matched `workspace/exp086_jed_fill_v26_safe85/attack.py`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v086-jed-v26-safe85` version 1
- Competition submission ref: `54726739`
- Status: complete
- Public LB: `61.290` as of 2026-07-16
- Outcome: below both `v085=63.495` and `v079=61.965`; `REPLAY_SAFE=0.85`
  appears too conservative for the current public score envelope.

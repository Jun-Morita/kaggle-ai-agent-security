# v086 JED Fill v26 Safe85

Safety-paired variant of `v085`.

## Strategy

- Same replay-cost-capped candidate selection as `v085`.
- Lower `REPLAY_SAFE` from `0.90` to `0.85`.

## Source

- Experiment: `workspace/exp086_jed_fill_v26_safe85/`
- Base: `workspace/exp085_jed_fill_v26_replaysafe/attack.py`

## Status

Submitted to Kaggle.

- Kernel: `junichiromorita/ai-agent-security-v086-jed-v26-safe85` version 1
- Competition submission ref: `54726739`
- Status: complete
- Public LB: `61.290` as of 2026-07-16
- Validation: SDK validate passed; deterministic smoke completed with score `0.00`

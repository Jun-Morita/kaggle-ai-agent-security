# v085 JED Fill v26 Replay Safe

Close transfer of public `pengwang91/jed-fill-v26-replaysafe`.

## Strategy

- Probe a small set of proven single-post templates.
- Keep only templates with full probe fire rate.
- Fill with the cheapest firing template.
- Cap returned candidates by measured replay cost:
  `REPLAY_SAFE * REPLAY_BUDGET_S`.

## Source

- Experiment: `workspace/exp085_jed_fill_v26_replaysafe/`
- Public reference: `pengwang91/jed-fill-v26-replaysafe`

## Status

Submitted to Kaggle.

- Kernel: `junichiromorita/ai-agent-security-v085-jed-v26-safe` version 1
- Competition submission ref: `54726743`
- Status: complete
- Public LB: `63.495` as of 2026-07-16
- Validation: SDK validate passed; deterministic smoke completed with score `0.00`

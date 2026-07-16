# v084 Multipost Router

High-risk / high-return submission based on public
`tensorliu/jed-attack-improved-nb`.

## Strategy

- Probe row latency.
- If row appears fast, use a one-post bare template.
- If row appears slow, use a three-post template to test whether multiple
  exfiltration events per candidate can amortize fixed per-candidate overhead.

## Source

- Experiment: `workspace/exp084_multipost_router/`
- Public reference: `tensorliu/jed-attack-improved-nb`
- Extraction: decoded public notebook `ATTACK_PY_B64` into `attack.py`.

## Status

Submitted as Kaggle Kernel version 1.

- Kernel: `junichiromorita/ai-agent-security-v084-multipost-router`
- Submission ref: `54689110`
- Status: `COMPLETE` as of 2026-07-15.
- Public LB: blank / no-score.
- Validation:
  - SDK `validate redteam` passed.
  - Deterministic smoke completed with score `0.00`.

## Result

The submission completed with blank public score. Treat as no-score / evaluator
failure. The multi-post routed profile is likely too heavy for the current
runtime/replay envelope.

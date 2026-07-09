# exp071 AI Agent V3 Margin44

## Hypothesis

`v070` is a close public v3.1.2 single-post transfer. This paired variant changes
only the deadline safety margin from `42.0` to `44.0`, matching the successful
`v064_july_safe_edge_prune` margin.

The goal is to reduce blank-score risk while preserving the same single-post
validated fill logic.

## Implementation

- Submission directory: `submit/v071_ai_agent_v3_margin44/`
- Notebook source:
  `submit/v071_ai_agent_v3_margin44/ai-agent-v3-1-2-single-post-exfiltration.ipynb`
- Changes from `v070`:
  - `MARGIN_S = 42.0` -> `MARGIN_S = 44.0`

## Validation

- Notebook JSON check passed.
- Build-cell execution generated `attack.py`.
- SDK validate passed on generated `attack.py`.
- Deterministic smoke completed in about `15.1s` with score `0.00`.
- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v071-ai-agent-v3-margin44` version 1.
- Hosted output contains `attack.py` and `submission.csv`.
- Hosted `attack.py` confirms `MARGIN_S = 44.0`.

## Result

- Submitted as ref `54463577`.
- Complete with public `57.825` as of 2026-07-09.
- This is the current confirmed post-update best.
- Notebook hash: `f9d8baa1db62`.
- Hosted `attack.py` hash: `c9c6c628cd3b`.

## Interpretation

The single-knob margin change from `v070` was decisive: `MARGIN_S=42.0`
no-scored, while `MARGIN_S=44.0` transferred successfully. Keep future
experiments close to this single-post deadline-aware family.

# exp072 AI Agent V3 Margin43

## Hypothesis

`v071` scored `57.825` with `MARGIN_S=44.0`, while `v070` no-scored with
`MARGIN_S=42.0`. A narrow boundary probe at `43.0` may recover a little more
generation budget without crossing the no-score boundary.

## Implementation

- Submission directory: `submit/v072_ai_agent_v3_margin43/`
- Baseline: `submit/v071_ai_agent_v3_margin44/`
- Change:
  - `MARGIN_S = 44.0` -> `MARGIN_S = 43.0`

All other attack logic remains unchanged.

## Validation

- Notebook JSON check passed.
- Kernel metadata JSON check passed.
- Local notebook execution generated `attack.py` and placeholder `submission.csv`.
- SDK validate passed on generated `attack.py`.
- Deterministic smoke completed in about `15.2s` with score `0.00`.
- Notebook hash: `32c64a455059`.
- Generated `attack.py` hash: `1fea9394aa99`.

## Result

- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v072-ai-agent-v3-margin43` version 1.
- Submitted as ref `54492957`.
- Status: `PENDING` as of 2026-07-09.

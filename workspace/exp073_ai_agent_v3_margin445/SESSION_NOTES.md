# exp073 AI Agent V3 Margin445

## Hypothesis

`v071` is the current best at `57.825` with `MARGIN_S=44.0`. A slightly safer
`44.5` margin may preserve most of the score while improving completion
reliability if the hosted evaluator has variance near the deadline boundary.

## Implementation

- Submission directory: `submit/v073_ai_agent_v3_margin445/`
- Baseline: `submit/v071_ai_agent_v3_margin44/`
- Change:
  - `MARGIN_S = 44.0` -> `MARGIN_S = 44.5`

All other attack logic remains unchanged.

## Validation

- Notebook JSON check passed.
- Kernel metadata JSON check passed.
- Local notebook execution generated `attack.py` and placeholder `submission.csv`.
- SDK validate passed on generated `attack.py`.
- Deterministic smoke completed in about `15.1s` with score `0.00`.
- Notebook hash: `048d91ff333d`.
- Generated `attack.py` hash: `e3b480afd95b`.

## Result

- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v073-ai-agent-v3-margin445` version 1.
- Submitted as ref `54492959`.
- Complete with blank public score as of 2026-07-10.
- Treat as no-score / `Submission Format Error` class.

## Interpretation

The slightly safer `MARGIN_S=44.5` setting did not transfer. Do not assume
larger margins are safer in this notebook wrapper; keep `v071=57.825` as the
active best unless `v072` succeeds.

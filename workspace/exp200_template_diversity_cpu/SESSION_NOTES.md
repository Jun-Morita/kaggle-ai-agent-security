# exp200 template diversity CPU

## Hypothesis

Keeping the `v169` mechanics but changing only the terminal wording may provide
a small public shake hedge and private diversity while preserving single-tool
Gemma compatibility.

## Change

- Source: `submit/v169_replay_costcoef095`
- `TEMPLATE` terminal wording changed to `Then answer OK only.`
- `FRAME_TEMPLATE` terminal wording changed to `Then answer OK only.`
- CPU kernel: `junichiromorita/ai-agent-security-v200-template-diversity`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- `aicomp_sdk` redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-30
- Competition ref: `55878860`
- Status at submit time: pending


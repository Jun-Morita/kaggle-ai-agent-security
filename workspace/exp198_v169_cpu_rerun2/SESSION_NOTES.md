# exp198 v169 CPU rerun2

## Hypothesis

`v169` remains the confirmed best at `89.685`, and hosted variance is meaningful.
An exact CPU rerun may sample a better public draw without adding format or
runtime risk.

## Change

- Source: `submit/v169_replay_costcoef095`
- Attack source is byte-identical to `v169`
- Attack SHA-256 prefix: `40dc80e8bdcd`
- CPU kernel: `junichiromorita/ai-agent-security-v198-v169-cpu-rerun2`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- `aicomp_sdk` redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-30
- Competition ref: `55878845`
- Status at submit time: pending


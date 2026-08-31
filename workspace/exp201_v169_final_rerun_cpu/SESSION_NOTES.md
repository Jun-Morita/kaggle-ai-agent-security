# exp201 v169 final rerun CPU

## Hypothesis

`v169=89.685` remains the confirmed post-refresh best. A final exact CPU rerun
may sample hosted variance above the current best without adding code risk.

## Change

- Source: `submit/v169_replay_costcoef095`
- Attack source is byte-identical to `v169`
- Attack SHA-256 prefix: `40dc80e8bdcd`
- CPU kernel: `junichiromorita/ai-agent-security-v201-v169-final-rerun`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- SDK redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-31
- Competition ref: `55915447`
- Status at submit time: pending


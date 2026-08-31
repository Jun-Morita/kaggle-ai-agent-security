# exp199 classify8 CPU balance

## Hypothesis

Discussion evidence suggests scores near `90` can reflect being optimized to one
model. Increasing split classification from `6` to `8` may reduce routing error
and improve the weaker model enough to offset two extra probe calls.

## Change

- Source: `submit/v169_replay_costcoef095`
- Only attack change: `SPLIT_CLASSIFY_N = 8`
- CPU kernel: `junichiromorita/ai-agent-security-v199-classify8-balance`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- `aicomp_sdk` redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-30
- Competition ref: `55878857`
- Status at submit time: pending


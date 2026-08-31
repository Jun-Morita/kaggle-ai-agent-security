# exp197 classify4 CPU

## Hypothesis

`v169` may spend slightly too much time on split classification. Reducing
`SPLIT_CLASSIFY_N` from `6` to `4` could return more fill candidates while still
preserving enough model routing signal.

## Change

- Source: `submit/v169_replay_costcoef095`
- Only attack change: `SPLIT_CLASSIFY_N = 4`
- CPU kernel: `junichiromorita/ai-agent-security-v197-classify4`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- `aicomp_sdk` redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-30
- Competition ref: `55878839`
- Status at submit time: pending


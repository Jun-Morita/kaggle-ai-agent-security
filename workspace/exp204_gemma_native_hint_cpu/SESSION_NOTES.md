# exp204 Gemma native hint CPU

## Hypothesis

Discussion `737781` suggests Gemma failures are tied to malformed or quoted-key
tool-call arguments. A short `bare keys` hint may improve Gemma parser
compatibility while retaining the `v169` single-call structure.

## Change

- Source: `submit/v169_replay_costcoef095`
- `TEMPLATE`: adds `bare keys`
- `FRAME_TEMPLATE`: adds `bare keys`
- Attack SHA-256 prefix: `6af8bb60c353`
- CPU kernel: `junichiromorita/ai-agent-security-v204-gemma-native-hint`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- SDK redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-31
- Competition ref: `55915453`
- Status at submit time: pending


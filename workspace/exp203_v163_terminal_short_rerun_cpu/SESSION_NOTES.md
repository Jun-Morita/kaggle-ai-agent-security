# exp203 v163 terminal short rerun CPU

## Hypothesis

`v163=88.920` is a separate compact terminal branch. It may be less aggressive
than `v169` and therefore useful for shake diversity.

## Change

- Source: `submit/v163_fastfirst_terminal_short`
- Attack source is byte-identical to `v163`
- Attack SHA-256 prefix: `8db3bcf9c275`
- CPU kernel: `junichiromorita/ai-agent-security-v203-v163-terminal-short`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- SDK redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-31
- Competition ref: `55915452`
- Status at submit time: pending


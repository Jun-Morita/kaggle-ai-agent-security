# exp205 deputy tail3 CPU hedge

## Hypothesis

Public LB penalized deputy tails, but private shake risk remains large. Reducing
the tail from 6 to 3 candidates preserves a tiny `CONFUSED_DEPUTY` hedge while
spending less public replay capacity than `v195`.

## Change

- Source: `submit/v195_deputy_tail6_cpu_hedge`
- Only attack change: `DEPUTY_TAIL_N = 3`
- Attack SHA-256 prefix: `30432c2e1d7b`
- CPU kernel: `junichiromorita/ai-agent-security-v205-deputy-tail3`

## Validation

- `py_compile`: passed
- notebook first-cell parity: passed
- metadata JSON: passed
- SDK redteam validation: passed
- hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source

## Submission

- Submitted: 2026-08-31
- Competition ref: `55915455`
- Status at submit time: pending


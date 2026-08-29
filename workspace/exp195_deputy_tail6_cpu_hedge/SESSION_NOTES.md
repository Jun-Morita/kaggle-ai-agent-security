# exp195_deputy_tail6_cpu_hedge

## Hypothesis

Large `CONFUSED_DEPUTY` tails harmed public score, but final/private shake risk
argues against identical final candidates. Keep the `v169` exfil head and shrink
the deputy tail to 6 candidates, smaller than the prior 10/40/160 tails.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v195-deputy-tail6` v1
- Competition ref: `55857886`
- Status: pending as of 2026-08-29 02:39 UTC

## Verification

- `python3 -m py_compile submit/v195_deputy_tail6_cpu_hedge/attack.py`
- SDK `validate redteam` passed.
- Notebook first-cell parity passed.
- Hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source.

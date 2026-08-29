# exp196_costcoef0965_cpu_safe

## Hypothesis

`v169` with `REPLAY_COST_COEF=0.95` remains the best confirmed branch, while
`0.975` underfilled and `0.925` overreached. Test the intermediate safer neighbor
`0.965` for a possible stability/variance gain.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v196-costcoef0965` v1
- Competition ref: `55857889`
- Status: pending as of 2026-08-29 02:39 UTC

## Verification

- `python3 -m py_compile submit/v196_costcoef0965_cpu_safe/attack.py`
- SDK `validate redteam` passed.
- Notebook first-cell parity passed.
- Hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source.

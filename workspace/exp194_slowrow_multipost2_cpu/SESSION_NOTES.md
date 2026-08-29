# exp194_slowrow_multipost2_cpu

## Hypothesis

`v169` is still the best post-refresh baseline, but discussion `737793` suggests
scores near 90 may be optimized too strongly to one model. Keep Gemma on the
single-call path and test a small `SLOW_MULTIPOST_N=2` push only on the
latency-classified slow/Harmony row.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v194-slowrow-multipost2` v1
- Competition ref: `55857877`
- Status: pending as of 2026-08-29 02:39 UTC

## Verification

- `python3 -m py_compile submit/v194_slowrow_multipost2_cpu/attack.py`
- SDK `validate redteam` passed.
- Notebook first-cell parity passed.
- Hosted output contained `attack.py` and `submission.csv`; hosted `attack.py`
  matched local source.

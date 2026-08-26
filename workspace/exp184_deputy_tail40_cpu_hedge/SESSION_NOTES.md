# exp184_deputy_tail40_cpu_hedge

## Hypothesis

`v182` adds a large `CONFUSED_DEPUTY` tail for private shake-down coverage, but
that may cost too much public throughput. Use a smaller `40`-candidate deputy
tail to keep most of the `v169` exfil profile while adding limited predicate
diversity.

## Base

- Base submission: `submit/v182_deputy_tail_cpu_hedge`
- Effective source: `submit/v169_replay_costcoef095` plus a separate
  `CONFUSED_DEPUTY` tail

## Changes

- Change only `DEPUTY_TAIL_N = 160 -> 40` from `v182`.
- Kaggle kernel slug/title changed to
  `junichiromorita/ai-agent-security-v184-deputy-tail40-cpu`.
- Notebook metadata uses `enable_gpu=false`.

## Validation

- `python3 -m py_compile submit/v184_deputy_tail40_cpu_hedge/attack.py`: passed
- Notebook first cell starts with `%%writefile /kaggle/working/attack.py`: passed
- Notebook embedded source equals `attack.py`: passed
- `aicomp validate redteam submit/v184_deputy_tail40_cpu_hedge/attack.py`: passed
- Hosted output contained both `attack.py` and `submission.csv`.
- Attack SHA-256 prefix: `198b4f66dac4`

## Kaggle

- Kernel push: succeeded on 2026-08-26
- Kernel status: `COMPLETE`
- Competition submission: pending, ref `55796580`


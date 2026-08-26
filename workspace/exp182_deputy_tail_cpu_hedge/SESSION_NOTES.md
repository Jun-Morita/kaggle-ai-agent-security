# exp182_deputy_tail_cpu_hedge

## Hypothesis

`v180_v169_deputy_tail_hedge` remained queued and was cancelled. Keep the same
private shake-down hedge idea, but run the output notebook as a CPU kernel to
avoid GPU queue pressure.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Hedge source: `submit/v157_confdeputy_only`
- Cancelled predecessor: `submit/v180_v169_deputy_tail_hedge`

## Changes

- Keep the `v169` live validation-fill exfil head.
- Append up to `160` separate `Notify ...` `CONFUSED_DEPUTY` tail candidates.
- Avoid compound `http.post` + `email.send` messages.
- Kaggle kernel slug/title changed to
  `junichiromorita/ai-agent-security-v182-deputy-tail-cpu`.
- Notebook metadata uses `enable_gpu=false`.

## Validation

- `python3 -m py_compile submit/v182_deputy_tail_cpu_hedge/attack.py`: passed
- Notebook first cell starts with `%%writefile /kaggle/working/attack.py`: passed
- Notebook embedded source equals `attack.py`: passed
- `aicomp validate redteam submit/v182_deputy_tail_cpu_hedge/attack.py`: passed
- Hosted output contained both `attack.py` and `submission.csv`.
- Attack SHA-256 prefix: `1c126f00e6ec`

## Kaggle

- Kernel push: succeeded on 2026-08-26
- Kernel status: `COMPLETE`
- Competition submission: pending, ref `55796398`


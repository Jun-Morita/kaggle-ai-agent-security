# exp181_v169_exact_cpu_rerun

## Hypothesis

`v179_v169_exact_rerun3` remained queued and was cancelled. Since the notebook
only emits `attack.py` and `submission.csv`, rerun the same `v169` attack as a
CPU kernel to avoid GPU queue pressure and sample hosted score variance.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Cancelled predecessor: `submit/v179_v169_exact_rerun3`
- Public score to beat: `89.685`

## Changes

- Attack source is byte-identical to `v169`.
- Kaggle kernel slug/title changed to
  `junichiromorita/ai-agent-security-v181-v169-cpu-rerun`.
- Notebook metadata uses `enable_gpu=false`.

## Validation

- `python3 -m py_compile submit/v181_v169_exact_cpu_rerun/attack.py`: passed
- Notebook first cell starts with `%%writefile /kaggle/working/attack.py`: passed
- Notebook embedded source equals `attack.py`: passed
- `aicomp validate redteam submit/v181_v169_exact_cpu_rerun/attack.py`: passed
- Hosted output contained both `attack.py` and `submission.csv`.
- Attack SHA-256 prefix: `40dc80e8bdcd`

## Kaggle

- Kernel push: succeeded on 2026-08-26
- Kernel status: `COMPLETE`
- Competition submission: pending, ref `55796355`


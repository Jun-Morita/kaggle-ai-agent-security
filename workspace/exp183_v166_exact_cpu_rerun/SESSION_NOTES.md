# exp183_v166_exact_cpu_rerun

## Hypothesis

`v166_terminal_say_ok_direct` is a distinct strong anchor from the current
`v169` best. Exact rerun can sample hosted variance while preserving diversity
against terminal-wording shake.

## Base

- Base submission: `submit/v166_terminal_say_ok_direct`
- Public score to beat: `89.235`
- Current repository best: `v169_replay_costcoef095=89.685`

## Changes

- Attack source is byte-identical to `v166`.
- Kaggle kernel slug/title changed to
  `junichiromorita/ai-agent-security-v183-v166-cpu-rerun`.
- Notebook metadata uses `enable_gpu=false`.

## Validation

- `python3 -m py_compile submit/v183_v166_exact_cpu_rerun/attack.py`: passed
- Notebook first cell starts with `%%writefile /kaggle/working/attack.py`: passed
- Notebook embedded source equals `attack.py`: passed
- `aicomp validate redteam submit/v183_v166_exact_cpu_rerun/attack.py`: passed
- Hosted output contained both `attack.py` and `submission.csv`.
- Attack SHA-256 prefix: `e399e259048b`

## Kaggle

- Kernel push: succeeded on 2026-08-26
- Kernel status: `COMPLETE`
- Competition submission: pending, ref `55796560`


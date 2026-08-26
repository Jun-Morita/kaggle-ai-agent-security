# exp178_replay_costcoef0975_fixed

## Hypothesis

`v177_replay_costcoef0975` was not evaluated because the hosted notebook failed
to emit `attack.py`. The attack idea remains valid to test: return to the proven
`Then say OK.` anchor and use a safer midpoint, `REPLAY_COST_COEF=0.975`, between
the default `1.0` and the current-best `v169` value `0.95`.

## Base

- Base submission: `submit/v177_replay_costcoef0975`
- Effective source: `submit/v169_replay_costcoef095` with
  `REPLAY_COST_COEF=0.975`

## Change

- Preserve the restored notebook `%%writefile /kaggle/working/attack.py` wrapper.
- Keep the `v177` attack logic unchanged.
- Change only the Kaggle kernel id/title relative to `v177`.

## Validation

- Notebook first-cell wrapper check: passed
  (`%%writefile /kaggle/working/attack.py` is present).
- Notebook first cell contains the exact `attack.py` body.
- `UV_CACHE_DIR=/tmp/uv-cache uv run python -m py_compile submit/v178_replay_costcoef0975_fixed/attack.py`: passed.
- `python3 -m json.tool submit/v178_replay_costcoef0975_fixed/kernel-metadata.json`: passed.
- SDK validate: passed.
- Attack SHA-256: `c0ad53ba4863`
- Hosted output check: `attack.py` and `submission.csv` downloaded from kernel
  version 1.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v178-costcoef0975-fixed`
- Version: 1
- Competition submission ref: `55772810`
- Status: complete as of 2026-08-26.
- Public score: `88.785`
- Submit-time quota message: `0 submissions remaining today`.

## Result

The fixed `REPLAY_COST_COEF=0.975` midpoint produced a valid score but remained
below `v169=89.685`. Keep `v169` as the current confirmed post-refresh best and
do not promote this midpoint.

# exp179_v169_exact_rerun3

## Hypothesis

The current best post-refresh family, `v169_replay_costcoef095`, may still have
hosted score variance near the top-10% boundary. This is an exact attack rerun
to sample that upper tail without changing the attack surface.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Public score to beat: `89.685`

## Changes

- Attack source is byte-identical to `v169`.
- Kaggle kernel slug/title changed to
  `junichiromorita/ai-agent-security-v179-v169-rerun3`.

## Validation

- `python3 -m py_compile submit/v179_v169_exact_rerun3/attack.py`: passed
- Notebook first cell starts with `%%writefile /kaggle/working/attack.py`: passed
- Notebook embedded source equals `attack.py`: passed
- `aicomp validate redteam submit/v179_v169_exact_rerun3/attack.py`: passed
- Attack SHA-256 prefix: `40dc80e8bdcd`

## Kaggle

- Kernel push: succeeded on 2026-08-26
- Kernel status after repeated polling: `QUEUED`
- Final kernel status after user stopped it: `CANCEL_ACKNOWLEDGED`
- Competition submission: not submitted.
- Superseded by CPU-kernel resubmission `v181_v169_exact_cpu_rerun`.

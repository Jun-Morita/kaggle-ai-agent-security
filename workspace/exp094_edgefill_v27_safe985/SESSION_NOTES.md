# exp094_edgefill_v27_safe985

## Hypothesis

EdgeFill v27 may improve over `v092=81.540` by reclaiming replay budget through a two-stage template race, rolling failover, and a small bounded tail.

## Source

- Public reference: `devchandra/ai-agent-security-v80-...`
- Extracted source: `/tmp/aas-code-20260718/extracted/devv80.py`
- Replay safety: `REPLAY_SAFE = 0.985`

## Implementation

- Uses EdgeFill v27 logic unchanged for this variant.
- Keeps the existing repo Kaggle notebook wrapper that writes `/kaggle/working/attack.py` and creates placeholder `submission.csv` outside competition rerun.

## Validation

- `python3 -m py_compile submit/v094_edgefill_v27_safe985/attack.py`
- SDK `validate redteam submit/v094_edgefill_v27_safe985/attack.py`: passed.
- SDK deterministic smoke, 60s: completed in about 38.2s with score `0.00`.
- Notebook validation with `nbformat.validate`: passed.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v094-edgefill-v27-safe985` version 1.
- Competition submission ref: `54808441`.
- Status: `PENDING` as of 2026-07-18 22:09 JST.

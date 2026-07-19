# exp095_adaptive_density_ladder_exact

## Hypothesis

The public `tetsutani/ai-agent-security-adaptive-tool-call-throughput-se` notebook scored `86.175`, above our confirmed best `v093=84.600`. Its main difference is not blind multi-post stacking, but guarded score-density selection across one-call, two-call, and three-call candidates with exact-fire qualification and rollback.

## Source

- Public reference: `tetsutani/ai-agent-security-adaptive-tool-call-throughput-se`
- Extracted source: `/tmp/aas-kernel-analysis-20260719/tetsutani_attack.py`
- Extracted source SHA-256 prefix: `a57847310bfd`
- Variant name in source: `v136_adaptive_score_density_ladder`

## Implementation

- Use the public attack logic unchanged for the first attempt.
- Keep the repo's proven Kaggle notebook wrapper that writes `/kaggle/working/attack.py` and placeholder `submission.csv`.
- Kernel slug shortened to avoid previous long-slug submission issues.

## Validation

- `python3 -m py_compile submit/v095_adaptive_density_ladder_exact/attack.py workspace/exp095_adaptive_density_ladder_exact/attack.py`
- SHA-256 exact match with extracted public source: `a57847310bfda7e1f544a7c76b0ce2968c1173bfc067ebe0a065f6e68c96e570`
- Notebook validation with `nbformat.validate`: passed.
- SDK `validate redteam submit/v095_adaptive_density_ladder_exact/attack.py`: passed.
- SDK deterministic smoke, 60s: completed in about 0.5s with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v095-density-ladder` version 1.
- Competition submission ref: `54831375`.
- Status: `PENDING` as of 2026-07-19 22:03 JST.

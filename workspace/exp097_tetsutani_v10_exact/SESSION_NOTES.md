# exp097_tetsutani_v10_exact

## Hypothesis

The visible public `86.175` on `tetsutani/ai-agent-security-adaptive-tool-call-throughput` belongs to version 10, not the later `v136` source used by `v095`. Exact-porting the version 10 attack should be a better reproduction target than `v095=73.980`.

## Source

- Public reference: `tetsutani/ai-agent-security-adaptive-tool-call-throughput`
- Best version: version 10, scriptVersionId `336277426`
- Public reference score: `86.175`
- Source variant: `v134_hybrid_single_dual_gate`
- Extracted source SHA-256 prefix: `91d5cf0edb92`

## Implementation

- Keep the attack logic unchanged.
- Use the repo's proven notebook wrapper that writes `/kaggle/working/attack.py` and a placeholder `submission.csv` outside competition rerun.
- Kernel slug: `junichiromorita/ai-agent-security-v097-tetsutani-v10`.

## Validation

- `python3 -m py_compile submit/v097_tetsutani_v10_exact/attack.py workspace/exp097_tetsutani_v10_exact/attack.py`: passed.
- SHA-256 exact match with extracted version 10 source: `91d5cf0edb92b364197ce41b836d797dfc8a693c5ac5347a06ba8df25a858e97`.
- Notebook validation with `nbformat.validate`: passed.
- SDK `validate redteam submit/v097_tetsutani_v10_exact/attack.py`: passed.
- SDK deterministic smoke, 60s: completed in about 0.7s with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v097-tetsutani-v10` version 1.
- Competition submission ref: `54842840`.
- Status: `PENDING` as of 2026-07-20 10:59 JST.

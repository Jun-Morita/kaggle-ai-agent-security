# exp098_yusuke_v52_exact

## Hypothesis

`yusuketogashi/ai-agent-sec-another-approach` version 52 has a recorded public score of `85.635`, slightly above our current confirmed best `v093=84.600`. Exact-porting this version gives a low-risk fallback candidate while `v097` is pending.

## Source

- Public reference: `yusuketogashi/ai-agent-sec-another-approach`
- Best version used: version 52, scriptVersionId `335827283`
- Public reference score: `85.635`
- Source header: `R1-009`, `RELAY PUSH100`
- Extracted source SHA-256: `3498266bd9a91cfdd4723a7357cb5dbb8bdea186cf8725402b1efc5a49116128`

## Implementation

- Keep the attack logic unchanged.
- Use the repo's proven notebook wrapper that writes `/kaggle/working/attack.py` and a placeholder `submission.csv` outside competition rerun.
- Kernel slug prepared: `junichiromorita/ai-agent-security-v098-yusuke-v52`.

## Validation

- `python3 -m py_compile submit/v098_yusuke_v52_exact/attack.py workspace/exp098_yusuke_v52_exact/attack.py`: passed.
- SHA-256 exact match with extracted version 52 source: `3498266bd9a91cfdd4723a7357cb5dbb8bdea186cf8725402b1efc5a49116128`.
- Notebook validation with `nbformat.validate`: passed.
- SDK `validate redteam submit/v098_yusuke_v52_exact/attack.py`: passed.
- SDK deterministic smoke, 60s: completed in about 0.5s with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v098-yusuke-v52` version 1.
- Competition submission ref: `54842998`.
- Status: `PENDING` as of 2026-07-20 11:13 JST.

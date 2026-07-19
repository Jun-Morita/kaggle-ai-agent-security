# exp096_density_ladder_margin150

## Hypothesis

`v095` exact-ports the public tetsutani density ladder with `MARGIN_S = 180.0`. If that reserve stops generation before the replay ledger is full, lowering the fixed reserve to `150.0` can return a few more validated candidates while preserving the conservative replay cap and qualification logic.

## Source

- Parent: `workspace/exp095_adaptive_density_ladder_exact/`
- Public reference: `tetsutani/ai-agent-security-adaptive-tool-call-throughput-se`, public `86.175`

## Implementation

- Single-knob change: `MARGIN_S = 180.0 -> 150.0`.
- Also updates `VARIANT_ID` / `VARIANT_NAME` for stderr identification.
- No prompt, payload, URL, replay ledger, holdout, exact matching, or fallback changes.

## Validation

- `python3 -m py_compile submit/v096_density_ladder_margin150/attack.py workspace/exp096_density_ladder_margin150/attack.py`
- Diff from `v095`: only `VARIANT_ID`, `VARIANT_NAME`, and `MARGIN_S = 180.0 -> 150.0`.
- Notebook validation with `nbformat.validate`: passed.
- SDK `validate redteam submit/v096_density_ladder_margin150/attack.py`: passed.
- SDK deterministic smoke, 60s: completed in about 0.4s with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v096-density-margin150` version 1.
- Competition submission ref: `54831468`.
- Status: `PENDING` as of 2026-07-19 22:08 JST.

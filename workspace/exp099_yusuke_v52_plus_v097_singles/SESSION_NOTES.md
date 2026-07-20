# exp099_yusuke_v52_plus_v097_singles

## Hypothesis

`v098` has a clean replay ledger and public reference `85.635`, while `v097` includes useful single-post challenger prompts. Adding only the single-post challengers to the `v098` effective-cost selector may find a faster firing template without taking on dual-post replay cost.

## Implementation

- Start from `v098_yusuke_v52_exact`.
- Add `v097` single-post arms:
  - `call_syntax`
  - `bare_min`
  - `post_short`
  - `inj_empty`
  - `inj_done`
- Do not add `double_plain`, `double_bare`, or `double_call`.
- Keep `REPLAY_SAFE=0.99`, `PROBE_REPS=5`, `MIN_FIRE_RATE=0.2`, `MARGIN_S=60.0`, and summed measured replay-cost cap unchanged.

## Validation

- `python3 -m py_compile submit/v099_yusuke_v52_plus_v097_singles/attack.py workspace/exp099_yusuke_v52_plus_v097_singles/attack.py`: passed.
- Source attack SHA-256: `db02caee28110933deb25b1335d9182ae408bc9920f97abb0cff792eba137c8a`.
- Notebook validation with `nbformat.validate`: passed.
- SDK `validate redteam submit/v099_yusuke_v52_plus_v097_singles/attack.py`: passed.
- SDK deterministic smoke, 60s: completed in about 0.5s with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v099-v52-singles` version 1.
- Competition submission ref: `54843094`.
- Status: `PENDING` as of 2026-07-20 11:20 JST.

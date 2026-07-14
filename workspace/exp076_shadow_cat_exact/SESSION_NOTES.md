# exp076 Shadow Cat Exact

## Hypothesis

The current highest-scoring public reference will outperform the local v071
implementation by using a complete replay-reserved live-validation fill design:
an untimed warm-up, a successful-event filter, and a conservative 49-second
deadline reserve.

## Implementation

- Submission: `submit/v076_shadow_cat_exact/`
- Source: `references/raw/notebooks/shadow-cat-firewall.ipynb`
- Attack logic changes: none.
- Compatibility-only change: disable GPU and Internet in Notebook metadata.

## Validation Plan

- Build the Notebook's generated `attack.py` in an isolated temporary working
  directory.
- Run Python syntax, SDK validation, and the deterministic red-team smoke test.
- Confirm normal-run artifacts contain both `attack.py` and `submission.csv`.

## Decision

Submitted independently from v077 as ref `54556021`; complete with public score
`54.740`. Do not blend this single-post fill with the v074 multipost or v075
diversity branches.
The hosted `attack.py` matches the locally validated source exactly
(`5b0b44ed2764`).

## Retrospective

The saved source is Shadow Cat v15. A current public pull on 2026-07-12 showed
v16 uses different attack code (`499ed856821c`) with adaptive multi-post fill.
The displayed public `63.650` score is therefore not a v15 reproduction target.

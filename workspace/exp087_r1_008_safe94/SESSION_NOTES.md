# exp087 R1-008 Safe94

## Hypothesis

`v085` improved the repo best to public `63.495` by adopting replay-cost-capped
JED fill v26. Current public Code suggests the next single-message frontier is
the same design with a slightly more aggressive replay cap and more template
choices.

## Source

- Public Code: `yusuketogashi/ai-agent-sec-another-approach`
- Pulled: 2026-07-16
- Extracted source hash: `5954b90db346`
- Saved raw notebook:
  `references/raw/notebooks/ai-agent-sec-another-approach-20260716.ipynb`

## Implementation

Close source transfer of public `R1-008`:

- `REPLAY_SAFE = 0.94`
- `PROBE_REPS = 3`
- `MIN_FIRE_RATE = 0.6`
- adds `bare`, `bare_ok`, and `call_syntax` templates to the `v085` template
  bank
- preserves measured replay-cost capping and fail-closed predicate validation

## Expected Outcome

This is the most direct score-up candidate from `v085`: it keeps the same
successful family but spends more replay budget and can select faster templates
per model. Risk is higher than `v085` but lower than `dhanvin`'s `REPLAY_SAFE=0.99`
variant.

## Validation

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: completed in about `0.6s`, score `0.00`.
- Notebook embedded source hash matched `workspace/exp087_r1_008_safe94/attack.py`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v087-r1-008-safe94` version 1
- Competition submission ref: `54761706`
- Status: pending as of 2026-07-16

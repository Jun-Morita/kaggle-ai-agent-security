# exp147_v140_three_arm_race

## Hypothesis

The current post-refresh best `v140=87.705` uses a two-arm template race between
the plain imperative prompt and the verbose Harmony-close frame. Public Dimong4
v16 suggests a shorter Harmony frame can be competitive. Instead of replacing
the proven `v140` frame entirely, test a three-arm race that keeps the same
six-message classifier budget and chooses among plain, verbose Harmony, and
short Harmony templates.

## Source

- Base: `submit/v128_template_race` / `v140_v128_template_race_postrefresh_rerun`
- Graft source: `dimong4/ai-agent-security` v16, scriptVersionId `339219173`
- Related submissions: `v145_dimong4_v16_exact`, `v146_v140_short_frame_graft`

## Implementation

- Copied `submit/v128_template_race` to `submit/v147_v140_three_arm_race`.
- Added `SHORT_FRAME_TEMPLATE` from Dimong4 v16.
- Preserved `SPLIT_CLASSIFY_N = 6`, `REPLAY_SAFE_FRAC = 0.975`,
  `PROBE_HOPS = 0`, and `SLOW_MULTIPOST_N = 1`.
- Changed the classifier from a 3+3 two-arm race to a 2+2+2 three-arm race.
- Updated kernel slug to `junichiromorita/ai-agent-security-v147-three-arm-race`.

## Expected Readout

- If `v147 > v140`, the short Harmony frame is useful as a conditional arm, even
  if direct replacement in `v146` is inconclusive.
- If `v147 <= v140`, the extra arm likely adds classifier noise; keep `v140` as
  the post-refresh baseline.

## Validation

- `python3 -m py_compile submit/v147_v140_three_arm_race/attack.py`: passed.
- Notebook JSON and kernel metadata JSON validation: passed.
- `aicomp_sdk.cli.main validate redteam`: passed.
- Deterministic smoke: completed in about 51.5s with score `0.00`.

## Submission

- 2026-08-13: local Kaggle push from Codex was blocked by approval review before
  external upload.
- Status: prepared, not yet submitted.

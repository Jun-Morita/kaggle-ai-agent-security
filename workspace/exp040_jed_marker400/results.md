# exp040 JED marker400

## Hypothesis

After the evaluator update, old classic replay-dense candidates no longer score,
but low-overhead JED-style `SECRET_MARKER` single-post candidates may still
score and scale to `N=400`.

## Source

- `submit/v038_jed_attack_improved_nb`
- Kaggle discussion `712642` evaluator update and comments

## Design

- Copy the v038 JED baseline.
- Change only candidate count from `100` to `400`.
- Keep one short prompt and one unique host per candidate.

## Result

- Kaggle kernel: `junichiromorita/ai-agent-security-v040-jed-marker400`
- Kaggle kernel version: `1`
- Submission ref: `54044490`
- Kaggle status: `COMPLETE` as of 2026-06-26
- Public LB: none / blank
- Local deterministic score: `0.00`
- Local deterministic runtime: about 22.7s
- Static return count: `400`
- Notes: py_compile, ruff, SDK validate, deterministic smoke passed.
- Hosted result completed with blank public score. Treat this as replay timeout
  / no-score; do not scale JED directly to 400 in this wrapper.

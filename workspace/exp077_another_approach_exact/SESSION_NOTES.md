# exp077 Another Approach Exact

## Hypothesis

This is the controlled v076 companion. Both references use the same
single-post, validated-fill family, but v077 retains the source's 45-second
reserve rather than v076's 49-second reserve. The comparison will test the
runtime margin without mixing in a different prompt or replay shape.

## Implementation

- Submission: `submit/v077_another_approach_exact/`
- Source: `references/raw/notebooks/ai-agent-sec-another-approach.ipynb`
- Attack logic changes: none.
- Compatibility-only change: disable GPU and Internet in Notebook metadata.

## Validation Plan

- Build the generated `attack.py` in isolation.
- Run syntax, SDK validation, and deterministic red-team smoke checks.
- Confirm the normal-run `submission.csv` has the required four evaluation IDs.

## Decision

Submitted independently from v076 as ref `54556032`; status `PENDING`. The only
intended behavioral difference is the source notebook's runtime reserve
implementation.
The hosted `attack.py` matches the locally validated source exactly
(`5b8d4f71864c`).

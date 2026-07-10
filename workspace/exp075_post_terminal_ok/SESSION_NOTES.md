# exp075 Post Terminal OK

## Hypothesis

The compact terminal instruction can reduce the unscored final-response tokens
per single-post candidate. This is an independent alternative to the v074
adaptive multipost mechanism.

## Implementation

- Submission directory: `submit/v075_post_terminal_ok/`
- Source: public `assiaben/jed-attack-post-one-word-terminal-ok`
- Intentional attack-logic changes: none.
- Not pushed or submitted.

## Wrapper Review

The downloaded source called `JEDAttackInferenceServer().serve()` unconditionally
and did not create `submission.csv` for a normal commit run. The wrapper was
changed without touching the embedded attack code:

- create `attack.py` and placeholder `submission.csv` on a normal run;
- start the inference server only when `KAGGLE_IS_COMPETITION_RERUN` is set.

Static inspection also confirms a 180-second diversity-probe allocation before
the primary live validation fill. Downloaded source SHA-256:
`967f99c3d9a112f15f2ef74b77842a7e08aaed51fdc28d9b4ffd3ac48b346149`.
Candidate notebook SHA-256 after the wrapper-only change:
`78e7378c175b53b888bc7a0bf4294af44f466c35052d5a54032f2a699e2cad80`.

## Validation

- Isolated notebook build passed.
- SDK validate passed for the generated `attack.py`.
- Deterministic smoke completed in `36.2s` with score `0.00`; this is a
  wiring-only result for the deterministic agent.
- Generated `attack.py` SHA-256:
  `44711a7ce898ac7581152abbf9766f4ca143e16cd8f5f4b3bbe19cda10c76cdf`.

## Decision Gate

Validate the wrapper separately from v074. Do not combine the terminal prompt
with v074's adaptive multipost branch in the first test.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v075-post-terminal-ok` v1.
- Submission ref: `54527543`.
- Status: `PENDING` as of 2026-07-10.

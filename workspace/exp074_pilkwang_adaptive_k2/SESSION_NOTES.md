# exp074 Pilkwang Adaptive K2

## Hypothesis

`v071` establishes the live-validated single-post path at public `57.825`.
The latest public v3.1.2 notebook adds a conditional rather than unconditional
multi-post branch: it measures the early single-post latency and asks only the
slow path to send to multiple distinct endpoints. The candidate is retained
only if at least two marker-bearing posts appear in the live trace.

This can increase the score per slow-model generation without spending the
same replay budget on fast-model candidates.

## Implementation

- Submission directory: `submit/v074_pilkwang_adaptive_k2/`
- Source: latest public `pilkwang/ai-agent-v3-1-2-single-post-exfiltration`
- Intentional changes to attack logic: none.
- Not pushed or submitted.

## Validation Plan

- Check notebook JSON and kernel metadata.
- Execute the notebook build path locally.
- Validate the generated `attack.py` with the SDK.
- Run deterministic smoke only as a wiring check.

## Static Validation

- Notebook JSON and kernel metadata are valid.
- Static inspection confirms the source uses `MARGIN_S = 42.0`, eight early
  single-post latency probes, a `17.0` second routing threshold, and a
  two-post minimum for the slow-path candidate.
- The normal notebook path writes a placeholder `submission.csv`; the scored
  rerun starts `JEDAttackInferenceServer` only when the competition-rerun
  environment variable is present.
- Notebook SHA-256:
  `ebe5817e3c4414788c762585f0b6288f9dde20439ad76eddb51a16225757dcd6`.
- The isolated notebook build completed after normalizing only the temporary
  copy's `nbformat_minor` from `4` to `5`; the submitted source file was not
  changed.
- Generated `attack.py` SHA-256:
  `603d46813017d002d892d03e30b2536303ac55fe69199ce33da93bc79da873b9`.
- SDK validate passed.
- Deterministic smoke completed in `15.2s` with score `0.00`, as expected for
  a wiring check against the deterministic agent.

## Decision Gate

- Submit only after local generation and SDK validation succeed.
- Do not mix a tail, a margin change, or another prompt family into this
  first transfer.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v074-pilkwang-adaptive-k2` v1.
- Submission ref: `54527586`.
- Status: `PENDING` as of 2026-07-10.
- The initial code-submit API call returned `400` before the kernel output was
  visible. After verifying hosted `attack.py` and `submission.csv`, one retry
  created the pending submission.

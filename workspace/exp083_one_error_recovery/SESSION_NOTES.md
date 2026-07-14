# exp083 One Error Recovery

## Hypothesis

`v079` remains the best confirmed baseline. Recent discussion and our `v082`
rerun show that hosted evaluation can fail or interrupt without a code change.
The current public `Another Approach` notebook adds one small robustness change:
tolerate a single transient interaction exception before aborting the live-fill
loop.

## Implementation

- Base: `workspace/exp079_security_eval_baseline_exact/attack.py`
- Prompt: unchanged from `v079`.
- Runtime settings: unchanged from `v079`.
- Change:
  - add `MAX_TRANSIENT_ERRORS = 1`
  - on one `env.interact` exception, update `slowest` and continue
  - abort only after the second consecutive transient error

## Risk

Low. This does not change the replay prompt, payload, URL style, or deadline
parameters. It can only help if the hosted generation phase has a transient row
failure before the useful candidate budget is exhausted.

## Validation

- Ruff passed.
- SDK `validate redteam` passed.
- Deterministic smoke completed with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v083-one-error` v1
- Submission ref: `54689109`
- Status: `PENDING` as of 2026-07-14.

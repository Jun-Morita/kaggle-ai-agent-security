# exp174_sayok_costcoef0925

## Hypothesis

`v166_terminal_say_ok_direct` showed that `Say OK.` beats `Then say OK.` as a
static terminal phrase, while `v169` showed that `REPLAY_COST_COEF=0.95` improves
candidate count on the `Then say OK.` anchor. `v172` combines those at `0.95` and
is pending. This experiment pushes the same `Say OK.` anchor one replay-cost rung
further to `0.925`.

## Base

- Base submission: `submit/v172_sayok_costcoef095`
- Related static anchor: `v166_terminal_say_ok_direct=89.235`
- Related sizing anchor: `v169_replay_costcoef095=89.685`

## Change

- Keep static `Say OK.` plain/frame templates.
- Keep `REPLAY_SAFE_FRAC=0.985`.
- Keep adaptive terminal router absent.
- Change only:
  - `REPLAY_COST_COEF=0.95`
  - to `REPLAY_COST_COEF=0.925`

## Risk

- Higher risk than `v173` because `v172` has not scored yet.
- If `Say OK.` replay behavior is slower than `Then say OK.`, the extra optimism
  can underperform.

## Validation

- `python3 -m py_compile`: passed.
- `python3 -m json.tool submit/v174_sayok_costcoef0925/kernel-metadata.json`: passed.
- Notebook first-cell parity with `attack.py`: passed.
- SDK validate: passed.
- SDK deterministic smoke completed in 41.3s with 0 findings, as expected for
  this deterministic local agent.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v174-sayok-costcoef0925` v1.
- Competition submission ref: `55743466`.
- Status at submission time: pending.
- Remaining daily submissions after submit: `3`.

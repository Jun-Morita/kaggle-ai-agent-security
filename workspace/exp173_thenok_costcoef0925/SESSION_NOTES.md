# exp173_thenok_costcoef0925

## Hypothesis

`v169_replay_costcoef095` improved the `Then say OK.` anchor to public `89.685`.
The current top-10% boundary moved to `89.830`, so a small additional candidate
count increase may be enough to recover the medal boundary. This experiment keeps
the proven `v169` shape and pushes replay-cost optimism one rung further.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Confirmed base public score: `89.685`

## Change

- Keep `Then say OK.` plain/frame templates.
- Keep `REPLAY_SAFE_FRAC=0.985`.
- Change only:
  - `REPLAY_COST_COEF=0.95`
  - to `REPLAY_COST_COEF=0.925`

## Risk

- More candidates may push replay too far if this hosted draw is slower.
- This is a boundary probe; high variance is expected near the replay budget edge.

## Validation

- `python3 -m py_compile`: passed.
- `python3 -m json.tool submit/v173_thenok_costcoef0925/kernel-metadata.json`: passed.
- Notebook first-cell parity with `attack.py`: passed.
- SDK validate: passed.
- SDK deterministic smoke completed in 41.0s with 0 findings, as expected for
  this deterministic local agent.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v173-thenok-costcoef0925`.
- Version 1 status: pushed, stayed `QUEUED` too long, then stopped.
- Version 1 final status after stop: `CANCEL_ACKNOWLEDGED`.
- Version 2 status: re-pushed, still `QUEUED` after polling.
- Competition submission: not submitted yet because `submission.csv` output is
  unavailable until the kernel completes.

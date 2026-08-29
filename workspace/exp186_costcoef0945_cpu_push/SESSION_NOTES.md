# exp186_costcoef0945_cpu_push

## Hypothesis

`v169=89.685` is the current best at `REPLAY_COST_COEF=0.95`.  The wider
`0.925` push collapsed while `0.975` under-filled, so test the close optimistic
neighbour `0.945` without changing prompt or live validation logic.

## Change

- Base: `v181_v169_exact_cpu_rerun`.
- Only attack behavior change: `REPLAY_COST_COEF=0.945`.
- CPU notebook wrapper retained.


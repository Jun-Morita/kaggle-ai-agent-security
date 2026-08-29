# exp187_costcoef0955_cpu_safe

## Hypothesis

The upper side of the `v169=0.95` replay-cost estimate has only been tested at
`0.975`.  `0.955` may trade a few late candidates for a more stable replay
boundary without the larger under-fill seen at `0.975`.

## Change

- Base: `v181_v169_exact_cpu_rerun`.
- Only attack behavior change: `REPLAY_COST_COEF=0.955`.
- CPU notebook wrapper retained.


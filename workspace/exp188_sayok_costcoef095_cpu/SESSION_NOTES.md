# exp188_sayok_costcoef095_cpu

## Hypothesis

`Say OK.` is a distinct terminal anchor from `v166=89.235`, but its exact CPU
rerun underperformed.  Combine that anchor with the best `v169` replay-cost
estimate (`0.95`) while keeping it isolated instead of mixing anchors, which
was negative in `v185=87.975`.

## Change

- Base: `v181_v169_exact_cpu_rerun`.
- `TEMPLATE` and `FRAME_TEMPLATE` use `Say OK.`.
- `REPLAY_COST_COEF=0.95`.


# exp190_legacy_slowframe_graft_cpu

## Hypothesis

The old public-Silver `v120`/`v123` family used a longer Harmony-close terminal
in its slow-model frame, while the post-refresh `v169` best uses the compact
`Then say OK.` terminal for both templates.  The direct old-family rerun
`v137=85.590` is not viable, but it changes several other components at once.

Restore only the old slow-frame terminal in the `v169` base:

- ordinary template: keep post-refresh `Then say OK.`;
- Harmony slow template: restore old `Then answer OK only.`;
- sizing, 3+3 template race, ordering, and `REPLAY_COST_COEF=0.95`: keep `v169`.

This isolates the one legacy mechanism that was never evaluated in that modern
throughput envelope and avoids the negative mixed-anchor frontload from v185.

## Validation Plan

- Python compile, kernel metadata JSON, first-cell notebook parity, SDK validate.
- Confirm hosted `attack.py` and `submission.csv` before competition submission.

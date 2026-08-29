# exp189_deputy_tail10_cpu_hedge

## Hypothesis

The 40-candidate deputy tail in `v184=84.480` hurt public throughput.  A
10-candidate tail keeps almost all of the successful `v169` exfil head while
retaining a minimal predicate-diversity and private-guardrail hedge.

## Change

- Base: `v184_deputy_tail40_cpu_hedge`.
- Only attack behavior change: `DEPUTY_TAIL_N=10`.
- CPU notebook wrapper retained.

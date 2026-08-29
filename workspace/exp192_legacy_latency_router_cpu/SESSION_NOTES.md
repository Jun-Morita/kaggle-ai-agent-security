# exp192_legacy_latency_router_cpu

## Hypothesis

The old public-Silver `v123` implementation chose the Harmony slow frame from
six ordinary-probe mean latency. `v169` instead races three ordinary and three
framed probes. Restore only the old routing rule while retaining `v169` prompt
strings, replay sizing, coefficient, and returned-candidate ordering.


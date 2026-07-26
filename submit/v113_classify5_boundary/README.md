# v110_kaiwalya_classify6

Small latency-only variant of the current best public-source transfer.

- Source: `kaiwalyaatulraut/ai-agent-security-solution` version 9
- Public source score: `89.055`
- Source scriptVersionId: `337445891`
- Baseline: `v106_kaiwalya_solution_v9_exact` scored `88.110` in this repo.
- Strategy: keep the live validation-fill / replay-safe single-hop `SECRET_MARKER` family, with no multipost or payload change.
- Change: `SPLIT_CLASSIFY_N=8 -> 6` to reduce slow-row plain-template classification overhead less aggressively than failed `v109` (`4`).
- Risk: smaller classification sample may still destabilize hosted replay, but this is a bounded middle rung between successful `8` and failed `4`.

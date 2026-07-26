# v109_kaiwalya_classify4

Small latency-only variant of the current best public-source transfer.

- Source: `kaiwalyaatulraut/ai-agent-security-solution` version 9
- Public source score: `89.055`
- Source scriptVersionId: `337445891`
- Baseline: `v106_kaiwalya_solution_v9_exact` scored `88.110` in this repo.
- Strategy: keep the live validation-fill / replay-safe single-hop `SECRET_MARKER` family, with no multipost or payload change.
- Change: `SPLIT_CLASSIFY_N=8 -> 4` to reduce slow-row plain-template classification overhead before switching to the Harmony frame.
- Risk: fewer classification probes could misclassify borderline hosted runs, but the known slow/fast split is wide enough that this is a bounded latency test.

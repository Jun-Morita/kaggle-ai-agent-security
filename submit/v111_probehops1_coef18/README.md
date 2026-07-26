# v111_probehops1_coef18

Probe-latency experiment based on the current best public-source transfer.

- Source: `kaiwalyaatulraut/ai-agent-security-solution` version 9
- Public source score: `89.055`
- Source scriptVersionId: `337445891`
- Baseline: `v106_kaiwalya_solution_v9_exact` scored `88.110` in this repo.
- Strategy: keep the live validation-fill / replay-safe single-hop `SECRET_MARKER` family, with no multipost, payload, or classification change.
- Change: `PROBE_HOPS=0 -> 1` and `REPLAY_COST_COEF=1.0 -> 1.8`.
- Rationale: Discussion evidence says remaining headroom is latency. Probing at one hop skips scoring-irrelevant wrap-up generation during fill while charging each kept candidate conservatively for replay.
- Risk: if `1.8` underestimates hosted replay cost, the returned set can exceed replay envelope and blank.

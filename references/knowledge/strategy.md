# Strategy Notes

提出結果、公開 notebook、discussion、ユーザー提供の助言から抽出した方針メモ。

## 2026-06-15: Post-v008/v009 Strategy

### Current Evidence

- `v005_trajectory_exfil_aggressive`: public `27.150`, completed.
- `v006_trajectory_exfil_multipost`: timeout.
- `v007_fast_aggressive_fill`: timeout.
- `v008_timeout_safe_multipost`: public `9.220`.
- `v009_exfil_mass_shift`: timeout.
- `v010_replay_dense_boundary`: pending.
- `v011_single_breadth_500`: pending.

The public single-post scaling rule continues to explain confirmed scores:

```text
score ~= successful_single_post_exfil_findings * 18 / 200
      ~= successful_single_post_exfil_findings * 0.09
```

`v008` scored close to the expected single-post value for 96 candidates, not to a multi-post multiplier. Treat hosted replay as effectively one scoring `http.post` per candidate unless public GGUF validation shows otherwise.

### Decisions

- Pause multipost development.
- Prioritize single-hop breadth with direct `http.post` prompts, unique domains, and short message chains.
- Use public GGUF validation before the next competition submission.
- Measure per-model validation rate, finding count, unique cell count, and wall time rather than relying on deterministic smoke score.
- Keep `sk_live_test` as the main private-hedge payload because it avoids obvious keyword wrappers such as `TOKEN`, `PASSWORD`, or `SECRET_API_KEY`.

### Next Submission Gate

Do not submit v012 until at least one of these is true:

- `v010` / `v011` Public LB results identify a safe candidate-count boundary.
- `exp011_aas_local_validation` produces model-specific public scores and timing that justify a candidate-count choice.

When choosing v012:

- If v010/v011 complete and validation rate is high, tune candidate count near the highest completed boundary.
- If public validation is high but competition submission times out, reduce candidate count or message length.
- If public validation is low, adjust prompt wording before scaling candidate count.
- If `gpt_oss` and `gemma` diverge sharply, choose a prompt set that balances both models instead of overfitting one.

### Final Submission Portfolio

Do not use both final slots for the same public-only EXFILTRATION trick unless private evidence changes.

Preferred portfolio:

- Slot A: best public single-hop breadth EXFILTRATION submission.
- Slot B: private-robust mixed strategy with `sk_live_test`, exfil diversity, confused-deputy coverage, and any verified lower-volume non-exfil predicate.

Rationale: private guardrail may inspect data payloads more strictly than public `OptimalGuardrail`; a pure neutral-URL public exfil strategy could collapse on private.

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

## 2026-06-16: v010 Becomes Current Baseline

### New Results

- `v010_replay_dense_boundary`: public `36.000`, complete, current best.
- `v011_single_breadth_500`: public `32.370`, complete.
- `exp011_aas_local_validation`:
  - v010 gpt_oss local public score `56.050`, 600 findings, 597 unique cells, wall time `2978.1s`
  - v011 gpt_oss local public score `51.350`, 500 findings, 487 unique cells, wall time `2968.4s`
  - both validation kernels failed when loading Gemma GGUF, so Gemma local public score is missing

### Interpretation

- v010 is the public baseline to beat.
- v011 shows that bigger returned breadth alone can underperform if validation rate, prompt mix, or model balance worsens.
- gpt_oss-only validation overpredicts Public LB. Public LB is likely constrained by Gemma behavior.
- If the displayed Public LB is a mean over public model rows, implied Gemma public scores are roughly `15.95` for v010 and `13.39` for v011. Treat this as an inference until Gemma validation works.

### Next Direction

- Keep v010's single-hop, short-message, low-search shape.
- Improve Gemma-followable prompt wording instead of increasing candidate count.
- Fix or bypass the Gemma GGUF validation failure before trusting local public validation as a hard gate.

## 2026-06-16: Public 45 Single-760 Notebook

### New Evidence

- Public notebook `Multi Endpoint Severity Stacker` reports public score `45`.
- Its implementation is actually `Single-post N=760`, not a successful multi-endpoint severity stacker.
- It keeps the v010-safe profile shape:
  - one endpoint per message
  - max hops `1`
  - max search `60s`
  - max verified `60`
  - max message chars `400`
- It scales only the breadth:
  - `guide16_single_600`: target `600`, min `400`, static fallback `300`
  - `single_760`: target `760`, min `500`, static fallback `380`

### Interpretation

- v011 underperformed because its `single_breadth_500` profile changed more than just candidate count: longer search, larger messages, and different fallback shape.
- The better public direction is to keep v010's short replay-dense profile and raise target count.
- Public `45` corresponds to roughly `500` successful single-post findings on average, so the profile is not reaching its full `760` theoretical ceiling.

### Next Direction

- Prepare v012 as a close port of `single_760`.
- Treat it as a public-LB attempt, not as a complete private strategy.
- Keep a separate private-robust final candidate family, because this notebook remains public exfil-scale optimization.

## 2026-06-16: Public 52.2 Replay-Dense Candidate

### New Evidence

- Public notebook `AI Agent: Replay-Dense Exfiltration` reports public score `52.2`.
- Its selected profile is `guide22_c580`:
  - target `800`
  - min return `580`
  - static fallback `400`
  - max verified `60`
  - max search `60s`
  - max message chars `260`
  - max hops `1`
  - safe target factor `0.88`
- Public notebook `Replay Dense Boundary Exact + Aggressive` reports public score `46.8`.
- Its selected profile `guide23_semanticboost800` keeps the same numeric settings but increases semantic-audit variant density.

### Interpretation

- `guide22_c580` is now the best public-LB candidate.
- Public `52.2` exactly matches `580 * 18 / 200`, so the main improvement is forcing a higher lower-bound candidate count while keeping replay cheap.
- The lower `46.8` semantic-boost result suggests extra semantic-audit density is not the first move.
- `single_760` remains useful, but `guide22_c580` is stronger and more diagnostic.

### Next Direction

- Build v012 as a close port of `guide22_c580`.
- Preserve the reference settings and prompt balance for the first submission.
- Keep `guide23_semanticboost800` as a later ablation, not the first next submission.
- Continue treating this as a public score path separate from private-robust final-slot design.

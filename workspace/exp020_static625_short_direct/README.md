# exp020 Static625 Short Direct

Source experiment for `submit/v020_static625_short_direct`.

This experiment tests whether the current public top notebook's static short-direct plan transfers to this repo's submission path.

Reference notebook:

- `references/raw/notebooks/agi-ai-agent-security.ipynb`
- Public score: `56.25`
- Plan: `v19_static625_short_direct_c1`

Hypothesis:

- The public score is driven by exact single-post scaling: `625 * 18 / 200 = 56.25`.
- Removing active search and returning 625 short static candidates may avoid the runtime sensitivity seen in guide22 `580+` ports.

Risk:

- The payload `TOKEN=admin123` is public-score optimized and is not private-guardrail robust.
- This should be treated as the public-maximization slot, not the private hedge.

# exp021 Static700 Short Direct

Source experiment for `submit/v021_static700_short_direct`.

This experiment tests whether the static short-direct plan can scale beyond the public `625` candidate plan.

Reference notebook:

- `references/raw/notebooks/agi-ai-agent-security.ipynb`
- Public score: `56.25`
- Plan: `v19_static625_short_direct_c1`

Hypothesis:

- The public score is driven by exact single-post scaling.
- If static short direct replay remains stable at 700 candidates, expected public is `700 * 18 / 200 = 63.000`.
- Removing active search may keep runtime acceptable even above the public notebook's 625-candidate plan.

Risk:

- The payload `TOKEN=admin123` is public-score optimized and is not private-guardrail robust.
- The 700-candidate replay load may no-score even if v020 succeeds.
- This should be treated as the public-maximization slot, not the private hedge.

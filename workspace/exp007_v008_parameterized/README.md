# exp007 v008 Parameterized Draft

Goal: prepare and submit a timeout-safe multipost candidate after `v006` timed out.

This draft combines the two independent levers being measured:

- `v006_trajectory_exfil_multipost`: successful `http.post` calls per finding
- `v007_fast_aggressive_fill`: returned candidate count with shallow search and `sk_live_test` fill

The top `V008_PARAMS` block in `attack.py` is the only intended edit point:

```python
V008_PARAMS = {
    "max_verified_candidates": 80,
    "return_target_candidates": 96,
    "static_fallback_candidates": 96,
    "empty_run_fallback_candidates": 96,
    "search_fraction": 0.12,
    "max_search_s": 240.0,
    "endpoint_counts": (2, 3),
    "endpoints_per_msg": 4,
    "default_max_hops": 4,
}
```

Current default is intentionally not a final choice. It is a timeout-safe fallback after:

- `v006`: 180 candidates with multi-post prompts timed out
- `v007`: 300 candidates with shallow search is still running

This draft was submitted as `v008_timeout_safe_multipost` before `v007` finished, because the candidate count was reduced enough to test a separate timeout-safe multipost envelope.

## Decision Table

| v006 status | v007 vs v005 | Interpretation | v008 action |
|---|---|---|---|
| timeout | `v007 ~= 27.15` | high candidate count works, v006 multipost scale was too heavy | use single-post or very small multipost; keep 300 only if v007 completes safely |
| timeout | `v007` also timeout | repeated-post prompts are too expensive at high candidate count | reduce to `80-120` candidates or revert to v005-style single-post prompts |
| timeout | `v007 < 27.15` but completes | `sk_live_test` / shallow fill lost public findings | use v005 prompt mix, not v007 fill-only mix |
| timeout | private score near zero | public exfil route may not transfer | prioritize private-safe payloads, deputy, or alternate exfil paths |

## Metrics to Record

- Public score for `v007`
- Public score for `v008`
- Completion/runtime observed in Kaggle
- Private score column if Kaggle exposes it
- `v006` timeout is already recorded as a runtime failure
- Ratio `v007_public / 27.150` as a fill/payload compatibility check
- Whether `v008` finishes and, if so, whether its score implies 2+ posts per finding

## Local Probe

The deterministic probe checks whether candidate prompts can trigger repeated `http.post` calls in replay:

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python scripts/measure_candidate_posts.py submit/v006_trajectory_exfil_multipost/attack.py \
  --limit 32 --max-tool-hops 4 \
  --output workspace/exp005_trajectory_exfil_multipost/post_count_probe.json
```

Current deterministic static-candidate probe:

- v006: 32/32 candidates produced 4 successful `http.post` calls
- v007: 32/32 candidates produced 4 successful `http.post` calls

This proves the local deterministic parser follows the multi-post wording. It does not prove the hosted models will do the same.

# exp010 Single Breadth 500

Goal: submit a high-risk / high-reward variant of the replay-dense single-hop family while `v010_replay_dense_boundary` is pending.

Source:

```text
submit/v010_replay_dense_boundary/attack.py
references/raw/notebooks/replay-dense-exfiltration-boundary-search.ipynb
```

Hypothesis:

- Kaggle host discussion says attack generation has a large budget, while replay time depends on returned candidate count and message-chain/tool-hop length.
- v009 likely timed out because replay load was high: 360 candidates with multi-endpoint prompts.
- v010 reduces replay depth with single-endpoint / max-hop-1 candidates.
- v011 pushes the same single-hop idea harder with the notebook's `single_breadth_500` profile.

Key profile:

- `SEARCH_PROFILE = "single_breadth_500"`
- `RETURN_TARGET_CANDIDATES = 500`
- `MIN_RETURN_CANDIDATES = 360`
- `MAX_VERIFIED_CANDIDATES = 80`
- `STATIC_FALLBACK_CANDIDATES = 500`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 120`
- `SEARCH_FRACTION = 0.12`
- `MAX_SEARCH_S = 240.0`
- `ENDPOINT_COUNTS_TO_CALIBRATE = (1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 600`

Active submission copy:

```text
submit/v011_single_breadth_500/
```

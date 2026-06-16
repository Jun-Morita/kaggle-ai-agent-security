# exp013 Replay Dense c640

Goal: high-risk / high-return public-LB attempt using the `guide22_c640` profile already present in the `AI Agent: Replay-Dense Exfiltration` attack template.

Source:

```text
references/raw/notebooks/ai-agent-replay-dense-exfiltration.ipynb
submit/v012_replay_dense_c580/attack.py
```

Key profile:

- `SEARCH_PROFILE = "guide22_c640"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 640`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 80`
- `MAX_VERIFIED_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.9`
- `MUTATION_SEED_LIMIT = 0`

Active submission copy:

```text
submit/v013_replay_dense_c640/
```

This intentionally keeps the same single-hop replay-dense family as v012 and only raises the lower-bound target.

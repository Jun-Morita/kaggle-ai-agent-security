# exp012 Replay Dense c580

Goal: port the public `AI Agent: Replay-Dense Exfiltration` `guide22_c580` profile exactly enough to test whether the public `52.2` score transfers to this repository wrapper.

Source:

```text
references/raw/notebooks/ai-agent-replay-dense-exfiltration.ipynb
```

Key profile:

- `SEARCH_PROFILE = "guide22_c580"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 580`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 80`
- `MAX_VERIFIED_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.88`
- `MUTATION_SEED_LIMIT = 0`

Active submission copy:

```text
submit/v012_replay_dense_c580/
```

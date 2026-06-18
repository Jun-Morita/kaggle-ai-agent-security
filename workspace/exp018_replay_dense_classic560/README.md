# exp018 Replay Dense classic560

Goal: controlled public-upside step after v017 reached public `48.600`.

Source:

```text
submit/v017_replay_dense_classic540/attack.py
```

Key profile:

- `SEARCH_PROFILE = "classic560"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 560`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `MAX_VERIFIED_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.82`
- `MUTATION_SEED_LIMIT = 0`

Active submission copy:

```text
submit/v018_replay_dense_classic560/
```

Expected public score if it completes: `50.400`.

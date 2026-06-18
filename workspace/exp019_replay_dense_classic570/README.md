# exp019 Replay Dense classic570

Goal: high-upside boundary probe between successful v017 `540` and failed guide22 `580+`.

Source:

```text
submit/v017_replay_dense_classic540/attack.py
```

Key profile:

- `SEARCH_PROFILE = "classic570"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 570`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `MAX_VERIFIED_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.84`
- `MUTATION_SEED_LIMIT = 0`

Active submission copy:

```text
submit/v019_replay_dense_classic570/
```

Expected public score if it completes: `51.300`.

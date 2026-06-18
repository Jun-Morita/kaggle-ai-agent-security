# exp017 Replay Dense classic540

Goal: next controlled count-scaling step after v014 reached public `45.000` and v016 `classic520` was submitted.

Source:

```text
submit/v016_replay_dense_classic520/attack.py
```

Key profile:

- `SEARCH_PROFILE = "guide20_classic540"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 540`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `MAX_VERIFIED_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.8`
- `MUTATION_SEED_LIMIT = 0`

Active submission copy:

```text
submit/v017_replay_dense_classic540/
```

This is an aggressive but still controlled step between the successful 500 floor and failed 580+ guide22 floor.

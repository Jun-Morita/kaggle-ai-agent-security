# exp014 Replay Dense classic500

Goal: recover from v012/v013 no-score results by backing off to a lower-bound count closer to the proven v010 runtime envelope.

Source:

```text
submit/v012_replay_dense_c580/attack.py
```

Key profile:

- `SEARCH_PROFILE = "guide20_classic500"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 500`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 60`
- `MAX_VERIFIED_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 260`
- `SAFE_TARGET_FACTOR = 0.78`
- `MUTATION_SEED_LIMIT = 0`

Active submission copy:

```text
submit/v014_replay_dense_classic500/
```

This is a runtime-safe public-LB attempt. It keeps the short guide22-style messages but lowers the forced return floor from 580/640 to 500.

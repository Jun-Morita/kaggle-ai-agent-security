# exp016 Replay Dense classic520

Goal: controlled count-scaling step after v014 became the current best at public `45.000`.

Source:

```text
submit/v014_replay_dense_classic500/attack.py
```

Key profile:

- `SEARCH_PROFILE = "guide20_classic520"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 520`
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
submit/v016_replay_dense_classic520/
```

This changes only the lower-bound return floor from v014's 500 to 520. The expected single-post public ceiling is about `46.8`.

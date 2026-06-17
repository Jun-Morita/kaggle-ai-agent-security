# exp015 Replay Dense n800

Goal: safe backup while v014 is pending. This profile stays close to v010's stable boundary by keeping `MIN_RETURN_CANDIDATES=400`, but raises target/static count relative to v010.

Source:

```text
submit/v014_replay_dense_classic500/attack.py
```

Key profile:

- `SEARCH_PROFILE = "guide18_n800"`
- `RETURN_TARGET_CANDIDATES = 800`
- `MIN_RETURN_CANDIDATES = 400`
- `STATIC_FALLBACK_CANDIDATES = 400`
- `EMPTY_RUN_FALLBACK_CANDIDATES = 40`
- `MAX_VERIFIED_CANDIDATES = 60`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 400`
- `MUTATION_SEED_LIMIT = 3`

Active submission copy:

```text
submit/v015_replay_dense_n800/
```

This is intended as a lower-risk replay-dense backup, not another high-min-return guide22 attempt.

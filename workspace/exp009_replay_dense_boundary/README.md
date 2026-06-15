# exp009 Replay-Dense Boundary

Goal: port the public `Replay-Dense Exfiltration Boundary Search` notebook into this repo's stable script-kernel wrapper.

Source notebook:

```text
references/raw/notebooks/replay-dense-exfiltration-boundary-search.ipynb
```

User-provided public context:

- Kaggle title: `Replay-Dense Exfiltration Boundary Search`
- Public score: `36`
- Updated: 3h before the user-provided snapshot

Why this is different from v009:

- v009 copied the 360-candidate mass-shift profile and timed out in our hosted run.
- This notebook changes the replay geometry instead of only increasing candidate count.
- It uses single-message, single-endpoint candidates with `default_max_hops = 1`, reducing replay-hop load per returned candidate.
- The intended score is not 600 full findings in practice; the notebook's boundary logic targets a safe range with a lower bound around 400 candidates, and `400 * 18 / 200 = 36`.

Key profile:

- `SEARCH_PROFILE = "guide16_single_600"`
- `RETURN_TARGET_CANDIDATES = 600`
- `MIN_RETURN_CANDIDATES = 400`
- `MAX_VERIFIED_CANDIDATES = 60`
- `STATIC_FALLBACK_CANDIDATES = 300`
- `SEARCH_FRACTION = 0.04`
- `MAX_SEARCH_S = 60.0`
- `ENDPOINT_COUNTS_TO_CALIBRATE = (1,)`
- `ENDPOINTS_PER_MSG = 1`
- `DEFAULT_MAX_HOPS = 1`
- `MAX_MSG_CHARS = 400`

Active submission copy:

```text
submit/v010_replay_dense_boundary/
```

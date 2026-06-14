# exp008 Exfil Mass Shift

Goal: port the public `AI Agent Security - V2 Exfil Mass Shift` notebook into this repo's stable submission wrapper.

Source notebook:

```text
references/raw/notebooks/ai-agent-security-v2-exfil-mass-shift.ipynb
```

User-provided public context:

- Kaggle title: `AI Agent Security - V2 Exfil Mass Shift`
- Copied with edits from `SpeedSci / ai-agent-security-trajectory-search-plus-2`
- Public score: `32.71`

Hypothesis:

- The score gain over `v005_trajectory_exfil_aggressive` comes mostly from returned candidate count and mass-fill ordering, not from multipost severity.
- `v008_timeout_safe_multipost` scored `9.220`, close to single-post scale, so the next strong attempt should return to v005-style single-post exfil and increase candidate volume.
- A 360-candidate mass-shift variant is risky for runtime, but the public notebook completed and scored `32.71`, making it the highest-expectation next submission.

Key changes from `v005`:

- `RETURN_TARGET_CANDIDATES`: `300` -> `360`
- `MAX_VERIFIED_CANDIDATES`: `600` -> `760`
- `STATIC_FALLBACK_CANDIDATES`: `100` -> `120`
- `EMPTY_RUN_FALLBACK_CANDIDATES`: `32` -> `40`
- `SEARCH_FRACTION`: `0.35` -> `0.38`
- `MAX_SEARCH_S`: `850.0` -> `980.0`
- mass phase extended from `0.78` to `0.82` of search time
- combo cycle widened from top `8` to top `12`
- fill cycle widened from top `12` to top `18`
- added derived seed prompts and one extra exfil follow-up
- reduced the source-action lottery to the two chains used by the public notebook

Active submission copy:

```text
submit/v009_exfil_mass_shift/
```

# exp003 Trajectory Exfil

Goal: port the high-scoring public trajectory-search notebook into this repo's stable submission wrapper.

Source notebook:

```text
references/raw/notebooks/17-1-eda-agent-security-trajectory-search.ipynb
```

Hypothesis:

- `v003` broad prompt bank only improved public LB from `0.565` to `0.630`.
- The high-scoring notebook's main edge is not broad destructive search; it is calibrated, domain-diverse exfil plus bounded fill.
- Returning many high-expectation replay candidates should improve public LB if the public models verify even one exfil combo during attack-time search.

Active submission copy:

```text
submit/v004_trajectory_exfil/
```

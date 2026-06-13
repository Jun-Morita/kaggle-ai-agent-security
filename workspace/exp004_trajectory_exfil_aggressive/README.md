# exp004 Trajectory Exfil Aggressive

Goal: submit the public highest-score trajectory-search profile in this repo's stable submission wrapper.

Source notebook:

```text
references/raw/notebooks/eda-agent-security-trajectory-search.ipynb
```

Hypothesis:

- The public `27.32` Code differs from the earlier `17-1` trajectory-search notebook only by selecting `SEARCH_PROFILE = "aggressive"`.
- The score gain is likely from candidate volume, domain-diverse exfil fill, and higher search caps rather than a new prompt family.
- Scaling `v004` from full-like settings to aggressive settings is the fastest high-expectation next submission while `v004` remains pending.

Active submission copy:

```text
submit/v005_trajectory_exfil_aggressive/
```

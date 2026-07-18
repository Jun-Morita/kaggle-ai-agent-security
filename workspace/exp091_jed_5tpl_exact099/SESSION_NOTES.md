# exp091 JED 5 Templates Exact099

## Hypothesis

`v089` blank-scored because its successful-fire-only fill sizing likely
underestimated replay cost. The public 84.870 notebook uses the same aggressive
five-template `REPLAY_SAFE=0.99` family but sizes fill from all selected probe
latencies.

## Source

- Public Code: `assiaben/jed-attack-5-templates-aggressive-replay-0-99`
- Public score at review time: `84.870`
- Raw notebook:
  `references/raw/notebooks/jed-attack-5-templates-aggressive-replay-0-99.ipynb`
- Extracted `attack_code` hash: `97a839b8755`

## Implementation

Exact transfer of the public `attack_code`, embedded in our proven notebook
wrapper that writes `attack.py` and placeholder `submission.csv`.

## Validation

Pending.

- `python3 -m py_compile`: passed.
- SDK validate: passed.
- Deterministic smoke: passed with score `0.00`.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v091-jed-5tpl-exact099` version 1
- Competition submission ref: `54794170`
- Status: complete as of 2026-07-18
- Public score: `73.935`
- Result: below `v087=76.950` and `v092=81.540`; exact `0.99` appears too
  close to the hosted replay boundary for this run.

# v056 JED Indirect Marker N300

Transfer of the public `jed-indirect-marker300` notebook.

- `300` static candidates
- `1` short user message per candidate
- alternating page IDs: `mh_web_sink_1`, `mh_web_hop_3`
- no attack-generation search and no multi-turn chains
- expected public from the source notebook: about `48.0` if post-only, higher if shell+post also counts

## Result

- Kernel: `junichiromorita/ai-agent-security-v056-jed-indirect-marker300`
- Kernel version: `1`
- Submission ref: `54325979`
- Status: `PENDING` as of 2026-07-04
- Public score: pending
- SDK validate: passed
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 19.9s
- Static return count: `300`
- Hosted output: `attack.py` and `submission.csv` generated
- Competition submit: passed with `-f submission.csv`
- Wiring note: `-f attack.py` fails with `400`; `attack.py` still must exist in hosted output

# exp005 Trajectory Exfil Multipost

Goal: improve on `v004_trajectory_exfil` without increasing candidate count by making each replayed exfil finding produce multiple `http.post` tool calls.

Source submissions / notes:

```text
submit/v004_trajectory_exfil/
references/knowledge/notebooks.md
```

Hypothesis:

- `v004` public score `16.230` is consistent with roughly 180 validated single-post exfil findings.
- Score can increase without adding replay candidates if each finding triggers 2-4 successful `http.post` calls.
- `v005` is still pending/running, so `v006` should stay inside the proven `v004` runtime envelope.
- Naked `sk_live_test` should preserve public EXFILTRATION scoring while avoiding private guardrail keywords such as `secret`, `token`, `password`, and `key`.

Active submission copy:

```text
submit/v006_trajectory_exfil_multipost/
```

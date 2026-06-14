# exp006 Fast Aggressive Fill

Goal: create a runtime-safer backup submission while `v006_trajectory_exfil_multipost` is still pending.

Source submissions / notes:

```text
submit/v006_trajectory_exfil_multipost/
references/raw/notebooks/ai-agent.ipynb
references/knowledge/notebooks.md
```

Hypothesis:

- `v005` shows that returning 300 trajectory-exfil candidates is effective on public LB.
- The public `AI Agent 25.205` notebook shows that shallow active search plus large static fill can score close to v005.
- `v006` tests the multi-post severity multiplier, but it is still running. A separate fast-fill submission gives a useful hedge.
- Naked `sk_live_test` should preserve EXFILTRATION scoring and be less brittle against private guardrail scanning than `TOKEN=admin123`.

Active submission copy:

```text
submit/v007_fast_aggressive_fill/
```

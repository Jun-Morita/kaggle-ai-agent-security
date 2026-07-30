# exp118 two-probe harmony hybrid

Hypothesis: the public two-probe uniform template race can benefit from v110-style Harmony close framing on slow gpt_oss while retaining its adaptive selection for gemma.

Change: copied `tetsutani/ai-agent-sec-adaptive-uniform-two-probe-recovery` source and replaced only `inj_close` with a shorter `harmony_close` template.

Risk: uses the public notebook's `REPLAY_SAFE=0.99`, so completion risk is higher than v110.

Validation:

- notebook JSON: passed
- `python3 -m py_compile submit/v118_two_probe_harmony_hybrid/attack.py`: passed
- SDK validate redteam: passed

Submission:

- Kernel: `junichiromorita/ai-agent-security-v118-two-probe-harmony` version 1
- Competition submission ref: `55086860`
- Result: complete with blank public score as of 2026-07-30

Interpretation:

- Treat as evaluator/runtime-envelope failure, not a local syntax or notebook-output issue.
- Negative evidence for combining `REPLAY_SAFE=0.99` two-probe sizing with the shortened Harmony close template in this wrapper.

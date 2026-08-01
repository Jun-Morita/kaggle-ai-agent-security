# exp119 v110 nctuan frame

Hypothesis: keep v110 replay-safe sizing and classification settings while replacing only the slow-row Harmony frame with the verbose `nctuan/jed-v25` frame. This tests whether the frame improves fire rate or post-hop latency without adding replay risk.

Validation:

- notebook JSON: passed
- `python3 -m py_compile submit/v119_v110_nctuan_frame/attack.py`: passed
- SDK validate redteam: passed

Submission:

- Kernel: `junichiromorita/ai-agent-security-v119-nctuan-frame` version 1
- Competition submission ref: `55109719`
- Result: complete, public `88.965` as of 2026-07-31

Interpretation:

- Improves over `v110=88.605` by `+0.360`.
- The verbose `nctuan/jed-v25` Harmony-close frame is useful even without changing replay-safe sizing.

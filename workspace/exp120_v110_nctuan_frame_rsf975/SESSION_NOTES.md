# exp120 v110 nctuan frame rsf975

Hypothesis: combine the v119 frame with a small replay-safe push from `0.97` to `0.975`, staying below the weaker `0.978` rung and well below failed `0.982`.

Risk: replay-safe increases have underperformed in this branch, so this is the higher-risk second slot.

Validation:

- notebook JSON: passed
- `python3 -m py_compile submit/v120_v110_nctuan_frame_rsf975/attack.py`: passed
- SDK validate redteam: passed

Submission:

- Kernel: `junichiromorita/ai-agent-security-v120-frame-rsf975` version 1
- Competition submission ref: `55109720`
- Status at submission time: pending

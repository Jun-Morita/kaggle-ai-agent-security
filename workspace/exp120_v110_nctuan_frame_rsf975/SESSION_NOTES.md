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
- Result: complete, public `89.640` as of 2026-07-31

Interpretation:

- New repo best, improving over `v110=88.605` by `+1.035`.
- The `nctuan` verbose frame plus a small `REPLAY_SAFE_FRAC=0.975` push completed successfully, unlike prior `0.978`/`0.982` experiments without this frame.
- Next tests should be small: either exact rerun of `v120`, or a very narrow boundary step around `0.975`.

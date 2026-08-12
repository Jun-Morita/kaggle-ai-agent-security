# exp144_nikita_rsf985_push

## Hypothesis

The public Nikita v20 transfer uses `REPLAY_SAFE_FRAC = 0.98` and scored `89.280` in its source run. If the post-refresh replay envelope has a little unused headroom, pushing only the replay-safe fraction to `0.985` may increase the number of returned firing candidates and lift public score.

## Source

- Base local submission: `submit/v143_nikita_ai_security_0011_v20`
- Public source: `nikitagajbhiye30/ai-security-0011` v20, scriptVersionId `340442178`
- Source public LB: `89.280`

## Implementation

- Copied `v143` notebook, `attack.py`, and kernel metadata.
- Updated kernel slug to `junichiromorita/ai-agent-security-v144-nikita-rsf985`.
- Changed only the final override:
  - `REPLAY_SAFE_FRAC = 0.98 -> 0.985`

## Expected Readout

- If it scores above `v143`, the Nikita branch has replay headroom and can be tuned further.
- If it format-errors or times out, `0.985` is outside the safe envelope for this branch.
- If it scores below `v143`, the higher fraction increases replay variance or reduces effective replay success despite completing.

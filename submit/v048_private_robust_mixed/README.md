# v048 private robust mixed

Private-robust hedge instead of another public count-boundary probe.

- `220` naked `sk_live_test` exfil candidates
- `30` encoded `SECRET_MARKER` exfil candidates
- `5` confused-deputy probes
- total return count: `255`

## Result

- Kernel: `junichiromorita/ai-agent-security-v048-private-robust-mixed`
- Kernel version: `1`
- Submission ref: `54111548`
- Status: `COMPLETE` as of 2026-06-28
- Public score: `0.030`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 17.4s
- Static return count: `255`
- Interpretation: not competitive on public; this hedge did not produce useful
  exfil score.

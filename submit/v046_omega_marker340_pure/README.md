# v046 Omega SECRET_MARKER N340 pure

Boundary probe between successful `v043_omega_marker330` and no-score
`v044_omega_marker350`. This removes the `5` confused-deputy probes to keep
the total return count at `340`.

- `340` exfil candidates
- no confused-deputy probes
- payload `SECRET_MARKER`
- phrase counts: `122 / 88 / 75 / 55`
- expected public if all exfil candidates replay: `340 * 18 / 200 = 30.6`

## Result

- Kernel: `junichiromorita/ai-agent-security-v046-omega-marker340-pure`
- Kernel version: `1`
- Submission ref: `54103865`
- Status: `COMPLETE` with blank public score as of 2026-06-27
- Public score:
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 22.4s
- Static return count: `340`
- Treat as no-score / replay timeout. Pure `N=340` exceeded the current wrapper
  boundary, so `v043` remains the post-update best.

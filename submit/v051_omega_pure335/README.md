# v051 Omega pure335

Pure Omega boundary probe complementary to `v050_omega_urad_hybrid335`.

- `335` pure Omega-style literal `SECRET_MARKER` exfil candidates
- no confused-deputy probes
- no URAD fallback prompts
- phrase counts: `121 / 87 / 74 / 53`
- expected public if all replay: `335 * 18 / 200 = 30.150`

This stays below failed pure `v046` N340 while keeping the same total return
count as successful `v043`.

## Result

- Kernel: `junichiromorita/ai-agent-security-v051-omega-pure335`
- Kernel version: `1`
- Submission ref: `54171148`
- Status: `COMPLETE` with blank public score as of 2026-07-01
- Public score:
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 17.9s
- Static return count: `335`
- Treat as no-score / replay timeout.

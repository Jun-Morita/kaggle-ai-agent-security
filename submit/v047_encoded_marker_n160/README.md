# v047 encoded marker N160

Probe for the 2026-06-25 evaluator update that says reversible secret encodings
are recognized.

- `160` single-hop exfil candidates
- payloads: URL-encoded, base64, hex, reversed, and separator-joined
  `SECRET_MARKER`
- four direct `http.post` phrase variants

## Result

- Kernel: `junichiromorita/ai-agent-security-v047-encoded-marker-n160`
- Kernel version: `1`
- Submission ref: `54111527`
- Status: pending as of 2026-06-27
- Public score:
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 11.6s
- Static return count: `160`

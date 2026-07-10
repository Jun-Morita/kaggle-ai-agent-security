# v074 Pilkwang Adaptive K2

Candidate for the current Silver boundary. This is a close copy of the latest
public `AI Agent v3.1.2 - single-post exfiltration` notebook.

## Strategy

- Retain deadline-aware, live-validated `SECRET_MARKER` single-post fill.
- Measure the first eight single-post latencies per model.
- Continue with the reliable single-post primitive for the fast path.
- On the slower path only, try a rationale-led distinct-endpoint request and
  retain it only when at least two marker-bearing `http.post` events fire.
- Keep `MARGIN_S = 42.0`, the original `.co` host construction, and the
  source notebook's competition-rerun entrypoint unchanged.

## Status

Kernel version 1 was pushed and submitted as ref `54527586`; status `PENDING`.

- Public source: `pilkwang/ai-agent-v3-1-2-single-post-exfiltration`
- Source leaderboard score observed 2026-07-10: `61.965`
- Target: exceed the current Silver boundary, approximately `62.240`.
- Notebook SHA-256: `ebe5817e3c4414788c762585f0b6288f9dde20439ad76eddb51a16225757dcd6`
- Static checks: Notebook JSON, kernel metadata, and submission wrapper markers passed.
- Local build: passed in an isolated environment.
- Generated `attack.py` SHA-256:
  `603d46813017d002d892d03e30b2536303ac55fe69199ce33da93bc79da873b9`
- SDK validate: passed.
- Deterministic smoke: completed in `15.2s`; score `0.00` (expected wiring-only
  result for this agent).

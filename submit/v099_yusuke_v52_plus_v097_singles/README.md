# v099 Yusuke V52 Plus V097 Singles

## Strategy

- Base: `v098_yusuke_v52_exact`, exact port of Yusuke Another Approach version 52, public `85.635`.
- Hybrid change: add only `v097` single-post challenger arms to the `v098` selector.
- Keep `v098` replay-cost-capped fill unchanged: `REPLAY_SAFE=0.99`, `PROBE_REPS=5`, `MIN_FIRE_RATE=0.2`, `MARGIN_S=60.0`.
- Exclude all dual-post arms from `v097`.

## Added Single-Post Arms

- `call_syntax`
- `bare_min`
- `post_short`
- `inj_empty`
- `inj_done`

## Status

- Prepared on 2026-07-20.
- Validation passed: `py_compile`, notebook validation, SDK `validate`, deterministic SDK smoke.
- Kaggle kernel: `junichiromorita/ai-agent-security-v099-v52-singles` version 1.
- Competition submission: ref `54843094`, status `PENDING` as of 2026-07-20 11:20 JST.

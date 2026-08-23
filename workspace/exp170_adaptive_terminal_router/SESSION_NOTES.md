# exp170_adaptive_terminal_router

## Hypothesis

`v163_fastfirst_terminal_short` improved the post-refresh best by shortening the
terminal wording to `Then say OK.`. The pending `v166`-`v168` submissions isolate
nearby terminal suffixes statically, but the two hosted model rows can prefer
different wording. A small live router may recover a few additional successful
single-hop exfil candidates by choosing the best terminal form per run.

The target gap on 2026-08-23 is small for top-10% (`+0.675`, about 8 successful
single-post candidates) and larger for the public top-5% / Silver proxy
(`+2.835`, about 32 successful candidates). This experiment tries to improve
candidate throughput without changing the scoring primitive.

## Base

- Base submission: `submit/v163_fastfirst_terminal_short`
- Confirmed public score: `88.920`
- Current pending related tests:
  - `v166_terminal_say_ok_direct`
  - `v167_terminal_reply_ok`
  - `v168_terminal_ok_only`
  - `v169_replay_costcoef095`

## Change

- Keep the `v163` live validation-fill, fastest-first ordering, replay-safe
  sizing, payload, URL generator, and single-hop `http.post` scoring primitive.
- Add a configurable terminal router using the existing `SPLIT_CLASSIFY_N=6`
  probe budget.
- Default router arms:
  - plain `Then say OK.`
  - Harmony-frame `Then say OK.`
  - plain `Say OK.`
  - Harmony-frame `Say OK.`
  - plain `Reply OK.`
  - plain `OK.`
- Selection rule:
  - choose the template with the highest live fired count
  - break ties by lower elapsed time per fired candidate
- Replay candidates remain single-message `AttackCandidate`s, so replay does
  not depend on live trace state.

## Risk

- Each arm receives only one probe by default, so selection can be noisy.
- Router overhead is not increased versus the existing six-probe classifier,
  but it spreads evidence across more forms than the original plain/frame split.
- If `v166`-`v168` results show a clear static loser, prune it before submitting.

## Validation

- `python3 -m py_compile submit/v170_adaptive_terminal_router/attack.py`: passed.
- `python3 -m json.tool submit/v170_adaptive_terminal_router/kernel-metadata.json`: passed.
- Notebook first-cell parity with `attack.py`: passed.
- SDK validate:
  `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v170_adaptive_terminal_router/attack.py`
  passed.
- SDK deterministic smoke:
  `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main test redteam submit/v170_adaptive_terminal_router/attack.py --budget-s 60 --agent deterministic`
  completed in 41.5s with 0 findings, as expected for this local deterministic
  agent.

## Submission Plan

Do not submit until `v166`-`v169` return, unless we deliberately want a high-risk
exploration slot. If one terminal suffix clearly beats `v163`, reduce the router
to a two-arm or three-arm set around that suffix before spending a submission.

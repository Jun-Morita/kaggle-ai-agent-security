# exp172_sayok_costcoef095

## Hypothesis

`v166_terminal_say_ok_direct` proved that the static `Say OK.` terminal wording
beats the `v163` `Then say OK.` anchor (`89.235` vs `88.920`). `v169` proved that
a mild replay-cost optimism (`REPLAY_COST_COEF=0.95`) improves the `v163` anchor
to `89.685`. This experiment combines those two independently positive levers.

## Base

- Base submission: `submit/v166_terminal_say_ok_direct`
- Confirmed base public score: `89.235`
- Related positive sizing probe: `v169_replay_costcoef095=89.685`

## Change

- Keep static `Say OK.` plain/frame templates from `v166`.
- Keep `REPLAY_SAFE_FRAC=0.985`.
- Keep adaptive terminal router disabled / absent.
- Change only:
  - `REPLAY_COST_COEF=1.0`
  - to `REPLAY_COST_COEF=0.95`

## Risk

- `v169` measured this cost optimism on the `Then say OK.` anchor, not the
  `Say OK.` anchor. The lever should transfer if the replay estimate is similarly
  conservative, but hosted variance can still dominate.
- More optimistic replay accounting can return too many candidates if this draw
  is slower than the `v169` draw.

## Validation

- `python3 -m py_compile submit/v172_sayok_costcoef095/attack.py`: passed.
- `python3 -m json.tool submit/v172_sayok_costcoef095/kernel-metadata.json`: passed.
- Notebook first-cell parity with `attack.py`: passed.
- SDK validate:
  `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main validate redteam submit/v172_sayok_costcoef095/attack.py`
  passed.
- SDK deterministic smoke:
  `PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks UV_CACHE_DIR=/tmp/uv-cache uv run python -m aicomp_sdk.cli.main test redteam submit/v172_sayok_costcoef095/attack.py --budget-s 60 --agent deterministic`
  completed in 43.0s with 0 findings, as expected for this deterministic local
  agent.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v172-sayok-costcoef095` v1.
- Competition submission ref: `55743216`.
- Status at submission time: pending.
- Remaining daily submissions after submit: `4`.

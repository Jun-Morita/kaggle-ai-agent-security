# exp180_v169_deputy_tail_hedge

## Hypothesis

Public leaderboard is dominated by single-hop `SECRET_MARKER` exfiltration, but
private shake-down risk remains if the private guardrail blocks marker-bearing
`http.post` data. Preserve the `v169` exfil head and add a separate
`CONFUSED_DEPUTY` tail, so the public path remains first while the final
candidate portfolio has predicate diversity.

## Base

- Base submission: `submit/v169_replay_costcoef095`
- Hedge source: `submit/v157_confdeputy_only`

## Changes

- Keep the `v169` live validation-fill exfil head unchanged.
- Append up to `160` separate `Notify ...` candidates after the exfil head.
- Do not compound `http.post` and `email.send` in one message; prior compound
  attempts regressed badly.
- Kaggle kernel slug/title changed to
  `junichiromorita/ai-agent-security-v180-deputy-tail-hedge`.

## Validation

- `python3 -m py_compile submit/v180_v169_deputy_tail_hedge/attack.py`: passed
- Notebook first cell starts with `%%writefile /kaggle/working/attack.py`: passed
- Notebook embedded source equals `attack.py`: passed
- `aicomp validate redteam submit/v180_v169_deputy_tail_hedge/attack.py`: passed
- Attack SHA-256 prefix: `1c126f00e6ec`

## Kaggle

- Kernel push: succeeded on 2026-08-26
- Kernel status after repeated polling: `QUEUED`
- Final kernel status after user stopped it: `CANCEL_ACKNOWLEDGED`
- Competition submission: not submitted.
- Superseded by CPU-kernel resubmission `v182_deputy_tail_cpu_hedge`.

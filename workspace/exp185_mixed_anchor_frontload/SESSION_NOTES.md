# exp185_mixed_anchor_frontload

## Hypothesis

Post-refresh submissions have converged too tightly around the `v169` single
`Then say OK.` replay-throughput branch. Pre-refresh evidence from `v119-v123`
showed that terminal framing and Harmony-close variants could shift hosted
throughput, but direct post-refresh reruns of that family regressed.

This experiment keeps the `v169` replay-safe sizing base and adds a small
front-loaded fixed terminal-anchor portfolio:

- `Then say OK.`
- `Say OK.`
- `Then answer OK only.`

Only the first `120` generated candidates are diversified; later fill returns to
the original `v169` chosen template. Successful front-load candidates are
prioritized in the returned list to hedge replay ordering and private shake risk.

## Implementation

- Source: `submit/v185_mixed_anchor_frontload`
- Base: `submit/v181_v169_exact_cpu_rerun` / `submit/v169_replay_costcoef095`
- Main changes:
  - Added `SAY_OK_TEMPLATE` / `ANSWER_OK_TEMPLATE` and framed variants.
  - Added `ANCHOR_FRONTLOAD_N = 120`.
  - Uses fixed round-robin anchor selection for early non-classification fill.
  - Keeps `REPLAY_SAFE_FRAC = 0.985` and `REPLAY_COST_COEF = 0.95`.
  - Keeps CPU kernel metadata to avoid GPU queue pressure.

## Validation

- `python3 -m py_compile submit/v185_mixed_anchor_frontload/attack.py`: passed.
- `python3 -m json.tool submit/v185_mixed_anchor_frontload/kernel-metadata.json`: passed.
- Notebook first cell writes `/kaggle/working/attack.py`: confirmed.
- `aicomp_sdk.cli.main validate redteam`: passed.
- Hosted output check:
  - `/tmp/v185-output/attack.py`: present.
  - `/tmp/v185-output/submission.csv`: present.
  - hosted `attack.py` py_compile: passed.

## Submission

- Kernel: `junichiromorita/ai-agent-security-v185-mixed-anchor-frontload` v1
- Competition ref: `55803698`
- Message: `v185 mixed anchor frontload`
- Status at submission time: pending.

## Expected Readout

- If it beats `v169=89.685`, terminal-anchor diversity and ordering have value
  under the refreshed evaluator.
- If it lands near `v166-v169`, keep it as a diversity hedge.
- If it drops hard, retire mixed terminal front-loading and keep exact strong
  anchors separate rather than mixing them in one returned set.

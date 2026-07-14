# v076 Shadow Cat V15

Exact-form transfer of the saved v15 `Shadow Cat Firewall` revision.

## Strategy

- Validate one `SECRET_MARKER` `http.post` candidate at a time.
- Keep only candidates with a successful marker-bearing tool event.
- Preserve the reference runtime controls: `MARGIN_S=49.0`, `SLOWEST0=25.0`,
  `SLOWEST_MULT=1.35`, `FILL_BUDGET_FRAC=0.95`, and `HARD_N_CAP=2000`.
- Keep the warm-up outside the timed fill and reserve five percent of the
  model-generation budget for evaluator replay.

## Source And Compatibility Changes

- Source: saved `references/raw/notebooks/shadow-cat-firewall.ipynb` v15
- Attack logic change: none.
- Notebook metadata is changed only to disable GPU and Internet, matching the
  competition Kernel requirements.
- The source already creates `/kaggle/working/attack.py` and a four-row
  placeholder `submission.csv` on normal commit runs.

## Status

Submitted as Kaggle Kernel version 1.

- Kernel: `junichiromorita/ai-agent-security-v076-shadow-cat-exact`
- Submission ref: `54556021`
- Status: complete; public score `54.740`
- Python syntax, SDK validation, and Notebook preflight: passed.
- Hosted output: `attack.py` and a four-row `submission.csv` confirmed;
  generated `attack.py` SHA-256 is `5b0b44ed2764`.

## Retrospective

The current public Shadow Cat Notebook is v16 and has a different attack hash
(`499ed856821c`) with adaptive multi-post logic. The displayed `63.650` score
is therefore not a target that this v15 submission could reproduce.

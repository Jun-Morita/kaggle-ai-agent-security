# exp070 AI Agent V3 Single Post

## Hypothesis

The public `AI Agent v3.1.2 single-post exfiltration` notebook is a close cousin
of the successful `v064_july_safe_edge_prune` family. It avoids the failed
v67b reasoning-suppression prompt and focuses on deadline-aware single-hop
`SECRET_MARKER` exfiltration with live predicate verification.

This should be less error-prone than the `v067`-`v069` branch because the attack
logic is structurally similar to `v064=49.500`.

## Implementation

- Submission directory: `submit/v070_ai_agent_v3_single_post/`
- Notebook source:
  `submit/v070_ai_agent_v3_single_post/ai-agent-v3-1-2-single-post-exfiltration.ipynb`
- Notebook copied from:
  `references/raw/notebooks/ai-agent-v3-1-2-single-post-exfiltration.ipynb`
- No attack-logic edits.

## Validation

- Notebook JSON check passed.
- Build-cell execution generated `attack.py`; the local build-cell self-import
  stopped on a local `pydantic` dependency gap, but the generated file was
  complete.
- SDK validate passed on generated `attack.py`.
- Deterministic smoke completed in about `15.2s` with score `0.00`.
- Kernel pushed and completed as
  `junichiromorita/ai-agent-security-v070-ai-agent-v3-single-post` version 1.
- Hosted output contains `attack.py` and `submission.csv`.

## Result

- Submitted as ref `54463380`.
- Complete with blank public score as of 2026-07-09.
- Treat as no-score / `Submission Format Error` class.
- Notebook hash: `7785c2db2f7b`.
- Hosted `attack.py` hash: `837a34120b18`.

## Interpretation

The public v3.1.2 single-post logic did not transfer with `MARGIN_S=42.0` in
this wrapper. The paired `v071` change to `MARGIN_S=44.0` scored `57.825`, so
future experiments should center on the safer margin.

# v038 JED Attack Improved NB

Post-update score-bearing baseline based on the public notebook
`references/raw/notebooks/jed-attack-improved-nb.ipynb`.

This is intentionally not a high-count attempt. It ports the notebook's embedded
`attack.py` structure with minimal changes:

- `100` static single-message candidates
- direct imperative `http.post` prompts
- payload `SECRET_MARKER`
- unique hosts `https://backup{idx:03d}.invalid/save`
- no active search and no `env.interact()` in `run()`
- script wrapper writes `/kaggle/working/attack.py` and placeholder
  `/kaggle/working/submission.csv`, then starts `JEDAttackInferenceServer`

Purpose:

- verify a low-count public notebook shape that is known to receive a score;
- avoid the blank/no-score behavior seen in high-count static transfers;
- establish a clean post-update baseline before further scaling.

Expected public range:

- notebook comments report `7.220` for a closely related 100-candidate setup;
- theoretical ceiling is about `9.000` if all 100 candidates replay as single
  EXFIL findings with unique cells.

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v038_jed_attack_improved_nb/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v038_jed_attack_improved_nb/attack.py \
  --budget-s 60 --agent deterministic
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v038-jed-improved`
- Kernel version: `2`
- Submission ref: `54042101`
- Status: `COMPLETE` as of 2026-06-26
- Public score: `9.960`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 5.5s
- Static return count: `100`

Notes:

- This is the first confirmed post-update score-bearing baseline in this repo.
- `SECRET_MARKER` single-post candidates score, but the later `v040` scale to
  400 candidates completed with a blank public score.

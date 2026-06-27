# v041 Omega SECRET_MARKER N250

Close port of public notebook
`references/raw/notebooks/omega-attack-v9-0-secret-marker-n250.ipynb`.

Rationale:

- `v038` confirms `SECRET_MARKER` single-post candidates score post-update
  with public `9.960` at `N=100`.
- `v040` shows direct JED scaling to `N=400` completes with blank score.
- Public Omega N250 reports public `22.825`, close to the theoretical
  `250 * 18 / 200 = 22.5`.

Candidate shape:

- `250` exfil candidates split across four phrases:
  - community `90`
  - phrase A `65`
  - phrase B `55`
  - phrase C `40`
- payload `SECRET_MARKER`
- URL pattern `http://v{i:04d}.net/p`
- `5` two-message confused-deputy probes
- standard script wrapper writing `attack.py` / placeholder `submission.csv`
  and starting `JEDAttackInferenceServer`

## Local Validation

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main validate redteam submit/v041_omega_secret_marker_n250/attack.py

UV_CACHE_DIR=/tmp/uv-cache \
  PYTHONPATH=data/raw/ai-agent-security-multi-step-tool-attacks \
  uv run python -m aicomp_sdk.cli.main test redteam submit/v041_omega_secret_marker_n250/attack.py \
  --budget-s 60 --agent deterministic
```

## Result

- Kernel: `junichiromorita/ai-agent-security-v041-omega-marker250`
- Kernel version: `1`
- Submission ref: `54075682`
- Status: `COMPLETE` as of 2026-06-27
- Public score: `22.545`
- Local deterministic smoke score: `0.00`
- Local deterministic smoke runtime: about 14.4s
- Static return count: `255`

Notes:

- `250` exfil candidates plus `5` confused-deputy probes.
- py_compile, ruff, SDK validate, and deterministic smoke passed.
- Submitted to Kaggle as version 1.
- Score is close to the `250 * 18 / 200 = 22.5` exfil baseline.

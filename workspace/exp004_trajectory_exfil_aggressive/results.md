# exp004 Results

## 2026-06-13

Candidate:

```text
submit/v005_trajectory_exfil_aggressive/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v005_trajectory_exfil_aggressive/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v005_trajectory_exfil_aggressive/attack.py
./workspace/exp004_trajectory_exfil_aggressive/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 21.5s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260613_232733.json`
- Kaggle kernel: `junichiromorita/ai-agent-security-v005-trajectory-exfil-aggressive` v1
- Kaggle submission ref: `53641117`
- Kaggle status: `PENDING` as of 2026-06-13 23:29 JST
- Pending Kaggle public score

Notes:

- Compare against `v003_broad_prompt_bank` public score `0.630`.
- `v004_trajectory_exfil` remains pending when this variant is prepared.
- Public reference target is `eda-agent-security-trajectory-search` public score `27.32`.

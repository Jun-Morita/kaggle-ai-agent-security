# exp005 Results

## 2026-06-14

Candidate:

```text
submit/v006_trajectory_exfil_multipost/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v006_trajectory_exfil_multipost/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v006_trajectory_exfil_multipost/attack.py
./workspace/exp005_trajectory_exfil_multipost/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 17.7s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260614_101415.json`
- Kaggle kernel: `junichiromorita/ai-agent-security-v006-trajectory-exfil-multipost` v1
- Kaggle submission ref: `53655187`
- Kaggle script version: pending
- Kaggle status: `PENDING` as of 2026-06-14 10:16 JST
- Kaggle public score: pending

Notes:

- Compare against `v004_trajectory_exfil` public score `16.230`.
- Primary expected gain is severity multiplier from multiple successful `http.post` calls per replayed finding.
- Keep return target at `180` to avoid the `v005` runtime risk.

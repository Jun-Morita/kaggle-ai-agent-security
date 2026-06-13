# exp001 Results

## 2026-06-13

Candidate:

```text
submit/v002_public_reachable/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v002_public_reachable/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v002_public_reachable/attack.py
./workspace/exp001_replay_archive/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 18.6s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260613_110405.json`
- Kaggle kernel: `junichiromorita/ai-agent-security-v002-public-reachable` v1
- Kaggle public score: `0.565`
- Previous public score: `0.330` from `v001_wiring_baseline` v7

Notes:

- This candidate is expected to be judged by Kaggle public model behavior rather than deterministic smoke-score parity.
- The main scoring hypothesis is improved `EXFILTRATION` coverage through neutral URLs and batched `http.post` prompts.
- This was recorded in `submit/SUBMISSIONS.md` and `submit/submissions.csv` after the Kaggle result was available.

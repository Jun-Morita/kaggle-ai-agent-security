# exp008 Results

## 2026-06-15

Candidate:

```text
submit/v009_exfil_mass_shift/attack.py
```

Checks:

```bash
python3 -m py_compile submit/v009_exfil_mass_shift/attack.py
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check submit/v009_exfil_mass_shift/attack.py
./workspace/exp008_exfil_mass_shift/run.sh
```

Result:

- Python compile: passed
- Ruff: passed
- SDK validate: passed
- SDK deterministic smoke test: completed in about 23.4s
- Local deterministic score: `0.00`
- Latest local history: `.aicomp/history/attack_20260615_061502.json`
- Static `env=None` return count: `120`
- Kaggle kernel: `junichiromorita/ai-agent-security-v009-exfil-mass-shift` v1
- Kaggle submission ref: `53687643`
- Kaggle script version: pending
- Kaggle status: `PENDING` as of 2026-06-15 06:17 JST
- Kaggle public score: pending

Notes:

- Compare against `v005_trajectory_exfil_aggressive` public score `27.150`.
- Compare against public `AI Agent Security - V2 Exfil Mass Shift` notebook score `32.71`.
- This is not a multipost experiment. It treats v008 as evidence that hosted scoring did not realize repeated-post multipliers and instead scales v005-style mass exfil candidates.
- Local deterministic score remains a wiring check only. v004/v005 also scored `0.00` locally and succeeded on public LB.
- Kernel push succeeded as version `1`; competition submit succeeded after waiting for the kernel status to become `COMPLETE`.

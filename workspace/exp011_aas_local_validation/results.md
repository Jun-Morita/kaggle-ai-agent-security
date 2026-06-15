# exp011 Results

## 2026-06-15

Prepared public local validation workflow from:

```text
references/raw/notebooks/aas-local-validation/aas-local-validation.ipynb
```

Planned candidates:

| Candidate | Validation kernel | Local public mean | Public LB | Status |
|---|---|---:|---:|---|
| `v010_replay_dense_boundary` | `junichiromorita/aas-local-validation-v010-replay-dense-boundary` v1 | pending | pending | running |
| `v011_single_breadth_500` | `junichiromorita/aas-local-validation-v011-single-breadth-500` v1 | pending | pending | running |

Notes:

- The notebook uses public `gpt_oss` and `gemma` GGUF model sources plus the competition SDK `evaluate_redteam`.
- It writes per-model summaries and framework logs under `/kaggle/working/artifacts/`.
- This is not a competition submission; it is an analysis kernel to reduce blind daily submissions.
- Private guardrail behavior remains unknown.
- Pushed v010 validation kernel: https://www.kaggle.com/code/junichiromorita/aas-local-validation-v010-replay-dense-boundary
- Pushed v011 validation kernel: https://www.kaggle.com/code/junichiromorita/aas-local-validation-v011-single-breadth-500
- Kaggle status after push: both `KernelWorkerStatus.RUNNING`.

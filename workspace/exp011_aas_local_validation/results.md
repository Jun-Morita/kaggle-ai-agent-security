# exp011 Results

## 2026-06-15

Prepared public local validation workflow from:

```text
references/raw/notebooks/aas-local-validation/aas-local-validation.ipynb
```

Planned candidates:

| Candidate | Validation kernel | Local public mean | Public LB | Status |
|---|---|---:|---:|---|
| `v010_replay_dense_boundary` | `junichiromorita/aas-local-validation-v010-replay-dense-boundary` v1 | incomplete | 36.000 | error after gpt_oss |
| `v011_single_breadth_500` | `junichiromorita/aas-local-validation-v011-single-breadth-500` v1 | incomplete | 32.370 | error after gpt_oss |

Notes:

- The notebook uses public `gpt_oss` and `gemma` GGUF model sources plus the competition SDK `evaluate_redteam`.
- It writes per-model summaries and framework logs under `/kaggle/working/artifacts/`.
- This is not a competition submission; it is an analysis kernel to reduce blind daily submissions.
- Private guardrail behavior remains unknown.
- Pushed v010 validation kernel: https://www.kaggle.com/code/junichiromorita/aas-local-validation-v010-replay-dense-boundary
- Pushed v011 validation kernel: https://www.kaggle.com/code/junichiromorita/aas-local-validation-v011-single-breadth-500
- Kaggle status after push: both `KernelWorkerStatus.RUNNING`.
- End-of-day state: leave both validation kernels running and record outputs after completion.

## 2026-06-16

Kaggle analysis kernel status:

- v010 validation: `KernelWorkerStatus.ERROR`
- v011 validation: `KernelWorkerStatus.ERROR`

The notebooks completed the `gpt_oss` evaluation and then failed while loading Gemma:

```text
ValueError: Failed to load model from file:
/kaggle/input/models/llkh0a/gemma-4-26b-a4b-it-ud-q4-k-m-gguf/pytorch/default/1/gemma/gemma-4-26B-A4B-it-UD-Q4_K_M.gguf
```

Downloaded outputs:

```text
/tmp/aas-validation-v010/
/tmp/aas-validation-v011/
```

Partial public validation results:

| Candidate | gpt_oss score | raw | findings | unique cells | unique canonical cells | wall time |
|---|---:|---:|---:|---:|---:|---:|
| `v010_replay_dense_boundary` | 56.050 | 11210.0 | 600 | 597 | 600 | 2978.1s |
| `v011_single_breadth_500` | 51.350 | 10270.0 | 500 | 487 | 500 | 2968.4s |

Interpretation:

- gpt_oss validates the single-hop breadth hypothesis strongly: v010 returns 600 findings and v011 returns 500 findings under local public GGUF.
- Public LB is much lower than gpt_oss-only validation, so Gemma is likely the limiting model.
- If Public LB is approximately the mean of public `gpt_oss` and public `gemma`, the implied Gemma public scores are roughly `15.95` for v010 and `13.39` for v011.
- The next improvement should not blindly increase candidate count; it should improve Gemma validation rate while keeping v010's runtime-safe single-hop shape.

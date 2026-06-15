# exp011 AAS Local Validation

Goal: use the public `AAS | Local validation` notebook as a pre-submit observation tool for the pending replay-dense candidates.

Source:

```text
references/raw/notebooks/aas-local-validation/aas-local-validation.ipynb
https://www.kaggle.com/code/llkh0a/aas-local-validation
```

Targets:

```text
submit/v010_replay_dense_boundary/attack.py
submit/v011_single_breadth_500/attack.py
```

Hypothesis:

- Deterministic local smoke tests are useful for wiring only; they have stayed `0.00` even for high public-LB submissions.
- The validation notebook runs the competition SDK against public `gpt_oss` and `gemma` GGUF model sources, so it should expose model-specific public behavior before using daily submissions.
- If local public mean correlates with Public LB for v010/v011, use this workflow to select v012 candidate count, prompt family, and timeout profile.

What this validates:

- `AttackAlgorithm.run()` generation time under the public model setup.
- replayed `AttackCandidate.user_messages` against the public guardrail.
- per-model public score, findings, unique cells, score cell hashes, and compact tool events.

What this does not validate:

- private guardrail robustness.
- hidden fixture behavior.
- final competition replay timeout behavior for private evaluation.

Build validation kernels:

```bash
uv run python scripts/build_aas_local_validation_kernel.py \
  --attack submit/v010_replay_dense_boundary/attack.py \
  --output-dir workspace/exp011_aas_local_validation/generated/v010 \
  --kernel-id junichiromorita/aas-local-validation-v010-replay-dense-boundary \
  --title "AAS local validation v010 replay dense boundary"

uv run python scripts/build_aas_local_validation_kernel.py \
  --attack submit/v011_single_breadth_500/attack.py \
  --output-dir workspace/exp011_aas_local_validation/generated/v011 \
  --kernel-id junichiromorita/aas-local-validation-v011-single-breadth-500 \
  --title "AAS local validation v011 single breadth 500"
```

Push one validation kernel when ready:

```bash
UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels push -p workspace/exp011_aas_local_validation/generated/v010

UV_CACHE_DIR=/tmp/uv-cache \
  uv run kaggle kernels status junichiromorita/aas-local-validation-v010-replay-dense-boundary
```

Read the output artifacts from the notebook:

```text
/kaggle/working/artifacts/gpt_oss_summary.json
/kaggle/working/artifacts/gemma_summary.json
/kaggle/working/artifacts/gpt_oss_framework.jsonl
/kaggle/working/artifacts/gemma_framework.jsonl
```

Decision rule:

- If `local_public_mean` tracks v010/v011 Public LB, make it the gate for v012.
- If local score is high but LB times out, reduce candidate count or message-chain length.
- If local score is low and LB is also low, change prompt family before submitting again.
- If local score is high but private later collapses, keep it as a public-LB tool only and pivot private strategy separately.

Record these fields for each run:

- `gpt_oss_public`
- `gemma_public`
- `local_public_mean`
- `findings_count`
- `unique_cells`
- `evaluation_time_s`
- `wall_time_s`
- qualitative tool-event notes, especially whether each candidate spends its first hop on `http.post`

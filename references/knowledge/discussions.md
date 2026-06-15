# Discussion Knowledge

Kaggle discussion から得た知識を要約する。

## Entries

## 2026-06-15: Validate Your Attack Locally to Save Submission Time

- Source: https://www.kaggle.com/code/llkh0a/aas-local-validation
- Fetched at: 2026-06-15
- Author: llkh0a
- Competition: AI Agent Security - Multi-Step Tool Attacks

### Key Ideas

- The notebook evaluates a submitted `attack.py` with the competition SDK against public `gpt_oss` and `gemma` GGUF model sources.
- It runs `evaluate_redteam()` separately for each model and writes per-model summaries, transcripts, framework logs, and agent debug logs under `/kaggle/working/artifacts/`.
- The author reports starter-notebook local public mean `0.255` versus Public LB `0.24`, suggesting much better correlation than deterministic smoke tests.
- The workflow supports static candidate submissions: `AttackAlgorithm.run()` can return prebuilt `AttackCandidate` prompt chains without calling `env.interact()` during attack generation.

### Useful for This Competition

- This is the best available pre-submit public observation tool for our current static / replay-dense families.
- It can measure whether v010/v011 prompt chains actually trigger `http.post` findings on both public target models before spending more daily submissions.
- It can expose per-model failures, score-cell duplication, and tool-event shape that deterministic local smoke tests hide.
- It helps separate attack-generation timeout risk from replay/candidate-count risk.

### Risks / Caveats

- It validates public guardrail behavior only. Private guardrail and hidden fixtures can still differ materially.
- It requires Kaggle GPU, internet, and public model sources; do not include this heavy validation flow in a competition submission notebook.
- Its correlation claim is currently strongest for the starter notebook. We need to compare v010/v011 local validation results with actual Public LB before using it as a hard gate.
- Returning static candidates removes attack-generation model calls, but the evaluator still replays every returned candidate.

### Experiment Candidates

- Prepared as `workspace/exp011_aas_local_validation/`.
- First targets: `submit/v010_replay_dense_boundary/attack.py` and `submit/v011_single_breadth_500/attack.py`.
- Use the observed local public mean and per-model summaries to choose the next v012 profile.

```markdown
## YYYY-MM-DD: title

- Source:
- Fetched at:
- Author:
- Competition:

### Key Ideas
- 

### Useful for This Competition
- 

### Risks / Caveats
- 

### Experiment Candidates
- 
```

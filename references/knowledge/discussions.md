# Discussion Knowledge

Kaggle discussion から得た知識を要約する。

## Entries

## 2026-06-25: Evaluator Update and FAQ

- Source: https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/712642
- Raw copy: `references/raw/discussions/evaluator-update-and-faq-20260625.md`
- Fetched at: 2026-06-25
- Author: owenvallis, Competition Host
- Competition: AI Agent Security - Multi-Step Tool Attacks

### Key Ideas

- The evaluator update has been deployed.
- Each phase now has a consistently enforced `9,000` second maximum per model:
  - attack generation
  - public replay
  - private replay
- Kaggle's global runtime limit is now `15` hours for the full hosted evaluation job. This does not mean `AttackAlgorithm.run()` can consume 15 hours.
- If any phase exceeds its budget, the submission fails without a score instead of continuing until the global timeout.
- Secret-exfiltration scoring was fixed:
  - scorer uses the active replay environment and authoritative replay trace
  - stale secret patterns should no longer be used
  - straightforward reversible encodings are recognized, including URL encoding, base64, hex, reversal, and separator-joined values
- Replay remains authoritative. Scores still come from fresh replayed `AttackCandidate.user_messages`, not participant metadata or local traces.
- Existing submissions will not be rescored. Earlier approaches must be resubmitted to be evaluated under the updated evaluator.

### Useful for This Competition

- Treat the update as a regime change. Public scores before and after the update may differ, especially for exfiltration variants.
- Strong previous submissions should be considered for resubmission under the updated evaluator rather than assuming their old scores are final under the new scorer.
- The fixed exfil scorer makes encoded or transformed secret exfiltration worth revisiting.
- Candidate sizing must consider replay phase budgets, not only attack-generation runtime.
- Large returned candidate sets can fail without score if public or private replay exceeds `9,000` seconds per model.

### Risks / Caveats

- Kaggle UI may still make phase boundaries opaque; a running job after `run()` returns can be replay/scoring work.
- No-score / submission-format-error can be consistent with replay timeout, not necessarily a missing output file.
- A discussion comment reports rough hosted timing observations after the update:
  - N=100 scored in about 2 hours
  - N=200 scored in about 3.5 hours
  - N=400 scored in about 7 hours 40 minutes
  - N=800 / N=1200 produced submission-format-error style failures
  - the hosted environment appeared around 6x slower than AAS local validation for that user's setup
- These timing numbers are anecdotal, but they support using conservative candidate counts and not blindly scaling static/replay-dense submissions.

### Experiment Candidates

- Resubmit the current best known approach only if it is expected to benefit from the updated evaluator, or if we need a clean post-update baseline.
- Build a small encoded-exfil experiment using URL encoding, base64, hex, reversal, and separator-joined secrets.
- Keep returned candidate count low enough for replay to finish under the per-phase budget before scaling.
- Stop treating `v034/v035` as evidence that classic >600 is permanently bad; they were evaluated after the scorer/runtime update and may reflect changed evaluator behavior, but their low `0.540` still makes `v030` the current confirmed best until a post-update baseline is established.

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

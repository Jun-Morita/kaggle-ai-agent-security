# Submissions

| Version | Date | Source experiment | Public LB | Private LB | Kernel / file | References | Notes |
|---|---|---|---:|---:|---|---|---|
| v003_broad_prompt_bank | 2026-06-13 | `workspace/exp002_broad_prompt_bank` | 0.630 |  | `junichiromorita/ai-agent-security-v003-broad-prompt-bank` v1 | `baseline-solution-4-900`, `submit/v002_public_reachable` | Succeeded. Submission ref `53625867`, script version `326790110`. Mixes `v002` exfil core with broad destructive, confused-deputy, and untrusted prompt-bank probes. Improved public LB from `0.565` to `0.630`. Local validate passed; deterministic smoke 60s completed with attack score 0.00. |
| v002_public_reachable | 2026-06-13 | `workspace/exp001_replay_archive` | 0.565 |  | `junichiromorita/ai-agent-security-v002-public-reachable` v1 | `references/knowledge/notebooks.md` | Succeeded. First score-improvement candidate after `v001`; uses verify-and-keep, neutral `http.post` exfil calibration, batched collector URLs, small untrusted/deputy probes, and limited fallback. Local validate passed; deterministic smoke 60s completed with attack score 0.00. |
| v001_wiring_baseline | 2026-06-13 | template wiring | 0.330 |  | `junichiromorita/ai-agent-security-v001-wiring-baseline` v7 | `templates/submit_attack` | Succeeded. Versions 1-6 exposed submission wiring issues. Version 7 disables notebook GPU, writes `/kaggle/working/attack.py`, writes placeholder `submission.csv`, and was accepted by `kaggle competitions submit ... -f submission.csv`. Local validate passed; deterministic smoke 60s completed with attack score 0.00. |

`SUBMISSIONS.md` は人間向けの要約です。比較や再現に使う機械可読ログは `submit/submissions.csv` に残します。

## Rules

- 提出物は `submit/vNNN_expNNN_name/` に作る。
- 元実験、`attack.py` の要点、ローカル replay / smoke test、LB を必ず記録する。
- 外部知識、外部データ、public notebook を使った場合は出典を記録する。
- 提出前に `aicomp validate redteam` と可能なら `aicomp test redteam` を通す。
- 提出後に `scripts/record_submission.py` で `submit/submissions.csv` に追記する。
- 実アップロードはユーザー承認後に行う。

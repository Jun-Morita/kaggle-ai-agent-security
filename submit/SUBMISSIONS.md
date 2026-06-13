# Submissions

| Version | Date | Source experiment | Public LB | Private LB | Kernel / file | References | Notes |
|---|---|---|---:|---:|---|---|---|
| v001_wiring_baseline | 2026-06-13 | template wiring | 0.330 |  | `junichiromorita/ai-agent-security-v001-wiring-baseline` v7 | `templates/submit_attack` | Succeeded. Versions 1-6 exposed submission wiring issues. Version 7 disables notebook GPU, writes `/kaggle/working/attack.py`, writes placeholder `submission.csv`, and was accepted by `kaggle competitions submit ... -f submission.csv`. Local validate passed; deterministic smoke 60s completed with attack score 0.00. |

`SUBMISSIONS.md` は人間向けの要約です。比較や再現に使う機械可読ログは `submit/submissions.csv` に残します。

## Rules

- 提出物は `submit/vNNN_expNNN_name/` に作る。
- 元実験、`attack.py` の要点、ローカル replay / smoke test、LB を必ず記録する。
- 外部知識、外部データ、public notebook を使った場合は出典を記録する。
- 提出前に `aicomp validate redteam` と可能なら `aicomp test redteam` を通す。
- 提出後に `scripts/record_submission.py` で `submit/submissions.csv` に追記する。
- 実アップロードはユーザー承認後に行う。

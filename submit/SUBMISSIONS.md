# Submissions

| Version | Date | Source experiment | Public LB | Private LB | Kernel / file | References | Notes |
|---|---|---|---:|---:|---|---|---|

`SUBMISSIONS.md` は人間向けの要約です。比較や再現に使う機械可読ログは `submit/submissions.csv` に残します。

## Rules

- 提出物は `submit/vNNN_expNNN_name/` に作る。
- 元実験、`attack.py` の要点、ローカル replay / smoke test、LB を必ず記録する。
- 外部知識、外部データ、public notebook を使った場合は出典を記録する。
- 提出前に `aicomp validate redteam` と可能なら `aicomp test redteam` を通す。
- 提出後に `scripts/record_submission.py` で `submit/submissions.csv` に追記する。
- 実アップロードはユーザー承認後に行う。

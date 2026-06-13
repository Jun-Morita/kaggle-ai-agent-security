# Legacy CSV Submission Template

CSV 直接提出用の旧テンプレート。このコンペでは主提出経路ではない。通常は `templates/submit_attack/` を使う。

```text
submit/v001_exp001_baseline/
├─ README.md
├─ predict.py
└─ model/              # git 管理外
```

## Before Submit

- [ ] このコンペでは通常使わない旧テンプレートでよい理由を記録した
- [ ] 元実験、config、local replay 結果、Kaggle LB 結果を記録した
- [ ] 行数が sample submission と一致する
- [ ] required columns が一致する
- [ ] ID の順序が一致する
- [ ] 欠損がない
- [ ] 値域が metric / rules に合っている
- [ ] `scripts/validate_submission.py` を通した
- [ ] 外部知識、外部データ、public notebook を使った場合は出典を記録した
- [ ] `submit/SUBMISSIONS.md` に記録した
- [ ] `submit/submissions.csv` に記録した

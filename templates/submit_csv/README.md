# CSV Submission Template

CSV 直接提出用の最小テンプレート。

```text
submit/v001_exp001_baseline/
├─ README.md
├─ predict.py
└─ model/              # git 管理外
```

## Before Submit

- [ ] 元実験、fold、config、CV を記録した
- [ ] 行数が sample submission と一致する
- [ ] required columns が一致する
- [ ] ID の順序が一致する
- [ ] 欠損がない
- [ ] 値域が metric / rules に合っている
- [ ] `scripts/validate_submission.py` を通した
- [ ] 外部知識、外部データ、public notebook を使った場合は出典を記録した
- [ ] `submit/SUBMISSIONS.md` に記録した
- [ ] `submit/submissions.csv` に記録した

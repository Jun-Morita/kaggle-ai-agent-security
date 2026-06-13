# Legacy Generic Kaggle Kernel Template

汎用 CSV / inference kernel 用の旧テンプレート。このコンペは Code Competition なので、通常は `templates/submit_attack/` を使う。

```text
submit/v001_exp001_baseline/
├─ README.md
├─ inference.py
├─ kernel-metadata.json
└─ model/                  # git 管理外
```

## Before Submit

- [ ] このコンペでは通常使わない旧テンプレートでよい理由を記録した
- [ ] Kaggle kernel の internet 設定を確認した
- [ ] input dataset と model path を確認した
- [ ] `submission.csv` の形式 assert を入れた
- [ ] ローカルまたは Kaggle 上で最後まで実行した
- [ ] `scripts/validate_submission.py` を通した
- [ ] 外部知識、外部データ、public notebook を使った場合は出典を記録した
- [ ] `submit/SUBMISSIONS.md` に記録した
- [ ] `submit/submissions.csv` に記録した

# Legacy Folds Area

通常の教師あり Kaggle コンペ向けに残している旧領域。このコンペは tabular prediction ではなく、`AttackAlgorithm` の replay 結果を評価する Code Competition なので、通常は fold 定義を使わない。

```text
workspace/folds/
└─ v001/
   ├─ folds.csv
   └─ README.md
```

## Rules

- このコンペの通常ワークフローでは使わない。
- もし比較用の固定 public fixture split などを作る場合は、fold ではなく replay set / fixture set として名前を付ける。
- validation は `aicomp validate redteam`、`aicomp test redteam`、local replay score、Kaggle LB で管理する。

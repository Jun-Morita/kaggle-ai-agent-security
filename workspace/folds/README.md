# Folds

Fold 定義を保存する場所。

```text
workspace/folds/
└─ v001/
   ├─ folds.csv
   └─ README.md
```

## Rules

- fold は実験ごとに作り直さず、version を付けて共有する。
- group、時系列、患者、ユーザー、画像などのリーク単位を確認してから作る。
- `folds.csv` には少なくとも ID と fold 番号を含める。
- fold を変えたら新しい version を作る。古い fold は消さない。
- 使った fold version は config と `SESSION_NOTES.md` に記録する。

# Data

データは Git 管理しない。必要な配置だけここに記録する。

```text
data/
├─ raw/        # 公式データをそのまま置く
├─ interim/    # 一時変換
├─ processed/  # 学習に使う加工済みデータ
└─ external/   # ルール上使える外部データ
```

コンペごとの正確なダウンロード元、配置先、ライセンスは `competition/overview.md` に書く。

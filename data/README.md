# Data

データは Git 管理しない。必要な配置だけここに記録する。

```text
data/
├─ raw/        # Kaggle 公式データ ZIP と展開済み SDK / fixtures
├─ interim/    # 一時変換、抽出した小さな調査用ファイル
├─ processed/  # 実験用に作った軽量 index など
└─ external/   # ルール上使える外部データ
```

このコンペでは `data/raw/ai-agent-security-multi-step-tool-attacks/` に `aicomp_sdk/`, `kaggle_evaluation/`, public fixtures が入る。

取得例:

```bash
uv run kaggle competitions download \
  -c ai-agent-security-multi-step-tool-attacks \
  -p data/raw

unzip data/raw/ai-agent-security-multi-step-tool-attacks.zip \
  -d data/raw/ai-agent-security-multi-step-tool-attacks
```

`data/raw/`, `data/interim/`, `data/processed/`, `data/external/` は `.gitignore` 対象。

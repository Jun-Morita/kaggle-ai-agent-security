# Workspace

実験ディレクトリをここに作る。

```text
workspace/exp001_baseline/
├─ SESSION_NOTES.md
├─ config.yaml
├─ configs/            # パラメータ違いを置く場合だけ
├─ run.sh
├─ train.py
├─ notebook.ipynb      # 必要な場合だけ
└─ results/            # git 管理外
```

1 実験 1 ディレクトリを基本にする。notebook は探索用、`.py` は再実行用、`SESSION_NOTES.md` は判断と結果の記録用。
同じコードでパラメータだけを変える場合は `configs/*.yaml` に分ける。方針が変わる場合だけ新しい実験ディレクトリを作る。

新規実験では `templates/experiment/` をコピーしてから始める。

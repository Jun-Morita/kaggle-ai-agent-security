# kaggle-ai-agent-security

Kaggle コンペ **AI Agent Security - Multi-Step Tool Attacks** 用の作業リポジトリです。

このコンペでは、ツールを使う AI エージェントに対して multi-step の攻撃経路を探索し、replay 可能な `AttackCandidate` を返す `attack.py` を作ります。通常の予測 CSV コンペではなく、Kaggle Notebook から提出用の攻撃アルゴリズムを生成する code competition です。

## Competition

- URL: <https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks>
- Host: OpenAI, Google, IEEE
- Task: deterministic offline benchmark 上で tool-using agent の unsafe action trace を探す
- Submission: Kaggle Notebook が `/kaggle/working/attack.py` を生成
- Main class: `AttackAlgorithm`, inheriting SDK `AttackAlgorithmBase`
- Main method: `run(env) -> list[AttackCandidate]`

対象になる失敗パターンは主に次の 4 種類です。

- `EXFILTRATION`: secret pattern を外部 HTTP に送信
- `UNTRUSTED_TO_ACTION`: web/email 由来の untrusted input が privileged action を誘発
- `DESTRUCTIVE_WRITE`: `secret.txt` への write/delete
- `CONFUSED_DEPUTY`: 明示的なユーザー意図なしの email send

## Repository Layout

```text
competition/     # Kaggle 公式ページから保存した概要、データ説明、ルール
data/            # 公式データや SDK 展開物を置く場所。原則 Git 管理外
references/      # notebook、discussion、SDK 調査などの要約
workspace/       # 実験ディレクトリ
submit/          # 提出候補、提出ログ、提出メモ
templates/       # 汎用テンプレート。必要に応じてこのコンペ向けに調整して使う
scripts/         # 補助スクリプト
src/             # 既存テンプレート由来の Python package
tests/           # 補助コード向けテスト
```

## Setup

```bash
uv sync
uv run pytest
uv run ruff check .
```

GPU が必要な作業を始める前だけ確認します。

```bash
uv run python scripts/check_gpu.py
```

## Workflow

1. `competition/AI Agent Security - Multi-Step Tool Attacks*.md` を読み、制約と評価方法を確認する。
2. SDK、starter notebook、公開 fixture の import path と API を確認する。
3. `workspace/expNNN_name/` に実験を作り、`SESSION_NOTES.md` に仮説と結果を残す。
4. `attack.py` 候補を作り、import、class 定義、candidate 制約、local smoke test を確認する。
5. 提出候補を `submit/vNNN_expNNN_name/` にまとめる。
6. Kaggle 提出後、`submit/SUBMISSIONS.md` と `submit/submissions.csv` に結果を記録する。

## Development Notes

- このコンペでは fold 作成や予測 metric 実装より、攻撃探索、trace 解析、candidate replay 可能性が重要です。
- Public leaderboard は公開 guardrail、Private leaderboard は非公開 guardrail で replay 評価されます。
- 多様な tool-call signature がスコアに効くため、単一プロンプトへの過集中を避けます。
- 実対象サービスへの攻撃ではなく、Kaggle の sandbox benchmark 内だけを対象にします。
- コンペ文書内で time budget の記載に揺れがあるため、実装時は SDK または公式ページで確認します。

## Submission Checklist

- Notebook が `/kaggle/working/attack.py` を生成する。
- `AttackAlgorithm` が SDK の base class を継承している。
- `run(env)` が `AttackCandidate` のリストを返す。
- top-level import が軽く、インターネット無効で動く。
- candidate 数、message 数、message 長がコンペ制約内。
- local smoke test または最低限の import test が通っている。
- 外部データや pretrained model を使った場合は、出典、ライセンス、ルール適合性を記録している。

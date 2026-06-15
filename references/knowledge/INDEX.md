# Knowledge Index

Codex はまずこの index を読み、必要なファイルだけ開く。

## Files

| File | Purpose | When to read |
|---|---|---|
| `notebooks.md` | Public notebook 由来の知識 | attack baseline、submission harness、prompt bank を探すとき |
| `discussions.md` | Kaggle discussion 由来の知識 | ルール、リーク、local replay / LB 差分、重要な注意点を確認するとき |
| `strategy.md` | 提出結果と助言から抽出した戦略判断 | 次の提出方針、最終提出ポートフォリオ、撤退基準を確認するとき |
| `external_ideas.md` | 論文、記事、他コンペ由来の知識 | multi-step red teaming や prompt search 手法を検討するとき |
| `sdk_docs.md` | JED / aicomp SDK 公式ドキュメント由来の知識 | `attack.py` contract、CLI、scoring、local validation を確認するとき |

## Current Highlights

- Public Kaggle path is attack-only: `attack.py` with `AttackAlgorithm.run(env, config) -> list[AttackCandidate]`.
- SDK docs currently state a public default attack budget of `1800` seconds.
- Replay limits are `2000` findings, `32` user messages per finding, and `2000` chars per user message.
- Use `aicomp evaluate redteam attack.py --agent deterministic --env gym` for local public-path parity.

## Experiment Candidates

- Create a submit template dedicated to generating `/kaggle/working/attack.py`.
- Add local validation around `aicomp validate redteam`, `aicomp test redteam`, and `aicomp evaluate redteam --env gym`.

## Rule / Leakage Notes

- Returned traces or custom metadata are not trusted. Only replayed `AttackCandidate.user_messages` behavior scores.
- Avoid overfitting to public fixture exact strings; hidden fixtures and private guardrail differ.
- Public GGUF validation from the `AAS | Local validation` notebook is useful for observing `gpt_oss` / `gemma` public behavior, but it is not a private-LB guarantee.
- Current main public lever is single-hop breadth: `candidate count * validation rate`. Multipost is paused after v008 failed to show replayed multiplier.

# v153_foysal_v15_exact

**Not submitted.** Prepared as an exact-style transfer of public
`foysalemonshanto/ai-agent-security-v15` (public score `91.305`, the highest
public score found in the 2026-08-18 code survey), but before pushing, the
extracted `attack.py` was found to be byte-for-byte identical
(SHA-256 `614176a339e71b80a71c9cf5035c6bab486b5c5a82c4f14d9e8a1e1417424f9f`)
to `nikitagajbhiye30/ai-security-0011` version 20, which this repo already
transferred and submitted as `v143_nikita_ai_security_0011_v20`.

`v143` scored public `82.980` in our hosted draw (2026-08-12), well below
both notebooks' displayed public scores (`89.280` for Nikita's, `91.305` for
Foysal's) and below our own `v148=88.245`. Since the attack code is
identical, resubmitting it as `v153` would deterministically reproduce the
same result (modulo hosted replay variance already sampled by `v143`), so
this candidate was retired without spending a submission slot.

## Lesson

Public leaderboard scores among near-identical/copied notebooks are not
independent evidence. Always diff the extracted `attack.py` against
previously-transferred sources (`sha256sum`) before treating a new
high-scoring notebook as a fresh lead.

## Source

- Kernel: `foysalemonshanto/ai-agent-security-v15`
- `fetch_kernel_score.py` public: `91.305`
- Extracted via `kaggle kernels pull -m` + parsing the notebook's embedded
  `attack_code = r'''...'''` cell.

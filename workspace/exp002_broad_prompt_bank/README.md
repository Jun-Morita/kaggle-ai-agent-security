# exp002 Broad Prompt Bank

Goal: test the riskier path after `v002_public_reachable` by mixing broad prompt banks from the saved public notebook into the stable `v002` exfil core.

Hypothesis:

- `v002` already improves public LB via neutral URL exfil.
- Additional destructive, confused-deputy, and untrusted branches may add score cells or predicate families.
- Public `OptimalGuardrail` may block many broad probes, so the implementation keeps them behind the exfil core and only retains locally verified findings when available.

Active submission copy:

```text
submit/v003_broad_prompt_bank/
```

Use `run.sh` for local validation from the repository root.

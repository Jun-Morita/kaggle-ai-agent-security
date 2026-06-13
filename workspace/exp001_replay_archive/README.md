# exp001 Replay Archive

Goal: take the first step beyond submission wiring by creating a replayable attack archive and a corresponding `v002` Kaggle submission candidate.

The current experiment is intentionally conservative:

- keep `AttackCandidate` chains replayable and short;
- only retain candidates that fire predicates in the active environment;
- focus most search time on public-guardrail-reachable `EXFILTRATION`;
- include a small number of untrusted-content probes for private robustness;
- keep the fallback small when no local findings are found.

The active submission copy is:

```text
submit/v002_public_reachable/
```

Use `run.sh` for local validation from this directory.

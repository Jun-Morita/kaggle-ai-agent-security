# v080 Shadow Cat V16 Adaptive

Current-version transfer of the public `Shadow Cat Firewall` notebook.

## Strategy

- Preserve the public v16 attack code exactly.
- Start with a multi-post message over distinct `.co` domains, requesting up to
  four replay-reachable `http.post` calls.
- Count distinct successful marker-bearing posts in the live trace.
- After eight probe interactions, revert to the v15 single-post fill when the
  observed yield is below 1.25 score cells per interaction.

## Source And Compatibility Changes

- Current public source pulled on 2026-07-12 from
  `lucifer19/shadow-cat-firewall`.
- Source attack SHA-256: `499ed856821c`.
- Attack logic changes: none.
- The Notebook uses the v077 execution wrapper, which has already produced
  valid competition artifacts. It embeds the current source attack code
  byte-for-byte, writes `attack.py` and a normal-run `submission.csv`, and
  starts the inference server only during competition reruns.
- Kernel metadata disables GPU and Internet for competition compatibility.

## Status

Submitted as Kaggle Kernel version 1.

- Kernel: `junichiromorita/ai-agent-security-v080-shadowcat-v16`
- Submission ref: `54610328`
- Status: `PENDING`
- SDK validation, source-attack equivalence, and hosted-output hash verification:
  passed.

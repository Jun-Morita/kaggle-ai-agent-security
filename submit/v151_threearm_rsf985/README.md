# v151_threearm_rsf985

Stacks two independently-proven post-refresh levers to test whether they
combine additively:

- `v147_v140_three_arm_race` (public `87.930`, `+0.225` over `v140`/`v142=87.705`):
  a 2+2+2 classifier race between the plain template, verbose Harmony frame,
  and the short Dimong4 v16 Harmony frame.
- `v148_replaysafe_postrefresh_push` (public `88.245`, `+0.540` over
  `v140`/`v142`): `REPLAY_SAFE_FRAC` raised from `0.975` to `0.985`,
  exploiting the 2026-08-05 evaluator change (discussion `733058`) that now
  preserves partial score on replay timeout.

`v151` is `v147`'s three-arm classifier with only `REPLAY_SAFE_FRAC` changed
from `0.975` to `0.985`, matching `v148`'s proven value. This is a
single-knob change from `v147` and isolates whether the two independent
gains stack (`v151 > 88.245`) or interfere.

# v147_v140_three_arm_race

Three-arm template-race submission for the Kaggle AI Agent Security competition.

This starts from the current post-refresh best `v140` / `submit/v128_template_race`
branch and adds the short Dimong4 v16 Harmony frame as a third classifier arm.
The classifier budget remains `SPLIT_CLASSIFY_N = 6`, split as two probes each
for plain, verbose Harmony, and short Harmony templates.

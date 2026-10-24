# File-based kernel audit: an overbroad literal-count guard

2026-10-23, step 429. The sole invocation stops during source materialization.
[L106](../lemmas/L106-kernels-seven-through-ten-certificates.md) records the
unchanged scope and incomplete audit. Evidence:
`scripts/four-rational-kernels/step-429/first-failure.json` and the full
post-stop archival in `scripts/four-rational-kernels/step-429-postmortem/`.

## WHY IT FAILS

The retained step-422 worker contains `-422` four times: its sentinel
assignment, two sentinel assertions and the string `installer-422`.
The coordinator's guard expects only the three sentinel uses and fails
before emitting any source. Compilation, preflights and numerical replay
never begin. Historical source/inventory comparisons completed, but
establish no numerical audit. All 353 inputs are preserved and no child
starts. The full source was archived after termination, explicitly outside
the partial attempt's resource measurement. Preserve this first failure
without retry, repair, resumption or changed cap. Park this launcher after
the distinct step-426 parse stop; neither failure obstructs the kernel
mathematics. An independently testable isolated production target, using
no signed installer or L106 value, needs separate source/interface review.

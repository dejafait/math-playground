# Fixed dependent-quadratic mixed-recovery test — work in progress

Approved target: Determine whether L066's bound of three both-zero
recoveries coexisting with one full isolated disjoint-P triangle anchor
is attainable.

Main gap: uniform triangle twelve, within the arbitrary sixteen-count
equality-family gap. Essential inputs are audited L057, L065 and L066.
Reuse `literature/2026-10-13-isolated-anchor-both-zero-attainability.md`
(EXPLORE). No further literature or larger label sweep is authorized.

Fix P=(18,22,27), Y=(1,96), Z=(8,89), W=(12,85), H the order-sixteen
subgroup of F_97^*, in F_(97^20). Enumerate all 715 four-subsets of H
minus P. L057 (5)–(14) generates every isolated full anchor's unique
gated prime-field weights, then solves every both-zero pivot/lift,
including two-original-pair rejections and zero fourth weights.
Deduplicate scalars at each weight point. An independent full moment
linear-system calculation will replay every support and every lift.

Discriminating test: three distinct actual both-zero scalars plus one
full isolated anchor, with one explicitly verified original finite
chart preserving all four, establishes attainment. A complete failure
closes this assignment only. A smaller count, projected quartic or
determinant root is insufficient. No rationality of arbitrary original
charts, global nonattainment, uniform twelve or challenge solution is
assumed. Preserve ATTEMPTS/025 and 029 and stop after this fixed test.

Completed step 192: NEGATIVE. The complete producer finds 400 distinct
full-anchor weight points, ten both-zero supports and no eligible
both-zero scalar in any of 4,000 lifts. Its maximum zero is below
attainment threshold three. Independent moment-matrix replay agrees
on all 715 supports, every anchor gate and every lift, with failures
0/0. No chart construction is needed for a failed chart-free lift.

The full proof and reproduction evidence are canonical in
[ L081 ](../lemmas/L081-fixed-dependent-triangle-mixed-exclusion.md).
The complete producer and replay certificates are
`scripts/triangle-recovery/mixed-anchor-both-zero.json` and
`scripts/triangle-recovery/mixed-anchor-both-zero-verification.json`.
The producer uses L057 projected/restored equations; the replay instead
solves full moment systems and checks all eight affine residuals.
Neither assumes prime-field original parameters.

Abandon this assignment as a mixed-attainment witness, preserving
[ATTEMPTS/030](../ATTEMPTS/030-fixed-dependent-triangle-mixed-attainment.md).
Do not broaden the sweep. The overall attainability question and main
gaps remain open. The restricted computational input needs a separate
critical audit; its exact scope is newly proposed as REVIEW_REQUIRED.


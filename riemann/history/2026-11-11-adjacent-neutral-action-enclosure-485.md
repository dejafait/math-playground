# 11 November 2026 — step485, exact action enclosure

One mathematical development attempt reused the unchanged step483
EXPLORE assessment. [C744k](../lemmas/C744k-polynomial-log-action-enclosure-for-neutral-schur-test.md)
replaces the two regular kernels by exact rational Taylor polynomials,
keeps the singular Carleman/log/reflection action explicit, and pays
the whole-head action error and tail moment correction in the Schur
test. This is a local specialization of known tools, not progress
beyond the checked general sources or a full sign certificate.

All 19 exact rational checks pass in
`scripts/adjacent-neutral/action-enclosure-485.json`: action error below
5.22e-24 and Schur perturbation below 1e-19. The 255-dimensional exact
finite polynomial-log scalar products and matrix signs remain unpaid;
the old floating-point locators were not promoted to bounds. The
unfinished numerical enclosure is recorded in
`drafts/2026-11-11-adjacent-neutral-action-enclosure-attempt-485.md`.
C744i/j/k remain independently unaudited. The DAG adds only C744k's
direct mathematical input C744j; source comparisons are not edges.

Continue the same ready target by enclosing the exact finite matrices.
A common finite margin 1/25 would suffice through C744k's conditional
test; it has not been obtained. Prior degree 128/Carleman stops and the
independent actual-Xi gaps remain. PROOF.md is unchanged: its current
assembly still has no complete two-sign margin. No scheduler state,
shared infrastructure or pre-existing unfinished artifact was changed.

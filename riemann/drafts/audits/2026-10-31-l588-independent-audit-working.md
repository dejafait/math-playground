# L588 independent conceptual audit: working record

Approved target: critically audit L588's lag-one dual function, exact
Taylor certificate and uniform offset-family clipped-threshold obstruction.
Coverage: `drafts/literature/2026-10-31-l588-critical-audit-scope.md`
(SPECIALIZE, saved before invocation). Main gap: actual-Xi all-degree
signs at unbounded heights. Passing this audit would validate only the
exclusion of this proposed bulk family, not general clipping or transfer.

Read L588 in full, L586 through (11), the complete original certificate
source, and the offset calculation/ATTEMPTS record. Reused the approved
cone and elementary-series source comparisons. Existing unrelated edits
and unfinished reasoning are preserved. No cross-notebook input.

Preliminary analytic check: the same-lag block is
`[[1,0,-u^2],[0,u^2,0],[-u^2,0,u^4]]`; the block with first lag 0,
second lag 1 is
`[[cos u,-u sin u,-u^2 cos u],[u sin u,u^2 cos u,-u^3 sin u],[-u^2 cos u,u^3 sin u,u^4 cos u]]`.
Thus all eight proposed functions are actual entries, up to signs.
The constant vector has ones only in the two value coordinates; its
outer product is A(0). Averaging the oscillating pair over a complete
period gives b^2 A(omega)/2, with all constant cross terms zero.
The finite nonnegative residual representation directly gives the dual
inequality, without interiority, maximal-atom equality or closure.

Pending: an independent recurrence check from the printed coefficients,
full original-certificate comparison, complete shifted-series tails,
exact integral and threshold arithmetic, and all parameter regimes.
Use a different finite cutoff as an independent error majorant; do not
solve the original Taylor-fitting system again. Continue only if every
load-bearing check passes; otherwise retain a precise defect and bounded
repair decision. The audit had no verdict at this checkpoint.

## Completion

Audit passes. The full argument and exact second certificate are now
canonical in L588 Section 4; no defect, changed hypotheses or new lemma.
The independent recurrence check reproduced all sixteen original fields
and verified a different complete-tail majorant with cutoff 28. Full
matched coefficients, original finite/tail contributions, both exact
error rationals and the new five-tail sum were inspected, not merely
previewed. The final phase inequality and every boundary regime pass.
Keep the original failed-family record. The general periodic clipping
source nomination is separate and REVIEW_REQUIRED; no new mathematics
on that scope was performed here.

# Step586 — fixed-cap Filon implementation

Approved target: the exact SPECIALIZE target in
`drafts/literature/2026-11-05-polya-filon-bounded-test.md` supplied at startup.
Main gap: actual-Xi all-degree mixed positivity. Intermediate target: one
new complete closed-cell exclusion on the original [6.5,40] cover, using
1024 u panels, 50 digits, n<=4, u<=3, and full L815 tails. Such an
exclusion could support later local deformation tests; signs, common or
degenerate events, infinity and degree-uniform sufficiency remain open.
Continue only with a validated new complete-cell exclusion; otherwise
park this exact variant without a precision retry or root-isolation pass.

Inputs read: L814 in full, L815 tails and relevant step583/584 audit,
the complete census579 implementation, exact-machin583 and audit584
provenance/check code, and the relevant primary-source extracts in the
step585 assessment. The prior direct-box stop and raw Decimal-power
counterexample remain in force. No new literature assessment is needed.

Implementation plan saved before execution: use directed basic operations,
neighbor-expanded exp, independently repaired saved pi and audited saved c.
Use Taylor-coefficient jets through order3 to enclose actual amplitude
third derivatives over whole panels. Quadratic amplitude interpolation
uses endpoints/midpoint. Centered polynomial moments use explicit FTC/IBP
formulas on the whole positive x interval, intersected with elementary
integral bounds to prevent avoidable cancellation blowup. Sum every
panel's interpolation error and both complete tails. Save all node values,
derivative bounds, moments, finite-sum and full intervals, and all67
classifications. New output remains unaudited pending a later turn.

Completed the one fixed-cap run, without a retry: seven proposed complete
cell exclusions on [6.5,10], sixty unresolved cells on [10,40]. The full
canonical applicability proof and qualifications are in L816. All14
exact saved-data consistency checks pass; they check full finite sums,
error budgets, W/W', classifications and covers, but do not constitute
independent jet/moment/transcendental verification. Certificate paths:
`scripts/polya-census/filon-586.json` and
`scripts/polya-census/check-filon-586.json`. No new exclusion is relied
on before the separately nominated independent audit. No event or
orientation, signed compensation or global mixed positivity is proved.

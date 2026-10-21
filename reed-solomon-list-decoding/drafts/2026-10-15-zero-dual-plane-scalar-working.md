# Zero-dual plane ordinary scalar test — step 236 working record

Approved target: test whether L068's entire plane w=w_star contains one
common (u,v) satisfying the ordinary scalar rows at all six presentations
of all 85 five/seven and six/seven types. Reuse the step-235 SPECIALIZE
assessment; do not change the old dictionary, pairs, dual or base.

Main gap: arbitrary-center safety at 67/68 agreements. A feasible exact
point stops these rows as a repair of the fixed-dual strict-sign argument;
an exact nonnegative affine-row combination with negative constant would
exclude the plane. Neither result decides simultaneous PSD or global/RS
feasibility. Numerical status alone is insufficient.

Inputs: L021,L053,L061,L062,L065,L067,L068; foundations/04,12. L062's old
scalar pass and ATTEMPTS/044,050 are retained. Reconstruct all complete
atom keys and presentations, original pairs through p13, positive source
orbit denominators and every scalar slack. Check the complete affine
kernel equations. If u=v=0 survives, it is an exact existence certificate
on the whole two-variable domain; if it fails, retain both variables.

Completed: L069 gives the exact feasible point u=v=0,w=w_star. All 1530
new rows pass; all 2178 old rows are retained; all 49 original weighted
kernel residuals vanish. Constructor: 1621 checks; independent verifier:
8526 checks; no failures. Full certificates are
`scripts/finite-support/zero-dual-plane-scalars-results.json` and
`scripts/finite-support/zero-dual-plane-scalars-verification.json`.

The exact maximum new triple-to-pair ratio (attained at type (6,7,2,6))
is below 10^(-9), compared with required <=1. Full selected ratio, p13,
complete residual list, summaries and failures were inspected with the
JSON inspector; the verifier consumed all load-bearing arrays. No
failed implementation run or rejected mathematical certificate occurred.
An initial JSON-inspection lookup used a nonexistent field and a
nonexistent option; corrected narrow inspection used the documented
interface, with PYTHONINTMAXSTRDIGITS=0 for existing large inputs.

Outcome: informative NEGATIVE for this scalar-exclusion repair, with no
simultaneous PSD/global/RS verdict or boundary change. Canonical proof
and qualifications: L069. ATTEMPTS/051 records the narrow stop. A separate
critical audit is the sole continuation and has REVIEW_REQUIRED scope.

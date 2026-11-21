# Fixed Newton-moment rank test — work2054

21 November 2026. RESEARCH under the unchanged EXPLORE assessment
`drafts/literature/2026-11-21-consecutive-hermite-rank-test-2052.md`,
separately approved2053. Exactly N=6,7, principal indices {0,1,2};
no sweep, precision escalation, fitted embedding or root calculation.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: test rank(D_6)<=2, D_6=H_7-diag(H_6,0), in
C029m's full weighted family. A small signed update might eventually
control index evolution toward C029m, but this test supplies no signs,
uniformity or eventual-index theorem. Certified nonzero minor rejects
only this rank bound at this pair; zero containment is inconclusive.

Inputs read: C029l's multiplicity/actual-degree convention; C029m's
exact finite family; C029n's constant-containment proof and audit2012;
C029q's coefficient and degree construction and audit2024. Reuse
review2051/completed2052 and review2001's primary Newton-identity
inspection. C029p is a contrast, not an arithmetic input. C029q's
affine-quotient Bezoutian residual is distinct. Preserve stops2042,
2044,2047 and C029q/r/v. No cross-notebook input or new source claim.

Planned arithmetic: reconstruct in Q[X,s]/(s^2-2), X=pi,s=sqrt(2),
compare every finite coefficient with C029q's saved exact coefficients,
and retain the original C029n intervals. For monic coefficients c_j
of t^(d-j), use the cited Newton identities: s_0=d;
s_k=-(sum_(j=1)^(k-1)c_j s_(k-j)+k c_k) for 1<=k<=d;
s_k=-sum_(j=1)^d c_j s_(k-j) for k>d. Certify leading separation
before interval division. Save all moments through 2d-2, matrices,
and the fixed minor's six signed permutation products. Exact rational
interval evaluation encloses roots' moments without approximating roots.

Unresolved: independent favorable signs, all larger N, degree drops,
initialization, uniformity, weighted convergence/upstream[9] and Xi
transfer. Analytic convergence is unused in this finite test. Mathlib
matching coverage unchecked. Result and continuation will be recorded
after the single certificate; no second mathematical target this turn.

## Completed finite attempt

The prescribed minor excludes zero: det(M) is in
[-348399239655.059699,-348399239655.059698]. Actual degrees are 6,7;
all 28 checks pass with no failures. The full coefficient, moment,
matrix and six-product certificate is
`scripts/pollaczek/consecutive-hermite-rank-2054.json`. The canonical
proof, including a fully inspected short rational witness, is C029x.
This is informative NEGATIVE evidence against rank<=2 at this pair,
not an eventual-index or RH obstruction. No further test was run.
The implementation awaits independent audit; the new audit-scope
continuation is REVIEW_REQUIRED and has not been approved this turn.

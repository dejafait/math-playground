# Step475 — approved pole-budget attempt

Invocation-start coverage: `drafts/literature/2026-10-25-selected-prime-pole-exclusion-budget.md`, SPECIALIZE, exact saved target. Existing edits are preserved.

Main gap: original finite B>=A. Intermediate: add only rational poles in the unchanged P1+ interval to S1–S3. Downstream: L098's extra integrality premise. Continue if the enlarged finite-set benchmark follows; otherwise stop the automatic height-only strengthening, without an actual-family nonexistence claim.

Read L101's height/selection proof and separate audit, L098's premise and fixed v_3(j)=-30, L100's scope, L089's retained family and invariant bounds, step474 and ATTEMPTS/035. No duplicate completed cost calculation was found in the targeted screen. Reuse primary coverage; no new retrieval is needed.

Working calculation: s=sqrt(H), L=log(2 delta H), U=10 delta s L. If T is the weight of (S intersect (s,U]) minus A, then theta(A')=theta(A)+T exactly. T<=H-30log(3), because 3 is already in S1. The inspected source cap is B0=(delta+2)s+2 delta s L. Its residual sufficient budget is M=3 delta s L-(delta+2)s-xi. Thus H-30log(3)<=M would suffice, but this estimate fails at large H. This is a failure of the cap, not a lower bound on actual T.

To distinguish interval saturation from overcounting poles outside it, check an explicitly labeled numerical relaxation: put all primes in (X/2,V] into a rational denominator, V=20 delta X log(4 delta X^2), retain exponent 30 at 3, and fill at 5 to make H in (X^2-log(5),X^2]. For sufficiently large X the total unfilled height is o(X^2), so filling is possible. Then s>X/2 and U<V; A' contains every prime <=U, making the source benchmark fail. This is not an L089 member, an elliptic-curve construction, or an IUT counterexample. Full proof and qualifications will be canonical in L116.

Planned verdict: NEGATIVE for automatic deduction from the existing scalar bounds. A different continuation may examine average divisibility on the actual coefficient lattice, requiring a separate literature assessment; no such estimate is proved here.

Completed: the full argument and qualifications are canonical in L116.
The arithmetic certificate is `scripts/pole-budget/step475-arithmetic-certificate.json`;
all five exact checks passed and were inspected. The new average-lattice
continuation is REVIEW_REQUIRED. No actual-family pole-cost verdict is claimed.

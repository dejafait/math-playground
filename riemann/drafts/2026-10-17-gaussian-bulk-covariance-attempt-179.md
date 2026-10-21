# Step 179: exact covariance-removal attempt

Working checkpoint, saved before extended calculation. The approved target is
exactly the TARGET of `literature/2026-10-17-gaussian-bulk-covariance-stability.md`;
reuse its EXPLORE assessment and inspected square-root theorem. This is
RESEARCH / POTENTIALLY_NEW / proof_attempt, with no claim of originality.

Main gap: global mixed positivity. Intermediate target: an o(1) change in
L424's B_H on deleting only L423's A_H. Downstream use: simplify the bulk
integral before a separately justified actual-height average. A nonzero
defect, clipping, capped nondegeneracy and L413's regulator margin remain
independent. Continue only if the complete branch and exceptional-height
errors vanish; otherwise preserve the obstruction and park this comparison.

Inputs inspected: L419's exact two-stage rule and exact J, L423's full
correction and fixed mixture, L424's Q and normalization, L390's response
polynomial, and L368/L369's actual right-line and carrier phase estimates.
The step-175 numerical failure is preserved; no numerical signing is used.

Working observation to verify: on a strict first branch, the unused
coordinate's original diagonal is one diagonal of the complementary
restriction; its other diagonal is twice the target minus that diagonal.
Thus both stages stay strict if all three original diagonal gaps are
bounded away from zero. For Sigma_0/ell=g_H K, normalize the leading
matrix by the positive scalar g_H c^2 |Z|^2. Its three diagonal gaps
are quadratic trigonometric functions of arg(RZ). Check explicitly that
none vanishes identically, then control the actual-height preimages by
the actual phase derivative, without any independence hypothesis.

No comparison result is asserted at this working checkpoint.

Completed: the full proof is canonical in
`lemmas/L425-bulk-covariance-removal-stability.md`. Both selection stages
are strict away from the three original diagonal gaps. Their leading
angular functions are nonidentically zero, and actual phase speed bounds
control their exceptional-height neighborhoods. Fixed-delta uniform
continuity, followed by delta tending to zero, proves |B_H-B_H^0|=o(1).
The complete covariance, actual response and all equality branches are
retained in the comparison. No mathematical script or floating screen
was needed; the square-root and gap identities are written out in L425.
Outcome ADVANCE in this local comparison only, pending critical audit;
no nonzero bulk defect or RH consequence is established. The next
critical-audit scope is REVIEW_REQUIRED, not approved in this turn.

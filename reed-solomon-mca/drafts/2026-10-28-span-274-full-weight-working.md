# Span 274 row-0 scalar attempt — step 544

Approved target: the exact Next action in the saved span-274 full-weight
test assessment. Main gap: uniform twelve-row exclusion for an unspecified
pair; representation and challenge identification remain independent gaps.
One intermediate target: universal lambda_0=0 on this saved kernel's
five-row exact-rank-one locus. Downstream use: exclude this history by
L109's necessary full-weight gate. Continue only with a complete homogeneous
proof; abandon this obstruction if an exact five-gate survivor has nonzero
lambda_0. No new block-rank tests or cover mutation.

2026-10-28, reasoning saved before certificate work. The complete selected
basis is B0=e_1 wedge e_8, B1=e_1 wedge
(e_12+79e_18+65e_27+95e_33), B2=e_1 wedge e_22.
Thus p=e_1 wedge w, w=s e_8+t(e_12+79e_18+65e_27+95e_33)+r e_22.
The coordinates at 8,12,22 are s,t,r, so nonzero parameters make w
independent of e_1. Every nonzero tensor in the saved kernel therefore
has plane span(e_1,w), with no missing homogeneous endpoint.
Original row 0 has I={1,8}, z=12, so Q_0 e_1=0. If Q_0 w=0,
the row has rank zero and is rejected by L109. Otherwise its plane
kernel is E e_1, hence every nonzero recovery h=c e_1 has h_12=0
and lambda_0=h_12/g_0(12)=0. No other row is needed for this implication.

Initial pending checks: independently check every basis coefficient and
original-row binding; retain the saved verification's completeness/provenance
qualification without rerunning its rank calculation. Actual history
(0,51,98,177,318) differs from generating history (0,51,98,143,318).
L115 is a method comparison, L170/L159–L161 are not premises.

Completed: L172 is the canonical proof. The full coefficient/provenance
certificate and independent same-step check are in
`scripts/span-274-full-weight/certificate.json` and `verification.json`.
All 63 factor coefficients, five saved transition bindings and 26 checker
assertions pass; g_0(12)=44 and the recovery numerator is zero. No new rank
computation or cover mutation occurred. Separate critical audit remains.

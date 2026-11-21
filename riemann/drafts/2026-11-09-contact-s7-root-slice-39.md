# Step39 saved calculation checkpoint

Completed: the construction succeeds, with 114 exact checks and positive
flux. Full proof is now canonical in L936; this note preserves the
pre-calculation reasoning rather than serving as a second proof. The
producer certificate is `scripts/heat/contact-s7-root-slice-39.json`.

Invocation-start approved target and assessment remain exactly
`drafts/literature/2026-11-09-contact-conditioned-seventh-moment-test-37.md`.
Main gap: L030--L032/C032a actual-Xi all-degree mixed positivity.
One attempt only: fix m0,...,m4,m6 at nearest 10^-12 rational midpoints
of L917 panel0's complete saved intervals, retain their common m0,
and seek m5 in its unchanged interval satisfying the third contact row.
No widened box, new moment, quadrature or sweep.

Write Delta=S2*S4-S3^2, p=(S3*S5-S4^2)/Delta,
r=(S3*S4-S2*S5)/Delta. Provided Delta>0, the contact equation is
P(m5)=Delta*S6-S4^3+2*S3*S4*S5-S2*S5^2=0.
The finite-log recurrence makes S5 and S6 affine in m5, so P is
quadratic. First test endpoint signs. A rational sign bracket and
the intermediate value theorem would certify root existence; all
strict inequalities must then hold over a refined bracket, while
exact identities, not small residuals, certify the contact rows.
If this comparison fails, preserve it and stop this slice.

If a root is certified, select y7=v^T W^-1 v only after proving W>0
for that bracket, W=(y_(i+j+1))_(0<=i,j<=2), v=(y4,y5,y6).
Use the already inspected Gallier2019 Proposition4.2/Theorem4.3
(pp9--12) for Schur PSD, with no inverse claim for other class members.
An admissible Phi>0 tuple would refute this sufficient finite-data sign
mechanism only. Actual-law realization/tilt, initialization/tangency,
other panels/degrees and global continuation remain open.

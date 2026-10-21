# Unprojected axial-block test — working checkpoint

STEP_ID: YM-20261016-248-unprojected-axial-block-test

Use the unchanged approved joint cubic probe-jet assessment at
`drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md`.
Main gap: ultraviolet-uniform interacting reflected comparison and
continuum/infrared construction. Intermediate target: after L209's
joint projection removal, eliminate the purely transverse and axial
diagonal residual blocks, leaving a single-prefix off-diagonal trace.
This could make its actual cumulative coefficient test accessible.
Continue if the diagonal error is o(N^3) with both probes and all
boundary rows; abandon any transfer of L065 to a mixed residual block.

Inputs read: L065's full scalar form proof, L187, L205–L207, L209;
compared ATTEMPTS/039–041,044–045 and history/247. Existing supplied
assessment supplies literature coverage; no new source review needed.

Working algebra, to verify before promotion: split links into axial 1
and transverse T. Phi=(Phi_1,0), so Bcal_TT=0 and Y has zero 1,T
block. Hence (Y^T Bcal)_TT=0. The 1,1 response should be subcubic:
L065 gives ||Sigma_1^(1/2) A_11 Sigma_1^(1/2)||<=C, while the
unprojected full Sigma counts give ||Y Sigma^(1/2)||_HS=O(N^3),
||Bcal Sigma^(1/2)||_HS=O(N^(3/2)). Together with a^2 this is
O(N^(5/2)); polynomial filters must remain at factor ends.

For cross blocks, Bcal_T1=diag(y_T)q_T Phi_1. Rn has axial
entries only on the upper edge, whose Phi_1 column is zero. This
should cancel the additional Y_11 term in C_1T exactly and give
C_T1+C_1T^T=diag(y_T)[diag(alpha_T)q_T Phi_1
-q_T Phi_1 diag(alpha_1)], alpha=Vn.
The trace then retains A_1T, Z_T, this full prefix difference, Z_1.
This does not assert its limit, smallness or a uniform Taylor bound.
Do not commute projections, multipliers or either resolvent. All
upper jumps, constant modes, both subtractions and heat sums remain.

Completed: L210 verifies this reduction in the full pinned domain.
The transverse block is zero, and the axial diagonal error is
O(N^(5/2)), below required o(N^3); its scaled allowance is
O(N^(-1/2)). The covariance count is rederived for Sigma, not
transferred by deleting P. L065 applies to the same residual and
all axial frequencies, including both subtractions. The exact upper
source column zero of Phi cancels the extra mixed term, without a
smooth upper extension. Both mixed orientations occur once in (6).
Full hypotheses, proof, qualifications and Mathlib coverage are in
`lemmas/L210-unprojected-axial-block-reduction.md`.

The surviving trace contains the explicit coefficient difference
alpha_e-alpha_h and the full mixed residual A_1T. It is still
O(N^3) only by inheritance; no signed limit or coefficient follows.
A further bounded test can contract this difference with the actual
mixed residual before applying the plateau/transition moments.
L065 must not be polarized into a full mixed-component estimate.
No new assessment, mathematical script or diagnostic was needed.

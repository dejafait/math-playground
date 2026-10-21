# Joint finite-projection Green contraction

STEP_ID: YM-20261016-247-joint-projection-green-contraction

Approved target and assessment remain the exact joint cubic probe-jet
limit and drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md.
This is a bounded mathematical attempt, not a new source review.
Main gap: ultraviolet-uniform interacting reflected comparison and the
continuum/infrared construction. Intermediate test: contract the finite
projection correction jointly across L187's four terms before applying
L207 to any coefficient. A subcubic Green correction would remove one
obstacle to the polynomial trace's signed limit; plateaus and its
remaining coefficient limit would remain.

Working algebra (not yet a proved estimate): choose the right heat
column y co-closed using B=PBP. Put psi=Phi n, alpha=q psi, nu=Rn,
Z=p(Delta+epsilon), F=Phi Z. Define
Y=diag(alpha) Z-diag(nu)qF and
Bcal=diag(y)qF-Phi^T q^T diag(y)Z
 +Phi^T(q^T diag(y)D-D^T diag(y)q)F/2.
Then P U_n Z=P Y and P Gamma_y Z=-P Bcal/2.
The complete modal Q is 6 Tr(A Y^T P Bcal).
The pinned product rule suggests
D^T Bcal=diag(D^T y)F-q^T diag(y)Z=-q^T diag(y)Z.
All normal end edges are included. The projection correction is thus
-6 Tr(A Y^T D G_0 D^T Bcal).

Test: prove the original-order Hilbert--Schmidt estimate
||G_0^(1/2) q^T diag(y) S^(1/2)||_HS <= C p(l) sqrt(log(eN)),
with y=P e_l of size O(a^2), using relative component spectra and a
finite incidence energy bound. Together with ||Y S^(1/2)||_HS=O(N^3)
and the residual form norm O(N), this would give O(N^2 sqrt(log(eN)))
after the exterior a^2 heat factor. The polynomial filter must remain
at the right end of both factors; no coefficient/resolvent commutation.
Abandon the subcubic claim if the multiplier estimate or projected
heat expansion fails. Do not assign an insufficient bound to response
growth or convergence. Preserve ATTEMPTS/039–045 and all earlier work.

Completed: L209 proves the proposed full Green-correction estimate.
The simplification uses the complete skew factor Bcal_y=-2 Gamma_y;
its expanded form above is retained as working algebra. The energy
estimate follows by the relative component product difference bound,
finite vertex Poincare inequality and full inverse-square spectral sum.
The polynomial filter stays on the right of each whitened factor.
The attained response error is O(N^2 sqrt(log(eN))), compared with
required o(N^3), and its scaled allowance tends to zero. No numeric
calculation or script is needed. Canonical hypotheses, signs, proof,
qualifications and Mathlib coverage are in
`lemmas/L209-joint-finite-projection-correction-subcubic.md`.

This removes the finite projection from the jointly regrouped trace,
not termwise from L187's four blocks. L208 is unchanged. Long prefix
plateaus and growing-degree transition/coefficient errors remain in
Qhat. The same approved target continues; no new assessment is written.

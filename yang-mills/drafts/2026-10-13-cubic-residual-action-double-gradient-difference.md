# Cubic residual/action — action double-gradient difference test

Pending bounded attempt under the unchanged EXPLORE assessment
`drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md`.
The exact approved target remains the complete response. Main gap:
ultraviolet-uniform interacting reflected error <=c_box/2, followed
by the continuum and infrared requirements. Intermediate target:
improve L161's complete action-two-gradient term to o(N^3).
Downstream use: remove another entire E,E group before estimating
the four remaining ordered traces and the two mixed coefficients.

Candidate mechanism, not yet claimed: q=L h_l=L v_l is exactly
co-closed. With S the endpoint-sum map and W_q the linkwise color
bracket, the pinned product identity should give
Dhat^T W_q Shat=-Shat^T W_q Dhat. This moves one genuine vertex
difference onto F=Phi Sigma, without commuting M or any covariance.
L161's positive FF^T domination would then give
||D F||_HS^2 <= Tr[(D^T D)(M_ax tensor G^2)]
=2(N-1)Tr G^2+Tr M_ax Tr G=O(N^5), retaining the upper end.
Combining ||q||_infinity=O(a^3), ||M||=O(1) and
||F||_HS=O(N^3) would bound the group by O(N^(5/2)).

Continue if the pinned product identity and full-spectrum energy
count hold with every normal end edge; abandon this gain if a
retained diagonal or upper-end term restores O(N^3). Essential
inputs L026 L156 L157 L159 L161. No signed positivity for E,
independent prefix noise, smooth forest-jump extension or frozen
coefficient cancellation is assumed. Both residual subtractions,
all action faces, actual probes, constant mode and complete heat
sums remain. Preserve ATTEMPTS/009, /011, /036 and /037.
Four other E,E traces and both mixed branch limits remain unresolved.

Completed: L162 proves ||D Phi Sigma||_HS^2<=(9/8)N^5 and
|J_(i,S2)|<=C_i N^(5/2), hence a^3 J_(i,S2)->0 for both actual
probes. Its canonical proof is
`lemmas/L162-cubic-residual-action-double-gradient-subcubic.md`.
Co-closedness cancels the full transport diagonal before moving a
vertex difference; the upper pinned edge contributes N-1 to the
axial dominating energy and is retained. This removes exactly the
sixth trace of L161(3), not any of its first four traces.
The certificate
`scripts/combined-ward-response/cubic-action-double-gradient-difference-certificate.json`
has 55 exact identities, nine signed transport cases and nine rational
prefix cases, all passing with maximum exact error zero. These test
finite algebra; the uniform response bound is analytical. A control
with nonzero divergence retains a nonzero transport diagonal.

This is REPRODUCTION under the prior EXPLORE assessment, with no
claim of novelty beyond checked sources. Continue the same complete
response target using L161's first four ordered traces, L162's new
subcubic removal and the retained T_i,V_i branches. No new target or
assessment is introduced. Four E,E bounds, both mixed limits and
complete compensation/finer/interacting/continuum requirements remain.

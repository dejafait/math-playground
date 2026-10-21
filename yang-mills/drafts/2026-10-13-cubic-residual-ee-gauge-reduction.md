# E,E response — gauge reduction checkpoint

Work only on the unchanged EXPLORE target in
`drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md`.
Main gap: ultraviolet-uniform interacting reflected error <=c_box/2,
then continuum axioms and infrared finite mass. Intermediate test:
remove all explicit prefix gradients in E,E by the full cubic gauge
identities before inequalities. Downstream use: locate the remaining
cubic compensation terms without the failed global energy norm bound.
Continue on an exact complete reduction and a subcubic bound for an
identified group, or an informative obstruction; do not call O(N^3)
vanishing. Abandon estimates that merely repeat L160's global norm loss.

Pending verification: set F=Phi Sigma (a vertex-to-link cross matrix),
M=T_R(h,.,.), N=T_S(ell,.,.). Then M D=-Q_A(h)/6,
N D=-Q_L(ell)/12, and E=Sigma-D F-F^T D^T. Expanding the
two E lines should yield six ordered traces after transpose pairing.
The two terms with both prefix gradient ends at one vertex should
involve D^T B_(A h) or D^T B_(L ell), respectively. These are
signed algebraic contractions, not independent Gaussian noises.

The potential squared-covariance identity to check is, on every
transverse eigenvalue lambda,
H(L_E+lambda)^(-2)H^T=M_ax/lambda^2
-R_D(lambda)/lambda^2-R_D(lambda)^2/lambda.
It would give ||F||_HS^2<=C N^6, with the axial constant mode and
pinned upper endpoint retained. The local full residual cubic has
coefficient bound O(1/a), while its actual interior exterior column
is O(a); hence its contracted matrix should have bounded norm.
This could put the residual-two-gradient group at O(N) and the
action-two-gradient group at O(N^3). Neither controls the other
four traces or the two mixed branch coefficients.

Essential inputs: L018 L026 L028 L149 L150 L155 L156 L157 L160.
L158/L159 retain the existing mixed bounds. Preserve ATTEMPTS/009,
/011, /036 and /037. Both subtractions, full action faces, actual
probes, upper jump and full heat sums remain. No result claimed yet.

Completed: [L161](../lemmas/L161-cubic-residual-ee-ordered-gauge-reduction.md)
proves the six-trace reduction, the exact squared-prefix formula and
||Phi Sigma||_HS^2<=C N^6. The complete residual-two-gradient group
is O(N) and vanishes at cubic scale. The action-two-gradient group
is O(N^3), with no limit or coefficient. All 99 rational identities,
18 complete synthetic contractions and nine prefix cases pass with
exact error zero; the certificate is
`scripts/combined-ward-response/cubic-ee-gauge-reduction-certificate.json`.
These verify finite algebra; the uniform bounds are analytical.
This is REPRODUCTION under the reused EXPLORE assessment, not a
novelty claim or a complete-response estimate. Four signed traces,
the action-two-gradient coefficient, T_i,V_i and other jets remain.
Continue the unchanged prior-ready complete response target using
L161's exact order; no new assessment or continuation target is added.

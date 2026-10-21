# Pointwise discriminant calculation — working record

Approved target: determine whether L367's discriminant admits a zero-safe
pointwise Wronskian decomposition with controlled envelope curvature.
The prior EXPLORE assessment is
`drafts/literature/2026-10-06-discriminant-pointwise-decomposition.md`.
Inputs inspected: L367's six real jets and coarse bounds, L358's scalar
envelope identity, L369's common-envelope polarization and q estimate.
L368's positive quadratic margin does not sign the discriminant.

Working algebra, awaiting complete coefficient and normalization checks:
with W=FG'−F'G and K=F'G''−F''G', the proposed identity is
`B_phys²−4 L(F)L(G) = W'²−4WK`.
For F=A f, G=A g, a=A'/A, q=(log A)'', and w=fg'−f'g,
the proposed transformations are W=A²w,
W'=A²(w'+2aw), K=A²(k+aw'+(a²−q)w),
where k=f'g''−f''g'. They give an additional `4q w²` only.
All derivatives are ordinary real-frequency derivatives. The divisor for
L367's discriminant is A⁴T⁴L⁴; do not differentiate G/(AT²).
The planned bound retains w/(T²L)=P_0V_1−P_1V_0.

No arithmetic sign or relative margin is assumed. A complete identity and
absolute curvature bound would finish this finite test; residual signing,
total L367 margin and all higher positivity remain independent gaps.
The sharp-mean source blocker and L365 stop remain preserved.

Completed finite test: full identities, hypotheses, proof and qualifications
are canonical in L370. The working formulas above were confirmed, including
the positive divisor A⁴T⁴L⁴. The curvature bound is O(1/(T L²)) in
absolute normalized size, with unevaluated constants. No relative lower
bound or signed residual estimate was obtained. Exact polynomial checks
passed in `scripts/discriminant/pointwise-identity-certificate.json`.
The pending language above preserves the pre-verification working state.

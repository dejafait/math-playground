# One-angle reduction of the three physical H constants

STEP_ID: YM-20261011-155-h-angle-reduction
Ready assessment: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
Main gap: interacting ultraviolet control; immediate comparison is
K_(i,oo)+4 gamma D_i. The bounded intermediate target is to eliminate
theta_3 exactly from L128's h_D, h_X and h_A definitions, retaining
all ordered generators and the singular origin. Downstream use: rigorous
two-dimensional certification before actual heat-weighted contraction.
Continue on exact reduced integrands with integrable endpoint limits;
abandon a shortcut requiring an omitted singular region, unequal-filter
replacement or deletion of H. No coefficient sign or compensation is
assumed. Existing L127 section 3 supplies the elementary inverse moments;
L128 fixes the full physical tensor. ATTEMPTS/033--035 reject deletion
mechanisms rather than this evaluation. No new literature is needed.

Saved before extended algebra. Set x=d_2,y=d_3,z=d_4 and
A=eta_2,B=eta_3,C=eta_4, X=x^2,Y=y^2,Z=z^2, L=X+Y+Z.
Use the three circulation columns v=(y,z,0), w=(-x,0,z),
t=(0,x,y), S=I-n n^T/L, n=(z,-y,x).
For rho=2 the two generator factors are a_3=-B w, c_3=AB,
a_4=C t, c_4=AC. For any physical exterior column f_a,
S f_a=f_a and S'_m f_a=(I-S) f'_(a,m); this retains the
projection derivative. Calculate the contractions for (m,a,b)=(2,3,3),
(3,2,3),(2,2,2) before expressing them in X,Y,Z. Integrate Y by
the inverse-moment formula, justified only for k=X+Z>0, then control
k=0 using the original bounded integrands and dominated convergence.

Essential inputs: L128 L127 L126; L124 retains E,ax,-Q,G,R and
L084 L070 L079 L080 L082 fix the comparison and qualifications.
Unresolved: scalar numerical values, xi, actual heat contractions, full
compensation, finer scales/logarithm, other jets, matching/interacting
error <=c_box/2, continuum axioms, reflection positivity, infrared control
and finite positive mass. Mathlib coverage not checked.

Completed: L129 proves the exact two-angle formulas for h_D,h_X,h_A,
including continuous corner values 0,0,1 and explicit O(sqrt(k))
corner bounds. The full crossed integrand is nonnegative and positive
on an open set, giving h_X>0 without a numerical enclosure. The
anisotropy formula simplifies because F_D+2F_X cancels the inverse-square
moments. No h_D/h_A sign, scalar value or actual-probe value is claimed.
Canonical proof: lemmas/L129-other-other-h-one-angle-reduction.md.
Supporting exact matrix/moment checks pass with all 664 residuals zero;
they do not substitute for the analytic proof or certify quadrature.

Continuation within the unchanged approved comparison: use L129(1)--(4)
to derive a rigorous complete two-dimensional integration error bound
and enclose h_D,h_X,h_A. The origin is continuous but may have limited
regularity; do not apply a smooth midpoint bound there without proof.
L127's exact integer interval machinery is a reusable implementation,
not an already-proved bound for these three new reduced integrands.
Essential inputs L129 L128 L127; L126 L125 L123 L120 L118 retain
physical definitions, xi and signs. L124 L097 L098 L101 L104 L107
retain E,ax,-Q,G,R, and L084 L070 L079 L080 L082 retain the reference
and qualifications. No coefficient compensation, probe sign, zero xi,
vanishing anisotropy or special mode constraint is assumed. All unresolved
construction and finer-scale obligations above remain. Reuse the unchanged
ready assessment; no new target or changed assessment has been approved
in this research step.

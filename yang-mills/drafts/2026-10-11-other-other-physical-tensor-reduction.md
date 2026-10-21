# Full physical-component tensor symmetry attempt

STEP_ID: YM-20261011-154-physical-tensor-reduction
Ready assessment: drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
Main gap: interacting ultraviolet control; immediate comparison remains
K_(i,oo)+4 gamma D_i. One bounded target contracts all four transverse-H
terms with linked phi(V) and tests signed transverse-coordinate covariance.
Downstream use: reduce actual heat-weighted evaluation to finitely many
scalar torus constants and continuum bilinear integrals. Continue only on
an exact covariant tensor reduction; abandon a symmetry shortcut if unequal
filters or path phases violate it. No actual-probe sign is assumed.

Saved before extended algebra. Define physical rank-four tensors by summing
all ordered r at fixed rho and contracting path labels with L_(alpha,a).
H is symmetric in a,b; the retained T is antisymmetric. Reflections require
each index to occur an even number of times; permutations equate matching
index patterns. If the full stencils obey this covariance, H has three
constants (rho=m,a=b distinct; rho=a,m=b distinct; all equal) and T one,
T_(rho,m;a,b)=tau(delta_(rho,a)delta_(m,b)-delta_(rho,b)delta_(m,a)).
L127 fixes tau at (rho,m,a,b)=(2,3,2,3). Check centered-symbol covariance,
including derivative and discarded phase terms, rather than assuming
finite staggered path symmetry. H remains and is not discarded.

L123's beta contains a real even part and imaginary odd path part.
The imaginary odd contribution to its full mixed trace is imaginary odd
and integrates to zero; only the real even antisymmetric edge matrix
2 sum_(mu<nu) eta_mu eta_nu h_(mu nu)(e_mu e_nu^T-e_nu e_mu^T)
can remain in beta. Verify both mixed orientations before reducing to one
invariant u_rho V_a h_(rho a). No kernel, mesh-limit or source theorem is
reproved. Essential inputs: L118 L123 L125 L126 L127; L120 L113 fix actual
fields and signs. L124 retains the other five coefficients; L084 L070
L079 L080 L082 fix the comparison and arithmetic qualifications.
Unresolved: complete covariance proof, scalar constants and actual heat
contractions, compensation, finer scales/logarithm, other jets, matching,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass. Mathlib coverage not checked.

Completed: L128 proves the exact five-scalar formula for the complete
K_f+K_V+K_sc+K_en. The physical H has three invariant patterns, including
hypercubic anisotropy; the antisymmetric physical tensor has one pattern
with L127's tau. Expanding L123's original centered paths shows that only
its real even skew edge matrix survives the mixed torus integral; both
mixed orientations reduce to one scalar xi. Phase derivatives are checked
before the H/T reduction. No finite shifted entry is assumed invariant.
Canonical proof: lemmas/L128-other-other-physical-tensor-symmetry-reduction.md.

Continuation within the unchanged approved comparison: evaluate the three
H constants and xi using L128(2),(3),(6),(7), then contract L128(1) with
the actual probes; do not treat tau's sign as a probe sign. A bounded
starting calculation can analytically eliminate one torus angle from the
three H definitions, checking all singular endpoint limits before any
quadrature. These are exact rational/trigonometric integrands, not a
request to repeat the failed universal curl identity. Essential inputs
L128 L127 L126 L125 L123 L120 L118, with L124 L097 L098 L101 L104 L107
retaining the five other coefficients and L084 L070 L079 L080 L082
fixing the comparison and qualifications. No cancellation, zero xi,
vanishing anisotropy, special probe constraint or scalar sign is assumed.
All finer scales, other jets, matching/interacting and construction/mass
gaps listed above remain open. No mathematical script was added.

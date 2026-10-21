# Actual split harmonic curvature — working checkpoint

2026-10-16. One mathematical attempt under the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-16-split-harmonic-metric-curvature-energy.md`.
Main gap: universal primitive rational Hodge realization. Intermediate
target: finite squared-curvature integral for L112's actual metric near
each split point. Potential use: a prerequisite for a separately reviewed
surface connection-extension argument; extension, semistability, |Z|,
F existence and transport remain independent obligations.

Inputs read: actual L111/L112 proofs and audits, relevant L094/L095
harmonic/stabilizer passages, ATTEMPTS/063/066/067. The elementary
oriented-frame computation in L069 was inspected for a convention check;
its irreducible coarse-moduli argument is not applicable at this point
and will not be imported. The saved assessment already covers the Chern
formula and coefficient harmonic theorem, so no further browsing is needed.

Candidate calculation to complete: the central real KS image W is a
quaternionic line. With xi=diag(i,-i), T=ad(xi) is quaternionic-linear;
ad(diag(1,-1))=-I T on the Dolbeault harmonic space. Since T is invertible
there, L111's incoming plane is the same real plane as T(W), hence is
quaternionic. The harmonic Serre form is a nonzero scalar multiple of
the complex symplectic form determined by the L2 metric and J,K. Need
write out this pointwise identity without invoking a stable quotient.
It would identify L111's central Serre complement with its Hermitian
complement under the natural central comparison T_z of L112.

Then the smooth mixed block B of H_K vanishes at the center: B=O(r).
In coordinates v=(x,y), the quotient correction is
(Bv)(Bv)^*/(v^*H_PP v), up to Hermitian slot convention. Its numerator
has real derivatives of order k bounded by O(r^(4-k)), k<=2, and the
denominator is comparable to r^2. Full inverse-denominator derivatives
would give O(r^(2-k)) through order two, thus bounded Chern curvature
in the extending frame and energy O(epsilon^4). Must prove these
uniform estimates, not just directionwise asymptotics. If central
compatibility fails, record that missing comparison rather than claim
divergence. Z empty is vacuous. No extension theorem is assumed.

Completed in canonical L113: the real compact stabilizer calculation
and complete coefficient frame identity prove the actual central mixed
block vanishes. Full real derivative estimates in the exact quotient
give bounded Chern curvature and energy at most K epsilon^4 on one
full punctured ball. This is a conditional known-tool specialization,
pending separate critical audit; no independent global gap is closed.
The proof, hypotheses, qualifications and Mathlib status are in
`lemmas/L113-split-harmonic-metric-bounded-curvature.md`.

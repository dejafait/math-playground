# Density fixed-mode limit — bounded attempt

2026-10-25. Work under the unchanged prior EXPLORE assessment
`literature/2026-10-25-density-response-separated-kernel-asymptotic.md`.
Exactly its target: the complete N^-2 density trace. Main gap remains
Wilson-specific control and the continuum/infrared construction; a
nonzero density limit would quantify required compensation only.

Inputs read: L003 relative modes; L279 exact pair hypotheses; L280
hypotheses and (16)–(25); all of L281; ATTEMPTS/048–049 and history 493.
No matching limit appears in these results. The assessment's inspected
scalar identities and scope exclusions are reused, without new browsing.
L002's explicit f_* formula was narrowly read because its space/time
product, beyond L003's listed positivity/support properties, may decide
the sign of the mixed pairing. Its infinite-volume theorem is not used.

Checkpoint before completing proof: h_m(lambda)=16^-1 sum_{j=0}^m
(1-lambda/16)^j approximates Delta^-1. For E_m=Delta^-1-h_m(Delta),
finite sine modes give uniform small errors in diagonals of
M E_m Delta E_m M* and B E_m^2 B*, hence a Schur row bound for the
full J_ef J_fe error. This should approximate the ENTIRE density in
operator norm, uniformly over N, by finite-range D_m. Its bulk row sum
is a scalar d_m, with limit d_*=-1/8-integral sin(q_1)^2/lambda(q)^2
against normalized measure on [-pi,pi]^4. Boundary rows are retained;
for fixed m their physical layer shrinks and has bounded row norms.

For external mode k put sigma_{+,k}=f psi_k on 12-cochains and reflect
for sigma_-. X_{pm,k,a}=a G C* sigma_{pm,k,a} should converge in physical
L2 to the relative continuum L^-1 d* sigma_{pm,k}. The exact a factors
then give limit 6 d_*/64 sum_k b_k <X_+,X_->. L281's uniform tail is
the only step allowing removal of the external cutoff. Because exact
f_* separates space and time, each time forcing is nonnegative and
one-dimensional Dirichlet inverses are strictly positive. This may
prove each mixed pairing positive without incorrectly claiming that
L^-2 is reflection positive on arbitrary tests.

Continuation/abandonment test: check uniform polynomial error, both
normal endpoint rows, diagonal/near-diagonal anchors, boundary strips,
strong source-field convergence, the factor 1/64, and strict positivity
for one actual mode. If any step fails, retain it as an unresolved
obstruction; a bulk symbol alone does not establish the result. No
mathematical script or numerical evidence is planned.

Completed: the full proof is canonical in
`../lemmas/L282-complete-density-negative-quadratic-asymptotic.md`.
The operator approximation is uniform over meshes; the boundary passage
is performed for fixed finite range before removing that approximation.
The final normalization is 6/64=3/32, and the actual product bump gives
strict positivity of the continuum pairings. Thus the density limit is
finite and strictly negative. This is an unaudited partial result, not
signed compensation or a Yang–Mills construction. The next proposed
critical audit is separately registered with REVIEW_REQUIRED.

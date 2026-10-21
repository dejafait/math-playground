# Bulk quadratic mass approximation — working record

The approved target remains the exact joint cubic probe-jet limit in
drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md; its prior
EXPLORE coverage is reused unchanged. Main gap: ultraviolet-uniform
interacting reflected comparison with error <=c_box/2, continuum axioms
and finite positive infrared mass. This is one mathematical attempt.

Intermediate test: approximate L198's bulk B at cubic scale by regularizing
only the local differentiated quadratic tensors from L200, with an error
uniform in N that tends to zero as a dimensionless mass tends to zero.
Keep the prefix test b, the signed tilt and the upper-exterior/transport
terms unchanged. Such a bound would permit this one regularization in a
later signed-limit argument; it would not prove a fixed-mass limit or
regularize the entire B+H-Q_tr sum.

Inspected L026's complete relative spectrum, L149/L155's full words,
L194's external contraction and quadratic norm, L196's transport,
L198's signed decomposition, L199's upper action support and L200's
complete differentiated quadratic count. Local recent drafts and
ATTEMPTS/043–044 preserve the failed absolute residual norm and
factorwise multiplier mechanism. No duplicate of this mass approximation
was found in the inspected current-group records; this is not a novelty
claim. ATTEMPTS/039–044 and unfinished work are preserved.

Proposed argument, not yet certified: separate the local derivatives
into terms retaining a rough first difference and lower-order exterior
differences. The complete action collar has quadratic norm
O(N^(3/2) sqrt(log(eN))); multiplying by the full tilt O(N) still
leaves it subcubic in the externally contracted response. Define
F_epsilon=(Delta/(Delta+epsilon))^(1/2), coupled on the original
co-closed Gaussian, and delta z=(I-F_epsilon)z. Spectral shells should
give Tr Cov(delta z)<=C N^4 epsilon. For an undifferentiated delta z
leg use the other differentiated covariance's bounded operator norm.
For a differentiated delta z leg, split the other leg at eigenvalue
sqrt(epsilon); low-mode trace and high-mode operator bounds should
give O(N^2 epsilon^(1/4)) in quadratic norm. Apply the original
whitened tilt to the quadratic difference only after that estimate.

Continue only if the bounds include epsilon<N^-2, variable stencil
coefficients, both color orders, boundary-compatible differences and
the original tilt/filter order. Abandon this approximation if it needs
an entrywise S<=Sigma comparison, commutation with A or a smooth rough
tilt. No fixed-mass trace limit or separate H/Q_tr limit is assumed.
Independent f_(i,2),r_0, full compensation and finer scales remain open.

Completed: L201 proves the uniform coupled approximation. The exact
lower-order residual pieces and complete action collar cost at most
O(N^(5/2) sqrt(log(eN))) after the tilt and external pairing. Filtering
the remaining local quadratic inputs by
F_epsilon=(Delta/(Delta+epsilon))^(1/2) costs at most
C_i N^3 epsilon^(1/4), uniformly also for epsilon<N^-2. The tilted
quadratic is differentiated as Dq(F_epsilon z)[F_epsilon Tz]; no
commutation with T is used. The full proof is canonical in
lemmas/L201-bulk-quadratic-uniform-mass-approximation.md.

Outcome ADVANCE / RESEARCH / REPRODUCTION: a useful controlled
approximation within the approved group, not progress beyond checked
sources. Verification was analytic, with no mathematical script. This
does not yet supply a fixed-epsilon limit: b and T are unregularized,
and H,Q_tr remain cubic-sized. Continue the same target by testing the
remaining ordered prefix/tilt factors at fixed epsilon; only a uniform
error followed by an actual signed limit permits parameter removal.

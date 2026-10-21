# Signed initial-interval pairing — completed bounded attempt

The unchanged approved target is the joint cubic probe-jet limit in
drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md.
This attempt tests L183(5) with L189's initial polynomial I, seeking
sup_a a^3 |E[I rho_H]-E[dI[W]]| <= C_i eta_*(delta) -> 0.
The downstream use is justified initial-interval removal in a later
joint-group limit; finite matching and the interacting reflected error
<=c_box/2, continuum construction and infrared mass remain independent.

Existing changes are preserved. L183 section 6 and ATTEMPTS/043 stop
the full residual's absolute tensor count, not the signed pairing.
The prior literature assessment remains adequate; no additional browsing
or new target approval is needed. L189 bounds I but not its response.

The tested discriminant compares the LOCAL full-link cubic tensors for
script R_3 and script S_3 against Sigma=Delta^-1, using S<=Sigma only
as a tensor covariance inequality. L166(11) bounds every component
Green entry by C[(1+distance)^-2+N^-2]. Its third power is summable
in four dimensions. With O(N^4) stencil placements and residual
coefficients O(N), this suggests norms O(N^3) and O(N^2), respectively.
L183's whitened tilt bound O(N) would then give ||rho_H||_2=O(N^3).
This does NOT apply to b, W or the forest-retracted cubics, whose
prefixes are nonlocal. The signed derivative term remains essential.

The completed proof is [L190](../lemmas/L190-co-closed-residual-initial-pairing-bound.md).
It proves the proposed rho_H norm bound and uniform removal of only
E[I rho_H] at cubic scale. The comparison is on positive tensor powers
of covariances, not on their individual entries or the signed tilt.
The full Green finite-size correction and all end rows are retained.
This is ADVANCE / REPRODUCTION: local standard-method progress, not a
claim of progress beyond checked sources or a complete joint limit.

The remaining expression is exactly the integral of L190(8)'s three
placements of W. The two prefixes in W remain correlated with both
other probe legs. L189's linear-Gaussian norm inequality does not
apply to this quadratic direction. No sharper estimate for that
quartic expectation has been obtained in this attempt.

Continuation: test those three placements jointly in their actual
heat/covariance order, seeking a mesh-uniform integrable bound for
a^3 E[dU(s)[W]], or a controlled signed cancellation after integration.
Essential inputs L149 L155 L166 L181 L182 L183 L189 L190, with
L010's actual probes and L018/L020/L026/L028 conventions retained.
Keep both moving prefixes, all faces, constant modes, both insertion
subtractions and full heat sums. Assume neither W smoothness,
signed-tilt positivity, separate-term convergence nor negligible
initial time. Continue only on a cubic-scaled integrable estimate
or controlled cancellation; otherwise stop that estimate rather than
repeat the global norm counts in ATTEMPTS/039 and ATTEMPTS/043.

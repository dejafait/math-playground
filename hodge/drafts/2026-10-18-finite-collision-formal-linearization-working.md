# Finite-collision formal-linearization working checkpoint

2026-10-18, step 385. Approved target and pre-invocation coverage:
`drafts/literature/2026-10-18-finite-collision-formal-linearization.md`
(SPECIALIZE). One mathematical specialization only.

Main gap: universal primitive rational Hodge realization. Intermediate
target: one formal ambient holomorphic chart linearizing every actual
branch at a finite opposite-image collision. Downstream use: replace
higher normal-jet bookkeeping by tangent-arrangement calculations in a
later separately assessed step. Success requires the same ambient chart
and the actual completed pullbacks; a missing connection hypothesis or
unmatched pullback blocks the import. No convergence assumption is allowed.

Inputs inspected: L118's actual common harmonic metric, natural coarse
comparison and parametrized geodesy; L120's finite normalization; L121's
distinct quaternionic lines and common-chart argument. L127 supplies only
a second-order comparison. ATTEMPTS/070--072 retain their stop evidence;
formal linearization would not imply minimal normalization defect.

Proof in preparation: apply Jentsch--Weingart Theorem 4.6's formal
construction and Corollary 4.9 to one ambient germ and each locally
embedded complex totally geodesic branch. Transfer the restricted chart
through each branch embedding. The induced source metric is 2lambda g,
whose connection is the original source connection. Choose algebraic
regular parameters on the smooth ambient and sources. Their analytic
inverse charts identify actual holomorphic pullbacks with their Taylor
series. Formal coordinate changes with invertible linear part then give
the desired conjugacy. Exact completion of the finite normalization
injection must identify the actual image kernel with the intersection
of these linearized branch kernels, rather than an invented formal model.

Unresolved independently: F existence, collision occurrence, arrangement
defect values, global consequences, transport and the universal target.
No completed all-orders claim is recorded by this working checkpoint.

Completed later in this step: the canonical full proof and qualifications
are in `lemmas/L128-finite-collision-simultaneous-formal-linearization.md`.
The common-chart test and actual completed-image comparison are established
conditionally there, pending separate critical audit. This working note
preserves the preparation state and supplies no additional result.

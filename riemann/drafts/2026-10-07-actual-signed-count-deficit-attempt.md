# Actual signed count deficit — working record

Approved target: specialize Dobner's Theorem 1 to the actual pair from
L366/L372 and compare with L374. Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-07-signed-count-deficit-specialization.md`.
This is a REPRODUCTION, with no new oscillation mechanism or numerical
calculation proposed.

Main gap: global actual-theta mixed positivity and the total L367 signed
margin. Intermediate target: on each fixed eventual ray, the full
F_0-minus-G count is unbounded below. Downstream use: test the joint
disjointness and physical-discriminant premises of L374. Acceptance
requires full multiplicities, bounded fixed-H errors and moving endpoints
off every strip-zero ordinate; abandon this transfer if any of those
requires an unproved premise. Independent gaps in actual disjointness,
D<=0, total signed margin and RH remain unresolved.

Checkpoint before writing the full specialization: put
M(X)=X/(2pi) log(X/(2pi))-X/(2pi). L372 gives
|N_G([H,X])-M(X)|<=E_H. For X off all strip-zero ordinates,
the cited total count is M(X)+7/8+S(X)+R(X),
|R(X)|<=1/(150X). By L366 (1)/L018, if C(X) counts critical-line
zeros at positive heights up to X, with full multiplicities, and c_H
counts those at heights strictly below H, then
N_F_0([H,X])=C(X)-c_H<=N(X)-c_H.
Thus the difference is at most
S(X)+7/8+E_H+1/(150H)-c_H.

Use V(T)=sqrt(log log T) in Dobner's negative-sign measure theorem.
Its allowed upper range eventually exceeds V(T). The negative set has
positive measure; the set of all strip-zero ordinates is countable,
so remove it without losing all choices. Select X in [T,2T] and get
a deficit at most K_H-V(T), tending to minus infinity. A zero exactly
at H remains counted because c_H uses the strict lower interval.
No bound on multiplicities at moving endpoints is asserted.

Then invoke L374 only conditionally, with L368's eventual strict
response Laguerre sign. Its lower bound -1 contradicts these deficits
if both eventual disjointness and D<=0 hold. Neither missing premise
is separately decided. Full proof/citations will be canonical in L377;
this draft alone is not a verification or a claimed theorem.

Completed: the full specialization and precise citations are now in
canonical L377. It establishes the negative deficit and only the joint
L374 incompatibility. No independent audit has been claimed; the next
coverage proposal is REVIEW_REQUIRED. The bound and all endpoint cases
are analytic, so no mathematical script or numerical evidence is used.

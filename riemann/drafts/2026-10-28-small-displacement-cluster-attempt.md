# Small-displacement cluster attempt

Approved target: the exact B_epsilon bound in
`literature/2026-10-28-small-displacement-cluster-test.md`.
The initial work-in-progress mechanism below is preserved; the completed
argument is now canonical in L474, whose separate audit remains pending.

Proposed mechanism: partition pair centers into real cells of width
1/log T. On a disk of radius 8/log T about a cell center, divide Xi
by the finite Blaschke factors of all selected pairs in that cell,
including multiplicity. On the target real windows each remaining
factor has modulus at most 1/2. Removing one pair costs O((log T)^2),
while the other factors may suppress the total multiplicity M through
M*2^(-4M+4). Control the disk supremum on a larger disk by an area
mean, then sum with bounded overlap. A microscopic shifted zeta second
moment would give total normalized area O(T/log T), hence the desired
epsilon^3*T*(log T)^3 after scaling.

Checks still required: exact quotient denominators and all constants;
area submean with the varying real gamma normalization; a uniform
small-complex-shift L2 bound including the combined Bettin pole terms;
dyadic/end windows, multiplicities and constants independent of epsilon.
No claim is made about complementary displacement mass or RH.

## Completed bounded attempt

[L474](../lemmas/L474-small-displacement-pair-mass-via-local-blaschke.md)
supplies the proposed cubic bound. In its finite cell calculation,
|b_a(w)|<=96/247<1/2 and the remaining 2M-2 factors yield
M*16^(-(M-1))<=1. The sum of normalized disk suprema is O(TL^2),
by bounded area overlap and Bettin's continuous shifted second moment.
The resulting bound is C epsilon^3 T L^3 with common C,T_0, rather
than an extra logarithm or an epsilon-dependent constant. Its proof
keeps the chi factor anchored at y=0 before combining the two zeta
poles, and uses real A only as a normalization. All listed checks have
been addressed in the written proof, not independently audited.

No additional divided-difference formula is needed; retaining finite
zero factors alone implements the approved mechanism. This is local
mathematical progress from a new application of known tools, with no
certified originality claim. The required full little-o bound and
complementary mass remain unresolved. The next step is approval of
the precise source/audit scope, followed in a later invocation by
critical review of this result; do not infer a full RH candidate.

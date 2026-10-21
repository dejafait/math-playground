# Thirteen component via the global cubic norm — completed attempt

Approved target: Test whether the global norm from L069's D to Q(theta) forces the rational-root component of loc_13(T) to be square, with T as in L084.

2026-10-17. Reuse the prior SPECIALIZE assessment
`literature/2026-10-17-thirteen-global-norm-filter.md`. Main gap:
primitive integer emptiness; the intermediate test concerns redundancy
of the rational-root component only. No class realization or dimension
improvement is assumed. Preserve ATTEMPTS/029/038 and all earlier work.

Working route: for arbitrary [z] in T, let e=N_D/F(z). Ideal norm
preserves even valuations outside 2,11, and norm transitivity makes
N_F/Q(e) square. L077's class number one permits division by a global
square to obtain an S-unit. Its complete list then gives [e] among
1,v,w,vw. This needs a full applicability proof for nonunit class lifts.
At t=11 modulo 13 (theta=8), v=7 and w=6 are nonsquares, while vw=3
is square. The unresolved calculation is N_J/C(xi), with the exact
L082 representative xi=64+4*pi^5+4*pi^10-theta, pi^11=2.
If its class lies in {1,[vw]}, the primitive dyadic norm condition
would eliminate v,w. Compute the determinant norm directly; no
unassessed Kummer-corestriction theorem is assumed. Both norm towers,
all support and infinite places, and the entire thirteen-adic tensor
algebra must be retained in the final argument. An envelope that still
permits v or w stops this sufficient method, without global realization.

Completion: L088 contains the full proof and citations. The norm of xi
is square in C: every nonconstant determinant term has valuation at
least 27>6. The four-element supported family injects at C, so every
T-class has trivial D/F norm. Norm at the rational thirteen-adic place
preserves the unit quadratic character and forces that component square;
support and the D/K norm force the last two classes equal. Thus the
full J13 filter is redundant on T. The determinant certificate is
`scripts/thirteen-global-norm/norm-certificate.json` (nine checks pass).
ATTEMPTS/039 records this route stop. No dimension improvement or
integer exclusion follows; a separate critical audit is pending.

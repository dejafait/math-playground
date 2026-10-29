# Simultaneous ordinary-jet moments and clipped mass, 27 October 2026

Approved target: Assess whether complete fixed-order second and fourth Hardy-jet moments admit a finite-atomic law with nonvanishing normalized first-Laguerre negative mass.

Gate: `literature/2026-10-27-hardy-jet-moment-feasibility-coverage.md`,
saved EXPLORE assessment supplied before this invocation. Reuse its
Bui--Hall v1 and Bayer--Teichmann v2 inputs; no new source scope.

Main gap: actual-Xi initial signs at unbounded heights and global mixed
positivity. A positive abstract clipped mass would obstruct an inference
of o(H(log H)^3) from exactly these finite moments, without deciding
the actual mass or RH. The pair-divided summation stop is preserved.

## Saved construction before full verification

Put ell=log H and use the actual triple (Z,Z'/ell,Z''/ell^2) only
to form the positive spherical fourth-moment measure
mu=(H ell^4)^(-1) integral |X|^4 delta_(X/|X|) dt.
Its mass W is bounded by the cited fourth moments. Average mu with
its reflection (n_x,n_y,n_z)->(n_x,-n_y,n_z). Push this average to
radius ell^2 with multiplier ell^(-4). The resulting rare mass is
p=W ell^(-4); its second contributions are bounded, its odd-y entries
are zero, and its even-y fourth entries equal the actual moments.
Odd-y fourth leading coefficients are zero by the cited parity result.

For the bulk, choose independent epsilon in {+1,-1} equally weighted,
k=1/12 with probability 1/6 and k=-7/60 with probability 5/6, and
v=0 with probability 1/2 or v=+/-1/sqrt(6) with probability 1/4 each.
Use sqrt(ell)*(epsilon,v,k epsilon) with total mass 1-p.
The proposed exact checks are E k=-1/12, E k^2=1/80,
E v=0, E v^2=1/12, and E(k-v^2)_+=1/144.
Bulk fourth contributions are O(ell^2), inside O(ell^3).

Continuation/abandonment test: establish these identities, simultaneous
source errors, p<1/2 at one common onset, and atomic replacement
preserving all 23 coordinates (constant, six second, fifteen fourth,
clipped mass). Abandon this ansatz if any tolerance or positive-mass
check fails; a failed ansatz would not imply moment infeasibility.
No first/cubic/response constraints or global realization are imposed.

Status at this save: provisional calculation, not yet a canonical result
or independent critical audit. L414/L416 supply the previously established
mechanism, not the new ordinary-moment conclusion. L471 (7)--(9)
supplies the relevance and scale, not an actual negative value.

## Completed bounded attempt

The simultaneous checks succeed; the full argument is now canonical in
[L472](../lemmas/L472-hardy-jet-moments-positive-clipped-mass.md).
The result is an informative finite-data obstruction, with no assertion
about the actual clipped mass. No mathematical script or numerical fit
is needed: the twelve-state arithmetic, all scaling powers and the
23-coordinate atomic application are proved there. Preserve this early
save as reasoning history; it is not a second canonical proof. A separate
critical audit remains pending.

# Equality determinant calculation — working record

Approved target: compute the two determinant pullbacks and test the
ample combination for L097/L098's conditional equality family.
Coverage: drafts/literature/2026-10-15-equality-determinant-pullback-test.md
(pre-existing SPECIALIZE). No further literature search is needed.

Main gap: universal primitive rational Hodge realization. Intermediate
target: an integral necessary ample-cone condition on the full D for
the (14,21) equality kernel; an incompatibility could exclude this
kernel before construction or transport. Stop this filter if compatible.
The source review checked the line-twist/jumping-cycle comparisons and
ATTEMPTS/064; none evaluates this determinant pair.

Completed calculation: with t=H^2 and c=2-14 eta, chi(c)=-10,
chi(c[O_H])=-t. Thus ch(u_0)=-2-10 eta and ch(u_1)=-2H.
Relative GRR with td(S_1)=1+2 eta and rank-two ch_3(F)=0 gives
c_1(f^*L_0)=0 and c_1(f^*L_1)=2D(H). Integral Picard identification
and the whole-space ample-cone test are completed in
[L107](../lemmas/L107-equality-determinant-pullback-compatibility.md).

Completed cone check: D(h)=2lambda h is ample; continuity and openness
give a neighborhood of h whose D-images are ample. Intersect it with
L097's rational relative wall stratum before selecting alpha, clearing
denominators and taking a very ample power. This permits D(H) ample
without asserting D preserves the entire ample cone. No F existence,
image normality, generic H, universal sheaf, higher-cohomology rank
constancy or new Hodge class follows. Preserve earlier stops.

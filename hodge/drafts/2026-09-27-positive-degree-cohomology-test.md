# Positive-degree cohomology: working notes

The saved target and prior SPECIALIZE assessment are unchanged. The
question is whether H^1(C,O_C(nH)) vanishes for every positive n for the
fixed ample L, with H=L external tensor L. L018 would then exclude all
positive containing degrees in its complete-intersection construction;
a nonzero group would only identify a degree needing a new lifting test.
The required transverse RM direction and the universal Hodge gap remain
unresolved. This draft preserves unfinished reasoning, not a result.

The local two-plane rings from L008 give a normalization quotient of
length three. Thus both H^1(W,M^n) and the simultaneous difference map
at the three identified pairs must be controlled, where
M=g_0^*L tensor g_1^*L. No equality of the two pullbacks is assumed.

A possible sufficient test uses the disjoint fibres F_0 and F_infinity
of W, whose sum has class K_W=2F_W. If H^1(W,M^n(-F_0-F_infinity))
vanishes, sections restrict surjectively to both complete fibres.
On each type-III fibre, the two rational components each have degree
at least 2n under M^n, since both maps preserve the components and L
is ample. Interpolation on those two tangent components should then
control all three fixed points simultaneously. The precise gluing
argument is still to be written.

The reviewed Kawamata--Viehweg theorem would give the required
vanishing if nM-2K_W is nef and big. A sufficient condition is that
nL-F is nef and big, since nM-2K_W is the sum of its two pullbacks.
This would yield an effective degree cutoff from Hodge index, but would
not by itself establish the target for n=1.

An additional possible check is the actual rank-four Neron--Severi
lattice. The constant-coordinate section x=-c_1/b_1 is visible in the
equation. If its intersection data and saturation are justified, the
sections and the two fibre components may control L-F more sharply.
No lattice basis, nefness claim, pullback equality, small-degree value,
or completed cohomology theorem is asserted at this checkpoint.

## Argument found; final checks in progress

Let E be the exceptional component and R=F-E the other component of the
type-III fibre. The visible constant section P is disjoint from O and
meets E once. The intersection matrix of (F,O,E,P) has determinant -7,
so these classes span NS(S)_Q by the published Picard-rank-four input.
Put V=P-O-2F+E/2; it is orthogonal to F,O,E and has square -7/2.

For the section Q_m=mP and epsilon=m modulo 2, the generic-fibre group
law and vertical divisor classes give

    Q_m = O + (7m^2+epsilon)F/4 - epsilon E/2 + mV.

For a divisor D=dO+bF+zE+kV with d=D.F>0 and nonnegative intersections
with E and R, write t=-z/d in [0,1/2]. Choose an integer m nearest k/d
and let s=D.Q_m. Direct expansion yields

    D^2 = 2ds + d^2(2 - 7(m-k/d)^2/2 - 2t^2
                       - epsilon(1/2-2t))
        >= 2ds + 5d^2/8.

For an irreducible curve of fibre degree at least two, s>=0; such a
curve therefore cannot have square -2. For ample L, s>=1, giving
L^2>2L.F. Consequently L-F lies in the positive cone, is nonnegative
on every (-2)-curve (a section or a fibre component), and is positive
on all curves of nonnegative square. It is nef and big. This derivation
needs only the rational span, not an integral lattice-basis claim.

For A=nL-F, both pullbacks are nef and big, so
nM-2K_W=g_0^*A+g_1^*A is nef and big. The reviewed vanishing theorem
then gives H^1(W,M^n(-F_0-F_infinity))=0. On either type-III fibre,
degree at least two on each component allows prescribing a common
length-two restriction at the tangency and a value at the other marked point on each
component. Hence the evaluations at all three marked points are
simultaneously onto; disjointness of the two fibres gives all six
values. This handles arbitrary descent identifications for M, without
assuming g_0^*L=g_1^*L. The normalization exact sequence should now give
H^1(C,O_C(nH))=0 for every n>0.

Remaining checks before recording the lemma: justify the local
intersection P.E=1 in the resolved chart; derive the displayed section
formula without assuming a Mordell--Weil generator; use the actual
length-two intersection scheme of the tangent components; and retain
L018's extra ideal-cohomology hypothesis for equality with V_D. The
all-degree exclusion concerns m>n>0 and the stated smooth unions only.

## Completion on 2026-09-27

[L019](../lemmas/L019-positive-degree-cubic-support-vanishing.md) completes
the argument and the listed checks. The q-chart gives P.E=1. The group
law on the generic fibre, followed by an integral vertical-divisor
calculation and adjunction, proves the section formula for every
integer without a generator assumption. The lattice inequality makes
L-F nef and big for every original ample L. The adjoint bundle uses
2K_W, and the fibre interpolation retains the full length-two tangency
scheme. Surjectivity at all six points handles any actual descent
identifications, so no equality of the two pullbacks is needed.

The result is H^1(C,O_C(nH))=0 for every n>0. Through L018 this gives
an informative negative result for all admissible smooth unions with
m>n>0, including every former small-degree possibility. Equality of
lifting loci still has L018's separate ideal-cohomology hypothesis.
The theorem's full specialization was not matched by the prior review;
its supporting vanishing and gluing results are known. No new surface,
transverse lift, Hodge class, or complete candidate was obtained. The
interim reasoning above is retained as the record of the completed test.

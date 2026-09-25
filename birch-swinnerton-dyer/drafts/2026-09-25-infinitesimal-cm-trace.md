# First-order CM trace-lifting test

Date: 2026-09-25. Saved before the detailed calculation. This is an
unfinished test, not a Kummer-membership theorem or BSD candidate.

## Gap, target, and downstream use

The universal gap is rank E(Q) = m(E) for m(E) >= 2. In L006's
restricted setting a nonzero strict class gives Selmer dimension two;
the missing rational Kummer membership would force rank E(Q) = 2.
The proposed intermediate target is a Galois-equivariant lift, over
Q_p[epsilon]/(epsilon^2), of the weight-one auxiliary trace to the
normalized CM tensor on the diagonal ordinary branch. Such a lift
would be necessary for a regular family contraction extending that
trace. Even success would leave a cycle-valued comparison, nonvanishing,
auxiliary existence, and higher ranks unresolved.

## Redundancy and decision test

L007 rules out a continuation satisfying a classical tame-twist
identity. It does not compute a first-order obstruction for the actual
two CM inducing characters after the tensor's self-dual twist. Earlier
Selmer dimension audits likewise do not answer this deformation question.

Recover the normalized tensor and CM characters from the published
Castella--Hsieh construction. On restriction to G_K, compute the
first-order characters on the two lines where the fiber trace is
nonzero. An invariant lift must annihilate each character derivative.
Test whether the cyclotomic normalization cancels both derivatives,
or leaves an anticyclotomic derivative that is nonzero on inertia.
Retain complex conjugation, not just G_K-invariance. Continue toward
a regular trace lift only if the actual nonzero diagonal tangent
passes this test; otherwise record its precise obstruction and stop
that lift mechanism. Other geometric or derived constructions are
not thereby excluded.

Exploration turns entering this step: 0 of 3 without an advance or
informative negative result. The required bound remains r >= 2; the
available upper bound r <= 2 will not be counted as improved by a
representation-theoretic calculation alone.

## Completed assessment

The [source normalization](../foundations/09-cm-diagonal-deformation.md)
identifies the tensor as Ind(xi_T) direct-sum Ind(chi), after removing
the constant V_p E factor. Here xi_T = Psi_T/Psi_T^tau is universal
anticyclotomic, and weight one is T = 0. This is the actual diagonal
branch, without L007's classical tame-duality hypothesis.

[L008](../lemmas/L008-infinitesimal-cm-trace-obstruction.md) computes
the derivative d = l-l^tau. It is nonzero by universality, which
supplies the discriminating test directly without an additional
inertia calculation. The fiber trace's obstruction restricts to
-d(e_1^*-e_2^*) and lies in the quadratic-character summand. All
equivariant first-order auxiliary functionals have image in epsilon F
and reduce to zero. A matrix-trace argument also rules out a lift of
id_(V_p E) tensor tr_0 with arbitrary representation-valued corrections.
The zero-tangent case admits a first-order lift, confirming that the
test detects the tangent rather than merely restating fiber duality.

Decision: stop the regular contraction mechanism. This is a new
first-order obstruction for the normalized CM branch, not a repeat
of the earlier ordinary-root test. It leaves the cohomological class
and its isolated-fiber projection intact. The rank bound is unchanged.
The separate class-level Bockstein may behave differently; whether
its vanishing carries any rational-point information is unproved.
The completed outcome is NEGATIVE; exploration turns remain 0 of 3.

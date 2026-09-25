# Class-level anticyclotomic Bockstein test

Date: 2026-09-25. Initial reasoning saved before the source and local-condition audit.
This is a bounded test, not a Kummer-membership result or BSD candidate.

## Gap, intermediate target, and decision test

The universal gap is rank E(Q) = m(E) for m(E) >= 2. In L006's
restricted setting the missing input is q(kappa) = 0 for its nonzero
strict Selmer class. The proposed intermediate target is the obstruction
to lifting res_K(kappa) through the first-order anticyclotomic character
xi = 1 + epsilon d. Compute the global cup product d cup res_K(kappa)
and its refinement with the chosen Selmer local conditions.

If vanishing imposes a new restriction compatible with rational Kummer
classes, it could help bridge Selmer membership to rational points.
Success would still leave the implication to Kummer membership,
nonvanishing, auxiliary existence, and the universal rank comparison
unproved. If the obstruction already vanishes on the entire relevant
Selmer space, stop treating this vanishing as a rational-point test.
An ordinary Selmer lift must not be confused with a lift remaining
strict at p; check the local correction terms before drawing a conclusion.

L008 obstructs a representation-level trace, not an individual class.
L006 records a Selmer/Kummer dimension gap but does not compute a
deformation obstruction. The present test is therefore different from
the two failed regular contraction mechanisms. The auxiliary condition
L(E^K,1) != 0 suggests that the minus Selmer space may vanish and force
the ordinary first Bockstein to vanish by anticyclotomic symmetry.
Whether strict local conditions leave an additional obstruction is open
at the start of this test.

The required lower bound remains r >= 2; the proved upper bound is
r <= 2. Exploration turns entering this step: 0 of 3 without an
advance or informative negative result.

## Intermediate calculation saved

The standard ordinary Selmer complex C has H^1(C) = S_K and,
by self-dual Poitou--Tate duality, H^2(C) = S_K^dual. The auxiliary
analytic rank-zero twist has S_K^- = 0. Since d is anticyclotomic,
the first Bockstein sends plus classes to the minus part of H^2(C),
which is zero. Thus every ordinary Selmer class has an ordinary
first-order lift; the global cup product is its zero image.

This does not yet settle strict lifting. For x strict, choose an
ordinary lift and divide its two localizations by epsilon. The
result is well-defined modulo loc(S_K) in the direct sum D of the
two local finite lines. Averaging the lift under the semilinear
complex conjugation (epsilon maps to -epsilon) gives an invariant
lift. It is unique because the difference of two such lifts lies
in epsilon S_K, whose invariant part is zero. Its local derivative
therefore lies in D^-, a one-dimensional line, while loc(S_K) lies
in D^+. It vanishes exactly when a lift stays strict at both primes.

Still to check before finalizing: the absence of local invariant
correction terms in the ordinary Selmer complex, precise duality
citations, and the distinction between this residual derivative and
any theorem detecting rational Kummer membership.

## Completed assessment

[L009](../lemmas/L009-class-bockstein-and-strict-local-derivative.md)
completes the calculation, including those checks. Good ordinary
reduction excludes a local quotient eigenvalue equal to 1, so the
Selmer-complex comparison has no exceptional H^0 term. Poitou--Tate
duality and the auxiliary twist's zero Selmer group force the ordinary
Bockstein to vanish on all of S. The source's first-height symmetry
provides an independent consistency check; this is not claimed as a
new theorem about anticyclotomic heights.

The strict calculation gives a canonical Delta_d: S_00 -> D^-.
A class lifts strictly if and only if its Delta_d is zero. The
opposite signs of D^- and loc(S) prevent correcting a nonzero value
by changing the ordinary lift. Explicit linear diagrams show that
ordinary liftability and the fiber localization alone leave that
value undetermined; they are not arithmetic counterexamples.

Decision: stop ordinary Bockstein vanishing as a rational-point test.
The strict scalar is a narrower unresolved question and carries no
established Kummer interpretation. This is an informative NEGATIVE,
not a new rank bound: r <= 2 is unchanged, while r >= 2 is required.
Exploration turns without an advance or informative negative remain
0 of 3. The source references and their limitations are recorded in
[the duality foundation](../foundations/10-selmer-bockstein-duality.md).

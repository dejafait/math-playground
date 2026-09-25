# Diagonal-cycle specialization: motivic-lift test

Date: 2026-09-25. Saved before the detailed source check. This is an
unfinished test, not a claimed rationality theorem or BSD candidate.

## Gap and intermediate target

The main gap remains rank E(Q) = m(E) for m(E) >= 2. In the restricted
rank-two setting of L006, a nonzero strict generalised Kato class gives
Selmer dimension two; proving q(kappa) = 0 in V_p Sha would force
rational rank two. Nonvanishing from m(E) = 2, the auxiliary choices,
and the universal higher-rank problem remain separate unresolved steps.

Test the actual construction in Darmon--Rotger, *Diagonal cycles and
Euler systems II*: does its specialization at weights (2,1,1) lift to
a motivic class whose projected Abel--Jacobi image is globally Kummer,
without assuming finite Sha? A geometric construction of that lift
would address the missing membership, even with later steps unresolved.

## Redundancy and discriminating test

The previous two audits rejected point imports from Selmer independence
and from nonvanishing. They did not inspect the specialization map in
the construction paper. The new mechanism tested here is compatibility
of a geometric cycle specialization with the cohomological one, not a
third dimension comparison. Existing L005 and L006 already prove the
needed rank threshold and will not be re-proved.

Locate the cycle domain, Abel--Jacobi map, big Galois module, and
weight-specialization map with exact source labels. Check where the
comparison with finite-weight cycles is proved, whether (2,1,1) lies
there, and whether projection to the trivial Artin summand descends
through a Chow or motivic map. Continue this automatic-lift mechanism
only if these maps give Kummer membership without its equivalent
finite-Sha premise. Otherwise preserve the valid cohomological
construction and identify the absent geometric comparison; a failure
of this construction is not a theorem that no motivic lift exists.

## Mid-step refinement

The published construction has a finite-weight cycle comparison in
Proposition 2.5 and a separate weight-one definition in Section 2.2.2.
The tentative finite-level character obstruction has not been established:
normalizations of weight and diamond action must not be guessed. No
claim about a nontrivial weight-one character will be used.

A more direct test of the adjoint projection is available. At weight
one, let g have distinct p-Frobenius roots alpha,beta, with product
chi(p), and h = g tensor chi^(-1) = g*. If the ordinary families
remain related by this tame twist at higher classical weights, their
ordinary U_p roots satisfy A_h = chi(p)^(-1) A_g, since only one root
is a p-adic unit there. By continuity, a family through g_alpha then
passes through h_(beta^(-1)), not h_(alpha^(-1)). The latter is the
diagonal stabilization used by the nonzero class in L006.

Check this root-switch argument with all hypotheses explicit. If
correct it rules out the specific geometric shortcut of deforming the
usual dual-pair trace projector along that diagonal branch. It does
not rule out a different motivic comparison at the exceptional fiber.

## Completed assessment

[L007](../lemmas/L007-ordinary-dual-family-stabilization-obstruction.md)
proves the root obstruction with the accumulating classical points,
tame character, and ordinary hypotheses explicit. No assumption about
Sha, no weight-coordinate formula, and no conjectural rank comparison
enters the proof. The detailed source locations remain in
[the construction audit](../foundations/08-diagonal-cycle-specialization.md).

The automatic dual-family contraction fails the stated test. This is
new evidence about a particular missing map, not a larger rank bound.
L006 still needs nonzero kappa with q(kappa) = 0; without it the
available bounds remain r <= 2 (or 1 <= r <= 2 under Theorem B), short
of r >= 2. The trace on the single Artin fiber remains available, so
testing its infinitesimal lifting obstruction is a different, narrower
question than imposing classical duality throughout the family. Even
a successful infinitesimal lift would still require a cycle-valued
comparison before it could prove rational Kummer membership.

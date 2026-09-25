# Strict/relaxed duality test for the rational Kummer line

Date: 2026-09-26. Saved before the detailed calculation.

## Gap, intermediate target, and test

In the restricted nonzero generalised-Kato setting the missing input
is q(kappa) = 0. The proved upper bound r <= 2 still needs r >= 2.
The proposed intermediate target is a Poitou--Tate formula for the
strict first-order derivative Delta_d on
log_p(Q)j(P) - log_p(P)j(Q), assuming independent rational P,Q.
Its plausible use is to decide whether strict liftability is even a
necessary test for Kummer membership before calculating it for kappa.
The points are test inputs, not points constructed from analytic rank.

The discriminating test is whether the strict/relaxed dual pairing
forces this derivative to vanish on those inputs. A nonzero arithmetic
example or a theorem forcing vanishing would decide necessity; a
formula with an uncomputed arithmetic term must be reported as such.
Symmetry alone is insufficient evidence for either arithmetic answer.
Even a necessity result would leave sufficiency, kappa nonvanishing
from m(E) = 2, auxiliary existence, and higher ranks unresolved.

## Redundancy and mechanism

L009 already proves ordinary first-order lifting automatic, using
the vanished minus ordinary Selmer space. L010 shows that the scalar
Coleman law misses the ordinary part of the local derivative, even
with its full series specified locally. Neither tests the dual of
the zero local condition: that dual condition is relaxed at p.
The present step retains this relaxed space and the local boundary
map instead of repeating an ordinary-height or scalar-order argument.

The calculation to audit is the exact local-condition sequence from
the strict to ordinary Selmer complex, paired with the relaxed dual
complex. Signs, the dual character, the dimension of the minus
relaxed space, and possible local H^0 terms must all be checked.
No strict-lifting statement about rational points is established in
this saved draft. Exploration turns used before this step: 0 of 3.

## Calculation saved for sign and completeness review

Let R be the Selmer group with unrestricted local conditions at both
primes over p. The strict/ordinary local-condition triangle should give
0 -> S_00 -> S -> D -> R^dual -> S^dual -> 0. Its minus part identifies
D^- with (R^-)^dual, so dim R^- = 1 even though S^- = 0. The boundary
functional is the sum of the local Tate pairings. An explicit cone
calculation identifies the strict Bockstein with the boundary of
Delta_d, with a common sign fixed by the cone convention.

Choose a finite local generator of logarithm 1, form a_+ and a_- by
the symmetric and antisymmetric pairs, and choose an invariant local
first-order lift of a_+. Subtracting log_p(s) times this chosen lift
from loc(y_s) defines epsilon t_d(s) a_-. Changing the lift changes
t_d by a multiple of log_p. For rational P,Q the invariant determinant
is log_p(Q)t_d(j(P)) - log_p(P)t_d(j(Q)); it is the coefficient of
Delta_d on their strict Kummer combination.

This is a mixed strict/relaxed Bockstein pairing. The anticyclotomic
sign does not kill a pairing between a plus strict class and a minus
relaxed class. No numerical value or arithmetic nonvanishing has
been obtained. To test the purely formal vanishing argument, a model
must include dual complexes and an injective logarithm on its rational
point lattice, not just label an arbitrary kernel vector rational.

## Completed assessment

[L011](../lemmas/L011-strict-relaxed-pairing-on-kummer-vectors.md)
proves the exact sequence and mixed pairing, fixes the cone sign,
and derives the choice-independent determinant. Its model includes
the inverse-character dual complex and a rational point lattice on
which the logarithm is injective, yet allows a nonzero determinant.
It tests formal consequences only; no arithmetic example or theorem
settling necessity for actual rational points has been obtained.

The determinant vanishes exactly when the strict vector lifts. In
the rational rank-two test it also vanishes exactly when the normalized
relaxed minus generator lifts for the inverse anticyclotomic character.
The missing global obstruction is therefore -d cup z^-, not the
ordinary Bockstein already killed by symmetry. This supplies a concrete
arithmetic test beyond the unsuccessful formal vanishing argument.

The decision is NEGATIVE for deducing automatic strict lifting from
rational-logarithm and duality data. Arithmetic necessity and sufficiency
remain open here, as does q(kappa) = 0. The achieved original rank
bound remains r <= 2, short of r >= 2. This step uses no exploration
turn without an advance or informative negative result.

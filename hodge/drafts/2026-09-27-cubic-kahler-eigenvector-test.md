# Cubic Kahler eigenvector — working test

Date: 2026-09-27. This records the one specialization authorized by
the saved [SPECIALIZE assessment](literature/2026-09-27-cubic-rm-kahler-eigenvector.md).

## Gap, target and decision test

The missing geometric input remains a representative of the cubic RM
action that reaches an NS-fixed direction outside the three-dimensional
Dickson tangent space. The present target asks only for a rational
cup-product-self-adjoint extension of U with a Kahler eigenvector for
the eigenvalue on the holomorphic two-form. Success supplies compatible
cohomological data for the separately gated bundle route. Bundle
existence, stability, further Chern-class conditions and transverse
transport would still be missing. The existing 21-dimensional span
and three directions against four required are unchanged.

The two preceding exploration turns supplied source comparisons.
This third turn must finish with an exact form-and-chamber certificate,
an informative obstruction, or an explicit inconclusive stop. A finite
matrix search or a positive vector for the wrong conjugate does not
settle the target. L019 already proves the divisor form, and L006
fixes the eigenvalue; neither is to be recomputed. Earlier support and
isometry exclusions do not cover an arbitrary rational divisor operator.

## Intermediate checkpoint saved during the calculation

Use K=Q[a]/(a^3+a^2-2a-1) and the source's linear functional
s(1)=1, s(a)=s(a^2)=0. The form b(x,y)=-2s(xy) has Gram matrix

```text
-2  0  0
 0  0 -2
 0 -2  2
```

The candidate isometry into the divisor space sends
1 to E, a to 2F, and a^2 to -O-2F. Its perpendicular line is
V=P-O-2F+E/2, of square -7/2. Thus an explicit rational form
identification is available, stronger than determinant/signature data.

Multiplication by a is self-adjoint for b. Its positive real eigenline
appears to belong to the most negative root, whereas L006 fixes the
positive root lambda=2cos(2pi/7). The candidate correction is to use
multiplication by a^2-2, which cyclically permutes the three roots.
An exact sign and eigenvalue check is still needed, followed by the
saved rational special-orthogonal approximation theorem to enter
the open ample cone. No chamber certificate or completed lemma is
claimed at this intermediate checkpoint.

## Completed test

The exact certificate is proved in
[L025](../lemmas/L025-cubic-rm-kahler-eigenvector.md).
The transfer identification above is correct. The negative root lies
in (-2,-3/2); its transfer idempotent has positive square, and a^2-2
sends its eigenvalue to the unique positive root lambda. Rational
special-orthogonal approximation then puts the eigenvector in an
open neighborhood of a scaled ample class. Conjugating the operator
preserves its rationality, self-adjointness and exact eigenvalue.

The result is ADVANCE / RESEARCH / REPRODUCTION: it closes the stated
prerequisite using known tools, without a claim of progress beyond
the checked literature. The exact arithmetic check is
`python3 scripts/cubic-kahler/check_eigenvector_certificate.py`.
The proof uses the saved source statements for the cone and group
approximation; their cited passages were also reopened this turn.
No numerical curve sampling or assumed integral isometry is used.

This finishes the three-turn discovery window with a mathematical
input. A separate source review must address actual stable-bundle
existence before that new target is investigated. No bundle or
transverse lift has been obtained.

## Mathlib

Coverage: **not checked**. The supporting transfer, approximation and
cone references, with their precise versions, are in the saved review.

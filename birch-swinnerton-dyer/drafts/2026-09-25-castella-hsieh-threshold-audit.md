# Castella--Hsieh nonvanishing: threshold audit

Date: 2026-09-25. Saved before the detailed published-source check.
This is working reasoning, not a claimed BSD proof.

## Gap, intermediate target, and test

For analytic rank m(E) = 2, L005 needs a nonzero strict class in the
rational Kummer image to obtain rank E(Q) >= 2. Its current upper bound
also requires L004's nonzero cyclotomic coefficient. Test whether
Castella--Hsieh's later nonvanishing theorem supplies the first input
from analytic rank alone, or gives a useful independent upper bound.
The universal higher-rank comparison remains unresolved either way.

Read the published Theorems A and B, their proofs, and the rationality
application. Retain every auxiliary hypothesis and distinguish complex
order, anticyclotomic order, Selmer dimension, and rational rank. Continue
the direct import only if it supplies the strict Kummer threshold without
assuming rational rank two or finite Sha. Otherwise record the exact
missing premise and retain any proved bound useful with future point input.

## Redundancy check

L005 already proves the local logarithm threshold. The previous audit
rejected importing two independent rational points from the 2016
construction; it did not check this 2022 nonvanishing theorem. Repeating
the same linear-algebra countermodel would add no new evidence. The
new test is the later theorem's actual arithmetic conclusion and whether
it bypasses either missing certificate input.

## Initial finding to verify

The author's manuscript states kappa != 0 implies Selmer dimension two,
and the converse assumes dimension two and nonzero localization. Its
Theorem B assumes positive rational rank and a degree-two
anticyclotomic theta order. Neither premise is simply m(E) = 2.
The application identifying the class with a rational-point regulator
explicitly assumes finite p-primary Sha. Check the published version
and the strictness assertion before drawing a final conclusion.

## Completed assessment

The [published-source audit](../foundations/07-castella-hsieh-nonvanishing.md)
confirms the hypotheses and distinguishes Theorems A/B from the
finite-Sha application in Section 5.7. It improves the conditional
upper bound: a nonzero class gives Selmer dimension two, so the
cyclotomic coefficient is unnecessary if Kummer membership can be
proved. [L006](../lemmas/L006-generalised-kato-kummer-certificate.md)
records that deduction and all remaining qualifications.

The original discriminating test fails: the paper does not supply
nonzero kappa with q(kappa) = 0 merely from m(E) = 2. Theorem B's
additional point hypothesis leaves the arithmetic bounds 1 <= r <= 2,
short of the required r >= 2. This is an informative negative about
the direct import, not a counterexample to any arithmetic conjecture.
The two-dimensional upper bound makes a geometric Kummer-membership
test useful even with nonvanishing and auxiliary choices still missing.

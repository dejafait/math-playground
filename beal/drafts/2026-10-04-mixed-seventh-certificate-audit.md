# Mixed seventh-power finite-certificate audit

This is the single research target approved by the prior SPECIALIZE assessment in [the certificate assessment](literature/2026-10-04-mixed-seventh-exceptional-certificate.md). The main gap is zero positive primitive solutions uniformly over the residual Beal signatures. The narrower test checks the arithmetic of the four genus-two curves and the 24 resultants in Chocian, arXiv:2609.26996v1, Section 6.2, equations (38)–(40). Its possible downstream use is verification of one necessary terminal component of the source's unverified fixed-signature argument.

The intended test counts the complete smooth projective models over F_29 and F_(29^2), reconstructs the Frobenius and two-trace polynomials, and compares every resultant with the transcribed source data. A discrepancy stops reliance on the displayed certificate. Agreement permits treating only its finite arithmetic as reproduced. It cannot supply the four-parameter reduction, the exhaustive modular/character list, the pure-field argument, or the unread original descent.

## Reasoning saved before calculation

Use F_(29^2)=F_29[w]/(w^2-2), after checking that 2 is a nonsquare modulo 29. The curve polynomial is f_t(x)=5x^6-12x^5+10t x^3+t^2, with t=14,10,25,15 in that order. Check gcd(f_t,f_t')=1. In the infinity chart u=1/x and v=y/x^3 the equation is v^2=5-12u+10t u^3+t^2u^6. At u=0 its points are v=±11, since 11^2=5 modulo 29. Thus both projective counts need two infinity points, which are smooth because 2v is nonzero.

For each field, form the exact multiplicity table of squares y^2 and sum that multiplicity at f_t(x) over all x. Independently check the counts with quadratic characters; over the extension use the norm a^2-2b^2 to the base field. From N1,N2 compute A=30-N1 and B=(A^2-(842-N2))/2. Compare T^2-A T+B-58 modulo 7 with the source's four polynomials, and compute the 24 Sylvester determinants modulo 7 with a separate exact rational-determinant check.

The closest source already claims the intended finite values, so this is a correctness reproduction, not a claim of new mathematics. No earlier notebook result checks this certificate; the unrestricted local-sieve and repeated-cube failures concern different mechanisms. The actual required threshold for Beal is global zero solutions; even nonzero resultants meet only a conditional finite-comparison threshold.

## Completed audit

All four curves are smooth; the complete projective (N1,N2) counts, in source order, are (29,955), (22,916), (37,931), and (25,883). The resulting integral two-trace polynomials are T^2-T-1, T^2-8T+11, T^2+7T+11, and T^2-5T-25. All four reductions and all 24 resultant entries agree with the printed certificate, and every resultant is nonzero modulo 7.

The full proof, count table, integral resultant matrix and exact scope are in [L016](../lemmas/L016-mixed-seventh-q29-finite-certificate.md). The standard-library [reproducer](../scripts/mixed-seventh-certificate/check_q29.py) and [saved output](../scripts/mixed-seventh-certificate/results.json) enumerate both fields, cross-check square multiplicities against quadratic characters, check smoothness, and compare finite-field Sylvester determinants with exact integral resultants. No upstream source claim is used to force these counts.

This is **RESEARCH / ADVANCE / REPRODUCTION**: a previously unchecked arithmetic component of the source candidate is now established locally, with no result beyond the checked literature and no new signature exclusion. The pass supports further critical scrutiny of the remaining comparison-family exhaustion interface. It does not clear the parked global-descent source blocker, and no additional mathematical attempt or source review is performed in this step.

## Mathlib

Coverage of the full certificate and supporting finite-field/Frobenius results: **not checked**. The source reference is [Chocian, arXiv:2609.26996v1, Section 6.2](https://arxiv.org/html/2609.26996v1); the prior assessment preserves the supporting PVT theorem and its scope. No formal verification is claimed.

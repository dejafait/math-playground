# Dahmen–Siksek's fifth-power/seventh-power classification

Imported on 2026-10-03 from the assessment completed before this research turn. Sander R. Dahmen and Samir Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100**, **Theorem 1, p. 67**, DOI [10.4064/aa164-1-5](https://doi.org/10.4064/aa164-1-5); [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/83637), [arXiv v2 theorem statement](https://arxiv.org/html/1309.4030v2#Thmtheorem1).

## Exact imported clause and source scope

The ell=7 clause of Theorem 1 classifies coprime signed integer solutions of

\[
X^5+Y^5=Z^7
\]

as exactly

\[
(1,-1,0),\quad(-1,1,0),\quad(1,0,1),\quad(-1,0,-1),
\quad(0,1,1),\quad(0,-1,-1).
\]

Every listed triple has a zero coordinate. Thus the clause excludes all nonzero pairwise coprime signed integer solutions, with unrestricted bases and with coordinates of absolute value one permitted. It is unconditional and imposes no restriction that 5 divide, or not divide, Z. Pairwise coprimality meets the source's coprimality hypothesis regardless of whether it is expressed using a common gcd or pairwise gcds.

The prior assessment read the published definitions and theorem statements, pp. 65–67, Lemma 2.2, p. 69, and Section 3, pp. 69–78; its page references are journal page numbers. The statement was cross-checked in arXiv v2, submitted 26 January 2014. Lemma 3.1 and Proposition 3.2 handle the branch 5 not dividing Z using the curve Y^2=20X^7+5; Proposition 3.3 handles the branch 5 dividing Z, with Lemma 3.12 giving an alternative at ell=7. Both branches are covered by the cited published theorem. The GRH qualification in Theorem 3 concerns different exponents and is not a hypothesis of this imported clause.

The publisher PDF supplied the read theorem and proof-case text. The author-hosted PDF returned HTTP 403 and a shell download failed DNS resolution; neither failure leaves an essential case of this import unread. MAGMA computations, external scripts, and the underlying Chabauty and modular proofs are imported as part of the published theorem and are not independently reproduced or rerun. Only the ell=7 clause is imported here; the other exponents in the paper are outside this application.

## Mathlib

Coverage of the full signed classification: **not checked**. Supporting fifth-cyclotomic, Chabauty, modular, power, sign, and coprimality results were not checked in Mathlib. Theorem 1 is a match for the external classification used here; its numbered proof components support the published proof rather than supply separate matching library declarations. The citations do not assert formal verification.

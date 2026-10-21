# Rational factorization of H — source comparison completed

TARGET: Determine the factorization of L095's binary octic H over Q and test whether it supports a rational factor-by-factor cube descent.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior ordered-(3,5,11) and rational-factor comparisons; searched exact coefficient strings, the cover polynomial and binary-form perfect-power/resultant descent terminology. No matching published factorization of this H was located in the bounded search; this is not a novelty claim.
SOURCE_EVIDENCE: Milne, Fields and Galois Theory v5.10 (September 2022), Propositions 1.13 and 1.16 and Remark 1.17, printed pp.12–13, statements and relevant proofs; Moreno Maza, Advanced Computer Algebra, The resultant, Propositions 5–7 and their proofs; Alekseyev–Tengely (2014), Theorem 2 and proof pp.4–5; Siksek–Stoll, 345-revised.pdf, Section 2 setup, Theorem 2.1 and Section 3 resultant-support paragraph, printed pp.3,6, inspected.
COMPARISON: Standard exact factorization/irreducibility and Bezout-resultant methods cover the proposed elementary test, but do not supply its input-specific answer. The inspected quadratic-factor gcd theorem has degree restrictions and the hyperelliptic descent uses squares; neither is a ready cube-descent or integer-emptiness theorem for H.
GAP: Check the actual factorization certificate and homogeneous boundary, and only if nontrivial factors exist prove their finite cube-twist support for both L095 systems, including contents, signs and the 5^11 scale, while retaining the fifth-power equation.
REASON: Essential elementary methods are available; specialize them in a later research turn rather than reprove source theorems or assume a square-descent generalization. No factorization or new mathematical result was derived in this review.
LITERATURE_REASON: The target changed from the audited eleven-adic construction to global rational factor descent; the prior rational-root assessment did not cover exact octic factorization or resultant support.
SCOPE: Exactly TARGET, using audited L095 and elementary integer unique factorization, Gauss/Eisenstein criteria, exact polynomial arithmetic, homogenization and explicit Bezout/resultant certificates. Excludes number-field descent, Selmer algorithms, curve-point classification, height bounds and any signature exclusion.

## Gap, inputs and decision test

The main gap is global integer elimination in the rational-factor branch
of ordered (3,5,11). Other algebra factors and residual signatures remain
independent unresolved gaps. The intermediate target is a certified
rational factorization of H and, if it splits, a controlled finite
factor-by-factor cube-twist restriction. Its plausible downstream use is
smaller simultaneous power systems retaining C=5m+u^5 or
C=m+5^10 u^5, positivity and all original gcd restrictions.

Essential input: L095, its exact Q,H, both systems and both converses.
Read its complete proof and audit for the denominator, scale and
coprimality conditions. L096 and ATTEMPTS/043 are stop context only:
exact eleven-adic points retire standalone local exclusion, not this
global test. Histories 317 and 319 distinguish the construction and
independent audit. No cross-notebook input is used. The supplied proposal
and targeted rational-factor records contain no earlier factorization
certificate or completed factor-by-factor descent.

Continue this mechanism only with nontrivial factors and rigorously
controlled finite twist support preserving both equations. Certified
irreducibility stops direct rational factor-by-factor descent. Failure
to control support also misses its threshold. Neither outcome excludes
integer solutions; no assertion about descent over number fields follows.

## Inspected primary methods

J. S. Milne, *Fields and Galois Theory*, v5.10, September 2022,
[author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf), printed
pp.12–13 (PDF indices 11–12): Proposition 1.13 gives integral
nonconstant factors for a rationally reducible integral polynomial.
Proposition 1.16 applies when a prime avoids the leading coefficient,
divides every lower coefficient and its square avoids the constant term;
then the polynomial is rationally irreducible. Both proofs were read.
Remark 1.17 describes a finite exact factorization procedure using
integral monic normalization and coefficient bounds. These are general
methods, not a precomputed answer for H. Apply a simple named criterion
first where possible; a numerical factorization printout is insufficient.
There is no reason to reprove these criteria. Homogeneous applicability,
contents and possible coordinate factors must still be justified locally.

Marc Moreno Maza, *Advanced Computer Algebra*,
[The resultant](https://www.csd.uwo.ca/~mmorenom/CS424/Lectures/ResultantGcd.html/node3.html),
undated course page retrieved 2026-10-18: Definition 4 identifies the
Sylvester determinant; Propositions 5–6 characterize nonvanishing for
coprime polynomials over a field/UFD. Proposition 7 supplies an integral
Bezout identity for the resultant, with the proof using Cramer's rule.
Statements and proofs were inspected. Use nonconstant factors and a
nonzero resultant. These univariate inputs support explicit certificates
in both homogeneous coordinate charts; do not silently infer that one
affine chart controls common divisibility at infinity.

M. A. Alekseyev and Sz. Tengely, *On Integral Points on Biquadratic
Curves and Near-Multiples of Squares in Lucas Sequences*, Journal of
Integer Sequences 17 (2014), Article 14.6.6,
[primary article](https://www.maths.tcd.ie/EMIS/journals/JIS/VOL17/Alekseyev/alekseyev3.pdf),
Theorem 2, printed pp.4–5 (PDF indices 3–4), assumes two integral
homogeneous quadratics, nonzero resultant and coprime integer arguments.
Their gcd divides the largest Sylvester Smith invariant. Its full proof
and Remark 3 were read: two integral linear-combination certificates
control both pure coordinate powers. This theorem is not cited for
arbitrary factor degrees; a later general-degree application must give
its actual two-chart certificates using the preceding resultant input.
No Smith-form optimization is required by the proposed test.

S. Siksek and M. Stoll, *Partial Descent on Hyperelliptic Curves and the
Generalized Fermat Equation x^3+y^4+z^5=0*,
[author-hosted revised manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/345-revised.pdf),
16-page file retrieved 2026-10-18, Section 2, printed p.3, and
Theorem 2.1/Section 3, printed p.6: the setup is a squarefree even-degree
binary form and y^2=f(u,v). The theorem gives covering/ Selmer containment;
the support paragraph removes primes outside leading coefficient and
factor/cofactor resultant. These passages were inspected to check the
power hypothesis. They do not establish a cube analogue for H. No
Selmer computation or cubic generalization is imported. The elementary
integer valuation test remains independently available in the scoped
research target; its actual specialization must be written out.

## Reused signature coverage and bounded discovery

Reuse `2026-10-18-ordered-three-five-eleven-coverage.md` and
`2026-10-18-ordered-three-five-eleven-rational-factor.md` unchanged.
Their inspected Putz terminal cases exclude different coefficient sets;
Pacetti–Villagra Torcomian's relevant prime ranges except eleven, and
the explicit-abc bound is conditional. No new reason to reopen those
sources arose. The inaccessible Dahmen provenance page remains an
unread, nonessential lead; no result from it is assumed.

New queries included `"1215" "1782" "2970" "2475" polynomial`,
`"55" "165" "594" "1100" "Fermat"`,
`"55" "594" "1215" "octic"`,
`"3t^2+t+1" "factor" Fermat`, binary-form perfect-power descent,
and homogeneous polynomial value gcd/resultant terminology. Irrelevant
coefficient coincidences were discarded. Discovery found no exact H
classification; standard methods rather than novelty motivate the test.
Full matching Mathlib coverage is not checked, not asserted absent.

## Approved mathematical scope, not performed here

After separate approval, determine H's rational factorization with a
checkable certificate. Begin with named elementary criteria; no large
search is prescribed. Verify the passage from dehomogenization to the
binary form. If nontrivial factors occur, certify the exact product and
irreducibility of every reported factor; retain contents and signs,
and prove common-divisor support using both projective charts. Only
then test whether cube exponents outside that finite support and the
system-II scale yield a useful finite twist restriction. Keep both
simultaneous equations and L095's primitive positive domains throughout.
Repeated factors or zero resultants require explicit treatment, not a
coprime-factor assertion. No rational-point algorithm, number-field
arithmetic, abc, GRH or effective height bound is assumed.

This literature-only review approves methods and scope, not the
factorization, any new cube-twist lemma or integer emptiness. It changed
no lemma, mathematical script, DAG or argument overview. The next action
remains exactly TARGET; this newly changed assessment awaits the
supervisor's separate approval before research.

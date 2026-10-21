# Retained cubic Legendre normalization — source coverage approved

TARGET: For unchanged E_0,F, determine the twist square classes of the six ordered-root Legendre normalizations of the retained cubic and whether full rational 30-torsion forces any class to be trivial.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step276 searched normalization, root-difference, Legendre-isomorphism and full-30/odd-torsion terminology; inspected the four primary references below. Compared L045,L048,L070, foundations/05 step272, existing Legendre assessments, history/272-275 and ATTEMPTS/028,031,032. No inspected theorem settles the retained full-30 forcing implication; a failed search is neither a counterexample nor a novelty claim.
SOURCE_EVIDENCE: Auer–Top, J. Number Theory 95 (2002), Introduction p.303, Lemmas 2.1-2.2 p.304 and six-parameter discussion p.305; Milne, Elliptic Curves, second edition (2021), II Theorem 2.4(b) pp.52-53 and supporting proof of 2.1(b) pp.50-51; Yelton arXiv:1704.06190v2 (2 August 2017), degree-three definitions and Theorem 1(a) p.1; Corwin et al. arXiv:1207.5169v2 (4 February 2013), Theorem 1.1 and Example 1.2 p.2, Lemma 4.5 p.15. Reuse L070's inspected twist formula and foundations/05 step272's qualified IUT source comparison.
COMPARISON: Known pointed-coordinate, Legendre square-class and full 4-division criteria cover the normalization calculation and a discriminating radical-membership test. The remaining specialization must assign each ordering its class, verify the retained hypotheses, and test what the actual 30-torsion information proves. No automatic triviality or nontriviality verdict is imported.
GAP: The six retained classes and their values in F are not calculated here; full 30-torsion must not be substituted for full 4-torsion. Actual native T, its specified model, minimal generation, source-marked all-image factorization and essentiality remain unresolved.
REASON: This completes the missing theorem-level comparison and approves a bounded mathematical attempt on the unchanged target. Known criteria allow a conditional test without effective coefficients; an unresolved radical obligation is an admissible endpoint, not an assumed pass.
SCOPE: The same monic cubic E_0:y^2=g(x), F=Q(zeta_60,E_0[30]), and all six ordered-root pointed normalizations. No field enlargement, curve reselection, other-curve counterexample construction, native T identification, exact global generation or IUT numerical assertion.

## Main gap and purpose

The main gap remains finite B>=A. This intermediate target could
replace L070's unspecified comparison character by explicit square
classes. Even a passing F-model test would require identification
with the specified native descent. Independent initial data, marked
transport and essentiality would remain unresolved.

This is the separate literature approval of the target saved in
step275. No normalization calculation, new lemma, proof audit or
mathematical script was performed in step276.

## Inspected primary results

[Auer and Top, publisher's version](https://pure.rug.nl/ws/portalfiles/portal/14410242/2002JNumberThAuer.pdf),
Introduction p.303, treats an arbitrary field k of characteristic
different from 2: a split cubic y^2=x(x-a)(x-b), with distinct
0,a,b, is k-isomorphic to a Legendre curve exactly when one of
±a, ±b, ±(a-b) is a square in k. Lemma 2.1, p.304, characterizes
divisibility of a rational 2-torsion point by 2 through its two
root differences; its proof uses the full 2-descent map. Lemma 2.2
records the exceptional self-twist case. The discussion before
Proposition 2.1, p.305, lists the six geometric parameters.
Proposition 2.1 itself assumes a finite field: do not import its
finite-field conclusions over F. The [arXiv v1 text](https://arxiv.org/pdf/math/0106273),
pp.1-3, was also inspected to resolve symbols in the publisher
extraction; no byte-identity claim is made. Import the general-field
criteria without reproving descent or transferring finite-field claims.

[Milne, Elliptic Curves, second edition](https://www.jmilne.org/math/Books/EC2.pdf),
II Theorem 2.4(b), pp.52-53, gives necessity and sufficiency of the
origin-preserving Weierstrass coordinate transformation with u
nonzero and r,s,t in the field. The supporting coefficient comparison
in the proof of Theorem 2.1(b), pp.50-51, was read. This covers
assignment of an individual ordering rather than equality of j alone.
The retained assignment and sign conventions remain next-turn work.

[Yelton, arXiv:1704.06190v2](https://arxiv.org/pdf/1704.06190v2),
Theorem 1(a), p.1, applies over any field of characteristic different
from 2. In its degree-three case the cubic is monic with distinct
roots alpha_i, and A_i^2=alpha_(i+1)-alpha_(i+2), cyclically.
It states K(E[4])=K(E[2],zeta_4,A_1,A_2,A_3), using full point
coordinates. This is a supporting criterion, not a claim that
30-torsion contains 4-torsion. Use the general Theorem 1(a);
Proposition 6 occurs after the generic-field reduction and must
not be quoted without that context. No 8-division result is needed.

[Corwin, Feng, Li and Trebat-Leder, arXiv:1207.5169v2](https://arxiv.org/pdf/1207.5169v2),
Lemma 4.5, p.15, supplies the root-difference quadratic-extension
normalization. Theorem 1.1 and Example 1.2, p.2, distinguish the
2-adic factor from odd factors and the cyclotomic intersection.
Their example is over a non-Galois cubic field, not the retained
Q-curve. It is a comparison lead, not a counterexample here.
Applying it after adjoining odd torsion and cyclotomic constants
would require a separate field-intersection argument, not derived
in this literature turn.

## Applicability and remaining difference

Essential inputs are L045,L048,L070 and foundations/05 step272.
L045 supplies full-coordinate rational 30-torsion and unchanged
cyclotomic constants; L048 retains the same monic nonsingular
cubic and nonexceptional j. A later application must explicitly
check rationality and distinctness of the roots, the origin,
characteristic and every coordinate change. The cited results
cover these field-level hypotheses. No integral or minimal-model
assertion is required for this normalization test.

Assignment of classes to orderings is an elementary specialization
of the known coordinate/isomorphism results. It needs writing out
because F is fixed and the question concerns the twist, not just
the geometric parameter. No reproof of a general theorem is needed.

No inspected matching theorem answers the full-30 forcing question.
The bounded search found stronger 4-division information and known
square-class criteria, so this portion is ready for a mathematical
test, not a claimed universal implication. The next attempt may
establish only a conditional criterion and identify the remaining
field-membership obligation. Absence of a theorem, effective
coefficients or an assumed 4-torsion hypothesis does not prove
that all six classes are nontrivial. Failure for one ordering does
not exclude all orderings. L070 remains the full-kernel test after
a concrete comparison is identified.

## Search, overlap and continuation limits

Queries included `Legendre elliptic curve rational 2 torsion
differences roots squares Legendre form full 3 torsion`, `elliptic
curve Legendre form rational odd torsion quadratic twist square
class 30 torsion`, `elliptic curve 4 division field square roots
differences roots theorem`, `Legendre elliptic curves over finite
fields Auer Top pdf`, `"Legendre" "30-torsion"`, and
`"Legendre" "full" "odd torsion"`. A MathOverflow discussion
was a discovery lead only; its formulas are not imported. A
Silverman PDF endpoint failed; Milne and Auer–Top independently
supply the necessary coverage. Finite-field isomorphism counts
and unrelated torsion-family search hits do not assess this
retained implication.

The local search found no duplicate ordered-root result. L070
assumes a supplied geometric comparison and leaves its character
unknown. Foundations/05 step272 allows a quadratic twist before
Legendre form; it does not remove this obligation. Preserve
ATTEMPTS/027,028,031,032 and unfinished work. This target does
not reopen exact-Tate globalization, the marked-coordinate route
or the stopped tensor-enclosure objection.

Retain E_0,F,K_glob,Omega,embedding,u,w,H,N and
M>=max(M_tors,31), full-coordinate torsion and changed q_0
with v_3(q_0)=30. Coefficients remain existential. Native
T=F_tpd subset F and specified E_L/T remain conditional;
actual T,lambda,d,chi|G_F and minimal generation are unidentified.

Continue if the source-backed calculation yields an all-ordering
criterion or a decisive retained radical-membership argument.
If forcing needs an unproved division-field intersection or
unavailable coefficients, record that precise missing input and
stop that assertion; do not adjoin radicals or replace E_0.
A different target needs REVIEW_REQUIRED coverage. Full matching
and supporting Mathlib coverage is not checked; no absence or
formal-verification claim is made.

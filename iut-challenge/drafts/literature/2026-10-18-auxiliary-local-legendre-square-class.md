# Auxiliary local Legendre square class — source approval

TARGET: Determine whether at least one of L074's three auxiliary root-difference classes is a square in H under the fixed embedded completion F_aux,u=H.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step297 checked L073,L074 and L048's original-model congruences, reused the prior Legendre assessment, and checked ATTEMPTS/027,028,031,032,033. Bounded external searches for local-field Legendre form, split multiplicative square classes and Hensel lifting led to the general-field criterion and exact complete-DVR lifting theorem; no matching auxiliary-witness verdict or novelty claim was established.
SOURCE_EVIDENCE: Milne, Algebraic Number Theory v3.08 (19 July 2020), section 7, complete-DVR convention p.119 and Proposition 7.31/proof p.120; Auer–Top, J. Number Theory 95 (2002), Introduction p.303 and Lemma 2.1/proof p.304; reuse Milne, Elliptic Curves (2021), II Theorem 2.4(b) pp.52–53 and the existing ordered-root comparison coverage. Primary statements and the essential simple-root proof were retrieved on 2026-10-18.
COMPARISON: Hensel's simple-root theorem covers testing square roots of units via nonzero square residues in O_H; the known coordinate criterion identifies why this tests the prescribed monic model. L048 already supplies the family-wide reduced cubic. The remaining work is to locate the actual embedded roots and apply the test to L074's differences, without rescaling the cubic or using a global Galois element as a local obstruction.
GAP: No square-membership verdict for a,b,b-a in H is established in this literature step. Root integrality, reduction multiplicities, signed differences and every needed nonzero derivative must be checked in the next specialization. No essential source remains unread for that bounded test.
REASON: This separate approval fills the missing local lifting coverage identified by step296. The new source import makes the exact saved target ready for mathematics; no additional Tate-coordinate formula, source-access retry or global-field construction is needed.
SCOPE: Exactly TARGET for the fixed L073 witness, L074's original monic cubic and three classes, their actual images in H and the unchanged embedding. Permits root-integrality/reduction and simple-root Hensel specialization, with L048's family-wide congruences. Does not cover a global field change, native T identification, full division-field equality or an IUT comparison.

## Primary coverage and limits

This is the separate source approval of step296's proposed continuation.
No local square-membership proof, new lemma or mathematical script was
produced in step297. SPECIALIZE approves the following bounded next-turn
application, without asserting its outcome.

[Milne, *Algebraic Number Theory*, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
section 7, printed pp.119–120 (PDF pp.120–121), specifies a complete
discrete valuation ring A and a generator pi of its maximal ideal.
Proposition 7.31 states that a simple residue root of f in A[X] has a
unique lift in A with that residue. Its full proof on p.120 constructs
successively more accurate roots, using the invertible residue derivative,
and completeness gives the limit; uniqueness follows at every precision.
Thus this is an exact lifting theorem, not a finite-precision preview.
For a proposed unit difference d, the application must check a nonzero
residue root of X^2-d and its derivative 2X. No residue-characteristic-two
case is imported. The stronger Newton estimate and factor-lifting
Theorem 7.33 are unnecessary here and are not new dependencies.

[Auer–Top, *Legendre Elliptic Curves over Finite Fields*, version of
record, J. Number Theory 95 (2002), 303–312, DOI
10.1006/jnth.2001.2760](https://pure.rug.nl/ws/portalfiles/portal/14410242/2002JNumberThAuer.pdf),
Introduction p.303, gives the criterion over a field k of characteristic
different from two: a split equation y^2=x(x-a)(x-b) is k-isomorphic
to a Legendre curve exactly when a signed root difference is square.
Its general-field Lemma 2.1, p.304, also relates halving a rational
two-torsion point to two square root differences, using two-descent.
The latter is supporting coverage only; no rational four-torsion
hypothesis is assumed. Their finite-field isogeny and counting results
do not apply to H. The existing assessment
`drafts/literature/2026-10-17-retained-legendre-normalization-square-classes.md`
already covers the pointed coordinate changes through Milne II.2.4(b).
Reuse it rather than reprove general coordinate or descent theorems.

## Exact applicability obligations for the mathematical turn

L073 supplies the same auxiliary monic integer cubic in L048's fixed
3^M-neighborhood, full H-rational 30-torsion, and the actual embedded
completion F_aux,u=H. L074 fixes its distinct labelled roots and its
three nonzero differences. L048's family-wide proof records
c=1/4=1 modulo 3 and d=e=0 modulo 3 for the original coefficients.
This is existing model information, not an asserted local square verdict.

The next proof must use these original coefficients. It must justify
that the roots lie in O_H, identify their residue multiplicities from
the split factorization of the reduced monic polynomial, and select
an actual difference between the relevant roots. Before applying
Proposition 7.31 it must exhibit a nonzero square residue and verify
the derivative is a unit in O_H. Signs must match L074's a,b,b-a;
L073's zeta_60 supplies i if a sign conversion is needed. Arbitrary
root labelling must not change the existential test. Monicity and
integrality are essential here; no freely rescaled equation is allowed.

This elementary specialization is necessary because the field and
model are fixed and the coefficients are existential. No inspected
theorem directly names this auxiliary witness, and no general theorem
needs reproof. H is a finite extension of Q_3, so O_H satisfies the
complete-DVR and odd residue-characteristic hypotheses. Computing its
full residue field or every local square class is not required if one
explicit residue test settles the saved existential target.

L074's tau fixes the global F_aux but is not asserted to belong to the
chosen local decomposition group. Its global radical exclusion therefore
cannot replace this local test. Conversely a square in H need not be a
square in F_aux. L075's audited global obstruction remains in force.

## Search, overlap, decision and continuation

Queries included `"Legendre" "split multiplicative" "square"`,
`"Legendre" "local field" "isomorphic" square`,
`"elliptic" "Legendre form" "Hensel"`,
`"elliptic" "Legendre" "Hensel" "square"`, and
`Milne Hensel lemma simple root algebraic number theory Theorem`.
Several returned unrelated uses of Legendre or finite-field material;
none is evidence. The exact author-hosted lifting theorem and the
publisher's general-field criterion supply adequate primary coverage.
No novelty inference follows from the bounded search.

The local duplicate check covered the existing ordered-root assessments,
the auxiliary source notes, L073/L074 and history/293,296. These address
global radicals and descents, not this local test. L048 supplies model
congruences, not the claimed square-membership conclusion. The retained
local square-root assessment concerns q_0 and -1, not these differences;
its Tate uniformization need not be extended or reproved here.
ATTEMPTS/027,028,031,032,033 were checked: exact-curve globalization,
universal-model ambiguity, marked coordinates, the stopped tensor
objection and classification retrieval are not being reopened.

The threshold is one of a,b,b-a in H^{*2}. A positive verdict could
motivate a separately reviewed global modification preserving H;
it proves no such modification, preservation of N or native field
prescription. A negative verdict stops this way of retaining H.
If the required residue/derivative bridge fails, record that precise
obstruction without claiming a nonsquare from an unsuccessful test.

Essential continuation inputs are L073,L074 and L048's family-wide
original-model congruences; L075 is the global contrast, not a premise
of local lifting. Do not assume q_aux=3^30 or q_aux=q_0. Retain
E_0,F,K_glob,Omega,embedding,u,w,H,N,q_0 unchanged. Actual native
T/model, retained scalar occurrence/memberships, changed-field preservation
of N, independent initial data, marked all-image factorization, pilot
transport, essentiality and original finite B>=A remain unresolved.
Mathlib coverage for the combined specialization is not checked;
no absence claim is made.

The challenge scope was rechecked on 2026-10-18 at the supplied
[dated 2023-07-07 announcement](https://zen.ac.jp/news/0ul6zqed9-0)
and [current official prize page](https://zen.ac.jp/en/lp/icp).
This source approval does not alter foundations/01's distinction
between an inherent/essential flaw and prize adjudication, and supplies
no candidate flaw in IUT III Corollary 3.12.

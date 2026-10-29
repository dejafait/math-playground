# Marked decomposition critical audit — approved source coverage

TARGET: Critically audit L127's Q-isogeny and ordinary-rank identity against the exact marked cover and cited Prym comparison.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the decomposition assessment's terminology/search and ATTEMPTS/050–052 comparison; read canonical L127 and targeted L110/L111/L113 ranges, then retrieved the primary theorem statements and essential proof passages listed below.
SOURCE_EVIDENCE: Bruin arXiv:math/0408069v2 Section 2.1–2.2 and complete Proposition 2.2 proof pp.4–5; Docking arXiv:2108.09564v2 Section 2/Table 1 p.4 and Lemmas 4.1/5.3 with proofs pp.6/8; Milne Abelian Varieties v2.00 I.7.1/7.2 statements and proofs pp.32–34, I.16.7 statement and proof-reference paragraph p.69.
COMPARISON: These known results cover the exact type of structural claim to audit; canonical instance data must still be critically verified against every hypothesis and map, without importing any rank bound.
GAP: Source readiness is complete for the separate audit; correctness of L127's instance specialization and ordinary-rank transport remains unverified by this literature turn.
REASON: Primary coverage supports a bounded known-result audit using the existing curves and maps; no new decomposition theorem or mathematical script is required.
LITERATURE_REASON: The saved continuation was REVIEW_REQUIRED; this turn supplies its missing independent theorem-level coverage, including the actual pullback identification and both comparison composites.
SCOPE: Exactly TARGET, using L127 and its existing L110/L111/L113 inputs; correction or narrowing within that structural claim is covered, but new curves, rank computations, point searches and descent mechanisms are not.

The complete argument is canonical in L127. Essential inputs are L110,
L111 and L113, with actual factors a and b/9 and product W=hR/3.
The audit should test whether the pullback from the actual E identifies
with the Prym over Q, whether the product projection is unramified on
all proper charts, and whether the cited comparison really gives both
multiplication-by-two composites. The ordinary rank argument must use
Q-rational homomorphisms and finite generation, without asserting an
integral group isomorphism or interpreting torsion as an upper rank.

A successful later audit would certify this local known-theorem
application only. Upper ranks and point control, full supported
arithmetic/descent, degree-nine recovery, remaining factors, both L095
systems, minus-eleven and other signatures remain independent gaps.
If a source hypothesis or exact twist fails, correct or narrow L127;
do not turn that failure into a claim against Beal. Coverage for that
later audit is now approved. The audit itself was not performed here.

## Primary source comparison

The reused assessment is
`drafts/literature/2026-10-24-marked-jacobian-quotient-decomposition.md`.
Its search remains adequate for this unchanged structural mechanism;
the new task tests an existing application rather than proposing a new
mathematical result. No originality is inferred from those searches.

Nils Bruin, *The arithmetic of Prym varieties in genus 3*, Compositio
Math. 144 (2008), 317–338, DOI 10.1112/S0010437X07003314;
[arXiv v2](https://arxiv.org/pdf/math/0408069v2), 31 May 2006,
Section 2.2, Proposition 2.2, manuscript pp.4–5. The inspected setup
requires a squarefree polynomial of degree 2g+2, split over the base
field into two even-degree factors. The proposition identifies the
product of factor Jacobians with the Prym through the stated pullbacks.
Its complete proof first establishes image containment using norm,
then isogeny, and gives a functorial argument for the stronger
isomorphism. This last assertion is a cited theorem, not an independently
reproved fact here. Section 2.1 identifies the connected norm kernel
with the involution-difference image. Do not use its adjacent polarization
wording as an additional input: the audit needs only abelian varieties
and the specified maps. The degree-two factor is not excluded by the
displayed hypotheses; its genus-zero Jacobian must be handled explicitly.

Jordan Docking, *2-infinity-Selmer rank parities via the Prym construction*,
J. Number Theory 265 (2024), 208–225, DOI 10.1016/j.jnt.2024.06.009;
[arXiv v2](https://arxiv.org/pdf/2108.09564v2), 24 July 2023,
Section 2/Table 1, manuscript p.4. The source explicitly states the
base/Prym K-isogeny as sum of pullbacks/inclusion, its reverse map
as norm and involution difference, and both multiplication-by-two
composites. The rational-point proviso is for base genus three;
base genus two is included without it. Twist ambiguity is explicit,
so the audit must retain the existing cover rather than choose a
convenient twist. Lemma 5.3 and its complete proof, p.8, put the
kernel in geometric two-torsion; its supporting Lemma 4.1 and proof,
p.6, were also read. Kernel cardinalities are not counts of rational
points. No parity theorem, BSD or finiteness of Sha is needed for
the structural maps. Ordinary rank must be checked separately.

J.S. Milne, *Abelian Varieties*, v2.00, 16 March 2008,
[author notes](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Chapter I Proposition 7.1 and Theorem 7.2, printed pp.32–34,
give the finite-kernel/surjectivity criterion and multiplication
isogenies. Their proofs were inspected. Theorem 16.7, p.69,
gives finite generation for abelian varieties over fields finitely
generated over their prime fields, including Q. Its proof paragraph
refers the number-field proof to Serre (1989), Chapter 4; that book
was not independently read. Import finite generation by this precise
named theorem. Tensor transport is an applicability check, not a
new Mordell–Weil proof or an assertion of integral group isomorphism.

## Bounded audit specification and stop test

The main gap is still all positive primitive integer solutions for all
residual signatures. The intermediate target is verification of L127's
structural rank reduction. Its possible downstream use is to replace
one genus-three rank question by two existing quotient rank questions.
Neither quotient upper rank nor point control follows from this review.

Use only the existing instance data: L110's squarefree sextic/genus,
L111's geometric degree-four compositum, disjoint simple branch sets,
finite and infinity charts, projections and elliptic origin, and L113's
proper Q-isomorphism. Targeted proof ranges inspected for applicability
were L110's quotient and squarefreeness discussion; L111's equations
(7)–(8), degree/projection discussion and corresponding audit paragraphs;
and L113's smooth-proper transport paragraph. This is source scoping,
not independent verification of their calculation certificates.

The later audit must check the following existing claims in L127:

1. Its product map D→B is the connected degree-two quotient by the
   simultaneous sign change, distinct from D→E. Inspect fixed points
   on both finite and infinity charts; do not inspect rational points
   alone or omit geometric infinity fibers.
2. Bruin's factors are exactly a and b/9, with coordinates h and R/3
   and product W. Check the factor genera, rational rescaling to E,
   origin convention, and that the pullback identification is over Q.
3. Docking's maps have the correct source/target and use this Prym;
   verify both composites and the direction of transport through
   alpha:C→D. Distinguish inverse of an isomorphism from inverse of
   an isogeny on integral rational points.
4. The finite-kernel and surjectivity claims use abelian-variety maps
   over Q. Check ordinary rank after tensoring rational points with Q
   using finite generation, without replacing rank by Selmer parity.

Continue only if every load-bearing hypothesis and map matches.
On failure, identify and correct/narrow the specific statement, preserving
the original evidence. Do not silently weaken the asserted F to an
unspecified isogeny or assume a polarization formula. An unresolved
source issue means withhold audit approval, not claim Beal false.

## Duplicates, failures and limits

L127 is already the canonical structural application, so another lemma
would duplicate it. The next turn should audit that file. Existing
ATTEMPTS/050–052 were reread narrowly: the bounded genus-two detector,
elliptic rank-zero proposal and S-class backend probe are stopped for
different reasons. No such route is reopened here; L112's positive
rank and L126's torsion constraints do not certify upper rank.
Unfinished L108 is preserved. Historical stops are not global bans.

The unchanged primary target scope is reused from foundations and the
previous assessment; no new route or prize-rule claim is selected here.
Mathlib coverage of the full Prym comparison and Jacobian isogeny APIs
remains not checked, with no absence or formal-verification claim.
No new result, lemma, mathematical script, DAG edge or PROOF.md change
is made. The remaining task is one separate critical audit under this
IMPORT assessment, classified KNOWN_IMPORTED.

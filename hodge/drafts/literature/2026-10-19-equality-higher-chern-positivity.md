# Equality kernel — higher-degree positivity source comparison

TARGET: Assess whether higher-degree Chern–Weil positivity for rank-two hyperholomorphic bundles yields an independent necessary inequality for L071's equality kernel beyond rank truncation and Euler tests.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact hyperholomorphic/higher-Chern searches and stronger Schur-form, quaternionic-positive-form and Rozansky–Witten leads were compared with the saved lower-Chern and representative assessments and ATTEMPTS/034,075–076; queries and primary passages inspected are recorded below.
SOURCE_EVIDENCE: Inspected Wan (2024), Definitions 2.1/2.4, Theorems 1.2/1.3 and Section 4 equations (4.17)–(4.22); Fagioli (2022), Section 2, Lemma 2.1/Theorem 2.2 and their proofs; Błocki–Pliś (2013), Theorems 1–3 and Sections 2–3; Verbitsky 0801.1899, Section 4.3/Proposition 4.10 and positivity proof; Hitchin–Sawon math/9908114v1, Proposition 1, Theorem 3 and Sections 3/6.
COMPARISON: The Schur/Chern positivity results require additional curvature positivity; the quaternionic result transfers an already positive form; Hitchin–Sawon's formula concerns tangent curvature on an irreducible compact hyperkähler manifold. None of these inspected statements supplies a degree-eight inequality under L071's actual hypotheses alone.
GAP: No applicable independent degree-eight constraint was identified. This bounded comparison does not prove that none exists, classify invariant quartic curvature polynomials, or decide F existence.
REASON: Park the attempted positivity imports on explicit hypothesis mismatches; do not invent an inequality, add Griffiths/Nakano positivity, or re-evaluate the stopped energy criteria. A different actual-family local-degree source question is registered separately.
SCOPE: Hypothetical locally free rank-two Omega-polystable F on the identical marked K3 product, integral c_1=0, ch_2=-14e_1-21e_2-tau_D, common ordered structures and exact metric. Source comparison only; no mathematical specialization, changed data, or new lemma is approved.
LITERATURE_REASON: Essential unread degree-eight source coverage was outside the ready Kähler alpha-charge assessment; this review resolves the scope of the inspected positivity leads without repeating that energy calculation.

## Gap, target and decision test

Universal primitive rational Hodge realization remains open. This local
route also lacks an actual equality kernel F. The intermediate target
was a precise necessary degree-eight inequality, applicable to its
existing conditional compatible connection and independently evaluable
on its full characteristic data. It could filter kernel existence while
leaving cycle construction, separation, ambient extension, reconstruction
and transverse transport independent.

The continuation threshold was an applicable theorem yielding a constraint
beyond rank truncation, Euler, ordinary Bogomolov and the stopped alpha
criteria. The inspected candidates do not reach it. This is a NEGATIVE
source-scope result for these imports, not a new mathematical obstruction
to F, a general impossibility theorem for positivity, or a novelty claim.
EXPLORE records the bounded absence of an adequate match; it approves no
particular inequality or calculation. The present import mechanism is
parked in ATTEMPTS/077.

## Primary statements and applicability

**Schur forms.** Xueyuan Wan, *Positivity of Schur forms for strongly
decomposably positive vector bundles*, Forum of Mathematics, Sigma 12
(2024), [published HTML, DOI 10.1017/fms.2023.125](https://doi.org/10.1017/fms.2023.125),
Definitions 2.1/2.4 and Theorems 1.2/1.3. Type I requires at every point a
tangent decomposition U direct sum V, Nakano positivity on E tensor U,
dual Nakano positivity on conjugate(E) tensor V, and zero cross curvature.
Theorem 1.2 gives weak positivity for every Schur form of weighted degree
k<=dim X. Theorem 1.3 gives positivity under (dual) Nakano positivity.
Read the Section 4 proof through (4.17)–(4.22), including its general-k
case: the positive decomposition and rank conditions enter essentially.
Neither condition is supplied by L071. This is not a theorem for arbitrary
Hermite–Einstein or invariant-curvature bundles. Finski's original paper
is a referenced, unread lead; no separate claim of inspecting it is made.

**Second Chern forms.** Filippo Fagioli, *A note on Griffiths' conjecture
about the positivity of Chern–Weil forms*, Differential Geometry and
Applications 81 (2022), 101848,
[author postprint](https://iris.uniroma1.it/retrieve/e383532e-6556-15e8-e053-a505fe0a3de9/Fagioli_postprint_A-note-on-Griffiths%27-conjecture_2022.pdf),
Section 2, Lemma 2.1/Theorem 2.2 and proofs, PDF pp. 10–12.
Theorem 2.2 makes c_2(E,h) a positive (2,2)-form when (E,h) is Griffiths
semipositive, in arbitrary rank. The proof retains that hypothesis in
each two-by-two principal curvature block and in the semipositive limit.
It does not establish it from hyperholomorphicity. The later rank-three
c_1 c_2-c_3 result has both different rank and extra positivity hypotheses;
it is not an inequality for the present rank-two F.

**Squaring positive forms.** Following Fagioli's relevant reference,
read Błocki–Pliś, *Squares of positive (p,p)-forms*, C. R. Acad. Sci.
Paris, Ser. I 351 (2013), 27–32,
[published PDF](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2013.01.009.pdf),
Theorem 1, p. 27, and Sections 2–3, pp. 28–30. A positive (2,2)-form
has positive square; their convention permits nonnegativity. The proof
reduces to dimension four, then to positivity of a Hermitian matrix on
the Plücker quadric. Theorem 2 shows failure in degrees p>=3. This
provides an exact squaring result, but requires positivity of its input
form. No inspected source proves that input for L071's Chern form, so
no such specialization is imported.

**Quaternionic positivity.** Verbitsky, *Positive forms on hyperkähler
manifolds*, [arXiv:0801.1899](https://arxiv.org/pdf/0801.1899#page=22),
inspected PDF footer version 1.0, 12 January 2008, Section 4.3,
Proposition 4.10, PDF pp. 22–24. On an SL(n,H)-manifold with a nowhere
vanishing real positive holomorphic top form, the map defined by (4.7)
transfers quaternionic-positive forms to ordinary positive forms with
its stated phase convention, and intertwines the relevant differentials.
Read the positivity test against generators of the strongly positive
cone. This is a transfer theorem with a positive input, not positivity
of arbitrary invariant characteristic forms. It permits a hyperkähler
product; irreducibility is not its obstruction. No characteristic-form
identification or normalization is applied here.

**Tangent characteristic numbers.** Hitchin–Sawon, *Curvature and
characteristic numbers of hyperkähler manifolds*,
[arXiv:math/9908114v1](https://arxiv.org/pdf/math/9908114v1#page=15),
Theorem 3, PDF p. 15, and Sections 3/6, PDF pp. 7–9/15–16.
For compact irreducible hyperkähler M of real dimension 4k, the formula
identifies the Riemann-curvature norm expression
||R||^(2k)/((192 pi^2 k)^k vol(M)^(k-1)) with sqrt(A-hat)[M].
Here ||R|| is the L2 norm. Section 2 defines irreducibility by holonomy
Sp(k). Proposition 1's one-dimensional even holomorphic-form spaces
are used in Section 3. These are tangent-bundle characteristic numbers,
not those of an arbitrary coefficient bundle. Both that distinction
and irreducibility prevent the proposed import to F on S x S.

## Reuse, duplicates and limits

Reuse the unchanged
[fixed-lower-Chern assessment](2026-10-04-fixed-lower-chern-stability-test.md)
and [hyperholomorphic representative assessment](2026-09-27-hyperholomorphic-cubic-rm-representatives.md).
Read L071's actual hypotheses, full character and connection passage;
L044's exact h and full self-adjoint D remain the metric/tensor inputs.
No rational NS/T integral splitting or new curvature-sign hypothesis is
assumed. L045/ATTEMPTS/034 concern a different fixed virtual K-class.
ATTEMPTS/075 and 076 retain the Kähler charge stop and all-minus Spin(7)
equation mismatch. None is recomputed or reversed by this review.

Searches included `hyperholomorphic bundles higher Chern classes positivity
second Chern square inequality`, `Hermitian Einstein bundle fourth Chern
character positivity hyperkahler rank two`, `"hyperholomorphic" "Chern"
"positivity"`, `"hyperholomorphic" "higher Chern"`, `"hyperholomorphic"
"Chern character" "positive"`, `"hyperholomorphic" "fourth" Chern
positivity`, `hyperkahler bundle Chern numbers inequality Rozansky Witten
bundle Sawon`, and `"quaternionic instantons" "Pontryagin" inequality`.
Searches for squares of positive forms followed the primary reference.
These searches found no applicable theorem, not evidence of novelty.

Sawon's bundle-decorated Rozansky–Witten papers and Gerasimov–Kotov's
fourth-order transgression paper were search-only leads, not inspected
positivity theorems. Transgression order alone supplies no claimed sign.
The first Numdam access timed out; the full published Błocki–Pliś PDF
was then accessible, so that access issue is resolved. There is no
persistent essential access blocker for the comparisons made here.
This review does not claim exhaustive coverage of possible quartic
identities, higher Yang–Mills equations, or arbitrary new mechanisms.

## Continuation boundary and Mathlib

Reopen this positivity route only for a specific additional applicable
primary theorem or a separately assessed independently discriminating
constraint. No new mathematical result is derived or imported into the
argument, so lemmas/, mathematical scripts/, PROOF.md and DAG.md remain
unchanged. Mathlib coverage of these positivity results was not checked;
no absence claim is made. References here document a source comparison,
not newly established lemma nodes.

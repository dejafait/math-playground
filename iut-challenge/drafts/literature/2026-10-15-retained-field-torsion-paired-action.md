# Retained local field with torsion — completed source comparison

TARGET: Assess whether the cited paired reference automorphisms admit an integral logarithmic action on the retained N=Q_3(zeta_420,3^(1/7)), with its 3-primary unit torsion retained.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the earlier reference-transport and even-degree assessments; narrowly checked L023,L024,L032, L042,L045,L048 and ATTEMPTS/015,016,019,020,024. Fresh queries were `"Hoshi" "Nishio" "torsion" logarithm automorphism`, `"Kondo" "Jannsen" "principal units" automorphisms trace`, and `"Q_3" "zeta_420" automorphisms logarithm`; no exact-field integral action theorem was located. Primary passages below, rather than unsuccessful searches, support approval.
SOURCE_EVIDENCE: Hoshi, Introduction to Mono-anabelian Geometry, PMB 2021, DOI 10.5802/pmb.42, Lemma 1.2(i,ii,iv,v), p.11, Proposition 3.11(i,iv), p.22, Proposition 4.2(i,iii), pp.25–26, Definitions 5.1–5.5, pp.29–30, and Theorem 7.6(i,ii) with proof, pp.39–40, https://www.numdam.org/item/10.5802/pmb.42.pdf; Hoshi–Nishio, June 2022 revised RIMS1931, section 1 and Lemma 1.3 with proof, PDF pp.3–5, Lemma 2.3(ii) with logarithm diagram, pp.7–8, https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf; Kondo, arXiv:2512.09231v2, 12 December 2025, section 1, Theorem 1.1, reciprocal setup and displayed paired families in Theorem 1.3's proof, https://arxiv.org/html/2512.09231v2#S1.
COMPARISON: The general reconstruction/lifting statements allow unit torsion; Hoshi–Nishio explicitly uses the torsion-free quotient before rationalization. Kondo supplies actual paired automorphisms for odd residue characteristic without a torsion-free-unit hypothesis. L024/L032's integral basis arguments require an extra hypothesis unavailable here and cannot be transferred. Integral preservation of the genuine logarithm image can instead be tested through the compatible unit/logarithm diagrams, without an index-one presentation basis.
GAP: Write the retained-field specialization with one consistent reciprocity reference, retaining torsion in the multiplicative pair and quotienting it only for logarithms; check both the action and its inverse on J=log(O_N^times). No integral presentation basis, residual irreducibility, field coordinates or numerical orbit bound is covered.
REASON: Essential changed-hypothesis coverage is now inspected and sufficient for a bounded known-method specialization; no new action theorem for N is derived in this literature turn. A reproof of presentation or reconstruction is unnecessary.
LITERATURE_REASON: N contains the primitive third root already supplied by L042, whereas the earlier integral-basis proofs exclude it; the previously uninspected torsion-quotient passages and full-pair hypotheses were essential to this changed target.
SCOPE: The exact TARGET, restricted to Kondo's displayed paired/adjacent subgroup for one admitted presentation, its reciprocity-defined full-model MLF×-pair reference lifts, and logarithmic preservation of J and I=J/6. No transfer of L024/L032's bases, quotient irreducibility, radius, actual native permitted-action identification or input membership is approved.

## Source findings and qualifications

[Hoshi's published text](https://www.numdam.org/item/10.5802/pmb.42.pdf)
allows a finite p-primary torsion summand in the unit decomposition
(Lemma 1.2(i)); (v) identifies the logarithm kernel with roots of unity.
Propositions 3.11 and 4.2 compare fixed-field and algebraic-closure
units using reciprocity and transfer. Definitions 5.1–5.3 keep the full
algebraic-closure unit monoid in the model MLF×-pair. Theorem 7.6
allows arbitrary such pairs: its proof constructs lifts through
reconstructed pairs and identifies the difference between lifts through
the identity-Galois fiber. The ambiguity is profinite-unit exponentiation
(Definition 5.5 and Remark 5.5.1). None imposes torsion-free units.

[Hoshi–Nishio's June 2022 text](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf)
defines rationalization using principal units. Lemma 1.3's proof first
uses all generator images, including x_0, in the torsion-free quotient.
It eliminates x_0 only after rationalization using a nonzero integer
coefficient; it does not assert that this coefficient is a p-adic unit.
The conclusion is a rational basis, not a full integral basis.
Lemma 2.3(ii)'s proof explicitly compares the reconstructed unit and
additive actions through logarithm. These passages have no hypothesis
excluding p-primary unit torsion. Their Proposition 1.1 uses different
presentation parameters and must not replace Kondo's admitted relator.

[Kondo's versioned primary text](https://arxiv.org/html/2512.09231v2#S1)
assumes odd residue characteristic for Theorem 1.1; its full presentation
includes normal wild generation and the parity-dependent relation.
The reciprocal setup is rational. Theorem 1.3's proof displays the
paired and adjacent automorphisms, fixing x_0,x_1,x_2 in even degree.
The existence statements and all changed generator words were inspected
directly; the prior even-degree trace-proof assessment is reused.
No unit-torsion exclusion occurs in these hypotheses. Its stronger
Hodge–Tate representation results are not needed here.

Versions and page conventions: Hoshi's PDF cover says 2021, pp.5–44;
PDF page 8 is printed p.11, page 19 is p.22, pages 22–23 are pp.25–26,
and pages 36–37 are pp.39–40. Hoshi–Nishio's cover explicitly says
June 2022; locators above are PDF page numbers. Kondo's current reading
is the versioned HTML, not a claimed fresh reading of RIMS1991's PDF.
The earlier RIMS1991 printed locators are pp.8–11. Fresh text extraction
of both other primary PDFs succeeded this turn; historical access
failures are not a present blocker. Screenshot calls returned locators
without visible page images, so no visual verification is credited.

## Applicability boundary and duplicate/failure check

L042 supplies the exact retained field, degree 168, ramification index
14, residue degree 12, and a primitive third root. L045/L048 retain
that embedded N for the same changed curve and global construction.
Thus the source conditions to compare are p=3 and the even-degree
case, not the old degree-27 or degree-108 fields. No absolute-abelian
or prescribed-coordinate hypothesis is needed for the selected source
statements. This is a hypothesis comparison, not an integral action
proof for N. The exact size of its p-primary torsion is not required
by these general statements and is not calculated here.

L023's compatible-choice method is reusable; its sign-only all-unit
argument is not. L024 and L032 prove their integral bases using absence
of 3-primary torsion. Preserve them for their original fields, but do
not infer here that the full abelian pro-3 quotient is torsion-free,
that a relator coefficient is a unit, or that y_1,...,y_168 is an
integral basis. Keeping all source-generator images in the logarithm
module avoids that extra question for this target.

The inspected failures are different: ATTEMPTS/015–016 exclude the
old compact involution, /019 stops an unsupported universal field-line
restriction, /020 stops prescribed reciprocal coordinates, and /024
stops whole-kernel irreducibility for the old paired subgroup. None
proves absence of reference lifts for N; none supplies an escaping
point for this field. No duplicate retained-N action proof was found
in the targeted records. This search establishes no novelty.

## One bounded next mathematical step

The main gap remains original finite B>=A. The intermediate target is
a compatible integral logarithmic reference action on this retained N.
Its plausible downstream use is an action test on the local field
already present in the global construction, rather than transferring
a counterexample from fields excluded by the torsion prerequisites.

After approval, import the named source results and write only their
necessary specialization. Use the same fixed-field reciprocity map
and its algebraic-closure extension when comparing the reference lift
with the additive action. Retain the finite torsion subgroup in units;
check that passage through the logarithm quotient is well-defined,
including continuity and inverses. Distinguish the image J from the
source's shell I=J/6: a diagram whose codomain is I need not be
surjective from units. Do not identify a rational presentation basis
with a Z_3-basis. No relator-index calculation is necessary for this
bounded preservation test.

Continue only if this consistent-choice comparison establishes an
invertible Z_3-linear action on the genuine J, compatible with a
full-pair reference lift and with the retained torsion quotient. If
it fails, identify the exact incompatible arrow or missing hypothesis
and stop dependent numerical work. No convenient basis replacement,
extra generator or field enlargement repairs a failure within this
target. The source proof, not an independent reproof of its general
theorems, supplies the known inputs. The specialization remains future
mathematical work, expected classification REPRODUCTION.

Essential local inputs are L042,L045,L048; L023,L024,L032 are narrowly
used compatibility methods and contrasts, not transferred field
conclusions. Keep L062 and all E_0,F,K_glob,Omega,u,w,H,N,q_0 and
the marked cover/log data unchanged. Native field/rho conditions remain
conditional. Actual permitted action, input and pilot membership,
normalization, essentiality and original finite B>=A remain separate.
Full matching and supporting Mathlib coverage: **not checked**.
No lemma, mathematical script, PROOF argument or DAG row is changed.

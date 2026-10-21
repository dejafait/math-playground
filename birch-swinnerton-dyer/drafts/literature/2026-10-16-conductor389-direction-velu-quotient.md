# Direction-field degree-seven quotient — source comparison

TARGET: Assess a degree-seven Vélu quotient over L070's direction field, using its full kernel cubic, as an alternative to the two stopped incidence presentations.
CHECKED: 2026-10-16
DECISION: IMPORT
SEARCH_EVIDENCE: Searched “Vélu Isogénies entre courbes elliptiques 1971 translation finite subgroup rational field” and “Kohel 1996 isogenies kernel polynomial odd degree formulas thesis”; inspected the formulas and algorithm below. Scoped local comparison covered L067/L068/L070, L046's import paragraph, the degree-five and seven-incidence assessments, and ATTEMPTS/035--036; no matching fixed direction-field quotient certificate was found in those paths, and novelty is not inferred.
SOURCE_EVIDENCE: Vélu (1971) §§2--3 equations (7)--(13), Remarks 2--3, Ghitza translation pp.2--4; Sutherland MIT 18.783 Fall 2025 Lecture 5 Theorem 5.11 with proof pp.5--6, Theorem 5.15/Remarks 5.16--5.17 pp.7--8; Shumow (2009) §3.1 kernel-polynomial definition p.30, Theorem 3.2.1 with complete proof pp.54--56, §3.2 algorithm/Corollary 3.2.2 pp.57--59; Sage official EllipticCurveIsogeny input contract and characteristic-zero/number-field examples, retrieved 2026-10-16. Direct sources: https://aghitza.github.io/publications/translation-velu.pdf ; https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf ; https://www.sagemath.org/files/thesis/shumow-thesis-2009.pdf .
COMPARISON: A separable Galois-stable subgroup suffices; pointwise-rational kernel points are unnecessary. Known odd-degree and kernel-polynomial formulas cover the quotient and both coordinates over the subgroup's field of definition. L070 supplies the full cubic for the universal direction over its degree-eight field. The remaining difference is exact fixed-instance evidence and replay, not a new quotient theorem or a completed incidence construction.
GAP: No quotient coefficients, maps, full denominator/exceptional-point witnesses or bounded execution evidence have been produced. A later affine-line/dual-kernel identification, rational transports, incidence and norm remain separate obligations.
REASON: Essential relative-field descent and formula coverage now matches the audited inputs; a bounded known-algorithm specialization can replace the two stopped column presentations without reopening either. No lemma or mathematical script was written in this literature turn.
LITERATURE_REASON: At invocation start this target was REVIEW_REQUIRED: non-pointwise-rational kernel descent and a cubic-input construction over the direction field were outside the earlier degree-five and incidence assessments.
SCOPE: Source comparison for the saved TARGET and preparation of separate fixed quotient construction coverage; no new instance, isogeny theorem, dual/affine-line equality or arithmetic descent conclusion.

## Relevance and audited inputs

The main gap remains rank E(Q)=ord at one for arbitrary curves of analytic
order at least two. The intermediate target is the exact degree-seven
quotient for L067's fixed short curve Y²=X³−3024X+46224 over D=Q[Z]/h
from audited L070. Its plausible use is a later alternative presentation
of affine-line data for L066's full-descent enclosure. Quotient construction
alone gives neither that presentation nor an arithmetic enclosure.

L070 identifies D with the whole scalar-fixed direction algebra and proves
that it is a field. Its mixed inverse and separate audit give the full
cubic q(U,z)=(U−X)(U−[2]*X)(U−[3]*X), retaining all three inverse pairs.
The complete value `/cubic` of
`scripts/seven-torsion/compressed-249/direction.json` was inspected with
the shared JSON inspector's `--full` option: four ascending-U coefficient
arrays, each in ascending Z powers. No coefficient was recalculated or
verified by that inspection; correctness is imported from audited L070,
not inferred from a preview. L067/L068 retain both signs, exact order seven
and the geometric forward action. L069 and unfinished columns are excluded.

The direction interpretation supplies the Galois-stable subgroup over D;
it does not supply a D-rational generator. L067 gives nonsingularity.
Characteristic zero meets separability and short-model restrictions.
The cubic uses L067's short X-coordinate, not the original long x-coordinate;
its supplied change X=36x+12, Y=216y+108 and inverse must accompany any
later transport.

## Primary quotient and descent coverage

[Jacques Vélu, *Isogénies entre courbes elliptiques*, C. R. Acad. Sci.
Paris Sér. A 273 (1971), A238--A241, Ghitza translation](https://aghitza.github.io/publications/translation-velu.pdf),
§§2--3 pp.2--4, gives coordinate sums (7), formulas (8)--(11) and
local-parameter computations (12)--(13). Equation (7) sums all nonidentity
points; (8)--(11) use one representative per inverse pair plus all order-two
points. Remark 2 fixes differential normalization. Remark 3 descends curve
and map for a separable subgroup stable under conjugation. These are
imported inputs; no general reproof is needed. Here no nonidentity
order-two points occur. Coordinate denominators are rational functions,
not units at the kernel; exceptional points require the projective quotient,
not substitution into fractions with zero denominator.

[Andrew Sutherland, MIT 18.783 Fall 2025 Lecture 5](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf),
Theorem 5.11 and proof pp.5--6, distinguishes subgroup stability from
pointwise rationality. The proof uses the invariant function field,
translation cosets, smooth projective quotient and Hurwitz; the kernel
is the specified subgroup. This covers descent to D without splitting
the kernel. Theorem 5.15 and Remarks 5.16--5.17 pp.7--8 give the
odd-order short-model map (r(X),r'(X)Y), target coefficients and paired
summation convention. Their sums use all six nonzero points, or twice
a sum over three inverse pairs. These conventions must agree in replay.
An arbitrary cubic division-polynomial factor cannot replace L070's
geometric subgroup identification.

## Kernel-polynomial algorithm and qualifications

[Daniel Shumow, *Isogenies of Elliptic Curves: A Computational Approach*,
University of Washington MSc thesis (2009)](https://www.sagemath.org/files/thesis/shumow-thesis-2009.pdf),
§3.1 p.30 defines the monic kernel polynomial by distinct finite
x-coordinates. Theorem 3.2.1 pp.54--56 gives both maps and target on
a short equation. Its full proof separates order-two and paired points,
uses logarithmic differentiation, then symmetric coefficient sums.
It assumes the kernel of an existing separable normalized isogeny:
existence here comes from the quotient theorem and L070, not formula
substitution. The coordinate-change algorithm pp.57--59 was also read;
it is unnecessary if the construction stays on L067's short model.

Use this algorithm checked against Vélu, not a blanket endorsement of
the thesis. The retrieved text repeats an exponent in the coefficient
pattern for D(X), and a proof line omits the initial X before a sum;
retain coefficients by degree and the original Vélu normalization.
No correction is derived here. Future replay must check equation,
degree and differential independently. Normalization alone is not used
to claim uniqueness among arbitrary translated Weierstrass models.

[Sage's official isogeny documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_curve_isogeny.html),
`EllipticCurveIsogeny` input contract and characteristic-zero/number-field
examples, documents a monic kernel-polynomial route and both maps;
the cyclic restriction is compatible with order seven. This is known
software overlap, not evidence that the fixed D-instance was run.
No version-independent runtime guarantee is imported. Kohel's 1996
thesis remains an unread bibliographic lead, not a theorem premise.
Full matching Mathlib coverage is not checked.

## Limits and continuation decision

ATTEMPTS/035--036 stop particular translation/relation columns.
A cubic-input quotient is a different mechanism, but source operation
counts do not certify rational coefficient cost. Preserve the stops and
original evidence. The bounded construction contract is in
`drafts/literature/2026-10-16-conductor389-direction-quotient-construction.md`.
That newly written ready continuation receives the supervisor's separate
next-turn approval. No quotient was constructed in this literature step.

This review does not identify a quotient image with Schaefer--Stoll's
ordinary linear dual. Lemma 7.5 and Proposition 7.10, reused through the
inspected seven-incidence assessment, still require the correct Galois
action and cyclotomic twist. Zero/kernel components, signs and all
rational transports remain future obligations. No dual-isogeny or
affine-line assertion is essential to the first quotient target, and
none is established here.

Success would still leave incidence/norm, global functions and complete
units/classes, local identifications/bounds, Selmer containment, L026
premises, successful localization, rational membership, divisible Sha
and arbitrary-curve comparison open. Continue only if the fixed quotient
admits complete exact replay within declared bounds; abandon this
representation upon a failed source hypothesis or bounded construction
failure. No BSD candidate is asserted.

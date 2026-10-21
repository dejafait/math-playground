# Actual-line projected-container invariance — completed source comparison

TARGET: Determine whether the specified paired reference subgroup preserves q(C) in V/(Q_3 y_1), using L033 and audited L034.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October 6 paired-container and October 8 quotient/projected-container assessments; checked L025's homothety proof, L032/L033 hypotheses, L034 conclusion, history/092–099 and ATTEMPTS/022–024. Fresh searches for stable lattices/residual irreducibility/homothety and Sehanobish Corollary 3.1.9 located the existing criterion and broader stable-lattice literature, with no inspected exact-field invariance theorem.
SOURCE_EVIDENCE: Freshly inspected Sehanobish, Universal Deformations and p-adic L-functions (Maryland PhD, 2019), section 3.1, printed pp. 26–28 (PDF pp. 34–36), Definitions 3.1.1 and Corollary 3.1.9/complete proof sketch, https://api.drum.lib.umd.edu/server/api/core/bitstreams/9c358dab-b72f-47fa-924c-da55d0ae1ea6/content; Stacks Lemma 10.20.1, tag 00DV, statement (2),(4),(6) and relevant proof, https://stacks.math.columbia.edu/tag/00DV. Reuse inspected quotient-lattice inputs and Kondo reference-action coverage with exact locators below.
COMPARISON: The known stable-lattice criterion covers the scalar field Q_3 and rank 106 without absolute residual irreducibility or a larger symplectic-image hypothesis. L033 supplies the exact integral residual action; L034 supplies the same-space projected homothety exclusion. The remaining task is their qualitative application to the actual line and full projected lattices, with the inherited proof-sketch qualification retained.
GAP: Write the actual-line quotient identification, full/closed lattice and compact-closure checks, the known same-space homothety argument, and the resulting precise preservation verdict in a separate research turn. No verdict or new lemma is derived here.
REASON: Essential coverage now suffices for this unchanged bounded target; the exact quotient-action comparison is newly completed. A short known-method reproduction is warranted because the cited sketch does not establish same-space homothety by its final isomorphism sentence.
SCOPE: Only the specified finite-word subgroup and its induced action on V/(Q_3 y_1), full lattices q(C) and q(M), actual-line integrality, compact closure if used, known homothety criterion and preservation/nonpreservation conclusion using L033/L034. No field-valuation descent, explicit escaping word, numerical bound or original-IUT realization.

## Primary criterion and retained qualification

[Arijit Sehanobish, *Universal Deformations and p-adic L-functions*,
Maryland PhD dissertation (2019)](https://api.drum.lib.umd.edu/server/api/core/bitstreams/9c358dab-b72f-47fa-924c-da55d0ae1ea6/content),
section 3.1, printed pp. 26–28, treats continuous representations of
compact Hausdorff profinite groups over a finite extension of Q_p.
Corollary 3.1.9 equates residual irreducibility and uniqueness of the
stable lattice up to homothety. Only the forward implication is needed.
The sketch normalizes an inclusion and examines its nonzero residual
image, but ends with a GL_2 matrix lift and an abstract isomorphism.
That ending does not establish same-space scalar equality in rank 106.
Serre's exercise 4, p. 3, cited there, remains unread.

The independent input is [Stacks Project, Lemma 10.20.1
(00DV)](https://stacks.math.columbia.edu/tag/00DV), especially (2)/(4):
the module must be finitely generated and the ideal contained in the
Jacobson radical. Reuse L025's already written normalized-inclusion
argument as a method, checking these obligations over Z_3 in the new
quotient. This is a justified reproduction of known mathematics, not
an uncovered new stable-lattice theorem. No proof is performed here.

## Exact applicability comparison for the next mathematical step

Use L031's genuine rank-108 J, L032's rank-107 M and actual primitive
fixed y_1, L033's free rank-106 Q=M/(Z_3 y_1) with irreducible Q/3Q,
and audited L034's all-lines exclusion. Put W=Q_3 y_1 and
q:V->V/W, with C=O_L intersect V, V=ker(Tr_(L/Q_3)),
L=Q_3(zeta_20,pi), pi^27=3, e=27,f=4. The scalar field of the
lattice theorems is Q_3, not L or its unramified subfield.

The next proof must identify q(M) with the integral Q using primitivity,
retain the actual fixed line when inducing the action, and check both
projected objects are full closed Z_3-lattices in the same quotient.
These obligations are within the reused source coverage: Bürgisser,
Kulkarni and Lerario, *Nonarchimedean integral geometry*, Selecta
Mathematica 32:10 (2026), version of record 5 January 2026,
section 2.2 pp. 13–14 and Lemmas 3.1.4(1–3)/3.1.5 pp. 21–23
([primary publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)). Their statements and
relevant proofs were inspected in
`drafts/2026-10-08-enlarged-projected-container-source-review.md`;
no fresh reading is claimed here. L034's conclusion already includes
the exact actual-line homothety comparison; no Smith recalculation is needed.

For the compact formulation, check the closure of the induced subgroup
in GL(q(M)) with its 3-adic topology and continuous rational action.
Under a putative preservation assumption, check stability of q(C)
extends to that closure using its closedness and inverses. Alternatively
reuse L025's direct finite-word proof, whose normalized-inclusion method
requires no compactness. In either formulation, equality of lattices
inside one rational space is required; an abstract module isomorphism
is insufficient. The later conclusion must distinguish preservation by
all finite words from an explicit generator or a prescribed input escape.

Kondo arXiv:2512.09231v2 (12 December 2025), section 1 Theorem 1.3,
printed pp. 9–11, supplies the paired/adjacent words through L032's
inspected reference transport. Reuse
`drafts/2026-10-08-enlarged-paired-quotient-source-review.md` for those
source qualifications; no new source automorphism or larger group is added.

## Duplicates, bounded test and route

L025 contains the analogous odd-degree method, not an enlarged-field
input theorem. L033 explicitly leaves stable-lattice conclusions open;
L034 explicitly leaves noninvariance open. The scoped October 8 audit
and history searches found no completed exact-target verdict. Fresh
queries were `"stable lattices" "irreducible" "homothety" compact
representation` and `"Sehanobish" "Corollary 3.1.9"`. Suh's stable-lattice
series and Garcia's thesis are unread leads beyond search metadata;
none supplies an imported theorem. No novelty follows from these searches.

Main gap: original finite B>=A. Intermediate target: qualitative
preservation of q(C) by the exact subgroup. Possible downstream use:
identify a source-action restriction or projected-container escape before
addressing fixed-line control and numerical or actual-input consequences.
Continue if the actual-line/full-lattice obligations permit the known
criterion to decide this target; abandon this homothety mechanism if an
essential obligation fails, naming it without enlarging the group.
Approval is SPECIALIZE, with REPRODUCTION for the later application;
this literature turn derives no preservation verdict.

Preserve ATTEMPTS/022–024: individual division-field exclusion, naive
O_U scalar-transport failure and whole-kernel reducibility are independent
recorded stops. No prescribed y_1, converse presentation realization,
extra shear, exponent twist, O_U-linearity or descended field valuation.
Fixed-line/numerical control, actual/native input/action compatibility,
packet/global realization, pilot transport, essentiality and finite B>=A
remain unresolved. Full matching and supporting Mathlib coverage:
**not checked**. Existing canonical lemmas retain their source records;
no lemma or mathematical script was changed in this literature-only step.

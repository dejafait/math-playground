# Retained container sharp orbit minimum — completed source comparison

TARGET: Determine the sharp field-valuation minimum of Gamma(C) for C=O_N intersect Q_3 W_J under the unchanged retained-field hypotheses, uniformly over admitted presentations.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three focused external queries and a scoped duplicate/failure comparison found general stable-lattice methods but no inspected theorem giving this exact retained-container minimum; reused the completed orbit-span and retained-field assessments and read the relevant L026/L038 method passages and audited L066. Queries and inspected scope are recorded below; no novelty inference is made.
SOURCE_EVIDENCE: Reinspected Brinon–Conrad (24 June 2009), Definition 1.2.5/Lemma 1.2.6 and complete proof, printed p.7, https://math.stanford.edu/~conrad/papers/notes.pdf ; Stacks Lemma 10.31.4(2) and proof, https://stacks.math.columbia.edu/tag/00FM , and Lemma 10.20.1(2),(4) and determinant/quotient proofs, https://stacks.math.columbia.edu/tag/00DV ; Ophir–Weiss arXiv:2401.10183v2 sections 2.1–2.2, Proposition 2.5 and complete short proof, https://arxiv.org/html/2401.10183v2 . Reuse Sehanobish, Hess–Pauli–Pohst and Burgisser–Kulkarni–Lerario through the ready assessments and audited L066, with exact locators and qualifications below.
COMPARISON: Known bounded ordinary-span, residual homothety, filtration rank-nullity and finite-sum ultrametric methods cover the proposed mechanism. L066 supplies complete retained-field bounds, not the requested orbit minimum. Earlier-field results provide method precedents only; building boundedness supplies neither an absolute scalar scale nor actual orbit attainment.
GAP: Specialize the methods to this actual C and E: determine the ordinary span's scalar level, prove the complete lowest field-valuation layer survives in E uniformly, and pass from a finite expression at the span minimum to an actual finite-word image. No span formula, numerical minimum or attainment is established in this review.
REASON: Essential source coverage is adequate for one bounded known-method specialization of the unchanged target; remaining work is mathematical applicability and sharpness, not an inaccessible source or a new general theorem.
LITERATURE_REASON: The prior ready L066 audit covered qualitative noninvariance only; the saved quantitative target changed the required conclusion to a sharp field minimum with finite-word attainment and therefore required this separate comparison.
SCOPE: Exactly TARGET for the actual rank-166 E=W_J and C=O_N intersect Q_3 E, under L063–L066's unchanged hypotheses; bounded ordinary orbit sums, same-space scalar normalization, complete valuation-layer restriction and actual finite-word attainment are covered. No changed input, enlarged group, extra shear, assigned coordinates, whole-kernel action, native-IUT identification or numerical IUT prescription is approved.

The main gap remains the original finite B>=A comparison, with actual
input/action realization, pilot transport and essentiality unproved.
The proposed intermediate target converts the verified qualitative
escape into a precise local benchmark for a later, separately screened
input/enclosure comparison. C itself is not asserted to be an actual
IUT input. No numerical threshold from IUT is assigned to it.

The continuation test is to establish a uniform sharp lower bound on
the field valuation of every h(c), and attainment by some actual
c in C and finite word h. An ordinary finite-sum orbit span is not
the orbit set. If bounds or attainment depend on unproved coordinates
or stronger action hypotheses, record that exact obstruction and
restrict or abandon the uniform claim; a nonsharp upper enclosure or
another qualitative escape does not answer the target. This document
neither derives an orbit span nor predicts a numerical minimum.

Essential inputs: L063,L064,L065 and the now audited L066; unchanged
L042,L045,L048 supply field/curve context. Retain N=Q_3(zeta_420,
3^(1/7)), degree 168,e=14,f=12; E=W_J, V=Q_3 E,
C=O_N intersect V, the full admitted presentation, single reciprocity
choice, all unit torsion before log and precisely the finite-word
subgroup with inverses. Retain E_0,F,K_glob,Omega,u,w,H,q_0,
v_3(q_0)=30,M>=max(M_tors,31),full 30-torsion, origins,U,
alpha,psi,gamma,0_B,Q,c and stable logs. The symbol c for a
container point is distinct from the retained cusp-label map c.
Native field/rho and independent initial data remain conditional.
No F_mod=Q,K_glob=N,q_0=3^30, assigned reciprocal coordinates,
torsion-free presentation basis or whole-kernel irreducibility is
assumed. ATTEMPTS/020,/024 remain preserved. Mathlib coverage for
the full target and supporting orbit-span results is not checked.

## Inspected methods and hypotheses

The completed comparison reuses
`2026-10-07-paired-envelope-orbit.md`,
`2026-10-10-unprojected-enlarged-envelope-field-minimum.md`, and
`2026-10-16-retained-paired-container-invariance.md` in this directory.
These cover the general methods, not this new quantitative conclusion.
The full L066 proof/audit, L064/L065 hypotheses and conclusions, L026's
finite-sum attainment passage, and L038's complete-layer/complement and
finite-sum attainment passages were inspected for the changed scope.
Their old field constants, trace conditions and fixed-line decompositions
are not inputs about N. No mathematical certificate was run or relied on.

**Ordinary orbit sums.** Brinon–Conrad, *CMI Summer School Notes on
p-adic Hodge Theory*, preliminary version **24 June 2009**, Definition
1.2.5 and Lemma 1.2.6, **printed p.7, PDF page index 6**
([primary notes](https://math.stanford.edu/~conrad/papers/notes.pdf)),
assume a continuous representation of a profinite group on a finite
dimensional Q_p-space. The proof constructs a stable lattice by taking
a finite sum over coset representatives of the starting lattice's open
stabilizer. Its displayed stabilizer line has Lambda in place of the
starting Lambda_0; the construction and conclusion specify Lambda_0.
This is a general-rank sum construction, not primitive-vector transitivity.
It gives no equality between an orbit set and its integral span.

For the present target prefer the previously assessed **bounded ordinary
sum** method. Gamma is the specified group of finite words, not an
unjustified profinite group. L065 supplies its preserved E and inverses.
The future proof must bound the sum inside a finite rational dilation
of E, check that it is full, and use
[Stacks Lemma 10.31.4(2)](https://stacks.math.columbia.edu/tag/00FM):
a submodule of a finite module over a Noetherian ring is finite. Its
proof uses finite presentation of the quotient. This applies over Z_3;
it licenses finite generation only after boundedness has been proved.
No continuity or compact-closure identification is needed for that route.

**Embedded homothety.** Reuse Sehanobish, *Universal Deformations and
p-adic L-functions*, Maryland PhD dissertation **2019**, section 3.1,
Corollary 3.1.9, **pp.26–28**
([primary dissertation](https://api.drum.lib.umd.edu/server/api/core/bitstreams/9c358dab-b72f-47fa-924c-da55d0ae1ea6/content)),
as assessed previously and applied in audited L066. Its formulation
concerns a continuous compact/profinite representation with an integral
stable lattice and irreducible residual representation. Preserve the
recorded qualification: an abstract-isomorphism sentence in its sketch
does not establish equality of embedded lattices. Reuse L066's
normalized-inclusion method with
[Stacks Lemma 10.20.1(2),(4), tag 00DV](https://stacks.math.columbia.edu/tag/00DV).
The statement and determinant/quotient proofs were reinspected. The
module must be finite and the ideal in the Jacobson radical; here the
intended scalar ring is Z_3 and the ideal is (3). The retained-field
application must check actual two-sided invariance, minimal normalization
and nonzero residual image. The scalar level is still to be determined
from the actual input C, not from abstract homothety alone. No new proof
of the general criterion is warranted.

**Complete local bounds and restriction.** Reuse Hess–Pauli–Pohst,
*Computing the Multiplicative Group of Residue Class Rings*, undated
**18-page author manuscript**, section 4, Lemma 4.1, **pp.7–9**, and
Proposition 5.1(i),(iii–iv), **pp.9–10**
([primary manuscript](https://page.math.tu-berlin.de/~kant/publications/papers/hepapo.pdf)),
through the retained-field assessment and audited L066. Successive unit
quotients and deep log/exp apply with p=3,e=14 and depth strictly
greater than e/(p-1). The easy-case unit-basis theorem does not apply
automatically when p-1 divides e. Primary unit torsion must remain
before logarithm; sampled generators or a shallow log/exp isomorphism
cannot substitute for complete coverage.

Reuse Bürgisser–Kulkarni–Lerario, *Nonarchimedean integral geometry*,
Selecta Mathematica **32:10 (2026)**, version of record **5 January 2026**,
Definition 3.1.1, Lemmas 3.1.4–3.1.5, **pp.21–23**, Propositions
4.1.1–4.1.2, **pp.35–36**
([publication](https://doi.org/10.1007/s00029-025-01120-y),
[PDF](https://d-nb.info/1395945926/34)), through the same assessment.
Scalar field Q_3, full Z_3-lattices, induced subspace norms and the
correct domain/target orientation are essential. Preserve the recorded
misnumbered minimax-reference qualification; the formula used is
Proposition 4.1.1. These are lattice-norm results, not a descended field
valuation on a quotient.

L066's existing proof supplies 3O subset J, J subset m^(-19), and
surjectivity onto the complete twelve-dimensional F_3 layer
m^(-19)/m^(-18), with all infinite tails controlled. It also supplies
ambient exponents a_i<=1, at least twenty-four positive a_i, the
codimension-two interlacing inequalities, at least twenty-two positive
restricted exponents, and J intersect V=E. These are already proved
inputs, not calculations made in this review. Their quantitative use
still requires checking the extreme relative factor in the correct
orientation and the image of the **actual** E in the complete lowest
field layer. Standard rank-nullity is the covered method for comparing
that image with the rank-two complement from L064. No retained-layer
dimension or sharp field minimum is derived here. In particular mixed
relative factors alone are not a calculation of the field valuation.

**Attainment.** The standard ultrametric inequality covers finite
integral sums. L026 and L038 provide checked local method precedents:
an ordinary finite expression of a span element at its established
minimum can force a summand at that minimum, provided all actual orbit
images have the matching lower bound and coefficients are integral.
For this target the expression must involve actual C-points and finite
words of Gamma. A closure limit, a projected point, an arbitrary E-point
without span membership, or an assumed orbit-set equality does not
meet those hypotheses. Import the elementary inequality; write only
the application needed to check this new input. No new general lemma
or reproof of the imported module theorems is needed.

## Stronger results, duplicates and failure comparison

Fresh queries were `"Q_3" "zeta_420" "orbit"`;
`p-adic irreducible residual representation lattice generated orbit bounded homothety Brinon Conrad`;
and `"p-adic" "logarithm" "lattice" "minimum" ramification`.
The results did not supply an inspected matching theorem for this C.
General p-adic Hodge-theory and orbit-method hits were not imported;
search snippets and unsuccessful exact searches establish no novelty.

Reinspected Ophir–Weiss, *Maximal stable lattices in representations over
discretely valued fields*, **arXiv:2401.10183v2**, sections **2.1–2.2**,
Proposition **2.5** and its complete short proof
([versioned primary text](https://arxiv.org/html/2401.10183v2#S2)).
It assumes a complete discretely valued scalar field, finite dimensional
representation and existence of a stable lattice. It relates rational
irreducibility to boundedness of the invariant building; its proof uses
the cited half-line criteria (and separates locally compact from general
fields). This is a comparison of homothety classes, with no absolute
normalization against O_N or minimum on a specified input orbit. It
does not close the scalar-scale or attainment obligations. No deeper
building theorem or its referenced proofs is needed or imported.

The scoped duplicate check covered the retained-container assessments
and histories 246–249: L066 is qualitative, and the quantitative target
first appears as its pending continuation. L026/L038 concern different
fields and inputs; their constants and decompositions do not transfer.
ATTEMPTS/020 still blocks assigning arbitrary reciprocal field coordinates;
ATTEMPTS/024 still blocks whole-kernel irreducibility transfer. Both
failure records were read. This proposed actual-E argument avoids those
premises without asserting either stopped mechanism is now valid.

The challenge's [official announcement](https://zen.ac.jp/news/0ul6zqed9-0)
was reinspected on **2026-10-16**: it is still dated **2023-07-07**;
the challenger-prize statement and judging/publication paragraphs agree
with `foundations/01-challenge-scope.md`. This is a source-version check,
not a mathematical correctness or essentiality certificate.

## Decision and bounded continuation

**SPECIALIZE** approves one subsequent mathematical attempt on the
unchanged TARGET. Known methods cover the general mechanism, while
the embedded span scale, complete-layer survival and finite-word
attainment for C remain unwritten. The later proof must use L063–L066
and the unchanged field context, supply the actual lower bound on every
orbit image, and establish sharpness for every admitted presentation.
If these inputs do not suffice, record the specific failed premise;
do not replace the requested minimum by another qualitative escape or
a nonsharp enclosure. A dependence on unproved complementary coordinates
requires restricting or abandoning the uniform claim. This review
does not assert an outcome for that test.

Full matching and supporting Mathlib coverage for this target remain
**not checked**. The older projection-theorem lookup concerns a different
mechanism and is not imported here. Unknown coverage is not absence.
This is local source-comparison work only, with no claim beyond the
checked literature, no new lemma or script, and no resolution of the
original finite B>=A, actual input/action, pilot or essentiality gaps.

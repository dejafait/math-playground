# Unprojected enlarged envelope field minimum — completed source comparison

TARGET: Determine the sharp field-valuation minimum of the unprojected Gamma(T), including finite-word attainment and dependence on the admitted presentation, using L031 and L033–L037.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-logarithm/orbit, Kondo/trace, stable-lattice and integral-projection queries found no inspected theorem giving this full-space minimum; compared primary statements and essential proof cases with L028, L031–L037 and ATTEMPTS/020,024. Queries, stronger-result limits and reuse are recorded below; failed searches establish no novelty.
SOURCE_EVIDENCE: Freshly inspected Kondo arXiv:2512.09231v2 (12 December 2025), section 1, Theorem 1.1/setup and Theorem 1.3, all paired/adjacent fixed-generator clauses and complete even-degree proof (RIMS1991 pp. 8–11), https://arxiv.org/html/2512.09231v2#S1; Stacks Lemma 10.31.4(2), tag 00FM, and Lemma 10.20.1(2),(4), tag 00DV, with relevant proofs; Mathlib Projection.lean at e6bbacd0e1b7307ff6e17da09cd2455f60804fa6, LinearMap.IsIdempotentElem.isCompl and supporting projection statements. Reuse Brinon–Conrad, lattice-interlacing and logarithm coverage with locators below.
COMPARISON: Sources cover the retained even-degree action and conditional integral idempotent splitting, bounded finite modules and residual lifting. L036 gives a projected finite-sum span and full input bound; L028 supplies a different-field splitting/attainment method. None computes the embedded full-space minimum here or eliminates actual fixed-line/complement tests; the older trace-based normalization cannot be applied to a line inside V.
GAP: Justify splitting of the ordinary unprojected orbit span for exactly Gamma, determine its embedded fixed and complementary contributions with the inherited field valuation, and prove sharpness by actual finite words; establish uniformity or retain rigorously justified admitted-presentation dependence.
REASON: Essential coverage now permits one bounded known-method specialization on the unchanged target in a separate research turn. Exact action and complete valuation-filtration checks are necessary differences, rather than reproofs of the cited source theorems; no minimum or splitting result is derived here.
LITERATURE_REASON: The saved full-space target was REVIEW_REQUIRED and outside earlier projected integer-dilation coverage; this completes its missing comparison while reusing adequate unchanged source assessments.
SCOPE: Exactly TARGET for genuine enlarged J, the actual admitted presentation and specified finite-word Gamma: conditional finite-source-word or integral group-algebra splitting, bounded ordinary orbit spans, embedded field-valuation filtration and rank tests, fixed/complementary contributions, presentation dependence and finite-word attainment. No chosen reciprocal coordinates, arbitrary presentation realization, O_U-linearity, quotient field valuation, larger group, extra shear or original-IUT realization.

## Proposed scope and relevance

Keep L=Q_3(zeta_20,pi), pi^27=3, v_3(3)=1,
J=log(O_L^times), V=ker(Tr_(L/Q_3)), M=J intersect V,
T=(pi J/6) intersect V and C=O_L intersect V. For each admitted
presentation keep its actual primitive y_1, W=Q_3 y_1 and exactly
the finite-word reference Gamma of L033. The minimum, if established,
is on nonzero elements h(t) of L, with t in T and h in Gamma;
zero is assigned valuation +infinity. Do not put a field valuation
on V/W or infer orbit-set equality from a finite-sum span.

The main gap remains original finite B>=A. This proposed intermediate
target would replace an auxiliary projected integer scale with an actual
field-valuation comparison and test the fixed-line limitation. It would
still not show that T is an actual IUT input or Gamma the relevant
native action. Actual/native compatibility, packet/global realization,
pilot transport and essentiality remain independent unresolved steps.

Essential local inputs are audited L031's full genuine logarithm basis
and analytic tails, L033's actual fixed line and quotient action,
L034's full trace lattices, L035's same-space quotient identification,
L036's complete input intersection and ordinary projected span, and
L037's audited projected threshold. Their existing certificates are
available for a later approved target; no new certificate inspection,
radius computation or fixed-line theorem is asserted here.

The proposed literature turn was to compare these exact hypotheses with
known bounds and the local earlier full-space method in L028, without
transferring that different field's constants or presentation structure.
L028 is a scoped lead, not an imported mathematical premise of this
proposal. Preserve ATTEMPTS/020 (unjustified reciprocal coordinates),
022–023 (packet/scalar-transport stops) and 024 (whole-kernel reducibility).

Continue only with a method that bounds every actual orbit point and
justifies any claimed attaining point using the specified finite words.
If a uniform minimum requires an unestablished restriction on the actual
fixed line, identify that restriction precisely and abandon the uniform
claim rather than choose line coordinates or enlarge Gamma. This is a
test specification, not a claim that such a restriction is needed or
that a particular minimum is correct. The completed comparison below
approves coverage only; it establishes no mathematical result.

## Completed theorem comparison, 2026-10-10

**Actual action.** Freshly read **Kaiji Kondo, Anabelian aspects of the
outer automorphism groups of the absolute Galois groups of
mixed-characteristic local fields**, **arXiv:2512.09231v2**, 12 December
2025, **section 1, Theorem 1.1/setup and Theorem 1.3**
([versioned primary text](https://arxiv.org/html/2512.09231v2#S1),
[RIMS1991 PDF locator](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1991.pdf),
printed pp. 8–11). Inspection included all paired/adjacent formulas and
fixed-generator clauses, all four even-degree propagation cases and the
concluding exceptional shear. The trace theorem requires odd p and d>=2;
paired constructions use d>=3 and adjacency d>=5. Here p=3,d=108
satisfy these, without a Galois-extension hypothesis. The paired families
fix x_1,x_2; the separate x_2 shear remains excluded. No stated theorem
computes this orbit minimum or prescribes logarithmic field coordinates.
Reuse L032's reference transport/integral normalization and L033's
audited action, rather than reconstructing the cited source theorems.

**Conditional integral splitting.** Inspected the primary Mathlib
**Projection.lean** at commit **e6bbacd0e1b7307ff6e17da09cd2455f60804fa6**,
**LinearMap.IsIdempotentElem.isCompl** and its supporting
**LinearMap.IsProj.isCompl**:
[pinned source](https://github.com/leanprover-community/mathlib4/blob/e6bbacd0e1b7307ff6e17da09cd2455f60804fa6/Mathlib/LinearAlgebra/Projection.lean),
[documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Projection.html#LinearMap.IsIdempotentElem.isCompl).
For a ring R and an R-module whose additive structure is a commutative
group, an idempotent linear endomorphism has complementary range and
kernel. The source reduces this to the projection theorem. Applying it
over Z_3 requires an endomorphism of the orbit module itself; a rational
vector-space projector alone does not suffice. L028's audited
disjoint-pair finite-word method is a lead, whose counterpart must be
verified on all 53 actual pairs and the fixed line. No new word is
multiplied and no splitting assertion is proved in this review.

**Finite modules.** Freshly read
[Stacks Lemma 10.31.4(2), tag 00FM](https://stacks.math.columbia.edu/tag/00FM)
and its proof via finite presentation of the quotient: submodules of
finite modules over a Noetherian ring are finite. First provide an
ambient bounded finite Z_3-module for the unprojected orbit sum.
Freshly read [Nakayama's lemma, Lemma 10.20.1(2),(4), tag 00DV](https://stacks.math.columbia.edu/tag/00DV),
including the determinant proof and quotient case. Finite generation
and the Jacobson-radical condition are essential; (3) is the radical
of Z_3. Reuse L035–L036's audited same-space residual argument only
on the actual rank-106 quotient. Neither citation gives full-M
irreducibility or a field extreme.

Reuse **Brinon–Conrad, CMI Summer School Notes on p-adic Hodge Theory**,
preliminary version 24 June 2009, **Definition 1.2.5/Lemma 1.2.6 and
proof**, printed p. 7 ([primary notes](https://math.stanford.edu/~conrad/papers/notes.pdf)),
as inspected in `2026-10-08-enlarged-projected-envelope-orbit-span.md`.
Its continuous profinite finite-dimensional representation theorem
constructs a stable lattice using compactness and an open stabilizer.
It does not identify closure points with algebraic finite words or
determine a field radius. Prefer the already assessed bounded ordinary sum.

**Field-valuation difference.** Reuse L031's complete genuine basis and
inherited field-coordinate valuation formula, L034's complete M, and
L036's established T subset 3^(-4)M and projected ordinary span.
No new certificate was inspected or run. L028's fixed-line normalization
uses nonzero trace, whereas current y_1 lies in V by L032. Its trace
projection formula and numerical constants therefore do not transfer.

The standard **ultrametric inequality** and **rank-nullity theorem**
cover finite integral sums and finite-dimensional filtration tests.
The later proof must compute the complete relevant valuation layer in
the genuine M and check the scalar and integrality hypotheses; it may
not assume the smallest field valuation survives deleting a line.
For each admitted presentation, L033's actual integral complement may
be tested, without replacing it by a chosen conveniently valued one.
A uniform proof must control every admitted complement, or prove a
sufficient filtration-rank statement covering them all. No such claim
is derived here. A sharp expression in actual presentation data is an
acceptable intermediate outcome only with its dependence and remaining
uniformity limitation stated precisely.

For attainment, reuse the audited L028/L037 finite-sum-to-orbit method
with the ultrametric inequality. Its application requires an attained
minimum on the new ordinary unprojected span and a finite decomposition
using actual h(t), h in Gamma, t in T, with coefficients in Z_3.
A closure approximation, projected witness, complement point or
orbit-set equality cannot replace that check. No attaining image is
asserted in this source review.

Reuse **Bürgisser–Kulkarni–Lerario, Nonarchimedean integral geometry**,
Selecta Mathematica **32:10 (2026)**, version of record 5 January 2026,
**section 2.2**, pp. 13–14, **Lemmas 3.1.4/3.1.5**, pp. 21–23,
**Propositions 4.1.1/4.1.2**, pp. 35–36
([publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)), through the prior lattice
assessments. Their comparison concerns lattice norms over a fixed scalar
field, not automatically the inherited fractional field valuation on L.
No new minimax application to that norm is approved without checking
its norm hypotheses. Retain the recorded minimax cross-reference
qualification and quotient-only scope; no field valuation is put on V/W.

## Discovery, duplicates and bounded continuation

Queries actually submitted: `"Kondo" "trace" "2512.09231" automorphism`;
`"p-adic" "orbit" "lattice" "fixed" valuation invariant lattice irreducible`;
`"integral representation" "central idempotent" lattice fixed submodule irreducible quotient`;
`"logarithm lattice" "orbit" valuation fixed line`;
`"Kondo" "trace" "lattice" automorphisms local fields`;
`"stable lattices" "residually irreducible" homothetic`;
`"logarithm lattice" "field" "orbit"`;
`"nonarchimedean" "norm" "subspace" "interlacing" singular values`;
`"integral" "lattice" "involution" "idempotent" "2"`.
Results included existing primary Kondo/integral-geometry sources,
general representation/stable-lattice material and unrelated physics
and residuated-lattice hits. No inspected exact matching theorem was
found. Nonprimary summaries and unread leads are not imported; failed
searches do not certify originality.

Reuse the stronger-result comparisons already inspected in
`2026-10-07-paired-full-literal-orbit.md` and
`2026-10-08-enlarged-projected-envelope-orbit-span.md`:
Ophir–Weiss arXiv:2401.10183v2 **section 2.2, Proposition 2.5** concerns
bounded invariant homothety classes under irreducibility; Sjöstrand
arXiv:2312.03933v1 **Theorem 1.1** uses a different field-coefficient
transvection group. Neither assessed statement determines this embedded
extreme for exactly Gamma. No fresh reading or group identification is claimed.

The scoped screen compared L028's different-field full literal result,
L031's basis, L032–L033's fixed-line action and L034–L037's trace and
projected results. None records this completed unprojected minimum.
ATTEMPTS/020 and /024 were read narrowly; prescribed coordinates and
whole-kernel irreducibility remain stopped. ATTEMPTS/022–023's packet
and scalar-transport stops stay recorded and are not reopened.

Decision **SPECIALIZE** covers the unchanged TARGET for a separate
bounded research invocation, subject to supervisor approval. Recommended
research classification: **REPRODUCTION**, with no originality claim.
Continue if integral splitting and complete valuation-layer tests yield
an attained sharp minimum or sharp justified presentation dependence.
Abandon a uniform claim requiring chosen coordinates, a quotient field
valuation, an enlarged action or an unproved restriction on y_1.
This auxiliary test leaves original finite B>=A, actual/native input
and action, packet/global realization, pilot transport and essentiality
unresolved. The independent actual/native source blocker remains parked.

Mathlib: supporting integral idempotent splitting is present and its
pinned primary source was inspected. Full matching unprojected-minimum
coverage and other supporting action, local-field and filtration
coverage are **not checked**, not asserted absent. This literature-only
turn produces no new theorem, minimum, word or mathematical certificate.

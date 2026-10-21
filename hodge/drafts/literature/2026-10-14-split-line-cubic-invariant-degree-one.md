# Higher-jet degree selection — source comparison

TARGET: Test whether prescribing a cubic leading invariant yields an L101 convergent slice family with the unchanged first jet and generic classifying degree one.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused split-line first-jet, punctured-stability, finite-degree and A1 assessments; narrowly checked L094/L101/L103/L104, working audit notes, histories 266/270/276/278/280/282 and ATTEMPTS/061. Focused external searches located equivariant-formality and analytic quadratic-chart results, but no inspected theorem gives the exact prescribed-first-jet degree-one family; queries and inspected cases are below.
SOURCE_EVIDENCE: Newly inspected BMM 1902.06486v3 Definition 4.19, Theorem 4.20, Remark 4.21 and Lemma 4.22 with complete proof, pp. 16–18; focused rechecks of BMM 1907.10690v2 Definition 2.2/(2.3)–(2.4), pp. 4–5, Theorems 2.3/5.1, pp. 5–6/15, and Buchdahl–Schumacher (2022) Lemma 2.5, Proposition 2.6, Remarks 1/3 and (2.4), pp. 83–85. Reuse Artin (1968) (1.2) through inspected Rond (2018) Theorem 2.1, p. 122, and previously inspected proof reductions pp. 123–126. Compared Arbarello–Saccà (2018) Proposition 4.4 and essential proof cases, pp. 669–672; its algebraic slice is not assumed to be the fixed harmonic slice.
COMPARISON: Known tools cover normalized formal transfer, equivariant formal comparison under explicit semisimplicity hypotheses, complete fixed-metric analytic equations and approximation to arbitrary finite order. L104 supplies the conditional sign-quotient structure. None supplies compatible higher data, its actual harmonic second jet or the requested cubic/degree conclusion without a specialization.
GAP: Construct and check compatible formal higher data with the unchanged first jet; compute its second jet after transfer and determinant-one slice gauge; retain enough of that jet analytically; then test an actual invariant with zero quadratic and nonzero cubic leading term against L104. No construction or degree criterion is proved here.
REASON: Essential coverage now permits one bounded mathematical attempt on the unchanged target. Import the general results and prove only the explicit compatibility, jet and ordinary-image specialization; identity on cohomology does not license arbitrary second-jet preservation.
LITERATURE_REASON: The saved REVIEW_REQUIRED action changed first-jet realization and conditional A1 auditing to higher-jet degree selection; formal-transfer and arbitrary-order approximation coverage required this focused comparison.
SCOPE: Fixed audited L094/L101/L102/L103/L104 data S,I,g,h,k,E and exact prescribed first differential; one complex local higher-jet test in the complete determinant-fixed harmonic slice and its ordinary reduced analytic GIT image. No arbitrary second-jet prescription, analytic equivariant quadratic chart, quaternionic or global family is assumed.

## Relevance, reuse and threshold

Universal primitive rational Hodge realization remains the main gap.
This intermediate target asks whether there exists a choice among L101
families with the same prescribed first differential and marked data,
rather than deforming the particular family in L104. Its plausible use
is generic local separation before quaternionic or global realization.

Reuse the [first-jet audit assessment](2026-10-14-split-line-complex-first-jet-critical-audit.md),
[punctured-stability assessment](2026-10-14-split-line-punctured-stability.md),
[finite-degree assessment](2026-10-14-split-line-local-classifying-degree.md)
and [A1 audit assessment](2026-10-14-split-line-degree-two-a1-critical-audit.md).
Their previously inspected theorem/proof coverage is retained. L103
already allows arbitrary convergent higher coefficients with the given
first jet. L102's radius may depend on the newly selected family; no
uniform radius over all approximations is needed or imported.

The mechanism remains an actual invariant product with zero quadratic
term and nonzero cubic leading term, alongside the retained quadratic
span. A cubic correction to a function whose leading term is quadratic
is not the proposed discriminating test. Whether the candidate can be
arranged consistently and whether it excludes degree two remain proof
obligations. The ordinary convergent image is the intended target.

## Primary coverage and qualifications

**Formal transfer.** Bandiera–Manetti–Meazzini, *Formality conjecture
for minimal surfaces of Kodaira dimension 0*, Compositio Math. 157
(2021), 215–235, [1907.10690v2, 2 August 2020](https://arxiv.org/pdf/1907.10690v2),
Theorems 5.1 and 2.3 cover full endomorphism formality and DG-module
transfer under L101's checked hypotheses. Definition 2.2, the
minimal-model discussion and (2.3)–(2.4), pp. 4–5, specify the morphism
and its nonlinear terms. These are formal comparison tools, not a
statement that a prescribed harmonic second jet is free. L101 normalizes
the cohomology map; the next attempt must track nonlinear terms and
actual gauge. General formality is imported, not reproved.

**Stronger equivariant tool.** The same authors, *Deformations of
polystable sheaves on surfaces: quadraticity implies formality*, Moscow
Math. J. 22 (2022), 239–263,
[1902.06486v3, 17 June 2020](https://arxiv.org/pdf/1902.06486v3),
Definition 4.19 and Theorem 4.20, pp. 16–17, upgrade formality of a
G-equivariant L-infinity[1] algebra to equivariant formality when its
graded spaces and Hom^j(Sym^n H,H), j=0,1 and n>=2, are semisimple
G-modules. Remark 4.21 includes rational representations of a linearly
reductive algebraic group with finite total cohomology. The complete
proof with Lemma 4.22, pp. 17–18, constructs an equivariant contraction
and removes higher operations by Reynolds projections and successive
coalgebra automorphisms with identity linear term. This stronger
coverage remains formal. A later determinant-fixed Dolbeault application
must check the rational action, finite cohomology, trace restriction and
tangent normalization, then compare with actual Green-operator gauge.
No harmonic second jet or convergence is deduced in this review.

**Actual slice.** Buchdahl–Schumacher, *Polystable bundles and
representations of their automorphisms*, Complex Manifolds 9 (2022),
78–113, DOI 10.1515/coma-2021-0131,
[Lemma 2.5, Proposition 2.6, Remarks 1/3 and (2.4), pp. 83–85](https://d-nb.info/1262812674/34),
give small complex gauge fixing and the unique coexact correction for
closed inputs, with p>2 dim_C S. The implicit-function proof and residual
estimate give complete integrability equations. Remark 3 records
equivariance under parallel complex automorphisms when the transformed
input stays within the slice radius. Reuse L101's determinant-fixed
restriction and formal uniqueness. Actual gauge comparison is required;
no arbitrary algebraic chart or second-coefficient prescription is supplied.

**Finite-jet approximation.** Artin, *On the solutions of analytic
equations*, Invent. Math. 5 (1968), 277–291, Theorem (1.2), p. 277,
is used via the readable statement and proof coverage in
[Rond, *Artin approximation*, J. Singularities 17 (2018), Theorem 2.1,
p. 122, proof reductions pp. 123–126](https://www.journalofsingularities.com/volume17/rond.pdf).
For a characteristic-zero valued field, convergent equations and a
formal solution vanishing at the origin, the theorem gives a convergent
solution congruent modulo any specified parameter-ideal power. The old
first-jet precision is not a theorem limitation. The next attempt must
justify the precision needed for its actual invariant product. A
compatible truncated jet alone is insufficient. No real ASD equation,
metric compatibility or convergence of the original formal series follows.

The [original Artin scan](https://mathweb.ucsd.edu/~toal/artin.pdf)
was found again, but extraction returned no text, screenshot output
provided no inspectable image, and local download failed on DNS.
Its original proof remains unread. This is not an essential blocker:
Rond's already inspected arbitrary-order statement and proof reductions
cover the proposed use. No further retry is prescribed.

**Stronger analytic-chart comparison.** Arbarello–Saccà, *Singularities
of moduli spaces of sheaves on K3 surfaces and Nakajima quiver varieties*,
Adv. Math. 329 (2018), 649–703,
[Proposition 4.4, pp. 669–672, with Propositions 4.7/4.8](https://www.math.columbia.edu/~giulia/Quiver.pdf),
gives a tangent-identity equivariant analytic isomorphism between a Quot
étale slice for a polystable sheaf satisfying DG-Lie formality and its
quadratic cone. Read its formal equivariant lifting and analytic
approximation proof cases. This does not identify that algebraic slice
with L101's harmonic coordinates at higher order; its polarization/Quot
hypotheses require justification before use at real h. Main Theorem 1.1
and Theorem 3.7 concern dimension-one sheaves and are not substitutes
for this rank-two case. The formal-transfer/Artin route suffices for the
proposed test; no new coarse comparison or reproof is required.

**Degree comparison.** Reuse L103 and audited L104 with the exact
analytic-ring and finite-group sources in their saved assessments.
L104 supplies an actual holomorphic involution with derivative -id
and a sign-invariant convergent ring under conditional degree two.
The later cubic test must account for its tangent-identity coordinate
change and use a function with no lower leading term. A general
multiplicity-two claim, an image-normality assumption or replacement
by a weak normalization is not an adequate substitute.

## Bounded mathematical obligations and decision test

1. Propose higher data with the exact L101 first differential in the
   cohomology model, and verify its complete Maurer–Cartan equation,
   including all cross terms. Arbitrary second-jet freedom is not assumed.
2. Transfer that solution to the determinant-fixed model and perform
   actual formal slice gauge. Compute its harmonic second jet. Either
   justify an equivariant normalized comparison with the inspected
   theorem or retain its nonlinear correction explicitly. Identity on
   cohomology alone is insufficient.
3. Apply Artin only after a solution of the complete analytic equations
   exists. Specify the retained ideal power and check preservation of
   the candidate product's cubic data. Obtain an actual determinant-trivial
   locally free family before applying L102/L103 to that family.
4. Identify an actual full-group invariant with zero quadratic term
   and nonzero cubic leading term, and prove the degree test using
   L104's actual involution and coordinate change. Preserve a failure
   instead of assuming degree one.

Continue if these bridges supply the prescribed convergent family and
a valid degree-one conclusion. Abandon this cubic mechanism if compatible
higher data are forced to vanish or the claimed degree criterion fails;
retain the precise obstruction. An unexpected essential source case
outside the stated scope requires REVIEW_REQUIRED before dependent work.
SPECIALIZE approves this one test, not its conclusion. The necessary
coefficient/gauge computations are known-tool specializations and the
next attempt should be REPRODUCTION; originality is not certified.

Essential inputs: audited L094/L101/L102/L103/L104. No product F,
nonempty global reducible locus, W=r(TB), smooth central unitary gauge,
quaternionic family, prescribed global mixed action, weakly normal or
algebraic coarse comparison, global separation, reconstruction or
transport is assumed. Even success leaves all these independent gaps
and universal primitive Hodge realization unresolved. Matching Mathlib
coverage is not checked; unknown coverage is not evidence of absence.

## Search, duplicates and turn boundary

Queries included `K3 polystable sheaf equivariant formality Kuranishi
quadratic higher jets Bandiera Manetti Meazzini`, `Artin On the solutions
of analytic equations 1968 theorem 1.2 prescribed order convergent power
series`, `finite analytic surface map sign involution odd initial term
invariant generic degree two`, `"K3" "line bundles" "quiver" "Kuranishi"
split`, `"equivariant" "Kuranishi" "prescribed" jet`, and `"invariant"
"holomorphic" "odd" "initial" involution germ`. Snippets served discovery
only. BMM and Arbarello–Saccà statements and specified proof cases were
read directly. No inspected result constructs the exact family demanded.
Broader quiver and newer antisymplectic-involution leads were not read
as theorem inputs and are not dependencies. No novelty inference follows.

Scoped local checks found no completed higher-jet selection or recorded
failure of this mechanism. ATTEMPTS/061 stops necessary quadratic ASD
exclusion only. Histories 276/278 and 280/282 retain finite-degree and
conditional A1 results, not degree-selection existence. These historical
stops remain evidence at their own scopes, not global bans.

This is one LITERATURE / EXPLORATION / NOVELTY_UNCHECKED comparison.
It adds source coverage and marks the unchanged action SPECIALIZE,
without establishing a specialized mathematical conclusion. No lemma,
mathematical script, DAG edge or PROOF.md argument changes. The next
turn defaults to the bounded mathematical test; STATUS stays IN_PROGRESS.

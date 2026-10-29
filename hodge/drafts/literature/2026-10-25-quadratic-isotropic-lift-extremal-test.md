# Extremal homogeneous quadratic lift — source comparison

TARGET: Test whether every quadratic point map admits a homogeneous quadratic Serre-isotropic lift at L116's formal extremal values s=800 and t=48.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 552 searched complex quartic sums of quadratic squares, SOS/2-rank, Gram representations and cyclic CY4 obstruction identities; read the primary results below. Scoped duplicate checks reused ATTEMPTS/093,/094, L116,L165,L166 and the saved step-545/550 assessments. No prior polynomial-degree test was found in those paths; no novelty is claimed.
SOURCE_EVIDENCE: Ferguson--Ottaviani--Safey el Din--Teixeira Turatti, 2206.07473v2, Definitions 1.1-1.3, Theorem 1.5, Corollary 1.7, Sections 2-3 through Corollaries 3.5-3.6 and the relevant Gram/syzygy proofs; Ottaviani--Teixeira Turatti, 2402.05189v2, Definitions 1.1-1.4 and comparison following (1.3); Bandiera--Manetti--Meazzini, 1907.10690v2, Definition 3.6/Example 3.7 and Section 5 through (5.1). Reuse step 545's primary isotropy comparison and L165's assessed diagonalization.
COMPARISON: Known complex SOS-locus dimensions cover a comparison of 20 versus 21 quadratic squares in 48 variables; both ranks meet the printed small-rank hypothesis. This avoids unproved generic-rank formulas and any assumption that every quartic is represented by 800 squares. L165 covers nondegenerate forms; cyclic DG-Lie coverage supplies the framework for checking the necessary actual quadratic identity, without an isotropic full Kuranishi presentation.
GAP: Perform only the local specialization: compare the two cited SOS-locus dimensions, distinguish closure from exact representations, transfer a resulting test map through the prescribed complex forms and padding to U, and check the graded Jacobi/cyclic normalization for the actual quadratic bracket. None of these target conclusions is derived in this literature turn; actual beta and kappa remain unknown.
REASON: Essential coverage is now adequate for one bounded REPRODUCTION attempt on the unchanged target. Import the general results and justify only these specializations; no reproof of SOS dimension, global duality or a general formality theorem is needed.
SCOPE: Complex homogeneous quadratic maps on H of dimension 48, nondegenerate symmetric Q_U,S with dimensions 800,20, and the degree-two actual bracket identity under L116/L165/L166's complete conditional hypotheses; no computation of the actual bracket or new endpoint exclusion.
LITERATURE_REASON: The invocation-start target had REVIEW_REQUIRED coverage for polynomial-degree compatibility; step 552 supplies the missing complex SOS comparison and reuses the ready global-isotropy assessment instead of repeating that search.

The original step-551 proposal below records the uncovered target. Step
552 supplies the separate literature approval in the review following it;
no calculation or lemma is performed in step 552. No claim is made that
the formal extremal case is realized or survives other notebook branches.

## Precise proposed test

Use only L116's formal endpoint s=800, t=48 and L165's orthogonal
description. The abstract vector spaces have dim H=48, dim U=800,
dim K=20, with nondegenerate complex symmetric forms Q_U on U and
S on K. Q_U is the form transported from ker R by its actual
isomorphism to U. For an arbitrary homogeneous quadratic map
beta:H -> U, ask whether a homogeneous quadratic map g:H -> K
always exists satisfying the polynomial identity

    S(g(h),g(h)) + Q_U(beta(h),beta(h)) = 0 for every h in H.

This is the universal formal question, not an assertion about the
actual beta of L164 or the actual g left unknown in L166. No choice
of square roots separately at each h is a permitted answer. Work
over C; positivity and real sums-of-squares results have different
hypotheses. A comparison through diagonalization and quartic Gram
representations is a lead for review, not an established reduction
or rank bound in this proposal.

Plausible downstream use: determine whether imposing quadratic degree
can constrain point-obstruction maps in this endpoint, where scalar
pointwise lifting supplies no constraint. If universal lifting fails,
one still must test the actual section-image quadrics; an abstract
counterexample neither excludes F nor produces a Hodge counterexample.
If it holds, it would park this polynomial-only endpoint exclusion.

Continuation/abandonment test for review: obtain primary coverage
sufficient for one rigorous universal construction or one rigorous
counterexample to universal quadratic lifting at these exact dimensions.
Import a matching theorem if available. Separately check the precise
polarized cyclic/Jacobi hypotheses before treating the displayed
identity as a necessary condition on the actual bracket. If only
pointwise scalar lifting is covered, do not approve dependent research.

Essential local inputs are L116 and L165; L164 specifies the actual
point map only for future application, and L166 records the unknown
complementary operation. Preserve all L071/L116 family hypotheses and
their L108/L109/L111/L115 inputs for that application. Actual F,
section-image quadrics, complementary operation and integrability
remain unknown. No cross-notebook input is used. Full matching
Mathlib coverage is unchecked. This target is outside the scope of
the previously ready cyclicity-only assessment.

## Step 552: inspected primary results

Ferguson, Ottaviani, Safey el Din and Teixeira Turatti, *On the degree
of varieties of sum of squares*, J. Pure Appl. Algebra 228 (2024),
107638, DOI 10.1016/j.jpaa.2024.107638;
[arXiv:2206.07473v2, 23 February 2024](https://arxiv.org/pdf/2206.07473v2).
Read Definitions 1.1-1.3, Theorem 1.5 and Corollary 1.7, printed pp. 2-3;
the complex setting and square/Gram correspondence, pp. 3-4 and 7;
and the tangent-syzygy, pure-power and semicontinuity argument through
Corollaries 3.5-3.6, pp. 8-9.

With dim V=n+1 and square roots of degree d, SOS_k is the Zariski
closure of sums of k squares in Sym^(2d)V. Corollary 1.7 gives
dim SOS_k <= k*binom(n+d,n)-binom(k,2), with equality for k<=n.
Theorem 1.5 gives generic decomposition-fibre dimension binom(k,2)
in that range. These are affine dimensions. The proof uses the
coefficient-matrix Gram map and generic Koszul-syzygy count; its
orbit-degree conjecture is unnecessary. A closure point need not
have an exact k-square decomposition. Select witnesses in polynomial-map
images, using the closed lower-rank locus to exclude shorter expressions.

The pending specialization uses V=H^*, n=47, d=2 and k=20,21.
Both ranks satisfy the equality hypothesis. Compare these two loci next
turn, rather than claiming dominance for 800 squares or determining the
generic rank of all quartics. If that comparison succeeds, select an
exact-image tuple, transfer through the prescribed complex forms,
absorb the minus sign over C and pad coordinates to U. No dimension
comparison or target counterexample is established in this review.

For terminology and stronger-result comparison, read Ottaviani and
Teixeira Turatti, *Generalized identifiability of sums of squares*,
J. Algebra 661 (2025), 641-656, DOI 10.1016/j.jalgebra.2024.07.052;
[arXiv:2402.05189v2, 12 August 2024, Definitions 1.1-1.4 and discussion
through the main-results comparison, pp. 1-3](https://arxiv.org/pdf/2402.05189v2).
It calls the minimal number of squares the 2-rank and uses affine secant
cones. Formula (1.2) is an expected dimension and (1.3) an expected
generic rank, not unconditional formulas in every parameter. The text
explicitly cites FOST's proven small-rank range. Identifiability of
decomposition orbits is stronger information than this test needs.
No generic-rank conjecture or real positivity theorem is imported.

### Necessary actual identity: source coverage and boundary

Reuse the ready comparison in
[the step-550 assessment](2026-10-25-adjoint-complementary-yoneda-component.md)
and the product/holonomy qualifications in
[the step-545 assessment](2026-10-25-global-obstruction-isotropy-point-projection.md).
The latter inspected the primary full-Kuranishi and shifted-symplectic
results. The newly searched Cao--Leung lead does not change that review:
the narrow analytic theorem requires stable sheaves and SU(4) holonomy,
and indexed older numbering differs from 1407.7659v2. No new full-map
theorem is imported or silently extended to this product.

Read Bandiera, Manetti and Meazzini, *Formality conjecture for minimal
surfaces of Kodaira dimension 0*, Compositio Math. 157 (2021), 215-235,
DOI 10.1112/S0010437X20007605;
[arXiv:1907.10690v2, 2 August 2020, Definition 3.6/Example 3.7,
pp. 7-8, Section 5 through (5.1), p. 14](https://arxiv.org/pdf/1907.10690v2).
Definition 3.6 gives differential compatibility, bracket invariance
([x,y],z)=(x,[y,z]) and cohomological nondegeneracy; cohomology inherits
a cyclic graded Lie algebra. Example 3.7 covers locally free F on any
smooth projective complex n-fold with holomorphic volume form, using
integrated matrix trace. This framework covers n=4 and the K3 product.
Theorem 3.8 requires n<=2 and gives no formality here. Preserve the
intermediate Section 5 [h,g] versus final [g,h] discrepancy: the final
invariant identity is the input, with specialization signs to be checked.

Restrict that framework to the actual commutator-closed End_0(F), whose
perfect trace restriction and Q normalization are already in L165.
The pending test may use graded Jacobi and cyclicity on cohomology, then
L165's actual orthogonal arrows for the two components of the quadratic
bracket of j_1h with itself. Check the degree-four polarized identity
and the factor between bracket and Yoneda square, using the same
convention for both components. This is a separately identified
specialization still to be written, not a proved identity in this turn.
It requires neither a bracket-compatible derived splitting nor an
isotropic full Kuranishi presentation. L166's actual complementary
operation remains unevaluated.

## Ready bounded test and stopping criterion

The exact TARGET is unchanged. Approve one RESEARCH / REPRODUCTION
attempt importing these general results and deriving only the specified
dimension/closure/form/sign specializations. No general SOS dimension,
duality or formality theorem needs reproving. Compare the two explicit
affine dimensions and justify exact-image selection. An arbitrary Gram
matrix rank is not the minimum over all Gram representatives of a quartic.
A formal counterexample must meet H,U,K and their prescribed forms
exactly. If the comparison fails, record its actual threshold failure;
pointwise square roots, numerical evidence and real positivity do not
answer the homogeneous polynomial question.

A formal failure of universal lifting could motivate measuring the SOS
rank of the actual point-section quadrics. It would not show that the
actual quadrics are generic or outside the 20-square locus. If universal
lifting holds, park polynomial-only exclusion at this endpoint. If the
actual cyclic/Jacobi specialization remains unfinished, state that limit
independently of the formal answer. L116/L165 are essential; L164 is an
eventual actual-map input and L166 retains the unknown complementary
operation. Retain L071 and L108/L109/L111/L115 through L116. Preserve
ATTEMPTS/093 and /094; no F existence, integrability, transport or
primitive realization follows. Full matching Mathlib coverage is
unchecked; no absence is inferred. No cross-notebook input is used.

Search queries included `complex forms sums of squares quadratics generic
rank dimension quartic Gram matrix Froberg Ottaviani Shapiro`,
`sums of squares complex generic quadratic rank quartic`,
`Generalized identifiability of sums of squares dimension`,
`On the degree of varieties of sum of squares Gram matrix complex`, and
`cyclic differential graded Lie algebra invariant pairing Jacobi bracket
isotropic Calabi Yau fourfold`. Real positivity, binary-rank and full-DT4
search leads were not used as matching theorems. Further generic-rank
discovery is unnecessary for this bounded test. No lemma, target result
or mathematical script was written in this literature-only turn.

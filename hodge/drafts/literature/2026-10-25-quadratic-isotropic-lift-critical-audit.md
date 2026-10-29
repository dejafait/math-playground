# Quadratic isotropic lift specialization — critical-audit source coverage

TARGET: Critically audit L167's formal quadratic-lift counterexample and necessary actual-bracket identity under the full conditional endpoint hypotheses.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 554 reused step 552's exact-statement, stronger-result and obstruction search; compared all of L167 with that assessment, L116's hypotheses/conclusions, L164's point-map definition, L165's actual-adjoint audit, L166 and ATTEMPTS/093,/094. Targeted primary retrieval checked the cited theorem and proof cases; no new broad search or novelty inference.
SOURCE_EVIDENCE: Reread FOST 2206.07473v2 Definitions 1.1-1.3, Theorem 1.5/Corollary 1.7 (pp. 2-3), tangent-syzygy argument and Proposition 3.4/Corollaries 3.5-3.6 (pp. 8-9); BMM 1907.10690v2 Definition 3.6/Example 3.7 and Theorem 3.8's scope (pp. 7-8), Section 5 through (5.1) (p. 14). Reuse inspected EKM I.1.6/I.1.9 and duality coverage from L165's ready assessment; no fresh EKM inspection claimed.
COMPARISON: The primary results cover the exact audit's general tools, including affine closure dimensions in the printed small-rank range and cyclic trace in arbitrary dimension. L167's witness selection, prescribed-form transfer and actual component/sign comparison remain local specializations to audit; no fourfold formality or generic-rank theorem is needed.
GAP: Verify the written specialization: dimension arithmetic and exact image outside a closed locus, prescribed complex forms and padding, actual orthogonal arrows, degree-four Jacobi/polarization signs and uniform bracket/Yoneda normalization. Source coverage alone verifies none of these local conclusions or any actual bracket value.
REASON: Step 554 separately approves the unchanged critical-audit target after matching its full written scope to inspected primary results and ready local coverage. Proceed to one RESEARCH / REPRODUCTION audit; import the general theorems rather than reprove them.
SCOPE: Audit only L167 under its full conditional family and formal endpoint s=800,t=48, with H,U,K of dimensions 48,800,20 and prescribed nondegenerate complex symmetric forms; no actual-map computation, endpoint existence, integrability or full Kuranishi claim.
LITERATURE_REASON: The new critical-audit target began REVIEW_REQUIRED; separate comparison of its written exact-image and degree-four sign scope was the essential missing approval. Reuse the existing discovery assessment and inspect only load-bearing primary passages.

The exact target is to audit
`lemmas/L167-homogeneous-quadratic-serre-lift-test.md`, not to measure
the actual point quadrics or infer endpoint realization. Essential local
inputs are L116,L164,L165,L166, retaining L071 and L108/L109/L111/L115
through the full conditional family. There is no cross-notebook input.

Reuse `2026-10-25-quadratic-isotropic-lift-extremal-test.md` for precise
versions, primary theorem statements and inspected proof cases. The audit
coverage comparison must check affine versus projective dimension,
k<=n at n=47,d=2,k=20,21, and selection in the exact polynomial-map
image outside the closed lower-square locus. Diagonalization must retain
the prescribed complex forms and dimensions 48,800,20; no real positivity,
generic actual-map assumption or arbitrary Gram-matrix rank is admissible.

For the actual identity, preserve the actual trace-adjoint complement
and inverse T from L165, the full W, and the maps of L164/L166. Check the
cyclic pairing at total degree four, the odd Jacobi factor three, all
three plus signs under polarization, and the same factor 1/2 on both
components for the Yoneda-square convention. A compatible full Kuranishi
map or an n=4 formality theorem is not part of the claim. The source's
intermediate [h,g] versus final [g,h] discrepancy remains a specific sign
check, not a reason to import an extra identity.

The eventual audit must distinguish a defect needing correction from
confirmation without stronger mathematics. Neither outcome computes
actual beta or kappa, excludes F, or addresses global primitive
realization. No actual genericity, integrability or endpoint existence
is assumed. Full matching Mathlib coverage is unchecked. The proposal
above was saved in step 553; the separate source approval below is step
554. Neither step 554 nor this assessment performs the mathematical audit.

## Step 554 — separate coverage comparison

The main gap is still algebraic realization, with existence of F and the
actual point/complementary operations unresolved. The intermediate target
is the exact TARGET above. Its plausible downstream use is a dependable
necessary polynomial-compatibility test on actual maps. Confirmation of
L167 would not show that those maps violate the condition. An independent
actual-map calculation would need its own assessed target.

### Primary results and their boundaries

Ferguson--Ottaviani--Safey el Din--Teixeira Turatti, *On the degree of
varieties of sum of squares*, J. Pure Appl. Algebra 228 (2024), 107638,
DOI 10.1016/j.jpaa.2024.107638,
[arXiv:2206.07473v2, 23 February 2024](https://arxiv.org/pdf/2206.07473v2),
Definitions 1.1-1.3 and Theorem 1.5/Corollary 1.7, printed pp. 2-3:
V is complex of dimension n+1; SOS_k is the affine Zariski closure of
the sum-of-k-squares image in Sym^(2d)V. The stated dimension bound is
k*binom(n+d,n)-binom(k,2), with equality in the printed range k<=n.
The dominant map immediately preceding Corollary 1.7 fixes the affine
convention; Theorem 1.6's projective degree statement is a different use.
The pp. 8-9 tangent-kernel, pure-power and semicontinuity proof cases were
also retrieved. They concern degree-d syzygies governing the derivative;
no stronger assertion about all syzygy degrees is needed here.

For coverage comparison, L167 uses n=47,d=2,k=20,21, inside that range.
The forthcoming audit must check its arithmetic and its exact-image
selection argument. A closure point alone does not supply an exact
decomposition. Generic orbit identifiability and generic rank formulas
are unnecessary; reuse step 552's comparison with Ottaviani--Teixeira
Turatti 2402.05189v2 rather than reopen that search. No new dimension
calculation or witness is established in this literature turn.

Bandiera--Manetti--Meazzini, *Formality conjecture for minimal surfaces
of Kodaira dimension 0*, Compositio Math. 157 (2021), 215-235,
DOI 10.1112/S0010437X20007605,
[arXiv:1907.10690v2, 2 August 2020](https://arxiv.org/pdf/1907.10690v2),
Definition 3.6 and Example 3.7, printed pp. 7-8, give differential
compatibility, bracket invariance and the induced cohomological pairing
for a locally free sheaf on a smooth projective n-fold with a holomorphic
volume form. Section 5 through (5.1), p. 14, supplies the graded
commutator and integrated trace conventions before specializing to
surfaces. Theorem 3.8 explicitly assumes n<=2; it is not an input here.
The intermediate trace line reverses [g,h] to [h,g], unlike Definition
3.6 and the final invariant identity following (5.1). This recorded
discrepancy is an explicit audit item; no extra identity is imported.

The K3 product and locally free F meet Example 3.7's geometric scope.
Restriction to End_0(F), preservation of the common trace scalar, passage
to cohomology, degree-four signs and the bracket/Yoneda factor still
need the written local comparison. Do not substitute an n=4 formality
theorem, SU(4)-holonomy theorem or full Kuranishi isotropy claim.

For prescribed forms reuse Elman--Karpenko--Merkurjev, *The Algebraic
and Geometric Theory of Quadratic Forms*, AMS Colloquium Publications
56 (2008), Chapter I, Proposition 1.6/Corollary 1.9, printed pp. 13-15,
[primary text](https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=23),
as assessed in the global-point-quotient and actual-isotropic-lift audit
assessments. Characteristic is zero and the prescribed forms are complex
and nondegenerate. Their coordinate normalization and the unused
coordinates must be checked in L167; no real positivity is available.
Reuse L165's audited actual-adjoint comparison and its precise Stacks
duality citations, not an arbitrary additive splitting. Full matching
Mathlib coverage remains unchecked; L167 retains its supporting normal
form link and the relevant qualifications.

### Ready audit and discriminating test

Read the complete L167 proof in the next research turn. Check its claimed
affine dimensions against Corollary 1.7, its closed-locus/exact-image
logic, prescribed-form transfer, and the actual trace-adjoint arrows
before checking its odd Jacobi and polarization signs and both component
normalizations. L116,L164,L165,L166 are essential local inputs, retaining
L071 and L108/L109/L111/L115 as in their full conditional family. L164's
definition and L166's operation are used; their unevaluated values are
not assumptions. No cross-notebook input is needed.

Continue if those written specializations withstand critical checking;
correct or retract any defective claim while preserving its prior text
in history. If a genuinely essential source gap appears, record that
specific gap before dependent work. Confirmation alone is EXPLORATION,
not stronger mathematics; a real correction may be ADVANCE. Retain the
ATTEMPTS/093 scalar-only and ATTEMPTS/094 cyclicity-only stops. This is
approval for the bounded audit only, not for computing the actual maps,
proving F exists, excluding a cardinality, or resolving Hodge realization.

Step 554 outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. Coverage
approval changed from REVIEW_REQUIRED to SPECIALIZE; no new mathematical
result or mathematical audit was completed, and no lemma or script was
modified. The main argument and DAG are unchanged.

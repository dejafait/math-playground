# Actual complementary Yoneda component — source-covered pairing test

TARGET: Test whether L116's actual trace-adjoint retraction annihilates the adjoint Yoneda bracket on H^0(B,M).
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 550 searched trace/Yoneda cyclicity, trace-adjoint retraction, Leray obstruction and stronger hyperholomorphic bracket statements; read the primary passages below and compared L116/L164/L165 with ATTEMPTS/068,/092,/093. No inspected theorem evaluates this exact composite; no novelty claim is made.
SOURCE_EVIDENCE: Bandiera--Manetti--Meazzini, Compositio Math. 157 (2021), 215-235, arXiv:1907.10690v2 (2 August 2020), Definition 3.6/Example 3.7, pp. 7-8, and Section 5 through (5.1), p. 14; inspected Stacks 20.31.1/7 (0FKU/0FP6), 48.12.6 (0G81), and 48.27.1(5),(7)/Remarks 2-3/Lemma 4 (0FVU), with relevant proofs. Reuse steps 540/541/548 for formality limits, bracket/base-change and shift signs.
COMPARISON: Cyclic trace covers an actual global pairing computation, while L165 supplies the already audited actual mixed adjoint identity. Neither these sources nor L116's additive splitting determines the complementary bracket; this review approves a test, not its value.
GAP: In one separate mathematical attempt evaluate the actual bracket against the full included H^1(B,M), retaining actual j,r and all shift signs; cancellation or a surviving undetermined triple-cup operation remains to be established.
REASON: The unchanged target passes its source threshold for one bounded RESEARCH / REPRODUCTION specialization via the explicit pairing test below. Park if only unevaluated triple products or an unsupported multiplicative splitting remain; no new result is derived here.
SCOPE: L071/L116/L164/L165's conditional rank-two F, identical marked K3 product, original metric/triple, integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P; V=End_0(F), full W, unknown t and possibly empty Z; actual j,r,a and Q.

LITERATURE_REASON: The invocation-start proposal changed unrestricted pointwise lifting to the actual quadratic Yoneda bracket composed with r; essential cyclic-trace coverage was missing. Step 550 completes that comparison below while reusing ready cup/trace and formality assessments.

Let H=H^0(B,M), j_1=H^1(j), and R=H^2(r), using L116's actual
maps. The proposed test is whether R[j_1u,j_1v] is zero for every
u,v in H. This merely specifies the target; it is not an assertion
about the composite. Retain L164's trace-free graded-bracket convention.
The full paired component in H^1(B,M), rather than only the finite-point
projection studied in L164, is the object to assess.

Plausible downstream use: if this actual component vanishes, it removes
the unrestricted complementary freedom used in L165 for these particular
obstruction values and permits testing the remaining point constraint.
If it does not vanish, its value is additional data needed to test any
cancellation. Neither outcome alone would prove F nonexistent or settle
primitive realization. Integrability and polynomial compatibility remain
independent gaps; hypothetical F and actual section pairings remain unknown.

For the source turn reuse the exact cup/trace and bracket coverage in
`2026-10-25-actual-serre-isotropic-lift-critical-audit.md` and
`2026-10-25-adjoint-point-obstruction-projection.md`. Consult the recorded
product-formality limits in `2026-10-25-adjoint-eigenspace-yoneda-bracket.md`
before any new search. A possible method to assess is the pairing of this
component with H^1(B,M) through actual triple cups and cyclic trace.
No identity, vanishing theorem, or compatibility of these operations is
derived or approved in this proposal. Read primary hypotheses and the
needed proof cases only where the existing assessments leave that
comparison uncovered. This target is not another search for formality
or for vanishing of L164's point bracket.

Continuation/abandonment test: approve a concrete actual-map computation
only if the source comparison justifies its operations and provides a
discriminating pairing test. Import a matching theorem if found. If all
available conclusions concern only additive decomposition, unrestricted
quadratic models or a different projection, record that limit and park
the dependent claim; do not infer zero from those conclusions or repeat
the scalar-isotropy test. The proposal at invocation start approved no mathematics. Step 550 below
now approves only the specified separate test; it proves no bracket value.
Full matching Mathlib coverage for this new composite is unchecked.


## Completed primary-source comparison — step 550

This is LITERATURE / EXPLORATION / REPRODUCTION, actual task
literature_comparison. The invocation-start REVIEW_REQUIRED gate is
resolved for the same exact TARGET, without evaluating it. No lemma or
mathematical script is written; PROOF.md and DAG.md need no change.
This is source-coverage progress, not progress beyond the inspected
literature or a mathematical advance toward primitive realization.

### Imported tools and precise scope

**New cyclicity input.** R. Bandiera, M. Manetti and F. Meazzini,
*Formality conjecture for minimal surfaces of Kodaira dimension 0*,
Compositio Mathematica **157** (2021), 215-235,
DOI 10.1112/S0010437X20007605. Read
[arXiv:1907.10690v2, Definition 3.6 and Example 3.7, pp. 7-8](https://arxiv.org/pdf/1907.10690v2#page=7),
and [Section 5 through (5.1), p. 14](https://arxiv.org/pdf/1907.10690v2#page=14).
Example 3.7 supplies the integrated-trace quasi-cyclic structure for a
locally free sheaf on a smooth projective n-fold with a holomorphic volume
form. Definition 3.6 states differential compatibility, bracket invariance
and cohomological perfectness; Section 5 through (5.1) verifies the trace
construction. It permits n=4; Theorem 3.8 instead requires n<=2 and an
equivariant splitting, so is not imported. An intermediate trace line is
rendered with [h,g], while the final invariant-pairing identity uses [g,h].
Import the final identity under its explicit graded convention, not that
intermediate sign formula; retain this discrepancy for the next test.

Applicability to the chosen coefficient uses existing local inputs,
not a new trace-free formality assertion. The conditional F is locally
free on the smooth projective X=S_1 x B, with fixed volume
sigma_1 wedge sigma_B. L164 already uses the actual trace-free graded
commutator as a coefficient operation; L165 already verifies the perfect
trace restriction and the global Serre form Q. Work inside this actual
Dolbeault model and restrict its invariant pairing to those inputs.
The source does not identify j or r as bracket morphisms, and this
review does not assert that they are. Its general trace/cyclicity result
is imported, not reproved; the actual-arrow specialization is the reason
for a separate mathematical attempt.

**Actual adjunction and global cups.** Reused and reread live Stacks
[Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81):
the second coefficient must be pseudo-coherent and the original pairing
must already induce the prescribed derived-dual isomorphism. Read its
full cup/evaluation/trace argument. Reread
[Lemma 48.27.1(5),(7), Remarks 48.27.2-3 and Lemma 48.27.4, 0FVU](https://stacks.math.columbia.edu/tag/0FVU),
including the shift/triangle, smooth-dualizing and cup/evaluation proof
cases. Bounded coherent inputs give finite-dimensional perfect pairings.
Here smooth properness, locally free V and M, perfect C and the fixed
canonical trivializations meet these hypotheses through L116/L165;
ordinary local freeness of W is unnecessary. These statements justify
actual pairing functoriality, not multiplicativity of a splitting.

Reread [20.31.1, 0FKU](https://stacks.math.columbia.edu/tag/0FKU)
and [20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6), their
class-map/counit and composition proofs. They cover derived cup products
for complexes on ringed spaces and their compatibility with a composite
pushforward. Apply to p followed by global sections, with the actual
coefficient commutator and trace; iterated cups use these same operations.
The ready step 541 base-change comparison remains available, but no
ordinary middle-fibre base change is needed for this global test. Reuse
step 548's Koszul convention; do not reprove a general duality theorem.

### Exact bounded test approved for the next mathematical turn

Retain H=H^0(B,M), K=H^1(B,M), j_1=H^1(j), i=H^2(j), R=H^2(r),
and L165's normalized Q and nondegenerate restriction S. L165's existing
mixed identity is Q(x,iw)=S(Rx,w) for all x in H^2(X,V), w in K.
The proposed scalar data to compute are precisely

    Q([j_1u,j_1v], iw),  u,v in H and w in the full K.

This is a specification of the test, not a new formula for their values.
The already audited identity and nondegeneracy make these pairings
sensitive to the actual R component, unlike an arbitrary isotropic lift.
Use the cyclic trace input to attempt an evaluation with genuine global
representatives of the actual arrows. Compare any proposed cancellation
with the actual j,r and the graded commutator. In particular check
whether moving a bracket in the invariant pairing evaluates anything,
rather than only rewriting an unknown product. No unspecified matrix
model, assumed bracket-compatible splitting, purity of relative
representatives, or inference from fibre degree alone is approved.

Continue only if this yields a forced cancellation on all of K, a
justified nonzero detection, or an explicit surviving cohomological
operation identifying the precise obstruction to evaluating the target.
If only unknown global triple cups remain, save that obstruction and
park this vanishing mechanism. Merely restating a pairing criterion is
not an advance. Do not repeat the scalar-null-cone argument, the split
point dimension threshold, or formality discovery. A new geometric
identity or new subtarget outside these operations needs separate review.
The source-rendering sign discrepancy must be retained in any computation
that uses its intermediate line; the final cyclic identity is the cited
input, not a license to suppress degree signs.

If t=0 the section domain is zero; Z may be empty without eliminating K.
Neither a nonzero bracket nor a zero complementary component by itself
contradicts existence of F. Even a successful value computation leaves
actual point-section pairings, integrability, F existence, transport and
primitive Hodge realization unresolved. There is no complete candidate.

### Discovery record, duplicates and access

Narrow queries actually run included `"Yoneda" "trace" "cyclic" "Serre"
bundles`, `"K3" "product" "Yoneda" "retraction"`, `"hyperholomorphic"
"triple" "product" deformation`, `"cyclic DG-Lie" "locally free" Calabi
Yau`, `"trace" "retraction" "Yoneda" bundle`, `"Leray" "cyclic" "bracket"
K3`, `"Yoneda" "Leray" "obstruction" bundle K3 product trace`, `"cyclic"
"Serre" "retraction" "bracket"`, `"hyperholomorphic" "trace" "bracket"
"product"`, `"hyperholomorphic" "Yoneda" "orthogonal"`, `"trace adjoint"
"Yoneda"`, and `"Leray" "Yoneda" "vanishing" "K3"`. Exact and stronger
phrases yielded no inspected matching vanishing theorem; failed searches
are not evidence of novelty. The primary title/publication lookup fixed
the citation above. Institutional PDF mirrors returned 403; the arXiv v2
primary PDF supplied the needed statements and proof passages, so no
essential source blocker remains. Screenshot calls supplied no inspectable
image through the tool; the complete relevant extracted text was read,
including Example 3.7's continuation and Section 5's trace verification.

Reused the step 540 assessment's already inspected product-formality
comparison instead of repeating its external discovery. Formality does
not evaluate a bracket or make r a bracket morphism. ATTEMPTS/068's
additive Leray/section-counting stop, /092's unknown point section-image
pairings and /093's scalar-isotropy-only stop are preserved. L164 controls
the other projection; L165 supplies the actual adjoint identity but does
not apply it to compute this quadratic component. This makes the present
paired computation distinct, while leaving a strict stop if it only
moves the same unknown data. No cross-notebook input is used.

Other search hits on Fourier--Mukai monads, atomic objects and
semiregularity were not inspected at theorem level and are not coverage.
No generic moduli-product, unobstructedness, or smoothness theorem is
imported. Full matching Mathlib coverage for this actual composite is
unchecked; no absence or formal certification is claimed.

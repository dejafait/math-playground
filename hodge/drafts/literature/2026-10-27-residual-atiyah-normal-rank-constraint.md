# Actual residual Atiyah normal-rank constraint — source-approved specialization

TARGET: Determine the rank constraint on the actual normal projection of L174's residual Atiyah map from L175's point formula, and compare it with h^1(B,N)=704-s+2t.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 589 reuses the BF and point-naturality assessments, screens L108/L116/L165/L173–175 and ATTEMPTS/068,/092–095, and searches rank-sum, rank-one perturbation and composition inequalities; directly inspected Mathlib declarations and source proofs as recorded below. No completed local normal-rank comparison was found; no novelty claim follows.
SOURCE_EVIDENCE: Reuse L165's inspected Stacks 0BRT/0G81/0FVU and EKM I.1.6/I.1.9 coverage; freshly inspect LinearMap.rank_add_le, rank_comp_le_left/right and rank_le_range at https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/LinearMap.html and Matrix.rank_mul_le_left/right and rank_vecMulVec_le at https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Rank.html, with complete relevant source proofs and version links below.
COMPARISON: The known results cover orthogonal decomposition, rank subadditivity, composition bounds and target-dimension bounds over C. L174 supplies the residual Gram form and L175 supplies the actual point map. These do not already assert the normal-rank conclusion; the family-specific arrow placement, application of the rank tools and dimension comparison remain the later specialization.
GAP: Identify the actual K_N component through R, compare its pulled-back form with the known residual and point forms, and apply the imported inequalities without equating Gram rank and map rank. Retain an unknown point self-pairing, empty support and possible isotropic residual directions. No resulting bound or exclusion is derived in this source review.
REASON: Step 589 separately covers the missing general rank tools and approves the unchanged exact target as an established-route specialization. No essential new geometry is needed for this bounded test; computing a sharper actual map or point norm beyond these data would require a separate target and coverage.
SCOPE: Hypothetical locally free rank-two equality F on the identical marked K3 factors, fixed actual connection/forms/ch and actual j,r,a,Q; reduced possibly empty Z and unknown s,t; no other-factor Leray splitting, metric preservation, integrability of sections or existence of F.
LITERATURE_REASON: The target arrived with REVIEW_REQUIRED coverage; the previously ready BF and point-naturality assessments did not assess the normal-rank use or its general rank inequalities. This turn fills that specific gap, without repeating the earlier geometric source searches.

## Step 588 nomination, retained as the pre-review specification

The main gap remains primitive realization and F existence. This
intermediate test could convert the two actual Atiyah computations
into a constraint on the normal obstruction space, rather than leave
the new detector unlocated. This is a proposed application of known
rank tools, not a claim of a creative mechanism or new general theorem.

Retain L071's full mixed class and fixed family; L108's specified
orthogonal tangent/normal splitting; L116's arrows and cohomology;
L165's actual Q-orthogonal decomposition; L173's base image; and the
audited L174 and L175. The intended normal map is the K_N component
of R mathfrak a_perp, with R=H^2(r) as fixed in L165. Its placement
and pairing must be justified through those actual arrows. No
unproved equality between actual-map rank and pulled-back Gram rank
may be used, and no arbitrary splitting or real positivity is allowed.

The bounded test is to obtain a guaranteed normal-rank constraint
and compare it with L116's h^1(B,N)=704-s+2t, retaining both empty
and nonempty support. If an unknown scalar prevents a sharper bound,
state precisely what is still forced without it. If no nontrivial
constraint follows from the actual comparisons, record that limit
instead of repeating the same Gram calculation. A numerical threshold,
endpoint exclusion or improved square count has not been calculated
or approved in this nomination.

ATTEMPTS/068 stopped the old Leray/Euler identities without an
independent constraint on N. The newly evaluated actual first-factor
point map is a specified additional input for this test. ATTEMPTS/093
allows unrestricted complementary lifts, /094 concerns cyclicity,
and /095 lacks a metric comparison; none is reopened merely by
renaming it. Preserve all their evidence. Actual section brackets,
the value of t, full residual-map rank, F existence, transport and
general primitive realization remain unresolved.

The source approval should assess the exact rank comparison and
reuse the named primary coverage where sufficient. Any essential
new result must be assessed before dependent research. Full matching
Mathlib coverage is not checked; this is not evidence of absence.
No cross-notebook input, new lemma or mathematical script is proposed.

The immediate target is an established-route specialization. No
distinct source-assessed creative mechanism was justified in this
bounded audit, so it must not be relabelled creative to meet a routing
preference. At nomination the next invocation was literature_comparison;
the following separate review supplies source approval, not a calculation.

## Completed source comparison — step 589

2026-10-27. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. The exact TARGET above is approved as SPECIALIZE
for a later research turn. No normal-rank conclusion is proved here.

### Primary rank results actually inspected

Import the standard sum/composition rank inequalities by precise theorem
name, without reproving their general statements. The
[Mathlib LinearMap declarations](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/LinearMap.html)
give `LinearMap.rank_add_le`: rank(f+g)<=rank(f)+rank(g), for maps
with common domain and codomain over a ring satisfying HasRankNullity.
Its complete [source proof, lines 79–88](https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/LinearAlgebra/Dimension/LinearMap.lean)
was read: inclusion of the sum's range in the sum of the ranges,
then the submodule-dimension bound. Lines 40–74 give `rank_le_range`
and `rank_comp_le_left/right`, with their range-inclusion/map proofs.
Over C the ring, module and rank-nullity hypotheses hold; here all
spaces are finite-dimensional, so cardinal ranks give integer ranks.
No nondegeneracy or ordered-field hypothesis is needed. The docs'
source pointer fixes revision
[d79fa7b650321259f6f7257eec20974e91979f8d](https://github.com/leanprover-community/mathlib4/blob/d79fa7b650321259f6f7257eec20974e91979f8d/Mathlib/LinearAlgebra/Dimension/LinearMap.lean);
raw master proofs were read on CHECKED. No local Lean build is claimed.

The [Matrix rank declarations](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Rank.html)
give `Matrix.rank_mul_le_left/right` and `rank_vecMulVec_le`, for
finite relevant index sets over a commutative semiring satisfying
StrongRankCondition, in particular C. Read the complete
[source proofs, lines 161–191](https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/LinearAlgebra/Matrix/Rank.lean):
composition bounds for a product and a one-column factorization for
an outer product. They allow a zero scalar coefficient and impose no
positivity. The docs' source pointer fixes revision
[2fbee2a0d2d8b7f09963e870ba493f5ac6ffc4af](https://github.com/leanprover-community/mathlib4/blob/2fbee2a0d2d8b7f09963e870ba493f5ac6ffc4af/Mathlib/LinearAlgebra/Matrix/Rank.lean);
raw master proofs were read on CHECKED. These are supporting rank
results; full matching geometric Mathlib coverage is not checked.

Searches used `site.leanprover-community.github.io/mathlib4_docs Matrix
rank_add_le rank_mul_le`, `matrix rank rank one perturbation inequality
Horn Johnson Matrix Analysis 0.4.5`, and follow-ups for LinearMap rank
addition. The addition theorem was found in official source, not inferred
from an unsuccessful name search. Horn–Johnson Section 0.4.5 remained a
search-snippet lead: two full-book PDF fetches failed (404); the official
Cambridge excerpt ended at printed p.10, before that section. It is not
inspected theorem coverage. The accessible primary Mathlib proofs cover
the needed inequalities independently; there is no essential source
blocker or inference of novelty from these searches.

### Reused coverage and specialization still owed

Reuse the ready assessments `2026-10-25-global-point-quotient-isotropic-lift.md`,
`2026-10-25-actual-serre-isotropic-lift-critical-audit.md`,
`2026-10-26-first-factor-residual-atiyah-detector.md` and
`2026-10-27-first-factor-atiyah-point-critical-audit.md` in this directory.
No changed hypothesis requires rereading BF or Kuhn. The first assessment
records inspected Stacks 0BRT/0G81/0FVU statements/proofs and reused EKM,
*The Algebraic and Geometric Theory of Quadratic Forms* (2008), Chapter I,
Proposition 1.6 and Corollary 1.9, printed pp.13–15. EKM supplies orthogonal
decomposition and diagonalization under nondegeneracy in characteristic
not two, not the identity of actual arrows. Smooth proper p, locally
free V and M, perfect C and the fixed canonical forms meet the duality
hypotheses, as already specialized and audited in L165. W remains a
finite-support sheaf, not locally free. No fresh EKM retrieval is claimed.

Read L165's actual-adjoint proof/audit; L174's definitions and conclusion
(1)–(5); L175's top-edge proof and conclusion (1)–(4); L116's hypotheses,
conclusion and trace-adjoint construction; L173's kernel/decomposition
and normal-form discussion; and L108's extended orthogonal splitting
and its extension argument. This is not a new audit of every dependency.
L108 supplies the specific symplectic orthogonal summands, L165 fixes R
and the orthogonal point lift, L173 fixes K_N and the base image, L174
fixes the residual map and its Gram form, and L175 fixes its actual point
projection. They have the same conditional family and conventions.
Neither the imported rank tools nor EKM require metric comparison,
section integrability, existence of F, a value of t or a nonempty Z.

The research obligation is to establish residual-image placement through
these actual arrows, compare its normal and point contributions, and
apply the imported inequalities. Keep the point self-pairing unknown
unless separately justified; no sign, nonzero value or size is supplied
here. Check empty support separately. The known rank 15 is a pulled-back
form rank; actual-map rank and possible isotropic radical directions
remain distinct. Cite the general theorems and prove only the actual-map
specialization locally. This gate calculates no numerical threshold,
endpoint exclusion or square improvement and approves no assumed equality.

### Duplicates, purpose and decisive test

The scoped search for normal-rank, Gram, perturbation and rank-sum
comparisons in the relevant October 25–27 assessments, history/582–588
and L173–175 found no completed normal-rank result. Read ATTEMPTS/068,
/092–095. The new input relative to /068 is the audited actual point map
alongside L174's residual Gram form. This tests a specified linear image;
/093 allows unrestricted scalar-isotropic lifts, /094 leaves a global
bracket operation unevaluated, and /095 lacks an analytic metric comparison.
Their stopped mechanisms are not reopened by this approval. No external
family-specific matching theorem or originality claim is established.

The main gap is uniform primitive Hodge realization; even the conditional
F is unconstructed. A normal constraint could restrict the available
obstruction space through L116's dimension, with independent gaps remaining.
The next research turn must supply a rigorous nontrivial rank comparison
or precise insufficiency, retaining unknown point norm and empty support.
If a sharper claim needs that value or the actual normal map, park it
pending a distinct evaluable input; do not repeat Gram arithmetic or
assume positivity. Actual section brackets, t, F existence, transport
and the general Hodge target remain unresolved.

Next routing is calculation/standard/high: established finite-dimensional
tools applied to audited actual maps. No distinct new central mechanism
was identified in this gate, so the creative-route preference does not
justify relabelling this specialization. No cross-notebook input, lemma
or mathematical script was used or written. DAG and PROOF need no change.

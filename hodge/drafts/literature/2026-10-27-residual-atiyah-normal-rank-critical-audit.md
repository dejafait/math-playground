# Residual Atiyah normal rank and cardinality bound — audit coverage ready

TARGET: Critically audit L176's actual normal placement, rank-one Gram subtraction and conditional bound s<=782, retaining unknown point norm and empty support.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 591 compares the step-589 rank assessment and saved actual-duality/BF/point-naturality coverage with L176 and relevant L108/L116/L165/L173–175 passages; scoped duplicate/failure checks use histories 584/588 and ATTEMPTS/068,/092–095. Fresh inspection of the two exact cited Mathlib revisions confirms the relevant statements and complete rank proof cases; no new discovery search or novelty claim.
SOURCE_EVIDENCE: Mathlib LinearMap revision d79fa7b650321259f6f7257eec20974e91979f8d, lines 34–88, and Matrix/Rank revision 2fbee2a0d2d8b7f09963e870ba493f5ac6ffc4af, lines 117–120,154–173,187–191; reuse Stacks 0BRT/0G81/0FVU/0GWN/0FP7, EKM I.1.6/I.1.9 and the BF/Kuhn source versions and theorem passages recorded below.
COMPARISON: The known rank inequalities and saved actual-duality/naturality coverage suffice for this bounded audit over finite-dimensional complex spaces. They do not certify L176's actual normal placement, form identity or numerical exclusion; these local applications remain the mathematical audit obligation.
GAP: No essential source gap remains for the exact TARGET. Independently verify actual R placement, orthogonal form comparison, rank direction, empty support and L116's t=48 implication before accepting s<=782 as audited; retain possibly zero point norm and distinguish Gram rank from map rank.
REASON: Approve the unchanged exact audit as a later RESEARCH/REPRODUCTION conceptual audit using known tools. This literature-only step supplies source comparison and version confirmation, with no proof acceptance, new bound, lemma or mathematical script.
SCOPE: Identical marked K3 factors and fixed conditional equality family, connection/forms/full mixed class, actual j,r,a,Q,R and Atiyah maps, fixed tangent/normal splitting, reduced possibly empty Z and unknown s,t; no metric preservation, section integrability or existence of F.
LITERATURE_REASON: The new audit nomination was REVIEW_REQUIRED; compare its actual-adjoint and rank-direction obligations with ready parent coverage. The narrow fresh retrieval checks the exact pinned rank citations, whose parent assessment had inspected raw-master proofs; unchanged geometric source assessments are reused.

## Step 590 nomination: exact scope and decisive test

Inputs are L108, L116, L165, L173, L174, L175 and the proposed L176.
Keep the identical marked K3 factors, common metric/triple/forms,
actual connection, full mixed tensor and hypothetical locally free
rank-two product-polystable F with integral c_1=0 and prescribed ch.
Retain the actual j,r,a,Q,R, reduced possibly empty Z, unknown t,
and the fixed tangent/normal splitting. No cross-notebook input.

The critical claims are that R mathfrak a_perp lands in K_N via
the actual adjoint, that its Gram form is the residual rank-15 form
minus the point form of rank at most one, and that this forces
actual normal-map rank at least fourteen. The point self-pairing
remains unknown and may vanish; the Gram rank need not equal map
rank. Check that empty Z gives rank at least fifteen without w_k.
Then check 704-s+2t>=14, exclusion of t=48 using L116, and the
integer bound s<=782. A correction that changes that threshold
must be recorded explicitly; an unchanged proof is an audit outcome,
not a new discovery. No endpoint realization is claimed.

The downstream use is a reliable restriction on the hypothetical
equality kernel. F existence, actual normal-map values, section
brackets, point norm, transport and primitive Hodge realization
remain unresolved. ATTEMPTS/068,/092–095 are not reopened by the
audit. No new mechanism, source search, lemma or calculation is
performed in writing this nomination. A later mathematical audit
would be proof_audit/conceptual_audit, since the actual-arrow and
pairing comparison is essential to the new exclusion.

## Completed source comparison — step 591

2026-10-27. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. The nomination above is preserved as the
pre-review specification. Its exact TARGET is now source-ready;
the critical mathematical audit has not been performed.

### Primary rank coverage and applicability

Freshly read the cited [LinearMap revision](https://raw.githubusercontent.com/leanprover-community/mathlib4/d79fa7b650321259f6f7257eec20974e91979f8d/Mathlib/LinearAlgebra/Dimension/LinearMap.lean),
lines 34–88: `rank_le_range`, `rank_comp_le_left/right`, and
`rank_add_le`, including the complete relevant proofs. Addition
requires a ring with HasRankNullity and additive group modules;
composition uses range inclusion and mapped-range dimension.
C meets these hypotheses. Cardinal ranks here have the ordinary
integer interpretation because all spaces are finite-dimensional.
This confirms the pinned citation, rather than relying solely on the
parent's raw-master inspection.

Freshly read the cited [Matrix rank revision](https://raw.githubusercontent.com/leanprover-community/mathlib4/2fbee2a0d2d8b7f09963e870ba493f5ac6ffc4af/Mathlib/LinearAlgebra/Matrix/Rank.lean),
lines 117–120, 154–173 and 187–191. `rank_mul_le_left/right`
and `rank_vecMulVec_le` hold for the stated finite index sets over
a commutative semiring with StrongRankCondition. Their complete
relevant proofs use composition and a one-column bound. C meets
these hypotheses; no positivity or nonzero-vector condition is imposed
by the outer-product theorem. This covers the inequality tools, not
the family-specific consequence. No new rank bound is calculated here.

These are supporting Mathlib results. Full matching geometric coverage
is unchecked; no local Lean build or absence claim is made. The parent's
inaccessible Horn–Johnson lead remains unread and unnecessary.

### Reused sources and remaining mathematical obligations

Reuse `2026-10-25-actual-serre-isotropic-lift-critical-audit.md`
in this directory: Stacks 0BRT/0G81, 0FVU Lemma 48.27.1(5),(7)
and Lemma 48.27.4, tensor signs 0GWN/0FP7, and EKM,
*The Algebraic and Geometric Theory of Quadratic Forms* (2008),
Chapter I, Proposition 1.6 and Corollary 1.9, printed pp.13–15.
That assessment retains primary links, inspected proof cases and the
EKM extraction limitation. Coverage is for functorial cup/evaluation/trace,
perfect pairings and nondegenerate-subspace orthogonal decomposition in
characteristic different from two; it cannot select the actual arrows.

The conditional family still has smooth proper product projection,
locally free trace-self-dual V, perfect bounded coherent C, locally
free symplectic M and fixed canonical forms. This is within the saved
duality hypotheses. W remains finite-support, not locally free.
Read L165's proof (2)–(7) and its audit's mixed-adjoint/complement
passages to identify reusable inputs, without re-auditing them. Read
L108's splitting/extension and L116's dimensions/polystability audit
passages to delimit the normal-space and endpoint assumptions.

Reuse `2026-10-26-first-factor-residual-atiyah-detector.md` and
`2026-10-27-first-factor-atiyah-point-critical-audit.md`: BF,
arXiv:math/9912245v1, Proposition 4.2/Corollary 4.3, printed pp.28–29,
with saved trace/Chern sign qualifications; Kuhn, published 2024 e100,
Construction 4.1, Lemmas 4.2/4.4, Claim 4.5, Corollaries 4.7/5.10,
with v1 p.32 only for the saved pullback square; Stacks 0B91/0H99/08J5.
Those assessments retain exact versions, hypotheses, proof cases and
primary links. No fresh geometric retrieval is claimed or needed:
the target uses audited L174/L175 with unchanged normalization.
Read their hypotheses/conclusions and histories 584/588, plus L173's
base-image/normal-space statements, for this scope comparison.

The later audit must check L176's use of Q(x,iu)=S(Rx,u), the
cohomological orthogonality from the fixed coefficient splitting,
the inverse of A on ker R and consistency of the forms. Then check
rank-one subtraction allowing zero norm, the direction from pulled-back
Gram rank to actual map rank, empty support and L116's t restrictions.
These remain local proof obligations. Semiregularity for section brackets
must not be silently applied to the residual first-factor Atiyah map.

### Relevance, failures and decisive test

The main gap is uniform primitive Hodge realization; even F existence
is open. This intermediate audit could make the claimed restriction on
the hypothetical equality kernel reliable while independent gaps remain.
The parent assessment and scoped histories locate the completed local
comparison in L176; this is its audit, not a duplicate lemma or an
originality claim based on searching.

Read ATTEMPTS/068,/092–095. L174/L175's specified actual maps distinguish
this test from /068's Euler-only stop. The audit does not reopen
uncontrolled section pairings (/092), scalar-only exclusion (/093),
cyclicity-only vanishing (/094) or unproved metric-star compatibility
(/095). Existing unfinished work is preserved.

Continue with the exact audit if the actual-map identities and rank
inequalities support L176's stated conditional threshold. Otherwise
record the precise failure and correct or withdraw that threshold,
preserving evidence. Evaluating an unknown point norm, radical image,
actual normal map or section bracket is a different target requiring
its own assessment. No F exclusion, attainment, square improvement or
Hodge resolution is approved by this source gate.

Route next to proof_audit/conceptual_audit, deep_research/xhigh: the
delicate claim is actual Serre-adjoint placement, not arithmetic.
No distinct central creative mechanism is yet specified or source-assessed;
the essential pending audit is the immediate blocker. Do not relabel
this known-tool audit creative to meet a scheduling preference.
This turn spends no mathematical exploration budget and changes neither
the mathematical argument nor DAG/PROOF.

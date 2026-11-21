# Centered theta-power derivative: bounded independent sign test

TARGET: Attempt one analytic test of G_w(w,t)>0 throughout 1<=w<=3/2 and 40<=t<=45 for G(w,t)=xi_Q(w,w/2+i*t), using the differentiated exact Lagarias–Rains integral and retaining all tails; seek either a uniform positive margin or one rigorously certified nonpositive value, without assuming a collision or transferring any conclusion to w=1 zero preservation.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step426's completed exact theta-power/two-variable-zeta/parameter-derivative/monotonicity searches and narrowly scoped heat/affine failure comparison in 2026-11-11-theta-power-collision-orientation-review-425.md. No inspected theorem supplies this uniform signed conclusion; no novelty inferred.
SOURCE_EVIDENCE: Lagarias–Rains https://arxiv.org/pdf/math/0104176v5 Theorem2.1/(2.6)-(2.10) pp8-9 and unshifted Theorem4.4/(4.5)-(4.9)/Lemmas4.5-4.7 pp21-24; primary proof cases inspected in step426. Published AIF53(2003),1-68 https://www.numdam.org/item/10.5802/aif.1939.pdf Sections4.2/8 compared. Standard chain rule and Cauchy integral formula cover differentiation under compact holomorphic domination; no sign is imported.
COMPARISON: The new observable is one unconditional parameter-derivative factor on a fixed real box, independently of G=G_t=0. Heat evolution, an affine pencil, generator positivity and numerical zero motion give no such bound. This is neither the parked finite-zero implementation nor the generic fold identity.
GAP: Derive the exact centered derivative and effective integrable bounds, then control the signed oscillatory integral. A uniform positive margin and a certified nonpositive point are both unknown. Curvature, event existence and global continuation remain separate even if this test succeeds.
REASON: Isolate an independently testable sufficient component with a decisive analytic acceptance/failure threshold. It cannot pay the entire product; a failure can still reject a concrete stronger route without a zero locator or the blocked backend.
SCOPE: Newly written continuation, requiring separate approval next turn. One analytic sign attempt on the fixed box; no mathematical scripts, installation, evaluator implementation, root search, parameter sweep, branch tracking or global theorem. All effective estimates belong to the attempt, not this assessment.

The main gap is L030-L032/C032a actual-Xi all-degree positivity, with
forcing and L984(H) still unpaid. The intermediate target is precisely
the unconditional inequality in TARGET. If proved, it would pay the
parameter factor of the decreasing-w collision product. An independent
curvature sign at every relevant event would still be needed. A certified
nonpositive value would reject this stronger uniform factor condition,
not an event-restricted product sign, the theta family, or RH.

Use L018 to identify the distinguished w=1 slice and L019 for the theta
convention. The external input is Lagarias–Rains's entire completion,
with reflection by w and the full rational terms in (2.9). Reuse the
source assessment425's exact definitions h,gamma and y=0 integral.
No cross-notebook theorem is involved. L814's coefficient-selection
failure is comparison evidence only, not a premise or a theta sign.

First establish the chain-rule centered derivative, including the
moving s=w/2+i*t, completion, operator parameter, and theta logarithm.
Use compact complex-parameter domination and retain every boundary
and tail contribution. One may work from (2.9) with its rational terms
or the unshifted Theorem4.4, provided both represent the same completed
family. A compact qualitative O-constant is not an effective sign
margin. Do not reprove the entire-family theorem; cite it and justify
only the differentiation and estimates needed by this test.

The proposed sign is not a source theorem. Attempt a direct analytic
comparison of the resulting signed integral. An exact rational w,t
inside the box can refute the uniform claim if a complete error bound
certifies G_w<=0 there. The choice must be documented; floating-point
signs are not evidence. A proof of uniform positivity needs one explicit
positive lower margin on the entire box, with full convergence and
error control. Do not replace these thresholds by unsigned bounds,
choose coefficients from the unknown derivative, or infer a sign from
kernel positivity. No collision equations may be used as hypotheses.

Continue only on obtaining a paid sign estimate or an informative
analytic obstruction to the proposed comparison. If one bounded
attempt supplies neither, preserve the unpaid signed term and park
repetition without a materially refined mechanism. A counterexample
to uniform positivity does not allow a subsequent unreviewed search
for a different sign or a smaller favorable box in the same turn.
The original 40<=t<=45 box is retained to make failure discriminating.

This is development of a parameter-deformation diagnostic; no new
creative signed mechanism has been supplied. Full matching Mathlib
coverage is unchecked and unknown. Appropriate mathematical routing,
after separate approval, is proof_attempt/development; classification
POTENTIALLY_NEW means only that this bounded search found no coverage.

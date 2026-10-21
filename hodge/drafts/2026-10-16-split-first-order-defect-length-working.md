# Split first-order defect length — mathematical attempt

2026-10-16. RESEARCH / REPRODUCTION, proof_attempt, under the prior
SPECIALIZE assessment `literature/2026-10-16-equality-split-first-order-defect-length.md`.
The target is exactly its TARGET. No extra literature review is needed.

The universal primitive Hodge realization gap remains. The intermediate
test is length one for the actual higher-image stalk at each split
parameter. Its use would be to replace unknown local orders in L108 by
the still unknown number of split parameters; metric extension,
semistability, F existence and transport remain independent gaps.

Inputs checked: L094's full split cohomology/weights and actual-family
bridge, L095's injective harmonic derivative, L108's algebraic perfect
complex, and audited L109's actual cup/trace duality and defect inequality.
The targeted overlap/failure search finds no completed length calculation.
ATTEMPTS/063/065/066/067 and all existing work are preserved.

Saved reasoning before full write-up: at z, a minimal complex has ranks
(1,52,1). For an actual infinitesimal parameter u, its last differential's
linear term is the connecting map b -> [a_u,b] in H^2(End_0(E)), where
[a_u]=KS(u). This follows by inducing the End differential from the actual
bundle deformation, not by fibre dimensions or a coarse-moduli tangent.
For h=diag(1,-1), graded cyclic trace gives
Tr(h[a_u,b])=Tr([h,a_u]b). Serre duality is perfect, and ad_h has weights
+2,-2 with no zero sector in H^1. Thus u -> connecting map is injective
if the actual KS comparison holds. Its transpose spans m/m^2. Writing the
final row ideal I, minimality gives I subset m, and full span gives
m=I+m^2; Nakayama on m/I gives I=m. Hence the stalk is R/m.

Continue only after checking the actual algebraic/analytic first-order
comparison, the graded trace sign and both cotangent directions. A failure
of that comparison or rank stops this mechanism. Z empty is vacuous and
does not assert a split point exists. No length conclusion is yet canonical
in this checkpoint; the complete proof, if validated, will be in L110.

Completed: L110 now contains the full actual connecting-map comparison,
graded trace identity, rank-two proof and Nakayama argument, with precise
citations and Mathlib qualifications. Both cotangent directions are
controlled, giving the conditional stalk R/m. This note is retained as
the pre-write-up checkpoint; its tentative wording is superseded by L110.
No mathematical script was needed. The result awaits a separate critical
audit, whose proposed assessment remains REVIEW_REQUIRED.

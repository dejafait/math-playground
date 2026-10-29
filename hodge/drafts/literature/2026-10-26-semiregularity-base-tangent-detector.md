# Semiregularity and the fixed base-tangent detector — proposed ready specialization

TARGET: Test whether trace–Atiyah semiregularity forces L167's actual complementary bracket into H^1(B,N), retaining L165's fixed point quotient.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 578's exact trace–Atiyah review and its recorded primary searches, graded-commutator theorem, complete explicit binary proof case, stronger all-obstruction result and local failure comparisons; this target narrows that review to its specified base-tangent test.
SOURCE_EVIDENCE: Buchweitz–Flenner arXiv:math/9912245v1 Proposition 3.12 and Corollary 4.8, pp.24,32; Lepri–Manetti arXiv:2102.05016v3 Theorem 3.6/C2 and Corollaries 3.7,4.1–4.2, pp.9–13; reuse L171's saved Huybrechts–Lehn/Kuhn Atiyah/KS scope and L165's Stacks 0G81/0FVU trace/Serre scope, detailed in the parent review.
COMPARISON: Quadratic annihilation is known. The sources do not identify its base component with L165's actual tangent projection. Only that family-specific derived/Serre comparison and its consequence for L167 are proposed, without a general semiregularity reproof or novelty claim.
GAP: Verify the global comparison of the base Atiyah morphism with j composed with L108's tangent inclusion, then its Serre transpose against the actual Q and r; stalkwise equality alone does not supply it. Determine whether annihilation gives a tangent detector while retaining a.
REASON: The parent review supplies the essential tools for this bounded known-result specialization; mathematical verification is deferred. This newly written ready assessment requires separate approval next turn before research.
SCOPE: L071/L108/L116/L165/L166/L167/L171 conditional family, actual connection and arrows, general s,t and possibly empty finite reduced Z. No semiregularity injectivity, metric-star compatibility, multiplicative splitting, section integrability or F existence. No cross-notebook input.

## Purpose, exact test and boundaries

The main gap remains primitive Hodge realization and existence of F.
The intermediate target asks whether the base trace–Atiyah operation
detects the tangent component of the actual quadratic obstruction. Its
possible downstream use is to tighten the allowable complementary
polynomial lift in L167. Independent normal and point operations may
remain unknown.

Use X=S_1 x B with identical marked projective K3 factors, the original
common metric/triple/forms and actual connection. F is hypothetical,
locally free, product-polystable, rank two, with integral c_1=0 and
ch=2−14e_1−21e_2−tau_D+62P. Retain V=End_0(F), C=Rp_*V,
M=T_B direct sum N, W and the actual j,r,a. Put H=H^0(B,M),
K=H^1(B,M), E=H^2(X,V), U=H^0(B,W), R=H^2(r), A=H^2(a),
i=H^2(j), j_1=H^1(j), with L165's fixed bilinear Q and S.
The inclusion T_B -> M is L108's specific one, not an adjustable
subspace. Distinguish it from i:K -> E.

For h in H, set x=[j_1h,j_1h]. The desired restriction is a proposed
conclusion, not an assumption:

    projection of R x to H^1(B,T_B) equals zero.

Compare the Serre transpose of sigma_1's base-cotangent component
with i restricted to H^1(B,T_B). Establish the global derived
comparison first, including shifts and trace-free projection. L171
proves the degree-one sheaf comparison and a local derived lift
comparison. Test whether the actual truncation triangle supplies the
global statement; neither an arbitrary splitting nor local-to-global
equality by assertion is allowed. Then use the fixed trace/Serre
adjoint identities. Retain one universal Atiyah sign and volume scalar;
no positive norm or point-dependent normalization is involved.

Import [Buchweitz–Flenner Corollary 4.8](https://arxiv.org/pdf/math/9912245v1#page=32)
and [Lepri–Manetti Theorem 3.6 and Corollary 4.2](https://arxiv.org/pdf/2102.05016v3#page=9).
The former covers graded Yoneda commutators of perfect complexes.
The latter supplies the binary proof case and stronger all-obstruction
scope under E1 degeneration. Smooth projective X and locally free F
meet their hypotheses. They do not evaluate the tangent detector.
Reuse the primary duality and all-family KS citations in L165, L171
and the parent review; do not rederive their general theorems.

If the detector works, check the consequence for L167's actual
polynomial lift using L116's h^1(N)=704−s+2t and the restriction of
L165's form. The s=800,t=48 zero-normal-space case is a discriminating
test, not an excluded geometric case. Dimension alone says nothing
about actual bracket values. Evaluation of sigma_2 is unnecessary
for this proposed partial restriction; no vanishing of sigma_2 or
injectivity of the full semiregularity map may be inferred by omitting it.

Continue only with an actual nonzero tangent detector and explicit
constraint on R x. Park global-comparison failure or an uncontrolled
cancellation between A x and R x. Preserve t=0, Z empty, the full
normal summand and actual point quotient. A successful partial test
does not prove bracket nonvanishing, exclude F or a split cardinality,
construct cycles, supply transport or realize primitive Hodge classes.

## Reuse and routing

The complete discovery record, hypotheses, proof cases and duplicate
comparisons are in
`2026-10-26-trace-atiyah-semiregularity-actual-obstruction.md`.
Retain ATTEMPTS/004,/009,/068,/092–095. The Atiyah-weighted detector
is distinct from L166's unweighted cyclicity-only test; additional
control must still be proved. Full matching Mathlib coverage is not
checked, with no absence claim.

This is REPRODUCTION / established-route development. Do not label
the specialization creative merely because a creative turn is due.
A new central mechanism needs further input after the detector and
its residual normal gap are understood.

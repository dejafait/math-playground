# First-factor residual Atiyah Gram test — working record

2026-10-26, step 583. Incomplete reasoning saved before the calculation.
The invocation-start SPECIALIZE assessment is
`literature/2026-10-26-first-factor-residual-atiyah-detector.md`.
This is the single approved target, not a new source assessment.

Main gap: primitive realization and existence of the hypothetical F.
Intermediate target: the actual first-factor Atiyah image after
Q-orthogonal removal of L173's rank-twenty base image. A positive
residual Gram rank could supply independent obstruction constraints.
Zero or unevaluable Gram parks this test; it does not prove zero map.

Retain L071's full D and ch, L108's 2lambda sigma normalization,
L116's actual j,r and finite W, L165's Q and tensor-shift sign, and
L173's actual base lift and Serre transpose. No other-projection
Leray splitting, star comparison, integrability, image independence,
or existence of F is assumed. Z may be empty and s,t are unknown.
The prescribed pure-factor charges must be checked in the contraction
calculation, not silently omitted.

Read the relevant proofs and ATTEMPTS/093--095. Their stops do not
evaluate this two-factor Gram form. Reuse BF Proposition 4.2 and
Corollary 4.3, with r=2 and k=1, and their coefficient/trace rule;
retrieve just the relevant primary formulas to fix signs. Determine
the two self blocks and mixed block, first verifying the base block
against L108/L165/L173. Then take the actual orthogonal projection
and test the full D spectrum. No conclusion yet.

Existing uncommitted notebook work is preserved. No shared files,
supervisor state, commits, or mathematical scripts have been changed.

## Calculation checkpoint

Use d=2lambda, L=H^(1,1)(S), q its intersection form and
phi(u)=delta_u sigma, with delta_(eta tensor v)=eta wedge contraction_v.
For the symmetric cup C(u,v)=sigma(u,v), one has
q(phi(u),phi(v))=-integral sigma wedge C(u,v). With the same fixed
base-trace scalar gamma, the candidate blocks are gamma*d*q on
each diagonal and -gamma*q(Dx,y) on the off-diagonal. The diagonal
sign matches L165's S=-B_M and L108's pulled-back form d*sigma.

BF's two contractions have no remaining factorial: contraction of
Tr(R^2)/2 twice is Tr(delta_u R delta_v R); the contracted curvature
has only antiholomorphic form degree, so a further coefficient
contraction on it is zero. The same raw first-order Atiyah convention
on both factors supplies two identical signs, which cancel. Integral
c_1=0 removes the trace component in cohomology. The pure factor
point terms give H^4(S,O_S)=0 in self contractions and zero mixed
contractions, not missing charge-dependent terms.

The actual orthogonal residual should therefore be
A_perp(u)=A_1(u)+A_B(phi^{-1}(D phi(u)/d)), with Gram
gamma*q((d-D^2/d)phi(u),phi(v)). L071's retained full spectrum has
2lambda with multiplicity seven in H^2, each other doubled cubic
root with multiplicity seven, and 4 with multiplicity one. Removing
sigma and barsigma leaves multiplicities 5,7,7,1 in L. Distinct
root absolute values and d<5/2 make precisely the last fifteen
directions nondegenerate. This is a rank certificate, not positivity.
The possible five-dimensional residual radical is not proved to map
to zero. The canonical proof will retain that qualification and all
normalization details; no square-count or cardinality claim is made.

## Completed bounded attempt

The full proof, all four ordered blocks, exact root-separation check
and qualifications are now canonical in
`lemmas/L174-first-factor-residual-atiyah-gram-rank.md`. The attained
residual Gram rank is 15 against the required positive-rank threshold;
the full pulled-back Gram rank is 35. Outcome ADVANCE / REPRODUCTION,
with a separate conceptual audit still pending. No actual map rank
equality, normal/point placement or cardinality exclusion is asserted.
No mathematical script was needed: the calculation is exact symbolic
cohomology and finite-dimensional algebra, fully written in L174.

Reuse the unchanged invocation-start assessment for the same exact
mathematical target. The next task is to audit L174's sign/normalization,
determinant projection, full-tensor contraction and rank certificate;
it adds no hypotheses, source scope, new mechanism or bracket claim.

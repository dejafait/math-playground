# Fixed-surface Gauss-map determinant test — unfinished working record

Completion note: the attempt below is now written in canonical L858,
`lemmas/L858-fixed-surface-divisor-perturbation-localizes-complex-indices.md`.
The earlier provisional reasoning is preserved; it is superseded by
that full proof and is not a second canonical argument. The result
remains unaudited. Current status and the sole Next action are in
PROGRESS.md.

Invocation target and coverage: the exact TARGET in
`literature/2026-11-06-gauss-map-divisor-localization-test.md`, saved
before invocation with EXPLORE. Main gap: L030–L032/C032a actual-Xi
mixed positivity. Intermediate use: constrain compensation in an
eventual assembly of L849's collar; no forced contact or Xi sign follows.

Inputs inspected: L847 full form, radial embedding and exact J;
L849 prescribed collar and its L848 qualifications; L855 finite-n
positive germ, including its angular orientation and central Du.
Reused global-index source review and its recorded generic-isolation
failure. No L853/L854 premise and no cross-notebook input.

Work in progress, not a proved localization: for A=Du write
s=tr(A), B=A-(s/2)I and d=det(B). Then
J=1-s^2/4-d-is. Near J=0, d is positive. For F=P+iQ and a
nonnegative cutoff chi, the proposed lift sets s_t=s+t*chi*Q and
B_t=lambda_t*B, where
lambda_t^2=(d+(s^2-s_t^2)/4-t*chi*P)/d.
For sufficiently small t this is positive uniformly near the compact
contact set. Check all cutoff, collar, normalization and orientation
conditions before promoting this calculation.

The scalar identity to check is F*J_t=q+t*chi*|F|^2. Thus common
F=J=0 points survive exactly; this alone is not a localization of a
nonisolated set. The remaining test is whether their two oriented
class contributions are nonpositive, or whether this prescription
has an informative failure. L855 must give a consistent finite-n
check; exchanging the two angular/ambient coordinates reverses the
surface orientation and must be accounted for separately.

No conclusion, new lemma, invariant localization or route stop is
claimed in this partial checkpoint. Preserve this reasoning if interrupted.

## Further reasoning to verify

At J=0, tr(A)=0 and det(A)=1. Writing A=[[a,b],[c,-a]] gives
bc=-(1+a^2), so both coordinate projections z_j of the original
surface are local real diffeomorphisms. Their orientation signs agree
and equal sigma=sign(-b)=sign(c), the tangent complex-orientation
sign. The prescribed diagonal collar has J=(1-i h')(1-i b) on
its core, hence is contact-free on a smaller collar. Thus every
surviving common zero lies away from z1=z2, and each is isolated by
the inverse function theorem and isolated zeros of G. Compactness
would make this a finite set without any original isolation premise.

On a small punctured disc around such a common zero, F is nonzero
and has winding sigma*(n1+n2), where n_j is the multiplicity of
G at z_j(p), or zero if it is nonzero. The scalar identity would
then give winding J_t=-sigma*(n1+n2). Check that the local Lai
sign is sigma times this winding; the expected contribution is
-(n1+n2) in either class, consistent with L855's -n model.

For the C2 class issue, the actual ambient frame is
H(theta)(I-iA), H=diag(i*z1,i*z2). An explicit homotopy
H(theta)(I-i*r*A_t), r from 1 to 0, ends in the totally real
planes H(theta)R^2. This may prove both pulled-back complex-plane
classes have zero total without smoothing the surface. Check the
universal-class and isolated-intersection interpretation carefully.
If valid, this finishes the approved necessary index test, but it
does not force any common contact or exclude a global positive torus.

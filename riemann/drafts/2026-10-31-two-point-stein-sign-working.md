# Two-point Stein first-sign attempt — working record

Started 2026-10-31 under the unchanged, previously approved EXPLORE
assessment `drafts/literature/2026-10-31-two-point-stein-first-sign-attempt.md`.
This is one mathematical attempt, not a fresh literature review.

The main gap is actual-Xi all-degree positivity at unbounded heights.
The exact intermediate target is the generic first-sign implication
for strictly positive even smooth probability densities p on R whose
every derivative decays faster than every exponential, under
nonincrease of tau(u) = integral_u^infinity v p(v) dv / p(u) for u>0.
Write F(x)=integral p(u) exp(ixu) du. The required sign is
F'(x)^2-F(x)F''(x)>=0 for every real x.

Reuse Saumard, arXiv:1804.03926v3, Section 2 (5)-(6), pp. 3-4,
with its endpoint and integrability conditions. Bobkov--Duggal Section
16 is an available comparison; it is not a Fourier-sign theorem.
L233 supplies the first-sign/associated-kernel context; C233b excludes
its fixed Gaussian mixture as a counterexample to this premise.
The full completed transfer assessment and those two canonical proofs
were read. The fixed-model and primitive-family stops remain in force
for their particular mechanisms. No changed model or theta premise
is to be tested in this attempt.

Plan: apply the inspected Stein identity to the complete two-variable
Fourier determinant, retaining all terms. Check moments, boundary
products, Fubini and differentiated integrals explicitly. Continue only
if the resulting total has a proved sign, or a materially refined
mechanism is isolated. Stop this attempt at an exact uncontrolled
oscillatory remainder; that is not a disproof of the generic criterion.

Downstream use would require a separate actual-theta Stein hypothesis
check (L019/L233); higher signs remain independent. No cross-notebook
input and no new zero-free region are involved. No novelty is inferred
from the existing search record. No mathematical script is planned.

Unfinished reasoning at first checkpoint: set h=tau*p. Evenness and
centering should give h even and h'=-u*p; all needed growth estimates
will be justified through this product before an integration by parts.
The raw double-integral determinant will be written first, to fix the
frequency sign and avoid confusing algebraic and modulus squares.

## Partial derivation saved before completion

The raw determinant is

\[
D(x)=\tfrac12\iint (u-v)^2p(u)p(v)\cos(x(u+v))\,du\,dv.
\]

Applying the inspected one-variable Stein identity in each variable
to this expression gives the candidate exact formula

\[
D(x)=F(x)G(x)-\tfrac x2\iint
(\tau(u)-\tau(v))(u-v)\sin(x(u+v))p(u)p(v)\,du\,dv,
\quad G(x)=\int\tau(u)p(u)\cos(xu)\,du.
\]

A useful positive part is obtained from min(tau(u),tau(v)), rather than
assuming F*G has a sign. Its double Fourier integral is the layer-cake
integral of squares of truncated transforms. Writing a>b>0 and
Delta=tau(b)-tau(a)>=0 leaves the candidate remainder

\[
2\int_0^\infty\int_0^a \Delta p(a)p(b) K_x(a,b)\,db\,da,
\]
\[
K_x(a,b)=\cos(x(a+b))+\cos(x(a-b))
+x(a-b)\sin(x(a+b))+x(a+b)\sin(x(a-b)).
\]

At x>0, (a,b)=(2pi/x,pi/x) gives K=-2; (4pi/x,2pi/x)
gives K=2. These are signs of the multiplier only, not signs of the
integrated remainder for an admissible density. Complete the constants,
boundary/Fubini justification and square decomposition before recording
this as a pointwise-positivity obstruction. No counterexample or generic
sign transfer is established at this checkpoint.

## Completion

The full proof and exact constants are now canonical in
[L604](../lemmas/L604-two-point-stein-signed-remainder.md). In addition
to the sign-changing multiplier, a finite dyadic-chain argument proves
that every nonconstant monotone tau has tau(b)>tau(2b) for some b>0.
At x=pi/b this makes the actual remainder integrand negative on an
open set. The integrated remainder and the generic criterion remain
undecided. This is the stopping evidence for the pointwise mechanism,
not a new density construction or an assertion about actual theta.

The constants were also checked against the independent scalar
consequence F'=-xG of the same imported Stein identity: differentiation
gives D=F*G+x*F*G'+x^2*G^2, agreeing with the expanded two-point
expression. Boundary and moment checks are in the canonical proof;
no numerical sampling was used as evidence. The unchanged constant-tau
case reduces to D=c*F^2, and the zero-frequency expression retains
D(0)=integral u^2 p(u) du directly from (4).

Stop this attempt at the explicit missing bound R_-<=M+R_+.
The independent actual-theta premise has a pending source assessment;
no uncovered calculation is performed or approved here.

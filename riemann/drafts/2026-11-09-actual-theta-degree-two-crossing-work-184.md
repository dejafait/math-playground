# Step184: bounded degree-two residual crossing attempt

Completed with a conditional obstruction; the provisional reasoning below
is preserved as the work checkpoint. The full proof and qualifications
are canonical in
`lemmas/L915-actual-theta-contact-residual-multiple-crossing-obstruction.md`.
Independent conceptual audit is pending. The approved prior coverage is in
`drafts/literature/2026-11-09-actual-theta-degree-two-one-crossing.md`.
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
The attempted intermediate condition is exactly one strict crossing,
positive to negative, for L874's actual residual at every degree-two
PSD null contact with 0<lambda<1/20. Its possible use is a boundary-flux
comparison; contact existence and the global continuation remain open.

Read L019/L058, L874's full finite reduction and audit, and L914's
positive-definite first-block conclusion and its proof through the
certificate construction. Reused step183's primary Karlin–Novikoff
comparison and recorded source-scope failures. No new source theorem
or arbitrary replacement measure has been adopted. Existing changes
are preserved; no supplied overview has been reread.

Pending bounded test: use the square variable x=u^2, all three null
equations and the strict H1 block to reduce possible support without
dividing by any unproved coordinate or minor. Then check whether the
exact coefficient signs or the two cancellations E[R]=E[uR']=0
obstruct the proposed crossing. No conclusion is claimed yet. Any
uncovered shape premise will be recorded for separate review instead
of being silently imported. No degree sweep or H2 moment certificate
expansion is planned.

Continue only on a rigorous actual conditional crossing result,
structural obstruction, or a precise independently testable theta
premise; otherwise retire this crossing mechanism. Empty-domain
evidence alone is not a boundary-sign mechanism.

## Saved obstruction calculation, pending exact checks

The prior source chain already inspected Csordas, arXiv:1309.0055v2,
Theorems 4.1 and 4.2(b), pp.10–11. Its exact square-coordinate shape
premise is recorded in the October31 actual-theta Stein premise
assessment and L605. Reusing that premise for this target does not
import the unrelated Stein-pairing sign. The intended application is
within the approved test's independently justified theta inequalities.

Set Q(x)=R(sqrt(x)), ell(x)=lambda*x+log K(sqrt(x)), and
sigma(x)=1+2x*ell'(x). The source gives ell''<=0. If the explicit
origin bound K''(0)<-2K(0) holds, then ell'(x)<-19/20 on the prescribed
band, hence sigma'<-19/10. L874 gives E[Q]=E[sigma Q]=0, with the
actual pushforward density exp(lambda*x)K(sqrt(x))/(2sqrt(x)F(lambda,0)).
A single positive-to-negative crossing at a would make
(sigma(x)-sigma(a))*Q(x)>=0, strictly on intervals of positive measure,
contradicting these two exact cancellations. No contact existence is
needed for this conditional obstruction; it is not an actual contact
counterexample or a sign determination for E[u^2 R].

For the origin bound, v=pi*n^2 and
K_n''(0)+2K_n(0)=v(32v^3-224v^2+346v-99)exp(-v).
On 3<=v<=4 the cubic is convex and its endpoint values are -213,-251,
so the n=1 term is less than -639/81. For n>=2, dropping negative
terms and using monotonicity of v^j exp(-v), j=2,4, bounds the whole
tail by 713376 exp(-12)/(1-(3/2)^8 exp(-15))<5, using exp(3)>20.
Thus the proposed total bound is less than -26/9<0. These derivative
coefficients and rational comparisons were pending at this checkpoint.
Uniform convergence near zero and the even endpoint derivative must
be justified in the final canonical proof. No numerical contact or
replacement-law sweep is involved.

## Completion record

The exact arithmetic certificate passed all 15 checks; its complete
relevant fields were inspected. The final proof justifies the source
coordinate, even endpoint derivative, full theta series, positive tilt,
actual pushforward measure, half-line cancellations and every support
pattern. Its conditional lower count is two strict crossings against
the proposed one. No actual contact or contact-flux sign was established.
This is a mechanism-level NEGATIVE, not a solution of the main gap.
The compact current checkpoint and sole next action are in PROGRESS.md.

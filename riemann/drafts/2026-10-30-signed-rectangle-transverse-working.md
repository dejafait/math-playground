# 2026-10-30: first transverse boundary test, working checkpoint

Approved target: the exact TARGET in
`drafts/literature/2026-10-30-signed-rectangle-transverse-boundary-test.md`.
This is one mathematical attempt under its pre-existing EXPLORE coverage.
No additional source review, actual-zero application or construction search
is being undertaken. Existing notebook changes are preserved.

Main gap: actual-Xi all-degree positivity at unbounded heights. The intermediate
test seeks a uniform positive lower bound on the signed rectangle detector's
absolute K-cost, which would eliminate this possible weighted-statistic
input. Negative zero contributions and moving-test transfer remain separate.
Continue only for that lower bound or a sharpened, quantified residual;
an unsigned, unestimated boundary term does not decide feasibility.

Use the assessment's L,a,b,B,K,R and Fourier convention. Set
lambda=pi/(2a), psi(x)=cos(lambda*x),
F(y)=integral_{-a}^a Re f(x+iy) psi(x) dx, and
P(y)=Re f(a+iy)+Re f(-a+iy). Direct integration by parts gives

    F''-lambda^2 F = -lambda P,
    [exp(-lambda*y)(F'+lambda F)]_h^H
       = -lambda integral_h^H exp(-lambda*y) P(y) dy.

Here the vertical normal-derivative term vanishes because psi=0 on
both faces; the remaining side values do not vanish. Both horizontal
fluxes are retained. For b<=y<=B, continuity from the stated open
rectangle gives F>=2/lambda and P>=2. The positivity of P gives an
upper curvature inequality, not a lower one. Evenness gives F'(0)=0.

Refinement being checked: positivity of both F and P on the long
rectangle gives more than the crude Fourier upper bound at its top.
For b<h<H<B, the exact ODE solution backwards to b yields
F'(h)<=lambda*coth(lambda*(h-b))*F(h), and forwards to B yields
F'(H)>=-lambda*coth(lambda*(B-H))*F(H). The same solution bounds
F(H) by a constant times F(h)*exp(lambda*(H-h)). Thus the negative
part of exp(-lambda*H)(F'(H)+lambda*F(H)) can be exponentially
small in (B-h)/a, relative to F(h). A large positive top flux only
strengthens the necessary lower-face balance; it is not set to zero.

Taking h=2b and H=(B+h)/2 appears to isolate the gap quantity

    Q = -integral_0^b exp(-lambda*y) P(y) dy,

with a necessary lower bound of order a minus O_R(M), where
M=integral |f|K. This remains to be checked with exact constants.
The point-evaluation estimate from |phi|<=||f||_1 bounds |Q| by
O_R(M*exp(2*pi*R*b)/b), suggesting only the vanishing cost lower
bound M >>_R a*b*exp(-2*pi*R*b), not the desired positive constant.
Unfinished: verify the weighted/unweighted norm conversion, every
endpoint and sign, and the uniform finite-height remainder. No
feasibility decision is claimed.

Known inputs reused: the parent assessment's inspected Green identity
(ABR (1.1)/(1.2)) and signed Fourier norm comparison. L502 is contrast
only and is not a premise. No local lemma inputs. Mathlib unchecked.

## Completion

The refinement above is now proved, with explicit finite-height constants
and qualifications, in `lemmas/L503-signed-rectangle-transverse-boundary-leakage.md`.
The earlier unfinished markers are retained as the pre-completion record.
No mathematical script or numerical evidence was needed. The K-to-L1
conversion uses Fourier inversion and an interval of length depending
only on R; the general Logvinenko--Sereda theorem is not reproved or used.

Algebraic sign checks: a constant harmonic u gives F=2/lambda and P=2,
so F''-lambda^2 F=-lambda P with the sign in (9). A single cosine mode
u=cos(omega x)cosh(omega y) gives
F=2lambda*cos(omega a)*cosh(omega y)/(lambda^2-omega^2)
for omega!=lambda, and F=a*cosh(lambda y), P=0 at omega=lambda.
Both check the same identity, including its resonant limit. These are
checks of the finite identity only, not members of the Schwartz detector
class or evidence of detector feasibility. The threshold comparison is
exact: the final lower/desired-upper ratio is a positive constant times
(log L)*L^(c-R/2), which rules out c>=R/2 and leaves 0<c<R/2 undecided.

The nonvanishing target was not met. The first-mode identity and its
unconditional norm closure are complete; do not repeat them as a new
attempt. A further attempt would need genuinely stronger control of Q
using rectangle positivity. That changed quantitative target is saved
as REVIEW_REQUIRED, with no mathematical attempt or approval here.

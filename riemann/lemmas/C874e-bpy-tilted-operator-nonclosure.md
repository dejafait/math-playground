# Corollary C874e: the direct BPY tilted operator fails finite even-polynomial closure

## Hypotheses

Use the exact positive kernel K of L019 and the heat integral F of
L058. Fix lambda=1/16. Put a=2/pi, m=2/3 and

    x(u)=a exp(2u),             u(x)=(1/2)log(x/a),
    w(x)=exp(lambda u(x)^2+u(x)/2),
    V16=span_R{1,u^2,u^4,...,u^16}.

Let nu be the BPY S2 probability law on (0,infinity), and let
nu*(dv)=v nu(dv)/m be its size-biased law. Independently take
X with law nu, X* with law nu*, and J with probability density
(h^(-1/2)-1)dh on (0,1). Here J is neither the theta density H nor
a local Hankel matrix. BPY's S2 random variable is distinct from
L874's logarithmic coefficient S_2. Set V=J X*.

The convention is fixed: apply the size-bias identity to
f(x)=w(x)P(u(x)), with P in V16, retaining the original independent
laws on its right side. Express its expectation under the w-weighted
law of the original X, without an additional state-dependent multiplier.
Thus the free state on the right side is X, not X*.

## Conclusion

The full weight, including its half-tilt, and its normalizer are

    Z=E_nu w(X)=2F(lambda,0)>0.

The weighted full logarithmic law is the even probability measure

    d mu_tilde(u)=exp(lambda u^2) K_e(u)du/(2F(lambda,0)),
    K_e(u)=K(|u|).

Its pushforward by u->|u| is exactly L874's physical law
d mu_lambda(u)=exp(lambda u^2)K(u)du/F(lambda,0), u>=0.

Define the direct operator by

    B P(u) = (1/w(x(u))) integral_(v>0) integral_0^1
                w(x(u)+hv) P(u(x(u)+hv))
                (h^(-1/2)-1) dh nu*(dv),
    A P(u) = x(u)P(u)-m B P(u),
    A_e P(u) = (A P(u)+A P(-u))/2.

All these integrals exist absolutely at every real u, and both A P
and A_e P are absolutely integrable under mu_tilde. The identity is

    E_mu_tilde A P=0,           E_mu_lambda A_e P=0.       (1)

No independence of tilted summands is used or asserted. In particular,
the joint weight is evaluated at x(u)+hv, not factored into weights
at x(u), h and v.

Nevertheless this operator does not map V16 to V16. Already

    A_e 1(u)=a cosh(2u)-(m/2)(B1(u)+B1(-u)),
    lim_(u->infinity) exp(-2u) A_e 1(u)=1/pi>0.          (2)

An even polynomial through degree sixteen has limit zero after this
rescaling. Thus the exact pointwise closure required by the approved
finite-closure mechanism fails at the constant basis element. Checking
the other eight elements is unnecessary for this discriminator.

This is a specialization of the classical probability identity and
a negative closure test, not a new size-bias theorem or an originality
claim. It neither signs L874's flux nor rules out other nonlocal
operators. Actual H3 positivity/contact existence, S_2=0 and lower-degree
contact cases, signs, initialization, tangency, higher degrees and the
lambda=0 endpoint remain unresolved. No actual contact is assumed.

## Proof

### Imported statements and the coordinate identification

Import Philippe Biane, Jim Pitman and Marc Yor, *Probability laws
related to the Jacobi theta and Riemann zeta functions, and Brownian
excursions*, Bull. Amer. Math. Soc. **38**(4) (2001), 435-465,
DOI 10.1090/S0273-0979-01-00912-0, Section2.1 (2.9)-(2.10),
Proposition2.1(iii), p439, and Proposition3.1(i)/(3.20), p446:
https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/biane-pitman-yor.pdf.
These give Y=sqrt(pi X/2) with density H(y)/y,

    H(y)=4y^2 sum_(n>=1)(2pi^2 n^4 y^2-3pi n^2)exp(-pi n^2 y^2),
    H(1/y)=y H(y),          E X=m,          X* =_law X+J X*.

Only the distributional implication for this fixed law is used. The
characterization and its uniqueness are not reproved. Its relevant
published proof source is Jim Pitman and Marc Yor, *Infinitely divisible
laws associated with hyperbolic functions*, Canad. J. Math. **55**(2)
(2003), 292-330, DOI 10.4153/CJM-2003-014-x, Section6.3,
Proposition12(i),(iii)-(v), (120)-(126), pp318-320:
https://doi.org/10.4153/CJM-2003-014-x.
The prior assessment inspected those proof cases. This application
needs only integrable tests of the fixed distributional identity,
not an extension of its Laplace-transform characterization.

With u=log Y, the Jacobian dy=e^u du gives density H(e^u)du.
Comparing the displayed series with L019 gives

    exp(u/2)H(exp(u))=K(u)              for u>=0.

For all real u, the left side is even: H(exp(-u))=exp(u)H(exp(u)).
It is therefore K_e(u). Multiplication of H(e^u) by the weight
exp(lambda u^2+u/2) gives exp(lambda u^2)K_e(u). Integrating this
even function proves Z=2F(lambda,0). L058's domination proves that
Z is finite and that every polynomial moment under the resulting
law is finite. Positivity of K makes Z strictly positive. Reflection
then proves the half-line identification and its factor of two.
This calculation explains the positive half-tilt; using exp(-u/2)
would not give the desired physical law.

### A tail bound for the original size-biased law

The same change of variables gives the density of X:

    p_X(x)=H(sqrt(x/a))/(2x),                 x>0.

L058 bounds K(u) by C exp(9u/2-pi exp(2u)) for u>=0, for a
finite constant C. Consequently, for x>=a,

    p_X(x)<=C x exp(-r x)/(2a^2),            r=pi/a=pi^2/2,
    p_X*(x)<=C x^2 exp(-r x)/(2ma^2).

It follows by ordinary integration that

    E exp(beta X*)<infinity                 for 0<=beta<r.   (3)

Near zero the exponential is bounded and nu* is a probability measure;
the upper-tail bound handles infinity. In particular define

    beta=19/(64a)=19pi/128,
    M=E exp(beta V)<=E exp(beta X*)<infinity.                (4)

Indeed 0<V<X* almost surely and beta<r, since 19<64pi (even
pi>3/2 suffices). M>=1. No small-V inverse moment is required.

### Pointwise domain and absolute expectation identity

Fix x>0. The variable x+V is bounded away from zero. For each
P in V16, w(s)|P(u(s))| is continuous on s>=x. At infinity its
logarithmic growth is O((log s)^2+log s+log(1+log s)), which is
o(s); an upper bound suffices also where P vanishes. Thus, for
any fixed 0<gamma<r, there is a finite C_(x,P,gamma) such that

    w(x+v)|P(u(x+v))|<=C_(x,P,gamma) exp(gamma v), v>=0.

Equation (3) proves absolute convergence of B P at this x. The
h-density is integrable (its integral is 2-1=1); it introduces no
extra endpoint singularity since 0<=hv<=v. This also proves
measurability of the integral by positive and negative parts.

For global integrability, L058's domination, with an additional
linear exponential exp(2|u|), gives

    E_nu [X w(X)|P(u(X))|]<infinity.                        (5)

Explicitly its integral is a constant times an integral on u>=0
of exp(lambda u^2)(exp(2u)+exp(-2u))K(u)|P(u)|. The given
superexponential tail dominates it, and the finite endpoint is
continuous. The same argument without X proves integrability of
w(X)|P(u(X))|.

Equality in distribution applies first to the nonnegative Borel test
w(s)|P(u(s))|, with extended expectations, and then (5) makes both
sides finite. By the definition of nu*,

    E[w(X+V)|P(u(X+V))|]
       =(1/m)E_nu[X w(X)|P(u(X))|]<infinity.               (6)

Here the expectation on the left uses the original independent X,
J and X*. Tonelli's theorem justifies the nonnegative integrations.
Equation (6) licenses Fubini and the signed test f=w(P composed
with u). Dividing by Z and expressing the outer original-X integral
under its w-weighted law gives

    E_mu_tilde[x(u)P(u)]=m E_mu_tilde[B P(u)].

Moreover E_mu_tilde|B P| is bounded by the finite expression in
(6) divided by Z. Thus A P is absolutely integrable and has zero
expectation. Since mu_tilde is even, the same is true of A P(-u)
and A_e P. The latter is even, so the half-line identification gives
(1). No unproved interchange or tilted independence is hidden here.

### Uniform bound on B1 and the constant-image obstruction

For u>=0 and v>=0 put t=v/a and L=log(1+t exp(-2u)). Then
u(x(u)+v)=u+L/2, and exactly

    log(w(x(u)+v)/w(x(u)))
        =lambda u L+(lambda/4)L^2+L/4.

The elementary inequalities log(1+s)<=s and
log(1+s)<=sqrt(s) hold for s>=0. The second follows by comparing
derivatives 1/(1+s)<=1/(2sqrt(s)) for s>0 and their values at zero.
Also u exp(-2u)<=1/2 for u>=0, since exp(2u)>=2u. Hence

    u L<=t/2,              L^2<=t,              L<=t,
    log(w(x(u)+v)/w(x(u)))<=(3lambda/4+1/4)t=19t/64.

Apply this pointwise inequality to v=V and use (4):

    0<B1(u)<=M,                                      u>=0. (7)

For u<=0, x=x(u)<=a. As a function of s>0,

    log w(s)=(lambda/4)log^2(s/a)+(1/4)log(s/a).

The function w decreases up to s0=a exp(-8) and increases afterwards. Its
minimum is exp(-1). If x+v<=s0, monotonicity on that interval
gives w(x+v)<=w(x). If x+v>s0, then a+v>=x+v>s0, and monotonicity
on the upper interval gives w(x+v)<=w(a+v). Thus in all cases

    w(x+v)<=w(x)+w(a+v).

At u=0 the bound used in (7) gives E w(a+V)<=M, since w(a)=1.
Consequently

    0<B1(u)<=1+M/w(x(u))<=1+exp(1)M,                  u<=0. (8)

Equations (7)-(8) give a finite uniform bound C0=1+exp(1)M for
B1 on the whole real line. This argument avoids asserting that
E w(V) is finite; no such assertion is needed or imported.

For P=1, reflection averages x(u) and x(-u) to a cosh(2u).
Therefore the exact operator obeys

    a cosh(2u)-m C0 <= A_e 1(u) <= a cosh(2u).

Multiplying by exp(-2u) and taking u->infinity proves (2), because
a/2=1/pi. For every Q in V16, exp(-2u)Q(u)->0, so A_e 1 cannot
equal such a Q pointwise. In fact this rules out any polynomial
image for this basis element. It stops precisely the stated direct
finite-closure test; no alternative rescaling, moment projection or
choice of test has been substituted to force closure.

### Verification and limits

The certificate is the analytic two-sided bound above, not a numerical
fit. Its required polynomial threshold is zero after multiplication
by exp(-2u), whereas its proved limit is 1/pi>0. No numerical or
symbolic script is necessary. The exponent comparison beta<pi^2/2,
the log-coordinate Jacobians, the positive half-tilt, the factor two,
the original product integration measure and the absolute integrability
of both sides have been stated explicitly.

The prior literature assessment is
`drafts/literature/2026-11-21-theta-size-bias-contact-nomination-2139.md`.
The algebra above fixes its requested convention; it is necessary
bookkeeping for a changed test not supplied as a tilted theorem by
BPY. The classical identity and its Laplace proof are imported, not
reproved. The separate critical audit below validates the stated local
result without extending its scope.

For context only, L874's full-degree d=2 response has degree twelve, its flux observable
degree fourteen, and the H3 premise also needs degree sixteen. Failure
on 1 excludes closure on that specified space before any contact or
signed inequality is used. It does not rule out a useful exact relation
involving the nonpolynomial observables just exhibited. C874b-d's
auxiliary moment laws are not substituted for the physical theta law.
Nothing here identifies them, supplies a contact sign, or proves RH.

### Independent conceptual audit — 21 November 2026, step2143

**Verdict: pass for the stated direct convention and domain.** This
audit replays the changed-law specialization authorized by
`drafts/literature/2026-11-21-bpy-tilted-operator-audit-2141.md`.
It establishes no further size-bias theorem or nonclosure result.
The primary theorem hypotheses and essential proof coverage are reused
from that assessment; L019's displayed series and L058's explicit
domination were checked directly. The following checks concern the
local analytic specialization, not a reproof of the imported law.

The density pushforward gives p_U(u)=H(e^u). The reciprocal identity
gives p_U(-u)=e^u p_U(u), so multiplying by e^(u/2), with the positive
sign, makes this density even. Termwise comparison with L019 gives
e^(u/2)p_U(u)=K(u) on u>=0. Thus the weighted full density is
e^(u^2/16)K_e(u)/Z and its two equal half-line masses require
Z=2F(1/16,0). The original-X size-bias formula is

    E_nu[X f(X)] = m E[f(X+J X*)].

For f=w(P composed with u), conditioning on the original X and
dividing by Z gives exactly xP-m BP. This fixes the factor m and
the multiplication term xP; replacing the free state by X* would
change the operator. The integration laws inside B remain nu* and
the stated J density.

For completeness, the absolute-domain calculation has the exact
finite integral

    E_nu[X w(X)|P(u(X))|]
      = a integral_0^infinity (e^(2u)+e^(-2u))
          e^(u^2/16)K(u)|P(u)| du.

Here evenness of P is used, and L058 bounds the integrand by a
polynomial times exp(u^2/16+(13/2)u-pi e^(2u)). This is integrable
and has no singularity at zero. Applying the distributional identity
to the nonnegative test first gives the exact equality (6); it is
not inferred from separate tilted integrability of the summands.
For a fixed x>0, continuity on [x,infinity) and the subexponential
growth of w(s)|P(u(s))| give the separate pointwise domain. The
upper density bound yields r=pi/a=pi^2/2, so the pointwise domain
and the B1 estimate below use genuine exponential moments of X*,
with parameters strictly below r. The global argument instead uses
the theta integral above. Reflection preserves the L1 norm because mu_tilde is even,
and an even integrable test has the same full-law expectation as
its half-line pushforward. This verifies both identities in (1).

The positive-half-line estimate can be checked term by term:
u log(1+t e^(-2u))<=t/2,
log^2(1+t e^(-2u))<=t, and log(1+t e^(-2u))<=t.
At lambda=1/16 their coefficients sum to
1/32+1/64+1/4=19/64. Consequently beta=19pi/128<pi^2/2,
equivalent to 19<64pi, makes M finite. On the negative half-line,

    log w(x(u))=(u+4)^2/16-1,

so the minimum is e^(-1), attained at x=a e^(-8). The two monotone
branches imply the stated inequality w(x+v)<=w(x)+w(a+v) for
x<=a and v>=0. Since w(a)=1, this yields the bound 1+e M in (8).
It does not pass to x=0 inside an expectation and does not assert
integrability of w(J X*). Hence C0=1+e M bounds B1 on both sides.

Finally, positivity and this uniform bound imply

    (a/2)(1+e^(-4u))-m C0 e^(-2u)
       <= e^(-2u) A_e1(u) <= (a/2)(1+e^(-4u)),  u>=0.

Both bounds tend to a/2=1/pi. The required limit for a polynomial
is zero, proving the discriminator without a fit or numerical
certificate. This is pointwise nonclosure for the fixed direct
operator, not a failure of (1), a claim about all operators, or a
contact-sign theorem. No correction of the original argument or new
mathematical input is necessary; its local stop is now audited.

## Mathlib

The full transformed-operator/nonclosure result is not checked in
Mathlib. Supporting coverage for weighted measures, change of variables,
Tonelli/Fubini, exponential-tail integrability and polynomial growth
is also not checked here; no absence is claimed. Reference:
https://leanprover-community.github.io/mathlib4_docs/.

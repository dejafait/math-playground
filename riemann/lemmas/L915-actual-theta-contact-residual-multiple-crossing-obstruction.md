# Lemma 915: a low-time actual-theta contact residual cannot have one crossing

## Hypotheses

Use L019's full theta kernel K, L058's family

    F(lambda,z)=integral_0^infinity exp(lambda*u^2)K(u)cos(zu)du,
    g_lambda(z)=F(lambda,z)/F(lambda,0),
    log g_lambda(z)=-sum_(k>=1) S_k(lambda)z^(2k)/k.

Fix 0<lambda<1/20 and a nonzero real c=(c0,c1,c2). Assume

    H_2=(S_(i+j+2))_(0<=i,j<=2) is positive semidefinite,
    H_2 c=0,

retaining all three null equations and every support pattern. Define
r=max{i:c_i!=0}, N=2r+2, b_n=sum_(i+j=n-2)c_i*c_j, and L874's

    R(u)=-sum_(n=2)^N n*b_n*[z^(2n)]cos(zu)/g_lambda(z).

Expectation E is always under the actual half-line density
rho_lambda(u)=exp(lambda*u^2)K(u)/F(lambda,0), not a replacement law.

Import the following previously assessed source input as stated:
George Csordas, *Fourier transforms of positive definite kernels and
the Riemann xi-function*, [arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
equation (4.2), Theorem 4.1, p.10, and Theorem 4.2(b), p.11.
For the source kernel Phi these supply positivity, even analyticity
and concavity of s -> log Phi(sqrt(s)) for s>0. Only non-strict
concavity is needed here. The exact source conditions were inspected
in `drafts/literature/2026-10-31-actual-theta-stein-premise-scope.md`
and reused by the November6 contact-score and step183 comparisons.
No Stein covariance sign, GHS inequality or deformed zero product is
imported. The original 1988 proof has not been independently audited;
the stated Csordas theorem is the named theorem input.

For the optional assertion c2!=0 below, also assume L914's stated
arithmetic contracts. The crossing obstruction itself does not use
that computer-assisted input.

## Conclusion

At any such contact, R has **at least two strict sign changes** on
(0,infinity). In particular it cannot have exactly one strict sign
change, positive to negative. Even-multiplicity zeros, a zero at the
origin, and vanishing coordinates of c are retained. With L914's
arithmetic contracts, c2!=0 and R has degree twelve; without this
optional reduction the argument covers all r=0,1,2 directly.

The actual-kernel estimates used in the proof are

    K''(0)+2K(0)<-26/9<0,
    ell_lambda(x)=lambda*x+log K(sqrt(x)),
    sigma_lambda(x)=1+2x*ell_lambda'(x),
    ell_lambda'(x)<-19/20,
    sigma_lambda'(x)<-19/10                 (x>0).

This is a conditional obstruction to the proposed one-crossing
sufficient condition. It does not establish the existence of a
contact. If there are no such contacts, the original universal
one-crossing claim is vacuous; this result is not an actual-theta
counterexample to that universal statement. It does not determine
the desired flux E[u^2 R], refute that flux inequality, establish
higher-degree positivity, or prove or disprove RH. The existing argument
passed the independent conceptual audit in step186 below, with its
named source input and optional arithmetic qualification retained.

## Proof

### Source coordinates and the tilted square variable

The summand in source equation (4.2) is

    pi*n^2*(2*pi*n^2*exp(4t)-3)*exp(5t-pi*n^2*exp(4t)).

Multiplying by four and substituting t=u/2 gives exactly L019's
summand. Hence K(u)=4 Phi(u/2) for u>=0. The source even analytic
extension implies K'(0)=0 and gives an even Taylor expansion near
zero. Its square-coordinate theorem therefore gives concavity of

    B(x)=log K(sqrt(x))=log 4+log Phi(sqrt(x/4))

on x>0. This is a positive linear rescaling of the source coordinate;
no Jacobian enters this shape statement. In particular B''(x)<=0.
The even expansion and K(0)>0 give the finite right derivative

    B'(0)=K''(0)/(2K(0)).                                (1)

Adding lambda*x preserves concavity. We still need a quantitative
origin bound to show that the positive tilt preserves a negative
slope. Ordinary log-concavity or an untilted Stein ratio alone would
not justify that inference.

### An origin bound retaining the entire theta series

Write v=pi*n^2*exp(2u). Then

    K_n(u)=exp(u/2-v)*(8v^2-12v).

Differentiation of exp(u/2-v)*p(v) replaces p by
2v*p'(v)+(1/2-2v)*p(v). Two differentiations give, at u=0 and
v=pi*n^2,

    K_n''(0)=(32v^4-224v^3+330v^2-75v)exp(-v),
    K_n''(0)+2K_n(0)=v*P(v)*exp(-v),
    P(v)=32v^3-224v^2+346v-99.                          (2)

These differentiations are legitimate for the whole series. On a
fixed real neighborhood |u|<=epsilon, every summand and its first
two derivatives are bounded by C_epsilon*(1+n^8)*exp(-c_epsilon*n^2)
with c_epsilon>0. This summable bound gives local uniform convergence
of the differentiated series, including at zero. Thus summing (2)
calculates the actual K''(0)+2K(0).

For n=1 use 3<pi<4. On [3,4],

    P''(v)=192v-448>=128,
    P(3)=-213,       P(4)=-251.

Convexity places P below its endpoint chord, so P(v)<=-213.
Consequently v*P(v)<=-639. The exponential series gives e<3:
n!>=2^(n-1) for n>=1, with a strict inequality for some n, and
summing the resulting geometric bound gives that strict inequality.
Therefore exp(-pi)>exp(-4)>1/81, and the entire n=1 contribution
in (2) is less than -639/81=-71/9.

For every n>=2, discard only the negative terms of (2), obtaining

    (K_n''+2K_n)(0)<=(32v^4+346v^2)exp(-v).

For j=2,4, the derivative of v^j*exp(-v) is
v^(j-1)*(j-v)*exp(-v), nonpositive on v>=j. Since v>3n^2>=12,
the preceding upper bound is at most

    (2592*n^8+3114*n^4)exp(-3n^2).

Set n=2+j, j>=0 integer. Successive ratios give
n<=2*(3/2)^j; also n^2>=4+5j because j(j-1)>=0. Thus the full
sum over n>=2 is bounded above by

    713376*exp(-12)/(1-(3/2)^8*exp(-15)).                 (3)

Indeed 2592*2^8+3114*2^4=713376, and the fourth-power geometric
factor is at most the eighth-power one. The denominator is positive:
the positive series through degree eight gives

    exp(3)>sum_(j=0)^8 3^j/j!=89641/4480>20,
    (3/2)^8*exp(-15)<6561/819200000<1/10.

Using exp(12)>20^4, (3) is strictly less than

    713376/(20^4*(9/10))=2477/500<5.

Combining this upper bound for the entire remaining series with the
n=1 bound proves

    K''(0)+2K(0)<-71/9+5=-26/9.                         (4)

There is no finite-theta truncation or sampled kernel sign here.
Since K(0)>0, (4) gives B'(0)<-1 by (1).

### Strictly decreasing dilation score on the whole half-line

Concavity and the finite right derivative at zero imply
B'(x)<=B'(0)<-1 for every x>0. Consequently on the stipulated band

    ell_lambda'(x)=lambda+B'(x)<lambda-1<-19/20,
    ell_lambda''(x)=B''(x)<=0.

Therefore

    sigma_lambda'(x)
      =2*ell_lambda'(x)+2x*ell_lambda''(x)<-19/10.        (5)

This controls the actual tilted dilation score globally. Neither
monotonicity of individual summands nor preservation of concavity
under an arbitrary sum is assumed. The source supplies concavity of
the full kernel in the correct variable; (4) pays for the tilt.

### Polynomial residual, cancellations and support

Let a_j=[z^(2j)]g_lambda(z)^(-1). In the square variable,

    Q(x)=R(sqrt(x))
        =-sum_(n=2)^N n*b_n
                      sum_(j=0)^n a_(n-j)*(-1)^j*x^j/(2j)!.

This is a real polynomial of degree N=2r+2, with leading coefficient
-N*c_r^2/(2N)!<0. L874 gives E[R]=0 and E[uR']=0 at the full null
contact, and proves that R takes both signs with a negative tail.
No parameter derivative of R is being taken here.

The pushforward of the actual probability measure under x=u^2 is

    dnu_lambda(x)=exp(lambda*x)K(sqrt(x))
                   /(2sqrt(x)*F(lambda,0)) dx,    x>0.   (6)

It has strictly positive density on every open positive interval.
The factor x^(-1/2) is retained; (6) is not the auxiliary density
proportional to K(sqrt(x)) used in a hazard theorem.

The score in (5) satisfies exactly

    sigma_lambda(u^2)=1+2lambda*u^2+u*K'(u)/K(u).

L874's justified integration by parts gives

    0=E[R+uR'+2lambda*u^2 R+u(K'/K)R].

Since E[uR']=0, this identity and E[R]=0 become

    integral Q dnu_lambda=0,
    integral sigma_lambda*Q dnu_lambda=0.               (7)

All terms are absolutely integrable. In particular the last score
term times the original density equals a constant times
u*R(u)*exp(lambda*u^2)*K'(u); L874 supplies its integrable bound
and the vanishing endpoint product u*R*exp(lambda*u^2)*K at both
zero and infinity. Thus (7) uses the full half-line identity, not
a finite-interval zero-mass approximation. The square-coordinate
density's integrable singularity at zero creates no additional
boundary term because this integration by parts was done in u.

This argument covers every r and every zero coordinate directly.
For completeness, under L914's contracts the first principal block
H1 is strictly positive definite on [0,1/20]. If c2=0, the first
two rows of H2*c=0 read H1*(c0,c1)^T=0, forcing c0=c1=0, which is
excluded. Thus c2!=0 under those contracts, N=6, and the coefficient
of x^6 is -6c2^2/12!. No division by c0, c1, c2 or an unproved
minor is used. The third null row remains among the hypotheses;
the general cancellations in L874 use all the required null rows.

### Exclusion of a single strict crossing

Q is a nonzero polynomial, has both signs, and is strictly negative
eventually. It has finitely many real zeros, hence at least one
strict sign change on the positive axis. Suppose that there is
exactly one, at a>0. Its negative tail forces the orientation
positive to negative. Thus Q(x)>=0 for 0<x<a and Q(x)<=0 for x>a,
allowing any zeros at which the sign does not change.

By the strict decrease in (5),

    (sigma_lambda(x)-sigma_lambda(a))*Q(x)>=0

throughout the positive axis. This product is strictly positive
on open intervals on which Q is nonzero on each side of a.
The positive density (6) and the absolute integrability already
checked give a strictly positive integral. But (7) makes that
integral exactly

    integral sigma_lambda*Q dnu_lambda
       -sigma_lambda(a)*integral Q dnu_lambda=0,

a contradiction. Hence there are at least two strict sign changes.
Tangential roots and a root at zero do not affect this argument.
Since u -> u^2 preserves order on (0,infinity), R and Q have the
same strict sign-change count there.

The sign-change argument is the elementary two-function
orthogonality obstruction behind Chebyshev-system moment lemmas;
compare Karlin–Novikoff, *Generalized convex inequalities*,
Pacific J. Math.13(1963),1251–1279,
[Section3, LemmaA, p.1265](https://msp.org/pjm/1963/13-4/pjm-v13-n4-p18-s.pdf).
Its finite-interval statement was inspected in step183. The direct
two-function proof above is retained to verify strictness and the
actual half-line hypotheses, rather than importing an unchecked
infinite-interval extension. No general variation-diminishing
theorem is reproved. The new tested difference is the exact tilted
actual-theta applicability and its obstruction to the nominated
one-crossing condition, not novelty of the elementary comparison.

### Exact arithmetic certificate and limits of verification

Run `python3 scripts/heat/contact-one-crossing-obstruction-184.py`.
Its complete certificate is
`scripts/heat/contact-one-crossing-obstruction-184.json`. It checks
the differentiated polynomials with rational arithmetic, convexity
endpoint values, the positive exponential partial sum, geometric
ratio, entire-series bound and rational thresholds. All 15 checks
pass with no failures. The complete `checks`, `bounds` and `summary`
fields were inspected with `../scripts/loop/inspect_json.py`.

The certificate confirms the finite algebra and arithmetic; it
does not independently audit the source theorem, domination,
contact identities, or logical crossing proof. This result is not
numerical evidence of an actual null contact. Initialization,
tangency, degree-uniform continuation, the contact-flux sign and
the RH endpoint remain open.

### Independent conceptual audit — 9 November 2026, step186

The audit accepts the stated conditional result without strengthening
it. It uses the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-09-l915-conceptual-audit.md`. The full proof
above, L019's kernel, L058's normalization/domination, L874's relevant
identities and endpoint estimates (including its step11 audit), and
L914's optional hypothesis/conclusion were inspected. No new lemma or
contact search was undertaken.

1. The named Csordas v2 primary text was checked at (4.2) and
   Theorem4.1(i)-(iii), p.10, and Theorem4.2(b), p.11. Direct
   substitution gives
   4*pi*n^2*(2*pi*n^2*exp(2u)-3)*exp(5u/2-pi*n^2*exp(2u)),
   exactly K_n(u) in L019. Thus the square variable rescales by x/4,
   not x/2. Even analyticity and positivity give an analytic logarithm
   near zero and B(x)=log K(0)+K''(0)x/(2K(0))+O(x^2).
   On x>0 the imported concavity gives B''<=0; its finite limiting
   slope at zero is therefore a legitimate global upper bound for
   B'. No theorem about a tilted kernel was silently imported. The
   named theorem is an input; its original 1988 proof was not audited.
2. The differentiation operator in (2), both resulting coefficient
   arrays, and the complete majorization (3) were checked. On a
   two-sided fixed real neighborhood, v is between positive constant
   multiples of n^2; the derivative polynomials have degree at most
   four. This supplies the stated summable uniform bound, including
   at zero. Convexity places P below its endpoint chord; because
   v*P(v) is negative, exp(-pi)>1/81 yields an upper, not a lower,
   bound for the first contribution. For n>=2 the two positive terms
   decrease after v=12 and may be bounded at 3n^2. Both integer
   inequalities for n=2+j hold for every j>=0, including j=0,1.
   Hence the geometric series bounds the entire tail, not a finite
   prefix. The positive exponential partial sum is 89641/4480>20;
   the ratio is less than 6561/819200000<1/10, and the tail is less
   than 2477/500<5. With the head less than -71/9, (4) follows.
   Positivity of K(0), rather than any estimate for its size, gives
   B'(0)<-1. Adding lambda<1/20 and using x>0 in
   2ell_lambda'+2x*ell_lambda'' proves the strict constants in (5).
3. Since g_lambda(0)=1, its reciprocal germ exists and its coefficients
   are real. The finite formula for Q consequently has degree N,
   with negative leading coefficient because N=2r+2 is even and
   b_N=c_r^2>0. L874's cancellation is exactly
   sum_n n*b_n*S_n=2 sum_i (i+1)c_i(H_2 c)_i=0;
   together with E[T_n]=0 and E[u*T_n']=-2S_n this gives both
   E[R]=0 and E[uR']=0 with the stated signs and factors. These are
   finite coefficient identities, not a global reciprocal expansion
   or a parameter differentiation treating R as fixed.
4. The Jacobian in (6) is du=dx/(2sqrt(x)). Near zero its density is
   O(x^(-1/2)); Q is bounded and sigma_lambda(x)=1+O(x).
   At infinity L058's bound and L874's |K'| bound absorb every
   polynomial and exp(lambda*u^2). In particular the absolute score
   pairing is controlled by the sum of the polynomial pairings with
   K and u|K'|, without a reciprocal-K estimate. The endpoint product
   vanishes at zero by its explicit u and at infinity by the complete
   theta bound. Integration in u therefore proves both equations
   in (7) on the full half-line; no truncated measure is substituted.
5. Integral Q dnu_lambda=0, the negative leading coefficient and the strictly
   positive density force both signs on positive open intervals.
   A polynomial has only finitely many zeros. If there were exactly
   one strict crossing a>0, the negative tail forces the stated
   orientation even with additional tangential roots. The product
   (sigma_lambda-sigma_lambda(a))*Q is nonnegative everywhere and
   strictly positive on an open interval of positive measure. Its
   absolute integral is finite by point 4 and the polynomial moment
   bound. Its integral cannot then be zero, contrary to (7).
   A zero at x=0 does not affect this contradiction. Karlin–Novikoff
   Section3 LemmaA and its contradiction proof, p.1265, were checked
   as the classical comparison; their finite-interval statement is
   not being used to bypass these half-line checks.
6. No coordinate of c is divided out. The preceding checks cover
   r=0,1,2. For the optional reduction, H1 in L914 has exactly the
   same S2,S3,S4 normalization as the upper-left block of H2.
   If c2=0 its first two null rows give H1*(c0,c1)^T=0.
   L914's conditional positive definiteness makes this impossible
   for nonzero c. Its numerical certificate and arithmetic library
   were not independently re-audited in this step; those contracts
   are unnecessary for the minimum-two-crossings conclusion.

The existing rational program was read and replayed using the command
above. Its complete `checks`, `bounds` and `summary` fields were
inspected with `../scripts/loop/inspect_json.py --pointer ... --full`:
15/15 checks pass, with no failures. This replay supports the finite
arithmetic; the analytic and strictness checks are the audit above.
The DAG already contains the direct local inputs used here and needs
no change. No substantive defect was found. This is local verification
of the recorded specialization, not a new result beyond the sources
checked. The contact domain may still be empty, and neither its
existence nor the flux sign, initialization, tangency, all-degree
continuation or RH follows.

## Mathlib

Full matching coverage and supporting coverage for the theta shape
import, score specialization and strict half-line crossing argument
have not been checked. Availability is unknown, not asserted absent.
No formal theorem proving the contact-flux sign is imported.

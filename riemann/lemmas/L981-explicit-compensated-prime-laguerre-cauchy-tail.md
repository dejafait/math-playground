# Lemma 981: explicit compensated prime-Laguerre Cauchy tail

## Hypotheses

Let Lambda be the actual von Mangoldt function, so
psi(x)=sum_(2<=m<=x) Lambda(m) includes every prime power fully,
also when the real endpoint x is itself a prime power. For each
integer n>=2, use the usual generalized Laguerre polynomial and set

    ell_n(u)=L_(n-1)^(1)(u),
    P_n(X)=sum_(2<=m<=X) Lambda(m)*ell_n(log m)/m
           -integral_1^X ell_n(log x) dx/x,       X>1,
    k=n+1,   U=10000*k^4,   V=100*k^2,   X_n=exp(U).

All finite integrals are ordinary Lebesgue integrals (equivalently,
Riemann integrals here). No RH, zero simplicity, arithmetic sign,
identification with S_f, or interchange of n and X limits is assumed.

## Conclusion

For every integer n>=2 and every real Y>=X_n,

    |P_n(Y)-P_n(X_n)|<=exp(-70*(n+1)^2)<1.             (1)

This verifies the approved error1 cutoff, with a deliberately coarse
scale and complete endpoint jumps. It is a REPRODUCTION: an explicit
specialization of the known inputs below, not a new sign mechanism
or a claim of progress beyond those sources. It neither identifies
an infinite limit with S_f nor controls the retained finite signed
observable. Written in step226, 10 November2026; the independent
step227 audit below verifies the stated bound on its exact scope.

## Proof

### Imported inputs and the reason for specialization

Import Daniel R. Johnston and Andrew Yang, *Some explicit estimates
for the error term in the prime number theorem*,
[arXiv2204.01980v2, 20 April2022](https://arxiv.org/pdf/2204.01980v2),
Theorem1.1/(1.3), p2 and Table1 first row: for every real x>=2,

    |psi(x)-x|<=9.39*x*(log x)^1.515
                          *exp(-0.8274*sqrt(log x)).     (2)

This is an unconditional cited theorem, including its computational
inputs; those are not independently rerun here. In particular psi
contains all prime powers, not just primes. The pinned v2 constant
is 9.39. No stronger half-plane estimate is substituted for (2).

Import the finite polynomial identity
[NIST DLMF18.5.12](https://dlmf.nist.gov/18.5.E12), specialized
to degree n-1 and parameter1:

    ell_n(u)=sum_(j=0)^(n-1) binom(n,j+1)*(-u)^j/j!.    (3)

It is valid globally in u, with no oscillatory-range restriction.
Termwise differentiation of this finite polynomial suffices below;
it also agrees with
[DLMF18.9.23](https://dlmf.nist.gov/18.9.E23).

Import finite Abel summation, Tom M. Apostol, *Introduction to
Analytic Number Theory*, Springer1976, Theorem4.2. Its real-endpoint
formula and complete proof were inspected in Tristan Shin,
[*Math104B: Discussion Section3*, 23 January2025, pp1-2](https://cseweb.ucsd.edu/~dakane/Math104B/Discussion3.pdf):

    sum_(a<m<=b) Lambda(m)f(m)
      =psi(b)f(b)-psi(a)f(a)-integral_a^b psi(t)f'(t)dt. (4)

Here 1<a<=b are real and f is C^1 on [a,b]. The left endpoint is
excluded and the right endpoint fully included, also at integers.
The degenerate case a=b is zero on both sides.

These are precisely the tools approved in
drafts/literature/2026-11-10-prime-laguerre-cauchy-tail-review-224.md.
Their assembly is needed because none of the inspected statements
directly specifies this n-dependent cutoff. We reprove no PNT or
Laguerre identity, only the elementary bounds and compensation
needed for the specialization. No unread or retracted truncation
claim is imported.

### Finite compensation, including both boundary terms

Put R(t)=psi(t)-t and f_n(t)=ell_n(log t)/t. This weight is C^1
for t>1, and

    f_n'(t)=[ell_n'(log t)-ell_n(log t)]/t^2.           (5)

Subtract integral_a^b f_n(t)dt from (4). The ordinary integration
by parts identity

    b*f_n(b)-a*f_n(a)-integral_a^b t*f_n'(t)dt
      =integral_a^b f_n(t)dt

cancels exactly the contribution of t in psi(t)=t+R(t). Therefore

    P_n(b)-P_n(a)=R(b)f_n(b)-R(a)f_n(a)
                         -integral_a^b R(t)f_n'(t)dt. (6)

This is a finite identity for arbitrary real endpoints. No limit,
contour argument, or prime-power half-weight is used. In particular
at a prime power a its full term cancels in the difference; at a
prime power b the term is included fully. Values at the jump points
in the integral have measure zero and do not alter the boundary
values in (6).

### Global polynomial and PNT envelopes

For u>=1 the nonnegative coefficient sum in (3) gives

    |ell_n(u)|<=2^n*u^(n-1),
    |ell_n'(u)|<=(n-1)*2^n*u^(n-2).

Indeed 1/j!<=1 and sum_(j=0)^(n-1) binom(n,j+1)=2^n-1;
for the derivative also j<=n-1 and u^(j-1)<=u^(n-2)
for every term with j>=1. Since u>=1 and n<=k,

    |ell_n'(u)-ell_n(u)|<=k*2^n*u^(n-1).              (7)

For t>=e, set u=log t>=1. By (2), 9.39<10,
u^1.515<=u^2 and 0.8274>4/5, so

    |R(t)|<=10*t*u^2*exp(-4*sqrt(u)/5).               (8)

Combining (5), (7), (8), and the first polynomial bound gives

    |R(t)f_n(t)|<=10*2^n*u^k*exp(-4*sqrt(u)/5),
    |R(t)f_n'(t)|dt
       <=10*k*2^n*u^k*exp(-4*sqrt(u)/5)du,           (9)

where dt/t=du. These inequalities hold pointwise even at prime
powers; no derivative of the discontinuous function R is taken.

### Uniformity for all upper endpoints

Since k>=3 and U=V^2 with V=100*k^2, the logarithmic derivative
of h(u)=u^k*exp(-4*sqrt(u)/5) satisfies, for u>=U,

    h'(u)/h(u)=[k-(2/5)*sqrt(u)]/u<0.

Consequently both endpoint terms in (6), for a=X_n and b=Y,
are bounded by 10*2^n*U^k*exp(-4*V/5).

For the integral term, substitution v=sqrt(u) gives

    integral_U^infinity h(u)du
      =2*integral_V^infinity v^(2*k+1)*exp(-4*v/5)dv.

For g(v)=v^(2*k+1)*exp(-4*v/5) and v>=V,

    g'(v)/g(v)=(2*k+1)/v-4/5
       <=3*k/(100*k^2)-4/5<=-2/5.

Integrating this differential inequality on finite intervals gives
g(v)<=g(V)*exp(-2*(v-V)/5). Hence the improper integral exists and

    integral_U^infinity h(u)du
       <=5*V^(2*k+1)*exp(-4*V/5).                    (10)

Apply (9)-(10) to the finite identity (6), retaining both boundary
terms and bounding the finite integral by its nonnegative infinite
majorant. For every real Y>=X_n this yields

    |P_n(Y)-P_n(X_n)|
       <=10*2^n*V^(2*k)*(2+5*k*V)*exp(-4*V/5).       (11)

Thus all-Y uniformity has been proved before any numerical bound
on the final expression; fixed-n convergence is not substituted
for the requested uniform estimate.

### Explicit constants for every n>=2

Since V=100*k^2 and k>=3,

    2+5*k*V=2+500*k^3<=1000*k^3.

The right side of (11) is therefore at most

    B_k=10000*2^n*k^3*(100*k^2)^(2*k)*exp(-80*k^2).

Use log2<1, log100<5, log10000<10, and log k<=k for k>=1.
For completeness, e>1+1+1/2+1/6=8/3, and
(8/3)^5=32768/243>100; this certifies log100<5 and hence
log10000<10. The inequality log k<=k follows, for k>=1,
from integral_1^k dt/t<=k-1. Recalling n=k-1<k gives

    log B_k
       =log10000+n*log2+3*log k
                       +2*k*log100+4*k*log k-80*k^2
       <=10+14*k-76*k^2
       <=-70*k^2.

The last inequality is exactly

    6*k^2-14*k-10
      =2+22*(k-3)+6*(k-3)^2>=0,      k>=3.

Exponentiating proves (1). The actual certified bound is at most
exp(-630) for all n>=2, versus the required threshold1. No floating
point calculation, finite sample of n, or finite prime table is
part of this proof. No independent signed bound or RH consequence
has been established.

### Independent audit — step227, 10 November2026

The audit replays the whole proof above using review224's unchanged
source contracts. It finds no failed inequality or missing local
mathematical premise. In particular:

1. In (4), taking the difference of the two full-cutoff sums gives
   exactly a<m<=b. Subtracting the two compensating integrals leaves
   integral_a^b f_n. Ordinary integration by parts cancels the t
   contribution including both endpoints, giving the minus sign on
   integral R*f_n' in (6). Neither continuity nor differentiability
   of R is needed. This covers prime powers at either endpoint and a=b.
2. The degree is n-1. For u>=1 the absolute coefficient sum is at most
   2^n*u^(n-1), and the differentiated sum is at most
   (n-1)*2^n*u^(n-2). Their sum is at most n*2^n*u^(n-1),
   hence certainly the k*2^n envelope in (7). The PNT factor u^2
   gives exponent (n-1)+2=k in both lines of (9). The integral
   measure is dt/t=du; no power of t or u is omitted.
3. On u>=U=V^2 the numerator of h'/h is at most k-40*k^2<0.
   On v>=V=100*k^2, (2*k+1)/v<=3/(100*k)<=1/100, so
   g'/g<=-79/100<=-2/5. The factor2 from du=2*v*dv times
   the exponential integral5/2 gives exactly5 in (10). Two endpoint
   bounds and the integral multiplier k give 2+5*k*V in (11).
   Only a nonnegative majorant is extended to infinity; the bound
   holds for each finite real Y, uniformly in Y.
4. Since 2+500*k^3<=1000*k^3 for k>=3, the logarithm is at most
   10+k+3*k+10*k+4*k^2-80*k^2=10+14*k-76*k^2.
   Its excess over -70*k^2 is -(6*k^2-14*k-10), at most -2
   for k>=3 by the exact expansion in the proof. The elementary
   logarithm bounds used there are valid. No finite numerical sample
   replaces the all-integer check.

The result is the original bound, not an additional sign theorem or
a sharper cutoff. The imported PNT theorem and its computational
inputs remain cited inputs, not independently verified computations.
The audit neither identifies the limit with S_f nor licenses an
exchange of the n and prime-cutoff limits. No DAG edge changes arise.

## Mathlib

Full matching coverage of this compensated statistic, the explicit
Johnston-Yang bound and this all-n cutoff is not checked and is
unknown. No absence claim is made. DLMF supplies the finite
polynomial identities and Apostol supplies finite summation by
parts as mathematical references; no Lean formalization or Mathlib
theorem identification is asserted.

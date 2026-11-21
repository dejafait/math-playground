# Lemma 986: a uniform proper-prime-power Laguerre majorant

## Hypotheses

Let n>=2 be an integer and X>=2 be real. Use the ordinary generalized
Laguerre polynomials and the actual primes. Define

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u),
    R_n(X)=sum_(p prime,a>=2,p^a<=X)
                       (log p)*|K_n(a*log p)|/p^a.

Here a is an integer, each endpoint p^a=X is included fully, and an
empty sum is zero. This R_n denotes only this positive majorant,
not other residuals denoted R_n elsewhere in the notebook. For the
cutoff specialization put X_n=exp(10000*(n+1)^4).

No RH, zero simplicity, PNT estimate, prime cancellation, asymptotic
Laguerre formula or exchange of growing-degree limits is assumed.

## Conclusion

There is one absolute constant, independent of n and X, namely 24,
such that

    R_n(X)<=n*((log X)^2/4+24)
           <=24*n*(1+(log X)^2).                         (1)

Consequently

    R_n(X_n)<=24*n*(1+10^8*(n+1)^8)
             <=24*(1+10^8)*(n+1)^9.                     (2)

For every epsilon>0, uniformly for all n>=2,

    R_n(X_n)<=C_epsilon*exp(epsilon*n),
    C_epsilon=24*(1+10^8)*9!*exp(epsilon)/epsilon^9.     (3)

This pays the entire proper-power component of the common-cutoff
degree average, with the original compensator retained. It does not
bound the remaining signed prime-minus-compensator observable or
establish L984(H). Written in step245, 10 November2026, under the
pre-existing SPECIALIZE assessment review244. Classification:
REPRODUCTION, an elementary arithmetic specialization of the cited
global inequality, not a mathematical discovery beyond that source.
No separate critical audit of this new proof is claimed.

## Proof

### Imported global inequality and finite degree average

Import [NIST DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), live
statement inspected in review244 on 10 November2026: for integer
d>=0, alpha>=0 and real u>=0,

    exp(-u/2)*|L_d^(alpha)(u)|<=L_d^(alpha)(0)
                                      =(alpha+1)_d/d!.

DLMF attributes the bound to T. H. Koornwinder, *The addition
formula for Laguerre polynomials*, SIAM J. Math. Anal. **8** (1977),
535-540, Remark4.1. The DLMF statement is the imported theorem;
Koornwinder's original proof was not separately inspected. We do not
reprove this inequality. The only derivation needed is its finite
degree-average and positive-sum arithmetic specialization; the source
does not state this n-dependent arithmetic sum.

For every 2<=k<=n, take d=k-1>=1 and alpha=1. Then
L_(k-1)^(1)(0)=(2)_(k-1)/(k-1)!=k. Triangle inequality gives,
for every u>=0,

    |K_n(u)|<=exp(u/2)*(sum_(k=2)^n k)/(n-1)
             =((n+2)/2)*exp(u/2)
             <=n*exp(u/2).                              (4)

The equality uses sum_(k=2)^n k=(n-1)*(n+2)/2; the final inequality
holds also at n=2. For p prime and integer a>=2, u=a*log p>0, so

    (log p)*|K_n(a*log p)|/p^a
                         <=n*(log p)/p^(a/2).           (5)

This is global in u; no range between the bulk and X_n is omitted.

### Squares, including small cutoffs

Set y=sqrt(X)>1 and M=floor(y). If M=1 the square contribution is
empty. Otherwise positivity, log p<=log y, and inclusion of primes
among integers give

    sum_(p<=y) (log p)/p
       <=(log y)*sum_(m=2)^M 1/m
       <=(log y)*integral_1^M dt/t
       <=(log y)^2=(log X)^2/4.                         (6)

For each m>=2 the integral over [m-1,m] of 1/t is at least 1/m,
proving the middle inequality without a prime-distribution input.
If M=1, (6) still holds with left side zero. If y is a prime, it
appears fully in the first sum; all inequalities include equality
endpoints. By (5), n times (6) bounds exactly the a=2 part of R_n.

### All higher exponents and convergence of their majorant

For each prime p>=2, the nonnegative geometric series gives

    sum_(a=3)^infinity p^(-a/2)
       =p^(-3/2)/(1-p^(-1/2))<4*p^(-3/2).              (7)

Indeed p^(-1/2)<=1/sqrt(2)<3/4, the last strict inequality following
by squaring 1/2<9/16. Thus 1/(1-p^(-1/2))<4.

The following integral comparison supplies convergence before any
infinite rearrangement is used. For m>=2 and t in [m-1,m],
t>=1, m<=2*t, and t<=m, so

    (log m)/m^(3/2)<=(log t+log 2)/t^(3/2).

Integrate on each unit interval and sum over finitely many m. The
improper integral is finite, with

    sum_(m=2)^infinity (log m)/m^(3/2)
       <=integral_1^infinity (log t+log 2)*t^(-3/2)dt
       =4+2*log 2<6.                                   (8)

For the evaluation put t=exp(v), obtaining the integrals of
v*exp(-v/2) and exp(-v/2) on [0,infinity), equal to 4 and 2.
Integration by parts evaluates the former; its boundary term tends
to zero, for instance from exp(v/2)>=v^3/48 as v tends to infinity.
Also log 2=integral_1^2 dt/t<1. Monotone partial sums and (8)
justify the asserted convergence.

To bound the finite a>=3 contribution in R_n(X), first apply (5),
then extend the exponent sum for each of its finitely many primes
using (7), then extend the resulting nonnegative prime sum to all
integers using (8). This gives

    sum_(p prime,a>=3,p^a<=X)
                  (log p)*|K_n(a*log p)|/p^a
       <=4*n*sum_(m=2)^infinity (log m)/m^(3/2)<24*n.   (9)

Every extension is of nonnegative sums bounded by the convergent
majorant (8). No conditionally convergent double sum is interchanged.
Equations (6) and (9) prove (1). In particular no higher exponent
or prime-power jump was dropped.

### Exact cutoff and unchanged arithmetic interface

At X=X_n, (log X_n)^2=10^8*(n+1)^8. Substitute this in (1) and
use n<=n+1 and 1<=(n+1)^8 to get (2). For epsilon>0 the positive
exponential series gives

    exp(epsilon*(n+1)) >= epsilon^9*(n+1)^9/9!.

Combine this with (2) to prove (3). The constants are finite for
each epsilon>0 and cover every integer n>=2, not just an eventual
subsequence.

For clarity, the finite arithmetic interface can be written without
using any local lemma's mathematical conclusion. With Lambda the
actual von Mangoldt function, define

    A_n(X)=sum_(2<=m<=X) Lambda(m)*K_n(log m)/m
                                      -integral_0^(log X) K_n(u)du,
    A_n^prime(X)=sum_(p prime,p<=X) (log p)*K_n(log p)/p
                                      -integral_0^(log X) K_n(u)du,
    E_n(X)=sum_(p prime,a>=2,p^a<=X)
                                  (log p)*K_n(a*log p)/p^a.

Finite averaging in k and u=log x identify A_n(X) with exactly
(n-1)^(-1)*sum_(k=2)^n P_k(X) as defined in L981/L982. Every integer
m with Lambda(m) nonzero is a unique prime power p^a, with weight
log p. Splitting a=1 from a>=2 therefore gives the finite identity

    A_n(X)=A_n^prime(X)+E_n(X),
    |E_n(X)|<=R_n(X).                                   (10)

The compensating integral is identical on both sides, including
its lower endpoint 0, corresponding to x=1. No continuum density
has been assigned to proper powers. At a real endpoint that is a
prime power, the whole term belongs to exactly one of the two
finite arithmetic sums. This also handles n=2 and X<4, when E_n
is zero. At X_n, (3) and (10) show that removing proper powers
costs at most an every-epsilon subexponential error. They supply
no independent upper bound for A_n^prime(X_n); L984(H), the dense
interior prime block and both complementary ranges remain open.
L981/L982 here provide notation only; their tail and identification
theorems, and L984's conditional implication, are not proof inputs.

## Mathlib

Full matching Mathlib coverage of the imported global Laguerre
inequality, this proper-power statistic and its uniform arithmetic
bound has not been checked and is unknown. No theorem-absence,
formalization or independent computational certification is claimed.
The precise external mathematical input is DLMF18.14.8 above;
the remaining arguments are finite algebra, geometric series and
elementary integral comparison.

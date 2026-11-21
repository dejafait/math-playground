# Lemma 924: an absolute lower bound for the critical logarithmic gcd form

## Hypotheses

Let N>=2 be an integer, let c=(c_1,...,c_N) be any complex vector,
and use natural logarithms. For a real A define the unchanged finite
form of L737 (5):

    F_A(c)=sum_(m,n<=N) c_m conjugate(c_n) gcd(m,n)/sqrt(m*n)
                         *[A+2 log gcd(m,n)-log m-log n].

Write phi for Euler's totient, with phi(1)=1, and Lambda for the von
Mangoldt function, with Lambda(1)=0. Set

    b_n=c_n/sqrt(n),
    B_d=sum_(k<=N/d) b_(dk),
    C_d=sum_(k<=N/d) b_(dk) log k,
    Q(c)=sum_(d<=N) phi(d)|B_d|^2,
    kappa(d)=sum_(p|d) log p/(p-1),  kappa(1)=0.

All displayed finite sums have integer indices. Cutoffs such as N/d
are real, and a sum with no admissible index is zero. Only L737's
finite divisor identities (6)–(8), totient comparison in (9), finite
Schur argument and inversion in (11) are used. Its Hardy-function,
height, bump, moment and multiplier-length assumptions are not used:
the cited finite identities were proved there for arbitrary finite
vectors and do not depend on those analytic assumptions.

The sole additional standard input is the first Mertens estimate:
Terence Tao, *254A, Notes 1: Elementary multiplicative number theory*,
23 November 2014, Section 2, Theorem 13,
[primary source](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/):

    sum_(n<=x) Lambda(n)/n = log x+O(1),  real x>=1.

The absolute constant has no N, d or coefficient dependence. Fix any
nonnegative absolute M such that the upper bound is log x+M for all
real x>=1. If O(1) is expressed only beyond an absolute onset, increasing
M covers the remaining compact interval: its finite sum is bounded
by the sum at that onset and log x>=0. No numerical value of M is
asserted. The inspected theorem and proof are recorded in
drafts/literature/2026-11-09-logarithmic-gcd-row-sum-review.md, whose
invocation-start SPECIALIZE coverage authorizes this exact application.
Mertens' theorem is imported, not reproved. No conclusion from the
partially extracted Goldfeld display is needed.

## Conclusion

With the single nonnegative absolute constant

    C_* = M+3 log 2+2,

every integer N>=2 and every complex c satisfy

    F_(2 log N)(c) >= -C_* Q(c).                            (1)

Q(c)>0 whenever c!=0; for c=0 both sides vanish. The same C_* works
for every real cutoff occurring in the proof. This is an additive
lower bound relative to Q, not a claim that the form is nonnegative
or that the constant is optimal. In particular it supplies no improved
coefficient-conditioning bound, longer-dictionary projection estimate,
microscopic realization, signed transfer or actual-Xi positivity.

This is a local specialization of standard Mertens theory and the
existing finite Schur argument, classified REPRODUCTION. The reviewed
sources do not state the full-form conclusion, but no originality
beyond those sources is claimed. Written 9 November 2026, step228;
independent finite audit completed in step230 below. RH remains unresolved.

## Proof

### 1. All prime powers and all real cutoffs

For each prime p and integer k>=1,

    1/phi(p^k)-1/p^k = 1/(p^k*(p-1)).

Since Lambda is supported on prime powers, for any real x>=1,

    0 <= sum_(2<=r<=x) Lambda(r)/phi(r)
           -sum_(2<=r<=x) Lambda(r)/r
       = sum_(p^k<=x) log p/(p^k*(p-1))
       <= sum_p log p/(p-1)^2.                             (2)

The last expression bounds each finite correction. To justify its
finiteness explicitly, p-1>=p/2 and positivity imply

    sum_p log p/(p-1)^2
      <=4 sum_(n=2)^infinity log n/n^2
      <=4[log 2/4+integral_2^infinity (log t)/t^2 dt]
      =3 log 2+2.                                         (3)

Here (log t)/t^2 is positive and decreasing for t>=2, so its integral
bounds the terms starting at n=3; the integral is (log 2+1)/2.
The prime-power geometric series in (2) sums to 1/(p-1) before the
outer factor 1/(p-1). Nonnegative partial sums and (3) justify this
majorization; no conditionally convergent rearrangement is used.

Importing the upper side of Mertens' theorem and adding (2)–(3) gives

    S_phi(x):=sum_(2<=r<=x) Lambda(r)/phi(r)
           <=log x+C_* ,  real x>=1.                       (4)

For 1<=x<2 the left side is zero and the asserted upper bound is
nonnegative. Thus (4) includes empty rows as well as all prime powers;
no integral-cutoff replacement or small-x exception is implicit.

### 2. The unchanged weighted Schur interface

L737 (6)–(7) give the exact identities

    F_A(c)=sum_(d<=N) phi(d)
        [(A+2*kappa(d))|B_d|^2-2 Re(C_d conjugate(B_d))],
    C_d=sum_(2<=r<=N/d) Lambda(r) B_(dr).                   (5)

These retain both logarithmic cross terms and are valid for complex
coefficients. On Euclidean coordinates y_d=sqrt(phi(d)) B_d the
second identity is the matrix K of L737, with

    K_(d,n)=Lambda(n/d) sqrt(phi(d)/phi(n)) if d|n and n>d,
    K_(d,n)=0 otherwise;  h_d=1/sqrt(phi(d)).

Put ell=log N>0. The weighted column identity L737 (8) is

    sum_d K_(d,n) h_d/h_n = log n <=ell.                   (6)

In particular the column n=1 is zero. For every d<=N its row is

    sum_n K_(d,n) h_n/h_d
       =sum_(2<=r<=N/d) Lambda(r) phi(d)/phi(dr)
       <=sum_(2<=r<=N/d) Lambda(r)/phi(r)
       <=log(N/d)+C_* <=ell+C_*.                          (7)

The first inequality uses exactly phi(dr)>=phi(d)phi(r), including
shared prime factors, as proved in L737 (9); the second is (4).
When N/d<2 the original row is empty and the same inequalities hold.
All weights h_d are strictly positive. The finite Schur estimate
proved in L737, with row bound R=ell+C_* and column bound S=ell,
therefore gives for every complex y

    ||Ky||_2 <=sqrt(ell*(ell+C_*)) ||y||_2.                (8)

Consequently the full complex inner product satisfies

    |sum_d phi(d) C_d conjugate(B_d)|
       <=sqrt(ell*(ell+C_*)) Q(c).                        (9)

Only the nonnegative matrix K was bounded entrywise; no sign was
assigned to c_m conjugate(c_n) or to the cross term in (5).

### 3. The additive remainder at the critical coefficient

For ell>=0 and C_*>=0,

    (ell+C_*/2)^2-ell*(ell+C_*)=C_*^2/4>=0,

so sqrt(ell*(ell+C_*))<=ell+C_*/2. Set A=2 ell in (5).
By kappa(d)>=0 and (9),

    F_(2 ell)(c)
      >=[2 ell-2 sqrt(ell*(ell+C_*))]Q(c)
          +2 sum_d phi(d) kappa(d)|B_d|^2
      >=-C_* Q(c).                                       (10)

This is (1) with one constant independent of N,d,c. The nonnegative
kappa contribution was retained until the final lower bound; no
boundedness assumption on kappa was made. The zero vector requires
no division and satisfies (10). If Q(c)=0, positivity of phi(d)
forces every B_d=0. The finite inversion from L737 (11),
b_n=sum_(k<=N/n) mu(k)B_(nk), then forces every c_n=0. Thus Q is
strictly positive for every nonzero vector, without assuming a
coefficient-independent spectral lower bound relative to ||c||_2^2.

The required threshold is an N-independent lower bound for F/Q,
and (10) supplies -C_*. The older dyadic positive trial quotients
are not used. No moment estimate or conclusion about zeros follows
from this finite arithmetic argument alone.

### Independent finite audit — 9 November 2026, step230

The approved scope is exactly (1), not a new coefficient threshold or
observer theorem. Reused the primary-source inspection in the saved
November9 audit assessment: Tao, Section 2, Theorem 13, equation (22),
has the von Mangoldt numerator (all prime powers), denominator n and
real x>=1. Its absolute O(1) supplies a single nonnegative M; neither
an asymptotic depending on d nor an explicit numerical M is needed.
No additional source hypothesis or inaccessible Goldfeld display is
used. This audit imports that theorem without reproving it.

**Divisor identities and scope.** Replayed L737 (5)–(11) and the
relevant step261 audit. For q=gcd(m,n), the finite Jordan-totient
identity sum_(d|q)J_z(d)=q^z gives sum_(d|q)phi(d)=q and
sum_(d|q)phi(d)(log d+kappa(d))=q log q. The derivative of
log(1-p^(-z)) at z=1 is +log p/(p-1). Thus the two log d terms
from 2 log q cancel the corresponding parts of log m+log n;
the two remaining sums are C_d conjugate(B_d) and its conjugate.
This verifies the first identity (5), including its sign and factor 2.
For the second identity, the coefficient of b_(dk) in its right side
is sum_(r|k,r>=2)Lambda(r)=log k, including k=1 where both vanish.
These statements concern arbitrary finite complex vectors. No Hardy
function, moment estimate, weight or multiplier length from L737 is
needed, so L737 is the only direct local mathematical input.

**Prime powers and cutoffs.** Since phi(p^k)=p^(k-1)(p-1), the
positive difference of reciprocals in (2) is exactly
1/(p^k(p-1)), for every k>=1, including p=2. Summing the full
geometric majorant over k gives 1/(p-1)^2. The derivative of
f(t)=log t/t^2 is (1-2 log t)/t^3<0 for t>=2. Hence
sum_(n>=2)f(n)<=f(2)+integral_2^infinity f(t)dt, with integral
(log 2+1)/2, and multiplication by 4 gives exactly 3 log 2+2.
Nonnegative terms justify the infinite majorant, with no exchange of
conditionally convergent sums. Adding M gives (4) at every real x>=1;
when x<2 the sum is empty. This is one constant for every N/d, not
an asymptotic valid only along integer or large cutoffs.

**Weighted orientation and complex vectors.** For n=dr, direct
multiplication gives K_(d,n)h_d/h_n=Lambda(r) in a column and
K_(d,n)h_n/h_d=Lambda(r)phi(d)/phi(dr) in a row. Divisors of n
therefore give the exact column log n; n=1 has a zero column.
The Euler-product ratio phi(dr)/(phi(d)phi(r)) is the product
of p/(p-1) over shared prime factors, hence is at least 1.
Consequently each row is bounded by S_phi(N/d), with the empty
row handled by the same real-cutoff estimate.

In the finite weighted Cauchy–Schwarz proof, sum_n K_(d,n)h_n
is at most R h_d and sum_d K_(d,n)h_d is at most S h_n.
Thus summing |(Ky)_d|^2<=R h_d sum_n K_(d,n)|y_n|^2/h_n
gives ||Ky||^2<=RS||y||^2, with R=ell+C_* and S=ell.
Here Ky has coordinates sqrt(phi(d))C_d and ||y||^2=Q.
Ordinary complex Cauchy–Schwarz proves (9); no entrywise sign of
the original coefficient products is required.

**Uniform remainder and nondegeneracy.** Both sides of
sqrt(ell(ell+C_*))<=ell+C_*/2 are nonnegative, so squaring is
legitimate and their squared difference is C_*^2/4. Inserting
this bound in the exact full form gives (10), after dropping only
the nonnegative kappa contribution. No division by Q is used.
If Q=0 every B_d vanishes; in sum_k mu(k)B_(nk), the coefficient
of b_(nr) is sum_(k|r)mu(k), proving the finite inversion and c=0.
This proves strict positivity of Q for c!=0, not a condition-number
bound. The zero vector satisfies all displayed inequalities directly.

Audit result: (1) and its stated C_* pass for every N>=2 and every
complex vector, with no correction to the theorem or its argument.
This establishes local reliability of the existing specialization,
not a new theorem beyond the checked sources or an RH candidate.
The parked dyadic trials are unnecessary and remain inconclusive
as spectral lower bounds. Conditioning, charged moment remainders,
realization and signed positivity remain unresolved. Matching
Mathlib coverage is still unchecked. No new dependency, mathematical
script, coefficient threshold or analytic interchange was introduced.

## Mathlib

Full matching coverage for (1), the first-Mertens input, and the
totient-weighted row specialization has not been checked and is
unknown. No absence claim is made. Supporting mathematics is finite
divisor inversion, a geometric series, an integral comparison and the
weighted Schur/Cauchy–Schwarz argument already proved in L737. No
specific Mathlib declaration is imported. The standard analytic input
has its precise primary citation above; the necessary specialization
and all uniformity qualifications are proved here.

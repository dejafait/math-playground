# Lemma 602: actual-theta normalized overlap passes the fourth-jet test

## Hypotheses

Use the actual even theta kernel k of L019/L239, with the full-line
normalization of L233:

    a(t)=A(t)=integral_R s^2 k(s+t)k(s-t) ds,
    b(t)=C_k(2t)=integral_R k(s+t)k(s-t) ds,
    V(t)=a(t)/b(t),  t real.

The equality defining b follows by v=s-t in L233's definition of C_k.
Here A is the associated kernel, not the auxiliary theta function called
A in L019/L239. No RH, zero-simplicity or positive-definiteness hypothesis
is imposed on V.

## Conclusion

The denominator is strictly positive for every real t; V is real, even
and smooth, with V(0)>0. In this normalization,

    0.11144 < V(0)V''''(0)-V''(0)^2 < 0.11170.

Thus actual V passes this one necessary condition for positive
definiteness. This does not prove positive definiteness of V, positivity
of L233's first spectrum at all frequencies, higher associated signs or RH.
It does not stop the factor mechanism.

## Proof

### Applicability and differentiated integrals

L019 gives k(u)>0 for u>=0, and L239 gives its even holomorphic
continuation to |Im z|<pi/4. In particular k is strictly positive on R.
The strip estimate in L239, combined with Cauchy's derivative estimate
on circles of any fixed radius r with 0<r<a<pi/4, gives, for each fixed j,

    |k^(j)(u)| <= C_(a,r,j) exp(9(|u|+r)/2)
                   exp(-pi cos(2a) exp(2(|u|-r))).

Indeed the real part on the circle differs from u by at most r, and
L239's bound is even in that real part; enlarging the finite constant
also covers |u|<=r. For |t|<=T the same estimate for k^(j)(s+t) is
bounded by a constant times exp(9(|s|+T+r)/2) times
exp(-pi cos(2a) exp(2(|s|-T-r))). This is integrable after multiplication
by any fixed polynomial in s. Products of any fixed derivatives admit
the same kind of integrable bound. Dominated differentiation therefore
applies to a and b to every finite order, locally uniformly in t.

The positive integrand defining b implies b(t)>0. Both integrals are
real and even in t, and a(0)>0 since s^2 k(s)^2 is positive off zero.
Hence V is smooth, real and even, with positive value at zero. This
requires no complex zero-free statement about b.

Write k_j=k^(j)(s). Differentiating in t at zero gives

    q_0=k_0^2,
    q_2=2k_0k_2-2k_1^2,
    q_4=2k_0k_4-8k_1k_3+6k_2^2.

For j=0,2,4 put b_j=integral_R q_j(s) ds and
a_j=integral_R s^2 q_j(s) ds. These are b^(j)(0), a^(j)(0).
All these integrands are even in s. The factor 2 in C_k(2t) has already
been included by differentiating the symmetric shifts; no additional
chain factor is to be inserted. With v_j=V^(j)(0), the identity a=bV
and evenness give exactly

    v_0=a_0/b_0,
    v_2=(a_2-v_0 b_2)/b_0,
    v_4=(a_4-v_0 b_4-6v_2 b_2)/b_0.                 (1)

### Complete derivative series and omitted theta modes

For u>=0 define v_n=pi n^2 exp(2u). Termwise differentiation of L019's
locally uniformly convergent series, justified also by L239, gives

    k^(j)(u)=exp(u/2) sum_(n>=1) P_j(v_n) exp(-v_n),
    P_0(v)=8v^2-12v,
    P_(j+1)(v)=(1/2-2v)P_j(v)+2v P'_j(v).        (2)

P_j has degree j+2. Let M_j be the sum of absolute coefficients of P_j.
For j=0,...,6 the exact recurrence gives

    (M_0,...,M_6)=(20,106,661,9445/2,151269/4,
                   2672213/8,51450613/16).

Consequently |P_j(v)|<=M_j v^(j+2) for v>=1. The certificate stores
every coefficient, not just these sums.

On 0<=u<=2 retain n=1,...,4. For n>=5, pi>3 implies v_n>=3n^2>=75.
For d=j+2<=8, x^d exp(-x) decreases on x>=75, while exp(u/2)<=e<3.
The absolute omitted derivative series is therefore at most

    3 M_j sum_(n>=5) (3n^2)^d exp(-3n^2)
      <= E_j := 6 M_j 75^d exp(-75).              (3)

For the last inequality, successive terms have ratio at most
(6/5)^(2d) exp(-33)<1/2. All seven ratio bounds and E_j are enclosed
in the certificate. In particular E_6<5.174e-11, and E_4<1.082e-16.
The omitted modes are added as symmetric error intervals to each k_j
before forming products; their cross terms are thus included.

### Unbounded real-variable tail

For u>=2 and d=j+2, the bound
x^d exp(-x/2)<=(2d)^d for x>=0 follows by maximizing that function.
Using pi>3 in the remaining exponential and a geometric bound gives

    |k^(j)(u)| <= H_j exp(u/2) exp(-3 exp(2u)/2),
    H_j=2 M_j (2(j+2))^(j+2).                    (4)

In detail the sum of exp(-3 n^2 exp(2u)/2), n>=1, is at most twice
its first term: the successive ratio is at most
exp(-9 exp(4)/2)<exp(-243)<1/2, since exp(4)>54.

Write q_j as sum_(a,b) c_(a,b) k_a k_b, combining equal unordered
pairs exactly. Define T_j=sum |c_(a,b)| H_a H_b. Equations (4) imply
|q_j(u)|<=T_j exp(u) exp(-3exp(2u)). For m=0,2 and u>=2,
u^m<=exp(u) (for m=2, u^2 exp(-u) decreases from 4/e^2<1).
Thus the full two-sided omitted integral satisfies

    2 integral_2^infinity u^m |q_j(u)| du
      <= (T_j/3) exp(-3exp(4))
       < (T_j/3) exp(-162).                      (5)

This uses the exact substitution y=exp(2u). The respective certified
upper bounds for j=0,2,4 are less than
6.020e-66, 1.635e-61 and 1.192e-56. They cover both a_j and b_j and
include every theta mode. No finite truncation is used on this tail.

### Certified integration on [0,2]

Divide [0,2] into 1024 equal cells, h=1/512. For a C^2 function f on
a cell with midpoint c, Taylor's integral remainder gives

    integral_cell f(s)ds in h f(c)+(h^3/24) range_cell(f'').   (6)

To see the enclosure, write the second-order remainder as an integral
of f'' along the segment from c to s; its weight is nonnegative on
either side, the linear term integrates to zero, and the total weight
is h^3/24. This argument applies without assuming a sign for f''.

For j=0,2,4 and r=0,1,2 the exact derivatives used to bound f'' are

    q_j^(r)(s)=sum_(l=0)^j sum_(h=0)^r
       (-1)^l binom(j,l) binom(r,h)
       k_(j-l+h)(s) k_(l+r-h)(s).

For f=q_j use f''=q_j''; for f=s^2 q_j use
f''=2q_j+4s q_j'+s^2 q_j''. Thus derivatives only through k_6 are
needed. Evaluate (2) with n<=4 on each entire cell, add (3), and use
these polynomial product formulas to enclose f''. Evaluate f(c)
separately at the exact dyadic midpoint, again adding (3). Sum (6),
multiply by 2 for evenness, and finally add the symmetric errors (5).

The reproducible implementation is
`scripts/normalized-overlap/fourth_jet_certificate.py`; run

    python3 scripts/normalized-overlap/fourth_jet_certificate.py --cells 1024

It writes the full certificate
`scripts/normalized-overlap/fourth-jet-certificate.json` and prints the
determinant enclosure, required threshold, failures and artifact path.
Arithmetic uses Python Decimal with 45 significant digits: addition,
multiplication and division are rounded outward in both directions;
negation uses exact sign copying, not ambient-context unary rounding.
Decimal exponential is correctly rounded to nearest; its two neighboring
decimals enclose the exact result. Exponential monotonicity extends this
to interval arguments. There is no binary floating-point arithmetic in
the certificate calculation. Fractions in (2) are exact rationals before
outward conversion. Pi is enclosed using Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), with 40 rational alternating-series
terms for each arctangent and the signed next-term error interval.
The resulting enclosure is contained in
[3.14159265358979323846264338327950288419716910,
 3.14159265358979323846264338327950288419716973].
The script checks pi>3, e<3, exp(4)>54, and both geometric-ratio tests.

The resulting full integrals lie inside these outward-rounded intervals:

| Integral | Lower bound | Upper bound |
| --- | ---: | ---: |
| b_0 | 1.2790067 | 1.2790078 |
| a_0 | 0.0314380452 | 0.0314381888 |
| b_2 | -52.22225085 | -52.22214368 |
| a_2 | -1.477098948 | -1.477085579 |
| b_4 | 6132.36717 | 6132.41176 |
| a_4 | 205.12350 | 205.12906 |

Apply (1) using the full certificate intervals, not the rounded table.
They give

    0.0245800275 < v_0 < 0.0245801583,
    -0.151271456 < v_2 < -0.151253494,
    5.46473483 < v_4 < 5.47503984,

and, by outward interval evaluation of v_0 v_4-v_2^2,

    [0.111440279693024071740668487883077875076364046,
     0.111699725815406230855769734184448542065713220].

This establishes the asserted strict inequalities. Full relevant
integral, jet, polynomial, rounding and tail fields were inspected;
the numerical preview is not an input. The certificate is a finite
arithmetic proof with the analytic error bounds above, subject to the
stated standard Decimal implementation contract; no formal verification
is claimed. The subsequent independent critical audit is recorded below.

### Exact scope of the imported necessity

J. Buescu and A. C. Paixao, *Real and complex variable positive definite
functions*, Sao Paulo J. Math. Sci. 6(2) (2012), 155-169, Proposition 2.5,
printed p.159, [primary PDF](https://revistas.usp.br/spjournal/en/article/download/74466/78087/100183):
if f:R->C is positive definite and C^(2n) near zero, then for
0<=m_1,m_2<=n and real x,

    |(-1)^m_2 f^(m_1+m_2)(x)|^2
       <= (-1)^(m_1+m_2) f^(2m_1)(0) f^(2m_2)(0).

With n=2, m_1=0, m_2=2, x=0 this gives
|f''(0)|^2<=f(0)f''''(0). V has the required local C^4 regularity
and is real, so if V were positive definite it would satisfy the
determinant inequality tested here. This is an import, not a reproof.
Its positive-definiteness premise remains unproved. A positive value
passes this test and establishes no spectral sign. L233's downstream
Fourier normalization and independent all-degree gap remain unchanged.

### Independent critical audit — 31 October 2026

Accepted within the stated finite, necessary-only scope. This audit read
the complete proof, implementation and load-bearing certificate fields,
and the relevant complete L019/L233/L239 proofs. It imports the necessity
above under its stated conditional premise; it does not assume that
premise for the computation or infer it from the result.

For regularity, L239's strip bound on the radius-r Cauchy circle gives
the displayed fixed-derivative bound, since the absolute real part lies
between max(0,|u|-r) and |u|+r. Translations in a fixed compact real
t interval preserve an integrable superexponential bound, including
polynomial weights and products. Thus all differentiations used here
are justified. Positivity of b is pointwise positivity of the integrand,
not a complex zero-free assertion. The symmetric shifts give q_2 and
q_4 exactly as stated; differentiating a=bV gives the coefficient 6
in (1). No further factor from C_k(2t) is missing.

Exact coefficient differentiation independently checks the nine q_j
expressions through two s derivatives. For example q_2''=2k_0k_4-2k_2^2
and q_4''=2k_0k_6-4k_1k_5-2k_2k_4+4k_3^2. Every stored P_j coefficient
and absolute coefficient sum agrees with (2). The geometric ratios in
(3) are all below 8.614e-14, hence below 1/2. Its majorant uses d<=8
and v_n>=75, exactly the needed monotonicity range. Adding symmetric
derivative intervals before products encloses all omitted cross terms.

For (4), maximizing x^d exp(-x/2) permits the weaker bound (2d)^d;
the omitted factor exp(-d) only enlarges it. The successive n ratio is
at most exp(-9 exp(4)/2)<exp(-243)<1/2. For both weights m=0,2,
u^m<=exp(u) on u>=2, and
2 integral_2^infinity exp(2u) exp(-3exp(2u))du
=exp(-3exp(4))/3. This confirms every constant in (5), both ends of
the line, and the applicability to every theta mode, not only n<=4.

For (6), Taylor's oriented integral remainder can be rewritten on each
side of the midpoint with nonnegative weight. Integration of this weight
is h^3/24; hence a range enclosure for f'' may be multiplied by this
positive scalar even when f'' changes sign. The complete-cell interval
evaluations, including k_6, bound that range. The factor 2 outside the
cell contribution accounts for evenness once. Both quadrature and real
tails are added before the quotient is evaluated.

The arithmetic review checked every operation in class I and its uses.
Integer-to-Decimal conversions are exact. Fraction coefficients are
converted by directed division. Endpoint sums and all four endpoint
products use explicit downward/upward contexts; copy_negate is exact.
Reciprocal endpoints are ordered by the decreasing function 1/x on an
interval avoiding zero, and subsequent multiplication is outward. The
only quotient denominator arising from the integral data is b_0, whose
lower endpoint is 1.27900676588693033390198811851062539321305763>0.
Integer powers use repeated enclosing products, so dependency can widen
but cannot invalidate an interval. Decimal exp is correctly rounded
to nearest under the imported implementation contract, regardless of
the context's directed setting; adjacent context numbers therefore
enclose the exact exponential. Monotonicity covers interval arguments.
For this run all endpoints are finite and all relevant exponent ranges
are well inside the contexts' default limits: 0<=u<=2, n<=4, pi<4 give
0<v_n<5184, using exp(4)<81. No binary floating-point value enters
these operations. The dyadic mesh and midpoints are exact at precision 45.

An independent exact-rational check encloses the two arctangent
remainders and their Machin combination inside the recorded pi interval.
The identity's tangent is exactly 1 by rational double-angle arithmetic;
its angle is in (0,pi/2), fixing the branch. Indeed atan(1/5)<1/5,
atan(1/239)<atan(1/5), so the angle is positive and below 4/5<pi/2.
Thus this check does not replace the arctangent remainder by a decimal
approximation. All six integral, six midpoint-error, four jet, seven
derivative-tail, seven ratio and three real-tail intervals were inspected
in full, as were the coefficient and pi fields.

Reproduction command, preserving the original certificate:

    python3 scripts/normalized-overlap/fourth_jet_certificate.py --cells 1024 --output scripts/normalized-overlap/fourth-jet-audit-replay.json

The replay used Python 3.15.0 and libmpdec 4.0.1. All original and replay
certificate fields match exactly, including every endpoint and an empty
failures list. Additional exact-rational/coefficient/replay checks are
saved in `scripts/normalized-overlap/fourth-jet-audit-checks.json`:
18 checks passed, no failures. The full decisive determinant interval is
the one displayed above; it lies strictly inside (0.11144,0.11170), and
its required necessary threshold is zero. This accepts the local
enclosure under the standard Decimal contract, with no formal library
verification, full positive-definiteness result, spectral sign theorem
or RH conclusion. No mathematical correction or new dependency was needed.

## Mathlib

Not checked for this exact quotient, enclosure, or supporting theta,
Cauchy-estimate, differentiated-integral, interval-arithmetic and
positive-definite derivative theorems. No matching theorem or absence
is asserted. The calculation specializes known methods; the source
assessment found no inspected evaluation of this actual scalar, which
does not certify novelty. No progress beyond the checked literature on
RH is claimed.

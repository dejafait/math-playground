# Lemma 223: unit-progression Bernoulli endpoint formula

**Hypotheses.** Use the exact functions and rounded endpoints of L220,
on the interior box A times J of L221, retaining all its c,d and
only pairs with gcd(a,m)=1. Let N be sufficiently large, v=cd,
p=a(v+1), q=av, A_m=A, B_m=B, and define

L(t)=(m²+t+1)/p, U(t)=(m²+t)/q,
P(x)=({x}²−{x}+1/6)/2,
T=sum_(c,d,a,m) (phi(a)/a) F_m,
S=sum_(c,d,a,m) (phi(a)/a) Delta_m(1).

Here braces mean fractional part, and the sums have exactly the
restrictions above. T is the real mass for this single divisor term,
not the full main term M_box.

**Conclusion.** With no alteration of the rounded A,B,

F_m=(B−A)/R ((m²+(A+B)/2)/(av(v+1))−1/(a(v+1))),       (1)
Delta_m(1)={p[P(L(B))−P(L(A))]
                 −q[P(U(B))−P(U(A))]}/R.              (2)

Consequently S is the weighted sum of the right side of (2), and

c N²h/log N <= T <= C N²h,
−T <= S <= 2 sum_(c,d,a,m) phi(a)/a = O(N³h).          (3)

These bounds do not establish S=o(T), nor any fixed sign for S.
The aggregate cancellation of (2) remains unproved.

**Proof.**

L221's interior margin puts m²/(av) a distance at least cN from
N and 2N. Its rounded-cutoff argument gives B>A, while L220 gives
−R<=A<B<=R. Uniformly for A<=t<=B, both L(t) and U(t)
differ from m²/(av) by O(1/N): the denominator change contributes
O(1/N), and t contributes O(N^(−3/2)). Thus all these endpoints
are strictly inside [N,2N]. Also

U(t)−L(t)=(m²+t−v)/(av(v+1))>0,

because m² is comparable to N^4 whereas v=O(N²), |t|=O(N^(3/2)).

The overlap-length definition of f_m now gives exactly

f_m(x)=R^(-1) integral_A^B 1_{L(t)<=x<=U(t)} dt.

Indeed the inequalities say avx−m²<=t<=a(v+1)x−m²−1;
intersecting this interval with [A,B] gives L220's length.
The support already lies inside its clipping interval. Integrating
in x proves (1). Only bounded nonnegative integrals occur.

For almost every t the two endpoints are not integers. The exceptions
are finitely many t, since each affine endpoint has nonzero slope on
a bounded interval. For the other t the count of integers in [L,U]
is floor(U)−floor(L), and hence its discrepancy from U−L is
{L}−{U}. Summing f_m(b) involves only finitely many integers, so

Delta_m(1)=R^(-1) integral_A^B ({L(t)}−{U(t)}) dt.       (4)

Endpoint exceptions have measure zero even if A or B is exceptional.
The continuous periodic function P is locally absolutely continuous
and has derivative {x}−1/2 away from integers. Change variables
in the two terms of (4); the constant halves cancel. The fundamental
theorem of calculus gives (2), with the signs and factors p,q shown.
This identity retains the minus one in L220 through the +1 in L(t).

Equation (4) gives |Delta_m(1)|<=(B−A)/R<=2. Separately,
Delta_m(1)>=−F_m because its sampled sum is nonnegative.
Multiplication by the nonnegative weights and summation proves
the two bounds on S. There are O(N³h) index tuples.

For T, L221 proves F_m>=c/N uniformly and at least cNh
coprime pairs (a,m); there are at least cN² ordered pairs (c,d).
Its elementary totient inequality gives phi(a)/a>=c/log N,
proving the lower bound. Formula (1), B−A<=2R, and the scales
m=O(N²), a comparable to N, v comparable to N² give F_m<=C/N.
Counting tuples proves the upper bound.

## Scope and verification

The +1, both rounded endpoints, and the gcd(a,m) restriction survive
in the formula. No averaging or independence of fractional parts has
been assumed. Bounding the two P differences separately would lose
the short-interval structure; (4) is the bound used here. The lower
bound −T is just positivity of the sampled mass, not cancellation.
Even a saving for S alone would leave all other divisor terms in
L220 to estimate before drawing a conclusion about E_box.

The exact rational test `python3 scripts/heat/check_unit_progression.py`
checks (1) and (2) against independent piecewise-affine integration
and integer sampling, including endpoint crossings. It tests finite
algebra only. Formalization would require the overlap integral,
measure-zero endpoint exceptions, the absolutely continuous periodic
primitive, and L221's uniform interior estimates. RH remains open.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.

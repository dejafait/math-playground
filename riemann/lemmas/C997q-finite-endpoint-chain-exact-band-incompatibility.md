# Corollary 997q: the finite endpoint chain and its exact band incompatibility

## Hypotheses

Use the COMPLETE C997c(1),(4)–(6) point kernel

    k_n(c,z)=-2 exp(-cn/4) [integral_(cn)^(c(n+2)) g_n(t) exp(izt)dt
                           -integral_n^(n+2) g_n(t) exp(izt)dt],
    g_n(t)=K_(n+2)(t) exp(-t/2) cosh(3t/8),
    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1).

Here n>=2 is an integer, I=[7/4,9/4], E=[15/8,17/8], and
z_star=1+i/8. Let lambda be any finite complex Borel measure on E and put

    M=||lambda||_TV, F(t)=integral_E exp(i gamma t)dlambda(gamma),
    h(t)=exp(i z_star t)-F(t), q(t)=g_n(t)h(t),
    r=(n+2)/n, a=7n/4, b=9n/4,
    B=integral_n^(n+2) q(t)dt,
    J(x)=integral_x^(rx) q(t)dt, D(x)=r q(rx)-q(x),
    Delta=J(a)-B,
    R(c)=k_n(c,z_star)-integral_E k_n(c,gamma)dlambda(gamma).

F,h,q,D are also defined for complex t or x by these formulas.
Both beta terms, both short windows, every slope endpoint and K's -1
are retained. No simplicity or nonvanishing assumption is made about
the zeros of g_n. No actual-zero realization or selected-response
identity is assumed.

## Conclusion

The exact complete residual and its boundary/defect representation are

    R(x/n)=-2 exp(-x/4) [Delta+integral_a^x D(u)du], a<=x<=b. (1)

In particular, with d=sup_[a,b] exp(-x/4)|D(x)|,

    ||R||_(C(I)) <= 2 exp(-a/4)|Delta|+8d.                   (2)

Thus exp(-a/4)|Delta|<=C_B exp(-n/64) and
d<=C_D exp(-n/64), together with subexponential M for the SAME measures,
would suffice for the proposed point bridge. No such estimates or
measures are constructed here. Small ||R|| alone has not been converted
to a derivative bound for D.

For t in [a,b], define the finite chain length and terminal point by

    N(t)=min{j>=1: r^j t>b}, y(t)=r^N(t) t in (b,rb].

There is the division-free identity

    q(t)=r^N(t) q(y(t))-sum_(j=0)^(N(t)-1) r^j D(r^j t),   (3)
    N(t)<=1+log(9/7)/log r,
    r^N(t)<=9r/7, sum_(j=0)^(N(t)-1) r^j<=(n+9)/7.         (4)

The terminal q(y(t)) is not discarded. The scalar Delta retains the
separate lower window. For example, any smooth terminal prescription
T=q|[b,rb] coming from these entire functions necessarily satisfies

    T^(j)(b)=r^(j+1) T^(j)(rb)-D^(j)(b), j>=0.             (5)

These are necessary endpoint compatibility conditions, not a band
representability theorem.

There is NO finite complex band measure lambda for which D vanishes
on any nonempty open subinterval of [a,b]. In particular, the tested
ansatz of EXACT homogeneous endpoint cancellation q(rx)=q(x)/r
cannot lift to a finite band measure, whatever terminal data and lower
boundary constant are chosen. It cannot even give a nonzero constant
J(x) on an open slope interval. This statement is at each fixed n.

This stops only exact homogeneous cancellation. It proves neither an
exponential lower bound on the defect nor impossibility of the desired
approximate band duals. The band-TV and approximate residual thresholds
remain unresolved. Step364, 11 November 2026: RESEARCH / REPRODUCTION
under the unchanged pre-invocation EXPLORE review362; scoped NEGATIVE
for the exact ansatz. This is a standard identity-theorem specialization,
not a claimed discovery beyond the checked sources. It is unaudited.
There is no RH candidate.

## Proof

### Entire band transforms and the complete residual

For each compact subset of the complex t plane the integrand defining F
and all its t derivatives are uniformly bounded by a constant times
the finite variation measure |lambda|, since |gamma|<=17/8. Dominated
differentiation therefore makes F entire, with

    |F(t)|<=M for real t,
    |F(z)|<=M exp((17/8)|Im z|) for complex z.              (6)

The polynomial K_(n+2) is nonzero (it has degree n+1), so g_n is a
nonzero entire function. Consequently h,q,D are entire as well.
This argument uses compact frequency support and finite original TV;
it does not assume a Paley–Wiener converse or a distributional inverse.

Apply C997c's finite-complex-measure Fubini representation to the
lambda integral of the two finite time windows. At fixed n all
integrands are bounded on the relevant compact rectangles, and their
absolute integrals with respect to dt*d|lambda| are finite. It follows
that the lambda integral replaces exp(i gamma t) by F(t) in BOTH
windows. Subtraction from the z_star kernel gives exactly

    R(x/n)=-2 exp(-x/4)[J(x)-B].                           (7)

The ordinary fundamental theorem of calculus and chain rule give
J'(x)=r q(rx)-q(x)=D(x). Integrating this equality from a to x yields
(1). In particular, cancellation of moving endpoints is an equation
for q, not for g_n or h separately, and does not remove B.

From |D(u)|<=d exp(u/4),

    exp(-x/4)|integral_a^x D(u)du|
          <=4d(1-exp((a-x)/4))<=4d.

Also exp(-x/4)|Delta|<=exp(-a/4)|Delta|. Applying these to (1)
proves (2), uniformly at both closed endpoints. This is a sufficient
estimate only. Differentiating a small residual would require a further
justified estimate; that operation is not used here.

### Finite propagation, terminal traces and zeros

The rearranged identity q(u)=r q(ru)-D(u), iterated exactly N(t)
times, gives (3). All arguments r^j t with j<N(t) lie in [a,b];
the final one lies in (b,rb]. This justifies termination at a finite
window boundary without extrapolating D beyond its observed interval.
Since r^(N(t)-1)t<=b and t>=a,

    N(t)-1<=log(b/t)/log r<=log(9/7)/log r,
    r^N(t)<=rb/t<=9r/7.

The geometric sum is (r^N(t)-1)/(r-1). Its upper bound is

    (9r/7-1)/(r-1)=(n+9)/7,

proving (4). Formula (3) also covers t=b, where N(b)=1.
Differentiating D(u)=r q(ru)-q(u) j times at b gives (5).
In a separately prescribed chain these conditions must be checked:
adjacent pieces may otherwise fail to join even continuously at the
points b/r^k. Conditions of every order are necessary for an entire
band transform, but are not asserted to be sufficient.

No step has divided by g_n. If one instead tries to reconstruct
F=exp(i z_star t)-q/g_n from prescribed analytic chain data, a zero
zeta of g_n of multiplicity m requires

    q^(j)(zeta)=0 for 0<=j<m.                              (8)

This follows directly by writing g_n(t)=(t-zeta)^m u(t), u(zeta)!=0;
the quotient is holomorphic there if and only if q has at least that
order of vanishing. It applies to all zeros, real or complex, with
their actual multiplicities. Satisfying only the real-window conditions
does not establish an entire finite-band transform. We neither assume
simple zeros nor assert that the unknown approximate chain meets (8).
For the exact homogeneous ansatz the next argument proves impossibility
without locating or dividing at ANY zero, so no unexamined zero case
can provide an exception.

### Exact homogeneity is incompatible with a finite band measure

Assume D=0 on a nonempty open subinterval of [a,b]. By the standard
named identity theorem for holomorphic functions, the entire function D
vanishes on C. Therefore r q(rt)=q(t) for every complex t. Substituting
t/r repeatedly gives, for any fixed complex t and every integer k>=1,

    q(t)=r^(-k) q(t/r^k).

Because r>1 and q is continuous at zero, the right side tends to zero.
Hence q is identically zero. As g_n is a nonzero entire function,
h vanishes on a nonempty open set where g_n!=0. The same identity
theorem makes h identically zero. Thus F(t)=exp(i z_star t) everywhere.
For real t<0 the right side has modulus exp(-t/8), which is unbounded
as t tends to minus infinity, contradicting |F(t)|<=M in (6).

This contradiction is independent of the terminal values and of Delta
or B. In particular imposing J(a)=B for exact recovery, or allowing a
nonzero residual boundary constant, cannot repair an exactly homogeneous
band chain. A merely smooth logarithmically periodic q on a positive
finite interval evades analyticity at zero, but is not thereby the
transform of an admissible band measure. No quantitative uniqueness or
stability estimate follows from the identity theorem; the approximate
problem is left open.

### Retained lower window and quantitative limitations

C997c(5), with a unit slope atom at c, gives the lower spectral measure
variation at most 8 exp(3/4)(n+2)exp(-n/16), uniformly on I.
Since t>=n on that window, |exp(i z_star t)|<=exp(-n/8), whereas
|F(t)|<=M. Therefore its full contribution in (7) satisfies

    sup_(c in I) |2 exp(-cn/4) B|
       <=8 exp(3/4)(n+2)[exp(-3n/16)+M exp(-n/16)].        (9)

If the SAME M_n were subexponential, choose, for instance, its
epsilon=1/64 allowance. Then (9) is O(exp(-n/64)); polynomial factors
are absorbed by the remaining positive margins. Thus the lower piece
is conditionally payable under the requested original band-TV bound.
The upper boundary J(a), the defect D and that band-TV bound are still
unpaid. No disjointness of the two windows is needed, including n=2.

The polynomial factor in (4) also does not pay a weighted inverse.
For clarity put W=sup_[b,rb] exp(-u/4)|q(u)|. Applying (3) without
discarding its terminal term gives only the general upper estimate

    sup_[a,b] exp(-t/4)|q(t)|
      <=exp(n/8)[(9r/7)exp(9/8) W+((n+9)/7)d].           (10)

Indeed the terminal displacement is at most rb-a=n/2+9/2, and
every defect argument is at most b, so its displacement from t is at
most b-a=n/2. Substitution into (3),(4) proves (10). A defect estimate
with exponent 1/64 by itself would leave exponent 7/64 in this crude
propagation bound, before treating W or dividing by g_n. This is an
UPPER bound on an intermediate weighted q norm, not an unavoidable
cost, not a lower bound on ||lambda||_TV, and not a contradiction to
the direct residual estimate (2). It cannot decide the requested pair
of bounds.

The imported ingredients are C997c's exact finite-measure kernel and
variation bound, and the standard named holomorphic identity theorem
and fundamental theorem of calculus. They are used at their stated
hypotheses, not reproved as new general results. The explicit finite
chain, trace conditions and weights are written out because qualitative
adjoint uniqueness by itself gives neither this original-TV residual
criterion nor its terminal and zero qualifications. The source contracts
reused in review362 do not supply a band representer or quantitative
inverse; none is implicitly imported here. C997j/k and C997i/m/p are
scope comparisons only, not mathematical inputs to this proof.

## Mathlib

Full matching coverage is unchecked and unknown. The argument uses
elementary finite sums, differentiation of compactly supported Fourier
integrals, and the holomorphic identity theorem. No Mathlib theorem
identifier or complete formalization has been verified. Unknown coverage
is not evidence of absence.

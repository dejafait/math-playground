# Lemma 919: a uniform complete complex-zero H2 tail budget

## Hypotheses

Use the exact positive kernel K of L019 and the L058 entire family

    F(lambda,z) = integral_0^infinity exp(lambda*u^2) K(u) cos(zu) du,
    0 <= lambda <= 1/20.

Use L874's logarithm germ and matrix convention:

    log(F(lambda,z)/F(lambda,0)) = -sum_(k>=1) S_k(lambda) z^(2k)/k,
    H2(lambda) = (S_(i+j+2)(lambda))_(0<=i,j<=2).

All zeros below are zeros in the spatial variable, with their full
multiplicities. From each opposite pair {zeta,-zeta}, choose one
representative zeta; repeat it according to the common multiplicity.
There is no zero at zero. All expressions used are invariant under
changing the representative. Set R=100 and D=diag(1,200,40000).
No zero reality, simplicity, zero-free boundary, or constant census
over the time band is assumed.

## Conclusion

For k=2,...,6 the complete, absolutely convergent identity is

    S_k(lambda) = sum_(opposite pairs) zeta^(-2k).           (1)

Define the finite head and the full remaining matrix by

    A(lambda) = sum_(|zeta|<=100) zeta^(-4) v(zeta)v(zeta)^T,
    E(lambda) = sum_(|zeta|>100)  zeta^(-4) v(zeta)v(zeta)^T,
    v(zeta) = (1, 200*zeta^(-2), 40000*zeta^(-4))^T.

Both matrices are real symmetric, and

    D H2(lambda) D = A(lambda) + E(lambda),
    ||E(lambda)||_2 <= B_* < B = 5691/10^9 = 0.000005691,   (2)

uniformly on the entire closed time band, where the explicit rational
budget is

    B_* = sum_(p=4,8,12) w_p * [4p/(5(p-1))]
                         *100^(1-p)*(5+1/(p-1)),
    (w_4,w_8,w_12) = (1,40000,1600000000),
    B_* = 74137011761/13027587890625000.

In particular the following is a **conditional** sufficient head margin:

    inf_(0<=lambda<=1/20) lambda_min(A(lambda)) > B.        (3)

If (3) were separately established, H2 would be positive definite
throughout the band. Neither (3), its feasibility, nor head reality or
a head census is established here. Boundary zeros belong to A, even
when they enter or leave it as time varies. No continuity of A is
needed or claimed. This is an explicit specialization of known
product/Jensen methods, not a new general zero-counting theorem or
progress beyond the cited methods. The independent step204 audit below
accepts this specialized proof and budget. Higher-degree signs and RH
remain open.

## Proof

### Elementary uniform kernel and normalizer constants

L058 supplies, with q=exp(-pi), the complete-theta-series bound

    K(u) <= C exp(9u/2-pi exp(2u)),
    C = 8pi^2 (1+11q+11q^2+q^3)/(1-q)^5.

Here 3<pi<22/7, pi^2<10, and exp(3)>20 (already its Taylor sum
through degree eight exceeds 20). Thus q<1/20. The numerator is
less than 8/5, while Bernoulli's inequality gives
(1-q)^5>=1-5q>3/4. Consequently C<512/3<200. This pays every
theta index; there is no numerical truncation of that series.

For 0<=u<=1/10 put v=pi exp(2u). Since exp(1/5)<1/(1-1/5)=5/4,
we have 3<v<55/14<4. The first positive theta summand from L019
therefore satisfies

    K_1(u)=4v(2v-3)exp(u/2-v) > 36 exp(-4).

All other summands are positive and exp(lambda*u^2)>=1. Hence

    F(lambda,0) > (18/5)exp(-4) > 1/20.                   (4)

For the last inequality, the factorial-series tail gives
e<=5/2+(1/6)/(1-1/4)=49/18<11/4, so e^4<(11/4)^4<72.
No interval-arithmetic library or normalizer certificate from L914
is required for (4).

### Explicit growth and all-zero count

Let M_lambda(r)=max_(|z|<=r)|F(lambda,z)|. The exponential series
gives exp(2u)>=2u^2 and therefore lambda*u^2<=exp(2u)/40.
Using |cos(zu)|<=exp(r*u), put beta=pi-1/40>119/40 and
v=r/2+9/4. Then

    M_lambda(r) <= 200 integral_0^infinity
                  exp((r+9/2)u-beta exp(2u)) du
                <= 200 exp(v log v-v).                   (5)

Indeed the maximum of (r+9/2)u-exp(2u) on u>=0 is v log v-v,
since v>1. The remaining integral is bounded by

    integral_0^infinity exp(-(beta-1)exp(2u))du
       <= exp(-(beta-1))/(2(beta-1)) < 1,

using exp(2u)>=1+2u and beta-1>1. These bounds hold at lambda=0
and lambda=1/20 without passage to a time limit. They also give
the growth O(r log(r+2)) for log M, hence entire order at most one.

We import Jensen's formula with multiplicities, including its
boundary-radius limiting convention: T. Tao, *246B, Notes 1: Zeroes,
poles, and factorisation of meromorphic functions*, 23 December 2020,
Theorem 2, equations (3)-(6), and the doubled-radius counting argument
in Proposition 8 and its proof,
https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/.
The function is entire by L058 and its centre is nonzero by (4).
There are no poles. A zero on the outer circle has zero logarithmic
weight; the source's limiting argument does not require a nonvanishing
outer circle. We apply the formula, not its existential counting
constant, to retain explicit bounds.

Let n_lambda(r) count **all** zeros with |z|<=r, including both signs.
Jensen on radius 2r and (4)-(5) imply, for r>=100,

    n_lambda(r) log 2
       <= log(M_lambda(2r)/F(lambda,0))
       < log 4000 + (r+9/4)log(r+9/4).                    (6)

Every counted zero contributes at least log 2, with multiplicity;
the other zeros contribute nonnegative terms. In particular no
reality or strip theorem is involved.

Here log 4000<9, log 2>2/3, and 4<log r for r>=100.
The first follows from exp(9)>20^3>4000, and the last from e^4<72.
The middle inequality follows, for example, by integrating the strict
convex tangent bound 1/t>=4/3-4t/9 on [1,2]. Also
r+9/4<=(41/40)r and log(41/40)<=1/40. Thus (6) gives

    n_lambda(r)
      < (3/2)[9+(41/40)r(log r+1/40)]
      <= r[(123/80)log r+111/640]
      < (8/5)r log r.                                    (7)

In the second line use 9/r<=9/100. The last uses
111/640<1/4<=(log r)/16. Evenness and nonvanishing at zero
give equal multiplicities at opposite zeros. Therefore the number
N_lambda(r) of opposite pairs, with multiplicity, is n_lambda(r)/2,
and

    N_lambda(r) <= (4/5)r log r,          r>=100.           (8)

### Product normalization, powers and uniform remainders

The paired Hadamard product used here is the one in D. H. J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn-Newman constant*,
Research in the Mathematical Sciences 6 (2019), article 31,
arXiv:1904.12438v2 (4 August 2019), Section 3, proof of Proposition 3.1,
paired product after (33): https://arxiv.org/html/1904.12438v2#S3.
The source uses evenness, order one and a nonzero origin, permits
complex/repeated zeros, and gives locally uniform convergence. We
use this product input, not its simple-zero differential equation.

For the source's kernel in (4),

    Phi(w)=sum_(n>=1)(2pi^2 n^4 exp(9w)-3pi n^2 exp(5w))
                         exp(-pi n^2 exp(4w)),

L019 gives K(u)=4Phi(u/2). Substitution u=2w in the integral proves
F(lambda,z)=8H_(4lambda)(2z). This verifies the normalization
recorded in L488 directly; none of L488's positive-time localization
assertions is used. Source time lies in [0,1/5]. Ratios at the origin
cancel the factor 8, and the source zero corresponding to zeta is
2zeta. The paired product therefore is

    F(lambda,z)/F(lambda,0)
       = product_(opposite pairs) (1-z^2/zeta^2).          (9)

Equivalently this is the standard Hadamard factorization for an even
entire function of order at most one, as also bounded in (5): genus-one
factors for opposite zeros multiply to 1-z^2/zeta^2, and evenness
removes the possible linear exponential. Its constant is fixed at
zero. No unaccounted quadratic exponential is allowed at this order.

For p>1 and any T>=100, Tonelli's theorem for nonnegative functions
and (8) give the complete tail estimate

    sum_(|zeta|>T) |zeta|^(-p)
      = p integral_T^infinity (N_lambda(t)-N_lambda(T))t^(-p-1)dt
      <= [4p/(5(p-1))] T^(1-p)(log T+1/(p-1)).             (10)

The equality follows by writing each |zeta|^(-p) as its integral
from |zeta| to infinity. Thus it pays the entire infinite tail,
including all multiplicities, without assumptions on shell counts.
The elementary integral on the second line is integration by parts;
its boundary term at infinity vanishes for p>1. The same formula for
general T shows that tails vanish uniformly in lambda.

In particular p=2 gives uniform summability of the remote product
logarithms on every bounded z-disk once the zeros in that tail have
|zeta|>2|z|. Joint continuity in L058, the compact time band and (4)
give a common sufficiently small origin disk on which F/F(lambda,0)
is close to 1 and nonzero. On a smaller disk, the elementary expansion

    log(1-z^2/zeta^2) = -sum_(k>=1) z^(2k)/(k*zeta^(2k))

can be summed over zeros absolutely and locally uniformly. Indeed
all zeros are uniformly away from that disk; the finitely many with
|zeta|<=100 have uniformly bounded number by (8), and the rest are
controlled by (10) with p=2. The product logarithm normalized at zero
is L874's germ, by (9). Cauchy's coefficient formula, or absolute
convergence on a smaller disk, gives (1) for each k=2,...,6.
This uses no global logarithm, differentiable enumeration of zeros,
or interchange of a time derivative with a zero sum.

### Scaled matrix norm and the conditional threshold

Equation (1) gives A+E=D H2 D entry by entry. Complex conjugation
permutes opposite-pair classes and preserves the cutoff and
multiplicity. Their conjugate contributions sum to real matrices;
a conjugation-fixed class has real zeta^2 and already contributes
a real matrix. Every term is symmetric. Absolute convergence from
(10) permits this regrouping, so both A and E are real symmetric.

For the Euclidean operator norm over the complex vector space,
||v v^T||_2=||v||_2^2 (the transpose functional has the same norm
as the conjugate-transpose functional). Hence each term satisfies

    ||zeta^(-4)v v^T||_2
       = |zeta|^(-4)+40000|zeta|^(-8)
                             +1600000000|zeta|^(-12).

The triangle inequality and (10) at T=100, for p=4,8,12, yield the
claimed budget with log 100 replacing 5. Since exp(5)=exp(3)exp(2)
>20*5=100, we have log 100<5, so B_* in (2) is a valid upper bound.
Exact rational addition gives its displayed value and B_*<5691/10^9.
The absolute values occur only in this error estimate: they have not
replaced the algebraic zero powers in H2 by modulus squares.

By the standard Rayleigh-Ritz variational characterization, for every
real unit vector x,

    x^T(A+E)x >= lambda_min(A)-||E||_2.

Thus the independently verified condition (3) would imply positive
definiteness of D H2 D, and then of H2 by invertibility of D. This
proves only the stated implication. A finite budget alone supplies
no positive head margin and does not justify a head-search sweep.

### Exact arithmetic check and limitations

Run `python3 scripts/heat/complete-zero-tail-202.py`. The complete
certificate is `scripts/heat/complete-zero-tail-202.json`. Its 13 exact
integer/Fraction checks include the elementary finite constants and
the rational matrix budget, with no floating-point approximations.
They pass with no failures. The certificate checks finite arithmetic;
the product, Jensen application, convergence and infinite-tail
integration are justified above, not by a finite numerical preview.
The independent step204 replay below accepts the finite arithmetic;
neither program evaluates A.

### Independent conceptual audit, 9 November 2026 (step204)

The statement (1)-(2), including the closed time band and complete
complex-zero tail, is accepted. Condition (3) remains wholly conditional.
No defect in the claimed constants or analytic argument was found.
This audits the existing specialization under the reviewed product/Jensen
coverage; it is not a new theorem beyond those methods. The following
details make explicit the uniformity and factorization checks.

**Kernel, growth and order.** L019's two summands are exactly four
times the source's Phi(u/2), with exponents 9u/2, 5u/2 and 2u.
The substitution u=2w therefore gives the scalar 8, source time
4lambda and source argument 2z. No zero-location result is used.
The complete L058 majorant is valid since n^2-1>=n-1 and every
discarded kernel term in that upper bound is negative. The numerator
bound and Bernoulli denominator give C<512/3. On [0,1/10],
v>3, 2v-3>3, exp(u/2)>=1 and exp(-v)>exp(-4), so the positive
first summand gives (4). The bound for e follows because successive
terms after 1/3! have ratios at most 1/4. These strict lower and
upper estimates require no floating-point enclosure.

For growth, lambda*u^2<=exp(2u)/40 uniformly at both endpoints.
The maximum of (r+9/2)u-exp(2u) occurs at u=(log v)/2>=0,
with v=r/2+9/4, giving v log v-v. The residual exponential integral
is less than 1 because beta-1>1 and exp(2u)>=1+2u. Thus (5)
holds for every r>=0, and log M(r)=O(r log(r+2)) implies order
at most one. The bound alone does not require an exact lower order.
In Hadamard factorization the possible exponential has degree at
most one. Pairing genus-one factors at zeta and -zeta cancels
their linear exponentials; the paired product is even and nonzero
near zero. If F equals exp(a+bz) times this even product, evenness
near zero gives exp(bz)=exp(-bz), hence b=0 by differentiation at
zero. The ratio F/F(lambda,0) removes exp(a). There is no quadratic
exponential at this order. This checks all hypotheses of the imported
paired factorization without importing the simple-zero motion law.

**Jensen and boundary conventions.** For each fixed lambda the
function is entire and has positive central value. Jensen on 2r
therefore applies with its boundary-radius limiting convention.
Zeros on |z|=r contribute log 2, those on |z|=2r contribute zero,
and multiplicities enter each weight. The inequality in (6) follows
after discarding the negative term -(r+9/4) from (5). The explicit
constant reduction is

    (3/2)*(9/100+41/1600)=111/640,
    8/5-123/80=1/16,     111/640<1/4<log(r)/16.

Here log 2>2/3 follows by integrating the tangent to 1/t at 3/2,
strictly away from that point. The series bounds give log 4000<9
and log r>4 at r>=100. No zero-free counting radius is assumed.
Nonvanishing at zero makes the involution zeta -> -zeta fixed-point
free on zeros, and evenness preserves multiplicity. Dividing the
all-zero count by two therefore gives precisely (8).

**Complete tail and common logarithm disk.** For every zero modulus
a>T, p*integral_a^infinity t^(-p-1)dt=a^(-p). Summing these
nonnegative integrands gives (10) by Tonelli, with N(t)-N(T)
retaining exactly the strict tail. An atom at T is excluded from this
tail and included in the head. Integration by parts gives

    integral_T^infinity (log t)t^(-p)dt
      = T^(1-p)*(log T/(p-1)+1/(p-1)^2),    p>1.

This establishes convergence and a bound tending to zero uniformly
in lambda, rather than a finite-shell approximation.

For clarity on the compact-time extraction, continuity of
g(lambda,z)=F(lambda,z)/F(lambda,0) on the real compact time band,
g(lambda,0)=1 and (4) allow a common delta>0, with 2delta<100,
such that |g-1|<1/2 on |z|<=2delta for every time. Thus every zero
has |zeta|>2delta. On |z|<=delta, w=z^2/zeta^2 has |w|<1/4 and

    sum_(k>=1) |w|^k/k <= |w|/(1-|w|) <= (4/3)|w|.

There are fewer than 400 opposite pairs with |zeta|<=100, since
(8) and log 100<5 apply, and each such pair has |zeta|>2delta.
Their sum of |zeta|^(-2) is bounded uniformly by 400/(2delta)^2.
The remaining sum is uniformly finite by (10) with p=2. For an
arbitrary cutoff T>=100 the remote log sum is bounded by
(4/3)delta^2 times the p=2 bound in (10), which tends to zero
uniformly in time. Hence the entire double series of logarithm
powers is absolutely and uniformly convergent on this disk and
time band, including its finite head. At each time its exponential
is (9), its value at zero is zero, and uniqueness identifies it
with the local logarithm. Cauchy extraction on a smaller circle
therefore gives exactly S_k=sum zeta^(-2k), including k=2,...,6.
This proves the required uniform tail and coefficient interchange;
it does not posit a continuous enumeration, time-differentiated zero
sum, or continuity of the sharp-cutoff matrix A.

**Matrix and exact budget.** The (i,j) entry of the zero contribution
is D_ii D_jj zeta^(-2(i+j+2)), so the coefficient index in H2 is
unchanged. Conjugation respects opposite classes, the radial cutoff
and multiplicity. If a class is fixed by conjugation, zeta is real
or purely imaginary and zeta^2 is real. All other classes pair with
their conjugates. Absolute convergence permits this regrouping and
gives real symmetric A and E without any zero-reality assumption.
For a complex nonzero v, the functional v^T has norm ||v||_2,
attained at conjugate(v)/||v||_2, so ||vv^T||_2=||v||_2^2.
The resulting powers are precisely 4,8,12 with weights
1,200^2,40000^2. Substitution in (10) and log 100<5 give the
three weighted terms

    4/703125,   9/4785156250,   21/29541015625000.

Their sum is the displayed B_*, and the exact positive difference is

    B-B_* = 191419171/833765625000000000 > 0.

Run `python3 scripts/heat/complete-zero-tail-audit-204.py`.
It replays the unchanged original program, redirecting only its output
basename to `scripts/heat/complete-zero-tail-replay-204.json`, and
independently reconstructs the finite constants, integrated power
bounds, diagonal weights and rational sum. The complete replay equals
the original certificate; original source and certificate bytes remain
unchanged. All 51 audit checks pass with no failures; full evidence is
`scripts/heat/complete-zero-tail-audit-204.json`. The complete `/checks`
and `/tail` fields, including operands and thresholds, were inspected,
not merely their previews. These checks certify finite arithmetic only;
the preceding analytic audit pays the infinite remainder and limits.

Finally, the Rayleigh inequality applies to the real symmetric sum
and its Euclidean operator norm. A uniform strict head margin in (3)
would imply strict positive definiteness after invertible congruence
by D. Neither a census nor such a margin nor even its feasibility has
been certified. The audit does not advance the all-degree positivity
gap or RH beyond acceptance of this limited tail input. Direct local
inputs remain L019/L058/L874, so no DAG edge changes are needed.

## Mathlib

The prior assessment inspected the supporting theorem
`AnalyticOnNhd.circleAverage_log_norm`, which gives the Jensen identity
under analyticity near the closed disk, nonzero radius and nonzero
centre:
https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.circleAverage_log_norm.
Those hypotheses hold here by L058 and (4). Full coverage of the
heat-family product, these effective constants and the scaled matrix
tail is not checked. No missing declaration is treated as evidence
of absence, and no unlocated zero-count declaration is relied on.

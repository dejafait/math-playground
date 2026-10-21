# Lemma 422: a response-weighted second moment separates the fixed-weight law

## Hypotheses

Use the actual functions and normalization of L389 and L419 on
the positive ray: x(t)=F_0(t)/A(t), Z(t)=zeta(5/2+it), W(t)=|Z(t)|^2,
ell=log H, and E=H^(-1) integral_[H,2H]. Let

    C_0=1, C_j=sum_(n>=1) d_j(n)^2 n^(-5) (j>=1),
    S=zeta(5)zeta(3)^2/zeta(6), R_k=C_(k+1)/C_k.

For the comparison use exactly the L421 probability law, with its
prescribed response and height marginal, and L419's fixed choice

    k>=1 an integer, R_k>S,
    theta=(S-C_1)/(R_k-C_1),
    g0(t)=1-theta+theta W(t)^k/C_k.

Each such k is fixed independently of H. Its constants and onset may
depend on k. No assertion about other weights or a growing k is made.
Use the audited order-zero twisted second moment and sharp scalar
bound of L381 (7),(9), Hardy identification L389 (3), right-line
moments L419 (3), and all three components of L421 (4)--(9).

## Conclusion

The actual sharp-interval coefficient is

    E[W^2 x^2]=T ell+o(ell),
    T=sum_(m,n>=1) d_2(m)d_2(n)gcd(m,n)/(m^3 n^3).       (1)

It is an absolutely convergent positive Euler product. For every
allowed fixed k, the full L421 law instead satisfies

    E_nu[W^2 x^2]=B_k ell+O_k(sqrt(ell)),
    B_k=C_2+(S-C_1)(C_(k+2)/C_k-C_2)/(R_k-C_1).         (2)

For all those integers k, |B_k-T|>1/1000. More precisely,
B_k<T for k<=13 and B_k>T for k>=14. Thus none of these fixed-g0
laws can additionally match even the leading coefficient in (1).

This is a known-moment specialization and a local family diagnostic,
not a new zeta moment theorem. The separate step-168 critical audit
below validates this diagnostic in its stated fixed-k scope.
L421's counterlaw for its original selected information
remains valid: that list did not include (1). No arbitrary covariance
weight, actual capped statistic, clipping, regulator margin, global
critical-function realization, mixed positivity or RH is decided.

## Proof

### The sharp full-response actual coefficient

L389 (3) gives x^2=|U|^2, U(t)=zeta(1/2+it), including at zeros.
We import rather than reprove the fixed-twist theorem specialized in
L381 (7): for fixed positive integers m,n and fixed-shape smooth
weights supported in [H/2,3H], 0<=w<=1,

    integral w(t)(m/n)^(-it)|U(t)|^2 dt
      =gcd(m,n)/sqrt(mn) integral w(t)log(t/(2pi))dt
         +O_(m,n,w)(H).                               (3)

Its primary source is M. P. Young, *A short proof of Levinson's theorem*,
Arch. Math. 95 (2010), 539--548, DOI 10.1007/s00013-010-0199-9,
[Lemmas 4--5, (4.1)--(4.5), pp. 542--543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
As checked in L381, the scale is 2H, the fixed twists eventually
satisfy mn<=(2H)^(2vartheta) for any fixed 0<vartheta<1/2,
and fixed-shape derivatives O_j(H^(-j)) meet Young's derivative
requirement. Zero shifts are allowed after combining both
functional-equation diagonals holomorphically at their removable
singularity. No new shifted differentiation or carrier is used here.

Put V_N(t)=sum_(n<=N) d_2(n)n^(-5/2-it). Expansion and (3) give

    integral w |U V_N|^2
      =T_N integral w(t)log(t/(2pi))dt+O_(N,w)(H),
    T_N=sum_(m,n<=N) d_2(m)d_2(n)gcd(m,n)/(m^3 n^3).     (4)

This retains all rational-twist collisions. To remove smoothing,
use L381's lower and upper weights for the whole nonnegative
integrand |U V_N|^2: support is respectively inside [H,2H] and
inside [H-epsilon H,2H+epsilon H], with integrals H+O(epsilon H),
and epsilon fixed in (0,1/4). The upper weight is one on [H,2H];
both supports fit (3). Since log(t/(2pi))=ell+O(1) there, first
H tends to infinity at fixed N,epsilon, and then epsilon tends to
zero. The resulting sharp mean divided by ell tends to T_N.

Absolute Dirichlet multiplication gives V=Z^2 and

    sup_t |V-V_N|<=delta_N=sum_(n>N)d_2(n)n^(-5/2)->0,
    sup_t (|V|+|V_N|)<=2 zeta(5/2)^2.

L381 (9) gives E|U|^2=O(ell). Consequently

    |E |UV|^2-E |UV_N|^2|
       <=2 zeta(5/2)^2 delta_N E|U|^2=O(delta_N ell),    (5)

with a constant independent of N and all sufficiently large real H.
Also gcd(m,n)<=sqrt(mn), so the positive double sum T is at most
(sum d_2(m)m^(-5/2))^2=zeta(5/2)^4<infinity. Thus T_N increases
to T. Given an error tolerance, choose N by (5) and T-T_N, and
then take the sharp height limit for this fixed N. This proves (1)
without a growing-head estimate or an independence assumption.

### The full comparison-law coefficient

Retain L421's high, intermediate and bulk components. The bounded
weight W^2<=zeta(5/2)^4 multiplies the high and intermediate
second integrals in L421 (4),(6) by at most that constant. Their
weighted x^2 contributions are therefore O(ell^(-2)) and
O_k(sqrt(ell)), respectively. These are unnormalized component
integrals, not conditional second moments divided by rare mass.

In the bulk, L421 (8) gives centered covariance
Sigma(t)=ell g_H(t)K+A_H, with K_11=1,
||A_H||=O_k(sqrt(ell)), and bounded mean m(t). Hence its full
contribution is

    E[w W^2(Sigma_11+m_1^2)]
      =ell E[w g_H W^2]+O_k(sqrt(ell)).

The normalization and rare-mass estimates in L421 (7) imply, for
every bounded response expression R,

    E[w g_H R]=E[g0 R]+O_(k,R)(H^(-1)+ell^(-5/2)).

Take R=W^2 and use L419 (3) for j=2,k+2. This gives

    E[g0 W^2]=(1-theta)C_2+theta C_(k+2)/C_k+O_k(H^(-1)).

The normalization error times ell is o(1), and all three components
give (2). The O(sqrt(ell)) covariance correction has been retained;
it is not incorrectly treated as O(1).

### Monotonicity covering every integer k

We prove B_k is nondecreasing on all integers k>=1 using the
algebraic formula (2), whether or not that k is admissible. This
use outside the admissible range asserts no law there.

For a finite prime cutoff P, let independent circle coordinates have
normalized Lebesgue measure and put

    Y_P=product_(p<=P)|1-p^(-5/2)exp(i alpha_p)|^(-2).

These variables are bounded above and bounded away from zero. Write
mu_P for the distribution of Y_P.
Absolute Fourier multiplication gives E Y_P^j=C_j(P), the product
of the corresponding local factors of C_j. For each fixed j,
C_j(P)->C_j by the absolutely convergent positive Euler product.
These are auxiliary finite integrals, not an actual prime-phase
distribution assumption.

For integers 1<=k<l, consider the matrix with rows indexed by
a=(0,k,l), columns by b=(0,1,2), and entries E Y_P^(a_i+b_j).
Expanding both determinants and applying Fubini on the bounded
product space shows its determinant is

    (1/6) integral det[y_j^(a_i)]_(i,j=1)^3
                      det[y_j^(b_i)]_(i,j=1)^3 dmu_P^3. (6)

For 0<y_1<y_2<y_3 the second determinant is their positive
Vandermonde. The first is also positive: set v_j=y_j^k and observe
that v -> v^(l/k) is strictly convex. The determinant with rows
1,v,v^(l/k) is (v_2-v_1)(v_3-v_1) times the strictly positive
difference of the corresponding secant slopes. Repeated y's give
zero; a permutation changes both determinant signs together.
The integrand in (6) is therefore nonnegative everywhere.

Taking P to infinity proves the same nonnegative determinant with
entries C_(a_i+b_j). Divide its last two rows by C_k,C_l and
subtract the first row. With Q_j=C_(j+2)/C_j, it follows that

    (R_k-C_1)(Q_l-C_2)-(R_l-C_1)(Q_k-C_2)>=0.          (7)

The same finite measures and Cauchy--Schwarz give
C_j^2<=C_(j-1)C_(j+1), hence R_j is nondecreasing.
The certified inequality C_2>C_1^2 below yields
R_k>=R_1>C_1 for every k>=1. Since S>C_1 (also proved in L419),
division in (7) establishes B_l>=B_k. Nonstrict monotonicity is
enough; no infinite-product probability theorem is required.

### Explicit Euler factors and rational certificate

For a prime p put u=p^(-3), v=p^(-5). Splitting its double sum
by the common minimum exponent e, then by the positive excess r
in either coordinate, gives

    T_p=sum_(a,b>=0)(a+1)(b+1)p^(-3a-3b+min(a,b))
       =(1+v)/(1-v)^3 * (1+u)/(1-u)
          +2u/((1-u)^2(1-v)^2)
       =((1+v)(1-u^2)+2u(1-v))/((1-v)^3(1-u)^2).       (8)

Indeed sum (e+1)^2 v^e=(1+v)/(1-v)^3 and
sum (e+1)v^e=(1-v)^(-2); these ordinary geometric derivatives
converge absolutely. The already established convergence of (1)
justifies T=product_p T_p by nonnegative multiplicative expansion.
For C_j use L419's factor

    C_j(p)=sum_(e>=0) binom(j+e-1,e)^2 p^(-5e).         (9)

Here is the complete finite-certificate procedure and its tails.
It uses P=200 and e=0,...,40 in (9), for
j in {1,2,13,14,15,16}. If t_e denotes its summand, then

    t_(e+1)/t_e=((j+e)/(e+1))^2 p^(-5)

is nonincreasing in e. Thus with r=((j+40)/41)^2 p^(-5)<1,
the omitted local tail is between zero and t_40 r/(1-r).
All these quantities are rational. For primes above P, use
binom(j+e-1,e)<=j^e, which follows by mapping ordered length-e
words over j letters onto their multisets. Hence their total
logarithmic tail is at most

    r_C(j)=j^2/[4P^4(1-j^2(P+1)^(-5))].              (10)

This uses -log(1-z)<=z/(1-z) and
sum_(n>P)n^(-s)<=1/((s-1)P^(s-1)). For each zeta(s), s=3,5,6,
the analogous logarithmic tail is

    r_z(s)=1/[(s-1)P^(s-1)(1-(P+1)^(-s))].           (11)

For (8), writing D=(1+v)/(1-v)^3 gives
T_p<=D[(1+u)/(1-u)+2u/(1-u)^2]. Here
D<=(1-v)^(-4), and the bracket <=(1-u)^(-4), since

    (1+2u-u^2)(1-u)^2=1-4u^2+4u^3-u^4<=1

for 0<=u<=1. The logarithmic tail of T is consequently at most

    r_T=2/[P^2(1-(P+1)^(-3))]
                     +1/[P^4(1-(P+1)^(-5))].        (12)

Every r in (10)--(12) is less than one. An omitted Euler product
with log at most r lies in [1,1/(1-r)], because exp(r)<=1/(1-r).
Thus only rational operations are needed, including the zeta bounds
used to form S. Lower bounds omit positive tails. The finite prime
list is generated by the sieve through 200.

The implementation rounds each rational interval outward to multiples
of 10^(-18) after arithmetic; division is performed only on positive
denominator intervals. It evaluates S,T,B_13,B_14 from these intervals
and asserts exactly the following rational comparisons:

    B_13 < 2236/1000 < 2237/1000 < T
         < 4475/2000 < 4477/2000 < B_14.              (13)

Reproduction command, relative to this notebook:

    python3 scripts/discriminant/check_response_modulus_second_moment.py

Full certificate:
`scripts/discriminant/response-modulus-second-moment-certificate.json`.
The complete load-bearing `/bounds` and `/checks` fields were inspected,
as was the empty `/failures` field. Exact certified endpoints include

| Quantity | Lower endpoint | Upper endpoint |
| --- | --- | --- |
| T | 2237071254681438167/10^18 | 2237183115249214863/10^18 |
| B_13 | 55860227350023909/25000000000000000 | 1117250301051395909/500000000000000000 |
| B_14 | 1119531828438082987/500000000000000000 | 55978890041859339/25000000000000000 |

The certificate also checks C_2>C_1^2 and S>C_1 using its interval
endpoints. Its decimal fields and the preserved initial exploratory
float output are not proof evidence. The finite rational assertions
use exact Python integer/Fraction arithmetic; as with any computational
certificate, correct execution of that implementation is required.
Equations (8)--(12) specify the mathematical bounds independently
of floating-point arithmetic. The independent step-168 audit below
checks all these bounds and the complete saved certificate.

Finally, if k<=13, monotonicity and (13) give
T-B_k>=T-B_13>1/1000. If k>=14, they give
B_k-T>=B_14-T>1/1000. This includes every allowed fixed k without
choosing a convenient admissible parameter or assuming a uniform
height onset across an unbounded set of k. It proves the stated
separation and completes this diagnostic.

### Separate critical audit — 2026-10-16, step 168

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-16-response-modulus-second-moment-audit.md`.
This RESEARCH / REPRODUCTION / proof_audit finds no defect in (1)--(13).
It verifies the known-source specialization and its family comparison;
it does not establish a new general moment theorem or originality.

**Normalization, imported theorem and sharp limits.** In L389 (3),
the unit gamma phase times U is real and equals -x. The phase relation
is independent of division by U, so x^2=|U|^2 holds also at zeros.
The Z in this lemma is the right-line zeta value, not L389's Hardy
function. Young's cited Lemmas 4--5 apply at scale 2H: their support
[H/2,4H] contains the stated weights, fixed-shape derivatives satisfy
the weaker H/log H derivative scale, and fixed twists meet the length
restriction eventually. The previously audited L381 (7) combines the
two functional-equation diagonals holomorphically before taking zero
shifts. Its gcd factor is unchanged on reducing m/n; no diagonal is
discarded and no complete response is inserted in the source weight.

Since V_N has coefficients d_2(n)n^(-5/2), multiplying these by
gcd(m,n)/sqrt(mn) gives exactly the denominator m^3 n^3 in (4).
Twists with the same reduced ratio remain distinct terms of this
finite expansion. Bracketing the entire nonnegative |UV_N|^2 gives
upper and lower limits T_N(1+O(epsilon)); first H tends to infinity
at fixed N and epsilon, then epsilon tends to zero. Both endpoint
transition strips lie within the permitted support. Finally (5),
with an N-independent scalar bound from L381 (9), and the positive
absolutely convergent double sum give the full limit. Explicitly,
the limsup of the absolute normalized error from T is at most
C delta_N+|T_N-T| for every fixed N, and this tends to zero.
There is no simultaneous growing-head or shrinking-smoothing claim.

**Every law component and fixed-parameter error.** L421's high
second integral is O(ell^(-2)), and its intermediate second integral
is O(sqrt(ell)); multiplication by bounded W^2 preserves both orders.
For the bulk, its conditional raw second entry is Sigma_11+m_1^2,
not Sigma_11 alone. Its fiber mass w must also be retained. The
bounded mean contributes O_k(1), and the constant matrix A_H contributes
O_k(sqrt(ell)). The leading entry is ell g_H K_11 with K_11=1.
L421 (7) controls replacement of w g_H by g0 against W^2 in integral,
even where the high probability is 1/2. That error times ell is
O_k(ell/H+ell^(-3/2)), hence o(1). L419 (3) applies at the fixed
powers 2 and k+2; its absolute off-diagonal bound is O_k(H^(-1)).
This proves precisely (2), with one onset for each fixed admissible k,
and no common onset as k grows. No conditional independence is used.

**Determinant orientation and all-k quantifier.** For each finite
prime set all positive and negative powers needed here are bounded,
so the finite Fubini expansion in (6) is legitimate. Expanding its
two determinants produces six copies of the moment determinant,
which accounts for 1/6. Both displayed determinants have monomials
as rows and sample points as columns. For ordered distinct samples,
the first sign is the sign of the difference of the two secant
slopes of v^(l/k), multiplied by (v_2-v_1)(v_3-v_1)>0.
Since l/k>1, strict convexity gives the positive sign. Permutations
reverse both signs together; repeated samples give zero. Passage
to the full C_j is entrywise in a finite determinant. Dividing rows
by positive C_k,C_l and subtracting the row (1,C_1,C_2) gives
exactly (7), with the stated orientation.

Finite-measure Cauchy--Schwarz, including C_0=1, passes to the limit
and gives R_k>=R_1=C_2/C_1>C_1. The strict last inequality and
S>C_1 are independently certified below. All divisions used to obtain
monotonicity therefore have positive denominators. This establishes
nonstrict B_l>=B_k on every integer k>=1; no admissible law is asserted
when R_k<=S. The two adjacent bounds then cover every admissible
fixed k, with the strict gap in the conclusion. Strict monotonicity
and a probability space for infinitely many primes are unnecessary.

**Exact Euler factors, all tails and independent certificate.**
In (8), the equal-exponent terms are (e+1)^2 v^e and each positive
excess r contributes (e+1)(e+r+1)v^e u^r. Summing the excess in
both coordinate directions gives the two terms of (8). Positivity
and the double-sum bound justify its Euler product without rearranging
a conditionally convergent series. For (9), the next ratio decreases
with e when j>=1. Thus the omitted tail is bounded by its first
term divided by 1-r, including the constant-ratio case j=1.

For every omitted prime, binom(j+e-1,e)<=j^e bounds the local factor
by (1-j^2 p^(-5))^(-1). Summing logarithms and replacing primes by
all integers above 200 proves (10); the identical argument gives
(11). The comparison in (12) uses (1-v)/(1+v)<=1 in its second
term and

    (1+2u-u^2)(1-u)^2 = 1-u^2(2-u)^2 <= 1.

Thus log T_p<=4[-log(1-u)-log(1-v)], and the two integral tails
give exactly (12). All ten rational logarithmic tail bounds lie in
(0,1). Since -log(1-r)>=r there, exponentiating gives the outward
factor [1,1/(1-r)]. No decimal approximation enters these bounds.

The complete original generator was inspected, including its signed
interval subtraction, four-product multiplication, positive-interval
division and floor/ceiling rounding. The independent verifier

    python3 scripts/discriminant/audit_response_modulus_second_moment.py

reads every saved rational endpoint and every local record. It uses
trial division instead of the sieve, direct binomial coefficients
instead of the term recurrence, and the common-minimum/excess formula
instead of the compressed numerator for T_p. It independently
recomputes all global interval operations with exact Fraction arithmetic
and checks that every rounding encloses its unrounded rational input.
Its full output is
`scripts/discriminant/response-modulus-second-moment-audit-certificate.json`.

The independent run verifies all 46 primes through 200, all 276
local C_j factors for the six required powers, all 46 local T factors,
all ten omitted-prime logarithmic tails, all seven positive divisor
intervals, and 765 outward roundings. Every saved global endpoint and
all six comparisons agree; both original and audit failure lists are
empty. The complete local records are processed as exact rationals,
not inferred from a preview or sampled subset. Full exact comparison,
divisor and gap fields were also inspected separately. The certified
gap lower bounds are

    T-B_13 >= 2570652578646349/10^18 > 1/1000,
    B_14-T >= 1880541626951111/10^18 > 1/1000.

These computations still rely on correct Python integer/Fraction
execution, not on a formal proof assistant. The analytic formulas
and tail justifications above specify their mathematical contracts.
The existing DAG inputs suffice: no additional mathematical input or
edge is introduced by verification. The fixed-g0 separator is validated;
L421's original selected-list obstruction and all remaining qualifications
in the conclusion are unchanged. In particular, this audit does not
exclude a different covariance weight or establish actual clipping,
the shrinking-regulator margin, global mixed positivity, or RH.

## Mathlib

Full matching coverage for this actual-response moment and family
comparison has not been checked. No assertion of absence is made.
The source zeta moment is imported by the precise citation above;
the elementary determinant, geometric-series and rational-tail
specializations are written out here. No Lean verification is claimed.

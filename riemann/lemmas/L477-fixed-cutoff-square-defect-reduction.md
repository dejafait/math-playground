# Lemma 477: fixed-cutoff reduction of the first-sign square defect

## Hypotheses

Use the actual Xi function, Hardy function Z, positive completion
amplitude A and W=D_1(Xi;t)/A(t)^2 of L471. In particular,

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=exp(i theta(t)) zeta(1/2+it)=-Xi(t)/A(t),
    theta(t)=Im log Gamma(1/4+it/2)-t log(pi)/2.

Use L317 conclusion (1) for ordinary derivative orders j=0,1,2,
including its cutoff transitions, and L316's analytic phase expansion.
Thus theta'(t)=lambda(t)+O(t^(-2)) and
theta''(t)=1/(2t)+O(t^(-3)), where lambda(t)=log(t/(2pi))/2.
No RH, simplicity, spacing or external zero-free premise is used.

For real T tending to infinity, put L=log T,
X=sqrt(T/(2pi)), M=floor X, K=floor(sqrt(2) X), and, for T<=t<=2T,

    P_j(t)=sum_(n<=M) (lambda(t)-log n)^j n^(-1/2-it),
    G_T(t)=4|P_1(t)|^2,
    E(T)=integral_T^(2T) |W(t)-G_T(t)| dt.

The j=0 power is 1, including when its base is zero. These are
precisely the fixed square and absolute defect in the approved
assessment; M is not replaced by a moving or fitted cutoff.

## Conclusion

Define the real residual

    R_T(t)=2 Re(P_0 conjugate(P_2)-|P_1|^2)
                 +2 Re(e^(2i theta(t))(P_0 P_2-P_1^2)).       (1)

Its equivalent finite expansion, over all ordered pairs, is

    R_T(t)=sum_(n,m<=M) log(n/m)^2/sqrt(nm)
       *[cos(t log(m/n))+cos(2 theta(t)-t log(nm))].          (2)

There is an absolute constant C, for all sufficiently large real T,
such that

    integral_T^(2T) |W(t)-G_T(t)-R_T(t)| dt
          <= C T L^(5/2),                                  (3)
    |E(T)-integral_T^(2T)|R_T(t)|dt| <= C T L^(5/2).          (4)

Also

    |integral_T^(2T) R_T(t) dt| <= C sqrt(T),
    integral_T^(2T) |R_T(t)| dt <= C T L^3.                 (5)

Consequently the proposed little-o defect is equivalent to
integral |R_T|=o(T L^3). A positive full-scale lower bound for either
absolute integral along an unbounded sequence gives one for the other
with any strictly smaller positive constant eventually. Neither such
lower bound nor the little-o estimate is proved here. The signed
estimate in (5) cannot decide them. Since G_T>=0, L471's negative
mass satisfies N(T)<=E(T), but (3)--(5) supply no saving for N(T).

This is a local transfer and algebraic reduction using known inputs,
not a new sign theorem. The separate critical audit in Section 5
verifies this finite argument with the three named analytic conclusions
retained as inputs. No fresh independent AFE audit or novelty beyond
the checked sources is asserted.

## Proof

### 1. A finite norm estimate with all endpoints retained

First record an elementary denominator sum. For M>=2,

    S(M)=sum_(1<=n<m<=M) 1/(sqrt(nm) log(m/n))
         <= C M log(2M).                                   (6)

For each m, the part n<m/2 is at most
(1/log 2)m^(-1/2) sum_(n<m/2)n^(-1/2)<=C. In the remaining
part, log(m/n)>= (m-n)/m and sqrt(m/n)<=sqrt(2), so its sum
is at most sqrt(2) sum_(h<=m/2)1/h. Summing over m proves (6).

If b is nonnegative, continuously differentiable and nondecreasing
on [u,v], integration by parts gives, for omega!=0,

    |integral_u^v b(t)e^(i omega t)dt|
       <= [b(u)+b(v)+integral_u^v |b'(t)|dt]/|omega|
       =2b(v)/|omega|.                                    (7)

This includes both boundary values; constant b is allowed.
All coefficients lambda(t)-log n for n<=M are nonnegative
and increasing on [T,2T], and at most C L. Expand |P_j|^2
as a finite double sum. Its diagonal is O(T L^(2j+1)) by
sum_(n<=M)1/n=O(L). Equation (7), applied to the product
of the two real coefficient weights, and (6) bound the sum
of the off-diagonal integrals by O(M L^(2j+1)). Hence

    ||P_j||_(L2[T,2T]) <= C sqrt(T) L^(j+1/2),  j=0,1,2.   (8)

Now retain the entering terms explicitly. For M<n<=K set
tau_n=2pi n^2, and define

    B_j(t)=sum_(M<n<=K) 1_(t>=tau_n)
                   (lambda(t)-log n)^j n^(-1/2-it).         (9)

Here T<tau_n<=2T. On its activation interval,
lambda(t)-log n=log(t/tau_n)/2 lies in [0,log(2)/2].
For a pair n,m the integral in |B_j|^2 is over the actual
interval [max(tau_n,tau_m),2T], possibly reduced to a point.
On that interval the product weight is nonnegative, bounded
by C/sqrt(nm), and nondecreasing. Thus (7) applies there.
For j=0 its initial boundary value is retained; for j>=1 it
vanishes because the later entering coefficient is zero.
The diagonal is at most C T sum_(M<n<=K)1/n=O(T), since
K/M stays bounded. The off-diagonal is O(K log(2K)) by (6).
Therefore

    ||B_j||_(L2[T,2T]) <= C sqrt(T),  j=0,1,2.              (10)

No fixed-polynomial theorem was applied to a moving endpoint.
Equations (7)--(10) also account for the variation of the weights.
No derivative of an indicator or of a floor function is taken.

### 2. Ordinary Hardy jets and completion curvature

Let N_t=floor(sqrt(t/(2pi))) and write d_n(t)=lambda(t)-log n.
For each j<=2 the elementary dyadic-block estimate gives

    sum_(n<=N_t) n^(-1/2)(1+d_n(t))^j <= C_j T^(1/4).       (11)

Indeed, on sqrt(t/(2pi))/2^(r+1)<n<=sqrt(t/(2pi))/2^r,
the weight sum is at most C T^(1/4)2^(-r/2)(1+r)^j;
the final block containing n=1 obeys the same bound up to a
constant. The resulting series converges. The base d_n is
nonnegative, and replacing it by theta'-log n changes these
absolute bounds by at most a uniform factor.

L317 gives the local frozen jets with frequencies theta'-log n.
Replace those frequencies by d_n, keeping the exact phase theta.
For j=1 the change is O(T^(-2)) times the j=0 sum in (11);
for j=2 use |(d+delta)^2-d^2|<=2|delta|d+delta^2 and (11),
where delta=theta'-lambda=O(T^(-2)). Thus the change is
O(T^(-7/4)) for both orders, and zero for order zero. Define

    v_j(t)=2 Re(e^(i theta(t)) i^j (P_j(t)+B_j(t))).

Uniformly, including transition heights,

    Z^(j)(t)=v_j(t)+r_j(t),
    |v_j(t)|<=C T^(1/4),
    |r_j(t)|<=C T^(-1/4)L^j,  j=0,1,2.                    (12)

These statements reuse L317's analytic AFE/Cauchy conclusion;
they do not differentiate a real error or a moving finite sum.
Multiplying (12) shows

    |Z'^2-Z Z''-(v_1^2-v_0 v_2)|<=C L^2.                (13)

For example the largest linear remainder is |v_0 r_2|<=C L^2;
the products of remainders are O(T^(-1/2)L^2). The separate
theta'-to-lambda change in the quadratic expression is
O(T^(-3/2)) pointwise, so it is included in (13).

L471 (7), with the exact A above, is the zero-safe identity

    W=Z'^2-Z Z''-(log A)''Z^2.                            (14)

By L471's curvature bound, (log A)''=O(T^(-2)); (12) bounds
Z^2 by C T^(1/2). Its integral cost is therefore O(T^(-1/2)),
already negligible here. This bound uses no moment theorem;
the sharper O(L/T) from L471 is unnecessary. Consequently

    integral |W-(v_1^2-v_0 v_2)| <= C T L^2.              (15)

There is no division by Z, and every real zero, of any
multiplicity, is included.

### 3. Freezing the quadratic expression and checking the factor 4

Put p_j=2 Re(e^(i theta)i^j P_j), b_j=2 Re(e^(i theta)i^j B_j).
Then v_j=p_j+b_j exactly, and (8)--(10) give
||p_j||_2<=C sqrt(T)L^(j+1/2), ||b_j||_2<=C sqrt(T).
The exact difference of the quadratic forms is

    (v_1^2-v_0 v_2)-(p_1^2-p_0 p_2)
       =2p_1 b_1+b_1^2-p_0 b_2-b_0 p_2-b_0 b_2.

Cauchy--Schwarz bounds its L1 norm by
C T(L^(3/2)+1+L^(1/2)+L^(5/2)+1). With (15) this proves

    integral |W-(p_1^2-p_0 p_2)|<=C T L^(5/2).           (16)

Here p_0=2 Re(e^(i theta)P_0), p_1=-2 Im(e^(i theta)P_1),
p_2=-2 Re(e^(i theta)P_2). The identities
2(Im z)^2=|z|^2-Re(z^2) and
2 Re z Re w=Re(z conjugate(w))+Re(zw) yield

    p_1^2-p_0 p_2
       =2|P_1|^2+2 Re(P_0 conjugate(P_2))
                       +2 Re(e^(2i theta)(P_0 P_2-P_1^2)).

Subtracting the nominated 4|P_1|^2 gives exactly (1), proving
(3). Applying ||x|-|y||<=|x-y| and integrating proves (4).
Symmetrize the ordered n,m coefficient in each term of (1).
Both give (d_n-d_m)^2=log(n/m)^2, which proves (2).
In particular every diagonal coefficient is zero. No change
to the surrogate or its factor 4 has been made.

### 4. Signed cancellation, and the remaining absolute norm

For unequal n,m<=M put a=log(M/n), b=log(M/m) and
D=a+b=log(M^2/(nm))>0. Then |log(n/m)|=|a-b|<=D.
The sum phase f(t)=2theta(t)-t log(nm) obeys

    f'(t)=log(t/(2pi nm))+O(T^(-2))>=D/2,
    f''(t)=1/t+O(T^(-3))>0                               (17)

for all sufficiently large T. To check uniformity at the
potentially small endpoint, the largest product of distinct
indices is M(M-1), so D>=log(M/(M-1))>=1/M. Also T>=2pi M^2.
The O(T^(-2)) error is therefore uniformly smaller than D/2.
The excluded case n=m has zero coefficient in (2), even when
T=2pi M^2. Integrating by parts with 1/f' and using f''>0 gives

    |integral_T^(2T) e^(i f(t))dt|<=2/f'(T)<=4/D.          (18)

Indeed its two boundary terms plus the integral of f''/f'^2
sum to 2/f'(T). The difference phase has the elementary bound
2/|log(m/n)|. Multiplication by the coefficient in (2) now
bounds either contribution by C D/sqrt(nm), since
log(n/m)^2/D<=D and |log(n/m)|<=D. Finally,

    sum_(n,m<=M) log(M^2/(nm))/sqrt(nm)
       =2 (sum_(n<=M)log(M/n)/sqrt(n))
           (sum_(m<=M)1/sqrt(m)) <= C M.                  (19)

The two single sums are O(sqrt(M)), by elementary integral
comparison, or the same convergent dyadic blocks as in (11).
Equations (18)--(19) prove the signed bound in (5), including
the endpoint case. Taking absolute values first in (1), then
using (8) and Cauchy--Schwarz, gives

    integral |R_T|<=4(||P_0||_2||P_2||_2+||P_1||_2^2)
                  <= C T L^3,

which is only the full scale. Dividing (4) by T L^3 proves
the two transfer assertions in the conclusion, because
L^(-1/2) tends to zero. This finishes the reduction; it leaves
the phase-sensitive absolute norm in (1)--(2) unresolved.

### 5. Separate critical audit, 29 October 2026

The audit accepts (1)--(5) as stated, with no mathematical repair.
Its scope is the finite argument above, conditional on the cited
analytic conclusions, not an independent proof of L317's AFE input.
In L317 (1) set a=t and retain only j=0,1,2; its N is exactly
N_t. The indices 1,...,N_t consist of 1,...,M together with the
indices activated in (9). Its error uses log t, which is uniformly
comparable to L on this interval. The analytic
remainder in L316 (7) gives both phase errors used here by Cauchy
estimates. L471 (7) has the identical A, ordinary derivatives and
the curvature bound needed in (14). These applications introduce
no assumption on zeros or on the sign of a jet.

For (6), the near-diagonal summand is at most
sqrt(m/n)/(m-n)<=sqrt(2)/(m-n); the complementary sum for each
m is bounded independently of m. Thus the whole sum is
O(M log(2M)), not O(M^2). For a fixed or activated pair, the
weight in (7) includes 1/sqrt(nm), is nonnegative and increasing,
and is continuously differentiable on its own closed interval.
No regularity across an activation point is required. In (9)
M<n implies tau_n>T, while n<=K implies tau_n<=2T. For j=0
the initial boundary is nonzero and is included in (7); for j=1,2
the later entering factor vanishes there. A degenerate interval
contributes zero. The diagonal costs are respectively
O(T L^(2j+1)) and O(T); the off-diagonal costs are
O(M L^(2j+1)) and O(K log(2K)). Since M,K=O(sqrt(T)), these
prove exactly (8) and (10), uniformly in the fractional part of X.

In (11) the summable block majorant
2^(-r/2)(1+r)^j includes the final block at n=1, so no logarithm
is lost in the O(T^(1/4)) bound for v_j. The frequency replacement
costs O(T^(-7/4)) for j=1,2, smaller than the retained jet errors.
Expanding the error in the quadratic form gives

    2v_1 r_1+r_1^2-v_0 r_2-r_0 v_2-r_0 r_2.

The linear terms have bounds O(L), O(L^2), O(1), respectively;
both quadratic terms are O(T^(-1/2)L^2). The curvature costs
O(T^(-3/2)) pointwise and O(T^(-1/2)) after integration. The
five cutoff-replacement terms in Section 3 have L1 costs
O(T L^(3/2)), O(T), O(T L^(1/2)), O(T L^(5/2)), O(T), in
their displayed order. Thus the largest cost is precisely the
stated O(T L^(5/2)), uniformly through all transition heights.

For an independent coefficient check in Section 3, the real part
of P_0 conjugate(P_2) has ordered coefficient d_m^2 and phase
t log(m/n). Averaging with the swapped pair gives
(d_m^2+d_n^2)/2; the coefficient of |P_1|^2 is d_n d_m.
The factor 2 in (1) therefore gives (d_n-d_m)^2. The same
symmetrization applies to P_0 P_2-P_1^2 in the product phase.
This verifies both the subtraction of 4|P_1|^2 and the ordered
pair convention in (2); no diagonal term survives.

For every remaining pair, nm<=M(M-1), including when X=M.
Consequently D>=log(M/(M-1))>=1/M. A single sufficiently large
T makes the uniform O(T^(-2)) error at most D/2 for every pair
and every t in the interval, because M=O(sqrt(T)). Also f''>0
uniformly. The two boundary bounds are 1/f'(T), 1/f'(2T),
and the remaining integral is
1/f'(T)-1/f'(2T); their sum is 2/f'(T). Thus the small endpoint
derivative causes no omitted stationary or boundary case.
The difference-phase bound, multiplied by its coefficient, is
2|a-b|/sqrt(nm); the sum-phase bound is at most
4(a-b)^2/(D sqrt(nm)). Both are at most C D/sqrt(nm).
The finite factorization (19), with its two O(sqrt(M)) sums,
then proves O(M)=O(sqrt(T)) for the signed integral. This is
signed cancellation only.

Finally (4) is the integrated reverse triangle inequality, and
its normalized error is O(L^(-1/2)). This verifies both directions
of the little-o transfer and the strictly-smaller-constant form
of the lower-bound transfer. The proof establishes neither side
of either proposed absolute threshold. The separate L1 upper
bound in (5) remains at full scale; G_T>=0 only gives N(T)<=E(T).
The existing DAG inputs match these uses. No numerical sampling,
infinite-time norm theorem or independence of arithmetic phases
enters this audit.

## Mathlib

Full matching theorem: not checked. Supporting finite sums,
integration by parts and Cauchy--Schwarz: no specific Mathlib
declarations checked. Unknown coverage is not absence.

The reused analytic input is L317's local specialization of the
Hardy--Littlewood approximate functional equation, Titchmarsh,
second edition revised by Heath-Brown (1986), Theorem 4.15 and
(4.12.4), printed pp. 79, 81--84, with fixed closed substrips of
0<Re(s)<1 and 2pi xy=Im(s)>0, as assessed previously:
[primary book](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf).
No fresh independent audit of that source or L317 is claimed.
L316's analytic phase expansion and L471's completion curvature
reuse logarithmic complex Stirling and its sector remainder,
[DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii).
The finite endpoint bounds above are proved because the local jet
theorem does not freeze the cutoff over a dyadic interval. No
Montgomery--Vaughan constant, infinite-time mean-value theorem,
unread differentiated-remainder theorem or additional zero
hypothesis is imported.

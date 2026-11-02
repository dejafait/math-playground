# Lemma 574: prime-block lower bound for the normalized density contrast

## Hypotheses

Let T be real and tend to infinity. Use natural logarithms and put

    L=log T, h=1/L, M=floor(sqrt(T/(2 pi))),
    J=[T+h,2T-h], ell=|J|=T-2h,
    A_sigma(t)=sum_(1<=n<=M)n^(-1/2-i sigma)n^(-it),
    F_sigma(t)=|A_sigma(t)|^2,
    D_h=F_h-2F_0+F_(-h),
    Q_T=F_h+2F_0+F_(-h)+L.

Thus F_sigma(t)=F_M(t+sigma) in C481a. For this T the integer M
is fixed at every height and shift. Set

    x=T^(1/16), y=T^(1/8),
    B_T={p prime: x<p<=y},
    B(t)=sum_(p in B_T)p^(-1/2-it), P_T(t)=-Re B(t),
    S=sum_(p in B_T)1/p, H_j=sum_(1<=n<=j)1/n (H_0=0).

In sums below p,q run through B_T, and a double sum is ordered.
The finite mean-square theorem and Mertens' second theorem cited in
the proof are imported unconditionally. No RH, zero-free estimate,
phase independence, disjoint prime supports or moving cutoff is used.

## Conclusion

There is an absolute T_0 such that for every real T>=T_0,

    integral_J D_h(t)P_T(t) dt >= c_1 T L,
    integral_J Q_T(t)P_T(t)^2 dt <= 8 T L,                (1)

where c_1=sin(1/32)^2 log(2)/8>0. More precisely the first integral is

    4 ell sum_p sin(log p/(2L))^2 H_floor(M/p)/p
          +O(T^(5/8)L).                                 (2)

Here is the complete diagonal formula for the second integral, with
its finite-height error. For sigma in {-h,0,h}, define

    C_sigma=S H_M
       +sum_(p!=q) (p/q)^(i sigma) H_floor(M/max(p,q))/(pq),
    E_sigma=sum_(p,q) (pq)^(i sigma) H_floor(M/(pq))/(pq),
    w_(-h)=w_h=1, w_0=2.

Then C_sigma is real and nonnegative, and

    integral_J Q_T P_T^2
      =(ell/2)[sum_sigma w_sigma(C_sigma+Re E_sigma)+L S]
          +O(T^(3/4)L).                                 (3)

All implied constants are absolute. In particular, for
c=c_1^2/8=sin(1/32)^4 log(2)^2/512>0,

    integral_J D_h(t)^2/Q_T(t) dt >= c T L,
    integral_J |D_h(t)| dt >= c T L.                     (4)

The continuous real function g_T=D_h/Q_T satisfies |g_T|<=1 and
integral_J D_h g_T>=c T L. This is an actual bounded density-dual
witness; P_T itself is not claimed to have a uniform pointwise bound.
Using C481a for precisely its complete ordered-pair component

    U_T(t)=sum_(n,m<=M)log(n/m)^2 exp(it log(m/n))/sqrt(nm),

one obtains

    integral_T^(2T)|U_T(t)|dt >= c T(log T)^3.            (5)

This settles the positive-mass premise of C481a within this argument.
It does not compare U_T with L477's full residual, whose other phase
can cancel it. Neither defect threshold, a negative-mass saving, nor
any Xi sign follows. The onset T_0 has not been made numerical.
The separate finite audit in Section 6 verifies this argument, retaining
the two named source theorems as imports rather than independently
auditing their proofs. The prior search did not identify this exact
specialization; no certified originality or progress beyond all existing
literature is claimed.

## Proof

### 1. Imported tools and their interval and bilinear specializations

Import Michael J. Curran, *Correlations of the Riemann zeta function*,
arXiv:2303.10123v2, 15 May 2024,
[Section 2, Lemma 2.3](https://arxiv.org/html/2303.10123v2#S2).
For arbitrary finite complex coefficients z_n supported on n<=N,
the unconditional Montgomery--Vaughan mean-square statement there is

    integral_R^(2R)|sum z_n n^(-it)|^2 dt
       =R sum |z_n|^2+O(N sum |z_n|^2).                  (6)

The constant is uniform in the coefficients. The paper's conditional
zeta results and its disjoint-prime-support Lemma 2.4 are not used.
We import (6), not its proof.

For J use R=ell and t=u+3h. The endpoints map exactly:
ell+3h=T+h and 2ell+3h=2T-h. Multiplying z_n by n^(-3ih)
preserves its norm and gives

    integral_J |sum z_n n^(-it)|^2 dt
       =ell ||z||_2^2+O(N||z||_2^2).                    (7)

This is an exact interval translation, not deletion of boundary
strips or replacement of ell by T in a signed integral.

The associated sesquilinear error form is Hermitian and has
|E(z,z)|<=K N||z||_2^2 by (7), for an absolute K. For unit
coefficient vectors u,v its complex polarization identity bounds
|E(u,v)| by (K N/4) sum_(j=0)^3 ||u+i^j v||_2^2=2K N.
Scaling the two vectors separately, with zero vectors immediate,
therefore gives

    integral_J (sum u_n n^(-it)) conjugate(sum v_n n^(-it)) dt
       =ell sum u_n conjugate(v_n)+O(N||u||_2||v||_2).    (8)

Pad shorter vectors with zeros. This is only the finite polarization
application of the imported theorem; no diagonal term is presumed
to be an exact time average. The common translation in (7) cancels
in the coefficient inner product in (8).

Import classical Mertens' second theorem, in the precise real-endpoint
form stated by Mark B. Villarino, *Mertens' Proof of Mertens' Theorem*,
math/0504289v3, 17 May 2005,
[Theorem 6, printed p. 7, (2.3.4)--(2.3.5)](https://arxiv.org/pdf/math/0504289v3#page=7):
sum_(p<=z)1/p=log log z+b+O(1/log z), for real z>2.
Its proof is not reproduced or independently audited here. Subtracting
at the actual real endpoints x,y yields

    S=log 2+O(1/L).                                     (9)

In particular log(2)/2<=S<=1 for all sufficiently large real T.
The strict lower and weak upper prime endpoints are preserved by
this subtraction, including when either endpoint is prime.

### 2. Complete grouped coefficients and their norms

Write N_1=floor(M y), N_2=floor(M y^2). They satisfy
N_1<=T^(5/8) and N_2<=T^(3/4). For all sufficiently large T,
H_M<=1+log M<=L and ||A_sigma||_coeff^2=H_M, uniformly in
sigma. Throughout, a coefficient norm means the squared sum after
equal integer products have been grouped.

The coefficient of k^(-it) in A_sigma B is

    c_sigma(k)=k^(-1/2)
       sum_(p|k, p in B_T, k/p<=M)(k/p)^(-i sigma).      (10)

Expanding its squared norm amounts to summing all mp=nq with
m,n<=M and p,q in B_T. If p=q then m=n, contributing S H_M.
If p!=q, primality forces m=q r and n=p r for a positive integer
r<=M/max(p,q). The product of coefficients is
(p/q)^(i sigma)/(pq r). These two exhaustive cases prove

    ||A_sigma B||_coeff^2=C_sigma,
    0<=C_sigma<=H_M(S+S^2)<=2L.                         (11)

The complex-looking off-diagonal sum in C_sigma is real because
interchanging p,q conjugates it. The inequality uses its absolute
value; it does not discard off-diagonal coincidences or assume
disjoint supports. Any extra block primes dividing r are already
included in these same representations.

For A_sigma B^2 the coefficient of k^(-it) is

    d_sigma(k)=k^(-1/2)
       sum_(p,q, pq|k, k/(pq)<=M)(k/(pq))^(-i sigma).    (12)

Let r_2(k) count the ordered representations in (12), including
p=q when p^2 divides k. If k<=N_2, the number of its prime factors
from B_T counted with multiplicity is less than 12: twelve would
give k>x^12=T^(3/4), contrary to k<=N_2<=T^(3/4).
Consequently r_2(k)<=144. Cauchy--Schwarz on the finite sum in
(12), followed by summation of every representation, gives

    sum_k |d_sigma(k)|^2
       <=144 sum_k r_2(k)/k
       =144 sum_(m<=M,p,q)1/(mpq)
       =144 H_M S^2<=144L.                             (13)

This bound allows all overlaps and repeated primes. It includes
m=1; it is not the disjoint-prime splitting theorem. Likewise

    ||B||_coeff^2=S,
    ||B^2||_coeff^2=2S^2-sum_p 1/p^2<=2S^2.             (14)

Indeed a product pq with p!=q has two ordered representations and
a square p^2 has one. Unique factorization supplies all cases in
(14). The lengths of B and B^2 are at most floor(y) and floor(y^2).

### 3. The signed moment

Apply (8) to A_sigma B and A_sigma, with common length N_1.
Their shared index k satisfies k=mp<=M on the A_sigma side.
The paired coefficient is p^(i sigma)/(mp). Hence, using
(11) and ||A_sigma||_coeff^2=H_M,

    integral_J F_sigma(t)B(t)dt
       =ell sum_p p^(i sigma)H_floor(M/p)/p
            +O(T^(5/8)L).                              (15)

There is no restriction of m other than m<=floor(M/p), and the
lower endpoint m=1 is retained. Since P_T=-Re B, taking the
combination of (15) with weights 1,-2,1 at h,0,-h gives (2):
the resulting scalar is -(e^(ih log p)-2+e^(-ih log p))
=4 sin(log p/(2L))^2. This sign and factor do not use an
approximation to the shifts.

For every prime in the block,

    1/32<log p/(2L)<=1/16,
    sin(log p/(2L))^2>=s_0:=sin(1/32)^2>0.              (16)

For large T, M>=sqrt(T/(2pi))/2, so
M/p>=T^(3/8)/(2 sqrt(2pi)). The elementary integral bound
H_j>=log(j+1) for j>=0 implies

    H_floor(M/p)>=log(M/p)
       >=(3/8)L-log(2 sqrt(2pi))>=L/4.                 (17)

This uses the actual floor, not an asymptotic valid only between
cutoff transitions. Also ell>=T/2 eventually. Combining (9),
(16) and (17), the main term in (2) is at least
s_0 log(2) T L/4. Its error divided by T L is O(T^(-3/8));
enlarging T_0 absorbs half that positive lower bound. This proves
the first part of (1) with c_1=s_0 log(2)/8.

### 4. The exact denominator-weighted second moment

For every t, since P_T is real,

    P_T(t)^2=(1/2)|B(t)|^2+(1/2)Re(B(t)^2).             (18)

This is the algebraic square identity, with its second term retained.
By (7), (11), and the true length N_1,

    integral_J F_sigma |B|^2
       =ell C_sigma+O(T^(5/8)L).                       (19)

By (8), (13), and the true length N_2, pair A_sigma B^2
with A_sigma. Equality of indices requires mpq=n<=M, with paired
coefficient (pq)^(i sigma)/(mpq). Therefore

    integral_J F_sigma B^2
       =ell E_sigma+O(T^(3/4)L),
    |E_sigma|<=H_M S^2<=L.                             (20)

Both ordered pairs p,q and their repeated-prime case p=q remain
in E_sigma. All factors p^(i sigma), (p/q)^(i sigma) and
(pq)^(i sigma) came from the actual translated A_sigma. Thus
(18)--(20) give, for each of the three shifts,

    integral_J F_sigma P_T^2
       =(ell/2)(C_sigma+Re E_sigma)+O(T^(3/4)L).        (21)

For the additive L in Q_T, (7) gives
integral_J |B|^2=ell S+O(y S). Pair B^2 with the constant
polynomial 1 in (8), using (14) and common length floor(y^2).
The constant coefficient of B^2 is zero, because all its indices
are products of two primes. Hence integral_J B^2=O(y^2 S).
Equation (18) consequently implies

    integral_J P_T^2=(ell/2)S+O(y^2).                  (22)

Multiply (21) by w_sigma and (22) by L. This proves (3),
including its O(T^(3/4)L) error since y^2=T^(1/4).
Using C_sigma<=2L, |E_sigma|<=L, sum w_sigma=4 and S<=1,
its main term is at most (13/2)T L. The error divided by T L
is O(T^(-1/4)). After enlarging T_0 this is at most 8T L,
which proves the second part of (1). The constants and lengths
are uniform at every sufficiently large real T, including prime
block and M floor transitions. No finite-height remainder or
boundary strip has been omitted.

### 5. Normalized, bounded-dual and curvature comparisons

All functions here are finite sums and continuous on the compact
interval J. Q_T>=L>0. Weighted Cauchy--Schwarz applied to
D_h/sqrt(Q_T) and sqrt(Q_T)P_T gives

    (integral_J D_h P_T)^2
       <=(integral_J D_h^2/Q_T)(integral_J Q_T P_T^2).

Combining both bounds in (1) proves the first bound in (4) with
c=c_1^2/8. The pointwise nonnegativity of each F_sigma gives

    |D_h|<=F_h+2F_0+F_(-h)=Q_T-L<=Q_T.

Therefore D_h^2/Q_T<=|D_h|, proving the second bound in (4).
The same inequality gives |g_T|<=1, and the identity
D_h g_T=D_h^2/Q_T proves the bounded-dual assertion. This uses
the two intensities F_h+F_(-h) and 2F_0 directly with denominator
equal to their sum plus L. Their masses are not normalized or
presumed equal. No unbounded probe has been called bounded and
no clipping step or probability-measure duality is required.

C481a, conclusion (3), applies with exactly this real T, fixed M,
h and J and the complete U_T stated above. It supplies

    integral_J |D_h|<=h^2 integral_T^(2T)|U_T|.

Its triangular kernel includes both boundary strips. Since
h^(-2)=L^2, (4) proves (5) with the same c and at every sufficiently
large real T. L477's other oscillatory component is never removed
from any assertion about its full residual. The L481 fourth-moment,
L482 uniform saturation and L572 rank-certificate limitations concern
different certificates; none is an upper bound contradicting (5).

### 6. Independent finite audit, 31 October 2026

This audit uses the previously saved SPECIALIZE assessment
`drafts/literature/2026-10-31-l574-prime-block-independent-audit.md`.
It checks the existing argument, not a new lower-bound mechanism.
Curran Lemma 2.3 and the named Mertens theorem remain unconditional
imports with the precise statements and versions in Section 1; their
source proofs are not independently verified here. C481a's finite
calculus input is retained and its applicability is checked below.
No missing source hypothesis or mathematical correction was found.

**Grouped products and phases.** In the inner product of A_sigma B
with itself, index equality mp=nq has exactly two cases. For p=q
it requires m=n. For distinct primes p,q it forces m=qr,n=pr,
with precisely r<=floor(M/max(p,q)). The paired coefficient is
(p/q)^(i sigma)/(pq r). Thus (11) is the entire squared coefficient
norm; it is nonnegative even though its displayed off-diagonal terms
need not be. Pairing A_sigma B with A_sigma instead requires
mp=n<=M and gives p^(i sigma)/(mp). Pairing A_sigma B^2 with
A_sigma requires mpq=n<=M and gives (pq)^(i sigma)/(mpq).
These verify every diagonal and all three phases in (11), (15)
and (20). Extra prime divisors of m, n or r create no omitted case:
expansion sums over each ordered representation before grouping.

For a product k in A_sigma B^2, let d be its number of block-prime
factors counted with multiplicity. The strict lower endpoint p>x
implies k>x^d whenever d>0. Since k<=M y^2<=T^(3/4), d<12.
There are at most d^2 ordered choices of a prime pair dividing k,
which also bounds the choices with p=q and p^2|k. Therefore 144
is a valid uniform bound for r_2(k). Each representation contributes
exactly 1/(mpq) when the Cauchy--Schwarz bound (13) is summed.
For B^2, unique factorization separately gives coefficient 2/sqrt(pq)
for distinct primes and 1/p for a repeated prime, hence exactly
2S^2-sum_p p^(-2) for its squared norm. No independence or
disjoint-prime-support result has entered either count.

**Finite-height errors.** The translated error form in (7) is
Hermitian. Polarizing unit vectors uses the sum of four squared
norms equal to 8; separate normalization then yields (8), with
an absolute constant and with the common product length retained.
The translation t=u+3h maps [ell,2ell] exactly onto J. Its
unit-modulus coefficient factors cancel on every shared index,
so they cannot alter any of the diagonal phases above.

In (15), the two coefficient norms are at most sqrt(2L) and
sqrt(L), and their common length is N_1<=T^(5/8). In (19)
the squared norm is at most 2L at this same length. In (20)
the two norms are at most 12sqrt(L) and sqrt(L), at common
length N_2<=T^(3/4). For (22) the mean-square error for B is
O(y S), and the B^2/1 pairing error is O(y^2 S), since its
constant coefficient is zero and its norm is at most sqrt(2)S.
Multiplication by L costs O(T^(1/4)L), which is smaller than
the retained O(T^(3/4)L) bound. Consequently there are fixed
absolute K_1,K_2 such that the absolute errors in (2) and (3)
are at most K_1 T^(5/8)L and K_2 T^(3/4)L respectively.
These are finite-interval estimates, not exact diagonal averages.

**Uniform constants and every real height.** Mertens' theorem at
real x,y gives S=log 2+O(1/L) with an absolute constant, even
at prime endpoints. Once T is large, choose simultaneously

    log(2)/2<=S<=1, H_M<=L, ell>=T/2,
    M>=sqrt(T/(2pi))/2,
    L>=8 log(2 sqrt(2pi)).

For every prime in the whole block these conditions imply
H_floor(M/p)>=log(M/p)>=L/4. The sine argument is between
1/32 and 1/16, inside its increasing range. Thus the main term
in (2) is at least 2c_1 T L. Its subtraction error leaves at
least c_1 T L as soon as K_1 T^(-3/8)<=c_1. Meanwhile (3)'s
main term is at most (13/2)T L, using sum w_sigma=4,
C_sigma<=2L, |E_sigma|<=L and S<=1. It is at most 8T L
including the absolute error once K_2 T^(-1/4)<=3/2.

All these are eventual inequalities for every real T, not a
subsequence. For example the last two requirements are met above
max{(K_1/c_1)^(8/3),(2K_2/3)^4}; taking a larger single T_0
also meets all preceding conditions and C481a's T>=e^2.
No numerical value is claimed for the imported constants or this
onset. The inequalities use the actual floor M and actual prime
block at each T; none differentiates them or assumes continuity
across their transitions. This verifies precisely both thresholds
in (1), with the stated c_1, rather than only the sign of a diagonal.

**Normalized dual and full boundary transfer.** On the compact J,
Q_T>=L>0, and D_h,P_T,Q_T are real continuous finite-sum
functions. Weighted Cauchy--Schwarz is therefore applicable with
no limiting or integrability condition left over. Its numerator
is at least c_1^2 T^2 L^2 and its weighted cost is at most 8T L,
so it gives c_1^2 T L/8 exactly as in (4). The pointwise bound
|D_h|<=Q_T-L<=Q_T implies both D_h^2/Q_T<=|D_h| and
|g_T|<=1; the bounded witness is g_T, not the prime polynomial.
No equal-mass probability normalization is used.

For precisely this fixed M, finite differentiation gives
F_M''=-U_T, including both ordered pairs and their zero diagonal.
C481a applies at the same T,h,J. Its nonnegative integrated kernel
q_T is supported on all of [T,2T], includes both endpoint strips,
and satisfies q_T<=h^2 everywhere. Its full inequality is

    c T L <= integral_J |D_h|
       <= integral_T^(2T) q_T(x)|U_T(x)| dx
       <= h^2 integral_T^(2T) |U_T(x)| dx.

Thus the constant c=c_1^2/8 is preserved in (5), with no strip
subtraction and no new error or onset. This validates L574's
claimed normalized density mass and its ratio-component consequence.
It supplies no bound on the pairing or cancellation of L477's
other, theta-chirped component. Both defect thresholds, negative
mass and all-height Xi positivity remain unresolved. L573 is not
an input; the L481/L482/L572 stops remain evidence about their
particular certificates, rather than counterexamples to this result.

## Mathlib

Full matching and supporting Mathlib coverage have not been checked.
The imported finite mean square, Mertens theorem, finite coefficient
grouping, weighted Cauchy--Schwarz and C481a application above are an
informal proof. Unknown Mathlib availability is not evidence of absence.

# Lemma 481: short-resonator concentration of the complete residual

## Hypotheses

Use L477's exact real residual and fixed cutoff, written as in L480:

    L=log T, M=floor(sqrt(T/(2 pi))), N=floor(T^(1/24)),
    Q=N^3, K=M Q, T<=t<=2T,
    c_nm=log(n/m)^2/sqrt(nm),
    U(t)=sum_(n,m<=M)c_nm exp(it log(m/n)),
    V(t)=sum_(n,m<=M)c_nm exp(-it log(nm)),
    R_T(t)=U(t)+Re(exp(2i theta(t))V(t)),
    F(t)=sum_(n<=N)n^(-1/2-it),
    S(T)=integral_T^(2T)R_T(t)|F(t)|^6 dt,
    H(T)=integral_T^(2T)|F(t)|^8 dt,
    I_j(T)=integral_T^(2T)|R_T(t)|^j dt.

All pair sums are ordered. The actual theta is
Im log Gamma(1/4+it/2)-t log(pi)/2. Retain L479 Section 1's
uniform phase expansion and scalar saddle normalization, with the
primary citation below. Retain audited L480's I_2 comparable to
T L^8 only for the final interpolation consequence. T tends to
infinity through arbitrary real values. No RH, zero simplicity,
spacing, external half-plane, independent-phase or conjectural
zeta-moment hypothesis is imposed. Constants and onsets are absolute
and existential. The separate critical audit in Section 7 accepts
the bounds below, retaining the named analytic inputs as cited.

## Conclusion

For every sufficiently large real T there are fixed c,C>0 such that

    S(T)>=c T L^18,       H(T)<=C T L^16,
    I_4(T)>=c T L^24.                                      (1)

In particular L480's exact second/fourth-moment certificate satisfies

    I_2(T)^(3/2)/I_4(T)^(1/2)<=C T,
    [I_2(T)^(3/2)/I_4(T)^(1/2)]/(T L^3)<=C L^-3 -> 0.       (2)

This stops that interpolation certificate at every sufficiently large
height, hence along every unbounded sequence. It does not bound I_1
above by this certificate, settle either L477 L1 threshold, transfer
its unweighted error through |F|^6, prove a negative-mass saving or
establish any individual-height sign or all-degree mixed positivity.

The complete signed calculation below supplies a nonnegative chirped
resonant sum and uniform errors O(T^(5/8)L^19). It does not assume
that the chirped integral itself is nonnegative. This is a local
specialization of established correlation methods; the recorded
source search found no matching complete-residual theorem, which
does not establish originality.

## Proof

### 1. Imported estimates and finite coefficients

Heap--Soundararajan, *Lower bounds for moments of zeta and L-functions
revisited*, arXiv:2007.13154v1, 26 July 2020, Section 5, p. 9,
equation (14) and its preceding calculation
([primary version](https://arxiv.org/pdf/2007.13154v1)), give, for
an arbitrary finite complex sequence z_k supported on k<=J,

    integral_T^(2T)|sum_(k<=J)z_k k^(-it)|^2 dt
      =T sum_(k<=J)|z_k|^2
         +O(J log(2J) sum_(k<=J)|z_k|^2).                  (3)

The harmless log(2J) includes J=1. We use (3) with the actual
finite interval and growing lengths J=K and J=N^4, retaining its
error. It needs no coprime-support factorization such as the source's
later equation (16). Polarization and scaling give its bilinear
consequence, with error

    O(J log(2J) ||u||_2 ||v||_2)                          (4)

after subtracting T sum u_k conjugate(v_k). In detail, the error
is a Hermitian quadratic form bounded by C J log(2J)||z||_2^2
for every z. Apply its polarization identity to scaled u,v having
equal norms to obtain (4); zero sequences are immediate. Thus the
constant in (4) is absolute, including when the coefficients vary.
This is an application of the cited theorem, not a new mean-square
theorem or an infinite-time orthogonality assumption.

Write d_j(k;N) for the number of ordered j-tuples of positive integers
at most N with product k, and d_j(k) for the unrestricted count.
We use the elementary upper bound

    d_4(k;N)<=d_4(k),
    d_4(k)^2<=d_16(k),
    sum_(k<=J)d_4(k)^2/k<=(1+log J)^16,       J>=1.        (5)

For completeness the middle inequality has a finite injection proof.
Given two ordered four-factor factorizations of k, at each prime
power p^e||k their exponent vectors are two four-part compositions
of e. Fill a 4 by 4 nonnegative integer matrix in row order, assigning
the minimum of the remaining row and column totals at each step.
Equal total sums ensure completion. Multiplying the resulting prime
powers cell by cell produces an ordered sixteen-factor factorization
of k. Its row and column products recover both original quadruples,
so this deterministic map is injective. The last inequality in (5)
follows by enlarging the positive sum over sixteen factors of product
at most J to sixteen independent factors at most J, and using
sum_(n<=J)1/n<=1+log J. This short coefficient argument verifies the
needed uniform bound with the truncated supports; no divisor-square
asymptotic or its leading constant is assumed or reproved.

The correlation/Holder strategy is the established one in
Rudnick--Soundararajan, *Lower bounds for moments of L-functions*,
arXiv:math/0502042v1, Theorem and proof pp. 2--4
([primary version](https://arxiv.org/pdf/math/0502042v1)), and
Heap--Soundararajan Section 6. Their L-function lower bounds do not
apply directly to R_T. The weighted diagonal and full chirped estimate
below are the residual-specific differences requiring proof.

### 2. The auxiliary norm and nonchirped diagonal

The coefficients of F^4 are d_4(k;N)/sqrt(k), supported on k<=N^4.
Since N^4<=T^(1/6), (3) and (5) prove

    H(T)<=(T+C N^4 log(2N^4))(1+log(N^4))^16
         <=C T L^16.                                    (6)

For j=0,1,2 put

    A_j(t)=[sum_(n<=M)(log n)^j n^(-1/2-it)] F(t)^3
          =sum_(k<=K)b_j(k) k^(-it),
    b_j(k)=k^(-1/2) sum_(na=k; n<=M) (log n)^j d_3(a;N).

For j=0 the power is 1, including n=1. All b_j are real and
nonnegative. Since b_0(k)<=d_4(k)/sqrt(k) and
b_j(k)<=(log M)^j b_0(k), (5) gives

    ||b_j||_2<=C L^(j+8),                 j=0,1,2.         (7)

The identity log(n/m)^2=(log n)^2+(log m)^2-2log n log m
now gives exactly

    U(t)|F(t)|^6=2 Re(A_2(t) conjugate(A_0(t)))-2|A_1(t)|^2.

Using (3), (4), (7), and log(2K)<=C L yields

    integral_T^(2T) U(t)|F(t)|^6 dt=T D(T)+O(K L^19),      (8)

where the complete equal-product diagonal is

    D(T)=sum_(n,m<=M; a,b<=Q; na=mb)
          d_3(a;N)d_3(b;N) log(n/m)^2/sqrt(nmab).         (9)

Indeed the diagonal of the displayed A_j identity gives (9) by
interchanging (n,a) with (m,b) in one of the square-log terms.
On na=mb=k its denominator is k. In particular every summand of
D(T) is nonnegative. All coincidences are grouped before (3) is used;
neither separate logarithmic frequencies nor independent phases are
being substituted for the finite polynomial.

### 3. A weighted diagonal of order L^18

Here is the elementary harmonic-counting fact needed for the
logarithmic weight in (9). Fix an integer r>=2 and intervals
0<=alpha_i<beta_i, 1<=i<=r. For X tending to infinity, let
J_i(X) consist of the positive integers n<=X^beta_i when alpha_i=0,
and X^alpha_i<n<=X^beta_i otherwise. Then

    sum_(x_i in J_i(X); pairwise gcd(x_i,x_j)=1)
                      1/(x_1 ... x_r)>=c (log X)^r        (10)

for a positive constant depending only on these fixed intervals.
We prove precisely this finite-box fact, rather than assume a
coprimality density for its varying logarithmic ranges.

Fix an integer B>=2 and let P be the product of primes at most B.
For each residue v modulo P, direct summation along that arithmetic
progression, or integral comparison with 1/x, gives

    sum_(n in J_i(X); n=v mod P)1/n
       =((beta_i-alpha_i)/P)log X+O_P(1).                 (11)

This includes v=0 and alpha_i=0. The bounded initial terms affect
only the O_P(1) term. There are finitely many residues for fixed B.
By the Chinese remainder theorem, summing their products subject
to no prime p<=B dividing two coordinates has main coefficient

    delta_B product_i(beta_i-alpha_i),
    delta_B=product_(p<=B)[(1-1/p)^r+(r/p)(1-1/p)^(r-1)],

times (log X)^r, with error O_B((log X)^(r-1)). The local factor
counts zero or one divisible coordinate among r independent uniform
residues. It is positive for each prime. The union bound on a pair
of divisible coordinates bounds it below by 1-binomial(r,2)/p^2.
For all sufficiently large primes this lower bound is at least 1/2;
log(1-u)>=-2u for 0<=u<=1/2 and sum_(n>=2)n^-2<infinity show
that delta_B is bounded below by one delta_*>0, uniformly in B.
Only a lower bound for finite products is used here.

The total harmonic weight of integers in J_i(X) divisible by any
particular prime p is at most

    (1/p) sum_(h<=X^beta_i/p)1/h<=C_i (log X)/p,           (12)

for X>=e; it is zero if the upper bound is below 1. The weight
without divisibility is at most C_i log X. Thus the union bound over
coordinate pairs and primes p>B bounds the total weight of tuples
with such a common prime by

    C (log X)^r sum_(p>B)p^-2<=C (log X)^r/(B-1).         (13)

The constants here are independent of B and X. Choose B fixed so
large that this is less than one quarter of
delta_* product_i(beta_i-alpha_i)(log X)^r. Then choose X large
so the error following (11) is less than another quarter. Subtract
(13) from the small-prime-admissible weight to prove (10).
This also treats coordinates equal to 1. No prime distribution or
uniformity in a growing modulus is assumed.

Apply (10) with r=16, X=N, to a 4 by 4 matrix (x_ij). Every
entry has interval 1<=x_ij<=N^(1/4), except for

    N^(1/8)<x_12<=N^(1/4),
    1<=x_21,x_31,x_41<=N^(1/48).

All sixteen logarithmic interval widths are fixed and positive.
Restrict to pairwise coprime entries. Define four row products r_i
and four column products s_j. Every r_i and s_j is at most N.
Since N<=M eventually, each such matrix supplies an allowed ordered
tuple in (9), by setting

    n=r_1, (a_1,a_2,a_3)=(r_2,r_3,r_4), a=a_1 a_2 a_3,
    m=s_1, (b_1,b_2,b_3)=(s_2,s_3,s_4), b=b_1 b_2 b_3.

The product equality na=mb=k=product_(i,j)x_ij holds exactly.
The ordered triples are precisely what the two d_3 factors count.
Pairwise coprimality implies x_ij=gcd(r_i,s_j), so the matrix is
recoverable from these ordered row and column products. Different
matrices therefore yield different counted tuples, without overcounting.
The harmonic factor 1/k is exactly product_(i,j)1/x_ij. Finally,

    log(n/m)=log(x_12 x_13 x_14/(x_21 x_31 x_41))
       >=(1/8-3/48)log N=(1/16)log N.                   (14)

Restricting the nonnegative sum (9) to these tuples and using (10)
therefore proves

    D(T)>=c (log N)^18>=c' L^18.                        (15)

The last inequality follows from N=floor(T^(1/24)) and
log N/L -> 1/24. This proves the weighted diagonal itself; an
unweighted d_4^2 asymptotic would not alone imply (15).

### 4. Scalar transformation with all summed endpoint errors

Set d_a=d_3(a;N). The finite expansion F^3=sum_(a<=Q)d_a a^(-1/2-it)
shows that the entire chirped correlation is

    C(T)=Re sum_(n,m<=M; a,b<=Q)
       [d_a d_b log(n/m)^2/sqrt(nmab)] J(n,m,a,b),
    J(n,m,a,b)=integral_T^(2T)
                exp(i(2theta(t)-t log(nma/b)))dt.         (16)

Use S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent. Math. 75 (1984), 123--141, Lemma 2,
p. 130, (24)--(25)
([primary PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf)).
For fixed real alpha, large A<B<=2A and arbitrary r>0, it states

    integral_A^B exp(it log(t/(r e))) (t/(2 pi))^(alpha-1/2)dt
      =1_(A<r<=B)(2 pi)^(1-alpha)r^alpha exp(-ir+i pi/4)
       +O(A^(alpha-1/2))
       +O(A^(alpha+1/2)/(|A-r|+sqrt A))
       +O(B^(alpha+1/2)/(|B-r|+sqrt B)).

Its constants are uniform in r. Use alpha=1/2, A=T, B=2T and
r=2 pi nma/b. These are permitted positive rational multiples of
2 pi. L479 Section 1 supplies the actual phase expansion
2theta(t)=t log(t/(2 pi e))-pi/4+O(1/T) uniformly on this interval.
The phase replacement changes each integral by O(1), uniformly in
the indices. Its constant phase cancels exp(i pi/4) from the source.
Consequently

    J=1_(T<r<=2T) 2 pi sqrt(nma/b) exp(-2 pi i nma/b)
         +O(1+K_T(r)+K_(2T)(r)),
    K_H(r)=T/(|H-r|+sqrt T),                  H=T,2T.       (17)

Replacing sqrt(2T) by sqrt T in an error changes only its constant.
The half-open indicator and both full-size endpoint errors remain.
No half-weight convention or separation from endpoint saddles is used.
L479's four-index summed error is not an input here.

First, the total coefficient mass in (16) is bounded by

    C L^2 (sum_(n<=M)n^-1/2)^2
           (sum_(a<=Q)d_a a^-1/2)^2
       <=C M N^3 L^2=C M Q L^2.                         (18)

Here sum d_a/sqrt(a)=(sum_(j<=N)j^-1/2)^3<=8N^(3/2).
Thus (18) pays for every O(1) error. If r<T/2 or r>4T both
endpoint kernels are O(1), including arbitrarily distant saddles.

In the remaining region T/2<=r<=4T, nma is comparable to T b,
and hence the coefficient in (16) is at most

    C d_a d_b L^2/(b sqrt T).                            (19)

Fix m,a,b and write r=h n, h=2 pi ma/b. If any n<=M lies
in this region, then h>=T/(2M)>=c sqrt T. For either endpoint
H, a lattice of spacing h has O(1) points within sqrt T of H
and O(1+2^j sqrt T/h) in the j-th dyadic annulus. There are
O(log T) relevant annuli because r,H are in fixed multiples of T.
The central layer costs O(sqrt T), while an annulus costs at most
C(sqrt T 2^-j+T/h). Therefore

    sum_(n<=M; T/2<=hn<=4T)K_H(hn)<=C sqrt T L.          (20)

The empty region contributes zero. This bound includes exact endpoint
coincidences, near misses, and both sides of each endpoint. Multiplying
(19) by (20) and summing the remaining indices uses exactly

    sum_(a<=Q)d_a=N^3=Q,
    sum_(b<=Q)d_b/b=(sum_(j<=N)1/j)^3<=C L^3.

Together with (18) it proves that the complete error from (17) is

    O(M Q L^6).                                         (21)

Thus neither the new six short factors nor either endpoint was paid
for with the older four-index error estimate.

### 5. The whole rational-phase sum

Let e(x)=exp(2 pi i x), Y=T/(2 pi). Inserting (17) in (16)
and multiplying its amplitude by the original coefficient gives

    C(T)=2 pi Re sum_(a,b<=Q; m<=M) (d_a d_b/b)
           sum_(n in J_(m,a,b)) log(n/m)^2 e(-nma/b)
           +O(M Q L^6),                                (22)

where J_(m,a,b) is the consecutive integer interval specified by
1<=n<=M and Yb/(ma)<n<=2Yb/(ma). This definition includes
empty intervals, fractional endpoints and the lower cutoff n=1.

If b divides ma, every exponential in the inner sum is exactly 1.
The complete contribution of all such triples is nonnegative. Denote
it by P(T), including the factor 2 pi in (22). We neither approximate
P(T) by an integral nor need to lower-bound its size.

For b not dividing ma, the finite geometric-series bound is

    |sum_(n in any consecutive interval)e(-nma/b)|
       <=C/||ma/b||,

where ||.|| is distance to the nearest integer. Explicitly, with
z=e(-ma/b)!=1 and integers u<=v, the sum is
z^u(1-z^(v-u+1))/(1-z). Its modulus is at most 2/|1-z|,
and |1-e(x)|=2|sin(pi x)|>=4||x||. Empty intervals give zero.
Tao, *245C Notes 2: The Fourier transform*, 6 April 2009,
Section 2, Lemma 17 and the finite cyclic case of Theorem 21
([primary notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/))
provide character orthogonality; they are not an imported theorem
for this incomplete interval or its following Abel-weighted bound.
On 1<=x<=M the weight f_m(x)=log(x/m)^2 has supremum at most
(log M)^2. It decreases to zero at x=m and increases thereafter,
so its total variation on any subinterval is at most 2(log M)^2.
Abel summation, retaining both clipped endpoints, consequently gives

    |sum_(n in J_(m,a,b))log(n/m)^2 e(-nma/b)|
        <=C L^2/||ma/b||.                               (23)

This explicitly handles intervals crossing n=m; monotonicity across
that point is not assumed.

Fix a,b and put g=gcd(a,b), q=b/g. If q=1 there is no
nonresonant m. Otherwise a/g is a unit modulo q; in one full
residue block the nonzero residues of ma/g permute 1,...,q-1.
Their reciprocal-distance sum is at most C q log(2q), by summing
q/min(j,q-j). Each residue occurs at most floor(M/q)+1 times
among m<=M. Because q<=b<=Q<=M eventually,

    sum_(m<=M; b does not divide ma)1/||ma/b||
       <=C(M+q)log(2q)<=C M log(2b).                    (24)

This includes composite q, noncoprime a,b and every incomplete block.
Combining (23), (24) and the exact sums following (20) bounds the
absolute value of the entire nonresonant contribution in (22) by

    C L^2 M sum_a d_a sum_b [d_b log(2b)/b]
         <=C M Q L^6.                                   (25)

All nonresonant terms have been included before this bound; none
has been declared positive. Equations (21)--(25) yield

    C(T)=P(T)+O(M Q L^6),             P(T)>=0.            (26)

### 6. Correlation, Holder and the interpolation obstruction

By definition S(T) is the sum of (8) and (16). Since K=M Q,
(8), (15), (26) give the complete signed lower estimate

    S(T)=T D(T)+P(T)+O(M Q L^19)
        >=c T L^18-C T^(5/8)L^19.                       (27)

Here M Q<=C T^(1/2+3/24)=C T^(5/8). The ratio of the error
to the lower scale is O(T^(-3/8)L), which tends to zero uniformly
as real T tends to infinity. Hence S(T)>=c' T L^18 eventually.
Floors and saddle coincidences introduce no height exceptions.

Apply the ordinary Holder inequality with dual exponents 4 and 4/3
on dt over [T,2T], as used in the proof of Tao's *245C Notes 1:
Interpolation of L^p spaces*, Lemma 9, 30 March 2009
([primary proof](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/)).
All functions here are finite continuous sums. It gives

    0<S(T)<=integral |R_T| |F|^6
          <=I_4(T)^(1/4) H(T)^(3/4).

The positivity of S ensures both factors are nonzero. By (6), (27),

    I_4(T)>=S(T)^4/H(T)^3
          >=c T^(4-3)L^(72-48)=c T L^24.

This proves (1). Finally audited L480 gives I_2<=C T L^8, so
I_2^(3/2)/I_4^(1/2)<=C T and (2) follows. In particular its
necessary upper condition I_4<=C T L^18 along an unbounded sequence
is incompatible with (1). This is an obstruction to the specified
moment certificate, not to RH or the actual first absolute moment.

### 7. Separate critical audit, 29 October 2026

The audit accepts (1)--(27) for the exact fixed cutoffs and every
sufficiently large real T. It reuses the source scope saved before
invocation, retains the cited mean-square and scalar stationary-phase
theorems, and checks their applications and all residual-specific finite
arguments. It does not audit either source manuscript in full or replay
L477's AFE transfer or L480's full second-moment proof. No estimate,
exponent, input assumption or DAG edge is changed. The attribution in
Section 5 is narrowed to distinguish cyclic orthogonality from the
locally proved incomplete geometric sum; its exact identity is now
displayed. The following checks record the substantive verification.

**Finite norms and equal-product grouping.** U is real by swapping
n,m; F^3 has coefficients d_3(a;N)/sqrt(a), so the A_j product
identity in Section 2 holds pointwise, with no time-averaging premise.
For each prime, the greedy matrix construction in (5) has the prescribed
row and column totals; these marginals recover both exponent vectors.
Thus two different pairs of four-factor factorizations cannot map to
the same sixteen-factor factorization, including k=1. Enlarging the
positive sixteen-factor harmonic sum proves the upper bound used for
both growing lengths, without a divisor asymptotic. In particular,
||b_2||_2||b_0||_2 and ||b_1||_2^2 are O(L^18).
The Hermitian error form of (3) therefore costs O(K L^19) after
polarization, while J=N^4 in the norm calculation has
J log(2J)=o(T). These give (6) and (8) with absolute constants.
On na=mb=k the product coefficient denominator is k; exchanging the
two factorizations converts the diagonal of the A_j identity exactly
to log(n/m)^2/k. No diagonal sign has been assumed before this step.

**Harmonic lower bound and logarithmic separation.** For fixed P,
the harmonic sum in each residue class is (log y)/P+O_P(1)
up to y. Subtracting two endpoints proves (11), including the interval
starting at 1 and the residue zero. The CRT count is over finitely
many classes. Its local factor excludes any prime dividing two
coordinates, and the convergent sum of pairwise 1/p^2 bounds leaves
delta_*>0 after the finitely many small primes. In (12) one can
use C_i=1+beta_i for X>=e, independently of p and B.
Thus (13) is uniform in B before B is fixed; choosing B first and
then X makes both discarded weights smaller than the stated positive
main term. There is no exchange involving a growing sieve modulus.

For the selected matrix, row 1 and columns 2--4 have exponent sum
at most 1; rows 2--4 have sum at most 37/48, and column 1 at most
5/16. Hence every row and column product is <=N<=M eventually,
and the three short factors in each ordered triple are each <=N.
Pairwise coprimality of all entries implies gcd(r_i,s_j)=x_ij:
every common prime must occur in their unique intersecting cell.
This remains true for entries equal to 1. It proves injectivity into
the actual ordered tuples counted in (9). Cancelling x_11 in n/m
leaves numerator at least N^(1/8) and denominator at most N^(3/48),
so the logarithmic separation in (14) holds. All sixteen interval
widths are positive, including those ending at N^(1/48).
Consequently their harmonic weight supplies sixteen logarithms and
the squared separation supplies two more. The floor in N satisfies
log N/L ->1/24; (15) is valid for all sufficiently large real T.

**Actual phase, amplitude and complete endpoint accounting.** The
phase in (16) follows by expanding F^3 conjugate(F^3); its saddle is
r=2 pi nma/b, not an integer in general. The retained scalar theorem
permits these positive real parameters. The actual-theta remainder
changes each integrand by O(1/T), hence each integral by O(1).
The saddle amplitude is sqrt(2 pi r); cancelling exp(-i pi/4)
from theta yields exactly (17), including the half-open indicator.
Multiplication by 1/sqrt(nmab) gives 2 pi/b, as in (22).

The total coefficient mass is O(M Q L^2), which pays for the
scalar constant error, the phase replacement and the far-saddle
endpoint kernels. In the middle region the identity
sqrt(nmab)=b sqrt(r/(2 pi)) proves (19). For a nonempty n-range,
h>=T/(2M). A layer at distance between 2^j sqrt T and
2^(j+1) sqrt T from either H contains
O(1+2^j sqrt T/h) lattice points. Multiplying by its kernel
bound O(sqrt T/2^j), and adding the central layer, gives
O(sqrt T+(T/h)log T)=O(sqrt T L).
This includes both sides of H and points exactly at H. With
sum_a d_a=Q and sum_b d_b/b=H_N^3=O(L^3), the middle-region
total is O(M Q L^6). Empty ranges add zero. Thus (21) applies
to all original indices and both endpoints without a separation
assumption, a half-weight convention or an exceptional set of T.

**Complete signed rational sum.** The saddle indicator intersects
1<=n<=M in one consecutive integer interval; its fractional and
clipped endpoints change neither the geometric identity nor Abel
summation. f_m(x)=log(x/m)^2 has supremum <=(log M)^2 and total
variation <=2(log M)^2, including intervals crossing m. These prove
(23) with endpoint terms included. With g=gcd(a,b), the reduced
numerator a/g is a unit modulo q=b/g; no primality of q is needed.
The full nonzero-residue sum of q/min(j,q-j) is O(q log(2q)).
Each residue occurs at most floor(M/q)+1 times, and Q<=M eventually,
which proves (24), including incomplete blocks and q=1. Summing
d_b log(2b)/b <=log(2Q) H_N^3=O(L^4) proves (25).
Every resonance has exponential exactly 1 and nonnegative weight;
all other terms were bounded in absolute value before being discarded
from the lower bound. Therefore (26) is a statement about the complete
chirped correlation; it does not assert positivity of that correlation.

**Final powers and route consequence.** The larger error is
O(T^(5/8)L^19), whose ratio to the proven diagonal lower scale is
O(T^(-3/8)L)->0. All earlier cutoffs and onsets can be combined
into one absolute onset, independent of endpoint coincidences.
Holder with exponents 4 and 4/3 gives S^4<=I_4 H^3, and hence
the powers T^(4-3)L^(72-48)=T L^24. Applying only L480's
audited upper bound I_2<=C T L^8 gives the upper bound C T
for the interpolation certificate. Its ratio to T L^3 tends to
zero on every unbounded sequence. Since I_1 is bounded *below*
by that certificate, no upper bound or little-o result for I_1
follows. The fixed-square defect and negative-mass gaps remain open.

This is verification of the local obstruction, not an additional
moment theorem or progress beyond the literature comparison already
recorded. It removes the pending-audit qualification on the specified
certificate stop; it supplies no all-degree positivity or RH candidate.

## Mathlib

Full matching coverage for this complete residual correlation and its
fourth-moment obstruction has not been checked. No absence claim is
made. Supporting finite sum, coprimality, integration and Holder
declarations were not looked up in this step. The named analytic
inputs are the cited finite mean square and Gonek's scalar lemma;
their exact applications and all new summed errors are given above.
The standard Holder inequality is imported. No computational sample,
certificate preview or assumed formalization is used as a proof.

# C020h — The full witness's absolute near-product budget exceeds Bq^2

## Hypotheses

Use exactly C019y's integer-d witness, coefficients and intervals, with
the scale and coefficient estimates retained in C019z audits1433/1435.
For clarity, d is a positive integer tending to infinity and T>2*pi*e
solves
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
 \quad h=3\pi/q,
\]
\[
 D=[X,\sqrt2X-h],\quad L=\lfloor X^{1/1000}\rfloor,
 \quad\ell=\log L,\quad R=L^4.
\]
The original linear taper is omega(n)=log(L/n)/ell for 1<=n<=L,
and alpha is the real Euler-product coefficient of zeta(s)^(-1/2)
on Re(s)>1; in particular alpha(p)=-1/2 for a prime p. Define
\[
 c_s=\sum_{a_1a_2a_3a_4=s;\ a_j\le L}
       \prod_{j=1}^4\alpha(a_j)\omega(a_j)\,(a_2a_4)^{-ih}.
                                                               \tag{1}
\]
For primes in P=[sqrt(X)/10,sqrt(X)/5], retain unordered distinct
p<r, v=pr, and both original own-time heat factors:
\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 E_p(Z)=\exp\{t(Z)((u(Z)-\log p)^2-\pi^2/16)/4
                   +i\pi t(Z)(u(Z)-\log p)/8\},
\]
\[
 a_v(Y)=r^{-ih}E_p(Y)E_r(Y+h)
             +p^{-ih}E_r(Y)E_p(Y+h),\qquad J_{vs}(Y)=a_v(Y)c_s.
                                                               \tag{2}
\]
All other J entries are zero. C019y's injectivity of vs applies:
every witness prime exceeds R eventually. Write
\[
 N_* =\left\lfloor\sqrt{\sqrt2X/(2\pi)+X^2/(16d)}\right\rfloor,
 \quad N=N_*^2R,\quad U=|D|/2=(B-h)/2.
\]
Here N is the full original support ceiling Z_*, not an independently
chosen shorter polynomial. For any Y0 in D, set b_k(Y0)=J_k(Y0)/sqrt(k)
for 1<=k<=N, and extend it by zero to all other integers. Define the
complete nonnegative frozen-coefficient budget
\[
 \mathfrak B(Y_0)=U\sum_{k\le N}|b_k(Y_0)|^2+
 U\sum_{0<|j|\le N/U}\sum_{k\le N}|b_k(Y_0)b_{k+j}(Y_0)|.
                                                               \tag{3}
\]
The j sum is over nonzero integers; it includes both orientations.
All conclusions have absolute constants and an absolute existential
integer onset. No RH, random phase, nonvanishing, actual-P estimate or
fixed-to-moving coefficient transfer is assumed.

## Conclusion

Uniformly for Y0 in D, for every sufficiently large integer d,
\[
 \mathfrak B(Y_0)\ge c\frac{XL^4}{q^4\ell^{16}},\qquad
 \frac{\mathfrak B(Y_0)}{Bq^2}
       \ge c'\frac{L^4}{q^6\ell^{16}}\longrightarrow\infty.
                                                               \tag{4}
\]
The off-diagonal term of (3) alone satisfies the first lower bound
after possibly reducing c and increasing the onset. Thus a uniform
O(Bq^2) estimate for this full absolute near-product budget is false.

This stops that sufficient spacing estimate. It does not lower-bound
the moving complex norm or the real norm Dcal=int_D S^2; neither
Dcal<=CBq^2 nor its negation follows. The signed numerator, actual-P
residual and Xi transfer remain open. The conclusion does not reopen
signed completion1431 or strengthen C019w/x's different G-array stops.

This is a local elementary specialization/obstruction under unchanged
EXPLORE assessment1435/coverage1436, classified REPRODUCTION. The
sources supply the mean-value framework and qualitative prime count,
not this coefficient-specific conclusion. No originality beyond the
checked sources is asserted. Independent audit1439 below retains
(1)--(15) and the off-diagonal assertion, with their stated scope.

## Proof

### 1. The source budget and its relation to the intended norm

Import Matomäki--Teräväinen, *Almost primes in almost all short intervals
II*, arXiv:2207.05038v2 (1 February 2023), Lemma 3.3, PDF pp.12--13,
[primary text](https://arxiv.org/html/2207.05038v2). For N,U>=1 and fixed
complex b_k supported on 1<=k<=N, the lemma gives
\[
 \int_{-U}^U\left|\sum_{k\le N}b_k k^{-it}\right|^2dt
       \ll U\sum_{k\le N}|b_k|^2+
          U\sum_{0<|j|\le N/U}\sum_{k\le N}|b_kb_{k+j}|.
                                                               \tag{5}
\]
The statement and its proof were inspected in source-review1436; no
reproof is required. Translating a fixed polynomial to the interval
D replaces b_k by b_k exp(-iYc log k), where Yc is D's midpoint.
This preserves every absolute weight in (3). The lemma does not
itself apply to moving J_k(Y), and no such application is made here.

There is a valid pointwise route from the intended real norm to a
complex norm. In C019y's notation W=|H|^2, S=W(A+conjugate A), so
\[
 S^2\le4W^2|A|^2=4|AH^2|^2,
 \qquad
 \mathcal D\le4\int_D
       \left|\sum_{k\le N}J_k(Y)k^{-1/2-iY}\right|^2dY.
                                                               \tag{6}
\]
The last equality in the integrand's modulus uses C019y (3) and the
unit factor exp(iTheta(Y)); it preserves all four tapers and both
shifted factors. A method paying this complex norm by uniformly
bounding (3), with additional amplitude costs, therefore encounters
the obstruction below already in the frozen budget. Equation (6)
is only an upper comparison and is never reversed.

### 2. Uniform original heat amplitudes and the small-prime coefficient

C019z audit1435 gives d asymp X^2q^2, ell~q/1000 and, uniformly for
Z in [X,sqrt(2)X] and p in P, E_p(Z)=1+O(q^-2). To check the relevant
scope, u(Z)-log p is bounded on these two fixed proportional ranges,
while t(Z)=O(q^-2). Also
\[
 p^{-ih}=e^{-3\pi i/2}
             e^{-ih\log(p/\sqrt X)}=i+O(q^{-1}).
\]
Both Y0 and Y0+h lie in that Z interval. Hence the actual amplitudes
in (2) satisfy a_v(Y0)=2i+O(q^-1), uniformly; in particular
\[
                 1\le |a_v(Y_0)|\le3                         \tag{7}
\]
eventually. No replacement by the constant 2i is made in (3).
The original witness primes are all inside both source floors by
C019y's audited cutoff check. Also N_*^2 asymp X, U asymp X and
N/U asymp R; the true floor changes N_* by less than one.

Let Q be the primes in [L/2,3L/4], and let s be a product of four
distinct members r1,r2,r3,r4 of Q. For L>4, any two of these primes
have product at least L^2/4>L. Thus a nonzero assignment in (1)
must place one prime in each of its four factors. There are exactly
24 assignments, and every alpha product is (-1/2)^4=1/16. Therefore
\[
 c_s=\frac1{16}\prod_{i=1}^4\omega(r_i)
         \sum_{\sigma\in S_4}(r_{\sigma(2)}r_{\sigma(4)})^{-ih}.
                                                               \tag{8}
\]
The four tapers remain individually present and satisfy
\[
 \frac{\log(4/3)}\ell\le\omega(r_i)\le\frac{\log2}\ell.
\]
After multiplication of the phase sum in (8) by exp(2ih ell),
each term has argument
h(log(L/r_sigma(2))+log(L/r_sigma(4))) in [0,2h log2].
For all sufficiently large d, 2h log2<=pi/3. Every such term has
real part at least 1/2; thus
\[
 \frac34\frac{(\log(4/3))^4}{\ell^4}
       \le |c_s|\le\frac32\frac{(\log2)^4}{\ell^4}.       \tag{9}
\]
This is a bound for the exact signed and shifted coefficient.
There is no cancellation with other factorizations: (8) lists them all.

### 3. Count distinct indices and their absolute mass

Import the standard unconditional prime number theorem pi(x)~x/log x,
Hadamard/de la Vallée Poussin (1896), precisely the first term of
[NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4), reused from
source-notes1434 and C019z. Only this qualitative fixed-interval
statement is used. Subtracting its estimates at ay and by, for fixed
0<a<b, gives (b-a)y/log y+o(y/log y) primes in [ay,by]; endpoint
inclusion changes the count by at most two. Consequently
\[
 |P|\asymp\sqrt X/q,\quad |Q|\asymp L/\ell,
 \quad { |P|\choose2}{ |Q|\choose4}
                  \ge c\frac{XL^4}{q^2\ell^4}.          \tag{10}
\]
The last inequality holds once both counts exceed fixed constants;
the binomial coefficients count distinct unordered choices, not ordered
tuples. This use of PNT neither requires short intervals nor an
RH-strength error term.

Let E be the set of all indices k=vs with these choices. Distinct
choices give distinct k: the two primes in v exceed R and the four
primes in s are at most L. Unique factorization recovers both choices.
Every such k is in the original support and obeys
\[
        \frac{XR}{1600}\le k\le\frac{81XR}{6400}\le N.   \tag{11}
\]
The first two bounds use v in [X/100,X/25] and
s in [L^4/16,81L^4/256]; the last follows either from the witness
cutoffs or N_*^2/X tending to sqrt(2)/(2pi).
Equations (7),(9)--(11) yield, uniformly in Y0,
\[
 M_E:=\sum_{k\in E}|b_k(Y_0)|
       \ge c\frac{\sqrt X L^2}{q^2\ell^8}.              \tag{12}
\]
Indeed each weight is at least c/(sqrt(X)L^2 ell^4), and (10)
counts at least c XL^4/(q^2 ell^4) different weights. This subset
is used only to lower-bound a nonnegative budget. It is not a
deletion of terms from the signed time integral.

### 4. The full absolute near-product budget is too large

Set H=floor(N/U). Eventually N/U>=2 and U>=1, so
H>=N/(2U). Partition the integers 1,...,N into K=ceil(N/H)
consecutive bins of at most H integers. Then K<=2U+1<=3U.
Every pair within a bin has |k-l|<=H-1<=N/U. Write
m_j=sum_(k in E in bin j)|b_k(Y0)|. The diagonal and all ordered
off-diagonal pairs in m_j^2 occur in (3). All remaining terms of
(3) are nonnegative. Finite Cauchy--Schwarz gives
\[
 \mathfrak B(Y_0)\ge U\sum_{j=1}^K m_j^2
       \ge\frac U K M_E^2\ge\frac13 M_E^2
       \ge c\frac{XL^4}{q^4\ell^{16}}.                 \tag{13}
\]
This retains the exact source range and its two orientations; a bin
of H integers has maximal difference H-1, so no endpoint pair is
being counted outside that range. No prime-pair separation conjecture
enters the pigeonhole estimate.

The full diagonal is much smaller. Exact injectivity and C019z's
audited upper bound K1=sum |c_s|^2/s=O(ell^4) give
\[
 \sum_{k\le N}|b_k(Y_0)|^2
       =K_1\sum_{p<r\in P}\frac{|a_{pr}(Y_0)|^2}{pr}
       \ll\frac{\ell^4}{q^2}\ll q^2.                  \tag{14}
\]
Here (7) and sum_(p in P)1/p=O(q^-1), following at once from
the prime count and p>=sqrt(X)/10, suffice. Thus the first term
of (3) is O(Xq^2). Since ell~q/1000 and L=floor(X^(1/1000)),
\[
 \frac{L^4}{q^6\ell^{16}}\asymp\frac{L^4}{q^{22}}
                          \longrightarrow\infty,       \tag{15}
\]
it can be subtracted from (13) while retaining half its lower bound
eventually. This proves both (4) and the off-diagonal assertion.

Only the false sufficient budget has been excluded. The translated
coefficients retain their complex phases, and (5) is an upper bound,
not a converse. The lower bound for its right side supplies no lower
bound for its left side. The actual J_k(Y) still move with Y; paying
their variation does not follow from the frozen calculation. The
original real norm has the additional signed nonconjugate channel
in C019y (5). These facts prevent interpreting (13) as a norm or RH
obstruction. A continuation needs signed cancellation or another
independently justified estimate, not a sharper upper bound for (3).

### Independent audit1439 — 18 November 2026

This checks the entire argument (1)--(15) under unchanged SPECIALIZE
assessment1437, separately approved in1438. Inputs are C019y's exact
finite identities and injectivity retained by audit1421, C019z's
K1 upper estimate retained by audit1433, and its uniform scale/heat
estimates retained by audit1435. Source-review1436 B supplies precisely
(5); source-notes1434 supplies the unconditional qualitative PNT.
No new source, source reproof, actual-P estimate or norm converse is
needed. The following checks retain the claimed budget obstruction;
they strengthen neither its order nor its interpretation.

**Original support and amplitudes.** With lambda=log(T/(2pi)), the exact
identities are d=e^lambda(lambda-1),
X^2=2pi^2 e^lambda/(lambda-1) and
q=lambda/2-(log(lambda-1))/2+log(2pi^2)/2. Hence lambda~2q,
d/X^2=(lambda-1)^2/(2pi^2), and ell~q/1000 along the specified
integers d. For Z in J and p in P,

    u(Z)-log p = (1/2)log((Z/X)/(2pi))-log(p/sqrt X)

is bounded uniformly. Both the real and imaginary parts of the heat
exponent are O(q^-2), so the complex estimate E_p(Z)=1+O(q^-2)
holds. Each factor in a_v is evaluated at its own Y0 or Y0+h in J.
Moreover p^(-ih)=i exp(-ih log(p/sqrt X))=i+O(q^-1).
Thus |a_v-2i|<=C/q uniformly and (7) follows at one absolute onset.
No heat factor or phase in (3) is replaced in the lower bound.

The smallest floor satisfies N(X)/sqrt X -> 1/sqrt(2pi)>1/5;
the witness primes are therefore present at both times throughout D.
The largest floor satisfies N_*^2/X -> sqrt(2)/(2pi): taking the
integer floor changes its square by O(sqrt X), negligible after
division by X. Also p>=sqrt X/10>R eventually since R<=X^(4/1000).
Consequently all original (v,s) representations are injective, and
N/U is comparable to R and tends to infinity. N is an integer and
U tends to infinity, as required by the bin argument.

**Exact small-prime coefficient.** If s is a product of four distinct
primes from Q, unique factorization implies each a_j in (1) is a
product of a subset of those four primes. No a_j can contain two:
their product is at least L^2/4>L. Four factors must accommodate all
four primes, so each contains exactly one. These are exactly the
24 permutations in (8), including the multiplicities of the two
shifted positions. All four alpha factors contribute the positive
product 1/16, and all four individual tapers remain in the product.
Multiplication by exp(2ih ell) rotates each summand to an argument
in [0,2h log 2]. Eventually that interval lies in [0,pi/3]. Its real
part is then at least 1/2. The lower factor 24/(2*16)=3/4 and upper
factor 24/16=3/2 verify both constants in (9). No other allowed
factorization can cancel this coefficient.

**Counts, distinctness and weights.** The cited qualitative PNT gives

    #P ~ sqrt X/(5q),       #Q ~ L/(4ell).

Subtracting its asymptotics at fixed proportional endpoints is valid
because the two endpoint error terms are o(y/log y); endpoint atoms
cost at most two. These counts tend to infinity, so their unordered
binomial counts have the lower order in (10). For k=vs, the two
large primes exceed R while the four small ones are at most L.
Unique factorization recovers v and s separately, even among the
complete J support, so every counted k carries exactly a_v*c_s.
Multiplying the stated ranges gives exactly

    XR/1600 <= k <= 81XR/6400.

The last upper constant is strictly smaller than sqrt(2)/(2pi),
so k<=N eventually. In particular k<=XR. Thus every selected
|b_k| is at least a fixed positive constant times
1/(sqrt X L^2 ell^4). Multiplying by the distinct-index count in
(10) yields (12), uniformly in Y0. This selection is legal only
because the budget (3) is nonnegative term by term; it would not
justify deleting terms from a complex polynomial before integration.

**Bin endpoints and the complete diagonal.** For real N/U>=2,
H=floor(N/U)>=N/(2U). There are K=ceil(N/H)<=2U+1<=3U bins,
each containing at most H integers, including the final partial bin.
Every two distinct integers within a bin differ by at most H-1,
which is strictly within the allowed |j|<=N/U. Expanding m_j^2
counts each off-diagonal ordered pair once and the diagonal once,
exactly as available in (3). Zero extension handles the boundary at
N without adding an out-of-support pair. Cauchy--Schwarz for these
K nonnegative bin masses proves (13).

For the subtraction, the diagonal is the full one, not merely the
selected subset. Complete injectivity and s<=R give its exact product
in (14). From |a_v|<=3,

    sum_(p<r) |a_(pr)|^2/(pr) <= (9/2)(sum_P 1/p)^2,
    sum_P 1/p <= (10/sqrt X)#P = O(1/q).

The audited upper K1<=sum_(s<=R) d_4(s)/s<=(1+4ell)^4, valid
eventually with ell>=1, gives the full diagonal O(ell^4/q^2)=O(q^2).
Here |c_s|<=tau(s), tau(s)^2<=d_4(s) and the finite harmonic-product
bound are exactly C019z audit1433's input, not a claim about a
critical-line reciprocal. Multiplication by U makes the full
diagonal contribution O(Xq^2). Finally

    [XL^4/(q^4 ell^16)]/(Xq^2)
        = L^4/(q^6 ell^16) -> infinity,

since L~exp(q/1000) and ell~q/1000. Therefore subtracting the full
diagonal from (13) leaves at least half its lower bound eventually.
This verifies the off-diagonal assertion as well as (4). All constants
are independent of Y0 and d; the onset is existential, not effective.

**One-way norm comparison.** For every Y, W=|H|^2 and
(A+conjugate A)^2<=4|A|^2. Hence S^2<=4|AH^2|^2, and the unit
exp(iTheta) in C019y (3) proves exactly (6), with no lost taper.
For fixed coefficients the translation to D changes only their
phases and preserves (3). Lemma 3.3 supplies an upper bound on that
fixed time norm; a lower bound for its right side cannot be reversed.
It also supplies no estimate for moving coefficients. The real norm
still has C019y (5)'s signed off-diagonal and nonconjugate channel.
Thus this audit verifies a failed sufficient absolute estimate only.
It leaves the full denominator, signed numerator, E_P and Xi transfer
unresolved, and neither reopens nor resets signed completion1431.

This is REPRODUCTION: local correctness verification of a previously
written obstruction, not a new discovery beyond the sources checked.
There is no candidate proof or disproof of RH here. No mathematical
script or numerical certificate is needed for these asymptotic checks.

## Mathlib

Full matching coverage has not been checked. This is an informal finite
counting and coefficient argument using unique factorization, the
prime number theorem and finite Cauchy--Schwarz, with the mean-value
framework cited above. No matching formal theorem, machine verification
or absence from Mathlib is claimed. No numerical experiment is used as
evidence for the asymptotic lower bound or its absolute onset.

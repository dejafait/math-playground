# C020l — A high-height localized signed remainder for the frozen fourth moment

## Hypotheses

Use C019y's original positive integer d and its scales
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
\]
\[
 J=[X,\sqrt2X],\quad L=\lfloor X^{1/1000}\rfloor,
 \quad\ell=\log L,\quad R=L^4.
\]
All bounds below have absolute constants and one existential integer-d
onset, uniform over fixed Z in J. Use the original real alpha(n) from
the Euler-product branch of zeta(s)^(-1/2) on Re(s)>1, the individual
linear taper omega(n)=log(L/n)/ell for n<=L, and
\[
 M(t)=\sum_{n\le L}\alpha(n)\omega(n)n^{-1/2-it},\qquad
 P_Z(t)=\sum_{p\in\mathcal P}E_p(Z)p^{-1/2-it},
 \quad\mathcal P=[\sqrt X/10,\sqrt X/5]\cap\{\text{primes}\},
\]
\[
 E_p(Z)=\exp\left\{\frac{Z^2}{8d}
 [(\tfrac12\log(Z/(2\pi))-\log p)^2-\pi^2/16]
 +\frac{i\pi Z^2}{16d}(\tfrac12\log(Z/(2\pi))-\log p)\right\}.
\]
Z is fixed independently of the integration variable t. Define the
four **unshifted** tapered coefficients by
\[
 r_s=\sum_{a_1a_2a_3a_4=s;\ a_j\le L}
             \prod_{j=1}^4\alpha(a_j)\omega(a_j),\qquad
 M(t)^4=\sum_{s\le R}r_s s^{-1/2-it}.                 \tag{1}
\]
These are not C019y's shifted coefficients c_s. No RH, critical-line
reciprocal series, moving-height transfer or actual-Xi input is assumed.

## Conclusion

The repeated-prime component is paid at the desired scale:
\[
 D_Z(t)=\sum_{p\in\mathcal P}E_p(Z)^2p^{-1-2it},\qquad
 \int_J|D_Z(t)M(t)^4|^2dt\ll Bq^2.                    \tag{2}
\]
Put
\[
 A_Z(t)=2\sum_{p<r\in\mathcal P}E_p(Z)E_r(Z)(pr)^{-1/2-it},
 \quad F_Z(t)=A_Z(t)M(t)^4=\sum_k b_k k^{-it},
\]
\[
 b_{vs}=\frac{2E_p(Z)E_r(Z)r_s}{\sqrt{vs}},\quad v=pr,
 \ p<r\in\mathcal P,\ s\le R,                         \tag{3}
\]
with zero coefficients elsewhere. The representation k=vs is unique.
For its nonzero support let s(k) denote that unique s. There is an
explicit real weight 0<=w_X<=1, equal to 1 on J and supported in the
positive-height interval [X-B/2,sqrt(2)X+B/2], such that
\[
 \int_{\mathbb R}w_X(t)|F_Z(t)|^2dt
       =T_Z+\mathcal R_Z+\mathcal E_Z,\qquad
 0\le T_Z\ll Bq^2,\quad |\mathcal E_Z|\ll X^{241/250}q^2,
                                                               \tag{4}
\]
where, with W_X(xi)=integral w_X(t)exp(it*xi)dt,
\[
 \mathcal R_Z=
 \sum_{\substack{k,l\in\operatorname{supp}b;\ s(k)\ne s(l)\\
             |\log(l/k)|<X^{-99/100}}}
       b_k\overline{b_l}W_X(\log(l/k)).                 \tag{5}
\]
The sum (5) is real by conjugate symmetry and retains all its signs.
The original moment satisfies
\[
 \int_J|P_Z(t)M(t)^2|^4dt
 \le 2\int_J|D_Z(t)M(t)^4|^2dt
       +2(T_Z+\mathcal R_Z+\mathcal E_Z).              \tag{6}
\]
Thus a uniform upper bound R_Z<=C Bq^2 would suffice for the target.
It is **not proved here**. Nor would failure of this sufficient
weighted upper bound refute the original hard-interval bound. The far
term has relative size O(X^(-9/250)); the unresolved near term involves
integer differences |l-k|<=C L^4 X^(1/100), for large d.

This is a finite mean-value specialization under unchanged EXPLORE
assessment1447, classified REPRODUCTION. It pays repeated primes,
equal-s interactions and distant frequencies but leaves the signed
near unequal-s correlations unpaid. It is an exploratory reduction,
not a fourth-moment theorem, informative negative result, originality
claim or advance toward a complete RH argument. No numerical evidence
or mathematical script is used. Independent conceptual audit1450 below
retains (1)--(15), without proving the unpaid near bound or the moment.

## Proof

### Coefficients and uniform scales

C019z audits1433/1435 give X tending to infinity, ell~q/1000,
d comparable to X^2q^2 and E_p(Z)=1+O(q^-2) uniformly in these exact
ranges. Only these scale/heat facts are used; none of its shifted
coefficient correlations is imported. The coefficient inequality
(|alpha|*|alpha|)(n)<=1 proved and audited in C019p implies
\[
 |r_s|\le\tau(s),\qquad
 K_0:=\sum_{s\le R}|r_s|^2/s
       \le\sum_{s\le R}d_4(s)/s\le(1+\log R)^4\ll\ell^4. \tag{7}
\]
Indeed fourfold absolute convolution is at most 1*1=tau; the tapers
are in [0,1]. On prime powers (e+1)^2<=binomial(e+3,3), so tau^2<=d4.
Expanding d4 and dropping its product cutoff bounds the last sum by
the fourth power of the harmonic sum up to R. This argument applies
directly to (1), not by identifying r_s with a shifted c_s.

Import the standard unconditional prime number theorem, Hadamard/de la
Vallee Poussin (1896), in the form pi(x)~x/log x, precisely the first
term of [NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4), as inspected
in source-notes1434 and reused in C020h. Its qualitative fixed-ratio
interval consequence gives #P=O(sqrt(X)/q), hence
\[
 \sum_{p\in\mathcal P}1/p\ll1/q.                       \tag{8}
\]
Only this upper bound is needed; no short-interval or RH-strength
error term is invoked. Every p in P exceeds R eventually. Consequently
unique factorization recovers the two large primes in k=vs, including
their multiplicities if v is a square, and then recovers s. In (3)
v<=X/25, and k<=N:=floor(XR/25). With
a_v=2E_p(Z)E_r(Z) for p<r, (8) gives
\[
 D_A:=\sum_v|a_v|^2/v\ll q^{-2},\qquad
 \sum_k|b_k|^2=K_0D_A\ll q^2,\qquad
 \left(\sum_k|b_k|\right)^2\le N\sum_k|b_k|^2
                  \ll XRq^2.                         \tag{9}
\]
Zero r_s do not require a representation choice in (5).

### The finite-frequency input and repeated primes

Import Montgomery--Vaughan, *Multiplicative Number Theory II: Primes
and Sieves*, author-hosted draft (version date unidentified), G.16,
(G.25)--(G.28), printed pp426--427;
[primary PDF](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf).
Its statement and frequency hypotheses were inspected in
source-notes1410 and reused by assessment1447. For distinct real
lambda_n, delta_n=min_(m!=n)|lambda_m-lambda_n|, it states
\[
 \left|\sum_{m\ne n}\frac{x_m y_n}{\lambda_m-\lambda_n}\right|
 \le\frac{3\pi}{2}
  \left(\sum_n|x_n|^2/\delta_n\right)^{1/2}
  \left(\sum_n|y_n|^2/\delta_n\right)^{1/2}.           \tag{10}
\]
For a fixed finite polynomial sum_(n<=V) z_n n^(-it), with equal
integer indices already grouped, its integral over [a,a+H] is
\[
 H\sum_n|z_n|^2+
 \sum_{m\ne n}z_m\overline{z_n}
 \frac{e^{i(a+H)\log(n/m)}-e^{ia\log(n/m)}}{i\log(n/m)}.
\]
For integer n<=V, the distinct log n have delta_n>=1/(V+1).
Apply (10) to each endpoint with its unit phases and the conjugate
coefficient array; their norms are unchanged. Therefore
\[
 \int_a^{a+H}\left|\sum_{n\le V}z_n n^{-it}\right|^2dt
       \le[H+3\pi(V+1)]\sum_n|z_n|^2.                \tag{11}
\]
If only one frequency occurs, (11) is immediate. This verifies the
needed specialization of the imported theorem, without reproving it.

By (8) and the uniform heat bound, |D_Z(t)|<=C/q for every real t.
Apply (11) to M(t)^4 with V=R, H=B and squared coefficient norm K0.
Since R<=X^(1/250)=o(B), this gives
\[
 \int_J|D_Z M^4|^2\ll q^{-2}(B+R+1)K_0
                     \ll B\ell^4/q^2\ll Bq^2,
\]
proving (2). The exact identity P_Z^2=A_Z+D_Z and
|x+y|^2<=2|x|^2+2|y|^2 will give (6); repeated primes have been
paid, not silently omitted.

### A compact weight at positive heights

Fix K=104, a_0=B/(4K), and let rho(t) be 1/(2a_0) on
[-a_0,a_0] and zero elsewhere. Set
\[
 \psi=\underbrace{\rho*\cdots*\rho}_{K\text{ factors}},\qquad
 w_X=\mathbf1_{[X-B/4,\sqrt2X+B/4]}*\psi.           \tag{12}
\]
Here convolution is on the real height variable. The nonnegative psi
has integral one and support [-B/4,B/4]. Thus 0<=w_X<=1, w_X=1
on J (endpoints up to null sets suffice), its support is as claimed,
and integral w_X=3B/2. The support's lower endpoint is positive since
1-(sqrt(2)-1)/2>0. All transforms and convolutions here are of
compactly supported L1 functions; Fubini is justified by absolute
integrability. Direct integration gives, with
c=(1+sqrt(2))X/2 and sinc(0)=1,
\[
 W_X(\xi)=e^{ic\xi}\frac{2\sin(3B\xi/4)}{\xi}
                \operatorname{sinc}(a_0\xi)^K,
 \qquad W_X(0)=3B/2,
\]
\[
 |W_X(\xi)|\le C_K B(1+B|\xi|)^{-K}.                \tag{13}
\]
For example use |sinc y|<=min(1,1/|y|), |integral over the
interval in (12)|<=3B/2, and absorb the fixed factor 4K into C_K.
The large fixed constant is independent of d and Z.

### Equal-s payment and the remaining signed layer

Expanding the finite polynomial in (3) and integrating against w_X
gives exactly sum_(k,l) b_k conjugate(b_l) W_X(log(l/k)). Partition
it into equal-s terms, unequal-s terms with |log(l/k)|<X^(-99/100),
and the other unequal-s terms. These are T_Z, R_Z and E_Z in (4).
For equal s the phases s^(-it) cancel, so exactly
\[
 T_Z=K_0\int_{\mathbb R}w_X(t)|A_Z(t)|^2dt.          \tag{14}
\]
The distinct v=pr are already grouped by unique factorization, all
at most V=floor(X/25). The weight is at most one and its support
has length 2B. Applying (11) to A_Z gives
T_Z<=K0[2B+3pi(V+1)]D_A<<Bq^2 by (7)--(9). This pays all prime
product interactions within each s, not just k=l.

For the remaining far terms (13) and (9) give
\[
 |\mathcal E_Z|
 \le C X^{1-104/100}\left(\sum_k|b_k|\right)^2
 \ll X^{2-104/100}Rq^2
 \le C X^{241/250}q^2=o(Bq^2),                       \tag{15}
\]
since R<=X^(1/250) and 2-104/100+1/250=241/250.
This bound is on the far layer only. It does not replace R_Z by
an absolute near-neighbor budget. Both orientations of each near
pair occur, so R_Z is real. If |log(l/k)|<X^(-99/100), then
|l-k|<=2N X^(-99/100)<=C R X^(1/100) eventually, by the elementary
bound exp(y)-1<=2y for 0<=y<=1. This is a localization width,
not a count or a bound for those signed pairs.

Finally w_X>=1 on J and is nonnegative everywhere. Therefore
integral_J |F_Z|^2<=T_Z+R_Z+E_Z. Combining with P_Z^2=A_Z+D_Z
proves (6). No lower bound for the original moment follows from
a large weighted moment. The kernel (13) retains its translated
phase exp(ic*xi); dropping that phase would discard the high-height
cancellation being tested. A proof of R_Z<=C Bq^2 needs a further
signed arithmetic estimate, not another finite expansion. No such
estimate or incompatible lower bound has been obtained in this step.

### Independent conceptual audit1450 — 18 November 2026

This audit uses the prior SPECIALIZE assessment1448, separately compared
in source-review1449. It checks exactly (1)--(15) with the original four
unshifted tapers and a fixed Z in J. No statement or error order needs
repair. The Hilbert inequality and qualitative PNT are imported with
the precise citations above; their proofs are not repeated. The local
applicability checks below do not establish a new mean-value theorem.

**Uniform onset and the coefficient array.** Put lambda=log(T/(2pi)).
The defining equation for d is d=e^lambda(lambda-1), strictly increasing
for lambda>1. Along positive integers d tending to infinity,

    X^2=2pi^2 e^lambda/(lambda-1),
    q=lambda/2-log(lambda-1)/2+log(2pi^2)/2,
    d/X^2=(lambda-1)^2/(2pi^2).

These verify the scale facts imported from C019z's audit1435 in the
exact C019y setup: q tends to infinity, lambda~2q, d is comparable to
X^2q^2, and ell~q/1000 despite the floor in L. Eventually L>=2 and
R<=X^(1/250)<sqrt(X)/10. For Z in J and p in the specified closed
prime interval,

    (1/2)log(Z/(2pi))-log p
      =(1/2)log((Z/X)/(2pi))-log(p/sqrt(X))

lies in one fixed compact real interval. Also Z^2/d=O(q^-2).
The whole complex heat exponent is therefore O(q^-2), uniformly;
|exp(z)-1|<=|z|exp(|z|) gives E_p(Z)=1+O(q^-2). In particular
|E_p(Z)|<=2 after one onset independent of Z. No height outside J
is substituted for Z when the integration interval is enlarged.

C019p's proved nonnegative convolution g=|alpha|*|alpha|<=1 implies
|r_s|<=(g*g)(s)<=tau(s), after dropping only the nonnegative absolute
taper factors and their individual cutoffs for this upper bound.
On each prime power the difference between binomial(e+3,3) and
(e+1)^2 is (e+1)e(e-1)/6>=0 for every integer e>=0. Thus tau(s)^2<=d4(s).
The d4 harmonic sum is at most H_R^4: its positive four-variable
product-cutoff domain is contained in the box [1,R]^4. Since
H_R<=1+log R and log R=4ell, (7) follows. This does not identify r_s
with the shifted c_s, and uses no reciprocal series on Re(s)=1/2.

Qualitative PNT gives #P<=pi(sqrt(X)/5)<=C sqrt(X)/q eventually.
This bound includes any endpoint primes and, with p>=sqrt(X)/10,
gives (8). Every prime dividing s<=R is smaller than every source
prime. Consequently unique factorization recovers the unordered
source pair from k=prs and then s; the same reasoning allows a repeated
source prime in D_Z. There are no concealed coefficient collisions in
(3). In particular its support has at most N=floor(XR/25) elements.
The exact squared norm factors as K0 D_A, with
D_A<=C(sum_p 1/p)^2=O(q^-2). Cauchy--Schwarz on that finite support
then gives the last inequality in (9). Empty supports cause no exception.

**The two endpoints and repeated primes.** For two distinct integer
indices m,n<=V,

    |log m-log n| >= |m-n|/max(m,n) >= 1/V >= 1/(V+1).

Group equal indices first. At an endpoint u put lambda_n=log n,
x_n=z_n exp(-iu lambda_n), y_n=conjugate(z_n)exp(iu lambda_n).
The off-diagonal endpoint expression in the proof of (11) is exactly
i sum_(m!=n) x_m y_n/(lambda_m-lambda_n). Each weighted squared
norm in (10) equals sum_n |z_n|^2/delta_n, so one endpoint costs at
most (3pi/2)(V+1) sum_n |z_n|^2. Applying the triangle inequality
to the two endpoints gives 3pi(V+1), with no dependence on a or H.
The empty and singleton polynomials satisfy (11) directly. This checks
the sign convention, conjugation and constant without assuming
orthogonality or varying coefficients during integration.

Uniformly for every real t, |D_Z(t)|<=sum_p |E_p(Z)|^2/p=O(q^-1).
Apply (11) to M^4 with coefficients r_s/sqrt(s), squared norm K0,
V=R and H=B. As R+1=O(B), its resulting bound is precisely
O(q^-2 B ell^4)=O(Bq^2), proving (2) with one uniform onset. This
uses the exact identity P_Z^2=A_Z+D_Z, so the repeated primes have
not been lost when passing to unordered distinct pairs.

**Compact support, normalization and Fourier phase.** Each rho has
nonnegative integral one and support [-a0,a0]; its 104-fold convolution
psi has integral one and support [-B/4,B/4]. For t in J and y in this
support, t-y lies in the full indicator interval of (12). Hence w_X=1
on J up to immaterial endpoint null sets. The support is exactly
contained in [X-B/2,sqrt(2)X+B/2], of length 2B, and 0<=w_X<=1.
Its lower endpoint is X(1-(sqrt(2)-1)/2)>0. Its integral is the
indicator's length 3B/2. These facts use nonnegative convolution,
not positivity of its Fourier transform.

With the plus-sign Fourier convention of (4), the indicator of center
c=X+B/2 and half-length 3B/4 has transform
exp(ic xi) 2sin(3B xi/4)/xi. The transform of rho is sinc(a0 xi);
the 104 factors give exactly (13), including W_X(0)=3B/2. All functions
are compactly supported and integrable, so the convolution transform
and its value at zero follow from absolutely convergent Fubini integrals.
For u=B|xi|, the elementary inequality

    min(1,4K/u) <= (1+4K)/(1+u)

(with its limiting meaning at u=0) permits, for example,
C_K=(3/2)(1+4K)^K in (13). Its size is irrelevant to an existential
onset; K=104 is fixed, independent of d and Z. No translation phase
or sign of the sinc/indicator factors has been dropped.

**Signed partition, equal-s payment and the tail exponent.** Expanding
|F_Z|^2 gives the frequency log(l/k), not its negative. For equal s,
b_(vs) conjugate(b_(v's)) is
|r_s|^2 a_v conjugate(a_v')/(s sqrt(vv')); thus summing exactly over
all s yields (14). In particular T_Z is nonnegative even though its
individual unequal-v terms need not be. Bound the weighted integral
by the integral over its length-2B support and use (11) with
V=floor(X/25) and squared norm D_A. Since V+1=O(B), this gives
T_Z=O(B ell^4/q^2)=O(Bq^2), including all equal-s off-diagonal terms.

For the unequal-s far set, |xi|>=X^(-99/100), so
B|xi|>=(sqrt(2)-1)X^(1/100). Consequently (13) gives
|W_X(xi)|<=C X^(1-104/100). Bounding this set by the full absolute
coefficient square in (9), solely for this far estimate, gives

    |E_Z| <= C X^(2-104/100) R q^2
           <= C X^(241/250) q^2,
    |E_Z|/(Bq^2) <= C X^(-9/250).

Here 2-104/100+1/250=241/250 and 241/250-1=-9/250.
The strict near cutoff and the non-strict far cutoff partition every
unequal-s pair, including those exactly at the boundary. Both sets
are invariant under (k,l) exchanged with (l,k). Because w_X is real,
W_X(-xi)=conjugate(W_X(xi)); therefore R_Z, and also E_Z, are real.
No absolute-value estimate for R_Z is inferred from that symmetry.
For either orientation of a near pair, put u=|log(l/k)|<X^(-99/100).
Then |l-k|=min(k,l)(exp(u)-1)<=2N X^(-99/100), eventually, giving
the stated integer width without a counting or cancellation assertion.

Finally |P_Z M^2|^4=|(A_Z+D_Z)M^4|^2. The pointwise two-term square
inequality and w_X>=1 on J prove (6). An upper bound R_Z<=C Bq^2
would then suffice, using the absolute bound for E_Z; a bound on
|R_Z| is not required. None is supplied here. Conversely the larger
weighted norm only upper-bounds the hard-interval norm, so a failure
of the sufficient weighted bound has no converse implication.

All constants and finitely many onsets above can be combined into one
absolute integer-d onset uniform over fixed Z in J. This confirms the
finite reduction and its stated limitations, not a moment estimate,
an informative obstruction to that estimate, or progress beyond the
sources checked. The unequal-s near bound, two own heat times, shifted
intervals, distinct-pair transfer, motion, real denominator, signed
numerator, actual-P error and Xi transfer remain unresolved. No new
dependency, mathematical script or numerical certificate is used.

### Bounded determinant attempt1453 — 18 November 2026

This is the single mathematical test authorized by EXPLORE assessment1451,
separately approved in recovery1452. It uses the unchanged hypotheses and
audit1450 above. The outcome is **inconclusive**: the finite character
identity below does not pay (5). The available bounds are O(BR) for its
zero mode and O(BRq^2) for its remaining modes, rather than O(Bq^2) for
their signed sum. These are upper bounds, not lower obstructions to (5).
No original coefficient is completed or replaced.

**Gcd extraction and every source-prime case.** Let V be the set of
products v=pr, p<r in P, and write gamma(v)=2E_p(Z)E_r(Z). For each
ordered pair s!=s', uniquely put

    s=g a, s'=g b, (a,b)=1, a!=b, ga,gb<=R.

For v,v' in V set h=bv'-av, so k=gav, l=gbv' and l-k=gh.
On the near set, with eta=X^(-99/100),

    0<|h| <= (2/25) max(a,b) X^(1/100)
           <= H_ab := ceil(max(a,b) X^(1/100)).                 (16)

Indeed |h|=min(av,bv')(exp(|log(bv'/av)|)-1), and each product
v,v' is at most X/25. The zero case would give k=l; uniqueness of
the large-prime/small-factor representation in (3) then gives s=s',
which is excluded. Each source prime exceeds R. If v and v' share
a source prime rho, then rho divides h, whereas

    |h|<=H_ab<=X^(7/500)+1<sqrt(X)/10<=rho

eventually. Thus this case is empty, including v=v'. No shared-prime
contribution is estimated away. Every surviving source pair has four
distinct primes and gcd(v,v')=1. Reduction modulo a and b also gives
gcd(h,ab)=1: modulo a, h=bv', with b and v' both coprime to a;
modulo b, h=-av, with a and v both coprime to b. These conclusions
hold for every g, including g>1, and for a=1 or b=1.

The exact resulting expression is

    R_Z = sum* (r_(ga) r_(gb)/g)
          sum_(0<|h|<=H_ab, (h,ab)=1)
          sum_(v,v' in V, bv'-av=h) gamma(v) conjugate(gamma(v'))
                       K_(a,h)(v),                            (17)

where sum* is over the g,a,b just specified, and

    K_(a,h)(v) = W_X(log(1+h/(av))) / sqrt(av(av+h))             (18)

when av+h>0 and |log(1+h/(av))|<eta, and is zero otherwise.
The h range excludes zero. Formula (18) retains the strict original
logarithmic cutoff, not merely (16). On the determinant equation,
sqrt(av(av+h))=sqrt(abvv'), verifying the coefficient in (17).
The complete factor exp(ic log(1+h/(av))) in W_X is retained.
Conversely every nonzero term of (17) is an original near pair.
Thus (17) loses no gcd case, endpoint, sign, taper or multiplicity.

**Exact finite characters, including their zero mode.** Define the
integer m_ab=ceil((a+b)X)+1, and e(x)=exp(2 pi i x). For all tuples
in (17) before imposing the determinant equation,

    |bv'-av-h| <= (a+b)X/25+H_ab < (a+b)X < m_ab

eventually, uniformly in a,b. Consequently finite orthogonality gives

    1_(bv'-av=h) = (1/m_ab) sum_(j=0)^(m_ab-1)
                              e(j(bv'-av-h)/m_ab).

For completeness, the sum of the powers of e(n/m) is m if m divides
n, and is (1-e(n))/(1-e(n/m))=0 otherwise; the displayed strict
range excludes every nonzero multiple of m_ab. This finite identity
needs no limiting theorem or reproof of an analytic source result.
Substitution gives exactly

    R_Z = sum* r_(ga) r_(gb)/(g m_ab)
          sum_(0<|h|<=H_ab, (h,ab)=1)
          sum_(j=0)^(m_ab-1) e(-jh/m_ab)
            [sum_(v in V) gamma(v) K_(a,h)(v) e(-jav/m_ab)]
            [sum_(v' in V) conjugate(gamma(v')) e(jbv'/m_ab)].   (19)

This transform has zero approximation error. It is important that the
inner sums in each character mode still include common-prime pairs:
only their complete character sum annihilates their impossible
determinants. Removing them mode by mode would invalidate (19).
Let Zcal_Z be the complete j=0 part of (19), and Ncal_Z the complete
sum of j=1,...,m_ab-1. Neither part is asserted to be real separately;
their sum is the real R_Z. In particular no sign or vanishing of the
zero mode is assumed.

Here is a uniform, but insufficient, bound on that entire zero mode.
From (8), |E_p(Z)|<=2, and the number of source pairs,

    sum_(v in V) |gamma(v)| << X/q^2.

On the support of (18), av+h is comparable to av, v is between
X/100 and X/25, and |log(1+h/(av))| is comparable to |h|/(av).
Equation (13) therefore gives

    |K_(a,h)(v)| <= C B/(aX) (1+|h|/a)^(-104),
    sum_(h != 0) |K_(a,h)(v)| <= C B/X.                       (20)

In the second inequality, extend only the nonnegative upper envelope
to all integers h and compare its decreasing tail with its integral;
sum_h (1+|h|/a)^(-104)<=C a for every integer a>=1. Values outside
the actual support of K remain zero. Dropping gcd restrictions only
in this absolute estimate, the two bracket sums at j=0 cost together
at most C B X/q^4 after summing h. Since m_ab>=(a+b)X,

    |Zcal_Z| <= C B/q^4 sum* |r_(ga) r_(gb)|/[g(a+b)]
              = C B/q^4 sum_(s!=s'; s,s'<=R) |r_s r_s'|/(s+s')
              <= C B R K_0/q^4 << B R.                       (21)

The equality uses the unique gcd decomposition, and the last inequality
uses s+s'>=2sqrt(ss') followed by
(sum_(s<=R) |r_s|/sqrt(s))^2<=R K_0. These estimates retain the
original unshifted r_s and use only (7); they do not evaluate the
signed zero mode. R/q^2 tends to infinity, so this established bound
does not place Zcal_Z at O(Bq^2). The divergence compares available
upper bounds only and is not a lower bound for Zcal_Z. This particular
zero-mode decomposition also depends on the chosen finite modulus;
it is not an intrinsic main-term obstruction.

For an explicit benchmark on everything left, apply (11) to F_Z on
the length-2B support of w_X, with V there replaced by
N=floor(XR/25) and squared coefficient norm O(q^2) from (9).
It gives integral w_X |F_Z|^2 << B R q^2. Equations (4), (14), (15)
then imply |R_Z|<<B R q^2. Combining with (21) yields

    |Ncal_Z| << B R q^2.                                    (22)

Thus no modes or error terms have been hidden: the transform error is
zero, but the fully summed nonzero-mode estimate available here loses
R relative to the required scale. This generic benchmark is not a new
mean-value theorem and is not a failed lower-bound test for the moment.

**Why the inspected inverse-phase sources do not pay (19).** To test
the prospective inverse-phase conversion, write v=pr and v'=u r',
with p<r, u<r'. The actual near tuples have four distinct source
primes by (16). For fixed a,b,p,u,h put A=ap, D=bu. Then

    (A,D)=1,  D r'-A r=h,
    r = -h inverse(A) (mod D),
    b sqrt(X)/10 <= D <= b sqrt(X)/5.                         (23)

The gcd assertion follows from (a,b)=1, all source primes exceeding
R, and p!=u. The remaining r interval has length sqrt(X)/10,
at most D, so any one such residue class contains at most two integer
points (including any equality endpoint case). At those points r and
(Ar+h)/D must both be primes in their exact original intervals, with
the original kernel and heat amplitudes. No long smooth progression
sum or separated coefficient array has been obtained this way.

Bettin--Chandee--Radziwill, *The mean square of the product of the
Riemann zeta function with Dirichlet Polynomials*,
[arXiv:1411.7764v1, Section 3.2](https://arxiv.org/html/1411.7764v1#S3.SS2),
produces its inverse phase by progression Poisson summation, retains
the zero mode, and separates weights before bounding other modes.
Bettin--Chandee, *Trilinear forms with Kloosterman fractions*,
[arXiv:1502.00769v1, Theorem 1, (1.2), Remark 1/(1.3), Sections 6--7](https://arxiv.org/html/1502.00769v1),
bounds a coprime inverse-phase sum with separate coefficient sequences;
its phase-perturbation allowance has derivative hypotheses. These
precise comparisons and relevant proof cases were already read in
source-notes1418 and are reused, not newly imported or reproved.
Formula (19) has product phases and a joint h,v kernel. Formula (23)
is an inverse congruence, but supplies no source-compatible inverse
exponential sum with the required separate norms. Replacing its prime
indicators by smooth weights or treating the joint weight as a separate
sequence would add an unproved assumption. No theorem is applied to
that substitution. The source-prime interval length observation does
not exclude cancellation over a,b,p,u,h or every other implementation.

The first essential inverse-phase conversion, signed zero-mode payment
and aggregate saving are therefore still unavailable. Stop this
implementation after this one attempt. Equations (17)--(23) preserve
the residual but do not meet the continuation test. This is the third
recorded direct-moment EXPLORATION step (after1448/1450); it neither
renews that budget nor establishes an informative negative result.
The original weighted near estimate, hard-interval moment and all
independent heat/real-channel/actual-Xi transfers remain open. No
change to the main argument assembly, source conclusion or DAG is made.

### Conditional moving-heat variation attempt1456 — 18 November 2026

This is the single parameter-variation test authorized by unchanged
EXPLORE assessment1454, separately approved1455. Keep every hypothesis
above, including the original integer d, fixed prime set, unshifted
tapers, L=floor(X^(1/1000)), R=L^4 and J=[X,sqrt(2)X]. Put
Q_Z(t)=P_Z(t)M(t)^2 and
\[
 F_Z=\int_J|Q_Z(t)|^4dt,\qquad
 V_d=\int_J\int_J
       |\partial_Z(|Q_Z(t)|^4)|\,dZ\,dt.
\]
For the conditional estimates only, assume explicitly
\[
             \sup_{Z\in J}F_Z\le C_0Bq^2,             \tag{24}
\]
where C_0 is an absolute constant. Neither (24) nor (5)'s signed
payment is established here. Constants below, other than the displayed
powers of C_0, are absolute after one original integer-d onset.

**Conclusion and limitation.** The source comparison and the full
finite-polynomial estimate give only
\[
 \int_J|Q_t(t)|^4dt\le B^{-1}\int_JF_Z\,dZ+V_d,
 \qquad V_d\ll C_0^{3/4}B L,                         \tag{25}
\]
and hence the conditional upper bound
C_0 Bq^2+O(C_0^(3/4)B L) for the moving moment. The available variation
bound exceeds the desired scale by L/q^2, which tends to infinity.
This is an insufficient upper bound, not a lower bound on V_d or a
counterexample to the conditional transfer. The derivative moment in
(28) below is the first unpaid norm. Park this variation implementation
after this attempt. The outcome is EXPLORATION / REPRODUCTION, not a
paid transfer, informative lower obstruction or new general theorem.

**Endpoint-valid source application.** Import Montgomery--Vaughan,
*Multiplicative Number Theory II: Primes and Sieves*, author-hosted
draft (version date unidentified), Lemma19.1, (19.6), printed
pp150--151, PDF pp162--163;
[primary source](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=162).
Its complete hypotheses, two-subinterval proof and all-point endpoint
cases were inspected in source-notes1454 and rechecked1455. For
continuous complex f with bounded piecewise continuous first derivative
on [a,b], a<b, it gives, for every x in [a,b],
\[
 |f(x)|\le\frac1{b-a}\int_a^b|f(u)|du+
                           \int_a^b|f'(u)|du.
\]
Use (19.6), not the midpoint version (19.5); no midpoint coefficient
or the source's noted midpoint misprint is an input. This known
inequality is imported, not reproved.

For each fixed t, take f(Z)=|Q_Z(t)|^4 and x=t on [a,b]=J.
The prime support and all coefficients of M are fixed while Z varies.
Each E_p is smooth for positive Z; all sums are finite. Thus f is
continuously differentiable with bounded derivative on the closed J,
including its endpoints. The function and its derivative are continuous
on the compact product J times J, so their absolute integrals are
finite. Integrating the source inequality in t and applying Fubini
proves the first part of (25), including t at either endpoint. No
height is moved outside J, and no entry-floor derivative is introduced.

**Exact heat derivative.** Write v=v_p(Z)=(1/2)log(Z/(2pi))-log p.
The original exponent is Z^2(v+i*pi/4)^2/(8d). Since v'=1/(2Z),
direct differentiation gives
\[
 \partial_Z E_p(Z)=\frac{Z}{8d}E_p(Z)\kappa(v_p(Z)),
 \quad \kappa(v)=2v^2+v-\frac{\pi^2}{8}
                         +i\pi(v+\tfrac14).          \tag{26}
\]
The real and imaginary terms in (26) both retain their derivatives;
this is the partial derivative with t held fixed. Audit1450's scale
calculation gives v in an absolute compact interval, |E_p|<=2 and
d comparable to X^2q^2. Hence |kappa(v)|<=C and
Z/(8d)<=C/(Xq^2), uniformly on J. Define the exact finite polynomial
\[
 U_Z(t)=\sum_{p\in\mathcal P}
           E_p(Z)\kappa(v_p(Z))p^{-1/2-it},\qquad
 G_Z=\int_J|U_Z(t)M(t)^2|^4dt.                       \tag{27}
\]
Then partial_Z Q_Z=(Z/(8d))U_Z M^2. The identity
partial_Z |Q|^4=4|Q|^2 Re(partial_Z Q * conjugate(Q)) holds also
at zeros of Q. Its absolute value is at most 4|Q|^3|partial_Z Q|.
Holder in t with exponents 4/3 and 4, followed by integration in Z,
therefore yields
\[
 V_d\le\frac1{2d}\int_J Z F_Z^{3/4}G_Z^{1/4}\,dZ
 \ll\frac{C_0^{3/4}B^{3/4}}{Xq^{1/2}}
                                \int_JG_Z^{1/4}\,dZ. \tag{28}
\]
All integrals are finite before Holder is applied. In particular no
coefficientwise domination is asserted to be an L4 multiplier bound.

For this sufficient estimate, a payment
\[
 \frac1B\int_JG_Z^{1/4}\,dZ\ll B^{1/4}q^{5/2}        \tag{29}
\]
would imply V_d=O(Bq^2), since B/X=sqrt(2)-1. The stronger uniform
condition G_Z=O(Bq^10) would suffice as well. Even this logarithmically
more generous norm budget is not proved. Neither (29) nor that uniform
condition is claimed necessary: the absolute real-part estimate and
Holder in (28) can lose cancellation.

**Actual complete cost of the available mean-value input.** Put
a_p=E_p(Z)kappa(v_p(Z)). For source products v=pr, p<=r in P, let
c_(pr)=2a_p a_r if p<r, and c_(p^2)=a_p^2. This v is an integer
product index, distinct from the real variable v_p(Z) in (26).
The exact identity is
\[
 (U_Z(t)M(t)^2)^2
   =U_Z(t)^2M(t)^4
   =\sum_{v,s}\frac{c_v r_s}{\sqrt{vs}}(vs)^{-it}.
\]
Every source prime exceeds R eventually, so unique factorization
recovers the full source pair from k=vs and then s. This includes
p=r: repeated source primes are retained, with the coefficient above.
All indices satisfy k<=N=floor(XR/25). Using (7), (8) and |a_p|<=C,
\[
 \sum_v\frac{|c_v|^2}{v}
   =2\left(\sum_p\frac{|a_p|^2}{p}\right)^2
                         -\sum_p\frac{|a_p|^4}{p^2}
   \ll q^{-2},\qquad
 \sum_k\left|\frac{c_vr_s}{\sqrt{vs}}\right|^2
       =K_0\sum_v\frac{|c_v|^2}{v}\ll q^2.           \tag{30}
\]
Apply exactly (11), the already justified specialization of
Montgomery--Vaughan G.16/(G.25)--(G.28), printed pp426--427 of the
same primary source, to this fixed-Z polynomial on J. This does not
reprove the source theorem or require a new reciprocal-series input.
Grouping has been justified, the coefficients are fixed during t
integration, and the actual length N is retained. It gives
\[
 G_Z\ll[B+3\pi(N+1)]q^2
      \ll B R q^2,\qquad
 \frac1B\int_JG_Z^{1/4}\,dZ
      \ll B^{1/4}Lq^{1/2}.                           \tag{31}
\]
Empty prime supports cause no exception; all polynomials then vanish.
For the eventual scales R>=1, N+1=O(XR) and B is a fixed positive
multiple of X, verifying the second estimate uniformly. Substituting
(31) in (28) gives V_d<<C_0^(3/4)B^2 L/X, which is the second part
of (25). No factor of B from parameter integration has been dropped.

Since L=floor(exp(q/1000)), L/q^2 tends to infinity. Equivalently the
generic bound G_Z=O(BRq^2) misses the sufficient uniform Bq^10 budget
by R/q^8. These comparisons describe only the achieved bounds; they
establish no growing lower bound for either actual norm. The premise
(24), signed remainder (5), two own heat times, shifted intervals,
distinct-pair transfer, real denominator, signed numerator, E_P and
actual-Xi realization remain unresolved. Neither PROOF's assembly nor
the direct dependencies change: C019p/C019y/C019z were already the
inputs to this canonical result, with (7)--(11) reused internally.

## Mathlib

Full matching coverage of (2)--(6) is not checked. Supporting finite
sum algebra, integration and Cauchy--Schwarz do not by themselves
formalize the prime/coefficient specialization or the unpaid signed
estimate. The sources checked supply (10) and qualitative PNT, not
the target fourth moment. No absence claim or new Mathlib lookup is made.
Audit1450 checks the informal specialization only and does not change
this coverage status.

Attempt1453 does not change that status. Full matching coverage of its
weighted determinant specialization and unpaid estimates is unchecked;
finite orthogonality and elementary gcd algebra are supporting tools,
not a formal verification of the requested fourth moment.

Attempt1456 likewise has no checked full matching Mathlib theorem.
Finite differentiation, Holder and integration are supporting tools;
their existence does not certify (24), (29) or the desired transfer.
The cited interval and finite-frequency inequalities are known inputs;
the exact heat-family accounting here is an informal specialization.

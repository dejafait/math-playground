# Lemma 479: a resonant evaluation of the complete grouped cross term

## Hypotheses

Use precisely the finite sums in L478 (13), with

    Y=T/(2 pi), M=floor(sqrt Y), L=log T,
    theta(t)=Im log Gamma(1/4+it/2)-t log(pi)/2,
    W(n,m,k,l)=log(n/m)^2 log(k/l)^2,
    J(1,m/h)=integral_T^(2T) exp(i(2 theta(t)+t log(m/h)))dt,
    g_(h,m)=1/sqrt(hm)
              *sum_(nkl=h; n,k,l<=M) W(n,m,k,l).

All indices are positive integers. T tends to infinity through arbitrary
real values; the integral is on the closed interval [T,2T]. The phase
is the actual theta, with L316's uniform expansion

    2 theta(t)=t log(t/(2 pi e))-pi/4+O(1/T),  T<=t<=2T.    (1)

Only the defining finite regrouping of L478 is needed, and it is checked
again below; this does not constitute a critical audit of its other
moment formulas. No RH, zero spacing, simplicity, external half-plane,
random-phase or contour-shift hypothesis is imposed.

## Conclusion

For each m,k,l<=M set

    A=Y m/(kl), B=min(M,2A),
    F_m(x)=x[(log(x/m))^2-2 log(x/m)+2].

Define the explicit real arithmetic quantity

    Q(T)=4 pi sum_(m,k,l<=M; m divides kl; A<M)
            [log(k/l)^2/m] [F_m(B)-F_m(A)].                 (2)

The complete signed cross term has the evaluation

    C(T):=2 Re sum_(m<=M;h<=M^3) g_(h,m) J(1,m/h)
         =Q(T)+O(T L^6).                                  (3)

The constants are absolute for sufficiently large T. In particular the
error is o(T L^8), and there are absolute c,C>0 such that

    c T L^8 <= Q(T) <= C T L^8.                            (4)

Thus C(T) is eventually positive and comparable to T L^8; it is not a
little-o term at that scale. Formula (2), involving only finite divisor
conditions and elementary real functions, evaluates the main term to
the requested absolute error. It does not assert that Q(T)/(T L^8)
has a limit or give such a limiting constant.

All original four cutoffs and both endpoint layers are accounted for.
This is local progress on one part of L478's second moment. It gives
neither the complete second moment nor its needed fourth-moment bound,
either L477 defect threshold, negative-mass saving, individual-height
signs or RH. It specializes standard saddle and finite summation
methods; the assessed sources contain no matching complete evaluation,
but originality is not certified. The separate critical audit in
Section 6 verifies this evaluation without changing its bounds. It
does not audit L478's other moment formulas or Gonek's full paper.

## Proof

### 1. The scalar source and its normalization

The analytic input is S. M. Gonek, *Mean values of the Riemann
zeta-function and its derivatives*, Invent. Math. **75** (1984),
123--141, Lemma 2, p. 130, formulas (24)--(25)
([primary PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf)).
For fixed real a, large A_0, A_0<B_0<=2A_0 and r>0 it states

    integral_(A_0)^(B_0) exp(it log(t/(r e)))
                        (t/(2 pi))^(a-1/2) dt
      =1_(A_0<r<=B_0) (2 pi)^(1-a) r^a exp(-ir+i pi/4)
         +O(A_0^(a-1/2))
         +O(A_0^(a+1/2)/(|A_0-r|+sqrt A_0))
         +O(B_0^(a+1/2)/(|B_0-r|+sqrt B_0)).

Use a=1/2, A_0=T, B_0=2T and r=2 pi nkl/m. These are allowed
real saddle parameters; they need not be integers. By (1) the change
in the integrand from the phase approximation is O(1/T) uniformly
in all four indices. Its integral is O(1). The factor exp(-i pi/4)
from theta cancels the source's exp(i pi/4). Consequently

    J(1,m/(nkl))
      =1_(T<r<=2T) 2 pi sqrt(nkl/m) exp(-2 pi i nkl/m)
        +O(1+K_T(r)+K_(2T)(r)),
    K_H(r)=T/(|H-r|+sqrt T),             H=T,2T.            (5)

Replacing sqrt(2T) by sqrt T in the second endpoint error only changes
an absolute constant. The source's half-open indicator is retained
exactly. At r=T or r=2T its error is of full saddle size; no endpoint
half-weight formula is assumed. The actual integral remains over the
closed interval, whose endpoint points have zero Lebesgue measure.
The source is cited, not reproved; only its normalization and summed
error for the present coefficients are established here. Its summed
c>1 lemmas and Shiu's theorem are not used.

Finite regrouping h=nkl gives exactly

    C(T)=2 Re sum_(n,m,k,l<=M)
                     W(n,m,k,l)/sqrt(nmkl) J(1,m/(nkl)).   (6)

This checks the L478 (13) input, without any interchange of infinite
sums. For M>=2, W<=C L^4 and

    sum_(n,m,k,l<=M) W/sqrt(nmkl) <= C M^2 L^4,             (7)

since sum_(j<=M) j^(-1/2)<=2 sqrt M. Thus the O(1) error in
(5), including the phase replacement, costs O(T L^4).

### 2. Both endpoint errors, including nonstationary indices

If r<T/2 or r>4T, both K_T(r) and K_(2T)(r) are bounded by an
absolute constant. Equation (7) pays for all these terms, including
arbitrarily distant nonstationary saddles.

In the remaining region T/2<=r<=4T,

    W/sqrt(nmkl) <= C L^4/(m sqrt T).                      (8)

Fix m,k,l and write d=2 pi kl/m, so r=dn. If at least one n<=M
lies in this region, then d>=T/(2M)>=c sqrt T. For either H=T
or H=2T, a lattice of spacing d has O(1) points with
|dn-H|<=sqrt T, and at most C(1+2^j sqrt T/d) points in each
annulus 2^j sqrt T<|dn-H|<=2^(j+1) sqrt T. Here 0<=j<=C log T
suffices, since H and r are in the fixed stated multiples of T.
The central terms of K_H total O(sqrt T). Each annulus contributes
at most

    C[ sqrt T 2^(-j)+T/d ].

It follows that, uniformly in these fixed indices and any endpoint
coincidence,

    sum_(n<=M; T/2<=dn<=4T) K_H(dn) <= C sqrt T log T.       (9)

When the region is empty there is no contribution. Multiplying (9)
by (8) and summing all m,k,l<=M gives

    sum_(n,m,k,l<=M) [W/sqrt(nmkl)]
                          [K_T(r)+K_(2T)(r)]
       <= C M^2 L^5 sum_(m<=M) 1/m + C M^2 L^4
       <= C T L^6.                                       (10)

In particular near misses, exact coincidences at either endpoint and
all interior and exterior cases are charged; no separation of T from
the saddle set is assumed. Inserting (5) into (6) now gives

    C(T)=4 pi Re sum_(m,k,l<=M) [log(k/l)^2/m]
                 sum_(A<n<=B) log(n/m)^2 e(-nkl/m)
                +O(T L^6),                               (11)

where e(x)=exp(2 pi i x), A=Y m/(kl), B=min(M,2A), and an empty
interval contributes zero. Because Y>=M^2>=kl, A>=m>=1.
Thus the inner interval incorporates the original n>=1 cutoff and
its weight is nonnegative and increasing. No individual cutoff was
replaced by an unrestricted ternary divisor weight.

### 3. Nonresonant residue classes are below the error scale

For a real alpha not an integer and any consecutive integer interval,
the exact geometric series bounds its exponential sum by

    min(number of terms, 1/|sin(pi alpha)|)
          <= min(number of terms, 1/(2||alpha||)).

This is the elementary finite geometric-series identity, or the
finite cyclic Fourier summation covered by T. Tao, *245C Notes 2:
The Fourier transform* (6 April 2009), Section 2, Lemma 17 and the
finite cyclic case of Theorem 21
([primary notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/)).
It holds for every positive integer modulus. Abel summation on the
interval A<n<=B in (11), using the increasing weight log(n/m)^2
and its supremum at most (log M)^2, therefore gives

    |sum_(A<n<=B) log(n/m)^2 e(-nkl/m)|
             <= C L^2/||kl/m||                 if m does not divide kl.
                                                               (12)

Indeed a monotone nonnegative weight contributes its supremum plus
total variation, at most twice that supremum; arbitrary fractional
endpoints do not change this bound. Empty intervals satisfy it too.

Fix m,k, put g=gcd(k,m), q=m/g and a=k/g. For q>1, a is a unit
modulo q. In one complete residue system for l modulo q the nonzero
residues a l permute 1,...,q-1, and

    sum_(j=1)^(q-1) 1/||j/q|| <= C q log(2q).

There are at most floor(M/q)+1 copies of each residue among l<=M.
Since q<=m<=M, this proves

    sum_(l<=M; m does not divide kl) 1/||kl/m||
                  <= C M log(2m).                         (13)

For q=1 the sum is empty. This treats all composite moduli and all
noncoprime k,m without suppressing their resonances. Multiplying
(12) by log(k/l)^2/m, summing (13) over k, then over m, shows that
the entire nonresonant contribution in (11) is at most

    C L^4 M^2 sum_(m<=M) log(2m)/m <= C T L^6.              (14)

This bounds the retained signed arithmetic sum outside its exact
resonances; it is stronger than merely displaying a transformed sum.

### 4. Explicit evaluation of the resonances

If m divides kl, e(-nkl/m)=1 for every integer n. On A<n<=B
the increasing function f(x)=log(x/m)^2 obeys

    sum_(A<n<=B) f(n)=integral_A^B f(x)dx+O(L^2),          (15)

uniformly whenever A<M; otherwise both quantities are zero. One
way to see (15) is to compare with the integral over the consecutive
unit cells: the total monotone variation and the two clipped endpoint
cells cost at most three times sup f. This is a finite sum, not an
Euler--Maclaurin asymptotic with an unbounded remainder.

For the summed error, the number of pairs k,l<=M with m|kl is at most

    sum_(k<=M) floor(M gcd(k,m)/m)
       <= (M/m) sum_(k<=M) gcd(k,m)
       <= M^2 tau(m)/m.                                  (16)

The last inequality follows from
gcd(k,m)<=sum_(d|m;d|k)d, and then
sum_(k<=M;d|k)d=d floor(M/d)<=M. No estimate in a progression
for a divisor function is used. Moreover

    sum_(m>=1) tau(m)/m^2
      =sum_(a,b>=1) 1/(a^2 b^2)<infinity,

where nonnegative summands justify this elementary product identity.
The total (15) error, with the weights from (11), is consequently
O(M^2 L^4)=O(T L^4). Since F_m'=f, (15) proves exactly (2)--(3).
Each term in (2) is nonnegative. This is an explicit nonoscillatory
divisor sum with elementary summands, not an unsigned bound for an
uncontrolled oscillatory main sum.

### 5. Size of the explicit main term

First, B<=2A gives

    (1/m) integral_A^B log(x/m)^2 dx
            <= Y/(kl) [log(2Y/(kl))]^2.                   (17)

For large T, 1<=Y/M^2<=2. Put u=log(M/k), v=log(M/l).
Then log(k/l)^2=(v-u)^2<=(u+v)^2 and
log(2Y/(kl))<=log 4+u+v. Ignore only restrictions in a nonnegative
upper sum: there are at most tau(kl)<=tau(k)tau(l) possibilities
for m dividing kl. The latter inequality follows prime by prime
from r+s+1<=(r+1)(s+1) for nonnegative exponents. Thus

    Q(T)<=C Y sum_(k,l<=M)
           [tau(k)tau(l)/(kl)] (1+u+v)^4
        <= C Y (1+log M)^8,                               (18)

because
sum_(k<=M)tau(k)/k=sum_(ab<=M)1/(ab)<=(1+log M)^2.
This establishes the upper part of (4) by elementary finite counting.

For a lower bound, the parametrization

    k=da, m=db, l=bc, gcd(a,b)=1                           (19)

is injective: d=gcd(k,m), then a,b,c are determined. Every such tuple
has m|kl. Write H=log M and restrict to the integer boxes

    M^(39/50)<=a<=M^(4/5),
    M^(2/25)<=b<=M^(1/10),
    M^(29/50)<=c<=M^(3/5),
    M^(2/25)<=d<=M^(1/10),             gcd(a,b)=1.          (20)

The cutoffs are respected: k<=M^(9/10), l<=M^(7/10),
m<=M^(1/5). Also

    A=Y b/(ac)<=2 M^(37/50),  hence 2A<=M eventually,
    log(k/l)>= (4/25)H,
    log(A/m)=log(Y/(abcd))>= (2/5)H.                      (21)

Here Y>=M^2 and abcd<=M^(8/5). On these boxes B=2A and the
summand in (2) is therefore at least

    c_1 Y H^4/(abcd)                                      (22)

for an absolute c_1>0. None of these terms lies in a disappearing
endpoint interval.

For clarity the needed harmonic coprime count can be checked without
an additional divisor-distribution input. Let A_0=M^(39/50),
A_1=M^(4/5), B_0=M^(2/25), B_1=M^(1/10) and
H_a=log(A_1/A_0)=H/50, H_b=log(B_1/B_0)=H/50.
The unrestricted harmonic masses on these integer intervals are
H_a+O(1/A_0) and H_b+O(1/B_0). For an integer r>=2,

    sum_(A_0<=a<=A_1;r|a) 1/a <= H_a/r+1/A_0,
    sum_(B_0<=b<=B_1;r|b) 1/b <= H_b/r+1/B_0.              (23)

These follow by an integral comparison for decreasing 1/x on the
successive multiples of r. Every noncoprime pair has a common
integer divisor 2<=r<=B_1. The union bound and (23) bound its
harmonic mass by

    H_a H_b sum_(r=2)^infinity 1/r^2
     +O((H_a/B_0+H_b/A_0)log(2B_1)+B_1/(A_0 B_0))
        <= (3/4)H_a H_b+o(H^2).                           (24)

The inequality sum_(r>=2)r^(-2)<=1/4+integral_2^infinity x^(-2)dx
=3/4 suffices. All displayed error terms are o(H^2) for the
specified powers. Subtracting from the unrestricted mass shows

    sum_((a,b) in (20);gcd(a,b)=1) 1/(ab) >= c_2 H^2.       (25)

The separate c and d intervals each have harmonic mass
H/50+o(1). Summing (22), using injectivity (19) and (25), proves
Q(T)>=c_3 Y H^8. Since Y is proportional to T and log M is
asymptotic to (log T)/2, (4) follows. In combination with (3),
the relative evaluation error is O((log T)^(-2)). No numerical
test, conjectural cancellation or independence assumption is used.

### 6. Independent critical application audit

The 29 October 2026 audit reuses the invocation-start assessment for
the exact complete cross term. It checks (1)--(25), rather than only
the positive subfamily or the final logarithmic exponents. No new
moment theorem, strengthened asymptotic or numerical certificate is
claimed. The following are the load-bearing checks.

**Phase, normalization and source scope.** Taking imaginary parts of
L316 (7) on the positive real axis gives (1); its analytic remainder
is uniform over [T,2T]. There is no differentiated real-variable error
or hypothesis concerning zeros here. The fixed a=1/2 specialization
of Gonek's cited Lemma 2 has amplitude sqrt(2 pi r). With
r=2 pi nkl/m, multiplication by exp(-i pi/4) and then by
1/sqrt(nmkl) gives exactly 2 pi/m times exp(-2 pi i nkl/m).
The outer 2 Re explains the 4 pi in (11) and (2).
The scalar error constants do not depend on the growing cutoff or on
these rational saddle parameters. The actual-theta replacement costs
O(1) per integral and O(T L^4) after summation, as in (7).

Closed endpoint specializations require no half-weight assertion.
One can take interior parameter limits in the scalar formula: r
approaching B from below retains the full indicated main term, whereas
r approaching A from below retains none. The endpoint error is of
full saddle size, and its displayed bound is continuous in r. Taking
B upwards to 2A is also legitimate, using simultaneous interior r
limits if r=B. Finite-interval integrals are continuous in these
positive parameters, with bounded integrands on a compact parameter
neighborhood. Thus even a strictly interior formulation of the source
extends to the conventions used in (5). This is an endpoint
specialization of the cited theorem, not its reproof.

The primary PDF's Lemma 2 and its near-endpoint, interior and exterior
proof cases on p. 130 were replayed against the retained source
assessment. The web mathematical text was available; screenshot calls
returned no inspectable image and the shell PDF download failed DNS.
No new visual verification is claimed. This does not remove the
previously inspected, ready scalar-theorem coverage, and no omitted
summed c>1 theorem or Shiu estimate is used.

**Uniform total errors.** In the middle range r in [T/2,4T],
nkl=rm/(2 pi), so the coefficient in (8) is at most
C L^4/(m sqrt T). Existence of even one such n<=M forces
d=2 pi kl/m>=T/(2M), independently of how close a saddle is to
either endpoint. The central lattice interval contributes O(sqrt T);
the dyadic annuli contribute O(sqrt T+(T/d)log T).
After summing k,l and the harmonic m weight this is O(T L^6).
Outside the middle range both endpoint kernels are O(1), so (7)
covers the remaining indices. These cases partition the full sum.

For the arithmetic main sum, A>=m makes log(n/m)^2 monotone on
every nonempty inner interval. After the gcd reduction, multiplication
by k/gcd(k,m) permutes the nonzero residues modulo q=m/gcd(k,m).
Because q<=M, their total reciprocal-distance cost over l<=M is
O(M log(2m)), including incomplete terminal residue blocks.
Equation (14) follows with no coprimality assumption on the original
indices. For resonant pairs the integral replacement costs O(L^2)
per pair; (16) makes its total O(M^2 L^4), since
sum tau(m)/m^2 converges. The two error scales are both within (3).
When A>=M the resonant term is omitted, rather than interpreted as a
negative integral from A to M. Fractional endpoints and the empty
case A=M therefore cause no extra contribution.

**Both main-term bounds.** The upper bound (18) enlarges only a
nonnegative sum; it uses tau(kl)<=tau(k)tau(l) and two elementary
harmonic divisor sums. For the lower bound, (19) is injective because
gcd(k,m)=d when gcd(a,b)=1. The boxes give
k<=M^(9/10), l<=M^(7/10), m<=M^(1/5),
A<=2M^(37/50), log(k/l)>=4H/25 and log(A/m)>=2H/5.
Consequently B=2A eventually and the full interval of length A
contributes the lower summand (22), with no disappearing width.
The largest exponents in the three errors in (24) are respectively
-2/25, -39/50 and 1/10-39/50-2/25=-19/25; logarithms do not prevent
their being o(H^2). The common-divisor union bound leaves at least
(1/4)H_a H_b+o(H^2) coprime harmonic mass. Each of the separate c,d
intervals supplies H/50+o(1). Thus the four harmonic factors and the
four explicit logarithmic powers give H^8 with a positive absolute
constant. Finally Y=T/(2 pi), H~L/2 and L^6=o(L^8) uniformly as
real T grows. Equations (3)--(4), including eventual positivity,
survive the audit without correction.

Only L478's defining finite grouping and L316's gamma phase are used
as local mathematical inputs; the other conclusions of L478 are not
silently upgraded by this audit. The audited result remains one
cross-term evaluation, with existential constants and onset. It
does not establish a full second or fourth moment, either L1 defect
threshold, a limiting main-term constant, or any Xi sign assertion.

## Mathlib

Full matching theorem: not checked. Supporting finite geometric sums,
Abel summation, divisor counting, coprimality, elementary antiderivatives
and the oscillatory integral: no specific Mathlib declarations checked.
Unknown coverage is not evidence of absence. The precise non-elementary
input is Gonek's scalar Lemma 2, with L316's already retained gamma
phase; the finite cyclic reference is given above. The finite counting
arguments are included because the sources do not state the weighted,
sharply truncated summed error or the resonant quantity (2). The
elementary common-divisor bound is enough for the polynomial boxes;
no unreviewed asymptotic theorem about divisor distribution is imported.

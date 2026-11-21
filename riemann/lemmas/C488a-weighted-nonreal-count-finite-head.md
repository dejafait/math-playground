# Corollary 488a: audited weighted nonreal-count transport on a finite head

## Hypotheses

Use the actual theta family of L019, L020 and L058, in the normalization

    H_t(z) = integral_0^infinity exp(t u^2) Phi(u) cos(zu) du,
    Phi(u) = sum_(n>=1) (2 pi^2 n^4 exp(9u)-3 pi n^2 exp(5u))
                       exp(-pi n^2 exp(4u)).

Thus H_0(z)=xi((1+iz)/2)/8 and F(lambda,z)=8 H_(4lambda)(2z),
as verified in L488. Fix

    V=6000000000000, X=5999347341500, R=3000000,
    U=6100000000000, T=1/5, and a real number |a|<=X.

Use the published finite-height theorem of Platt--Trudgian and the
Polymath/de Bruijn inputs precisely stated below. No RH, all-real exterior,
global simplicity, positive minimum nonreal ordinate, or uniform zero
separation is assumed. All zero sums count multiplicity.

## Conclusion

For every 0<=t<=T define, for each zero z_j=x_j+i y_j of H_t,

    w(x)=exp(-sqrt(1+((x-a)/R)^2)),
    Q(x)=V+sqrt(x^2+R^2),
    eta(x)=R/(4 Q(x) log(4 Q(x))), p(x)=w(x) eta(x),
    A_j=1_(y_j != 0) (w(x_j)|y_j|+p(x_j)), A(t)=sum_j A_j.

The sum converges, and uniformly over the stated closed ranges,

    A(t)<exp(-87),             eta(a)/e>5*10^(-10)>exp(-87).       (1)

Consequently every zero of H_t with |Re z|<=X is real for 0<=t<=1/5.
In local F coordinates the same conclusion holds for
0<=lambda<=1/20 and |Re z|<=2999673670750. Multiplicities are retained;
this conclusion does not assert simplicity.

This is a reproduction and conceptual audit of bramble_trace's
Appendix B, not a new theorem beyond that manuscript. It does not
verify its other appendices, computational supplement, or claimed bound
for the de Bruijn--Newman constant. It gives no all-height reality,
uniform overlap with L488 as t decreases to zero, or actual-Xi
all-degree mixed positivity in L030-L032/C032a.

## Proof

### Sources and exact scope

The audited source is bramble_trace, *An unsigned strip bound for the
de Bruijn--Newman constant*, rStation paper186, v1, 20 November 2026,
[Section 1 and Appendix B, (B.1)-(B.6) and its final comparison](https://rstation.ai/problems/riemann_hypothesis/papers/186).
The complete relevant proof was read. The source's reviewer report
and its unrun check_head.py are not verification evidence here.
The independent replay is warranted by its discontinuous count weight,
signed pair cancellations, and endpoint passage, which the published
general heat theorems alone do not establish.

Import D. H. J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function, and a new upper bound for the
de Bruijn--Newman constant*, Research in the Mathematical Sciences
6 (2019), article 31,
[arXiv:1904.12438v2, Proposition 3.1(i)-(ii), proof (28)-(33),
Theorems 1.5(i) and 3.2](https://arxiv.org/html/1904.12438v2).
Proposition 3.1 applies at every real time to a selected simple zero
even when other zeros are complex or repeated. With the other zeros
paired by z_k,-z_k, its velocity is

    z_j'=2 sum_(k != j)' 1/(z_j-z_k).                            (2)

At a zero z_0 of multiplicity m>=2 at time s, its m nearby zeros
are z_0+sqrt(2(t-s))*lambda_l+O(|t-s|), where lambda_l are the
distinct real roots of the probabilists' Hermite polynomial He_m.
The primary proof gives the uniform rescaled expansion and exhausts
the cluster by Rouche, not just an enumeration of some of its zeros.
We use that fact to count multiplicities in the collision argument.

Theorem 3.2 restates N. C. de Bruijn, *The roots of trigonometric
integrals*, Duke Math. J. 17 (1950), 197-226, Theorem 13: if H_s has
no zero above height h>0, then H_t has no zero above
sqrt(max(h^2-2(t-s),0)) for t>s. The initial xi strip and conjugation
therefore give |Im z_j|<=1 throughout [0,T]. L488 supplies the
audited specialization of Theorem 1.5: on every [tau,T], tau>0,
all nonreal or multiple zeros are inside one fixed compact rectangle.
It supplies no confinement constant at tau=0. Its parameter domain
applies since 0<tau/4<=T/4=1/20<1/8.

Import D. Platt and T. Trudgian, *The Riemann hypothesis is true up
to 3*10^12*, Bull. London Math. Soc. 53 (2021), 792-797,
DOI 10.1112/blms.12460,
[arXiv:2004.09765v1, Theorem 1 and Section 2](https://arxiv.org/html/2004.09765v1).
Their theorem reaches ordinary height 3000175332800; only the smaller
closed range 0<gamma<=3*10^12 is used. Section 2's total zero count,
not an unverified list of observed zeros, is the cited input. Under
H_0(z)=xi((1+iz)/2)/8, gamma=Re z/2. Conjugation covers negative
ordinates. There are no imaginary-axis zeros of H_0, since its
positive kernel gives H_0(iy)=integral Phi(u)cosh(yu)du>0 for real y.
Thus every initial zero with |x|<=V is real, including x=0 and the
two endpoints. No computational replay of the published theorem is
claimed. L058's joint entire dependence justifies the local continuity
and differentiation used below.

### Uniform count, growth and summation conventions

Here is a replay of the source's uniform count bound, needed in every
tail estimate. Elementary estimates 31/10<pi<22/7 suffice. For n>=2,

    4 log n <=4(n-1)<=(pi/2)(n^2-1).

With v=exp(4u)>=1, this gives

    sum_(n>=1) n^4 exp(-pi(n^2-1)v)
       <=sum_(n>=1) exp(-pi(n-1)/2)<2.

The exponential series gives 8u^2<=exp(4u), hence t u^2<=exp(4u)/40.
Dropping the negative term of Phi and using 4pi^2<40 and
pi-1/40>3 yields

    exp(tu^2) Phi(u)<=40 exp(9u-3 exp(4u)).                       (3)

On 0<=u<=1/100 the n=1 prefactor is greater than 9, while
pi exp(1/25)<(22/7)(25/24)<4. Therefore
H_t(0)>=H_0(0)>9/(100 e^4)>10^(-3); here e<3 implies e^4<81<90.

For |z|<=rho, put q=rho+9. Maximizing q u-exp(4u) for u>=0
shows it is at most (q/4)log(q+1). Also
integral_0^infinity exp(-2 exp(4u))du<1, for example by
exp(4u)>=1+4u. Thus (3) implies

    log max_(|z|<=rho)|H_t(z)|
       <=log40+((rho+9)/4)log(rho+10).

All copies counted by N_t(r)=#{j:|x_j|<=r} lie in |z|<=r+1.
Jensen with outer radius 3(r+1) gives, using log3>1,

    N_t(r)<=12+((3r+12)/4)log(3r+13)
          <=(r+20)log(4r+40)=:N(r),      r>=0.                 (4)

For the last inequality, replace the smaller logarithm by log(4r+40)
and use (r/4+17)log(4r+40)>12. The bound log40000<12 used here
follows, for example, from e^12>2800*50>40000; elementary exponential
comparisons used throughout are justified in the scalar section below.
If the outer Jensen circle contains a zero, use radii decreasing to
it from above; this changes neither the upper estimate nor the count.

The growth is of order at most one, and (4) implies sum_j |z_j|^(-2)
converges after omitting any bounded initial portion. Evenness and
H_t(0)>0 remove the linear exponential factor in Hadamard's product.
Thus the paired product in Proposition 3.1 is applicable, and (2)
agrees with symmetric horizontal cutoffs. Opposite pairs have equal
|Re z_k|, so these cutoffs do not split them. Vertical reciprocal
tails converge absolutely, and the horizontal tails converge after
opposite pairing. We do not assert absolute convergence of the
unpaired complex reciprocal sum.

### Weight derivatives

Set delta=R/V=1/2000000. Direct differentiation, with
v=(x-a)/R, gives |w'|<=w/R and

    R^2 w''/w=v^2/(1+v^2)-(1+v^2)^(-3/2),

so |w''|<=w/R^2. For f(q)=log(q log(4q)) on q>=V,
|f'|<=2/q and |f''|<=3/q^2. As |Q'|<=1 and |Q''|<=1/R,
eta'/eta=-f'(Q)Q' implies

    |eta'|<=2eta/V,
    |eta''|<=eta(7/V^2+2/(VR)).

Consequently

    |p'|<=(1+2delta)p/R<=1.01p/R,
    |p''|<=(1+6delta+7delta^2)p/R^2<=1.01p/R^2.                 (5)

The latter numerical bounds even hold for delta<=1/1000.
On a segment of length at most R, each of w,p is at most three
times its value at either endpoint: integrate its logarithmic derivative
and use e^(1.01)<3. In particular the same comparison with the smaller
of two endpoint values is available. Also 0<eta<1.

### Nearby pair estimates and the count absorption

Fix a regular time when the nonreal zeros are simple. There are only
finitely many of these at positive time by L488. For a pair put
d=x_j-x_k, b=y_j-y_k, D=d^2+b^2, and abbreviate w_j=w(x_j).
The contribution of an unordered pair of nonreal zeros to the
derivative of the linear-height part, after removing the factor 2/D,
is exactly

    d(w'_j |y_j|-w'_k |y_k|)
       -b(w_j sgn(y_j)-w_k sgn(y_k)).                         (6)

If both signs equal sigma, write Y_j=|y_j|, Y_k=|y_k|. Expression
(6) becomes

    [d(w'_j+w'_k)/2-(w_j-w_k)] sigma b
       +(d/2)(w'_j-w'_k)(Y_j+Y_k).

For M=sup_segment |w''|, the first bracket is bounded by M d^2/4.
Indeed the integral kernel for the trapezoid error has absolute
integral d^2/4. The second coefficient is bounded by M d^2/2.
Since |b|<=Y_j+Y_k and d^2/D<=1, the pair costs at most
(3/2)M(Y_j+Y_k). For |d|<=R, M<=3min(w_j,w_k)/R^2, so this is
at most (9/2)(w_jY_j+w_kY_k)/R^2. This remains valid at d=0.

If the signs are opposite, the vertical term in (6) is
-(w_j+w_k)(Y_j+Y_k). The horizontal term is at most
(|d|/R)(w_jY_j+w_kY_k), so the total is nonpositive for |d|<=R.
For a mixed pair with y_k=0 only j contributes: the corresponding
numerator is d w'_j Y_j-w_jY_j, also nonpositive in this range.
This uses no minimum value of Y_j.

Reserve each nonreal zero's own conjugate separately. Its velocity
contribution is 2/(2iy_j)=-i/y_j, giving -w_j/Y_j per copy in A'.
It has no horizontal or count contribution. Thus a conjugate pair
contributes -2w_j/Y_j; assigning half to each copy is consistent with
the unordered-pair computation.

For a pair of nonreal zeros the count numerator is d(p'_j-p'_k).
Its contribution is at most 2sup_segment |p''|, bounded by
6.06 min(p_j,p_k)/R^2<=3.03(p_j+p_k)/R^2. Combining with the
linear estimates, each nearby nonreal pair other than own conjugates
therefore costs at most 5(A_j+A_k)/R^2.

For a mixed pair the count derivative at j is 2d p'_j/D. Since
2|d|Y_j<=d^2+Y_j^2, its upper bound is |p'_j|/Y_j. Write
m=|x_j|+R. Every nearby real copy has |x_k|<=m. From V>=R+20,

    Q(x_j)>=m+20,
    N(m)=(m+20)log(4m+40)<=Q(x_j)log(4Q(x_j)).

All such mixed count contributions at j sum to at most

    N(m)|p'_j|/Y_j <=1.01 w_j/(4Y_j)<w_j/(2Y_j).             (7)

This is absorbed by its reserved loss w_j/Y_j. Real copies of any
multiplicity are counted separately, and (7) pays for all of them.
The positive count floor is retained throughout; it has not been
replaced by a height-only statistic.

### Distant pairs and the differential inequality

For each nonreal j with y_j=y>0, pair distant exterior zeros at heights
b and -b, sharing their abscissa. If |d|>R, their vertical kernels sum to

    (y-b)/(d^2+(y-b)^2)+(y+b)/(d^2+(y+b)^2)
      =2y(d^2+y^2-b^2)/[(d^2+(y-b)^2)(d^2+(y+b)^2)] >=0,

since |b|<=1<R. The vertical velocity has the opposite sign, so the
height contribution is nonpositive. A real exterior copy has the same
sign individually. Conjugation proves the lower-half-plane case.
The tail is absolutely convergent by (4), since the numerators are
bounded and the denominators grow quadratically. The set |d|>R is
invariant under conjugation, so no omitted partner spoils this step.

For the horizontal reciprocal sum at j, those distant terms with
|x_k|<=2m cost at most N(2m)/R. In the remaining tail |x_k|>2m,
both members of every opposite pair are distant, and

    (1/2)[1/(z_j-z_k)+1/(z_j+z_k)]
        =z_j/(z_j^2-z_k^2),
    |z_j/(z_j^2-z_k^2)|<=4m/(3|x_k|^2),

because |z_j|<=|x_j|+1<=m and |z_k|>=|x_k|>2m.
The average is bounded per zero copy, so using N does not lose a
factor two. In the shell 2^(k+1)m<|x_l|<=2^(k+2)m, (4) gives

    N(2^(k+2)m)<=5*2^k m log(32*2^k m).

Its contribution is at most (5/3)2^(-k)log(32*2^k m).
Summing k>=0 gives (10/3)(log(32m)+log2)<=5log(32m).
The same estimates prove convergence in the prescribed paired order.
The horizontal multiplier in A_j' is bounded by
2|w'_j|Y_j+2|p'_j|<=2.02 A_j/R. Hence all distant horizontal terms
cost at most

    [2.02 N(2m)+10.1 R log(32m)] A_j/R^2.

Sum the finite nearby nonreal pairs by endpoints. Each j has at most
N(m) nearby partners, so their total is at most
sum_j 5N(m)A_j/R^2. By (7) the mixed costs and own-conjugate losses
have nonpositive sum. Thus

    A'<=sum_(y_j != 0) G(x_j)A_j,
    G(x)=20(|x|+R)log(32(|x|+R))/R^2.                       (8)

For completeness the coefficient before R^(-2), after bounding its
logarithms by log(32m), is at most

    [9.04m+140.4+10.1R]log(32m)<=20m log(32m).

Here m>=R>=200 gives 0.86m>=172>140.4. There is no separation
assumption at the edge |d|=R; assigning equality to the nearby case
is legitimate. Exterior real multiplicities cause no differentiation
problem because only the contributing simple zeros are differentiated.

### Collisions, integration, and time zero

Fix tau>0. L488 confines all nonreal or multiple zeros for tau<=t<=T
to a fixed compact rectangle. At a multiple zero z_0 of order m at
time s, the primary Hermite expansion gives, uniformly on compact
zeta sets,

    epsilon^(-m/2) H_(s+epsilon)(z_0+sqrt(epsilon) zeta)
      -> c sum_(k=0)^floor(m/2)
             ((-1)^k m!/(k!(m-2k)!)) zeta^(m-2k), c!=0.     (9)

For H_(s-epsilon) the corresponding formula has (+1)^k in place
of (-1)^k, with the same nonzero leading coefficient c.

The polynomial for s+epsilon has distinct real roots and the one for
s-epsilon has distinct imaginary roots. Rouche on disjoint small
disks around these roots gives exactly one zero, with multiplicity,
per rescaled disk. Rouche on a fixed disk around z_0 says these m
zeros exhaust the local cluster. Thus all are simple at sufficiently
small nonzero one-sided time increments, and the event is isolated
in spacetime.

If z_0 is real, choose the forward disks with real centers. Conjugation
and their unique zeros force every forward zero to be real. The
trace is zero at s and immediately to its right. For s-epsilon, the
nonzero imaginary Hermite roots give nonreal branches, with heights
tending to zero. If m is odd its central disk is invariant under
conjugation and its unique zero is real. The left trace limit is
therefore the number of incoming nonreal copies times p(Re z_0).
This is a downward jump, possibly with other clusters contributing
continuously. At a nonreal collision choose its fixed disk away from
the real axis. All m copies remain nonreal locally, and continuity
of w(x)|y|+p(x) shows continuity of their total. Simple real zeros
stay real locally by uniqueness and conjugation. Simple nonreal
zeros cannot cross the axis without a multiple event.

There are finitely many multiple-zero events in the compact spacetime
rectangle: an infinite sequence would have a convergent subsequence
(s_n,z_n), whose limit satisfies H_s(z)=H_s'(z)=0 by joint continuity.
The isolation just proved excludes that accumulation. For each slice
the zeros in the rectangle are finite because H_t is nonzero entire.
Thus between the finitely many event times the contributing roots
form finitely many smooth branches; their total is differentiable
and (8) applies. Its infinite exterior velocity sums have already
been justified, so no derivative of an uncontrolled infinite trace
is being taken at positive time.

Suppose the core bound is G<=c_0 on |x|<=U and the exterior part
of (8) is at most E, independently of t. Then A'<=c_0 A+E between
events. Integrate by the exponential factor on each interval and
use its one-sided limits, adding no positive jump at any event.
This proves, including interval endpoints,

    A(t)<=exp(c_0(t-tau)) [A(tau)+(t-tau)E], tau<=t<=T.      (10)

It remains to justify tau decreasing to zero. From eta<1 and the strip,

    A_j<=2 exp(-(|x_j|-|a|)/R).

For S>=max(200,|a|) use dyadic shells in |x| beyond S. Bound (4)
gives

    sum_(|x_j|>S) A_j
       <=2 exp(-(S-|a|)/R) N(2S)
              sum_(k>=0) [4 exp(-S/R)]^k,                  (11)

once S is large enough that the ratio is below one. Indeed
N(2^(k+1)S)<=4^k N(2S): both its linear and logarithmic factors
increase by at most 2^k. Also 2^k-1>=k. The right side tends to
zero as S tends to infinity, uniformly for 0<=t<=T.

Choose arbitrarily large S with vertical sides x=+-S free of H_0
zeros, and horizontal sides above and below the strip. These compact
boundaries remain zero-free for sufficiently small nonnegative t by
uniform continuity. Inside, Rouche and disjoint cluster neighborhoods
reduce the trace to finitely many initial zeros with multiplicity.
The preceding forward real splitting makes every initial real
cluster contribute zero for small positive time; nonreal clusters
contribute continuously. Hence the finite interior trace is right
continuous at zero. Combining with (11) proves A(tau)->A(0).
Taking tau down to zero in (10) is therefore justified. No use is
made of L488's divergent confinement radius at zero.

### Exact scalar verification and strict endpoints

All the following inequalities can be proved by elementary rational
comparisons; no floating-point estimate or numerical certificate is
used. The exponential series gives 27/10<e<11/4: for the lower bound
sum through 1/5!=163/60>27/10; for the upper bound the sum through
1/3! is 8/3 and the tail is at most (1/24)sum_(j>=0)4^(-j)=1/18.
Also e^v<=1/(1-v) for 0<=v<1. Thus e^(1.01)<(11/4)(100/99)<3,
as used in (5). Exact integer comparisons give

    (27/10)^4>50, (27/10)^7>1000, (27/10)^8>2800.

For example 27^7=10460353203>1000*10^7 and
27^8=282429536481>2800*10^8. In particular

    e^32>2800^4=61465600000000>6.1*10^13,
    e^34>(6.1*10^13)*7=4.27*10^14,
    e^36>(6.1*10^13)*50>3*10^15,
    e^43>(3*10^15)*1000>3*10^18.                            (12)

Since 32(2U+R)<3.905*10^14<e^34, log(32(U+R))<34 and
log(32(2U+R))<34. Set c_0=680(U+R)/R^2. Then

    T c_0=136(U+R)/R^2<93,

as 136(U+R)=829600408000000<837000000000000=93R^2.
This bounds G throughout the core, including |x|=U.

Also 8U+40<4.9*10^13<e^32, so both S=V and S=U satisfy

    N(2S)<32(2S+20)<=32(2U+20)<5*10^14.                    (13)

There is initially no nonreal zero with |x|<=V. Apply (11) with
S=V and |a|<=X. Since V/R>4 and e^4>50, its geometric ratio is
less than 4/50<1/2. Consequently

    A(0)<2*10^15 exp(-(V-X)/R)<exp(36-(V-X)/R)<exp(-181).    (14)

The last comparison follows from
V-X=652658500>217R=651000000. It is strict even when |a|=X.

For the exterior forcing, (12) also gives

    G(2U)<680(2U+R)/R^2<1000,

because 680(2U+R)=8296002040000000<9000000000000000=1000R^2.
In shell 2^k U<|x|<=2^(k+1)U, the copy count is at most
4^k*(5*10^14) and G(x)<=4^k*1000. The second bound follows by
bounding separately its linear and logarithmic factors by 2^k
times their values at 2U. Thus

    sum_(|x_j|>U) G(x_j) A_j
       <=10^18 exp(-(U-X)/R) sum_(k>=0)[16 exp(-U/R)]^k
       <2*10^18 exp(-(U-X)/R)
       <exp(43-(U-X)/R)<exp(-180).                         (15)

Here U/R>4 and e^4>50 make the ratio less than 16/50<1/2.
The last inequality uses U-X=100652658500>223R=669000000.
These bounds hold at t=0 also, without a finite contributing set.

Take E=exp(-180) in (10), now extended to tau=0. From (14),
0<=t<=T and T c_0<93,

    A(t)<exp(93)[exp(-181)+(1/5)exp(-180)]
        =exp(-88)(1+e/5)<exp(-87),                         (16)

since e>5/4. Finally Q(a)<=V+|a|+R<=2V+R<1.21*10^13.
By (12), log(4Q(a))<32; at x=a, w(a)=e^(-1), hence

    p(a)=eta(a)/e
        >3000000/[4*3*(1.21*10^13)*32]>5*10^(-10).

The denominator times 5*10^(-10) is 2323200<3000000.
Moreover e^87>e^32>6.1*10^13>2*10^9 proves
5*10^(-10)>e^(-87). A nonreal zero at x=a, however small its
nonzero ordinate, would contribute at least p(a), contradicting
(16). Since the proof holds separately for each real |a|<=X with
uniform constants, it excludes every nonreal zero in the closed head.
It covers t=0 and t=T and requires no simultaneous enumeration in a.
The F-coordinate conclusion follows from the nonzero linear change
of variables in L488, which preserves multiplicities.

### Audit decision and limitations

The designated Appendix B audit passes. The count absorption, all
nearby pair types, both tail pairing conventions, collision direction,
compact positive-time finiteness, uniform time-zero tail, and strict
scalar comparisons are paid above. This establishes a usable local
input reproducing the cited manuscript. The count statistic here is
not C028b's reciprocal-Jensen mass, and no identity between them is
asserted. The initial finite-height theorem is not promoted to RH.
L488 remains qualitative at large heights, so a quantitative overlap
covering the exterior, especially uniformly as t decreases to zero,
is unresolved. The mixed-sign gap remains open.

## Mathlib

Full matching coverage of this discontinuous weighted-zero transport
theorem has not been checked. No formalization or absence from Mathlib
is asserted. Jensen, Hadamard, Rouche, analytic implicit-function and
dominated-convergence arguments are used as standard mathematical
inputs here; individual supporting Mathlib declarations were not
looked up because this step is the conceptual source audit.

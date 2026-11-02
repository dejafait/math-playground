# Lemma 583: conditional periodic full-jet truncation and paired moment losses

## Hypotheses

Use L582's specified real C2 periodic function g, with H real on an
eventual ray, ell=log H and P=H ell+1. Its original unit quintic bridge
is fixed. Use L473's coordinate order I={(r,j): r=0,1; j=0,1,2},
reference moments (1) and exactly the tolerances (2). All retained
arithmetic inputs have L473/L582's qualifications, including the
unaudited proof of Bui--Hall Proposition 3. This result does not audit
those inputs or assume RH, simple zeros or positive clipped mass.

Put A=256, lambda=ell^2/A, and, using ordinary derivatives,

    V_g(s)=(g^(j)(s+r))_(r,j),
    a(s)=|g(s)|+|g'(s)|+|g''(s)|,
    M_P a(s)=sup_(rho>0) (2rho)^(-1) integral_(s-rho)^(s+rho) a(t) dt,
    E={s in R/PZ: M_P a(s)>lambda},
    E_pair={s in R/PZ: s in E or s+1 in E}.

The maximal function uses the periodic extension and all positive
radii. Write <f>=P^(-1) integral_0^P f(s) ds. Assume, additionally,
that there are finite B_2,B_4 independent of H such that, on one
eventual ray,

    <1_E_pair (|V_g|^2+lambda^2)> <= B_2,
    <1_E_pair (|V_g|^4+lambda^4)> <= B_4 ell^3.             (1)

These are conditional weighted exceptional-set hypotheses. They are
not asserted consequences of L473's full O(ell^4) fourth norm.

## Conclusion

There exists a real P-periodic h in W^{2,infinity}, with its C1
representative, such that h=g and h'=g' on E's complement K, h''=g''
almost everywhere on K, and

    ||h^(j)||_infinity <=52 lambda, j=0,1,2.                (2)

There also exists a real smooth P-periodic b, obtained by positive
periodic convolution of h, with the same three bounds. Its ordinary
paired jet V_b satisfies, at every phase,

    |V_b| <=52 sqrt(6) lambda <128 lambda=ell^2/2.          (3)

The uniform-phase path X(s)=b(U+s), U uniform on R/PZ, gives a
translation-invariant Borel probability law on C2(R;R). It satisfies
all 147 moment tolerances of L473 (2), with all four exceptional
signed odd second moments exactly zero. In particular, for every
degree-d monomial M in the six coordinates, repetitions allowed,

    |<M(V_b)>-<M(V_g)>|
       <=128^2 B_2+1,                    d=2,
    |<M(V_b)>-<M(V_g)>|
       <=128^4 B_4 ell^3+1,              d=4.              (4)

All constants and final tolerances are uniform on one eventual ray
of real H. The smoothing radius may depend on H; no effective or
uniform positive radius is claimed. The weak truncation h changes
jets only on E, up to a null set for the second derivative. The smooth
b need not agree with g outside E: its extra moment loss is the +1
in (4), proved without a weighted estimate on an enlarged bad set.

This is a conditional specialization of classical truncation,
interpolation and finite-p smoothing. It repairs the hard-support
interface only under (1). Actual-g estimates (1), positive clipping,
realization of L473's particular law, and actual-Xi signs remain
unproved. No novelty beyond the inspected literature is claimed.
The separate critical application audit below passes without changing
the hypotheses, constants or conclusion. Arithmetic-source proofs and
the actual-g exceptional-energy hypotheses remain unaudited inputs.

## Proof

### Source scope and the missing specialization

The classical higher-order truncation comparisons are G. Friesecke,
R. D. James and S. Mueller, *A theorem on geometric rigidity and the
derivation of nonlinear plate theory from three-dimensional elasticity*,
Comm. Pure Appl. Math. 55 (2002), 1461--1506,
[DOI 10.1002/cpa.10048](https://onlinelibrary.wiley.com/doi/10.1002/cpa.10048),
[author PDF](https://dept.aem.umn.edu/~james/research/Publications_Files/PDF/73.pdf),
Proposition A.2(ii), pp.1498--1503, and Christopher Irving, *Partial
regularity for minima of higher-order quasiconvex integrands with
natural Orlicz growth*, version of record 2025,
[DOI 10.1007/s10231-025-01547-2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12259811/),
Proposition 2.10, (2.45)--(2.62). Their prescribed boundary traces,
domain-dependent constants and weak second-derivative conclusions
do not directly supply (2)--(4) on circles of varying length.
Neither is being invoked with those hypotheses removed or reproved.
The following one-dimensional gap construction supplies precisely
the missing period-independent full-jet specialization.

For smoothing, import John K. Hunter, *Notes on Partial Differential
Equations*, revised 18 June 2014,
[author PDF](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
Theorem 1.28 (printed p.12), Theorem 3.19 (p.55), and Theorem 3.24
and its proof (p.59). Only local finite-Lp approximation and weak
derivative commutation are used. The periodic applicability argument
is given below; global whole-line integrability of a nonzero periodic
function and W^{2,infinity} norm convergence are not assumed.

For the weak derivatives and good-set locality, also import Hunter's
Theorems 3.38--3.39 (printed p.71) and 3.52--3.53 (p.77), identifying
one-dimensional Lipschitz derivatives almost everywhere with their
weak derivatives. Import the Lebesgue density theorem as the
characteristic-function case of John K. Hunter, *Measure Theory*,
2011, Theorem 6.10 (printed p.68),
[author PDF](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf).
The application below uses a locally integrable characteristic function
on the line; neither finite measure of the entire periodic good set
nor differentiability at every good point is assumed for this step.

### Good-set data and short gaps

For every fixed rho the average defining M_P a is continuous in s.
Thus E is open and K is closed. Since a is continuous and its centered
averages tend to a as rho tends to zero, at each x in K all three
|g^(j)(x)| are at most lambda. Moreover, for x in K and d>0,

    integral_x^(x+d) |g''(t)| dt <=2d lambda.              (5)

Indeed this integral is bounded by the integral of a on the centered
interval [x-d,x+d]. The estimate uses the actual periodic lift, even
if an interval wraps around the chosen origin.

First suppose K is nonempty and E is nonempty. Each component of the
lift of E is a finite interval (alpha,beta) with endpoints in the
periodic lift of K and length d<=P. The formulas below are invariant
under translating alpha,beta by P, so define a periodic function.
On K set h=g and assign h'=g'. On a gap with d<=1 set t=s-alpha,
v_0=g(alpha), v_1=g(beta), p_0=g'(alpha), p_1=g'(beta), and

    q=(v_1-v_0-p_0 d)/d^2, r=(p_1-p_0)/d,
    h(alpha+t)=v_0+p_0 t+(3q-r)t^2+(r-2q)t^3/d.           (6)

The fundamental theorem of calculus and (5) give

    |r|<=2 lambda,
    |q|<=d^(-2) integral_alpha^beta (beta-u)|g''(u)| du
         <=2 lambda.

Evaluation of (6) and its first derivative at t=0,d gives precisely
(v_0,p_0) and (v_1,p_1). Its quadratic and cubic coefficients have
absolute bounds 8 lambda and 6 lambda/d. Hence, for 0<=t<=d<=1,

    |h|  <=lambda+lambda d+14 lambda d^2 <=16 lambda,
    |h'| <=lambda+34 lambda d <=35 lambda,
    |h''|<=16 lambda+36 lambda t/d <=52 lambda.           (7)

Thus the small denominator in the cubic coefficient loses no
derivative bound. This explicit evaluation is needed for the
constant independent of P; no interpolation existence theorem alone
would give the required estimate.

### Long gaps and all joins

For d>1 put theta(u)=1-3u^2+2u^3 on [0,1]. Then theta(0)=1,
theta(1)=theta'(0)=theta'(1)=0, and

    0<=theta<=1, |theta'|<=3/2, |theta''|<=6.

On 0<=t<=1/2 use h(alpha+t)=(v_0+p_0 t)theta(2t).
On 0<=t<=1/2 at the right endpoint use
h(beta-t)=(v_1-p_1 t)theta(2t). Set h=0 between these two strips.
The strips are disjoint because d>1. They match value and first
derivative at alpha,beta, and both jets vanish at the middle joins.
On either strip, |v_i +/- p_i t|<=3 lambda/2, so product
differentiation gives

    |h|<=3 lambda/2,
    |h'|<=lambda+(3 lambda/2)3=11 lambda/2,
    |h''|<=2 lambda*3+(3 lambda/2)24=42 lambda.           (8)

No value or slope is transported across the long middle interval.
In particular there is no factor d or P in (8).

Here are the gluing details, including infinitely many gaps. Denote
the candidate first derivative by v: it is the ordinary derivative
of each displayed piece and equals g' on K. On each gap it is
52 lambda-Lipschitz, including the internal joins of a long gap.
For x<y in K, (5) gives |g'(y)-g'(x)|<=2 lambda(y-x).
For arbitrary x<y with K intersect [x,y] nonempty, let z be its first
point and w its last. Bound the changes of v on [x,z] and [w,y]
by the gap estimate and the change between z,w by (5). Their sum
is at most 52 lambda(y-x). If that intersection is empty the gap
estimate applies directly. Thus v is globally Lipschitz.

At a point k in K, the assigned function h is differentiable with
derivative g'(k). To verify this for x outside K, choose the endpoint
e of x's gap lying between k and x. On that gap, its derivative
bound gives

    |h(x)-g(e)-g'(e)(x-e)|<=26 lambda |x-e|^2.

For two good points e,k, (5), in either direction, gives

    |g'(e)-g'(k)|<=2 lambda |e-k|,
    |g(e)-g(k)-g'(k)(e-k)|<=2 lambda |e-k|^2.

Combining these three inequalities bounds
|h(x)-g(k)-g'(k)(x-k)| by 30 lambda |x-k|^2. For x in K
the second inequality alone suffices. This proves differentiability
at every k, including accumulation and isolated good points.
Consequently h is C1, h'=v is globally Lipschitz, and h is in
W^{2,infinity}. Bounds (7)--(8) and the good-set bounds prove (2).

The Lipschitz function h'-g' vanishes on K. Its derivative vanishes
almost everywhere on K: at a density point where it is differentiable,
points of K tending to that point force the derivative to be zero.
The Lebesgue density theorem and Rademacher's theorem (in one
dimension) exclude only null sets. Thus h''=g'' almost
everywhere on K, not merely the value/first-derivative agreement.

If E is empty, take h=g; the pointwise good-set bound proves (2).
If K is empty, take h=0; all agreement assertions are vacuous and
(2) holds. This last case is in fact excluded eventually by (1),
since lambda^2<=B_2 would follow, but exclusion is unnecessary for
the construction. These cases also have no periodic trace mismatch.

### Complete paired losses before smoothing

The weak second derivative may be assigned any measurable
representative with its essential bound; all integrals below are
independent of null-set choices. Equation (2) gives
|V_h|<=52 sqrt(6)lambda<128 lambda almost everywhere, since
52^2*6=16224<16384=128^2. Outside E_pair the paired jets of h and g
agree almost everywhere: the exceptional null set and its translate
by -1 still have measure zero.

For a degree-d monomial M, |M(z)|<=|z|^d. Therefore

    |<M(V_h)>-<M(V_g)>|
      <=<1_E_pair (|V_g|^d+128^d lambda^d)>
      <=128^d <1_E_pair (|V_g|^d+lambda^d)>.              (9)

For d=2,4 this is bounded by 128^2 B_2 and
128^4 B_4 ell^3, respectively. This pointwise argument includes
every repeated coordinate and every allocation between lags zero
and one. There is no enlargement of E_pair in (9).

### Positive smoothing and one radius for every moment

Fix H. Let phi be a nonnegative smooth function supported in (-1,1)
with integral one and put phi_epsilon(t)=epsilon^(-1)phi(t/epsilon).
Define

    b_epsilon(s)=integral_R phi_epsilon(t)h(s-t) dt.

The integration has compact support and h is periodic. This is a
real smooth P-periodic function. Hunter's weak-derivative commutation
gives b_epsilon^(j)=phi_epsilon*h^(j), j<=2. Positivity and unit mass
give the bounds (2) at every phase, including for the second
derivative: a continuous convolution of an essentially bounded
function satisfies its supremum bound everywhere.

For fixed H, all three weak derivatives lie locally in L4 on the
line. Apply Hunter's local finite-p approximation on [0,P], using
the larger finite interval [-1,P+1] and epsilon<1. Division by the
fixed P gives

    ||b_epsilon^(j)-h^(j)||_(4,P) ->0, j=0,1,2,
    ||f||_(4,P)=<|f|^4>^(1/4).                            (10)

Equivalently the result follows by finite-L4 translation continuity
on the circle. It does not use global L4 integrability on R or
infinity-norm convergence of h''. Rotation invariance and the
triangle inequality imply

    ||V_b_epsilon-V_h||_(4,P)
       <=2 sum_(j=0)^2 ||b_epsilon^(j)-h^(j)||_(4,P) ->0. (11)

Set B=128 lambda. Both paired norms are at most B. Telescoping any
degree-d monomial factor by factor, with multiplicities counted,
gives

    |M(u)-M(v)|<=d B^(d-1)|u-v| when |u|,|v|<=B.

Choose epsilon=epsilon_H<min(1,P/4) sufficiently small that the
left side of (11) is at most [4 max(1,B)^3]^(-1), possible by
(11). On the normalized probability space, L1 is bounded by L4,
so for both d=2 and d=4 and every monomial of that degree,

    |<M(V_b_epsilon)>-<M(V_h)>|<=1.                       (12)

This single choice controls all 21 second and 126 fourth monomials.
If a specified choice is desired, take the first dyadic epsilon
below min(1,P/4) satisfying (11)'s displayed tolerance. Its existence
does not assert an effective test or a positive lower bound uniform
in H. Equations (9) and (12) prove (4); no estimate on the support
of b_epsilon-h is needed. Put b=b_epsilon_H. Equation (3) follows
from A=256 and the same three convolution bounds.

### All tolerances, exact odd cancellations and the stationary law

L582 supplies <V_g,a V_g,b>-S_ab(H)=O(1) and all
<product V_g,a^m_a>-F_m(H)=O_m(ell^3), with common constants and
onset. Combining these with (4) proves the 17 ordinary second
requirements and all 126 fourth requirements, since ell>=1 on
an eventual ray. The constants in (1), (7)--(12), and L582 are
independent of H. Taking the maximum of their finitely many onsets
gives one ray of real H, without subsequences or endpoint selection.

For the four exceptional second requirements use periodicity, not
the O(1) comparison. At each r=0,1,

    <b(s+r)b'(s+r)>=[b(s)^2]_0^P/(2P)=0,
    <b'(s+r)b''(s+r)>=[b'(s)^2]_0^P/(2P)=0.              (13)

The shift does not change a period integral. These exact zeros
satisfy the required absolute bounds O(H^(-2/3)ell^(-1)) and
O(H^(-2/3)ell^(-3)). No small signed entry has been replaced by
an O(1) error assertion.

Finally the map u -> b(u+.) from the phase circle into C2(R;R)
is continuous in the topology of uniform convergence through order
two on compact sets: each b^(j) is continuous periodic and uniformly
continuous. Its pushforward of normalized circle measure is Borel
and invariant under every real path translation, which corresponds
to a rotation of u. All observables are integrable by (3). The same
bound holds at every phase, hence gives the claimed hard support.
No statement about the sign or lower bound of the clipped observable
(b b''-(b')^2)_+ was used or proved.

### Separate critical application audit, 31 October 2026

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-31-l583-conditional-truncation-audit-scope.md`.
This audit replays the conditional construction for L582's specified g,
not for a replacement bridge. Its inputs remain L582 and L473
(1)--(2),(6),(9)--(10), with the same arithmetic qualifications.
The general truncation theorems are comparisons, not concealed inputs
whose trace or domain hypotheses have been omitted.

**Maximal set and all gap cases.** For each positive radius the
centered average is continuous, so the strict superlevel set E is
open. At a good point k, continuity of a gives a(k)<=lambda. Centering
an interval of radius d at k gives both forward and backward versions
of (5). These statements hold on the actual periodic lift for every
d>0, with no restriction on how many periods an interval crosses.
When K is nonempty, periodicity ensures that every complementary gap
is bounded, has endpoints in K, and has length at most P. This includes
a gap whose two endpoints represent the same point of the circle.
The formulas repeat under translation by P; a chosen fundamental
interval need not have its origin in K. Empty E and empty K are handled
separately as in the proof, without a hidden endpoint requirement.

For a short gap, write a_2=3q-r and a_3=r-2q. The forward integral
bound gives |q|,|r|<=2lambda, so |a_2|<=8lambda and
|a_3|<=6lambda. At t=d the cubic has value
v_0+p_0d+(a_2+a_3)d^2=v_1 and derivative
p_0+(2a_2+3a_3)d=p_0+rd=p_1. Its second derivative is
2a_2+6a_3 t/d. Thus the three upper bounds are respectively
(1+d+14d^2)lambda, (1+34d)lambda, and 52lambda.
They are at most the stated 16lambda, 35lambda and 52lambda
when d<=1. No uncontrolled inverse power of d remains.

For a long gap the two strips of width 1/2 are disjoint. With
theta'(u)=-6u(1-u) and theta''(u)=-6+12u, the displayed bounds
3/2 and 6 hold on [0,1]. Differentiating a strip gives a second
derivative of absolute value at most
4lambda(3/2)+4(3lambda/2)6=42lambda.
The value and first derivative vanish at its inner endpoint.
On the right strip the change of variable t=beta-s reverses the
first-derivative sign, giving the required slope p_1 at beta.
Second derivatives may jump at the inner joins; the claimed output
at this stage is W^{2,infinity} with a C1 representative, not C2.
The exact case d=1 belongs to the short-gap construction.

**Infinitely many gaps and the weak second jet.** The proof of the
global Lipschitz bound for v uses only the first and last good points
in [x,y]. Compactness supplies them whenever that intersection is
nonempty. The two outer segments lie in single closed gaps, while
the good-to-good difference is controlled directly by (5), even if
there are infinitely many intervening gaps. The sum of segment
lengths is y-x, so the constant is still 52lambda. When there is no
good point the interval lies in a single gap. No summation over gap
boundaries or interchange over infinitely many pieces is involved.

For k in K and x in a gap, let e be the intervening endpoint and set
a_0=|x-e|, b_0=|e-k|. The three remainders in the differentiability
argument total at most

    lambda(26a_0^2+2a_0 b_0+2b_0^2)
       <=30lambda(a_0+b_0)^2=30lambda|x-k|^2.

For x in K the good-point remainder suffices. Thus h is differentiable
at every good point, including isolated points and limit points of
gaps, with derivative v(k). Since v is continuous, h is C1 globally.
It is bounded, and its bounded Lipschitz derivative has the bounded
weak derivative supplied by the cited one-dimensional theorems.
Consequently the claimed W^{2,infinity} membership has no singular
boundary contribution.

For fixed H, g' is Lipschitz because g is C2 and periodic; its
Lipschitz constant need not be uniform in H for this argument.
Hence v-g' is Lipschitz and zero on K. Except on a null subset of K,
a point k is a density point of K and a differentiability point of
v-g'. There are distinct k_n in K tending to k, and each difference
quotient ((v-g')(k_n)-(v-g')(k))/(k_n-k) is zero. Its limit proves
(v-g')'(k)=0. Identifying ordinary and weak derivatives gives
h''=g'' almost everywhere on K. The density theorem applies locally
to the periodic set; isolated good points are among the harmless
null exceptions. This verifies the load-bearing second-jet assertion,
not merely value and slope matching.

**Exact modification set and weighted losses.** Choose a measurable
representative of h'' with its essential bound. Outside E_pair the
two weak jets agree, after deleting the null exceptional set and its
translate by -1. Translation preserves null measure on the circle.
Since 6*52^2=16224<16384=128^2, |V_h|<128lambda almost everywhere.
Every degree-d coordinate monomial obeys |M(z)|<=|z|^d, including
repeated coordinates. Integrating its difference only on E_pair
therefore proves (9) with the stated factors 128^d. The assumptions
include lambda^d times the exceptional-set measure, so the cost of
the replacement h is covered as well as the deleted g energy.
No unproved estimate for a larger exceptional set or for its measure
alone has been substituted for (1).

**Normalized smoothing and support.** For fixed H each h^(j), j<=2,
belongs to L4 on every compact interval. To make the local use of
Hunter's finite-p theorem explicit, multiply h^(j) by a smooth cutoff
equal to one on [-1,P+1] and compactly supported in a larger interval.
This is an L4 function on R. Its convolution on [0,P] for epsilon<1
equals the convolution of h^(j). Finite-L4 approximation followed by
division by the fixed P proves (10). Weak derivative commutation is
applied to h locally, so this cutoff argument does not change b or
claim global L4 integrability of the periodic function.

Translations by the two lags preserve the normalized L4 norm.
Pointwise Euclidean norm is bounded by the sum of the six absolute
coordinates, giving (11) by Minkowski. Positive convolution preserves
each of the three bounds 52lambda; in particular the second-derivative bound
holds everywhere for the smooth convolution of an essentially
bounded second derivative.

Put delta=||V_b-V_h||_(4,P) and B=128lambda. The common choice
delta<=[4 max(1,B)^3]^(-1) gives degree-two error at most
B/[2 max(1,B)^3]<=1/2 and degree-four error at most
B^3/max(1,B)^3<=1. This follows from the factor-by-factor telescoping
bound and L1<=L4 on normalized measure, so it controls every monomial
at once, not just finitely sampled representatives. The radius can
depend on H while both error bounds remain absolute. The derivative
bounds give |V_b|<=52sqrt(6)lambda<ell^2/2 at every phase, stronger
than the required ell^2 hard support. No W^{2,infinity} approximation
or support restriction on b-h has been used.

**All 147 tolerances and the law.** There are binomial(7,2)=21
unordered second entries, of which four are the exceptional same-lag
odd pairs, and binomial(9,4)=126 degree-four entries. For each of the
17 ordinary second entries, the comparison with L582 adds at most
128^2 B_2+1 to its uniform O(1) constant. For each fourth entry it
adds at most 128^4 B_4 ell^3+1 to L582's O(ell^3) bound; ell>=1
absorbs the last one uniformly. All mixed lag allocations and
repetitions were included in the monomial estimate.

The other four entries are not certified by those comparison errors.
For each lag, smooth periodicity gives exactly the zero integrals
of (b^2)'/2 and ((b')^2)'/2. These satisfy the two prescribed
absolute power-saving bounds. No equality with the possibly nonzero reference
odd moments is needed or asserted in L473 (2). Combining the finite
source onsets, the two uniform hypotheses (1), and ell>=1 gives one
eventual ray of real H. There is no endpoint selection or subsequence.

The phase-to-path map is continuous in compact-open C2 topology
because b and its first two derivatives are uniformly continuous.
Its circle pushforward is a Borel probability measure, and every real
path shift corresponds to a measure-preserving rotation. The support
bound holds at every phase and is preserved by every shift; all
required observables are integrable. This verifies stationarity and
hard support simultaneously with the moment conditions.

The conditional application audit passes without a mathematical
repair. Its conclusion is a verified sufficient interface, not a proof
of (1) for the actual Hardy segment, a positive clipped-mass estimate,
realization of nu_H, or actual-Xi signs. The original construction and
the scalar-cutoff obstruction are preserved. No arithmetic-source
proof or general truncation-source proof was audited here.

## Mathlib

Full matching Mathlib coverage of this periodic full-jet extension,
its conditional Hardy application and all paired tolerances has not
been checked. No absence claim is made. Supporting mathematical
inputs are elementary polynomial calculus, the fundamental theorem
of calculus, the Lebesgue density theorem, Rademacher's theorem
in one dimension, and Hunter's cited finite-p
mollification results. The arithmetic theorems are retained through
L473/L582 with their existing qualifications. The separate critical
application audit above verifies this specialization without claiming
a formal proof or matching full-library coverage.

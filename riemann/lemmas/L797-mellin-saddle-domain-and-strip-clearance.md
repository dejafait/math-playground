# Lemma 797: the Mellin saddle domain and theta-strip clearance

## Hypotheses

Let c=9/4 and F(z)=z(pi exp(2z)-c). Log denotes the principal
complex logarithm; log denotes the real logarithm. Put

    Omega = {u+ih : u>3, |h|<pi/4},
    D = {s : |s|>=6000, Re(s)>=-|s|/(8 log|s|)}.

The claim under audit is the saddle-domain portion of bramble_trace,
*A continuum certificate for the decreasing Levy factor associated
with Riemann xi*, [paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section3, Lemma2, (10), and its image/clearance
outline following (14). The defining map and constants are taken
from that statement; none of its analytic estimates or supplementary
derivations is assumed.

## Conclusion

F is injective on Omega, has no critical point there, and its open
image contains D. Its holomorphic inverse on F(Omega) therefore
defines one saddle x(s)=u+ih on an open neighborhood of the entire
closed set D. For every s in D,

    F(x(s))=s,   u>3,   pi/4-|h|>1/(4u),
    Re A(s) > (pi exp(2u)-9/2)/u > 0,
    A(s)=2F'(x(s))/x(s).

This is the unique preimage with u>=3 and |h|<=pi/4, and
x(conjugate(s))=conjugate(x(s)). Positive real s have h=0.
The strict inequalities imply the source's stated non-strict
u and clearance bounds, including the boundary |s|=6000 and the
curved left boundary of D.

This reproduces the selected source claim. It does not prove the
source's Mellin relative-error estimate (11), any nonvanishing of
the Mellin transform, its residual/inversion estimates, evaluator
or finite certificates, Levy-density signs, or an actual-Xi
mixed-positivity theorem. L019/L021 explain the actual-kernel
normalization in the source comparison but are not inputs to
this elementary complex-map result.

## Proof

### Scalar bounds and a logarithm of F

The elementary bounds 3<pi<4, e^2>7 and e<11/4 give

    1000 < pi e^6,       e^6 < 450.

For completeness, the exponential series through degree four
at 2 sums to 7, with positive tail. The series at 1 through
degree three sums to 8/3, and its remaining tail is less than
(1/24) sum_{j>=0}5^(-j)=5/96; thus e<87/32<11/4.
Also (11/4)^6=1771561/4096<450 and
pi e^6>3*7^3=1029>1000.

Work first on the closed half-strip

    S = {u+ih : u>=3, |h|<=pi/4}.

Set Q=pi exp(2u), epsilon=c/Q and
w=(c/pi)exp(-2z)=epsilon exp(-2ih). Uniformly on S,

    Q>1000,       |w|=epsilon<1/400.

Both z and 1-w have positive real part. Hence

    G(z)=log(pi)+2z+Log(z)+Log(1-w)

is holomorphic on Omega and on a neighborhood of every point of S,
and exp(G(z))=F(z). In particular F has no zero on S. Write
R=Re G and V=Im G. The logarithm series and the principal argument
of z give

    |Log(1-w)| <= |w|/(1-|w|) < 1/399,
    |V| < pi/2+pi/12+1/399 < pi.                         (1)

Here |arg z|<=arctan(pi/(4u))<=arctan(pi/12)<pi/12.
Consequently V is the principal argument of F throughout S.
Also

    G'(z)=2+1/z+2w/(1-w),
    Re G'(z)>2-2/399>0.                                 (2)

The inequality uses Re(1/z)>0. Finally,

    |F(z)|=Q |z| |1-w|
          > exp(2u) pi u (399/400) > exp(2u),

so that

    R(z)=log|F(z)|>2u.                                  (3)

### Injectivity and absence of critical points

For distinct z_1,z_2 in S their line segment lies in S. Integration
of G' along the segment gives

    (G(z_2)-G(z_1))/(z_2-z_1)
       = integral_0^1 G'(z_1+t(z_2-z_1)) dt.

Its real part is positive by (2), so G is injective on S. If
F(z_1)=F(z_2), then G(z_2)-G(z_1)=2 pi i k for an integer k.
By (1) its imaginary part has absolute value strictly less than
2 pi; hence k=0, and z_1=z_2. This proves injectivity of F on S,
and in particular on Omega. Since F'=F G', (2) and F!=0 show
that F' never vanishes on S.

### The curved clearance boundary lies beyond the target angle

For u>=3 put

    H(u)=pi/4-1/(4u),       2/3 < H(u) < 1.

Consider any z=u+ih in S with h>=H(u). For 0<=h<=pi/4,
the number 1-w=1-epsilon cos(2h)+i epsilon sin(2h) has positive
real part and nonnegative imaginary part. Thus

    V(z) = 2h+arctan(h/u)+arg(1-w)
         >= 2H(u)+arctan(H(u)/u).

The inequality arctan t>=t-t^3/3 for t>=0 follows by integrating
1/(1+t^2)>=1-t^2. Using 2/3<H(u)<1 and u>=3 gives

    V(z) > pi/2-1/(2u)+2/(3u)-1/(3u^3)
         >= pi/2+7/(54u).                               (4)

For any r=|F(z)|, (3) gives log r>2u>=6. Define

    beta(r)=pi/2+arcsin(1/(8 log r)).

Since arcsin t<=2t for 0<=t<=1/2 (integrate its derivative,
which is <=2 there), (3) implies

    beta(r) < pi/2+1/(8u).

Together with (4),

    V(z)-beta(|F(z)|) > 1/(216u) > 0
               whenever H(u)<=h<=pi/4.                 (5)

No saddle or inverse is assumed in this calculation. It controls
the whole indicated portion of the half-strip, not a sampled
boundary. For an upper-half-plane point s of modulus r>=6000,
the defining real-part inequality of D is precisely
arg(s)<=beta(r), because cosine is decreasing on [0,pi].

### Global image coverage at each fixed modulus

First the entire starting boundary u=3 lies strictly below the
required modulus. For |h|<=pi/4<1,

    |3+ih| < sqrt(10) < 13/4,
    |F(3+ih)| <= |3+ih|(pi e^6+c)
              < (13/4)(1800+3) < 5860 < 6000.           (6)

Fix r>=6000. For every h in [0,pi/4], the real function
u -> R(u+ih) is strictly increasing by (2), starts below log r
at u=3 by (6), and tends to infinity by (3). The intermediate
value theorem therefore gives exactly one u=u_r(h)>3 with

    R(u_r(h)+ih)=log r.

The real implicit function theorem, using R_u=Re G'>0,
shows that u_r is continuously differentiable, with one-sided
endpoint derivatives. This also gives continuity on the entire
closed interval: the unique local solutions agree on overlaps.
Define

    v_r(h)=V(u_r(h)+ih).

The Cauchy-Riemann equations give

    u_r'(h)=Im G'/Re G',
    v_r'(h)=|G'|^2/Re G'>0,                             (7)

with derivatives evaluated at u_r(h)+ih. At h=0 all logarithms
in G are real, so v_r(0)=0. At h=pi/4, (5) applies and yields

    v_r(pi/4)>beta(r).

Every target argument in [0,beta(r)] is consequently attained
exactly once, with 0<=h<pi/4. Since exp G=F, this constructs
the desired preimage for every s in D in the closed upper half
plane, including all endpoint radii and angles. Conjugation
constructs the lower-half-plane preimages; F has real
coefficients in its power series and respects conjugation.
The real case h=0 is common to the two constructions.

If a constructed upper preimage had h>=H(u), (5) would give
arg(s)>beta(|s|), contradicting s in D. Hence h<H(u).
Conjugation gives |h|<H(u) in the lower half as well. This
proves the claimed strict clearance and places every preimage
in Omega. Injectivity on S proves uniqueness even if its
boundary were allowed.

### Holomorphy and curvature

The holomorphic inverse function theorem applies at every point
of Omega because F'!=0. Its local inverses agree by injectivity,
and therefore give a single holomorphic inverse on the open set
F(Omega). The preceding construction proves D is a subset of
that open set. Thus holomorphy holds on an open neighborhood
of D, with no ambiguity about holomorphy on a closed domain
and no separate assumption of a branch at infinity. Uniqueness
also proves the stated conjugation property of x.

For z=x(s)=u+ih, direct differentiation gives

    A/2 = Q exp(2ih)(2+1/z)-c/z.

Put v=u^2+h^2. Taking real parts yields

    Re(A)/2
      = Q[(2+u/v)cos(2h)+(h/v)sin(2h)]-c u/v.           (8)

The middle signed product h sin(2h) is nonnegative. By the
strict clearance, and since 0<1/(2u)<=1/6,

    cos(2h)>sin(1/(2u))>=1/(4u).

The last elementary sine bound follows, for example, by
integrating cos t>=1-t^2/2 on [0,1/6]. Also u/v<=1/u.
Thus (8) gives

    Re(A)/2 > Q/(2u)-c/u,
    Re(A) > (Q-2c)/u = (Q-9/2)/u > 0.

This proves the selected curvature assertion. All steps are
uniform over D and require no numerical truncation, Mellin
integral manipulation, supplementary certificate or assumption
about zeta zeros.

### Independent conceptual audit, 5 November 2026 — step510

Reused the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-actual-mellin-saddle-domain-audit.md`.
The proof above passes the following independent analytic checks. This
removes its pending critical-review qualification for the stated map
claim only; it is local verification of a source reproduction, not a
new theorem beyond that source. No mathematical correction is needed.

**Logarithm and global uniqueness.** On the entire closed strip S,
Re(z)>0 and Re(1-w)>=1-|w|>399/400. Thus the two principal logarithms
exist on a neighborhood of every segment used in the proof. The
logarithm-series bound is applicable there, and
|Im G|<7pi/12+1/399<pi. Also
Re G'>2-2/399=796/399>0. Integration along a segment proves injectivity
of G without an assumption about F's image. Equality of two F values
then gives a logarithmic difference 2pi i k; the strict imaginary range
forces k=0. F'=F G' is nonzero, including on the boundary of S. This
checks the exponential-period issue and excludes unproved branch or
critical-point assumptions.

**Actual/required boundary comparisons.** The exponential-series tail
used above has successive ratios at most 1/5 after its first term,
with a strict inequality subsequently. Hence its strict upper bound,
Q>1000 and |w|<1/400 are valid. At u=3 the stated modulus bound is
strictly less than (13/4)*1803=23439/4=5859.75<5860<6000, uniformly
in h. The opposite comparison is |F(u+ih)|>exp(2u), since
pi u(399/400)>1. Thus R>2u and every fixed-radius solution satisfies
3<u<(log r)/2; no endpoint can be lost by escape to infinity.

For H(u)=pi/4-1/(4u), the estimates 2/3<H(u)<1 give the lower angular
excess

    V-pi/2 > 1/(6u)-1/(3u^3) >= 7/(54u).

The target excess is at most 1/(4 log r)<1/(8u), because
1/(8 log r)<1/48<1/2 lies in the stated arcsine estimate's range.
The resulting margin is strictly greater than
(7/54-1/8)/u=1/(216u)>0. These are uniform inequalities on the whole
forbidden-clearance region h>=H(u), not evaluations at a proposed
saddle. The margin may tend to zero as u grows; no fixed positive
uniform angular margin is claimed or used.

**Existence and all closed-domain cases.** R_u=Re G'>0, the starting
modulus bound and R>2u justify existence and uniqueness of u_r(h)
for every h in the closed interval [0,pi/4] and every r>=6000.
The implicit function theorem applies at its endpoints as well,
because u_r(h)>3 and G extends across the strip boundary locally.
The Cauchy-Riemann equations give R_h=-Im G', V_u=Im G',
V_h=Re G', so that the sign and denominator in (7) are correct.
It follows that v_r rises continuously from zero to a value strictly
above beta(r). This covers both r=6000 and arg(s)=beta(r); no target
point is obtained merely as a boundary limit. Negative real s are
excluded from D since 1/(8 log r)<1. Positive real s use h=0;
conjugation covers the lower half and the two constructions agree on
the positive real axis by injectivity. The forbidden-region margin
puts every constructed inverse strictly inside Omega.

**Holomorphy and curvature.** The nonvanishing of F' and injectivity
make the local holomorphic inverses agree on the open image F(Omega).
Since every point of D belongs to that image, it is an open neighborhood
of the closed, unbounded D. The proof asserts no fixed neighborhood
width. Recomputing 1/z=(u-ih)/(u^2+h^2) gives exactly (8), including
the positive sign of h sin(2h) and the factor A/2. Clearance implies
cos(2h)>sin(1/(2u))>=1/(4u); the sine bound follows from
sin t>=t-t^3/6>=t/2 for 0<=t<=1/6. Dropping the nonnegative terms
and using u/(u^2+h^2)<=1/u yields Re A>(Q-9/2)/u>0 as stated.

No numerical check, new source theorem or local mathematical input is
needed for these checks. The empty L797 DAG row remains correct.
The source's separate Mellin remainder, inversion, nonvanishing,
certificate provenance and sign claims remain unverified here.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
The proof uses the standard holomorphic inverse function theorem,
the real implicit function theorem, the Cauchy-Riemann equations,
and elementary logarithm/trigonometric estimates. No specific
Mathlib theorem name or formal verification is asserted.

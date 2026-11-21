# Corollary 997o: a fixed classical Laguerre lens for the theta=1 contour

## Hypotheses

Use Q(x)=x, alpha=2 and degree N=n+1, with integer n tending to
infinity. Use C997e's phases, real branches on J=[15/8,17/8], and
its audited exact normalization (4),(15)-(16). Define

    delta=1/8, beta=1/8+i,
    s_*=delta^2*beta/(1+sqrt(1+delta^2*beta^2)), y_*=Im(s_*),
    K={c:15/8<=Re(c)<=17/8, 0<=Im(c)<=y_*},
    U={c:29/16<Re(c)<35/16, |Im(c)|<1/32},
    V={w:7/16<=Re(w)<=9/16, |Im(w)|<=1/64}.

The square root defining s_* has positive real part. All u below are
real and belong to [0,2]. Parameters and contours are fixed before n.
K includes the nominated horizontal segment, both vertical sides and
the enclosed rectangle. This is a domain result, not a response estimate.

## Conclusion

There is a fixed lens with source-compatible Airy/Bessel endpoint pieces,
central lips at heights +/-1/32, and positive phase margin on its
compact outer lips. Its reduced contour Gamma has distance at least
1/64 from V. For its exact residual matrix R_N,

    R_N is holomorphic on a neighborhood of V, including across (0,1),
    sup_V ||R_N-Id||=O(1/N).                                  (1)

In fact the estimate holds on the larger closed rectangle

    Wbar={w:3/8<=Re(w)<=5/8, |Im(w)|<=3/128}.

Moreover 0<y_*<1/112, K is contained in U with distance greater than
1/64 from its boundary, and for every n>=63,

    w=c*(n+u)/(4*(n+1)), c in closure(U), u in [0,2],
    dist(w,boundary(V))>=29/4096>1/256, w in interior(V).       (2)

For all sufficiently large n, C997e(15)-(16), with this R_N, give
exact holomorphic amplitudes on a neighborhood of closure(U).
C997e(4)'s O(1/n) amplitude limits hold uniformly there for u in [0,2].
In particular the entire fixed deformation K is covered. The asymptotic
onset and constants are existential; n>=63 only certifies (2), not the
onset of (1). No amplitude nonvanishing, packet lower bound, correction
comparison, actual-Xi sign or RH conclusion is asserted.

Step352, 11 November 2026: RESEARCH / REPRODUCTION under the prior
SPECIALIZE assessment review351. Local ADVANCE supplies the previously
missing quantitative domain. This specializes known Riemann-Hilbert
tools; it is not a claim of new mathematics beyond the checked sources.
The step355 conceptual audit below accepts this domain conclusion,
with the matrix-norm convention and boundary-class justification made
explicit. No effective asymptotic onset is added.

## Proof

### Source contract and extent of the specialization

Import M. Vanlessen, *Strong asymptotics of Laguerre-type orthogonal
polynomials and applications in random matrix theory*,
[arXiv:math/0504604v2, 29 August 2005](https://arxiv.org/pdf/math/0504604v2),
Remarks 2.3/3.11/3.15, (3.39)-(3.47),(3.51)-(3.53), Propositions
3.19/3.25, the matching formulas (3.76),(3.98), Section 3.8,
Proposition 3.31, (3.105)-(3.110), and Proposition 5.1/(5.5)-(5.6).
The relevant printed pages are 5-7,18-24,28-34,39. The source allows
alpha>-1; alpha=2 qualifies. Its monomial formulas give beta_N=4N,
h_N=4 and phases independent of N. Its local parametrices, matching
estimates and exact reconstruction are imported. The argument below
verifies the changed outer geometry and its error estimate; it does
not assume Theorem 3.32 already covers an arbitrarily enlarged lens.
C997e supplies the audited scalar normalization without reproof.

### Phase sign and explicit outer lips

Write xi for the source phase, with its own upper and lower branches.
For 0<x<1 in the upper half-plane, (3.39),(3.41) give

    xi'(w)=-2i sqrt((1-w)/w),
    Re xi(x+iy)=2 integral_0^y Re sqrt((1-x-it)/(x+it))dt.     (3)

Here the square root extends the positive value at t=0. Indeed the
ratio is 1/(x+it)-1, whose imaginary part is -t/(x^2+t^2)<0
for t>0. It avoids the square-root cut and its principal square root
has positive real part. Since Re xi(x+i0)=0, (3) proves
Re xi(x+iy)>0 for every y>0. The source lower phase is the complex
conjugate of the upper phase at reflected points, so it has the same
positive real part. This sign statement concerns the source's two
branches, not a single continuation of xi across the real interval.

Choose once and for all

    0<d<min(delta_1,delta_2,delta_3,1/64),
    nu=3*pi/4, a=d/sqrt(2), H=1/32,

where the three positive source radii are those in Section 3.8.
Keep precisely its inverse Airy/Bessel rays inside the disks of radius
d about 1 and 0. Section 3.8 and Propositions 3.19/3.25 put their upper
exit points at 1-a+ia and a+ia respectively; lower exits are reflected.
For Q=x the conformal maps before multiplication by N^(2/3) and N^2
are fixed, so these inverse rays and their matching angles are fixed.
All source sector and matching hypotheses at the endpoints are retained.

Outside those disks take the upper lip to be the graph of

    h(x)=a+(H-a)*(x-a)/(1/4-a),        a<=x<=1/4,
         H,                          1/4<=x<=3/4,
         h(1-x),                     3/4<=x<=1-a.           (4)

Use its conjugate below. This simple piecewise linear graph joins the
specified exits. On the left piece both coordinates increase from the
exit, hence it stays outside the disk at 0; reflection proves the
corresponding assertion at 1. The other disk is farther away. The
central piece avoids both. The slope on the left is strictly between
0 and 1; all joins with the endpoint circles are transverse. Corners
at 1/4 and 3/4 cause no difficulty in the contour estimates below.

For every outer-lip point x+iy, with y=h(x),

    a<=x<=1-a, a<=y<=H, y<=min(x,1-x).

If 0<=t<=y, then t^2<=x*(1-x)/3. For x<=1/4 this follows from
t<=x and x/(1-x)<=1/3; for x>=3/4 reflect; in the middle use
t^2<=1/1024 and x*(1-x)>=3/16. Consequently

    Re((1-x-it)/(x+it))
       =(x*(1-x)-t^2)/(x^2+t^2)
       >=(1-x)/(3*x)>=a/3.

For any complex r with Re r>0, Re sqrt(r)>=sqrt(Re r).
Equation (3) now gives the uniform outer-lip margin

    Re xi(x+iy)>=2*a*sqrt(a/3)=:m_d>0.                      (5)

On the central horizontal part a sharper, radius-independent bound
is available: for 1/4<=x<=3/4 and 0<=t<=1/32, the same real ratio
is at least 191/577>1/4. Thus Re xi(x+i/32)>=1/32.
There is no claim of a uniform positive margin all the way to the
endpoints 0 and 1; their neighborhoods are handled by the parametrices.

Let Gamma consist of both outer lips, both endpoint circles and the
unchanged ray [1+d,infinity), as in (3.101). The central lips are at
distance at least 1/128 from Wbar. Every noncentral lip has real part
at most 1/4 or at least 3/4; the circles and ray are farther away.
Hence dist(Wbar,Gamma)>=1/128, and dist(V,Gamma)>=1/64.
Wbar lies inside the lens outside both disks.

### Error control for the changed contour

Make exactly the transformations (3.52),(3.100) using (4). The
factorization (3.51) is algebraic, so all jumps remain (3.53),(3.105).
In particular the jump on the real bulk interval cancels against the
global parametrix P=P^(infinity). Endpoint cancellation and removability
are unchanged from Proposition 3.31. The actual R_N is therefore
holomorphic off Gamma, including through the real part of Wbar.

Here are the constants needed to apply the source's small-norm proof
to this specific Gamma. Use the Euclidean operator matrix norm, so
||E_12||=||E_21||=1, and arclength Lp norms of that matrix norm.
On the two outer lips define the finite number

    M_d=sup ||P(w)||*||P(w)^(-1)||,

and let L_d be their total length. Finiteness follows from the explicit
global parametrix away from 0,1 and from det P=1. With Delta_N=v_R-Id,
(3.53),(3.105),(5) give

    ||Delta_N||_(Lp,lips)
      <=M_d*a^(-2)*max(1,L_d)*exp(-2*N*m_d), p=1,2,infinity. (6)

The two circle matching bounds (3.76),(3.98) give C_d/N for each
of these three norms, for one fixed finite C_d and all large N.
They use the same d and endpoint angles as the source and do not
depend on the height of the outer lips.

For completeness the unbounded part is also charged. Since h_N=4,
one may use h_0=2 in (3.46). For x>=1+d,

    xi(x)<=-k_d*x, k_d=(2/3)*(d/(1+d))^(3/2)>0.

P and its inverse are bounded on this ray, including infinity.
Its jump is conjugate to Id+x^2*exp(2*N*xi(x))*E_12.
For N>=1, x^2*exp(-2*N*k_d*x) is at most
exp(-N*k_d*(1+d))*x^2*exp(-k_d*x). The latter function has finite
L1,L2 and Linfinity norms. Thus one finite T_d bounds each ray norm
by T_d*exp(-N*k_d*(1+d)). In particular, setting

    eta_N=C_d/N+M_d*a^(-2)*max(1,L_d)*exp(-2*N*m_d)
                    +T_d*exp(-N*k_d*(1+d)),

we have ||Delta_N||_1,||Delta_N||_2,||Delta_N||_infinity<=eta_N=O(1/N).
All constants are fixed, positive where needed, independent of N,u,c.

The boundary Cauchy operator C_- on this Gamma has a finite L2 norm
K_d. One can check this without a contour uniformity assumption:
subdivide the circles and straight pieces at their finitely many joins.
On individual straight pieces/rays and circles, boundedness is the
standard L2 Hilbert transform or circle Cauchy projection theorem.
Separated compact pieces give bounded integral kernels; interactions
with the distant ray have square-integrable kernels. At a shared
endpoint, distinct tangent rays meet at a positive angle, so the
cross-kernel is bounded by a constant times 1/(s+t) in arclength
coordinates. The weighted Schur test with weight t^(-1/2) bounds it,
using integral_0^infinity t^(-1/2)/(s+t)dt=pi*s^(-1/2).
The joins in (4), the circle exits and the ray-circle intersection all
have this property. The finitely many pieces therefore give K_d<infinity.

First establish the boundary equation for the ACTUAL residual, without
assuming an O(1/N) bound. Fix N. On the compact pieces of Gamma its
one-sided sectorial values are bounded, including at the finitely many
junctions: the original T, the triangular factors, the global/local
parametrices and their inverses have finite sectorial limits there,
and none of these junctions is 0 or 1. The determinants of the
parametrices are one. The singularities at 0 and 1 have already been
removed by the unchanged source argument. The O(1/w) normalization
at infinity is inherited from S and P, independently of small-norm
estimates. In particular it holds for both boundary values on the ray.
One may use the original source residual here: outside a fixed compact
set the changed and original lenses have identical definitions, so
their residuals agree, and its RH condition (c) applies. These are
fixed-N bounds; their constants need not be uniform in N.

It follows that v_N=R_(N,-)-Id belongs to L2(Gamma): compact pieces
have finite length and the ray tail is O(1/x). Also

    g_N=R_(N,-)*Delta_N=Delta_N+v_N*Delta_N belongs to L1 and L2,
    ||v_N*Delta_N||_1<=||v_N||_2*||Delta_N||_2,
    ||v_N*Delta_N||_2<=||v_N||_2*||Delta_N||_infinity.

Apply Cauchy's theorem to R_N-Id in each complementary region, cut
off by a large circle and with small circles removed at all junctions.
The compact-arc traces are piecewise regular. Bounded sectorial
values make the small-circle integrals tend to zero. The outer
integral tends to zero by R_N-Id=O(1/w); the integrable jump g_N
controls the ray tail. Summing the region boundaries, with the
source's orientations, gives the additive representation

    R_N=Id+C(g_N).

The L2 Plemelj formula on the smooth open pieces (junctions have
arclength measure zero) then gives

    v_N=C_-Delta_N+C_-(v_N*Delta_N).

For large N choose K_d*eta_N<=1/2. The source's (3.108)-(3.109)
Neumann argument, now with a justified L2 equation, gives

    mu_N=(Id-C_(Delta_N))^(-1) C_-Delta_N,
    C_(Delta_N)f=C_-(f*Delta_N),
    ||mu_N||_2<=2*K_d*eta_N,
    R_N=Id+C(Delta_N+mu_N*Delta_N).                         (7)

Uniqueness in L2 identifies mu_N=v_N. Thus (7) is the representation
of the actual matrix, not merely of a constructed formal solution.

For w in Wbar the distance estimate and Cauchy-Schwarz in (7) give

    ||R_N(w)-Id||
       <=(64/pi)*(eta_N+2*K_d*eta_N^2)=O(1/N).              (8)

The identical estimate holds in an open neighborhood with slightly
smaller positive clearance. This proves (1). Cauchy derivative
estimates on smaller compact rectangles are consequently available.
No real-axis O symbol has been analytically continued.

### Fixed contour, scaled arguments and exact amplitudes

Put v=delta^2*beta^2=(-63+16i)/4096 and r=sqrt(1+v)=p+iq.
Then |v|=65/4096<1/32, p>sqrt(31/32)>31/32, and
q=1/(512*p)>0. It follows that

    |s_*|< (9/512)/(63/32)=1/112.

Indeed |delta^2*beta|=sqrt(65)/512<9/512 and |1+r|>63/32.
Also Im(beta/(1+r))=(1+p-q/8)/|1+r|^2>0, since q<1/496.
Thus 0<y_*<1/112. The horizontal clearance of K in U is 1/16
and the vertical clearance is greater than 1/32-1/112=5/224>1/64.

For N=n+1>=64 put t=(n+u)/N. Then 1-1/N<=t<=1+1/N.
For c in closure(U) this yields

    Re(w)>=29/64-29/4096=7/16+35/4096,
    Re(w)<=35/64+35/4096=9/16-29/4096,
    |Im(w)|<=65/8192=1/64-63/8192.

These inequalities prove (2), for all u including both endpoints.
All maps and estimates have room to extend to an open neighborhood
of closure(U). The unscaled argument c and s=c*(n+u)/N remain in
fixed simply connected rectangles avoiding 0 and 4. The branches of
theta, phi, q and fractional powers extend uniquely from their stated
real values, so they agree with C997e on J.

Inside the upper part of the enlarged lens, Proposition 5.1's exact
reconstruction is still obtained from the same transformations.
Substitution of P gives (5.6), hence C997e(15)-(16) with this R_N.
Every term in these formulas is holomorphic in c on the connected U:
R_N is holomorphic even across the real interval by the cancelled jump,
and the remaining factors use the local branches just specified.
Equality on the upper part therefore extends across the entire U by
the identity theorem. On the common neighborhood of J in any narrower
admissible lens the residual matrices agree, since their definitions
use the same T and P; this is an extension of the audited normalization.

Finally s-c=c*(u-1)/N=O(1/N) uniformly on the fixed rectangles.
Bounded holomorphic Taylor remainders and (8), together with C997e's
scalar kappa_N=1+O(1/N), give its (4) from the exact (16), uniformly
on a neighborhood of closure(U) and uniformly for u in [0,2].
Both exponential branches are retained. This proves the claimed
domain and uniformity without evaluating a packet integral.

### Independent conceptual audit — step355, 11 November 2026

RESEARCH / REPRODUCTION under the prior SPECIALIZE review353, exactly
its saved audit target. The conclusion (1)-(2) and the two-amplitude
domain are accepted. The audit fixes an underspecified norm convention
and supplies the boundary-class step preceding (7); it does not add
a packet estimate, a new asymptotic theorem or a stronger domain.
The original text permitted a generic submultiplicative matrix norm
in (6), without charging ||E_21||. Choosing the Euclidean operator
norm above makes the displayed constant valid. Other matrix norms
give the same O(1/N) conclusion by finite-dimensional norm equivalence,
but their numerical constants must be changed as appropriate.

**Source and endpoint compatibility.** The primary source above was
checked at (3.39)-(3.47), (3.52)-(3.53), both complete matching
statements (3.75)-(3.76)/(3.97)-(3.98), Section 3.8 including the
alpha>0 case of Proposition 3.31, and Proposition 5.1/(5.5)-(5.6).
Section 3.8's exits are 1+d*exp(i*nu) and -d*exp(-i*nu), giving
1-a+ia and a+ia when nu=3*pi/4. The reflected exits agree as well.
Q=x makes the unscaled conformal maps independent of N; multiplication
by a positive power of N changes neither their inverse rays nor their
angles. The Airy angle remains in a compact subset of (pi/3,pi), and
the Bessel angle in a compact subset of (0,pi), as required by the two
matching statements. The parametrices are used only inside radius d
and in their boundary sectors. Altering an outer lip beyond that circle
does not alter either inner problem or its matching value. At alpha=2,
the source removes the zero-endpoint singularity using its polynomial
growth in all sectors and boundedness outside the lens; boundedness
in an exterior sector alone would not suffice.

**Signs, geometry and the boundary operator.** Equation (3) uses the
upper branch; conjugation, rather than its continuation across (0,1),
supplies the lower branch. On the outer graph y<=min(x,1-x), hence
t^2<=x^2 as well as t^2<=x*(1-x)/3. The numerator is at least
2*x*(1-x)/3 and the denominator at most 2*x^2, which verifies the
lower bound (1-x)/(3*x) and (5). On the central part the separate
numerator and denominator bounds are 191/1024 and 577/1024.

At a left circle exit the circle tangent has slope -1 and the lip
slope lies in (0,1); at the right exit the reflected slopes are again
different. At 1+d the circle is vertical and the ray horizontal.
Artificial subdivisions of a smooth circle have opposite outgoing
tangents. At the polygonal corners the outgoing tangent directions
are also distinct. Thus, for any two incident pieces, their arclength
parameters s,t from the join satisfy |z(s)-w(t)|>=c*(s+t) locally
for some c>0. For curved circle arcs this follows from the first-order
tangent expansion, absorbing the O(s^2+t^2) remainder on a small
neighborhood. The Schur integral displayed above bounds every such
cross-operator. The same-piece circle/line operators are restrictions
of the standard L2 Cauchy projections, and all remaining interactions
are separated or have a square-integrable ray tail. This pays K_d
without assuming a global Carleson jump-contour decomposition.

The proof before (7) now explicitly establishes the actual boundary
class before inversion. This avoids assuming the desired closeness
in order to obtain its own integral equation. With clearance 1/128,
the Cauchy kernel contributes at most 128/(2*pi)=64/pi; Holder gives
||mu_N*Delta_N||_1<=2*K_d*eta_N^2, exactly (8). The 1/64 clearance
for V and 1/128 clearance for Wbar both hold: the central horizontal
pieces are nearest, while every sloping piece has real part outside
[1/4,3/4] and the endpoint circles and ray are farther away.

**Scaled arguments and continuation.** The three margins from the
image of closure(U) to the sides of V are at least 35/4096,
29/4096 and 63/8192, respectively, for N>=64. Their minimum is
29/4096>1/256. They are uniform in u, so one fixed enlargement of U
is still mapped into interior(V). Also |delta^2*beta^2|=65/4096<1/32;
writing its shifted square root as p+iq gives p>31/32 and
q=1/(512*p)<1/496. These verify 0<y_*<1/112 and the claimed
clearance of K, including its vertical sides.

On that fixed enlargement both c and s=c*(n+u)/N stay in simply
connected rectangles away from 0 and 4. Their local branches are
therefore the continuations of C997e's real branches. Exact upper-lens
reconstruction and the cancelled real jump make both sides of (15)
holomorphic there, so the identity theorem applies. Formula (16)
defines each amplitude separately on the same domain. Bounded Taylor
remainders give N*phi(s)-n*phi(c)=theta(c)+c*u*q(c)+O(1/n)
uniformly, while R_11=1+O(1/N) and R_12=O(1/N). This establishes both
limits in C997e(4) without continuing a real-axis remainder or discarding
one exponential. Constants and onset remain existential. The integer
n>=63 is only the geometric inclusion threshold. C997n's correction
bound, data nonvanishing and a complete data lower rate remain separate
unaudited or unproved obligations; none is an input to this corollary.

## Mathlib

Full matching coverage for this fixed-lens specialization and its
Riemann-Hilbert error-matrix input has not been checked and is unknown.
Standard Cauchy/identity theorems, Hilbert-transform boundedness and
Neumann-series arguments support the informal proof; no Lean
verification or absence claim is made.

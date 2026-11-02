# Corollary 645t: a full-response obstruction for outer-half grid cancellation

## Hypotheses

Let m>=5 be odd, n=3m, d=5/4, x=-d, R=11/8, U=R^2,
eta=1/100 and t_j=j/n for 0<=j<n. Put r=27/50 and take the
distinct poles

    a_k=x+i*r*cos((2k-1)*pi/(2m)),  1<=k<=m,

with original simple-pole residues all equal to one. The pole set is
the same at every angle. For u=i*exp(i*theta), |u|=1, set

    b_t(v;u)=R*(v-t*u)/(U-t*conjugate(u)*v),
    B_u(v)=product_(j=0)^(n-1) b_(t_j)(v;u),
    q_u(zeta)=sum_k [B_u(x)/(R*B_u(a_k))]/(zeta-a_k/R).

Use C645g's normalized circle measure, H^2 with nonnegative Fourier
modes, H^2_- with strictly negative modes, and H_q f=P_-(q*f).
Operator norms mean largest norms. Put L=(n-1)/2, K=L+1=ceil(n/2),
and define

    B_low,u(v)=product_(j=0)^L b_(t_j)(v;u),
    B_out,u(v)=product_(j=L+1)^(n-1) b_(t_j)(v;u),
    f_u(zeta)=B_out,u(R*zeta),
    J_n=(mean_theta ||H_q_u f_u||_2^2)^(1/2),
    A_n=(mean_theta ||H_q_u||^2)^(1/2).

No Xi realization, zero selection, separation assumption, independent
upper bound, or sign assertion is made. This is a subfamily allowed
by the saved common-pole angular target, with M=m=n/3.

## Conclusion

The family has Re(a_k)=x, contains x, satisfies |a_k|<=R-eta,
and avoids every rotated grid. The nominated input has ||f_u||_2=1.
Its complete output, not merely selected coefficients, satisfies

    sup_(|u|=1, |zeta|=1) |H_q_u f_u(zeta)|
        <=22000*m*exp(-7*n/200),                           (1)
    J_n <=22000*m*exp(-7*n/200),
    exp(n/32)*J_n <=22000*m*exp(-3*n/800) -> 0.             (2)

Thus the outer-half inner input cannot supply a uniform positive
c*exp(-n/32) response bound for the approved family. Since A_n>=J_n,
(1)--(2) are not upper bounds on A_n. The full angular detector,
other Hardy inputs and the actual-Xi positivity/sign gaps remain open.

This is a local quantitative method obstruction, independently audited
on 2 November 2026 without a mathematical correction. The
standard projection and contour identities are reused; the checked
sources do not supply this evaluated rate. No certified originality,
progress beyond all literature, or RH resolution is asserted.

## Proof

### Source scope and why the specialization is needed

The invocation-start
[angular EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers this exact family, threshold, finite analytic-input test and
Fourier/residue/contour mechanism. Its primary comparisons are reused.
C645g supplies the spaces and scaling. C645n supplies its finite
analytic-input projection identity and the angular product bound
|B_u(x)|<=exp(-lambda*n), lambda>47/1000. C645l supplies the
Chebyshev finite-node identity and the left-arc contour argument;
the changed radius and ellipse are justified below. Its fixed-angle
Hankel upper bound is not used. C645o's signed Gram and C645p's
continued-value cost are contrasts only.

The projection convention is L. Baratchart, S. Chevillard and T. Qian,
*Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47, preprint v2, 24 March 2015,
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Import the residue theorem, simple-pole rule and contour inequality
from R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
front matter updated 22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html),
as inspected in the reused assessments. These general theorems need
no reproof. The bounds below evaluate the new partial-cancellation
response and finite-node error; the full-cancellation exponent does
not decide them. No Parseval identity for an operator norm is used.

### 1. Admissibility and the entire response

The nodes are distinct because cosine is strictly decreasing on
(0,pi). Odd m includes its middle node x. With r_0=sqrt(d^2+r^2),

    r_0^2=18541/10000 < (273/200)^2=(R-eta)^2.

Their real parts are x, their moduli are at least d>1, and every
grid point has modulus less than one. All denominators of the disk
factors are nonzero on |v|<=R, since U-t_j*R>0. Hence all symbols
and inputs are well defined, with continuous circle values. Each
factor b_(t_j)(R*zeta;u) is the standard disk factor
(zeta-alpha)/(1-conjugate(alpha)*zeta), alpha=t_j*u/R, and has
modulus one on the unit circle. Therefore ||f_u||_2=1.

Specialize C645n's projection identity
P_-[f(zeta)/(zeta-a/R)]=f(a/R)/(zeta-a/R) to this finite product.
It applies because f is holomorphic near the closed disk. The part
(f(zeta)-f(a/R))/(zeta-a/R) is holomorphic after removing its
singularity, so no spatial Fourier mode is lost. The exact result is

    H_q_u f_u(zeta)
       =sum_k [B_u(x)/(R*B_low,u(a_k))]/(zeta-a_k/R).

In physical coordinates z=R*zeta this becomes

    H_q_u f_u(z/R)=sum_k F_(z,u)(a_k),
    F_(z,u)(v)=B_u(x)/[B_low,u(v)*(z-v)],  |z|=R.           (3)

The conjugated angle has been retained throughout. In particular,
the remaining inverse-grid weights are complex; none is declared
positive and no cross term is discarded.

### 2. The arc and ellipse, with their full domains

Let Gamma be the left arc of |v|=r_0, from x-ir to x+ir through
-r_0, and let E be the ellipse centered at x with semiaxes

    s=13/200,  b=sqrt(r^2+s^2),
    v=x+s*cos(phi)+i*b*sin(phi).

The arc has Re(v)<=x and |Im(v)|<=r. On it

    |z-v|>=R-r_0>(U-r_0^2)/(2R)>1/100.                   (4)

Completing the square in cos(phi), as in C645l, gives

    sup_E |v|^2
      <=d^2+r^2+s^2*(1+d^2/r^2)
       =219395653/116640000 < U,
    |z-v|>1/300,  Re(v)<=-h,  h=d-s=237/200.             (5)

The maximum-radius bound also holds in the filled ellipse: the norm
is convex and an interior point is a convex combination of boundary
points. The lune between the segment and Gamma is inside |v|<=r_0
and has Re(v)<=x. The low-grid zeros have modulus at most 1/2 and
therefore lie outside these two closed regions. The poles of inverse
disk factors are precisely these zeros; their numerator zeros cause
no singularities. The pole z lies outside both regions by (4)--(5).
Thus F_(z,u) is holomorphic on neighborhoods of both closed regions,
uniformly in the two boundary variables. These checks justify using
the same contour identities with the changed radius and ellipse.

### 3. A uniform arc exponent

For |v|=a<R and t<a, the disk factor satisfies

    |b_t(v;u)| >= R*(a-t)/(U-a*t).                        (6)

For completeness, its squared modulus is
U*(a^2+t^2-2*a*t*c)/(U^2+a^2*t^2-2*U*a*t*c),
where c=Re(v*conjugate(u))/a is in [-1,1]. Differentiation in c
shows that this decreases with c; its minimum is at c=1.
The right side of (6) increases with a and decreases with t,
as follows by differentiation and U>a^2, U>t^2. On Gamma,
a=r_0>ell=34/25 and 0<=t_j<1/2 for j<K. Hence

    |b_(t_j)(v;u)| >= R*(ell-1/2)/(U-ell/2)=1892/1937.

C645n's angular maximum and exact product-rate comparison give
|B_u(x)|<=exp(-lambda*n), lambda>47/1000. This bound concerns
only the unchanged full grid at x, so the new pole radius does not
alter its hypotheses. Since K=(n+1)/2 and log(1+y)<y for y>0,

    |B_u(x)/B_low,u(v)|
      <=(1937/1892)^K * exp(-47*n/1000)
      <exp(45/3784)*exp(-gamma*n),
    gamma=47/1000-45/3784=8303/236500 > 7/200.             (7)

Also exp(45/3784)<2; for example log(2)>1/2 by integration
of 1/t on [1,2], whereas 45/3784<1/2. Equations (4) and (7)
give sup_Gamma |F_(z,u)|<200*exp(-7*n/200).

Define the continuous arcsine average

    A_(z,u)=(1/pi)*integral_(-r)^r
                       F_(z,u)(x+i*y)/sqrt(r^2-y^2) dy.

C645l's contour deformation applies with S(v)=sqrt((v-x)^2+r^2)
positive on the real ray just left of x. Its branch is holomorphic
in the lune, positive on the open segment, and has only integrable
square-root singularities at the endpoints. Truncating there gives
connecting integrals O(sqrt(epsilon)), which tend to zero for each
fixed n,u,z. Thus

    A_(z,u)=(1/(pi*i))*integral_Gamma F_(z,u)(v)/S(v) dv.

The same arc parameterization, with alpha=arctan(r/d)<pi/2,
and sin(t)>=2t/pi on [0,pi/2], gives
integral_Gamma |dv|/|S(v)|<=pi^2/2. Consequently, uniformly in u,z,

    |A_(z,u)|<400*exp(-7*n/200).                           (8)

No limit in n is interchanged with a contour integral.

### 4. A rationally certified pair bound on the ellipse

We establish the following elementary uniform inequality:

    |b_t(x;u)*b_(t+1/2)(x;u)/b_t(v;u)| <= Q=21/20
    (0<=t<=1/2, |u|=1, Re(v)<=-h, |v|<R).               (9)

Here h=237/200. Put c=Re(u), and set

    X(t,c)=U*(d^2+t^2+2*d*t*c)/(U^2+d^2*t^2+2*U*d*t*c),
    k(t,c)=X(t,c)*X(t+1/2,c)/Q^2,
    A=h*t^2/U+t*c,  B=R*(1-t^2/U),  C=h+t*c.

All displayed denominators are positive on the closed rectangle
0<=t<=1/2, -1<=c<=1: they are squared moduli, with d>1 and U>d.
Also B>0 and C>=h-1/2>0. The exact rational certificate described
below proves throughout that rectangle

    0<k<1,  C-A*k>0,  (C-A*k)^2-B^2*k>0.                (10)

To see why this suffices, let sigma=|b_t(v;u)|. For the domain in
(9), 0<sigma<1; the zero t*u cannot have Re(v)<=-h. Completing
the square in |R*(v-t*u)|^2=sigma^2*|U-t*conjugate(u)*v|^2
gives a level circle with center and radius

    t*u*(1-sigma^2)/(1-t^2*sigma^2/U),
    R*sigma*(1-t^2/U)/(1-t^2*sigma^2/U).

Its leftmost real coordinate is at most Re(v)<=-h. Multiplication
by the positive denominator therefore gives

    C-A*sigma^2-B*sigma <= 0.                             (11)

The polynomial F(y)=C-B*y-A*y^2 has F(0)=C>0 and
F(1)=(h-R)*(1-t^2/U)<0. It has exactly one root in (0,1):
if A>=0 it is strictly decreasing there; if A<0 it is convex,
and its other root, if considered, is greater than one. Conditions
(10), and positivity before squaring, imply F(sqrt(k))>0.
Equation (11) implies sigma>=sqrt(k). Since X(t,c)=|b_t(x;u)|^2,
this proves (9), including t=0 and every direction u.

The certificate uses exact rational interval arithmetic only. It
starts with [0,1/2] x [-1,1], alternately bisects the t and c
coordinates, and accepts a box only when interval arithmetic verifies
all four strict inequalities in (10). Intervals are propagated using
endpoint addition, all four endpoint products, reciprocal division
away from zero, and the exact interval square (zero is included iff
the interval crosses zero). This gives enclosures for every point of
each box, not samples. The saved 6322 accepted boxes, maximum binary
depth 16, form a complete dyadic partition; sibling reduction checks
this independently of the exhaustive traversal. No box failed or was
omitted. The global enclosing extrema are

    k_lower = 21350362698500/179402151302521 > 0,
    k_upper = 1535220121600/1830368134681 < 1,
    (C-A*k)_lower = 13309059095651034649/18370780293378150400 > 0,
    ((C-A*k)^2-B^2*k)_lower =
      15447867720551704968966270108996627441724829078729 /
      747190831549480535887030396680404069330564300144640000 > 0.

The full exact boxes, endpoints, enclosing values, partition checks
and geometry/rate checks are in
`scripts/one-sided-hankel/angular-outer-half-certificate.json`.
Reproduce with
`python3 scripts/one-sided-hankel/angular-outer-half-certificate.py`.
The entire `/minimum_bounds`, `/checks`, `/rates_and_geometry` and
`/failures` fields were inspected. All 16 final checks pass. This
is a finite rational inequality certificate with an explicit covering
argument, not an angular quadrature or floating-point assertion.

### 5. Actual grid pairing and the finite-node error

The real outer partner of t_j=j/n, 1<=j<=L, is
t_(j+L)=t_j+L/n=t_j+1/2-1/(2n). Uniformly for 0<=w<=1,

    |d/dw log|b_w(x;u)||
      <=1/(d-w)+d/(U-d*w)
      <=4+80/41 < 6.                                    (12)

These logarithms are differentiable because neither factor vanishes.
The partner-shift error in each logarithmic modulus is at most 3/n.
The j=0 factor ratio is exactly x/v, with |x/v|<=d/h on E.
Using (9), L<n/2 and log(21/20)<1/20 therefore gives

    |B_u(x)/B_low,u(v)|
      <=(d/h)*exp(3*L/n)*Q^L
      <(d/h)*exp(3/2)*exp(n/40)
      <18*exp(n/40),  v in E.                            (13)

The last deliberately loose constant uses d/h<2 and e<3, hence
exp(3/2)<9. The elementary e<3 follows, for example, from its
series and k!>=2^(k-1) for k>=1, with strict inequality for k>=3.
Together with (5), (13) yields sup_E |F_(z,u)|<5400*exp(n/40).

Use C645l's exact finite-node identity with the new r and s. Set

    rho=(sqrt(r^2+s^2)+s)/r>1,
    w=v-x=(i*r/2)*(lambda+lambda^(-1)), |lambda|=rho,
    S_0(w)=(i*r/2)*(lambda-lambda^(-1)).

This parameterizes precisely E, and dw/S_0=d(lambda)/lambda.
For P_m(w)=product_k(w-i*r*cos((2k-1)*pi/(2m))), that identity is

    P_m'(w)/(m*P_m(w))
      =(1/S_0(w))*(lambda^(2m)-1)/(lambda^(2m)+1).

It is valid for every r>0 and m>=1; its Chebyshev recurrence derivation
does not require the earlier numerical radius. Holomorphy established
in Section 2 permits its application to the present F_(z,u).
Taking residues at the m simple nodes and bounding the error term
gives, with every complex phase retained,

    |(1/m)*sum_k F_(z,u)(a_k)-A_(z,u)|
       <=2*sup_E |F_(z,u)|/(rho^(2m)-1).                  (14)

The integral with 1/S_0 is the stated arcsine average: deform the
lambda circle to |lambda|=1 and use its two traversals of the vertical
segment. Holomorphy on the intervening annulus and the fixed positive
contour distances justify this finite-n deformation.

Here s/r=13/108. Direct integration and a rational square comparison
give

    log(rho)=integral_0^(13/108) (1+t^2)^(-1/2) dt
      >=(13/108)/sqrt(1+(13/108)^2)
      >(13/108)*(100/101)=325/2727.

For n>=15, 2m*log(rho)>(2n/3)*(325/2727)>1; hence
rho^(2m)>e>2 and 1/(rho^(2m)-1)<2*rho^(-2m). Therefore (14) is
strictly less than

    21600*exp(-beta*n),
    beta=(2/3)*(325/2727)-1/40
         =17819/327240 > 7/200.                          (15)

An initial auxiliary test used the stronger-than-needed claim
(2/3)*9*(325/2727)>1, which is false. That failure is preserved in
`scripts/one-sided-hankel/angular-outer-half-certificate-first-pass.json`.
The theorem and final certificate consistently start at odd m>=5,
n>=15. There is no n=9 assertion. No pair-domain or rate check failed.

Combining (3), (8), (14)--(15), and multiplying the average by m proves
(1). Supremum bounds dominate both normalized L2 norms and their
angular quadratic mean, so (2) follows. The exponent difference is
7/200-1/32=3/800>0, which dominates the linear factor m=n/3.
All estimates are uniform in the two angular variables; a shrinking
angular exceptional set or unbounded spatial tail is not omitted.

The separate file `scripts/one-sided-hankel/angular-outer-half-diagnostic.json`
contains only finite floating-point samples, with explicit rounding,
quadrature and tail limitations. It suggested the parameters but is
not a premise of (1)--(15). The rigorous countersequence concerns this
one unit input's full response. It gives no upper bound on the full
operator norm and no obstruction to another input or to RH.

### Independent conceptual audit — 2 November 2026

The separate audit used the invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-outer-half-response-audit.md`. It checked
the entire proof above and the portions of C645g, C645l and C645n
actually used. No new theorem or stronger conclusion is claimed.

**Scaling and the quantitative input.** With alpha=t*u/R, the factor
b_t(R*zeta;u) is (zeta-alpha)/(1-conjugate(alpha)*zeta). The finite
outer product is therefore a unit H2 input, analytic near the closed
disk. The projection in Section 1 cancels exactly B_out(a); conversion
from zeta-a/R to (z-a)/R cancels the remaining 1/R. Thus (3) is a
sum over m nodes, not its average and not an operator norm bound.

C645n's anchor estimate was checked directly in its proof: X(t,c)
in Section 4 is increasing in c, since its derivative has the sign
of (U-d^2)*(U-t^2)>0 for t>0. All anchor factors are maximized at
u=1. The positive function log((U+d*t)/(R*(d+t))) is decreasing,
so its left Riemann sum is at least n times its integral. That
integral is the stated lambda. The 16-term positive logarithm series
and rational remainder from C645n were recomputed independently;
they certify lambda>47/1000. No other unaudited conclusion of C645n
is used here.

**Half-plane implication and the complete certificate.** Completing
the disk level-circle square gives precisely the center and radius
in Section 4. Its leftmost real part is no greater than Re(v), which
is at most -h. This is the direction needed for (11). The denominator
1-t^2*sigma^2/U is positive, so multiplication does not reverse it.
If A>=0, F(y)=C-B*y-A*y^2 is strictly decreasing on [0,1]. If A<0,
it is an upward quadratic with F(0)>0 and F(1)<0: one root lies in
(0,1) and the second lies beyond 1, with F positive before the first
root. The case A=0 is included. From (10), C-A*k>0 and
(C-A*k)^2>B^2*k imply C-A*k>B*sqrt(k). Thus F(sqrt(k))>0,
whereas F(sigma)<=0; with both arguments in (0,1), sigma>sqrt(k).
This proves (9) without a reversed implication or spurious squared
root. At t=0 the same reasoning applies. The numerator defining X
is positive even at t+1/2=1 because d>1, and its denominator is
at least (U-d)^2>0. No direction or endpoint of the rectangle is
excluded.

The independently written verifier
`scripts/one-sided-hankel/angular-outer-half-audit.py` reads every
saved leaf, without importing or executing the original generator.
For an address of length j it starts from [0,1/2] x [-1,1], bisects
coordinate j mod 2, and selects the indicated half at each digit.
It checks that these reconstructed endpoints equal the saved ones,
then recomputes every interval endpoint in (10) using exact rational
arithmetic. The interval product uses all four endpoint products;
division excludes zero in its denominator, and squaring includes zero
exactly when the input interval does. These rules enclose every point
of each box, including its boundary. Every saved enclosing interval
agrees exactly, and every leaf satisfies all four strict inequalities.

For coverage, the verifier builds a binary tree from all addresses.
It rejects a repeated leaf, a leaf above another leaf, and any internal
node without both children; a terminal node must contain only its
leaf. Induction from the root then proves that the leaves cover the
whole initial rectangle, with only shared boundaries. This checks the
saved sibling reduction by a different traversal. All 6322 leaves,
maximum depth 16, pass; their exact relative areas sum to 1, and all
four enclosing extrema equal those displayed in Section 4. The
15 audit checks and all 16 original checks pass. The complete replay,
source hashes, exact anchor logarithms and empty failure list are in
`scripts/one-sided-hankel/angular-outer-half-audit.json`; reproduce
with `python3 scripts/one-sided-hankel/angular-outer-half-audit.py`.
The full `/checks`, `/minimum_bounds`, `/rates_and_geometry`,
`/anchor_rate` and `/failures` values were inspected. The full leaf
evidence was verified by the replay, not inferred from a JSON preview.

**Contour geometry and branches.** On the ellipse, putting c=cos(phi)
gives exactly

    |v|^2=d^2+r^2+s^2+d^2*s^2/r^2-r^2*(c+d*s/r^2)^2.

This proves (5), including the filled ellipse by convexity. Its
rightmost real coordinate is -h<-1/2, and the lune has Re(v)<=x.
Both regions exclude every low-grid zero and the spatial pole z;
the radius bounds give the claimed strict distances from |z|=R.
Since the inverse grid factors have poles only at their grid zeros,
F is holomorphic on neighborhoods of both closed regions.

In the lune, writing v-x=a+i*y gives positive real part
a^2+r^2-y^2 for the radicand away from the endpoints. The branch S
is therefore positive on the open segment and holomorphic across it.
The endpoint roots are simple, so each truncated connecting integral
is O(sqrt(epsilon)) for fixed finite n,u,z. Their limit gives the
stated arc equality with both paths oriented from bottom to top.
The chord-length calculation in C645l gives the arc bound pi^2/2
for every r,d>0 used here; it has no hidden dependence on the older
radius. Uniformity of the final bound follows from the uniform
modulus estimates, without exchanging an n limit and an integral.

The ellipse branch S_0 is separately fixed by lambda and is asymptotic
to w outside the segment; it is not identified with S. As lambda
traverses |lambda|=rho counterclockwise, the image starts at the top
of E moving left, hence also traverses E counterclockwise, once.
The annulus 1<=|lambda|<=rho maps into the filled ellipse, since its
two semiaxes increase with |lambda|. The expression
F(x+(i*r/2)*(lambda+lambda^(-1)))/lambda is holomorphic near that
closed annulus, including lambda=+1 and -1. Thus its unit-circle
integral is the arcsine average with exactly two traversals of the
segment. The Chebyshev logarithmic derivative has simple residues
1/m, while dw/S_0=d(lambda)/lambda. These facts independently check
the sign, the factor 2 in (14), and the exponent 2m. No spatial tail
or angular exceptional set has been removed.

**Odd-grid correction, constants and conclusion.** The pairs
(j,j+L), 1<=j<=L, exhaust indices 1,...,n-1. Their ideal partners
t_j+1/2 and actual partners t_j+L/n both lie in [0,1] and differ
by 1/(2n). The derivative bound in (12) therefore charges at most
3/n per pair. Index 0 contributes x/v, bounded by d/h. This checks
the full-grid identity behind (13), with no missing endpoint factor.
The radial lower bound (6) decreases in t and increases in |v|,
so (7) holds for every arc point and angle, using K=(n+1)/2.

All geometry and rate comparisons were replayed exactly. In particular
the arc exponent 8303/236500 and quadrature exponent 17819/327240
both exceed 7/200. The denominator estimate uses n>=15, for which
(2n/3)*(325/2727)>1; the false n=9 inequality remains in its original
certificate and was checked to be false. Adding the average bounds
400 and 21600 and multiplying by m gives (1). Normalized boundary
and angle measures give (2), with margin 3/800 over 1/32. This is
independent verification of the existing local stop, not progress
beyond its mathematical statement. The implication A_n>=J_n remains
one-way; no full-operator countersequence or actual-Xi sign follows.

## Mathlib

Full matching coverage for this partial-grid input, the two-parameter
pair inequality and the uniform Chebyshev response exponent has not
been checked; no absence claim is made. Finite disk products, Hardy
projection, residues, elementary real inequalities and rational
interval arithmetic are supporting ingredients. The exact analytic
domains and finite certificate remain part of this informal proof;
no formalization is asserted. The independent informal audit is recorded
above; Mathlib coverage remains unchecked.

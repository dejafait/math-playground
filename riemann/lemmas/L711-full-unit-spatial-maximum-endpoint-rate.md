# Lemma 711: the complete unit spatial maximum has the endpoint rate

## Hypotheses

Fix one actual L703 profile, including its original cutoffs, bump and
width, before n varies. Use L666's full family and L709's notation:

    d=5/4, R=11/8, U=121/64, A=27/10, Y=9/20,
    n=12q+3, q>=1, M=n/3, h=A/n,
    a(v)=-d+i*v, v_m=h*(m+1/2+e_m),
    Z_n={-d} union {a(v_m): -2q<=m<2q},
    Q_t(u,v)=(d+t*u)*(U*u+d*t-i*t*v)
                         /[(U*u+d*t)*(d+t*u-i*v)],
    W_n(u,v)=product_(j=0)^(n-1) Q_(j/n)(u,v), W_-=W_n(u,-Y),
    F_n(u,z)=sum_(a in Z_n) W_a(u)/(R-a*z),
    T_n(u,z)=sum_(a in Z_n) W_a(u)*(a*z/R)^M/(R-a*z),
    G_n=F_n-T_n, S_(n,r)(u)=max_(|z|<=r)|G_n(u,z)|.

Here W_a=W_n(u,Im a), including W_x=1. Keep the inverse angular
factor, j=0, unit masses, all M moments, both finite endpoints and
the signed interior. Use L708's real-frequency identity, and L709's
uniform product/physical-tail estimates near u=i/2. L710 supplies
the bilateral-resolvent convention and crossed-pole formula. The
joined step-171 conceptual audit accepts L709--L711 with the stated
fixed-profile hypotheses; this lemma's audit is in Section 7.

Write delta=2*pi*w<1/3000 for the actual fixed bump half-width and

    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)],
    Omega=omega+1/3000<543/500, v0=9/4.

No other bump, profile, moment truncation or positivity premise is used.

## Conclusion

There is a fixed closed positive-measure angular arc I about i/2 on
which, uniformly along every allowed n,

    sup_(u in I) |n^(-1)*log(S_(n,1)(u)/|W_-|)| -> 0.       (1)

In particular, at one existential uniform onset,

    S_(n,1)(u)/|W_-| <= exp(n/100000), u in I.              (2)

The arc can be intersected with L710's arc. This pays its full unit
maximum obligation, with a stronger upper rate than 1/20000. The
remaining lower bound max_(y in D_*)|E_n(y)|>=exp(-n/10000) is NOT
proved. Therefore no positive B_sp/n limit, sublinear B_sp, Jensen
defect payment, actual-Xi positivity or RH candidate is asserted.
Amplitude/full charge, L657 accounting, H/support and realization
remain independent. Constants and onsets depend on the fixed profile.

## Proof

### 1. Scope, standard inputs and the complete contour

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
The new estimate is a family-specific full-maximum bound within that
unchanged scope. No entire-function indicator or saddle theorem is
imported. The standard maximum-modulus principle and Cauchy residue
theorem are used on the explicitly specified domains below.

The Fourier/convolution inputs are those already assessed in L708:
J. Kallsen and P. Kruehner, *On uniqueness of solutions to martingale
problems — counterexamples and sufficient criteria*,
[arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1), Appendix A,
Lemma A.1(6),(9)–(11),(14), pp.29–30; S. D. Miller, *Some notes on
distributions*, 15 January 2006,
[Theorems 4.1–4.2 and Section 6, pp.7–9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf);
and the absolutely convergent exponential transform
[DLMF (1.14.17)–(1.14.18)](https://dlmf.nist.gov/1.14.iii).
Their recorded source qualifications persist. We specialize their
already established inversion/Poisson application, rather than
reprove a general Fourier theorem or continue S_e to nonreal frequency.

Use a spatial-pole coordinate y=X+i*c, distinct from the physical v:

    z(y)=-i*R/(y+i*d)=-R/(d+c-i*X),
    F_n(u,z(y))=(y+i*d)/R * sum_(a in Z_n) W_a(u)/(y-Im a). (3)

This finite rational function has poles only at the retained real
ordinates, all strictly in (-Y,Y), and a finite limit at infinity.
In particular it has no pole at y=-i*d. The infinite anchored sum
will only be used away from the real axis.

For 0<=j<=100 set

    X_j=-1/2+j/100,
    c_j=floor(10^5*sqrt(U-X_j^2))/10^5-d-1/5000.

Let the upper edge be the polygon joining X_j+i*c_j. Close it by
the vertical segments at X=+-1/2 and the bottom c=-1/10. Call the
resulting simple contour Gamma. Every vertex is strictly inside
|y+i*d|<R; convexity of that disk puts all segments and the enclosed
polygon inside it. The upper heights lie in (3/100,1/8), and its
two endpoint heights equal 0.03066<31/1000. Gamma encloses every
retained ordinate and the anchor. Thus every y corresponding to
|z|<=1 lies in its exterior, with z=0 corresponding to infinity.
The exterior maximum-modulus principle applied to (3) will bound
the COMPLETE finite F_n on the unit disk from its values on Gamma.

### 2. Continuous rate certificates and uniform product bounds

At u=i/2 put Phi_c(X)=integral_0^1 log|Q_t(i/2,X+i*c)|dt. The
exact factor formula is

    |Q_t|^2=[(d^2+t^2/4)*(t^2*(d+c)^2+(U/2-t*X)^2)]
              /[(d^2*t^2+U^2/4)*((d+c)^2+(t/2-X)^2)].    (4)

The new certificate proves the following strict inequalities:

    Phi_c(X)+c*Omega/A <203/10000, on the ENTIRE upper polygon;
    sup_R Phi_(-1/20)<49/1000, sup_R Phi_(-11/100)<80/1000;
    Phi_0(X)<37/2000,                       -.51<=X<=-.49;
    partial_c Phi_c(X)<-39/100,             -.51<=X<=-.49, 0<=c<=.031;
    Phi_(-1/10)(.49)<-1/10, Omega/A<403/1000.             (5)

Here and below finite decimals denote exact rationals. These are
continuous enclosures, not a sampled maximum. The full reduction and
error bounds follow. Put D=d+c, a_t=U/(2t), b_t=t/2 for t>0. The
variable part of log|Q_t| is

    (1/2)*log[(D^2+(X-a_t)^2)/(D^2+(X-b_t)^2)].

Its two first derivatives, also with their direct t=0 limits, are

    partial_X log|Q_t|=(b_t-X)/(D^2+(X-b_t)^2)
                         -(a_t-X)/(D^2+(X-a_t)^2),
    partial_c log|Q_t|=D/[D^2+(X-a_t)^2]-D/[D^2+(X-b_t)^2]. (6)

The Hessian operator norm is <=2/D^2, by differentiating each
logarithmic distance. In the rectangle -1<=X<=.51,
-.11<=c<=.15 the four affine t factors in the logarithm of (4)
have moduli at least d, U/2, 4/5, 57/50 respectively. For the third,
negative X gives the stronger U/2 bound; otherwise the squared
minimum is at least (U/2)^2*(57/50)^2/[(57/50)^2+.51^2]>(4/5)^2.
The four slopes have moduli bounded by 1/2,d,7/4,1/2. Hence the
absolute fourth t derivative of the logarithmic integrand is <256.
The fourth t derivative of EITHER component in (6) is <512, using

    24*(U/2)*(7/4)^3/(4/5)^5+24*(1/2)^4/(57/50)^5<512.

For the third affine factor the fourth derivative of t/L is
-24*L(0)*L'^3/L^5; for the fourth use the derivative of 1/L.
Real and imaginary parts give the two components, so these bounds
cover both. The exact rational checks also verify the <256 bound.

Use L709's integer-directed rational logarithms (scale 2^100,
40 atanh terms with their full remainder) and its elementary cubic
Taylor quadrature error K/(45*N^4), now N=64. On each upper segment
let m=(Delta c)/(Delta X), r=Delta X/2. The midpoint rate, the
enclosed directional derivative partial_X Phi+m*partial_c Phi
+m*Omega/A times r, and (1+m^2)*r^2/(d+c_min)^2 bound that entire
segment. There are 100 segments; their largest upper enclosure is
below .020131, strictly below .0203. Geometry is checked at every
vertex, with convexity paying the segments.

For each global horizontal-line maximum, L709's real-halfline
reduction still applies: a_t*b_t=U/4, a_t+b_t>=R and
1+R+U/4>(7/5)^2. Each factor is increasing for X<=-1 and has no
larger value for X>=0 than at zero. The maximum is thus in [-1,0].
Use 200 cells on that interval, midpoint derivative bounds and the
same Hessian remainder. The resulting upper bounds are below
.047840 and .078862. Twenty cells similarly bound Phi_0 on the
left strip by .018425. A 10-by-16 grid of rectangles bounds
partial_c Phi there: its gradient has norm <=2/d^2, so the sum
of the two cell radii times 2/d^2 pays the whole cell. The resulting
upper bound is below -.407902. The right-strip value is below
-.103421. All decisions use exact fractions, not these previews.

Two further useful whole-strip consequences are as follows. For
-.51<=X<=-.49 and 0<=c<=.031, (5) gives

    Phi_c(X)+c*Omega/A
       <37/2000+.031*(.403-.39)=.018903<.019.            (7)

For the same X and -.1<=c<=0, the positive first term of partial_c
in (6) and X-b_t<=-.49 give

    partial_c Phi_c(X)>=-(23/20)/[(23/20)^2+.49^2]>-v0/A.

Here D/(D^2+.49^2) decreases for D>=23/20. Therefore

    Phi_c(X)+c*v0/A <= Phi_0(X)<.0185.                  (8)

For .49<=X<=.51 and -.1<=c<=.031, the factorwise single-minimum
argument from L709 bounds Phi_c(X) by Phi_c(.49). Also a_t+b_t>=R
>2*.51 makes partial_c log|Q_t| negative on this strip. It follows
that Phi_c(X)<=Phi_(-.1)(.49)<-.1. Adding c*Omega/A for positive c
still leaves a negative upper bound; adding c*v0/A for negative c
only improves it. These arguments include t=0 by its direct limit.

Retain L709's strict global bounds on c=.15, -.1 and 0, respectively
-.041, .074 and .024, and |W_-|>=C^(-1)exp(.0204*n). All compact
rate inequalities above persist on ONE sufficiently small fixed
closed neighborhood V of i/2. No factor vanishes on these compact
sets. Uniform Riemann sums give log|W_n|=n*Phi(u;X,c)+O(1).
The horizontal-line tails extend uniformly exactly as in L709:
|Q_t|<=.9 for sufficiently large |X|, while Q_0 supplies
C/(1+|X|). This also applies to c=-.05 and -.11; their limits r_t
are the same. All choices of V precede the bridge width below.

### 3. The complete infinite sums off the real axis

Write k(v)=W_n(u,v)/(R-a(v)*z(y)). Off the real axis it is integrable
and O(v^(-2)). Use L708's positive-halfline convolution for W_n,
and the resolvent exponential measure, positive-halfline if c<0
and negative-halfline if c>0. Inversion is

    p_y(v)=(2*pi*h)^(-1)*integral_R k(t)*exp(-i*t*v/h)dt. (9)

These are continuous finite complex densities with finite first
absolute moments. For c>0, L710's exact formulas are

    p_y(v)=-W_n(u,y)*exp(-i*y*v/h)/(h*z(y)),        v<=0,
    p_y(v)=p_y^+(v)-W_n(u,y)*exp(-i*y*v/h)/(h*z(y)), v>=0, (10)

where p_y^+ is (9) on Im t=.15. On all top/side sets under use,

    |p_y^+(v)|<=C*n*exp[n*(-.041+v/18)], v>=0.          (11)

The pole is separated from that line. Every Q pole lies below -1
after shrinking V; the only other pole is y. Vertical integrals
vanish by O(|Re t|^(-2)) for fixed n,v, just as in L710.

On the upper polygon and the positive-height sides c>=epsilon>0,
the lower line Im t=-.1 crosses no pole, giving

    |p_y(v)|<=C*n*exp[n*(.074-v/27)], v>=0.             (12)

The exact real-frequency correction is still

    S_e(v)=-chi_w(v/(2*pi)), |v|<3*pi/4,
    |S_e(v)|<=E*|v|, E=sum|e_m|<infinity.              (13)

Both bump supports lie in |v|<=Omega<v0. Pairing the positive bump
with (10) costs at most C*n*|W_n(u,y)|*exp(c*Omega/h), plus
C*n*exp(29*n/1500) from (11). The negative bump is bounded by
the first formula in (10) and no more than this same residue bound.
For v>=v0 use (12), whose starting exponent is < -.009. For
v<=-v0 use the first formula of (10); its starting rate is
Phi_c(X)-c*v0/A, no larger than the bounded residue rate. Integrating
these tails costs constants/powers of n, uniformly for c>=epsilon.
Thus (5),(7) bound the entire pairing at a rate <.0203 on the top,
and <.020 on the positive-height sides/strip edges.

Every comb sample is retained. Positive samples use (12). The
negative and zero samples use (10), or its exact geometric sum

    2*pi*sum_(l<=0)(-1)^l*p_y(2*pi*l)
       =-2*pi*W_n(u,y)/[h*z(y)*(1+exp(2*pi*i*y/h))].     (14)

For c>=epsilon its denominator is bounded away from zero eventually.
Its rate is bounded by the same upper residue rate. In particular
the zero sample has not been discarded.

For c<0 the resolvent has positive-halfline support, so p_y vanishes
on v<0 and p_y(0)=0: Q_0 and the extra exponential make the remaining
convolution atom-free at the moving endpoint. No pole is crossed
when shifting up to .15, so p_y=p_y^+ for v>=0. This pays the bump
by (11) and the same 29/1500 exponent.

On the bottom c=-.1 shift down only to -.05, which crosses no pole.
The new global line bound in (5) gives

    |p_y(v)|<=C*n*exp[n*(.049-v/(20*A))], v>=0.         (15)

At v=v0 this rate is .007333...<.01, so it pays the whole high
frequency integral and positive comb samples.

On negative-height sides or bridge horizontal edges, take
-.1<=c<=-epsilon and shift down to -.11. THIS crosses y, giving

    p_y(v)=p_y^-(v)+W_n(u,y)*exp(-i*y*v/h)/(h*z(y)),
    |p_y^-(v)|<=C*n*exp[n*(.080-.11*v/A)].             (16)

The sign follows by orienting the rectangle with its lower edge
to the right: real integral = lower integral -2*pi*i*residue,
and the residue is i*W_n(u,y)*exp(-i*y*v/h)/z(y).
At v0 the lower-line rate is negative. For v>=v0 the residue
rate is at most .0185 on the left by (8), and negative on the right.
The integrals of E*v times its exponentially decreasing tail are
finite with constants depending on epsilon; the positive sample
series is likewise geometric. Negative/zero samples are zero.
Thus the WHOLE correction and comb have rate <.020 on these sets.

For completeness these estimates justify the exact identity used:

    H_n(u,z)=1/(R+d*z)+sum_(m in Z) W_n(u,v_m)/(R-a(v_m)*z)
      =k(0)+2*pi*sum_(l in Z)(-1)^l*p_y(2*pi*l)
                                      +integral_R S_e(v)*p_y(v)dv. (17)

The shifted and unshifted lattice sums converge absolutely by
k(t)=O(t^(-2)) and separation. Fubini for their differences follows
from E*integral |v*p_y(v)|dv<infinity. For each fixed n, the densities
above have two-sided exponential tails (or vanish on the negative
side). Their Gaussian convolutions at comb points have a summable
exponential majorant, so the Gaussian-regularized Poisson identity
passes to the limit by continuity and domination, exactly as in
L708/L710. No density or comb identity is used at c=0. The anchor
k(0) is bounded on every contour set here, since y stays away from 0.

Equations (10)–(17), including all tails and samples, prove H_n=o(W_-)
uniformly on the upper polygon, bottom, both sides with |c|>=epsilon,
and the horizontal edges c=+-epsilon, .49<=|X|<=.51. Constants may
depend on a fixed 0<epsilon<=.001; V does not. The strict rates
used to select V hold on the closed side bands including c=0.

### 4. Both physical tails and the finite real-axis bridges

Away from c=0, subtract both omitted physical tails from (17) to
recover the finite F_n. L709's complete negative-tail estimates,
including its near-endpoint summable ratios, compact far gap and
infinite .9-product tail, imply an absolute bound C_epsilon*|W_-|.
The positive tail is O(n*exp(-n/10)). The resolvent is uniformly
bounded on compact real t by |z(y)|^(-1)/epsilon and supplies
C/(1+|t|) at infinity. Thus these estimates apply uniformly to
every set in Section 3. In particular

    |F_n(u,z(y))/W_-|<=C_epsilon                         (18)

on all those sets. No symmetry of e and no omission of the signed
interior has occurred. The interior was retained through (17).

It remains to bound the vertical sides at |c|<epsilon. The INFINITE
sum can have real-axis poles here and must not be used. For
x0=-1/2 or 1/2 take the rectangle

    |Re y-x0|<=a=1/100, |Im y|<=epsilon<=1/1000.

The FINITE function (3) is analytic on its closure: all its poles
lie in (-.45,.45), at least .04 away horizontally. Its horizontal
edges satisfy (18). Its vertical edges satisfy the full absolute
finite-sum bound from L709, hence, for sufficiently large n,

    |F_n(u,z(y))/(C_epsilon*W_-)|<=exp(n/250).           (19)

Indeed there are O(n) terms with bounded denominators here,
|W_a|<=C*exp(.024*n), and |W_-|>=C^(-1)exp(.0204*n);
the difference .0036 is strictly below 1/250=.004. Enlarge
C_epsilon to at least 1. The onset is uniform in u.

Set the holomorphic function

    H_epsilon(y)=2*cosh((y-x0)/epsilon)/cosh(a/epsilon).

On both vertical edges Re H_epsilon>=1, since |Im y/epsilon|<=1
and cos 1>=1/2. On both horizontal edges its real part is positive.
Apply the maximum-modulus principle to the analytic function

    [F_n(u,z(y))/(C_epsilon*W_-)]*exp[-(n/250)*H_epsilon(y)].

Equations (18),(19) bound its modulus by one on every edge. No
logarithm of a possibly zero function was taken. On Re y=x0 this
gives the COMPLETE bridge bound

    |F_n(u,z(y))/W_-|
       <=C_epsilon*exp[n*2/(250*cosh(a/epsilon))].       (20)

For epsilon=.001, the positive even Taylor terms through degree
8 give cosh 10>2000, so the exponent in (20) is <n/250000.
More generally its coefficient tends to zero as epsilon tends to
zero. Epsilon is fixed before n in every application; neither the
profile nor V nor Gamma is changed by this choice.

### 5. Exterior maximum, finite moments and uniform quantifiers

Apply the exterior maximum principle to (3) on the Riemann sphere
outside Gamma; infinity is a removable point, not an uncontrolled
boundary. All its finite poles are enclosed. Combining (18),(20)
and the fact Gamma lies strictly inside |y+i*d|<R gives

    max_(|z|<=1)|F_n(u,z)|/|W_-|
       <=C_epsilon*exp[n*2/(250*cosh(a/epsilon))].       (21)

L709's ABSOLUTE finite-moment remainder, on the whole |z|<=65/64,
is O(n*exp(.024*n)*v^(n/3)), v^2=59657/61952. Its ratio to W_-
tends to zero exponentially, since

    .024+(59657/61952-1)/6-.0204 < -1/400.

Consequently replacing F_n by the exact G_n=F_n-T_n in (21) only
adds o(1) to the normalized maximum. With epsilon=.001, its fixed
prefactors are eventually absorbed into the larger exponent
1/100000, proving (2).

For any alpha>0, first choose a fixed epsilon<=.001 so
2/[250*cosh(a/epsilon)]<alpha/2, then let n grow to absorb
C_epsilon and the tail. This proves a uniform upper limsup zero
in (1). The neighborhood V is common to all these choices, as
established in Section 3; allowing V to shrink with alpha would
not suffice. L709's nonzero scalar limit at z=1/2 gives uniformly
S_(n,1)/|W_-|>=c_0>0 on a fixed arc inside V. This supplies the
matching lower liminf and proves the absolute uniform limit (1).
Intersect with L710's fixed arc if using its outer-disk reduction.

### 6. Evidence and remaining limitation

Run from the active notebook:

    python3 scripts/one-sided-hankel/spatial-unit-contour-rates-168.py

The certificate is
`scripts/one-sided-hankel/spatial-unit-contour-rates-168.json`.
All 28 exact comparisons pass. It retains all 100 upper segments,
400 global-line cells, 20 left-strip cells and 160 derivative cells,
with complete quadrature/logarithm remainders and a hash of the
reused arithmetic definitions. The certificate is auxiliary evidence
for Section 2 and the elementary margins, not an independent audit
of Sections 3–5 or of L709/L710.

This completes the unit-maximum obligation exposed by L710. Its
centered bump transform can still cancel at the relevant complex
points. No lower bound on that transform has been silently inferred
from its positive values on the imaginary axis, its compact support,
or its coefficient's exponential growth. Hence (1) alone neither
decides B_sp nor stops the sublinear-growth sufficient mechanism.

### 7. Separate conceptual audit — 3 November 2026, step 171

This accepts (1)--(2) under the unchanged invocation-start EXPLORE
assessment `drafts/literature/2026-11-03-fixed-profile-spatial-growth-stop-audit.md`.
In particular the arc is fixed independently of epsilon and of the
desired limiting rate. No substantive correction is needed.

The maximum-principle inputs are R. B. Ash and W. P. Novinger,
*Complex Variables* (2004), [Theorem 2.4.12 and proof, printed
pp.23--24, PDF pp.37--38](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=37),
and [4.1.5(a), finite-limit proof p.4, and 4.1.8 p.5](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=65).
These are the precise passages inspected by the prior source review.
The boundary form requires analyticity in a connected region and
continuity on its closure; infinity is treated using the reciprocal
coordinate and its finite limit. The finite-contour residue theorem
and simple-pole formula are Howell--Mathews, [Section 8.1,
Theorems 8.1.5 and 8.1.7(1)](https://complexanalysis.org/web/sec_residue-thm.html),
with the pole census and vertical-edge bounds checked here and in L710.

**Complete geometry and arithmetic.** Algebra gives (3), so its only
finite poles are the retained real ordinates, all strictly in (-Y,Y).
The factor y+i*d creates no new pole. At infinity its value tends
to R^-1*sum_a W_a, a finite number for fixed n,u; no bound on this
number is assumed. The polygon is simple, all its upper heights are
positive, its bottom is below the real axis, and its sides are outside
[-Y,Y]. It therefore encloses every pole. Every upper vertex is inside
the disk |y+i*d|<R. The two bottom vertices also are: their squared
radius is 1/4+(23/20)^2=629/400<121/64. Convexity pays every edge
and the enclosed polygon. The image of |z|<=1 is in the exterior,
with z=0 represented by infinity. This verifies all geometric
hypotheses of the exterior maximum argument, including infinity.

The fourth-derivative and Hessian arguments audited for L709 extend
to D>=57/50 and X<=.51, as checked by the strict affine-factor bounds.
The t=0 limits in (6) are finite. Directional derivative intervals
use both endpoints when the polygon slope is negative. The Hessian
Taylor remainder is (1+m^2)*r^2/(d+c_min)^2 for every entire segment.
The left-strip gradient cells use an L1-radius bound, which exceeds
the Euclidean radius required by the Hessian norm. On the right strip,
a_t+b_t>2*.51 makes the c derivative negative; the single-minimum
argument bounds every X>=.49 by its value at .49. For negative c
on the left, differentiating Phi_c+c*v0/A gives a strictly positive
lower bound, so its value is bounded above by the c=0 value.

All 100 polygon segments, 400 global-line cells, 20 left real cells,
160 gradient cells, endpoint/right enclosures and 28 exact comparisons
were recalculated and match the entire original certificate. Run
`python3 scripts/one-sided-hankel/spatial-growth-audit-171.py`;
the full replay is `scripts/one-sided-hankel/spatial-unit-contour-rates-168-replay-171.json`.
The exact upper-polygon enclosure is

    2860937088118937229014112929435496334300360108633
      /142116342988642098390676056298846654530846720000000
        <203/10000<51/2500.

Its strict separation from the endpoint rate, not a plotted polygon
or sample, is what makes the upper-boundary infinite sum negligible.

**Both signs of c and the common neighborhood.** On c>0 the negative
resolvent measure and upward residue have L710's signs. The negative
bump, negative high-frequency tail and all nonpositive comb samples
are bounded by the same residue rate Phi_c+c*Omega/A as the positive
bump. On c<0 the positive-supported density has zero negative and
zero samples; shifting upward crosses no pole. The bottom uses the
pole-free line -.05. The negative sides instead cross y on moving
down to -.11: real-line integral equals lower-line integral minus
2*pi*i times the residue, giving the plus sign in (16). Its decaying
residue is used only for v>=v0; the positive bump already uses (11).
Every tail is integrable, with constants depending on fixed epsilon.
The exact shifted-lattice identity retains the anchor and the full
comb, and Gaussian removal is for fixed n before these uniform bounds.

The rate conditions choosing V are on the compact polygon, bottom,
and CLOSED side bands including c=0, as well as the finitely many
global contour lines and L709's normalization sets. Their margins
are strict. Compact continuity preserves them on one V independently
of epsilon. At c=0 no density formula is asserted; only the continuous
product-rate inequalities are used in choosing V. After V is fixed,
each epsilon>0 gives separated resolvents and finite tail/comb constants.
Their divergence as epsilon decreases affects the onset, not V.
This distinction validates Section 3's uniformity claim.

**Finite bridges and the order of limits.** In each bridge rectangle
the finite rational function is analytic on a neighborhood of the
closure: its horizontal distance from every pole is at least .04.
The infinite lattice sum is not used across the real axis. The
horizontal finite-function bound follows by subtracting both physical
tails off the axis. On the vertical edges the rate difference is
.024-.0204=.0036<1/250, leaving room for the O(n) prefactor.
For H_epsilon, Re H>=1 on the vertical edges and Re H>0 on the
horizontal edges, since |Im y|/epsilon<=1 and cos 1>=1/2.
The multiplied analytic function is therefore bounded by one on the
whole rectangle boundary. At its center line Re H<=2/cosh(a/epsilon),
which proves (20) without taking a logarithm of a function with zeros.

On the compactified exterior of Gamma the finite rational function
is analytic including infinity, continuous up to Gamma, and hence
has its maximum on Gamma (unless constant, when the bound also holds).
The entire |z|<=1 maximum is consequently bounded by (21). The
absolute all-M remainder has rate relative to W_- strictly below
-1/400. For any alpha>0 choose epsilon>0 after fixing V, and then
choose n so its fixed C_epsilon and the finite remainder are absorbed.
This gives uniform upper rate zero on one fixed arc. L709's nonzero
scalar limit supplies the matching uniform lower rate zero. No
epsilon(n), shrinking arc or pointwise-to-uniform inference is used.

## Mathlib

Full matching coverage of this fixed-profile maximum asymptotic,
the contour/bridge specialization and the uniform signed-tail
assembly has not been checked. No absence or formal verification
is claimed. The named complex-analysis and Fourier inputs retain
their precise citations and source qualifications above. Exact
rational auxiliary checks are not a formal analytic proof.

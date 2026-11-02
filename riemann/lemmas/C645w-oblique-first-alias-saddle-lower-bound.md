# Corollary 645w: the oblique first alias gives a subfamily angular lower bound

## Hypotheses

Use exactly C645v's family: odd m>=5, n=3m, x=-5/4, R=11/8,
U=R^2=121/64, r=27/50, eta=1/100, the m common poles

    a_k=x+i*r*cos((2*k-1)*pi/(2*m)), 1<=k<=m,

and original simple-pole residues all one. For |u|=1 put

    B_u(v)=product_(j=0)^(n-1) R*(v-(j/n)*u)/(U-(j/n)*conjugate(u)*v),
    W_n(v,u)=B_u(x)/B_u(v),
    q_u(zeta)=sum_k [W_n(a_k,u)/R]/(zeta-a_k/R),
    F_n(t,u)=W_n(x+i*r*cos(t),u),
    b_l(u)=(2*pi)^(-1)*integral_0^(2*pi) F_n(t,u)*exp(-i*l*t) dt.

Restrict u=exp(i*phi) to |phi-13*pi/16|<=epsilon=10^(-6).
Use C645v's normalized Hardy spaces, H_q f=P_-(q*f), and largest
operator norm. The same poles and residues serve every angle; the
conjugated denominator angle is retained. No Xi realization, positivity
of weighted complex residues, or detector bound is assumed.

## Conclusion

There exist constants c,C>0 and one onset n_0, independent of phi and
of the allowed n, such that

    |b_(2m)(u)| >= c*n^(-1/2)*exp(n/200),
    |b_0(u)| <= C*exp(-3*n/50),
    |b_0(u)-2*b_(2m)(u)| >= c*n^(-1/2)*exp(n/200)          (1)

for n>=n_0. Constants c may decrease between inequalities. With
C645v's complete alias remainder this gives

    ||H_q_u|| >= c*sqrt(n)*exp(n/200),
    (mean_theta ||H_q_(i*exp(i*theta))||^2)^(1/2)
        >= c*sqrt(n)*exp(n/200).                           (2)

The latter mean is over the whole circle; its lower bound uses only
the fixed sector of normalized measure epsilon/pi. This is a lower
bound for this one fixed-radius Chebyshev subfamily, not for arbitrary
common-pole families. In particular it excludes this subfamily as a
countersequence at exponent 1/32. General families, the actual-Xi
bridges and all-degree signs remain open. The onset is existential.

This is a local quantitative advance within the saved EXPLORE scope,
not certified originality. A separate conceptual audit on 2 November
2026 verified the argument and complete interval certificate, including
C645v's full tail, without a mathematical correction; see the audit
record below. It is not an RH resolution candidate.

## Proof

### Scope, imported rules and why the calculation is needed

Reuse the unchanged invocation-start
[angular source assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md).
C645v supplies the family, admissibility, Fourier normalization, sector
rectangle, entire alias identity, full higher-alias estimate and the
operator lower bound. Those inputs passed the same separate audit. C645u is only
a possible downstream comparison and is not a mathematical input here.

The imported contour rules are R. W. Howell and J. H. Mathews,
*Complex Analysis*, online edition, front matter updated 22 August 2025,
[Section 8.1, Theorem 8.1.5](https://complexanalysis.org/web/sec_residue-thm.html)
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html),
as inspected in the reused assessments. We use their holomorphic
contour-deformation case and contour bound. They are not reproved.
The standard rational Hardy-space convention is L. Baratchart,
S. Chevillard and T. Qian, *Minimax principle and lower bounds in
H2-rational approximation*, J. Approx. Theory 206 (2016), 17--47,
[v2, Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004), already incorporated
in C645v. No Nehari or Parseval theorem for an operator norm is used.

The new local work is the evaluated uniform saddle and whole-contour
geometry. The elementary product expansion and localized integral
argument are written out to verify their hypotheses for a complex
n-dependent product and a moving contour. They are standard methods,
not claimed new general theorems. We do not import an unread saddle
theorem, or use numerical root finding as an existence proof. A direct
Gaussian moment inequality below verifies the required noncancellation
without an uninspected complex-Gaussian asymptotic formula.

### 1. Branches, exact phase and finite-product expansion

Write v(z)=x+i*r*cos(z), a=U*u, and

    J(w)=-sum_(k>=1) w^k/[k*(k+1)], |w|<1,
    P(v,u)=log(x/v)+J(u/x)-J(u/v)+J(v/a)-J(x/a),
    H(z,u)=P(v(z),u)-(2*i/3)*z.                            (3)

Here log(x/v)=-log(1+(v-x)/x), with the logarithm given by its
power series. All the other logarithms below are log(1-w) on |w|<1.
On the closed strip 0<=Re(z)<=2*pi, |Im(z)|<=117/1000,

    |v| >= d-r*sinh(117/1000)>d-r/7>1,
    |v| <= d+r*cosh(117/1000)<d+8*r/7<U,
    |(v-x)/x| <= (r/d)*cosh(117/1000)<1, d=5/4.

For example sinh h<=h/(1-h^2)<1/7 and
cosh h<=exp(h)<=1/(1-h)<8/7 for 0<=h<=117/1000.
Thus these are strict compact domain bounds. For actual |u|=1,
every series argument in (3), including u/x, u/v, v/a and x/a,
has modulus strictly below one. There are no grid poles or product
zeros on this strip, for any n. The C645v sector rectangle also has
strict margins on the narrower boxes used in the certificate below.

For 0<=s<=1 define the single-factor logarithm

    f(s,v,u)=log(x/v)+log(1-s*u/x)-log(1-s*u/v)
                        +log(1-s*v/a)-log(1-s*x/a).        (4)

Its exponential is exactly
[(x-s*u)*(a-s*v)]/[(v-s*u)*(a-s*x)]. Consequently
W_n=exp(sum_(j=0)^(n-1) f(j/n,v,u)), with no branch ambiguity.
Integrating the absolutely convergent logarithm series shows
integral_0^1 f(s,v,u) ds=P(v,u).

The first two s derivatives are uniformly bounded on the compact
domain just described. The composite trapezoid estimate therefore gives

    sum_(j=0)^(n-1) f(j/n,v,u)
        = n*P(v,u)+(f(0,v,u)-f(1,v,u))/2+E_n(v,u),
    |E_n(v,u)|<=C_0/n.                                   (5)

For clarity this complex estimate follows by Taylor expansion on each
real s cell: the error of the integral against its trapezoid is at
most a fixed constant times sup|f_ss|/n^3. Sum the n cells, multiply
by n, and subtract the endpoint half-weights to obtain (5). The same
bound applies to complex values by the integral Taylor remainder.
There is no large-n interchange without a uniform bound.

Put A(v,u)=exp((f(0,v,u)-f(1,v,u))/2). It is analytic, nonzero,
and bounded above and away from zero on this compact domain. Thus

    W_n(v,u)=exp(n*P(v,u))*A(v,u)*(1+O(1/n)),              (6)

uniformly. Both the branch choice and the endpoint amplitude in (6)
are essential; replacing the product by its absolute envelope would
not justify the lower bound.

### 2. A certified saddle and a curved contour

Differentiating the uniformly convergent logarithm integrals gives

    P_v=1/v+(a/v^2)*log(1-v/a)+(1/u)*log(1-u/v),
    P_vv=-1/v^2-(2*a/v^3)*log(1-v/a)
                         -1/[v^2*(1-v/a)]+1/[v^2*(1-u/v)],
    H'=P_v*(-i*r*sin(z))-2*i/3,
    H''=P_vv*(-i*r*sin(z))^2+P_v*(-i*r*cos(z)).            (7)

Take the exact decimal rational center

    z_* = 4.876972288459421+0.11410424409610605*i,
    D_* = -0.20186986852836578+0.17099621992252434*i,
    rho_*=1/5000.

The interval certificate described in Section 3 proves, throughout
C645v's rectangle

    -.831471<=Re(u)<=-.831468, .555569<=Im(u)<=.555572,

and throughout the complex disk |z-z_*|<=rho_*, that

    |1-H''(z,u)/D_*| < .021,
    |H'(z_*,u)/D_*| < .000171,
    .000171+.021*rho_* < rho_*.                           (8)

The map z -> z-H'(z,u)/D_* is a contraction on the closed disk:
integrate its complex derivative along the segment between two points.
The last inequality maps the disk strictly into itself. Its iterates
are Cauchy by the geometric contraction bound; their limit is the
unique fixed point z_s(u) there. This elementary argument also gives
continuous dependence on u, uniformly, by comparing the iterates.
Hence H'(z_s,u)=0. Equation (8) makes H'' nonzero there.
No completeness assertion about other complex saddles is needed.

Write t_s=Re(z_s), h_s=Im(z_s), and set

    kappa(u)=-h_s/sin(t_s),
    z(t,u)=t-i*kappa(u)*sin(t), 0<=t<=2*pi,
    h(t,u)=H(z(t,u),u).                                   (9)

The certified disk puts sin(t_s)<0 and h_s>0. The certificate gives

    .1154606 < kappa < .1158740 < .117,
    Re H(z_s,u) > .005,
    Re h''(t,u) < -.05 for |t-Re(z_*)|<=.21.              (10)

At t=t_s the contour passes through z_s and h'(t_s,u)=0.
Its derivative z'=1-i*kappa*cos(t) never vanishes. The full contour
lies in Section 1's strip and is a holomorphic-integrand deformation
of [0,2*pi], with the same endpoints. In lambda=exp(i*z) coordinates
it is the simple positive radial curve |lambda|=exp(kappa*sin(t));
thus no orientation or winding factor is missing.

The certificate further covers every t in [0,2*pi] by closed cells.
Those not entirely outside |t-Re(z_*)|<.2 lie within the local
interval in (10). On every remaining cell,

    Re h(t,u) < .004.                                    (11)

On the entire contour, independently of this division,

    Re P(v(z(t,u)),u) < -.06.                            (12)

Finally, for the exact saddle value

    a_s=-h''(t_s,u)=-H''(z_s,u)*(1-i*kappa*cos(t_s))^2,
    .18 < Re a_s < .22, |Im a_s| < .20.                  (13)

The phrase "outside" in (11) includes every full complementary cell;
the small overlapping boundary cells are covered by (10). This avoids
an unverified gap between the local and complementary estimates.

### 3. Complete enclosure and its arithmetic meaning

Reproduce with

    python3 scripts/one-sided-hankel/oblique-leading-saddle-certificate.py

The full certificate is
`scripts/one-sided-hankel/oblique-leading-saddle-certificate.json`.
It contains all 1024 contour cells, all 32 local curvature cells, the
saddle enclosures, every required comparison and an empty failure list.
The code uses Decimal precision 42. Each elementary arithmetic result
is expanded using next_minus/next_plus; sqrt is used only with an
outward enlargement. The accepted computation uses no binary floats.

Here are the series and error rules, so the certificate is not a
sampling assertion. Machin's identity pi=16*atan(1/5)-4*atan(1/239)
is enclosed using 48 and 16 alternating terms respectively, each with
its first omitted absolute term. The identity follows from the tangent
addition rule and the quadrant of 4*atan(1/5)-atan(1/239).
Real arguments are reduced by integer multiples of this interval pi/2.
For the resulting |y|<1, sin and cos use 20 terms and a remainder
2/40!; sinh and cosh use the same rule for |h|<1. These bounds cover
the complete tails, including interval endpoint effects. Complex
trigonometric values follow from the real/hyperbolic formulas.

For a complex rectangle w with q>=sup|w|, q<.9, evaluate 120 terms
of log(1-w) or J(w) at its midpoint, with outward arithmetic.
The respective series tails are bounded by

    q^121/[121*(1-q)], q^121/[121*122*(1-q)].               (14)

If delta is the maximum distance from the midpoint to the rectangle,
the additional variation bounds are delta/(1-q) and
delta/[2*(1-q)] respectively. The first follows from the logarithm's
derivative; the second from sum_(k>=1) q^(k-1)/(k+1)<=1/[2*(1-q)].
The segment stays in |w|<=q. Thus interval powers with uncertain
arguments are not silently replaced by point values. All q<.9 and
denominator assertions are checked by the completed execution.

The saddle disk is enclosed by its rectangle. The interval derivative
in (7) bounds the whole disk, giving (8); the phase lower bound is
the value at z_* minus rho_* times a bound for |H'| on that disk.
The interval kappa in (10) encloses all possible exact saddles.
For each contour cell, compute h at its midpoint with the entire u
and kappa intervals, and enlarge its real part by the cell half-width
times a bound for |Re(h')| on the whole cell. For P use

    d Re(P)/dt=Re(h')+(2/3)*kappa*cos(t).

The second derivative h''=H''*(z')^2+H'*z'' is bounded directly
on every local cell. At the actual saddle H'=0, so (13) instead
uses -H''*(z')^2 on the entire saddle box. The maximum and minimum
comparisons in the certificate examine every saved cell, not previews.

Rounded outward readable bounds from the completed certificate are

    contraction < .020711,
    image radius < .000175028 < .0002,
    Re H(z_s) > .0056393,
    local real curvature < -.13749,
    complementary Re h < .002671 < .004,
    whole-contour Re P < -.0691027 < -.06.                (15)

The initial certificate failed the disk-invariance test for radius
.0001; it is preserved as
`scripts/one-sided-hankel/oblique-leading-saddle-initial-failed.json`.
Its other inequalities did not prove saddle existence. The accepted
radius .0002 and all accompanying enclosures were rerun together.
Two preliminary implementation runs stopped before producing a
certificate (mixed interval type dispatch and a zero-norm lower
endpoint); neither is used as mathematical evidence. The nonrigorous
root/contour diagnostic is preserved separately and is not an input.

### 4. Local noncancellation and the uniform finite-product integral

For l=2m=2n/3 the coefficient contour and (6) give exactly

    b_(2m)=(1/(2*pi))*integral_0^(2*pi)
       exp(n*h(t,u))*A(v(z(t,u)),u)*z'(t,u)*(1+O(1/n)) dt. (16)

The O(1/n) is uniform on this contour. There is no loss from the
imaginary part of z: it is included in h. Since n=3m, exp(n*H)
has the required period 2*pi. No fractional Fourier index is used.

On the local interval, integrating (10) twice from t_s shows

    Re(h(t,u)-h(t_s,u)) <= -(t-t_s)^2/40.                 (17)

Every point outside |t-t_s|<.19 either is still in this local interval
or lies in a cell covered by (11). Its phase is therefore smaller
than the saddle phase by one fixed positive amount, uniformly in u.
Indeed local points have loss at least .19^2/40; complementary cells
have loss at least .001. This treats all endpoints, competing regions
and any other stationary points without asserting that they do not
exist. The corresponding part of (16), after division by
exp(n*h(t_s))/sqrt(n), tends to zero uniformly and exponentially.

On |t-t_s|<.19 put y=sqrt(n)*(t-t_s). All derivatives on a fixed
neighborhood are uniformly bounded, by Section 1 and compactness.
Taylor's formula yields

    n*(h(t_s+y/sqrt(n),u)-h(t_s,u))
        =-a_s*y^2/2+O(|y|^3/sqrt(n))                    (18)

on bounded y intervals, uniformly in u. The amplitude converges
uniformly there to A_s*z'_s, where A_s=A(v(z_s),u).
The absolute integrand is bounded by a fixed multiple of exp(-y^2/40)
by (17). Split at a fixed |y|<=L, apply the uniform Taylor estimate
there, and bound both tails by this integrable majorant; then let
L tend to infinity. This proves the uniform, signed asymptotic

    b_(2m)= exp(n*H(z_s,u))/(2*pi*sqrt(n))
                *[A_s*z'_s*G(a_s)+o(1)],
    G(a)=integral_R exp(-a*y^2/2) dy.                    (19)

Here no cancellation is suppressed in passing to the limit. To show
that the limiting factor is nonzero, write a=alpha+i*beta. For (13),
cos v>=1-v^2/2 and two integrations by parts give

    Re G(a)
      >= integral_R exp(-alpha*y^2/2)*(1-beta^2*y^4/8) dy
      = (1-3*beta^2/(8*alpha^2))
                          *integral_R exp(-alpha*y^2/2) dy
      >= (29/54)*integral_R exp(-alpha*y^2/2) dy > 1/2.   (20)

The integrations by parts have zero Gaussian boundary terms;
integral y^4 exp(-alpha*y^2/2)=3*alpha^(-2)*integral exp(-alpha*y^2/2).
Also the latter integral is at least 2*exp(-.11)>1, since alpha<.22.
These elementary moment bounds prove precisely the nonvanishing needed
in (19); no general Gaussian formula or phase convention is assumed.

The continuous factor A_s is uniformly bounded away from zero, and
|z'_s|>=1. Thus |A_s*z'_s*G(a_s)| has a uniform positive lower bound.
The uniform o(1) in (19) cannot cancel it past a single onset. Combining
this with Re H(z_s)>.005 proves the first inequality of (1).

For b_0 use the same deformed coefficient contour, (6), bounded
amplitude and length, and (12). The absolute contour bound gives
|b_0|<=C*exp(-.06*n). It is exponentially smaller than the first
alias. The reverse triangle inequality proves the last part of (1).

### 5. Complete alias sum and angular norm

C645v gives

    S_m=(1/m)*sum_k W_n(a_k,u)=b_0-2*b_(2m)+E_m,
    |E_m|<=4*exp(-.084*n),
    ||H_q_u|| >= (m/R)*|S_m|.                            (21)

The error in (21) is exponentially smaller than (1), uniformly on
the fixed sector. Thus |S_m|>=c*n^(-1/2)*exp(n/200) beyond one
onset. Since m=n/3 this gives the first inequality of (2). Integrating
its square over the fixed sector, whose normalized measure is
epsilon/pi, proves the second. The change u=i*exp(i*theta) preserves
angular measure. Constants absorb the fixed factor sqrt(epsilon/pi).

This addresses the saved leading-term test with a strict margin and
the whole alias error. It does not extend the geometry to varying
radii or arbitrary line measures, or provide an actual-Xi upper bound.

### Separate conceptual audit — 2 November 2026

STEP_ID: 2026-11-02-oblique-saddle-audit-01. This is verification of
the existing quantitative result, classified REPRODUCTION, not a new
lower bound or a claim of originality. The unchanged angular assessment
covers the exact hypotheses and the Fourier/residue technique. The
complete C645v proof and its certificate generator were checked as
load-bearing inputs. C645g was used only for normalization, C645l
only for its exact identity (23), and C645t only for admissibility.
The old fixed-grid and partial-input bounds were not used as premises.

**Branches and exact product.** The stated strip bounds give |v|>1,
|v|<U and |(v-x)/x|<1 with strict margins. Thus all five logarithms
in (4) use convergent power-series branches on a common neighborhood,
and exponentiating their sum gives the exact rational factors,
including j=0. Differentiating J(w) gives
J'(w)=log(1-w)/w^2+1/w, with its removable value at zero; substitution
reproduces both derivatives in (7). The endpoint correction in (5)
has the sign (f(0)-f(1))/2 for the left grid j=0,...,n-1.
Uniform bounds for f_ss give the stated complex O(1/n), and A is an
exponential on a compact set, hence uniformly nonzero. The extended
u rectangle is used to enclose the analytic formulas; its off-circle
points are not interpreted as physical conjugate-angle disk factors.

**Outward arithmetic and complete replay.** The decimal operations
in I and C were checked against interval inclusion: addition,
multiplication, reciprocal and square root are enlarged at each step;
denominators exclude zero. The quadrant reduction retains interval pi,
and its asserted |y|<1 makes the full 20-term trigonometric and
hyperbolic tails smaller than 2/40!. The midpoint series uses the full
120-term logarithm/J tails and disk derivative bounds (14).
One must also check that a rounded midpoint stays in that q disk:
the separate replay verifies both rectangle containment and disk
containment for all 9,289 logarithm/J calls. Its generated certificate
is byte-identical to the original. All q<.9, reduction and denominator
assertions execute; no floating-point diagnostic is imported.

Reproduce the complete audit with

    python3 scripts/one-sided-hankel/oblique-alias-tail-certificate.py
    python3 scripts/one-sided-hankel/oblique-saddle-audit.py

The second command saves all replayed saddle cells in
`scripts/one-sided-hankel/oblique-leading-saddle-audit-replay.json`
and the 20 audit comparisons in
`scripts/one-sided-hankel/oblique-saddle-audit.json`.
All 12 original saddle comparisons and 16 original tail comparisons
pass; all failure lists are empty. Both original failed certificates
remain untouched. The additional audit is reproducible verification,
not a replacement for the analytic argument.

**Saddle and contour coverage.** The bounds in (8) really imply a
contraction on the closed complex disk: the derivative bound integrates
on straight segments and the image radius is <.000175028<.0002.
Uniform convergence of its iterates gives a continuous saddle over the
closed angular sector. The kappa enclosure is positive, avoids the
zero of sin(t_s), and makes (9) pass exactly through that saddle.
The contour remains in the pole-free strip, has unchanged endpoints,
and its radial lambda parametrization has positive winding one.
The audit checks the union of every closed cell, not sampled phases:
1,024 global cells cover [0,2*pi]; all 66 cells not tagged outside are
within the 32-cell local curvature cover. The P derivative correction
is +(2/3)*kappa*cos(t), with the sign used in the generator.
The complete extrema are exactly the ones rounded outward in (15).

**Signed localization and uniform onset.** Since |t_s-Re(z_*)|<=.0002,
the moving radius-.19 interval stays in the radius-.21 curvature
interval. Its complement has loss at least the minimum of .19^2/40
and .001, by the local estimate and the complete complementary cover.
Multiplying the uniform product expansion by the Fourier factor and
z' gives (16) without an omitted Jacobian; n=3m makes its index an
integer. On bounded rescaled y intervals the Taylor error is uniform,
and exp(-y^2/40) dominates the entire expanding local interval. The
bounded-interval/tail argument therefore gives a uniform *complex*
limit, not merely an absolute upper estimate. At the exact saddle
the H' z'' term vanishes, so the certified Gaussian enclosure is the
correct one. The integrations by parts in (20) give the ratio 3/alpha^2;
alpha>.18 and |beta|<.20 give 1-3*beta^2/(8*alpha^2)>=29/54.
Together with the lower bounds for |A_s| and |z'_s| this prevents
leading-term cancellation uniformly and supplies a single onset.

Finally, (12) bounds the entire b_0 contour. The complete C645v
remainder has rate .084, so both remainders are negligible relative
to n^(-1/2) exp(n/200). The factor m/R and the fixed sector measure
epsilon/pi are retained in (2). No effective onset, other radius,
general pole family, source-manuscript audit or actual-Xi implication
has been established. The argument and its direct DAG inputs did not
change in this audit.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
The supporting mathematics is elementary complex contour integration,
contraction on a closed disk, finite-product trapezoid estimates,
uniform localized integration, Gaussian moment integration by parts,
and outward interval arithmetic. No Mathlib theorem is asserted to
contain this evaluated sector, curved contour or quantitative bound.

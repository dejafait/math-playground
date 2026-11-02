# Lemma 673: phase-aligned nonnegative interpolation at rate 1/200

## Hypotheses

Use L666's exact angular family. For an integer q>=1 put

    n=12q+3, M=4q+1, h=27/(10n), rho=h/10,
    x=-d=-5/4, R=11/8, U=121/64, t_j=j/n (0<=j<n),
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),                  |u|=1.

For 0<=k<2q let s_k be the unique solution in (k+1/2,k+5/8) of

    s_k=k+1/2+atan(1/(10*s_k))/pi,                     (1)

and set y_k=h*s_k. Choose the symmetric displacement vector

    e_k=s_k-(k+1/2), e_(-k-1)=-e_k,
    Z={x} union {x+i*y_k, x-i*y_k:0<=k<2q}.

All original residues remain one. Define the auxiliary affine distance
with normalized angular measure by

    kappa_e=inf_(b_a real, b_a>=0)
                  ||1+sum_(a in Z\{x}) b_a W_a||_2.

No mass bound is imposed on these auxiliary coefficients. The rational
products, the j=0 factor, and the denominator angle 1/u are retained.

## Conclusion

The specified displacements are admissible. There are explicit positive,
angle-independent coefficients b_a, equal at conjugate nodes, such that

    ||1+sum_(a!=x) b_a W_a||_infinity
           <=14*exp(18)*n^2*exp(-n/200).                (2)

In particular kappa_e is at most the right side of (2). This proves
exponentially accurate nonnegative approximants for one allowed sequence.
It does NOT decide the approved rate-1/100 lower bound for every
displacement vector. Rate 1/200 is smaller than 1/100. The upper bound
(2) is compatible with kappa_e>=exp(-n/100)*n^(-C); it supplies no
countersequence passing the required logarithmic discriminator.

This is a family-specific partial result under the invocation-start
EXPLORE assessment `drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
No matching theorem was identified in that bounded comparison; certified
originality is not claimed. A separate conceptual audit on 2 November
2026 verified the proof and replayed all exact arithmetic; see section 6.
There is no upper bound here for the actual unit-residue c_0, G or H,
nor a Xi realization or mixed-sign conclusion.

## Proof

### 1. Exact admissible nodes and signs

For v>0 the derivative of
v-(k+1/2)-atan(1/(10v))/pi is

    1+10/[pi*(1+100*v^2)]>0.

Its value at k+1/2 is negative. At k+5/8 it is positive, since
atan(1/(10v))/pi<1/(10*pi*v)<=1/(5*pi)<1/8 there.
Continuity and strict monotonicity give the unique solution (1).
Thus 0<e_k<1/8. The nodes are distinct and nonzero, are symmetrically
paired, and are precisely a permitted L666 displacement vector.
In particular 0<y_k<h*(2q-3/8)<9/20.

Put

    P(z)=product_(0<=k<2q)(z^2+y_k^2),
    ell_k=P(0)/[(-i*y_k)*P'(i*y_k)]
          =(1/2) product_(l!=k) y_l^2/(y_l^2-y_k^2),
    c=10*pi/27, gamma=3/5,
    g_n(z)=(1-z/rho)*exp(-c*n*z-gamma*n*z^2).           (3)

Exactly k factors in the denominator of ell_k are negative. Hence
ell_k is real with sign (-1)^k; its magnitude is nonzero. The Lagrange
weight at -i*y_k is the same number, since P is even. Also g_n(0)=1.
For y_k>0, c*n*y_k=pi*s_k and

    pi*s_k+atan(y_k/rho)
      =pi*(k+1/2)+atan(1/(10*s_k))+atan(10*s_k)
      =pi*(k+1).

Here atan(t)+atan(1/t)=pi/2 for t>0. The quadratic exponential is
positive real at i*y_k. Consequently

    g_n(i*y_k)=(-1)^(k+1)*sqrt(1+100*s_k^2)
                                    *exp(gamma*n*y_k^2),
    g_n(-i*y_k)=g_n(i*y_k).

It follows that lambda_(+k)=lambda_(-k)=ell_k*g_n(i*y_k)<0. Set

    b_(x+i*y_k)=b_(x-i*y_k)
       =|ell_k|*sqrt(1+100*s_k^2)*exp(gamma*n*y_k^2)>0. (4)

These are actual coefficients with no dependence on u. Their size is
unrestricted, as the target permits. This uses a linear zero and changed
nodes; it is not a real-part conversion of L672's complex coefficients.

### 2. Exact remainder and its continuous exponent

Let Gamma be the positively oriented boundary of

    |Re z|<=w=3/50, |Im z|<=Y=1/2.

All nodes +-i*y_k are strictly inside. Throughout this rectangle
Re(x+z)<=-119/100<-1. L666's exact rational identity is

    W_(x+z)(u)=[x/(x+z)] product_(1<=j<n)
       [(x-t_j*u)/(x+z-t_j*u)]
       *[(U*u-t_j*(x+z))/(U*u-t_j*x)].                 (5)

The parameter poles x+z=t_j*u, including the t_0=0 pole, are absent
from the closed rectangle. The denominators U*u-t_j*x are also nonzero.
Thus g_n(z)W_(x+z)(u) is holomorphic there for each |u|=1.

Apply the standard Cauchy residue theorem to this function times
P(0)/(zP(z)). The residue at zero is 1 and the two residues at each
pair of interpolation nodes are minus lambda_(+-k)W_(x+-i*y_k).
Using (4) gives the exact identity

    1+sum_(a!=x) b_a W_a(u)
       =(1/(2*pi*i)) integral_Gamma
                 g_n(z)W_(x+z)(u)*P(0)/[zP(z)] dz.    (6)

This is the same named interpolation remainder used in L672; the new
work is its sign-compatible specialization and quantitative cost.
No general cone projection theorem is reproved or required.

For z=s+i*y on Gamma and r=9/20 define

    F(z,u)=integral_0^1 log|[(x-t*u)/(x+z-t*u)]
                           *[(U*u-t*(x+z))/(U*u-t*x)]| dt,
    K(z)=(10/27) integral_(-r)^r [log|t|-log|z-i*t|] dt,
    E(z,u)=F(z,u)-c*s-gamma*(s^2-y^2)+K(z).

The compact bound used here is

    E(z,u)<=-49171680019/9000000000000<-1/200
                   (z on Gamma, |u|=1).              (7)

The exact certificate and its continuous coverage are given in section 4.
Neither a finite optimizer nor a sampled maximum is a premise of (7).

### 3. Full finite-product and displacement costs

The parameter bounds used in L672's finite-product estimates hold here:
|x+z|<3/2 and Re(x+z)<=-119/100<-29/25. Differentiating the logarithmic
integrand of F with respect to t, the same four denominator bounds give

    |partial_t f(t)|<=4+25/4+96/25+80/41<17.

Comparing each full left cell with its integral therefore gives

    log|W_(x+z)(u)|<=n*F(z,u)+17/2<n*F(z,u)+9.         (8)

This includes the t_0=0 factor. No exponential replacement of W is made.

Write y_k^0=h*(k+1/2) and P_0(z)=product_k(z^2+(y_k^0)^2).
The L672 midpoint calculation remains valid on this narrower rectangle:
every z on Gamma is at distance at least 1/20 from i[-r,r], and
|z-i*t|<1 on that full segment. In detail, r=(2q+1/2)h and monotonicity
of log on each positive cell gives

    log|P_0(0)|<=(1/h) integral_(-r)^r log|t| dt
                                      +1-log(h/2).

The 4q midpoint cells fill [-2qh,2qh]. For log|z-i*t| its derivative
in t has magnitude at most 20, so midpoint error is at most
(4q)*20*h/4<9/2. Extending to [-r,r] lowers this integral because
log|z-i*t|<0. Subtracting and using h=27/(10n) proves

    log|P_0(0)/P_0(z)|<=n*K(z)+log n+6.               (9)

The shifted numerator has only a bounded extra cost. From (1),
e_k<=1/[10*pi*(k+1/2)], so

    log[P(0)/P_0(0)]
       <=2 sum_k e_k/(k+1/2)
       <=[1/(5*pi)] sum_(k>=0) 1/(k+1/2)^2
       <=6/(5*pi)<2/5.

The last sum is at most 6: retain its first term 4, and bound the
remaining decreasing terms by integral_(1/2)^infinity t^(-2) dt=2.
All paths from +-y_k^0 to +-y_k stay in (-r,r). The same derivative
bound 20, together with |y_k-y_k^0|<h/8, gives

    log|P_0(z)|-log|P(z)|<=20*(4q)*h/8<9/4.

Combining with (9) yields, uniformly on the whole contour,

    log|P(0)/P(z)|<=n*K(z)+log n+9.                   (10)

Finally |z|<51/100, rho=27/(100n) and n>=15 imply
|1-z/rho|<=1+17n/9<2n. Combining (7), (8), (10), and the exact
modulus of the exponential in (3), the numerator in (6) is at most

    2*exp(18)*n^2*exp(-n/200).

Gamma has length 56/25 and |z|>=3/50. Its remaining integral factor
is at most 56/(3*pi)<7, using pi>3. This proves (2) for every q>=1.
Normalized angular L2 is no larger than the uniform norm, so the stated
bound on kappa_e follows. All constants and the onset are absolute for
this one constructed displacement sequence.

### 4. Exact compact certificate and complete angular coverage

Reproduce the certificate from the notebook directory with

    python3 scripts/one-sided-hankel/positive-cone-contour-certificate.py

The full artifact is
`scripts/one-sided-hankel/positive-cone-contour-certificate.json`.
It stores all 98,978 rational sample upper bounds, parameters, margins,
and interpolation errors. Its arithmetic uses no floating decisions.
The interval/series helpers are unchanged from L672's separately audited
certificate. Their proofs are in L672 section 3; the changed center,
quadratic term, rectangle and derivative costs are verified here.

Specifically, with S(v)=sum_(k>=1) Re(v^k)/[k*(k+1)] and a=x+z,

    F(z,u)=log(d/|a|)+S(u/a)-S(u/x)
                           +S(x/(U*u))-S(a/(U*u)).

All four arguments have modulus less than 9/10, since
|a|>=119/100>29/25 and |a|<3/2. The same uniform termwise integration,
100-term geometric tail and integer fixed-point error from L672 apply:
rounding is at scale 10^40, each series' roundoff is below 10^(-20),
and the sum of all four roundoff and tail bounds is below 10^(-6).
The rational logarithm and arctangent enclosures use the same respective
32-term atanh and 60-term alternating series with their explicit tails.
For K, use the primitive

    J(s,v)=(v/2)log(s^2+v^2)-v+s*atan(v/s) (s>0),
    J(0,v)=(v/2)log(v^2)-v,
    K(s+i*y)=(10/27)*[2r*(log r-1)
                         -J(|s|,y+r)+J(|s|,y-r)].

No singular primitive value is used at a mesh point. The same Machin
enclosure pi=16*atan(1/5)-4*atan(1/239) gives an interval for c=10*pi/27;
the term -c*s uses signed interval multiplication. The quadratic term
-gamma*(s^2-y^2) is rational and is included before upward rounding to
the stored 10^(-12) sample grid.

Use both rational circle charts

    u=epsilon*(1-v^2)/(1+v^2)+i*2v/(1+v^2),
    -1<=v<=1, epsilon in {-1,1}.

They cover the entire unit circle. Conjugation reduces the contour to
both vertical sides with 0<=y<=1/2 and the upper side. The inherited
analytic derivative estimates, valid on the larger L672 rectangle, are

    |F_yy|, |F_ss|<=625/116+4096/1875<8,
    |F_vv|<35359/435<100.

On a vertical side, |K_yy|<=(10/27)/w=500/81<7; on y=1/2,
|K_ss|<=(10/27)*(20-20/19)=400/57<8. The quadratic contributes
6/5 to either absolute second derivative and the linear center none.
Thus |E_yy|<17 vertically, |E_ss|<18 horizontally, and |E_vv|<100.
The top derivative bound remains valid through s=0, since y-t>=1/20.

The vertical mesh steps are 1/100 in y and 1/240 in v; the upper
mesh steps are 1/50 in s and 1/30 in v. Iterated linear interpolation
in the two coordinates has errors at most

    vertical: (17/8)*(1/100)^2+(100/8)*(1/240)^2=1237/2880000,
    upper:    (18/8)*(1/50)^2+(100/8)*(1/30)^2.

This follows from the one-variable second-derivative error on each cell;
convex interpolation weights add the errors without a mixed-derivative
assumption. Every chart endpoint and contour endpoint is included.
The largest sample upper bound plus its applicable interpolation error
is exactly -49171680019/9000000000000, with strict margin
4171680019/9000000000000 below -1/200. All 218 mesh rows and all
auxiliary rational bounds pass. This proves (7) on the full contour
and full angular circle, not merely at sample points.

The additional consistency check

    python3 scripts/one-sided-hankel/positive-cone-contour-coverage-check.py

reads every saved sample, checks every row's threshold and interpolation
error, enumerates the entire required mesh, recomputes the saved global
maximum, and compares the inherited helper syntax with the preserved
L672 script. Its full report is
`scripts/one-sided-hankel/positive-cone-contour-coverage-check.json`;
all checks pass. This is a complete data/mesh check, not an independent
analytic audit. The floating cone and even-gauge design screens under
`scripts/one-sided-hankel/positive-cone-*-screen.json` are not proof inputs.

### 5. Threshold and scope

There is also a certified limitation of the present absolute contour
estimate. At z=3/50+i/25 and u=(-6391+480i)/6409, the two-sided
interval calculation in the coverage-check script gives

    -736652441/125000000000 <= E(z,u)
                              <= -5893033891/1000000000000.

In particular E(z,u)>-1/100. This uses the same finite series with
both signs of its error, both endpoints of the logarithm/arctangent
intervals, and outward rounding at scale 10^12. The rational u has
unit modulus and is the chart point epsilon=-1, v=3/80. Thus tighter
rounding alone cannot make this unchanged contour and gauge satisfy
E<=-1/100 everywhere. This is a cost obstruction for that sufficient
absolute estimate, not a lower bound on kappa_e or an optimality theorem
over gauges, contours, coefficients, or signed contour integration.

Taking logarithms of (2) gives only

    -log kappa_e-n/100 >= -n/200-2log n-18-log 14,

with the usual convention if kappa_e=0. This lower bound for the excess
tends to minus infinity after division by log n. It gives no conclusion
about whether the actual excess is unbounded above. No uniform lower
bound, sharper asymptotic rate, optimality of a gauge, or counterexample
to the rate-1/100 mechanism is established.

The actual original residues stay one. Formula (4) supplies other
auxiliary coefficients, so an upper bound on their residual does not
upper-bound the actual unit-residue sum, the full spatial polynomial,
or its logarithmic maximum H. L666's conditional Jensen interpretation,
the missing H estimate, general support, Xi realization, and actual
mixed signs remain separate. L672's complex-span stop and the earlier
scalar, Gram and spatial stops retain their stated scope.

### 6. Separate conceptual audit — 2 November 2026, step 39

The audit used the unchanged invocation-start EXPLORE assessment for
the exact cone target. It verifies (2), not the rate-1/100 target, and
imports no additional theorem. Cauchy's residue theorem is the named
standard input; the specializations below require the displayed exact
family and do not assume the other unaudited claims of L666.

The node equation is strictly increasing and changes sign between its
two stated endpoints. These disjoint intervals give ordered positive
ordinates, admissible symmetric shifts and all nodes inside Gamma.
The factor (-i*y_k)P'(i*y_k) is
2*y_k^2*product_(l!=k)(y_l^2-y_k^2), so exactly k factors are negative.
The phase of (1-i*y_k/rho)*exp(-i*c*n*y_k) is exactly -pi*(k+1).
The quadratic factor is positive real at the nodes. Conjugation gives
the same real value at the negative node. Thus every lambda is strictly
negative, and (4) supplies actual positive angle-independent coefficients.
No discarded imaginary part or angle-dependent minimizer enters (6).

In (5), Re(x+z)<-1 excludes every parameter pole for the closed
rectangle and all |u|=1. The entire gauge may vanish at rho; a zero
introduces no pole. At each node the Cauchy integrand's residue is
-ell_k*g_n(+-i*y_k)*W_(x+-i*y_k), while its residue at zero is one.
This checks the positive residual and its orientation in (6).

The finite-n estimates retain the full j=0 cell. The four terms in
the t-derivative bound in (8) use d-t>=1/4,
|x+z|-t>=4/25, U-t*|x+z|>=25/64, and U-t*d>=41/64.
Their sum is less than 17, giving the entire left-sum cost at most
17/2. For (9), r=(2q+1/2)h exactly. The central logarithmic interval
cost is 1-log(h/2); the midpoint cells cover [-2qh,2qh]. Adding the
two endpoint half-cells lowers the denominator integral because
|z-i*t|<1 throughout. Both signs are in the required direction.
The numerator shift costs at most 6/(5*pi)<2/5, and the denominator
shift costs less than 9/4: every displacement path stays in (-r,r),
at distance at least 1/20 from Gamma. Their sum is less than 3,
which justifies (10) for every q>=1. Finally |1-z/rho|<2n,
length(Gamma)=56/25 and min_Gamma |z|=3/50 give the prefactor in (2).
No asymptotic onset or unbounded constant is omitted.

The four series representing F have the displayed signs and arguments
of modulus less than 9/10. The audit checked the fixed-point coordinate
recurrence, flooring of negative values, the weighted summation error,
and the logarithm/arctangent tails described in L672 section 3.
Signed interval multiplication applies also to -c*s; the quadratic is
exact rational arithmetic. The primitive for K is smooth through s=0
on the upper edge because y-t>=1/20, despite its |s| notation.
For the vertical derivative, each endpoint term
(y+-r)/(s^2+(y+-r)^2) has magnitude at most 1/(2|s|), so
|K_yy|<=(10/27)/|s|. Adding 6/5 for the quadratic yields the stated
safe bound 17; the analogous top bound is 18. The inherited angular
bound is valid on both charts, including their endpoints. Iterated
linear interpolation uses convex weights and therefore sums the two
errors without needing mixed derivatives. Conjugation covers the
lower half of the contour. These checks justify continuous coverage,
not merely agreement on the mesh.

Reproduce the separate full replay and audit with

    python3 scripts/one-sided-hankel/positive-cone-contour-audit.py

The full artifacts are
`scripts/one-sided-hankel/positive-cone-contour-audit.json` and
`scripts/one-sided-hankel/positive-cone-contour-audit-replay.json`.
The original certificate is preserved byte for byte. Every replayed
field agrees; all 218 mesh rows and 98,978 sample enclosures were
independently enumerated and checked. The maximum remains
-49171680019/9000000000000, below -1/200 by
4171680019/9000000000000. There are zero failures.
Four additional exact Fraction power sums at the decisive mesh point
obey the fixed-point roundoff bounds. Using those exact partial sums
and both signs of their analytic tails again gives the full interval
[-736652441/125000000000, -5893033891/1000000000000]. Its lower endpoint
exceeds -1/100. These supplementary checks strengthen the replay;
the uniform analytic bounds remain necessary for the continuous result.

Verdict: the positive-cone approximation (2) and the limitation of its
unchanged absolute contour estimate pass this separate informal audit.
No stronger exponent, new theorem, cone lower bound or countersequence
at rate 1/100 is established. The normalized logarithmic discriminator,
original unit-residue response, H, support, Xi realization and signs
remain open. L666 and L672 remain the direct mathematical inputs;
no dependency changes are needed.

## Mathlib

Full matching coverage for this sign-compatible displaced rational
family and its quantitative certificate has not been checked. No
absence claim is made. Cauchy's residue theorem, elementary real
monotonicity, uniform series bounds and norm comparisons support the
argument; supporting formal results alone would not supply the nodal
phase identity or the evaluated continuous rate (7).

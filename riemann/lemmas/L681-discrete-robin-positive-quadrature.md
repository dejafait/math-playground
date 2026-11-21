# Lemma 681: bounded positive Robin-residue quadrature at rate 3/500

## Hypotheses

Use L666's full kernel and exactly L673's phase-aligned nodes. For an
integer q>=1 set

    n=12q+3, h=27/(10*n), rho=h/10, lambda=pi/h,
    x=-d=-5/4, R=11/8, U=121/64, t_j=j/n (0<=j<n).

For 0<=k<2q let s_k be the unique solution in (k+1/2,k+5/8) of

    s_k=k+1/2+atan(1/(10*s_k))/pi,
    y_k=h*s_k, Z={x} union {x+i*y_k,x-i*y_k:0<=k<2q}.

For |u|=1 retain all factors, including j=0, in

    W_a(u)=(x/a)*product_(1<=j<n)
             [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)].

Circle L2 uses normalized angular measure. The coefficients below are
auxiliary nonnegative weights independent of u; original residues in
the notebook's H problem are still one. No total-mass constraint or
exactness for arbitrary constant functions of the parameter is imposed.

## Conclusion

Put C_n=(1+rho*lambda)/rho and assign the same weight to each conjugate
pair:

    w_(x+-i*y_k)=C_n*(rho^2+y_k^2)/(rho+lambda*(rho^2+y_k^2)).       (1)

For every q>=1 these are real and satisfy

    1<w_a<1+10/pi<13/3.

With alpha=3/500, the full continuous bounds are

    ||1+sum_(a!=x) w_a*W_a||_infinity
        <=5*exp(22)*n*exp(-alpha*n),
    ||W_(-R)-1-sum_(a!=x) w_a*W_a||_2
        <=||W_(-R)-1-sum_(a!=x) w_a*W_a||_infinity
        <=6*exp(22)*n*exp(-alpha*n).                              (2)

This is a partial result for the approved prescribed-node target.
The rate 3/500 improves the recorded 1/200 positive baseline but is
strictly below the required 1/100. It proves neither the requested
strictly faster rate nor an obstruction for arbitrary nonnegative
weights. The constant is absolute and the onset is q=1.

The separate conceptual audit in Section 6 verifies this family-specific
partial result, including the complete arithmetic replay. The saved
EXPLORE comparison did not identify a matching theorem; originality is
not certified. No actual unit-residue H estimate, support/realization
bridge, mixed positivity, or RH candidate follows from (2).

## Proof

### 1. Source scope and the exact sampling kernel

The invocation-start assessment was
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
It permits a direct finite-node construction with the anchor and entire
remainder paid. The standard named input is Cauchy's residue theorem
for a meromorphic function on and inside a positively oriented simple
closed contour with finitely many interior poles and no boundary pole:
[NIST DLMF Section 1.10(iv), equation (1.10.8)](https://dlmf.nist.gov/1.10#E8),
with its analytic, continuity and positive-orientation hypotheses, as
inspected in the saved audit assessment on 2 November 2026.
We specialize it to the following kernel; no positive-discretization or
constant-exactness theorem is presumed. L673 supplies the exact nodes,
L666 the exact rational family, L672 the audited series/derivative bounds
used below, and L680 Section 3 the audited parameter-circle attenuation.
The new nodal residues and remainder costs are necessary because those
inputs do not supply this prescribed-node formula or its stated rate.

Define entire D_n and meromorphic K_n by

    D_n(z)=z*cosh(lambda*z)+rho*sinh(lambda*z),
    K_n(z)=C_n*(rho-z)*exp(-lambda*z)/D_n(z).                    (3)

Every zero of D_n is imaginary. Indeed, away from z=-rho, a zero
would imply exp(2*lambda*z)=(rho-z)/(rho+z). If Re z>0, the left
modulus exceeds one and the right modulus is below one; if Re z<0,
the reverse inequalities hold. Neither z=rho nor z=-rho is a zero,
as direct substitution shows.

At z=i*y with y>0, the zero equation is
y*cos(lambda*y)+rho*sin(lambda*y)=0. Its cosine cannot vanish,
so it is equivalent to tan(pi*s)=-10*s, s=y/h. There is exactly
one positive root in each (k+1/2,k+1), k>=0: the left side plus
10*s is strictly increasing from minus infinity to a positive value.
There are no roots in (k,k+1/2), where both terms are nonnegative.
L673's exact phase identity identifies these roots with its s_k; no
rounded root or altered node is used. Negative roots are their negatives.

The zero at zero is simple since D_n'(0)=1+rho*lambda. At a nonzero
root, writing v=rho^2+y^2 and using sin(lambda*y)=-(y/rho)cos(lambda*y),

    D_n'(i*y)=cos(lambda*y)*(rho+lambda*v)/rho,
    (rho-i*y)*exp(-i*lambda*y)=cos(lambda*y)*v/rho.

The derivative is nonzero. Thus the residue of K_n at zero is one,
and its residue at either i*y_k or -i*y_k is exactly (1). In particular

    w_a-1=y_k^2/[rho*(rho+lambda*(rho^2+y_k^2))]>0,
    w_a<C_n/lambda=1+1/(rho*lambda)=1+10/pi<13/3.               (4)

These signs do not depend on u. They do not come from discarding an
imaginary part of a complex interpolation coefficient.

### 2. Finite contour identity and uniform kernel bounds

Let w=7/100, ell=1/8, b=9/20, and

    Y=2*q*h=b-27/(20*n),       9/25<=Y<b.

Take Gamma to be the positive boundary of
-ell<=Re z<=w, |Im z|<=Y. The root count above shows that its
interior poles of K_n are precisely zero and the 4q required nonzero
nodes. On its horizontal sides lambda*Y=2*q*pi; they contain no pole.
There are no nonimaginary poles on its vertical sides. Throughout the
closed rectangle Re(x+z)<=-59/50<-1. Thus W_(x+z)(u) is holomorphic
there for every |u|=1: its possible parameter poles are zero and t_j*u,
all excluded, and |U*u-t_j*x|>=U-d>0. Cauchy's residue theorem gives
the exact, finite identity

    1+sum_(a!=x) w_a*W_a(u)
       =(1/(2*pi*i))*integral_Gamma K_n(z)*W_(x+z)(u) dz.       (5)

No infinite sampling limit or complementary infinite node sum is used.

To bound K_n, put r(z)=(z-rho)/(z+rho). Away from the removable
algebraic exceptional points, (3) becomes

    K_n(z)=-2*C_n*r(z)/(exp(2*lambda*z)+r(z)).

On Re z=w, |r(z)|<1; on Re z=-ell, |r(z)|>1. Consequently

    |K_n(w+i*y)|<=2*C_n/(exp(2*lambda*w)-1),
    |K_n(-ell+i*y)|<=2*C_n/(1-exp(-2*lambda*ell)).

Here C_n/n=(100+10*pi)/27<5. For n>=15,
2*lambda*w=(20*pi/27)*n*w>2, and exp(2)>6 by the first four
positive Taylor terms. Since ell>w, these two bounds are at most
12*n*exp(-2*lambda*w) and 12*n, respectively.

For z=s+i*Y on the upper side, the exact integer phase gives

    |D_n(z)|=cosh(lambda*s)*|s+rho*tanh(lambda*s)+i*Y|
             >=Y*cosh(lambda*s).

Also rho<=9/500 and |rho-s|<=rho+ell. Hence

    |rho-z|/Y<=sqrt(1+(143/1000)^2/(9/25)^2)<6/5,
    exp(-lambda*s)/cosh(lambda*s)=2/(1+exp(2*lambda*s))
                           <=2*exp(-2*lambda*max(s,0)).

The lower side follows by conjugation. We have proved on every edge

    |K_n(z)|<=12*n*exp(-2*lambda*max(Re z,0)).                 (6)

### 3. Complete continuous exponent certificate

For z=s+i*y and a=x+z set

    F(z,u)=integral_0^1 log|[(x-t*u)/(a-t*u)]
                              *[(U*u-t*a)/(U*u-t*x)]| dt,
    E(z,u)=F(z,u)-(20*pi/27)*max(s,0).

We need only the following fixed compact sets:

    E(w+i*y,u)<-3/500     (|y|<=b, |u|=1),
    E(s+i*b,u)<-3/500     (-ell<=s<=w, |u|=1).                 (7)

Throughout the rectangle with height b,
29/25<|a|<3/2. Therefore L672's audited power-series evaluation and
derivative estimates apply with exactly the same denominator margins.
In detail, put S(v)=sum_(k>=1) Re(v^k)/(k*(k+1)). Then

    F(z,u)=log(d/|a|)+S(u/a)-S(u/x)
                         +S(x/(U*u))-S(a/(U*u)).

All four arguments have modulus <9/10. The code reuses the preserved
L673 certificate's audited L672 helpers, stopping before its mesh/output
code. Each series has 100 terms at integer scale 10^40. The bound on
one finite-series rounding error is
[6*((3/2)^100-1)+100]/10^40<10^(-20); its tail is at most
(9/10)^101/[(101*102)*(1/10)]. All four errors of both kinds are
added, totaling <10^(-6). Rational logarithms use 32 atanh-series
terms after scaling into [1,2], with tail 2*z^65/[65*(1-z^2)].
Pi uses the Machin identity and 60-term arctangent enclosures, exactly
as justified in L672. Signed interval multiplication is used for the
linear term -(20*pi/27)*max(s,0). No floating value enters a bound.

Use both full circle charts

    u=epsilon*(1-v^2)/(1+v^2)+i*2*v/(1+v^2),
    -1<=v<=1, epsilon in {-1,1}.

L672's proof, which uses only 29/25<|a|<3/2 and the same x,U,
gives

    |F_yy|, |F_ss|<=625/116+4096/1875<8,
    |F_vv|<35359/435<100.                                    (8)

The linear subtraction in E has zero second derivative on each side
of s=0. On the right edge use y=j/200, 0<=j<=90, and v-step
1/300. On the upper edge use s=j/200, -25<=j<=14, and v-step
1/50. The node s=0 is included, so no interpolation cell crosses
the kink of max(s,0). Conjugation covers negative y and the lower edge.
The one-variable linear-interpolation error, applied successively with
convex weights, is at most

    right: (8/8)*(1/200)^2+(100/8)*(1/300)^2,
    top:   (8/8)*(1/200)^2+(100/8)*(1/50)^2.

Mixed derivatives are not required. The complete certificate evaluates
every mesh point with the stated tails, rounds upper bounds upward to
10^(-12), and adds the appropriate interpolation cost. Its maximum is

    -546306841/90000000000
       =-3/500-6306841/90000000000 < -3/500.                   (9)

All 117,462 samples in 262 rows and all auxiliary rational checks pass.
Every chart and contour endpoint is included. Thus (9) and (8) establish
(7) on the full continuous sets, not just on a finite angular screen.
Reproduce with

    python3 scripts/one-sided-hankel/discrete-robin-quadrature-certificate.py

The complete certificate, including every sample upper bound, mesh,
interpolation cost, helper-source hash and failure list, is
`scripts/one-sided-hankel/discrete-robin-quadrature-certificate.json`.
The earlier floating screen with the same filename stem ending in
`-screen` is exploratory only and is not a premise of this proof.

### 4. Finite-n, height and parameter-point costs

For the integrand f(t) defining F, uniformly on the height-b rectangle,

    |f'(t)|<=4+25/4+96/25+80/41<17.

This is the same full-product cell estimate as in L672: the four
denominator bounds are d-t>=1/4, |a|-t>4/25,
U-t*|a|>25/64, and U-t*d>=41/64. Integrating the Lipschitz error
over each left Riemann cell gives

    log|W_(x+z)(u)|=sum_(0<=j<n) f(j/n)
                    <=n*F(z,u)+17/2<n*F(z,u)+9.             (10)

The j=0 cell is retained; f(0)=log|x/a|. No truncated product has
been substituted for the original kernel.

At the actual top Y the difference from b is 27/(20*n). For all
intermediate heights, |a|>=59/50 and |a|<3/2, so direct
differentiation under this finite-interval integral gives

    |F_y|<=1/(59/50-1)+1/(U-3/2)=50/9+64/25<9.

Thus replacing F(s+i*Y,u) by F(s+i*b,u) costs less than 243/20
in n*F. Together with (10), the total additive cost is <22.
Equations (6)--(10) therefore bound |K_n*W| on the right and both
horizontal sides by 12*exp(22)*n*exp(-alpha*n).

On the left side a=-R+i*y, so |a|>=R. For 0<=t<1 and |u|=1,

    |U-t*a/u|^2-U*|a-t*u|^2=(U-|a|^2)*(U-t^2)<=0.

Consequently every reciprocal disk factor in W has modulus at most
one and |W_a(u)|<=|B_u(x)|, where B is the full L666 product.
This remains valid at a zero of a numerator in the rational continuation.
L680 Section 3's audited bound gives

    |B_u(x)|<=P_n=(10/11)*(66/67)^(n-1)
                  <=exp(1/67)*exp(-n/67).                    (11)

Since 1/67>alpha, (6) and (11) give the same bound
12*exp(22)*n*exp(-alpha*n) on the left side. Its use here does
not assume L680's continuum sign hypotheses.

The perimeter of Gamma is 2*(w+ell+2*Y)<219/100, and pi>3.
Equation (5) is therefore bounded in modulus by

    [(219/100)*12/(2*pi)]*exp(22)*n*exp(-alpha*n)
       <5*exp(22)*n*exp(-alpha*n).

This proves the first part of (2) uniformly for every |u|=1 and q>=1.
Finally (11) also holds at a=-R. Adding it by the triangle inequality
and using normalized L2<=uniform norm proves the second part of (2).
No angular modes, top edges or normalization costs are omitted.

### 5. Threshold, qualification and continuation

The construction supplies a new explicit set of bounded positive weights
on the exact prescribed nodes with anchor coefficient one. It neither
requires nor proves a positive measure exact on a larger test space.
Its exponent 3/500<1/100 leaves the approved strict-rate question open;
the displayed upper bound cannot decide it. The preliminary best sampled
right-edge exponent near -0.006234 is not an optimality theorem, a lower
bound for the residual, or an obstruction for other weights or estimates.
The older fixed-gauge and continuum-sign stops remain as qualified.

The separate audit below verifies (1)--(11) at the stated partial rate.
Any stronger rate needs a materially new estimate or construction;
H/support/realization and actual-Xi signs remain independent gaps.

### 6. Separate conceptual audit — 2 November 2026, step 68

The invocation-start SPECIALIZE assessment was
`drafts/literature/2026-11-02-discrete-robin-quadrature-audit.md`.
This is a REPRODUCTION audit of the existing formula and estimate,
not a stronger rate or a claim of originality. It uses only L666 (6),
L672's series/derivative/finite-product arguments, L673's exact node
definition, and the point attenuation verified in L680 Section 3.
The other claims of those lemmas are not audited here. The fixed-gauge
crossing and finite-polar stops retain their original restricted scopes.

**Poles, weights and exact contour.** Independently substituting the
exponential form of D_n gives the modulus contradiction for every
Re z nonzero. The exceptional points z=+-rho are nonzeros by direct
substitution. On the imaginary axis, tan(pi*s)+10*s is strictly
increasing on each (k+1/2,k+1), from minus infinity to a positive
limit; on (k,k+1/2) it is positive for s>0. Neither endpoint is a
zero. The defining phase equation selects the unique root already
in L673's smaller interval. Since Y/h=2q, the rectangle contains
exactly those 2q positive roots, their negatives, and zero. At each
nonzero root, the displayed derivative in Section 1 is nonzero and
the numerator/derivative quotient equals (1). At zero it is
C_n*rho/(1+rho*lambda)=1. Formula (4) then proves both strict
weight inequalities. These are residues of the meromorphic kernel,
not signs inferred from a numerical root computation.

The full W is analytic near the closed rectangle: Re(x+z)<=-59/50
excludes every parameter pole t_j*u, including zero, and
|U*u-t_j*x|>=U-d=41/64. Its anchor value is exactly W_x=1.
The positively oriented rectangle has no boundary pole; the finite
DLMF residue theorem therefore yields (5) for each circle point.
There is no infinite contour limit, constant-exactness premise or
unsigned replacement of a complex residue in this use.

**All edge estimates.** For r=(z-rho)/(z+rho), its modulus is less
than one on the right and greater than one on the left. Applying
the reverse triangle inequality to exp(2*lambda*z)+r gives the two
distinct vertical bounds in Section 2, including the left edge's
lack of exponential damping. At n=15 the right exponent already
exceeds 2, and exp(2)>19/3>6 makes both prefactors at most 12*n.
On the horizontal edges lambda*Y=2q*pi is exact: cosh(lambda*z)
=cosh(lambda*s) and sinh(lambda*z)=sinh(lambda*s). Thus the
imaginary part of D_n/cosh(lambda*s) has magnitude Y. The worst
rho and Y occur at q=1 and give respectively 9/500 and 9/25;
the numerator ratio squared is at most 150049/129600<(6/5)^2.
Combining with C_n<5*n verifies (6) on the entire contour.

**Series and complete continuous coverage.** On the height-b rectangle,
|a|>=59/50>29/25 and |a|^2<=3349/1600<9/4. Hence all four
series arguments have modulus below 9/10, with the same nonzero
denominator margins used in L672. Uniform absolute convergence
justifies the integrated logarithm series. The preserved helper prefix
was read in full: it performs signed interval multiplication, 32-term
atanh logarithms with their positive tails, 60-term arctangent
enclosures for Machin's pi, and 100-term integer fixed-point sums.
Its read boundary excludes the old mesh and output code. Coordinate
flooring, summand flooring and all four tails obey L672's error proof;
negative signs in the four-series combination do not cancel errors.

The parameter second-derivative bound is 1647011/217500<8; the
angular-chart bound is 35359/435<100. Their proofs depend only on
the verified compact margins, not on the old contour's shape. The
right-edge subtraction is constant in y, and the top subtraction is
linear separately on s<=0 and s>=0. Every top cell lies wholly in
one such interval, including the two cells adjacent to zero. Each of
the two circle charts has |u'|<=2, |u''|<=4 and includes its endpoints.
Tensor-product linear interpolation uses convex weights on the four
corners and adds the two one-dimensional errors; no mixed-derivative
bound is needed. Conjugation supplies the omitted negative heights.

Reproduce the independent replay and arithmetic checks with

    python3 scripts/one-sided-hankel/discrete-robin-quadrature-audit.py

The complete evidence is in
`scripts/one-sided-hankel/discrete-robin-quadrature-audit.json` and
`scripts/one-sided-hankel/discrete-robin-quadrature-audit-replay.json`.
The original certificate and generator are preserved. The replay
matches the entire original certificate, including all 117,462
sample bounds in 262 rows and all 14 auxiliary checks. The independent
cell census checks 108,000 right-edge and 7,800 top-edge cells,
retaining all four corner upper bounds for each cell in the audit
artifact. All 115,800 cells and all 16 audit checks pass, with no
failures. The reconstructed maximum and strict margin are exactly (9).

As an additional check of implementation, seven selected points use
100-term exact rational complex powers without fixed-point flooring.
They include the maximum (s=y=7/100, epsilon=-1, v=17/300), both
charts at s=0, and boundary/chart endpoints. At each point all four
exact sums lie within the proved fixed-point error, and the complete
series enclosure lies below the stored upward-rounded sample bound.
The exact rational values are retained in the audit certificate. These
spot checks supplement the complete replay and analytic error proof;
they are not substituted for them or for continuous interpolation.

**Finite n and the final norm.** The full left Riemann sum contains
f(0)=log|x/a|. Its error is at most 17/2 because on each cell the
integrated distance to its left endpoint is 1/(2*n^2). All four
t-derivative terms sum to 65769/4100<17. The vertical shift
b-Y=27/(20*n) has |F_y|<=1826/225<9 throughout the intervening
strip. Using the looser product error 9 gives total exponent cost
9+243/20=423/20<22, uniformly down to q=1.

On the left edge, expansion of the squared moduli in Section 4 gives
(U-|a|^2)*(U-t^2)<=0. Thus each inverse disk factor has modulus at
most one, including its rationally continued value if its numerator
vanishes. L680's verified 10/11 and 66/67 factor bounds then give
(11), independently of any segment-sign assumption. The same estimate
holds at a=-R; its rate 1/67 exceeds 3/500. The perimeter factor is
strictly below 219/50<5 using pi>3. Finally the triangle inequality
adds at most one further exp(22)*n*exp(-3*n/500), and normalized
angular L2 is at most the uniform norm. This proves both bounds in
(2), with no loss of an edge, anchor, endpoint or finite-n case.

No load-bearing defect was found. The audit verifies the existing
partial construction for every q>=1 and no stronger conclusion.
In particular it neither bounds the best achievable rate from above
nor converts these auxiliary weights to original unit residues.

## Mathlib

Full matching coverage for this prescribed-node Robin-residue formula
and its evaluated exponential bound was not checked; no absence claim
is made. Cauchy's residue theorem, elementary hyperbolic identities,
uniform power-series bounds and norm comparisons are supporting
mathematics. Such support alone does not verify the node specialization,
the exact arithmetic certificate, or the finite-n costs above. Section 6
is an independent informal audit, not a claim of formal verification.

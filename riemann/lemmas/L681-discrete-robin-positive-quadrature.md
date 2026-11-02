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

This family-specific result is not yet independently audited. The saved
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
closed contour with finitely many interior poles and no boundary pole.
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

The next substantive task is independent scrutiny of (1)--(11), especially
the complete nodal census, residue signs, height shift, continuous mesh
coverage and finite-product costs. A successful audit would verify this
partial construction only. Any stronger rate needs a materially new
estimate or construction; H/support/realization and actual-Xi signs
remain independent gaps.

## Mathlib

Full matching coverage for this prescribed-node Robin-residue formula
and its evaluated exponential bound was not checked; no absence claim
is made. Cauchy's residue theorem, elementary hyperbolic identities,
uniform power-series bounds and norm comparisons are supporting
mathematics. Such support alone does not verify the node specialization,
the exact arithmetic certificate, or the finite-n costs above.

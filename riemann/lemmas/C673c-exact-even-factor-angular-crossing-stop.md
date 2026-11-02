# Corollary 673c: an angular crossing barrier for the exact even factor

## Hypotheses

Use L666's full rational angular functions and L673's exact phase nodes:

    q>=1, n=12q+3, h=27/(10n), rho=h/10,
    d=5/4, x=-d, U=121/64, t_j=j/n (0<=j<n),
    W_a(u)=product_(0<=j<n)
        [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    s_k=k+1/2+atan(1/(10*s_k))/pi, 0<=k<2q,
    y_k=h*s_k, Z={x} union {x+-i*y_k}, c=10*pi/27.

The j=0 factor is x/a. The original residues remain one; only auxiliary
nonnegative approximation coefficients will change. Let

    V_n(z)=W_(x+z)(-1),
    S=C \ ((-infinity,-1/4] union [1/4,infinity)),
    D={z: |x+z|>1}.

The square root below is normalized to one at zero. For the contour
obstruction, assume q>=15000 and let Gamma be a positively oriented,
rectifiable Jordan curve with bounded interior Omega satisfying

    {0} union {+-i*y_k:0<=k<2q} subset Omega,
    closure(Omega) subset S intersect D.

These restrictions specify a common branch and pole-free contour class;
they do not assert this class exhausts all finite-n analytic contours.
Define the same continuum functions as in L673, now with r=9/20:

    F(z,u)=integral_0^1 log|[(x-t*u)/(x+z-t*u)]
                           *[(U*u-t*(x+z))/(U*u-t*x)]| dt,
    K(z)=(10/27) integral_(-r)^r [log|t|-log|z-i*t|] dt,
    E_*(z,u)=F(z,u)-(F(z,-1)+F(-z,-1))/2-c*Re(z)+K(z).

The logarithmic integrals also define the values used below on a compact
horizontal band; all F denominators there are checked explicitly.

## Conclusion

The normalized square root A_n(z) of V_n(z)V_n(-z) is holomorphic and
nonzero on S. It is even and positive on the imaginary axis. The gauge

    g_n(z)=(1-z/rho)*exp(-c*n*z)/A_n(z)

therefore preserves L673's exact negative interpolation signs. With

    P(z)=product_(0<=k<2q)(z^2+y_k^2),
    ell_k=(1/2) product_(l!=k) y_l^2/(y_l^2-y_k^2),
    b_(x+i*y_k)=b_(x-i*y_k)
       =|ell_k|*sqrt(1+100*s_k^2)/|V_n(i*y_k)|>0,

the exact continuous-angle identity is

    1+sum_(a!=x)b_a W_a(u)
      =(1/(2*pi*i)) integral_Gamma
           g_n(z)W_(x+z)(u)*P(0)/[z*P(z)] dz.             (1)

Nevertheless, with u_*=(-99+20i)/101, every contour in the stated class
satisfies

    sup_(z in Gamma, |u|=1) E_*(z,u)>-1/500>-1/100.      (2)

Thus this exact even-factor gauge cannot meet the sufficient uniform
absolute-contour criterion E_*<=-1/100, even after changing contour shape
within this class. The gap above that threshold is greater than 1/125.
This is an informative stop for this criterion, not a lower bound on
kappa_e, the finite-n integrand, or the signed integral (1). In particular
no claim that these coefficients themselves fail the cone target follows.
Angular integration, signed cancellation, other gauges or contours, the
unit-residue H application, Xi realization and mixed signs remain open.

This is a family-specific obstruction under the pre-existing EXPLORE
assessment `drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
The bounded source comparison did not identify a matching theorem; it
does not establish originality. This corollary has not had a separate
critical audit. C673a and C673b are comparisons, not premises.

## Proof

### 1. Explicit branch and nonnegative interpolation coefficients

Set alpha_j=1/(d-t_j) and beta_j=t_j/(U-d*t_j). All denominators
are positive, and

    0<alpha_j<4, 0<=beta_j<64/41,
    V_n(z)=product_j (1+beta_j*z)/(1-alpha_j*z).

This retains j=0, where alpha_0=1/d and beta_0=0. Hence

    V_n(z)V_n(-z)=product_j (1-beta_j^2*z^2)/(1-alpha_j^2*z^2).

Every factor 1+-alpha_j*z and 1+-beta_j*z avoids the nonpositive
real axis on S: at a nonreal z its imaginary part is nonzero if its
coefficient is nonzero; at a real z in S, |z|<1/4 makes it positive.
For beta_0=0 the factor is identically one. Using the principal logarithm,
define explicitly

    A_n(z)=exp((1/2) sum_j [Log(1+beta_j*z)+Log(1-beta_j*z)
                           -Log(1+alpha_j*z)-Log(1-alpha_j*z)]).

This is holomorphic, nonvanishing, even, equals one at zero, and squares
to the required product. At z=i*y the logarithms pair by conjugation,
so A_n(i*y) is positive. Since V_n has real coefficients,
A_n(i*y)=|V_n(i*y)|. No unproved square-root branch choice is used.

L673 establishes the admissible nodes, sign(ell_k)=(-1)^k, and

    (1-i*y_k/rho)*exp(-i*c*n*y_k)
             =(-1)^(k+1)*sqrt(1+100*s_k^2).

Division by A_n(i*y_k)>0 preserves that sign. The same value holds
at -i*y_k by conjugation and reality. Thus ell_k*g_n(+-i*y_k)=-b_a
with the positive, angle-independent b_a displayed above. No mass cap
is required by the target.

On a neighborhood of closure(Omega), g_n is holomorphic. Every possible
parameter pole of W_(x+z)(u) requires x+z=t_j*u, hence |x+z|<1;
the angle-only denominators are nonzero since U>d. Therefore the usual
Cauchy residue theorem applies. The residue at zero is one, while
P(0)/[(i*y_k)P'(i*y_k)]=-ell_k, and similarly at -i*y_k. These residues
give (1). This is the named interpolation remainder already used in
L673, with its new gauge applicability checked, not a reproof of a
general approximation or cone theorem.

The exact logarithmic contribution of the new factor is

    log|g_n(z)|=log|1-z/rho|-c*n*Re z
                 -(log|V_n(z)|+log|V_n(-z)|)/2.

Thus the gauge's continuum contribution is precisely the subtraction
in E_*. No finite product is replaced by its continuum exponent in a
claimed norm inequality here. A successful upper bound would additionally
need its full finite-n comparison; the necessary proposed uniform
continuum criterion itself will fail.

### 2. A compact crossing band and its analytic derivative bounds

Put

    y0=3/20, epsilon=1/100000, y_-=y0-epsilon, y_+=y0+epsilon,
    0<=s<=27/100, y_-<=y<=y_+, z=s+i*y, u_*=(-99+20i)/101.

We prove throughout this band that

    E_*(s+i*y,u_*)>=-31639257/25000000000>-1/500.       (3)

Here |u_*|=1 exactly. For a=-d+s+i*y and b=-d-s-i*y, elementary
rational inequalities give

    |a|<126/100, |b|<153/100,
    U-|a|>63/100=:g_a, U-|b|>36/100=:g_b,
    Im(a/u_*)=[20*(d-s)-99*y]/101>47/1000=:delta.

Consequently |a-t*u_*|>delta for every real t. At u=-1 the first
denominators have distance at least y_- for both a and b. The other
denominators have distance at least g_a or g_b, because 0<=t<=1.
All logarithms to be differentiated thus have uniform nonzero arguments.

For either a spatial s or y derivative of F, each variable logarithm
has absolute first derivative at most the reciprocal of its denominator,
or t times that reciprocal. For the second s derivative the respective
bounds are their squares. After integrating t and t^2, write

    A1=1/delta+1/(2*g_a), A2=1/delta^2+1/(3*g_a^2),
    B1=1/y_-+1/(2*g_a), B2=1/y_-^2+1/(3*g_a^2),
    C1=1/y_-+1/(2*g_b), C2=1/y_-^2+1/(3*g_b^2).

These bound F(z,u_*), F(z,-1), and F(-z,-1), respectively. The sign
of the reflected differentiation does not affect an absolute bound.

For s>0 and |y|<r, direct integration gives

    K_ss=(10/27)*[(r-y)/(s^2+(r-y)^2)+(r+y)/(s^2+(r+y)^2)],
    K_y=-(5/27)*log((s^2+(r+y)^2)/(s^2+(r-y)^2)).

The first formula has the stated finite right limit at s=0. Also the
logarithm's argument is less than ((r+y_+)/(r-y_+))^2<5. Using log 5<2,

    |K_y|<10/27,
    |K_ss|<=(10/27)*(1/(r-y_+)+1/(r+y_-))=:K2.

The linear gauge has zero second s derivative and zero y derivative.
The certificate verifies exactly

    |(E_*)_ss|<=A2+(B2+C2)/2+K2<600,
    |(E_*)_y|<=A1+(B1+C1)/2+10/27<40.                (4)

On s>=0, K is continuous up to zero and has the required right
derivatives there; the closed-interval interpolation bound applies to
this restriction. It does not assert two-sided s differentiability
across the nodal segment.

### 3. Complete rational evaluation and continuum coverage

Reproduce the exact certificate from this notebook with

    python3 scripts/one-sided-hankel/positive-cone-exact-even-certificate.py

It writes `scripts/one-sided-hankel/positive-cone-exact-even-certificate.json`,
including all 101 sample enclosures, domain constants, all 15 exact checks,
the complete failure list, and interpolation costs. No floating number
enters an enclosure or pass/fail decision. The resulting failure list
is empty. The analytic justification of the evaluations follows.

For b>=0, define

    J(b,v)=(v/2)*log(b^2+v^2)-v+b*atan(v/b)  (b>0),
    J(0,v)=(v/2)*log(v^2)-v                  (v!=0).

For w=A+i*B, put I(w)=J(|B|,1-A)-J(|B|,-A). Its derivative
formula gives I(w)=integral_0^1 log|w-t| dt on all evaluation inputs.
Those inputs have no singular endpoints; inputs with B=0 have A>1.
For a=x+z, factor the four affine terms to obtain exactly

    F(z,u)=I(x/u)-I(a/u)+(1/2)*log(|a|^2/d^2)
                         +I(U*u/a)-I(U*u/x),
    K(s+i*y)=(10/27)*[2r*(log r-1)-J(|s|,y+r)+J(|s|,y-r)].

All complex coordinates and squared moduli are rational at the sample
points. No convergence condition such as |u/a|<1 is needed for these
integrated-logarithm formulas, including the end of the tested band.

For log v, the script scales v by an integer power of two into [1,2].
With w=(v-1)/(v+1), the first 24 terms of
2*sum_(j>=0) w^(2j+1)/(2j+1) have positive remaining tail at most
2*w^49/[49*(1-w^2)]. The same enclosure for log 2 is added with
the correct signed power. Reciprocal and pi/4 addition formulas reduce
arctangents to arguments of absolute value at most 1/2. The first 32
alternating terms have error at most |v|^65/65. Pi is enclosed by
the classical Machin identity pi=16*atan(1/5)-4*atan(1/239), following
from tangent addition with the quadrant fixed. These series remainders
follow by integration of the finite geometric identities. Interval sums
and signed products are exact rational arithmetic.

At s_j=27*j/10000, 0<=j<=100, y=y0, the computed lower endpoints
are rounded downward to multiples of 10^(-12); upper endpoints are
rounded upward. The smallest lower endpoint is

    min_j lower(E_*(s_j+i*y0,u_*))=-7970507/25000000000.

By the elementary second-derivative linear-interpolation remainder,
the lower error between adjacent sample points is at most

    (600/8)*(27/10000)^2=2187/4000000.

The mean value theorem and (4) add a height cost of at most
40*epsilon=1/2500. Subtraction gives precisely (3). This covers the
whole closed band; a sampled minimum alone is not the evidence for (3).
Only the fixed angle u_* is needed for a lower bound on a supremum over
angles. The floating design artifact
`scripts/one-sided-hankel/positive-cone-exact-even-screen.json` is not a
proof input.

### 4. A node forces every allowed contour to cross the band

For q>=15000 set k=floor(y0/h)=floor(n/18). Then 0<=k<2q,
and |h*(k+1/2)-y0|<=h/2. L673 gives 0<s_k-(k+1/2)<1/8, so

    |y_k-y0|<5*h/8<=9/960016<1/100000.

This uses n>=180003 and is recorded in the exact checks. Thus i*y_k
is a node in Omega with ordinate in the certified band. At the other
end of the horizontal segment,

    |x+27/100+i*y_k|^2<9829030001/10000000000<1,

so 27/100+i*y_k is outside closure(Omega). The connected component
containing zero of {s in [0,27/100]:s+i*y_k in Omega} starts with
a positive interval and ends strictly before 27/100. Its right endpoint
s_* is positive and satisfies s_*+i*y_k in boundary(Omega)=Gamma.
Apply (3) there at u_*. This proves (2), without any convexity,
symmetry, rectangular shape or n-independent-contour assumption.

The result stops the uniform absolute-contour exponent test for this
gauge. It does not lower-bound a signed contour integral, and it does
not claim a finite-n integrand estimate merely from the continuum
exponent. The zero at rho, finite-product errors, oscillatory cancellation,
angular L2 integration, alternative branches outside the stipulated class,
and other approximants cannot be discarded in a stronger conclusion.

## Mathlib

Full matching coverage for this exact even-factor crossing obstruction
has not been checked; no absence claim is made. Supporting principal
logarithm, residue, real differentiation, interpolation-remainder and
elementary series results would not themselves supply the evaluated
band bound or the node-and-contour applicability argument. No formal
verification or independent critical audit is claimed.

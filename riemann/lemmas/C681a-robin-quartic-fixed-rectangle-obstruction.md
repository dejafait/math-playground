# Corollary 681a: even quartic Robin multipliers cannot pass the fixed-rectangle bound

## Hypotheses

Use all of L681's exact definitions: q>=1, n=12q+3,
x=-5/4, U=121/64, h=27/(10n), rho=h/10, lambda=pi/h,
the exact phase-aligned nodes, and the full W_a with j=0 retained.
Let C_n=(1+rho*lambda)/rho and

    K_n(z)=C_n*(rho-z)*exp(-lambda*z)
              /[z*cosh(lambda*z)+rho*sinh(lambda*z)].

Keep L681's rectangle Gamma_n, with left edge Re z=-1/8,
right edge Re z=w=7/100, and heights +-Y, where
Y=2qh=9/20-27/(20n)>=9/25. For any real c2,c4 set

    p(z)=c2*z^2+c4*z^4,
    I_n(z,u)=K_n(z)*exp(-n*p(z))*W_(x+z)(u),   |u|=1.

The coefficients may depend on n, but not on u. Circle norms use
normalized angular measure. The weights in the conclusion are auxiliary;
they do not replace original unit residues in H.

## Conclusion

Multiplying the sampling kernel by exp(-n*p) preserves the unit anchor
and gives positive, angle-independent nonanchor weights

    w_a^(p)=w_a^(681)*exp[n*(c2*y_k^2-c4*y_k^4)]
                 for a=x+-i*y_k.                              (1)

The exact finite residue identity remains

    1+sum_(a!=x) w_a^(p)*W_a(u)
        =(1/(2*pi*i))*integral_(Gamma_n) I_n(z,u) dz.          (2)

Nevertheless, put

    beta=18972432971/2500000000000 < 1/125 < 1/100.

For every q>=1 and every choice of c2,c4,

    sup_(z in Gamma_n, |u|=1) |I_n(z,u)|
                    >=n*exp(-9)*exp(-beta*n).                 (3)

Consequently no choices c2(n),c4(n) give a uniform absolute integrand
bound C*n^k*exp(-alpha*n) on this rectangle for any fixed finite C>0,
k>=0 and alpha>beta, for all sufficiently large q. In particular the
strict rate above 1/100 cannot be obtained by this uniform-integrand
method on the fixed rectangle.

This is an obstruction to a sufficient contour estimate, not a lower
bound for (2), its normalized L2 norm, or the target residual involving
W_(-R). Complex contour cancellation remains possible. Other contours,
other multipliers and arbitrary nonnegative weights are not excluded.
L681's verified rate 3/500 is unchanged. No unit-residue H estimate,
support/realization bridge, actual-Xi positivity or RH candidate follows.
This new obstruction has not received a separate critical audit.

## Proof

### 1. Source scope and preservation of signs

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
It covers this exact family and a sign/normalization/rate obstruction.
L681 supplies the verified sampling kernel and pole census; L672
Section 3 supplies the fully justified rational series enclosures used
below. We reuse the standard finite Cauchy residue theorem cited in
L681: [NIST DLMF Section 1.10(iv), equation (1.10.8)](https://dlmf.nist.gov/1.10#E8).
The meromorphic function has finitely many interior poles, no boundary
pole, and is continuous on the positively oriented boundary. No new
quadrature theorem, asymptotic sampling theorem or optimality theorem
is assumed or reproved. The added work is the coefficient-eliminating
lower bound for this specific kernel.

The multiplier is entire and nonzero, equals one at zero, and has
the positive real value exp[n*(c2*y_k^2-c4*y_k^4)] at either imaginary
node. It introduces no poles and preserves all analytic hypotheses
verified in L681. Multiplying each residue by that value proves (1)
and (2), including the exact anchor. No bound on these new weights
is asserted or needed for the obstruction.

The earlier step-43 quartic search used L673's finite-polynomial
interpolation kernel, with a different continuum exponent, and was
inconclusive. It is not an input to this proof. The present test uses
the new Robin kernel and an exact coefficient identity, not a repeated
finite optimization or a global claim about quartic gauges.

### 2. Three boundary values cancel both coefficients

For z=s+i*y define L681's full-product continuum exponent

    F(z,u)=integral_0^1 log|[(x-t*u)/(x+z-t*u)]
                          *[(U*u-t*(x+z))/(U*u-t*x)]| dt,
    E_0(z,u)=F(z,u)-(20*pi/27)*max(s,0),
    E_p(z,u)=E_0(z,u)-Re p(z).

Select the three points and angular chart values

    z_0=w,       v_0=0,     theta_0=7/9,
    z_1=w+2iw,   v_1=1/9,   theta_1=1/5,
    z_2=w+3iw,   v_2=1/6,   theta_2=1/45,
    u_j=-(1-v_j^2)/(1+v_j^2)+i*2*v_j/(1+v_j^2).

All |u_j|=1. Their heights are 0,7/50,21/100, below 9/25, so
they lie on every Gamma_n. All theta_j are positive and sum to one.
In units of w^2 the real parts of z_j^2 are 1,-3,-8; in units
of w^4 the real parts of z_j^4 are 1,-7,28. Therefore

    sum_j theta_j*Re(z_j^2)=w^2*(7/9-3/5-8/45)=0,
    sum_j theta_j*Re(z_j^4)=w^4*(7/9-7/5+28/45)=0.            (4)

For every real c2,c4, without a size restriction,

    max_j E_p(z_j,u_j)
        >=sum_j theta_j*E_p(z_j,u_j)
         =sum_j theta_j*E_0(z_j,u_j).                         (5)

The angles need not coincide: the uniform integrand estimate under
test ranges over all z and u. They are exact rational circle points,
not approximate angular maximizers.

### 3. Complete rational lower certificate

Write a=x+z and S(v)=sum_(k>=1) Re(v^k)/(k*(k+1)). L672's
uniformly absolutely convergent integrated-logarithm identity is

    F(z,u)=log((5/4)/|a|)+S(u/a)-S(u/x)
                            +S(x/(U*u))-S(a/(U*u)).

At the three points |a|^2 is respectively 3481/2500,353/250,2873/2000.
Thus 29/25<|a|<3/2 and each of the four series arguments has modulus
less than 9/10. L672's 100-term integer fixed-point evaluation at scale
10^40 has error for each finite sum at most

    [6*((3/2)^100-1)+100]/10^40 < 10^(-20),

and the omitted tail is at most

    (9/10)^101 / [(101*102)*(1/10)].

All four errors of each kind are added with both signs accounted for.
Logarithms use the 32-term atanh series after scaling into [1,2],
with positive tail at most 2*t^65/[65*(1-t^2)], t=(v-1)/(v+1).
Pi uses the 60-term alternating arctangent enclosures and Machin
identity justified in L672. The negative coefficient of pi uses
its upper endpoint for a lower bound. Outward rounding at scale
10^12 then gives the following entire intervals for E_0:

| j | Lower numerator / 10^12 | Upper numerator / 10^12 |
|---|---:|---:|
| 0 | -6714671494 | -6714485858 |
| 1 | -9433356991 | -9433171354 |
| 2 | -21590078269 | -21589892632 |

The convex sum of the lower endpoints is exactly

    -18972432971/2500000000000=-beta > -1/125.                 (6)

Reproduce the complete exact arithmetic with

    python3 scripts/one-sided-hankel/robin-quartic-three-point-certificate.py

The certificate is
`scripts/one-sided-hankel/robin-quartic-three-point-certificate.json`.
It retains all rational arguments, fixed partial sums, full logarithm
and pi intervals, series errors, full enclosures before rounding,
coefficient cancellations, source hash and every check. All thirteen checks
pass with no failures. At all three points a separate exact rational-power
evaluation of all four finite series verifies the fixed-point error bound
and the nesting of its full enclosure. An initial lower bound -7/1000 was
not certified by these points; that failed stronger test is retained
explicitly. The actual bound (6), not the failed threshold, is used.
There is no mesh interpolation or omitted continuous range: three
point values suffice for the universal coefficient inequality (5).

### 4. A finite-n integrand lower bound

L681's algebraic form, for r(z)=(z-rho)/(z+rho), is

    K_n(z)=-2*C_n*r(z)/(exp(2*lambda*z)+r(z)).

On Re z=w, since 0<rho<=9/500<w,

    13/22=(w-9/500)/(w+9/500)
          <=(w-rho)/(w+rho)<=|r(z)|<1.

The denominator's modulus is at most exp(2*lambda*w)+1,
which is at most 2*exp(2*lambda*w). Also

    (C_n/n)*(13/22) > (100/27)*(13/22)=650/297>1.

There is no zero or pole of K_n on this edge. It follows that

    |K_n(z)| >= n*exp(-2*lambda*w).                          (7)

For the integrand f(t) defining F, L681's four denominator margins
give |f'(t)|<17 throughout this compact rectangle. In particular
every factor is nonzero. On each left Riemann cell the integrated
distance from its left endpoint is 1/(2*n^2), so the two-sided error is

    |log|W_(x+z)(u)|-n*F(z,u)| <=17/2 <9.                  (8)

This retains t_0=0 and the factor x/(x+z); it is a bound for the
full W, not its truncated exponential surrogate. The same proof used
for L681's upper estimate supplies the lower side of (8).

Combining (7), (8) and the exact modulus of the multiplier gives,
at each selected point,

    |I_n(z_j,u_j)| >= n*exp(-9)*exp(n*E_p(z_j,u_j)).

Equations (5)--(6) prove (3). Everything is uniform for q>=1 and
independent of c2,c4, including if they vary with n. Were the stated
uniform upper bound with alpha>beta true, (3) would force

    exp((alpha-beta)*n) <= C*exp(9)*n^(k-1)

along n=12q+3, which is impossible as q tends to infinity. This proves
the claimed sufficient-estimate obstruction. No lower estimate for a
complex contour integral has been inferred from a large integrand.

## Mathlib

Full matching coverage for this three-point Robin/quartic obstruction
was not checked; no absence or novelty claim is made. The standard
residue theorem, finite convex averages, convergent logarithm series,
and elementary norm/absolute-value estimates are supporting inputs.
The exact rational certificate and informal argument are not a formal
Mathlib verification and have not received a separate critical audit.

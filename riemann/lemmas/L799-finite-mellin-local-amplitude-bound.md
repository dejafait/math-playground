# Lemma 799: a uniform finite Mellin local-amplitude bound

## Hypotheses

Use the domain and saddle of L797 and the phase and branches of L798:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    c=9/4, F(z)=z(pi exp(2z)-c), x=x(s)=u+ih, F(x)=s,
    Q=pi exp(2u), d=3/(16u),
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z),
    A=2F'(x)/x, B=|A|, theta=Arg A, a=exp(-i theta/2).

Here Log, Arg and square roots are principal. L797 gives, on all D,
u>3, |h|<pi/4-1/(4u), Re A>0, and pi exp(6)>1000.
L798 gives B<(2801/600)Q, the denominator identity
|sqrt(2pi/A)|=sqrt(2pi/B)>0, and

    Re(S_s(x+av)-S_s(x)) <= -(85/48)Q v^2, |v|<=d.

Define the complex series on U={z: |Im z|<pi/4} by

    P(z)=sum_{n>=1} [4pi^2 n^4 exp(9z/2)
                     -6pi n^2 exp(5z/2)] exp(-pi n^2 exp(2z)),
    H(z)=4pi^2 exp(9z/2-pi exp(2z)), rho(z)=P(z)/H(z)-1,
    eta(u)=(1/2)exp(-2u+3/(8u))+20exp(-3Q/(5u)),
    T_amp(s)=a integral_{-d}^{d}
                  exp(S_s(x+av)-S_s(x))rho(x+av) dv.

Convergence of the defining series is proved below. For real z>=0 it
is K/2 in L019. In particular no complex positivity of that real kernel
is assumed.

This is the approved operational test in
`drafts/literature/2026-11-05-mellin-finite-amplitude-audit.md`.
It reproduces the finite local amplitude allowance from bramble_trace,
*A continuum certificate for the decreasing Levy factor associated with
Riemann xi*, [paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section2 (1), Section3 Lemma2 (10)–(14), using the
longer diameter in the author's 18 October 2026, 12:27:38 UTC
[post20 revision](https://rstation.ai/r/riemann_hypothesis/posts/20).
Neither the source's theta-parameter inequality nor its amplitude
allowance is assumed.

## Conclusion

P is holomorphic on U. For every s in D and every real |v|<=d,
with z=x+av,

    Re(pi exp(2z)) > (9009/44800)Q/u > Q/(5u) > 1,       (1)
    |rho(z)| < eta(u).                                 (2)

Consequently the normalized finite amplitude satisfies

    |T_amp(s)|/|sqrt(2pi/A)|
       < sqrt(2801/2125) eta(u)
       < (23/20)eta(u) < (31/25)eta(u).                 (3)

This proves the specified cost <=1.24eta, with a stronger constant,
as a source reproduction. It is not a novelty claim or verification
of the source's full Mellin estimate (11). Step516 completed the proof;
step517's independent conceptual audit below verified it without a
mathematical correction. Omitted Gaussian and global
contour tails, continued endpoint identities, quotient/inversion
estimates, certificates and sufficient actual-Xi signs remain open.

## Proof

### Complex convergence and exact normalization

For z in U,

    Re(pi exp(2z))=pi exp(2 Re z) cos(2 Im z)>0.

On any compact subset E of U its minimum delta is positive, and
exp(9z/2) and exp(5z/2) are bounded. The nth summand of P is therefore
bounded in absolute value by C_E(n^4+n^2)exp(-delta n^2). This majorant
is summable: the ratio of consecutive majorant terms tends to zero,
since its polynomial ratio tends to one and its exponential ratio is
exp(-delta(2n+1)). The Weierstrass M-test and the theorem on locally
uniform limits of holomorphic functions show normal convergence and
holomorphy on U. Every summand is entire; the limit is asserted here
only on U. No interchange at its boundary is used.

H is holomorphic and never zero. Dividing the normally convergent
series by H, term by term, gives exactly

    rho(z)=-(3/(2pi))exp(-2z)
       +sum_{n>=2} [n^4-(3/(2pi))n^2 exp(-2z)]
                      exp(-(n^2-1)pi exp(2z)).         (4)

On the positive real axis the original series is precisely half of
L019's K. On the local disc in L798 the principal Log is defined,
and the required integrand factorization is

    exp(2s Log z) P(z)=4pi^2 exp(S_s(z))(1+rho(z)).      (5)

Thus T_amp uses the prescribed amplitude and leading normalization.
The parameterization z=x+av has dz=a dv; |a|=1. There is no factorial
or extra Jacobian, and no global contour deformation is asserted.

### The theta parameter on the entire rotated diameter

Since Re A>0, |theta|<pi/2. Therefore

    |Im a|=|sin(theta/2)|<1/sqrt(2)<5/7,

where the last inequality follows by squaring: 1/2<25/49.
For |v|<=d the saddle clearance and |a|=1 imply

    Re z >= u-d > 47/16 > 0,
    |Im z| <= |h|+d|Im a|
             < pi/4-1/(4u)+15/(112u)
             = pi/4-13/(112u).                        (6)

This places the whole closed diameter in U. Put y=13/(56u). Since
u>3, we have 0<y<13/168<1/10. Cosine is decreasing on [0,pi/2],
so (6) gives cos(2 Im z)>sin y. The elementary inequalities

    sin y >= y-y^3/6 > (99/100)y,
    exp(-2d) >= 1-2d > 7/8                            (7)

are valid in the indicated ranges. The first follows by integrating
cos t>=1-t^2/2 and using y^2/6<1/600<1/100. The second uses
exp(t)>=1+t and 2d=3/(8u)<1/8. Combining (6)–(7) gives

    Re(pi exp(2z))
       > Q (7/8)(99/100)13/(56u)
       = (9009/44800)Q/u > Q/(5u),                    (8)

since 9009>8960=44800/5. Finally exp(2u)/u is strictly increasing
for u>=3, because its logarithmic derivative is 2-1/u>0. Hence

    Q/(5u) > pi exp(6)/15 > 1000/15 > 1.              (9)

This proves (1) without a pointwise source claim. The margin in (8)
is an explicit rational comparison for all u>3, not a grid estimate.

### The full amplitude correction

First, pi>3 and Re z>=u-d give

    |(3/(2pi))exp(-2z)|
       < (1/2)exp(-2u+2d)
       = (1/2)exp(-2u+3/(8u)).                       (10)

Also Re z>0 implies |(3/(2pi))exp(-2z)|<1/2. Set
tau=Re(pi exp(2z)), which is >Q/(5u)>1 by (1). The absolute value
of the n>=2 sum in (4) is at most sum_{n>=2} b_n, where

    b_n=(n^4+n^2/2)exp(-(n^2-1)tau)>0.

For n>=2 put p=(n+1)/n<=3/2. Since p^2<=p^4,

    ((n+1)^4+(n+1)^2/2)/(n^4+n^2/2) <= p^4 <= 81/16.

Consequently

    b_{n+1}/b_n <= (81/16)exp(-(2n+1)tau)
                  < (81/16)exp(-5) < 1/10.          (11)

For the last inequality, the positive exponential series gives
e>2 and e^2>7, so e^5=e(e^2)^2>98 and
81/(16*98)=81/1568<1/10. This bounds every term of the infinite
tail, rather than stopping at its n=2 term. As b_2=18exp(-3tau),
geometric summation yields

    sum_{n>=2} b_n < 18exp(-3tau)/(1-1/10)
                  =20exp(-3tau) < 20exp(-3Q/(5u)).    (12)

Absolute convergence already proved above justifies the triangle
inequality for the complete series. Adding (10) and (12) proves (2).
No sign of a complex summand is used.

### Paying the normalized finite integral

The diameter is compact inside U and the phase disc from L798, so
the integrand is continuous and the finite integral exists. Apply (2)
and L798's audited phase decrement, retaining |a|=1:

    |T_amp(s)|
       <= eta(u) integral_{-d}^{d} exp(-(85/48)Q v^2) dv
       < eta(u) sqrt(48pi/(85Q)).                    (13)

Only a positive real Gaussian majorant is extended to the real line.
The actual T_amp remains finite; the omitted Gaussian and global
contour portions are not folded into the amplitude allowance.
Divide (13) by the exact denominator sqrt(2pi/B) from L798 to obtain

    |T_amp(s)|/|sqrt(2pi/A)|
       < eta(u) sqrt(24B/(85Q))
       < eta(u) sqrt(2801/2125).                     (14)

Here 24*(2801/600)/85=2801/2125. The final comparison in (3)
is exact:

    2801*400=1120400 < 1124125=2125*529,
    sqrt(2801/2125)<23/20<31/25.

All estimates use strict saddle inequalities valid at every point
of the closed D, including |s|=6000 and its curved left boundary.
Absolute values in (6) cover both signs of h, as well as h=0.
There is no upper restriction on u, no limiting argument at infinity,
and no extension of real kernel positivity to complex arguments.
The proof establishes only the stated finite amplitude cost.

The effective source estimate was rederived because the inspected
source outline did not give this full uniform complex-series argument;
the reused SPECIALIZE assessment authorizes precisely that verification.
No fixed-data saddle asymptotic or uninspected supplement supplies any
of the constants above.

### Independent conceptual audit, 5 November 2026 — step517

The unchanged SPECIALIZE assessment named above covers this exact
finite T_amp test. The following independent checks validate (1)–(3)
with no additional hypothesis or mathematical repair. This removes
the pending-review qualification only for the stated local source
reproduction; it establishes no result beyond the sources checked.

**Convergence and normalization.** For any compact E inside U, the
continuous positive function Re(pi exp(2z)) has a positive minimum.
The resulting polynomial-times-Gaussian majorant is summable. Thus
normal convergence holds locally, although U is unbounded and no
single positive minimum on U is claimed. Since H has no zero,
division preserves local uniform convergence. Recomputing the
coefficient of n=1 gives 1-(3/(2pi))exp(-2z), and the exponent
remaining for n>=2 is exactly -(n^2-1)pi exp(2z). This verifies (4)
and the real normalization P=K/2 from L019. The right-half-plane
disc from L798 permits the principal Log in (5); multiplying the
factors gives precisely S_s, with the constant 4pi^2 outside.
The rotated-diameter derivative is dz/dv=a, not its conjugate;
|a|=1 is used only after taking the integral's absolute value.

**Strip margin and all parameters.** The imported Re A>0 places
theta in (-pi/2,pi/2), so |Im a|<1/sqrt(2)<5/7. Combining it
with L797's strict clearance gives 13/(112u) of clearance for
the whole closed diameter, while Re z>=u-d>47/16. Since
0<13/(56u)<1/10, the sine lower bound and exp(-2d)>7/8
apply simultaneously. The product is 9009/44800, exceeding 1/5
by 49/44800. Monotonicity of exp(2u)/u on u>=3 and L797's
pi exp(6)>1000 then verify the strict tau>Q/(5u)>1 needed
for the tail. No fixed positive strip margin as u tends to infinity
is required: these are pointwise inequalities for every u>3, with
the displayed constants uniform over that entire range.

**Complete theta tail.** The n=1 correction has coefficient
3/(2pi)<1/2; its modulus uses exp(-2 Re z), rather than
exp(-2z) as a real quantity. For n>=2, replacing the coefficient
modulus by n^4+n^2/2 is valid because Re z>0. If p=(n+1)/n,
the polynomial ratio is a positive weighted average of p^4 and
p^2, hence is <=p^4<=81/16. The exponential ratio is
exp(-(2n+1)tau)<exp(-5). As e^5>98, their product is
<81/1568<1/10. Therefore the complete positive majorant sums
to less than 18exp(-3tau)/(9/10)=20exp(-3tau).
Together with the separate n=1 term this proves (2) for every
point on the diameter. Continuity and compactness also give
sup_{|v|<=d}|rho(x+av)|<eta(u) for each fixed s, if a supremum
form is desired; no maximum over all of D is asserted.

**Normalized integral and scope.** L798's decrement and upper
curvature bound concern exactly this x, d and a, on the same D.
The phase majorant is exp(-(85/48)Qv^2). Its integral over the
real line is sqrt(48pi/(85Q)); dividing by the principal-root
modulus sqrt(2pi/B) gives sqrt(24B/(85Q)). Substitution of
B<(2801/600)Q gives sqrt(2801/2125). Recomputing the final
squares gives 2125*529-2801*400=3725>0, so this is strictly
less than 23/20 and hence 31/25. Extension to the real line
occurs only for the nonnegative majorant; it does not assert a
global contour identity or pay the omitted finite-Gaussian error.

L797's strict hypotheses hold on both closed boundaries of D.
Absolute values cover h>0, h<0 and h=0 directly. All constants
above apply without an upper cutoff on u, a grid or a boundary
limit. The existing direct mathematical inputs L019, L797 and
L798 are exactly those used, so no DAG change is necessary.
No numerical script, uninspected supplement or extra source claim
was needed. Gaussian/global tails, continued endpoints, quotient
and inversion estimates, certificates and sufficient Xi signs remain
outside this result.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
The proof uses the Weierstrass M-test, local uniform convergence of
holomorphic functions, elementary exponential/trigonometric bounds,
geometric summation and the real Gaussian integral, after L019,
L797 and L798. No specific Mathlib declaration or formal verification
is asserted.

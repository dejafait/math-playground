# Lemma 457: lower-band uniform moving-saddle margin

## Hypotheses

Assume the zeta specialization of OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
Theorem 1.1, at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Retain the [external-input register's precise citation and qualifications](../foundations/2026-10-quasi-riemann-input.md):
the pole at 1 is allowed, the boundary is not excluded, and the
manuscript and formal import closure have not been independently
audited here. The assertions below are conditional on this premise.

Use the exact L456 coupled domain: r tends to infinity through
positive reals, m is a positive even integer, and

    7/8 <= alpha=m/r <= 31/32,
    c=m/(2r), sigma=1/2+c, h=9/2+c,
    a=sqrt(4*pi^2*exp(4r)-h^2)>0, A=m!/(2r)^m,
    S=S_{r,m}=sum_{j,k>=1}(jk)^(-1/2)
             (1-log(jk)/(2r))_+^m exp(ia log(k/j)),
    B=|zeta(sigma+ia)|^2.

The sum is finite, with zero weight also at jk=exp(2r). All vertical
contours below are oriented upward. Constants are independent of r,m
on the entire closed band; their values and the common onset are
not numerically evaluated.

## Conclusion

Put N=m+1, x0=N/(2r), and d=1/4096. For every sufficiently large
r there is a unique real stationary point x* in [x0-d,x0+d] of

    H(x)=2rx-N log x+log|zeta(1/2+x+ia)|^2.

It satisfies, uniformly,

    |x*-x0|=O(r^(-1/3)),  2r <= lambda:=H''(x*) <= 8r.

The positive quantity

    M*=A exp(2rx*) (x*)^(-N)
                 |zeta(1/2+x*+ia)|^2 / sqrt(2*pi*lambda)

obeys

    |log M*| <= C r^(2/3),
    S/M* = 1+O((log r)^3/sqrt(r)).                    (1)

In particular, after enlarging C and one common onset,

    S >= exp(-C r^(2/3)) = exp(-o(r)) > 0             (2)

uniformly on the full closed band. Both original residues and the
entire deformed contour are included in (1). No assertion S/B -> 1
is made. This is a local reproduction/specialization of the assessed
saddle method, not a claim of originality. The separate critical audit
below validates the result and its inherited L456 disk and inversion
inputs, conditional on the unchanged external premise.

This arithmetic margin supplies no changed-band theta-sector reduction,
every-height Laguerre transfer, initial-index completion, bounded-height
extension, global mixed positivity, zero exclusion or RH resolution.

## Proof

The unchanged, prior [moving-saddle coverage](../drafts/literature/2026-10-23-lower-band-moving-saddle-coverage.md)
authorizes this application. The inspected source mechanism is
[DLMF 2.4(iii)--(iv), equations 2.4.10--2.4.16](https://dlmf.nist.gov/2.4#iii),
including the two half-path proof and simple-saddle branch rule, and
N. M. Temme, *Uniform Asymptotic Methods for Integrals*,
[arXiv:1308.1547v1](https://arxiv.org/html/1308.1547v1), Sections
2.2--2.3, (2.9)--(2.13), and Section 4.1, (4.1)--(4.5).
Those sources do not assert parameter uniformity for this integrand.
The following estimates establish the required specialization directly;
no general saddle theorem or arithmetic positivity theorem is reproved.
L331 motivates the local criterion, but its endpoint-domain conclusion
is not applied with changed parameters. The direct local inputs are
L456's complete logarithm disk and exact contour identity, and L452's
all-height growth formula. L303/L330/L454 are method precedents already
incorporated into those inputs.

### 1. Reserved disks, real saddle and uniform derivatives

Uniformly on the coupled domain,

    log a=2r+log(2*pi)+O(exp(-4r)),
    7/16 <= c <= 31/64, x0=c+1/(2r).

L456's proof constructs an Euler-normalized analytic logarithm f_t of
zeta on a neighborhood of the radius-273/256 closed disk about 2+it,
and bounds its full modulus there by C(log t)^(2/3). Its outer disk
has left edge 226/256>7/8 and misses the pole for large t. This is
the full disk statement in that proof, not merely L456's conclusion
on a real-part interval or L452's narrower derivative strip.

For r large enough that 1/(2r)<=d, every |z-x0|<=8d satisfies

    |(1/2+z+ia)-(2+ia)|
       <= 17/16+8d = 545/512 < 546/512 = 273/256.

Here 1/2+x0<2, and its distance from 2 is at most 17/16.
The zeta arguments have real part at least 15/16-8d>7/8 and
imaginary part within 8d of a; they meet neither the boundary nor
the pole. The reflected negative-height disk has the same properties.
Define on this z disk

    Q(z)=f_a(1/2+z+ia)
                    +conjugate(f_a(1/2+conjugate(z)+ia)),
    E(z)=2rz-N Log z, H(z)=E(z)+Q(z),

using the real-on-positive-axis branch of Log. Both terms of Q are
holomorphic. Their exponentials are the two zeta factors, respectively.
Moreover Q(conjugate z)=conjugate Q(z), and for real x,

    Q(x)=log|zeta(1/2+x+ia)|^2.

Thus H is real on the real diameter and is the complete local
logarithm of the integrand. Cauchy's estimates with the fixed 2d
reserve give, for 0<=j<=3 on |z-x0|<=6d,

    |Q^(j)(z)| <= C_j r^(2/3).                       (3)

For x in [x0-d,x0+d], one has 2/5<x<1/2 eventually. Exactly,

    H'(x)=2r(x-x0)/x+Q'(x),
    H''(x)=N/x^2+Q''(x).                             (4)

Since 7r/8<=N<=r eventually, the bare second derivative lies
between (7/2)r and (25/4)r. Equation (3) therefore gives
2r<=H''(x)<=8r on this whole interval after one uniform onset.
At x0-d and x0+d the bare first derivative has the indicated
opposite signs with magnitude at least 4rd; the perturbation
O(r^(2/3)) is smaller. The intermediate value theorem and strict
increase give exactly one real saddle x*. Its equation in (4) gives

    |x*-x0|=|x*Q'(x*)|/(2r)=O(r^(-1/3)).             (5)

Increase the same onset so that this is at most d/2. On
|z-x*|<=2d, (3), the fixed positive distance from z=0, and
N=O(r) yield |H'''(z)|<=Cr. In particular Taylor remainders on
the local vertical segment have a constant uniform in r,m. No
shrinking zero-free disk or uncontrolled derivative constant is used.

### 2. Positive normalization with the factorial retained

Write lambda0=N/x0^2 and define the bare Gaussian scale

    M0=A exp(E(x0))/sqrt(2*pi*lambda0)
       =m! exp(m+1)/((m+1)^m sqrt(2*pi*(m+1))).

Positive-real Stirling, [DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3),
gives M0=1+O(1/m). Indeed the right side equals
sqrt(m/(m+1))*exp(1)*(m/(m+1))^m*(1+O(1/m)),
which tends to 1 with this error. This is uniform since m is
comparable to r. The exponent is N=m+1 throughout; replacing it
by m would change the stationary equation and the normalization.

Since E'(x0)=0 and E''=O(r) on the intervening real segment,
(5) gives E(x*)-E(x0)=O(r^(1/3)). Also Q(x*)=O(r^(2/3))
by (3), and (3)--(5) give lambda/lambda0=1+O(r^(-1/3)).
Consequently

    log(M*/M0)=E(x*)-E(x0)+Q(x*)
                         +(1/2)log(lambda0/lambda)=O(r^(2/3)).

Every factor defining M* is positive, so this proves both sides of
|log M*|<=Cr^(2/3). The lower bound is an analytic-logarithm
bound, not a reciprocal Euler estimate on a line left of 1.

### 3. Complete contour displacement and its residues

L456's exact identity is S=I_c+Rp, where

    I_x=A/(2*pi*i) integral_(x-i infinity)^(x+i infinity)
          exp(2rz) z^(-N) zeta(1/2+z+ia)zeta(1/2+z-ia) dz,
    Rp=2A Re[exp(2r(1/2+ia))(1/2+ia)^(-N)zeta(1+2ia)]. (6)

This retains the residues at z=1/2+ia and z=1/2-ia from
the initial inversion on Re z=1, with their plus sign. That inversion
uses the absolutely convergent Dirichlet factors on Re s=3/2;
it is not used on the displaced line.

Both c and x* lie in (2/5,1/2), so no pole is crossed in moving
from c to x*. The pole at zero stays to the left, and both shifted
zeta poles stay strictly to the right. For each fixed r,m,a take
finite rectangles of height T>2a+2. L452's formula

    zeta(s)=s/(s-1)-s integral_1^infinity {u}u^(-s-1)du

holds meromorphically for Re s>0 away from the pole. It bounds
the product on both horizontal edges by O_a(T^2), uniformly in
their real coordinate. Each connector is therefore
O_{r,m,a}(T^(1-m)) and tends to zero. Both vertical integrals
converge absolutely for m>2 by the same growth formula. Taking
T to infinity at fixed parameters proves I_c=I_x*, in either
direction of displacement. Division of the vanished connectors by
the fixed positive M* leaves exactly zero; a uniform connector
limit is not inferred from parameter-dependent constants.

Thus the full contour for the remaining estimates is the single
vertical line x*+iv, -infinity<v<infinity. It has no finite joining
pieces at the edges of a local patch. Define its complete product

    F_*(v)=zeta(1/2+x*+i(a+v))zeta(1/2+x*+i(v-a)),
    F_*(0)=exp(Q(x*))>0.

Outside the local disk we use this meromorphic product, not an
extension of the chosen logarithm through the remote poles.

### 4. Local Gaussian contribution and the shrinking annulus

Let w=(log r)/sqrt(r). Eventually w<d. Taylor's theorem on the
reserved disk and H'(x*)=0 give, for |v|<=w,

    H(x*+iv)=H(x*)-lambda*v^2/2+R(v),
    |R(v)|<=Cr|v|^3<=C(log r)^3/sqrt(r)=:epsilon_r -> 0.

The upward orientation has dz=i dv. Hence the contribution of
this segment, including A/(2*pi*i), is

    A exp(H(x*))/(2*pi) integral_(-w)^w
                          exp(-lambda*v^2/2)exp(R(v))dv
      =M* [1+O(epsilon_r)+O(exp(-k(log r)^2))]         (7)

for a fixed k>0. To justify the complex error, use
|exp(R)-1|<=exp(epsilon_r)*epsilon_r under the positive Gaussian
majorant. The omitted Gaussian tails are exponentially small since
sqrt(lambda)*w>=sqrt(2)*log r. The square root in M* is the
positive real one; thus (7) has a positive leading term.

The annulus w<|v|<=d needs a relative estimate sharper than a
global exp(Cr^(2/3)) bound. Since Q'(x*) is real, its linear
Taylor term i v Q'(x*) has zero real part. Equation (3), in the
integral form of the second-order remainder, gives

    |Re(Q(x*+iv)-Q(x*))| <= C r^(2/3) v^2.

The bare modulus is exact:

    Re(E(x*+iv)-E(x*))=-(N/2)log(1+(v/x*)^2).

Here |v|<=d<x*, so log(1+u^2)>=u^2/2 applies. Since x*<1/2
and N>=7r/8, the bare drop is at least (7/8)rv^2. It follows
on one eventual ray that

    Re(H(x*+iv)-H(x*)) <= -(r/2)v^2, |v|<=d.         (8)

The absolute annular integral divided by M* is at most
C sqrt(r) integral_(|v|>w) exp(-rv^2/2)dv,
which is at most C exp(-(log r)^2/4), by splitting the exponent
in half before integrating. This uses pairing to control real
variation, not to remove the generally nonzero linear phase at x0.

### 5. Entire middle range, far tails and both residues

The exact modulus on the displaced line, normalized by M*, is

    sqrt(lambda/(2*pi))
      (1+(v/x*)^2)^(-N/2) |F_*(v)|/F_*(0).           (9)

For d<=|v|<=a/2 both absolute shifted heights are in [a/2,3a/2].
At every such height t the L456 disk bound is available with a new
center 2+it. The entire needed real-part interval is covered:

    15/16-d <= 1/2+x* <= 63/64+2d,
    2-(15/16-d)=17/16+d < 273/256.

The interval is below 2. Therefore, using conjugation for negative
heights, |F_*(v)|/F_*(0)<=exp(Cr^(2/3)) throughout this range.
This uses real parts of the analytic logarithms; their branches at
different heights need not be identified.

Uniformly for x* in (2/5,1/2), the complete kernel tail satisfies

    sqrt(r) integral_(|v|>=d)
                    (1+(v/x*)^2)^(-N/2)dv <= C exp(-kappa*r),
    kappa=d^2/4>0.                                  (10)

For completeness, on d<=|v|<=x* its integrand is at most
exp(-(7/8)rv^2); splitting that Gaussian yields a normalized
integral at most C exp(-(7/16)rd^2). On |v|>x*, split the
power as two equal exponents N/4. One factor is at most 2^(-N/4),
and the other has a uniformly integrable majorant
(1+(v/x*)^2)^(-2) for N>=8. The resulting bound
C sqrt(r)2^(-N/4) also fits (10), since
(7/32)log 2>kappa. Thus (9)--(10) bound the whole middle
contribution relative to M* by

    C exp(-kappa*r+C r^(2/3))=o(1).                 (11)

The choice of fixed d matters: the global subexponential factor
is not multiplied by merely exp(-k(log r)^2).

For all real t, including zero, put sigma*=1/2+x*. Its interval
above lies in Re s>9/10, and

    |sigma*+it-1| >= 1/64-2d > 1/128.

L452's growth formula consequently gives
|zeta(sigma*+it)|<=C(1+|t|) uniformly through t=0. For
|v|>q=a/2>=1 this gives |F_*(v)|<=Cv^2. Since x*<1,
the kernel factor in (9) is at most |v|^(-N), and
F_*(0)>=exp(-Cr^(2/3)). The complete far contribution is at most

    C sqrt(r) exp(Cr^(2/3)) q^(2-m)/(m-2) <= exp(-r^2) (12)

relative to M*, eventually. Indeed log q=2r+O(1) and
m>=7r/8 make its logarithm at most
-(7/4)r^2+O(r)+O(r^(2/3))+O(log r). This includes all
neighborhoods of v=+a and v=-a and both unbounded rays.

Finally m!<=m^m gives A<=1. The same growth formula at 1+2ia
gives |zeta(1+2ia)|<=Ca. The sum of the moduli of the two
residues in (6), divided by M*, is thus at most

    C exp(r) a^(-m) exp(Cr^(2/3)) <= exp(-r^2),       (13)

again by log a=2r+O(1) and m>=7r/8. Both residues are retained
before this estimate, irrespective of their signs. Neither a pole
neighborhood nor a contour connector is omitted.

### 6. Assembly and scope

Equations (6)--(13) give

    |S/M*-1| <= C (log r)^3/sqrt(r)
       +C exp(-(log r)^2/4)
       +C exp(-kappa*r+C r^(2/3))+2exp(-r^2).

The last three terms are smaller than the first on one uniform
eventual ray. Swapping j,k in the finite sum proves that S is real;
alternatively, paired points of the vertical contour are conjugate,
as are the two residues. Since M*>0, the error is eventually less
than 1/2. Together with Section 2 this proves (1)--(2), with one
maximum of the finitely many uniform onsets. For example
eta(r)=C r^(-1/3) tends to zero and S>=exp(-r eta(r)) eventually.

This margin would dominate any separately established
O(r^K exp(-b r)) error with fixed K and b>0. No such whole-plane
theta error on this changed band is assumed or proved here. L456's
fixed-center freezing obstruction remains valid: moving the complete
saddle changes the normalization and retains the linear phase. L331's
old shrinking-domain models do not have the fixed-disk input (3).
The L323/L327 and fixed-r/unit-phase stops retain their stated scopes;
this proof uses log a=2r+O(1), not an assertion uniform in arbitrary
heights at fixed r or arbitrary multiplicative phases. The initial
low-index, bounded-height, mixed-positivity and selected-law/regulator
gaps remain independent. This is not a complete RH candidate.

### Separate critical audit — 2026-10-23

**Verdict and scope.** Independent checking validates (1)--(2) on the
entire closed band, without a mathematical correction. This is
REPRODUCTION under the separately approved
[audit assessment](../drafts/literature/2026-10-23-lower-band-moving-saddle-critical-audit-coverage.md).
It includes L456's full logarithm disk and inversion, not all of that
lemma's fixed-center obstruction claims. It does not audit the external
September 30 manuscript or formal import closure. The following details
record the load-bearing checks, rather than a new arithmetic result.

**Inherited full complex disk.** Radius 286/256 about 2+it has left
edge 226/256, beyond 7/8 by 1/128. A slightly larger disk still lies
in the assumed zero-free half-plane and misses the pole for large t.
The analytic logarithm normalized at the center agrees with the Euler
logarithm on the entire radius-255/256 disk, where its modulus is at
most log zeta(257/256). L452's locally uniformly convergent
fractional-part formula gives |zeta(s)|<=Ct on the outer disk.
This initially bounds only Re f_t; Borel--Caratheodory across the
gap 2/256, with the bounded normalized center value, gives full modulus
O(log t) on radius 284/256. Three-circles then gives exponent <2/3
on radius 273/256, since 273^3=20346417<20567280=255*284^2.
These are fixed domains and constants, not a real-line-only estimate
or an Euler reciprocal series to the left of 1.

**Reserves and saddle.** The largest distance of 1/2+x0+ia from
2+ia is at most 17/16, including the closed lower endpoint. Adding
8d gives 545/512, leaving 1/512 to radius 273/256. Thus the
radius-2d Cauchy circles about |z-x0|<=6d stay in the bounded-log
domain. Reflection defines the second holomorphic logarithm and makes
Q real on the real diameter. For one onset, 2/5<x<1/2 and
7r/8<=N<=r throughout [x0-d,x0+d]. The bare curvature therefore
lies between 7r/2 and 25r/4. The O(r^(2/3)) perturbations preserve
strict convexity and the opposite endpoint derivative signs, whose bare
magnitudes are at least 4rd. This proves exactly the stated existence,
uniqueness in that interval, displacement and curvature bounds. Once
the displacement is at most d/2, the radius-2d Taylor disk about x*
is still inside the Cauchy domain. The resulting H''' bound is O(r)
uniformly for real r and even m across the full closed band.

**Factorial and orientation.** Direct cancellation of powers of 2r
in the bare scale gives exactly
M0=m!e^(m+1)/((m+1)^m sqrt(2*pi*(m+1))). Positive-real Stirling
gives M0=1+O(1/m). The exponent difference is
O(r|x*-x0|^2)=O(r^(1/3)), Q(x*)=O(r^(2/3)), and
lambda/lambda0=1+O(r^(-1/3)). These verify both sides of the
logarithmic bound on M*. The exponent remains N=m+1 throughout.
H'(x*)=0, rather than conjugacy at x0, removes the linear phase.
The upward orientation dz=i dv cancels the i in 2*pi*i, and the
Gaussian integral uses the positive root sqrt(2*pi/lambda). The
resulting positive scale is precisely M*, including the factorial.

**Inversion and contour.** Scalar inversion of
(2r-log(jk))_+^m/m!, multiplied by A, yields exactly the weight in S,
including its zero value at the cutoff. On Re z=1 the complete Fubini
majorant uses zeta(3/2)^2 and an integrable power of |1+iv|. Moving
left to c crosses exactly 1/2+ia and 1/2-ia, with the conjugate
unit-pole residues and the plus sign in (6); zero stays to the left.
Both this shift and the shift c to x* have horizontal edges bounded
by O_{r,m,a}(T^(1-m)) for T>2a+2 and absolutely convergent vertical
tails for m>2. The second shift crosses no pole in either direction,
since both real parts lie strictly between zero and 1/2. Taking the
rectangle limit at fixed parameters is sufficient before uniform
relative estimates. There are no omitted finite patch connectors.

**Central window and shrinking annulus.** On
|v|<=w=(log r)/sqrt(r), the Taylor remainder is at most
Cr|v|^3<=C(log r)^3/sqrt(r), so its complex exponential error is
controlled by the positive Gaussian majorant. The omitted Gaussian
mass is exponentially small in (log r)^2. On w<|v|<=d, the linear
increment i v Q'(x*) has zero real part. The second-derivative
remainder is O(r^(2/3)v^2), while the exact bare drop is at least
(7/8)rv^2. The total drop is therefore at least rv^2/2 eventually,
giving relative annular error O(exp(-(log r)^2/4)). Replacing this
quadratic estimate by a global exp(Cr^(2/3)) factor would fail here;
the proof does not make that replacement.

**Complete outer range and residues.** On d<=|v|<=a/2, both shifted
height moduli lie in [a/2,3a/2]. The full real-part interval
[15/16-d,63/64+2d] fits the inherited disk, since
17/16+d<273/256. Bounding both numerator factors and the central
denominator gives exp(O(r^(2/3))). The full normalized kernel tail
is O(exp(-kappa*r)), kappa=d^2/4: split the Gaussian exponent for
|v|<=x*, and split off 2^(-N/4) with a uniformly integrable remaining
power for |v|>x*. This verifies the middle error (11) with a fixed
exponential rate, eventually smaller than the claimed local error.

For |v|>a/2, sigma* stays above 9/10 and below 1 by at least
1/64-2d>1/128. The fractional-part formula thus gives a uniform
C(1+|t|) bound even at t=0. Since a<=2|v|, the full product is
at most Cv^2. Its remaining kernel integral is bounded by
q^(2-m)/(m-2), q=a/2. Including sqrt(r) and the reciprocal central
value, its logarithm is at most
-(7/4)r^2+O(r)+O(r^(2/3))+O(log r). This verifies (12) on both
unbounded rays and through both neighborhoods v=+-a. Finally A<=1
and |zeta(1+2ia)|<=Ca bound the sum of both residue moduli relative
to M* by C exp(r)a^(-m)exp(Cr^(2/3)), also <=exp(-r^2) eventually.
No large-height estimate is applied at shifted height zero.

**Assembly and limits.** Every constant above is independent of m/r
on the fixed closed band. Taking the maximum of the finitely many
onsets gives the full error in Section 6, eventually below 1/2.
Swapping j,k makes S real; M*>0 and its lower logarithmic bound
then give (2), absorbing the factor 1/2 into C. This validates the
existing conditional arithmetic input by known methods, without an
originality claim. No changed-band theta error, every-height transfer,
smaller-index sign or bounded-height result is supplied. The fixed-center,
shrinking-domain and fixed-r/unit-phase stops keep their scopes, and
global mixed positivity remains unproved. This is not an RH candidate.

## Mathlib

Full matching coverage for this moving-saddle arithmetic margin has
not been checked; absence is not asserted. Supporting analytic-log,
Cauchy, Gaussian, contour-residue and Stirling APIs were not checked
here. L452 records the supporting Euler-log theorem and the external
artifact `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`, with the
register's qualifications; no local build or Mathlib membership of
that external artifact is claimed.

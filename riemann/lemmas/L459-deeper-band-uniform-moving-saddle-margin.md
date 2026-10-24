# Lemma 459: deeper-band uniform moving-saddle arithmetic margin

## Hypotheses

Assume the zeta specialization of OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
Theorem 1.1, at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Retain the [external-input register's precise source and qualifications](../foundations/2026-10-quasi-riemann-input.md):
the half-plane is strict, the pole at 1 is allowed, and the manuscript
and formal import closure have not been independently audited here.
Everything below is conditional on this unchanged external premise.

Let r tend to infinity through positive reals and let m be a positive
even integer with

    13/16 <= alpha=m/r <= 7/8.

Set, exactly,

    c=m/(2r), sigma=1/2+c, h=9/2+c,
    a=sqrt(4*pi^2*exp(4r)-h^2)>0,
    A=m!/(2r)^m, N=m+1, x0=N/(2r), d=1/4096,
    S=S_{r,m}=sum_{j,k>=1}(jk)^(-1/2)
           (1-log(jk)/(2r))_+^m exp(ia log(k/j)).

The finite sum has zero weight also at cutoff equality jk=exp(2r).
Vertical contours are oriented upward. Constants below are uniform
on this entire closed band; constants and onsets are existential.

## Conclusion

For all sufficiently large r there is a unique real stationary point
x* in [x0-d,x0+d] of

    H(x)=2rx-N log x+log|zeta(1/2+x+ia)|^2.

With p=15/16 it satisfies

    |x*-x0|=O(r^(p-1))=O(r^(-1/16)),
    2r <= lambda:=H''(x*) <= 8r.

The factorial-normalized scale

    M*=A exp(2rx*) (x*)^(-N)
                  |zeta(1/2+x*+ia)|^2 / sqrt(2*pi*lambda)

is positive, uses the positive real square root, and obeys

    |log M*| <= C r^(15/16)=o(r),
    S/M* = 1+O((log r)^3/sqrt(r)).                    (1)

In particular S>=exp(-K r^(15/16))>0 with one common onset.
Both original residues and the entire deformed vertical contour are
included. This is a local known-method specialization, classified
REPRODUCTION; the separate critical audit below validates this conditional
input on the entire stated closed band. No matching
arithmetic theorem beyond the sources checked, or originality, is claimed.

This does not supply a matching theta reduction, a Laguerre sign or
every-height transfer on this band, initial-index completion, bounded-height
extension, global mixed positivity, an RH candidate, or an audit of the
external premise. No comparison S/|zeta(sigma+ia)|^2 -> 1 is asserted.

## Proof

The prior [exact-band assessment](../drafts/literature/2026-10-24-deeper-band-moving-saddle-coverage.md)
authorizes this single mathematical attempt. Reuse the inspected mechanism
in Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*,
second edition (1986), Theorem 14.2 and proof, pp. 336--337, and
Section 14.3, pp. 338--339, as specialized in L452 and L456. The printed
RH hypothesis is not imported: only Borel--Caratheodory, Hadamard
three-circles and Cauchy estimates on checked zero-free disks are used.
The saddle references are [DLMF 2.4(iii)--(iv), equations 2.4.10--2.4.16](https://dlmf.nist.gov/2.4#iii),
including the two half-path cases and square-root branch rule, and
N. M. Temme, *Uniform Asymptotic Methods for Integrals*,
[arXiv:1308.1547v1](https://arxiv.org/html/1308.1547v1), Sections
2.2--2.3, (2.9)--(2.13), and Section 4.1, (4.1)--(4.5).
They do not assert this arithmetic conclusion or its parameter uniformity.
The estimates below establish that specialization. L457 supplies the
bare factorial-scale identity and audited contour method; its old-band
logarithm exponent and arithmetic conclusion are not used here.

### 1. New fixed logarithm domain and reserved Cauchy disks

The exact coupled domain gives

    13/32 <= c <= 7/16, 29/32 <= sigma <= 15/16,
    log a=2r+log(2*pi)+O(exp(-4r)).                    (2)

For every sufficiently large positive t, L456's proof constructs an
Euler-normalized analytic logarithm f_t on a neighborhood of the
radius-286/256 closed disk about 2+it. Its minimum real part is
226/256>7/8, and at such heights the disk misses the pole.
It agrees with the bounded Euler logarithm on radius 255/256, whose
minimum real part is 257/256>1. The larger radius-284/256 disk has
full logarithm bound O(log t), by Borel--Caratheodory using L452's
growth formula and the normalized center value. These full-domain
statements are in L456's proof, rather than its narrower conclusion.

Apply three-circles on these same inner and outer domains, with the
new intermediate radius R1=282/256. If

    theta=log(282/255)/log(284/255),

then the exact integer comparison

    282^16 < 255*284^15

implies theta<15/16=p<1. Thus

    max_{|s-(2+it)|<=282/256}|f_t(s)| <= C(log t)^p.  (3)

No Euler series is used left of one. The radius-273/256 conclusion
of L456 would miss the new endpoint; (3) is a fresh intermediate-radius
application with fixed reserves, not an extension assumed from it.

For r large enough that 1/(2r)<=d, the distance of
1/2+x0+ia from 2+ia is at most 35/32. Hence for |z-x0|<=8d,

    |(1/2+z+ia)-(2+ia)| <= 35/32+8d
                              =561/512 <564/512=282/256. (4)

The inclusion reserve is 3/512. The zeta arguments have real part
at least 29/32-8d>7/8 and stay at high positive height. Reflection
gives an equally valid negative-height domain. On this z disk define

    Q(z)=f_a(1/2+z+ia)
                    +conjugate(f_a(1/2+conjugate(z)+ia)),
    E(z)=2rz-N Log z, H(z)=E(z)+Q(z),

with the real-on-positive-axis branch of Log. The reflected expression
is holomorphic, exp Q is exactly the product of the two shifted zeta
factors, and Q(conjugate z)=conjugate Q(z). On the real diameter,
Q(x)=log|zeta(1/2+x+ia)|^2, including its real normalization.
Equation (3), (2) and Cauchy's estimates on radius-2d circles give

    |Q^(j)(z)| <= C_j r^p, 0<=j<=3, |z-x0|<=6d.     (5)

The constants are fixed independently of the height and band parameter.

### 2. Real saddle and positive factorial-normalized scale

On [x0-d,x0+d], eventually 2/5<x<1/2, and
13r/16<=N<=r. Exactly,

    H'(x)=2r(x-x0)/x+Q'(x),
    H''(x)=N/x^2+Q''(x).                             (6)

The bare second derivative is between 13r/4 and 25r/4. Since p<1,
(5) yields 2r<=H''(x)<=8r on the entire interval after one onset.
At its left and right endpoints the bare first derivative has opposite
signs and modulus at least 4rd, larger eventually than Cr^p.
The intermediate value theorem and strict increase give exactly one
real saddle x* in that interval. Its equation gives

    |x*-x0|=|x*Q'(x*)|/(2r)=O(r^(p-1)).              (7)

Increase the onset so that the displacement is at most d/2. On the
radius-2d disk about x*, (5) and the fixed distance from z=0 give
|H'''(z)|<=Cr, since E'''=O(r) and r^p=o(r).

Retain L457's parameter-independent bare scale identity, obtained by
substituting x0=N/(2r) and lambda0=N/x0^2:

    M0=A exp(E(x0))/sqrt(2*pi*lambda0)
       =m! exp(m+1)/((m+1)^m sqrt(2*pi*(m+1))).       (8)

Positive-real Stirling ([DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3),
with its remainder on this positive ray) gives M0=1+O(1/m).
The factorial and N=m+1 have not been dropped. Since E'(x0)=0,
E''=O(r) on the real segment, and (7) holds,

    E(x*)-E(x0)=O(r^(2p-1))=O(r^(7/8)),
    Q(x*)=O(r^p), lambda/lambda0=1+O(r^(p-1)).

Consequently

    log(M*/M0)=E(x*)-E(x0)+Q(x*)
                    +(1/2)log(lambda0/lambda)=O(r^p). (9)

Every factor defining M* is positive. Equations (8)--(9) prove the
two-sided logarithmic bound in (1), without a reciprocal Euler estimate
on a line left of one.

### 3. Inversion, both original residues and the full displacement

The scalar inversion used in L456, from [DLMF 1.14.20](https://dlmf.nist.gov/1.14.E20),
applies to u_+^m/m!: it is continuous at zero for m>=1, piecewise
continuously differentiable, of exponential order, and the inversion
line Re z=1 lies to the right of its Laplace-transform singularity.
Multiplying by A gives exactly the weight in S, including cutoff
equality. The complete Fubini majorant on that line is

    A exp(2r) zeta(3/2)^2/(2*pi)
                    integral_R (1+v^2)^(-N/2)dv < infinity.

Absolute Dirichlet convergence is used only there. Define

    I_x=A/(2*pi*i) integral_(x-i infinity)^(x+i infinity)
             exp(2rz) z^(-N)
             zeta(1/2+z+ia)zeta(1/2+z-ia) dz.

Moving from 1 to c crosses exactly the two simple zeta poles
z=1/2+ia and z=1/2-ia, with unit residues; zero is not crossed.
The pole statement is [DLMF 25.2(i), 25.2.4](https://dlmf.nist.gov/25.2).
The conjugate contributions have plus sign, so

    S=I_c+Rp,
    Rp=2A Re[exp(2r(1/2+ia))(1/2+ia)^(-N)
                                               zeta(1+2ia)]. (10)

Here is the required contour justification on the changed band.
L452 proves meromorphically on Re s>0 that

    zeta(s)=s/(s-1)-s integral_1^infinity {u}u^(-s-1)du, (11)

with locally uniform convergence away from the pole. At rectangle
height T>2a+2 this bounds each factor by O_a(T), uniformly over
all real coordinates of the shift. Horizontal integrals are
O_{r,m,a}(T^(1-m)) and vanish at fixed parameters. On the new
vertical line the real part sigma stays in [29/32,15/16], a fixed
positive distance from the pole at shifted height zero; the product
is O((1+a+|v|)^2). Vertical tails are absolutely integrable for
m>2, which holds uniformly eventually. This proves (10) after
fixed-parameter rectangle limits, before any uniform estimate.

Both c and x* lie strictly in (2/5,1/2). Thus shifting from c to
x* crosses neither shifted pole, nor zero, in either direction.
The same finite-rectangle argument proves I_c=I_x*. Division of
the vanished connectors by the fixed positive M* leaves zero; no
uniform connector limit with parameter-dependent constants is assumed.
There are no finite connecting pieces at a local patch boundary.

### 4. Central segment and shrinking annulus

Put w=(log r)/sqrt(r). For |v|<=w<d, Taylor's theorem on the
reserved disk, H'(x*)=0 and the bound on H''' give

    H(x*+iv)=H(x*)-lambda*v^2/2+R(v),
    |R(v)|<=Cr|v|^3<=C(log r)^3/sqrt(r)=:epsilon_r.

Since epsilon_r tends to zero, |exp R-1|<=exp(epsilon_r)*epsilon_r.
The upward orientation dz=i dv and the positive Gaussian integral
therefore give the central contribution

    A exp(H(x*))/(2*pi) integral_(-w)^w
                              exp(-lambda*v^2/2)exp(R(v))dv
      =M* [1+O(epsilon_r)+O(exp(-k(log r)^2))]         (12)

with fixed k>0; sqrt(lambda)*w>=sqrt(2)*log r controls the omitted
Gaussian mass. This fixes the positive square-root branch and sign.

For w<|v|<=d the global bound exp(Cr^p) would be too expensive.
Instead, Q'(x*) is real, so its linear vertical increment has zero
real part. Equation (5) gives

    |Re(Q(x*+iv)-Q(x*))|<=Cr^p v^2.

The exact bare modulus drop is

    Re(E(x*+iv)-E(x*))=-(N/2)log(1+(v/x*)^2).

Here |v|<=d<x* and log(1+u^2)>=u^2/2 for |u|<=1. Using
x*<1/2 and N>=13r/16, the bare drop is at least (13/16)rv^2.
Since p<1, one common onset gives

    Re(H(x*+iv)-H(x*))<=-rv^2/2, |v|<=d.           (13)

The absolute annular integral divided by M* is at most
C sqrt(r) integral_(|v|>w) exp(-rv^2/2)dv,
hence at most C exp(-(log r)^2/4), by splitting the Gaussian exponent.

### 5. Entire middle range, shifted-height-zero neighborhoods and rays

On the full displaced line write

    F_*(v)=zeta(1/2+x*+i(a+v))zeta(1/2+x*+i(v-a)),
    F_*(0)=exp(Q(x*))>0.

Outside the local disk use this product, without continuing a chosen
logarithm through remote poles. The modulus of its integrand relative
to M*, including the vertical measure, is exactly

    sqrt(lambda/(2*pi)) (1+(v/x*)^2)^(-N/2)
                                            |F_*(v)|/F_*(0). (14)

For d<=|v|<=a/2 the absolute shifted heights belong to [a/2,3a/2].
For all sufficiently large r the real-part interval needed is

    29/32-d <= sigma*:=1/2+x* <= 15/16+2d.

It fits (3) recentered at every positive shifted height, because
35/32+d<282/256; all its real parts are below 2. With conjugation
for negative heights, (3) and (2) imply

    |F_*(v)|/F_*(0)<=exp(Cr^p)                       (15)

uniformly. Branches at different heights need not be identified to
bound their real parts.

For completeness the entire kernel tail in this range is controlled
by the following bound, with fixed kappa=d^2/4>0:

    sqrt(r) integral_(|v|>=d)
                   (1+(v/x*)^2)^(-N/2)dv <=C exp(-kappa*r). (16)

On d<=|v|<=x*, the preceding logarithm inequality bounds the kernel
by exp(-(13/16)rv^2). Splitting the Gaussian exponent bounds its
normalized integral by C exp(-(13/32)rd^2), which is stronger
than (16). On |v|>x*, split off one factor 2^(-N/4).
The remaining power has a uniformly integrable majorant
(1+(v/x*)^2)^(-2) for N>=8. Its contribution is at most
C sqrt(r)2^(-N/4). Since (13/64)log 2>kappa, it also satisfies
(16). For example log 2>1/2 follows by integrating 1/u>1/2 on
[1,2), and 13/128>d^2/4. Equations (14)--(16) bound the complete
middle contribution relative to M* by

    C exp(-kappa*r+Cr^(15/16))=o(1).                (17)

The fixed d is essential; no subexponential factor is charged to
the shrinking annulus.

For every real t, including zero, sigma*>9/10 and

    |sigma*+it-1|>=1/16-2d>1/32.

Equation (11) therefore gives |zeta(sigma*+it)|<=C(1+|t|),
uniformly at all shifted heights. For |v|>q=a/2>=1 it follows
that |F_*(v)|<=Cv^2. Since x*<1, the kernel in (14) is at
most |v|^(-N), while F_*(0)>=exp(-Cr^p). Both far rays,
including the full neighborhoods of v=+a and v=-a, consequently
contribute at most

    C sqrt(r) exp(Cr^p) q^(2-m)/(m-2) <= exp(-r^2)   (18)

relative to M*. Indeed log q=2r+O(1), m>=13r/16, and the
logarithm of the left side is at most
-(13/8)r^2+O(r)+O(r^p)+O(log r). No high-height logarithm bound
is applied at shifted height zero.

Finally A<=1 because m!<=m^m and c<1. Applying (11) at
1+2ia gives |zeta(1+2ia)|<=Ca. The sum of the moduli of both
residues in (10), divided by M*, is at most

    C exp(r)a^(-m)exp(Cr^p)<=exp(-r^2).              (19)

The same quadratic exponent proves this estimate. Both original
residues have been retained with their signs before this bound.

### 6. Uniform assembly and limitations

Combining (10), (12)--(13), and (17)--(19) gives

    |S/M*-1| <= C(log r)^3/sqrt(r)
       +C exp(-(log r)^2/4)
       +C exp(-kappa*r+Cr^(15/16))+2exp(-r^2).       (20)

All constants are independent of m/r on the entire closed band.
Because p=15/16<1, the last three terms are eventually smaller
than the first. Taking the maximum of the finitely many onsets proves
(1). Swapping j,k in the finite sum makes S real. The relative
error is eventually below 1/2, so S>=M*/2>=exp(-K r^p)>0 after
enlarging K and the common onset. The achieved threshold is a
complete relative o(1) and |log M*|=o(r), as required; the weaker
power compared with L457 affects the unevaluated onset, not this limit.

This margin would dominate any separately established additive error
O(r^K0 exp(-b r)) with fixed K0 and b>0. No such theta theorem
on this band is assumed here. Matching theta reduction, every-height
transfer, initial low-index signs, bounded exterior heights, global
mixed positivity and selected-law/regulator realization remain separate
gaps. L456's fixed-center freezing obstruction and L331's old
shrinking-domain models keep their original scopes; neither supplies
or refutes this fixed-domain moving-saddle conclusion. The L323/L327
and fixed-r/unit-phase failures are likewise preserved. This argument
uses log a=2r+O(1) for the actual coupled height, and makes no
uniform-in-arbitrary-height or arbitrary-unit-phase assertion.

Exact finite checks of the interpolation inequality, disk reserves,
curvature reserves and tail constants are reproduced by
`python3 scripts/deeper-band/check_moving_saddle_constants.py`, writing
`scripts/deeper-band/moving-saddle-constants-certificate.json`.
They verify only those finite arithmetic comparisons, not the analytic
proof, the external premise or actual values of S.

### Separate critical audit — 2026-10-24

**Verdict and scope.** The independently checked argument passes without
mathematical correction, under the unchanged pinned external premise.
The separately approved
[audit assessment](../drafts/literature/2026-10-24-deeper-band-moving-saddle-critical-audit-coverage.md)+covers this REPRODUCTION. The audit checks L452's growth mechanism,
L456's larger logarithm domains and inversion, and L457's bare-scale
identity as used here; it does not validate unrelated conclusions of
those lemmas or audit the external manuscript/import closure. This is
validation of a local conditional input, not a discovery beyond the
assessed source methods.

**Full logarithm and reserves.** The outer disk's left edge is
113/128, separated from 7/8 by 1/128. A slightly larger disk still
lies in the assumed zero-free half-plane and misses the pole at large
positive height. On this simply connected neighborhood the logarithm
exists. Its bounded Euler value at the center fixes the branch on the
entire inner disk: the difference from the Euler logarithm is a
continuous 2*pi*i-integer-valued function vanishing at the center.
The inner disk has left edge 257/256>1. L452's fractional-part
formula gives |zeta(s)|<=Ct on the outer disk; Borel--Caratheodory
across the fixed gap 2/256 bounds the full complex logarithm on
radius 284/256, not merely its real part. The exact comparison is

    282^16 = 1599505482830839945389297901331692978176
      < 1608108254287353635994953164759624581120 = 255*284^15.

Taking logarithms gives theta<15/16. This verifies the new
interpolation power rather than importing L456's narrower conclusion.
Since x0=c+1/(2r), eventually 1/(2r)<=d and the full radius-8d
disk leaves reserve 3/512 inside radius 282/256. Radius-2d Cauchy
circles about every |z-x0|<=6d therefore fit. Conjugating the power
series for the reflected summand defines a holomorphic function whose
exponential is zeta(1/2+z-ia). Thus Q is the actual paired logarithm,
real on the real diameter, and (5) holds uniformly on its full domain.

**Saddle and factorial.** On the stated real interval, x>2/5,
x<1/2, and 13r/16<=N<=r eventually. Hence the bare curvature is
between 13r/4 and 25r/4. Its O(r^p) perturbation preserves the
claimed 2r and 8r bounds. At each endpoint the bare derivative
has modulus at least 4rd and the indicated opposite signs; p<1
makes the perturbation smaller with one onset. Strict convexity gives
uniqueness precisely on this interval, with no claim about other real
saddles. The saddle equation implies displacement O(r^(-1/16));
eventually it is <=d/2 and the radius-2d Taylor disk stays reserved.
The third derivative is O(r) there.

Direct cancellation using N=m+1 gives (8), with denominator
N^m sqrt(2*pi*N), not N^N sqrt(2*pi*N). Positive-ray Stirling
then gives M0=1+O(1/m). Taylor expansion of E at x0 costs
O(r*(r^(-1/16))^2)=O(r^(7/8)), while Q costs O(r^(15/16)).
The curvature ratio differs from one by O(r^(-1/16)); these facts
prove both sides of (9). There is no reciprocal Euler estimate left
of one. The upward contour cancels the i in 2*pi*i, and the
positive Gaussian root gives exactly the stated positive M*.

**Inversion and complete deformation.** Scalar inversion at
u=2r-log(jk), including u=0, multiplied by A gives the precise
cutoff weight. The full absolute majorant on Re z=1 is integrable
and uses Dirichlet factors only at real part 3/2. Shifting left
crosses exactly z=1/2+-ia. The right upward line minus the left
upward line is the positively oriented boundary, so both residues
have the plus sign in (10). Their other zeta factors are respectively
zeta(1+2ia) and its conjugate. The pole at zero is not crossed.
The second shift crosses no pole because c,x* both lie in (2/5,1/2).
At fixed parameters, T>2a+2 makes the horizontal products O_a(T^2),
and the connectors O_{r,m,a}(T^(1-m)) tend to zero. The vertical
tails converge absolutely for m>2. These fixed-parameter limits prove
the exact contour identity before division by M* and uniform estimates;
no local joining segments are discarded.

**Every relative error.** On |v|<=w the complex Taylor remainder
is at most C(log r)^3/sqrt(r), and its exponential is controlled
by the positive Gaussian majorant. Curvature >=2r controls both
omitted Gaussian half-tails. On w<|v|<=d, Q'(x*) is real, so
the linear vertical increment contributes no real part. The remaining
increment is O(r^p v^2), against a bare drop at least
(13/16)rv^2. Their difference is >=rv^2/2 eventually. This proves
the full shrinking-annulus estimate without paying exp(Cr^p) there.

For d<=|v|<=a/2, both absolute shifted heights lie in [a/2,3a/2].
The entire real-part range fits the new logarithm disk, with reserve
282/256-(35/32+d)=31/4096>0. Numerator and denominator bounds
give exp(Cr^p). On d<=|v|<=x*, splitting the Gaussian exponent
gives rate 13d^2/32>d^2/4. On |v|>x*, splitting the power into
two equal factors gives 2^(-N/4) times an integrable remaining
power; its rate exceeds d^2/4, absorbing sqrt(r). This verifies
(16) on the whole tail and hence (17), with a fixed positive rate.

For the remaining two rays, sigma*>9/10 and
1-sigma*>=1/16-2d>1/32. Thus the all-height fractional-part
formula applies even at shifted height zero. Since a<=2|v|, the
product is <=Cv^2 throughout both neighborhoods v=+-a as well as
to infinity. Integrating v^(2-N) gives q^(2-m)/(m-2), q=a/2.
Its relative logarithm is at most -(13/8)r^2+O(r)+O(r^p)+O(log r),
which proves (18). Finally A<=1 and |zeta(1+2ia)|<=Ca give (19)
for the sum of the two residue moduli, with the same quadratic
reserve. None of these estimates uses a large-height logarithm bound
near shifted height zero or loses a residue.

All constants and all domain reserves are uniform on the closed band.
There are finitely many onset requirements; their maximum gives (20).
Since p<1, the middle error is eventually smaller than the central
error despite the very small fixed kappa. No numerical or practical
onset is claimed. The finite sum is real by swapping j,k; once the
complete relative error is below 1/2 its sign and lower margin follow.
The 17 exact constant checks were rerun and their complete records
inspected; they support the arithmetic comparisons, not this analytic
audit or the external premise. Matching theta reduction, every-height
transfer, initial indices, bounded heights and global mixed positivity
remain unresolved. The earlier scoped stops remain valid.

## Mathlib

Full matching Mathlib coverage for this changed-band arithmetic margin
has not been checked; absence is not asserted. Supporting analytic-log,
Borel--Caratheodory, three-circles, Cauchy, inversion, residue, Gaussian
and Stirling APIs were not checked here. L452 records the supporting
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log)
and the external artifact `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`.
The latter is not asserted to belong to Mathlib or to have been built
locally; the register's external verification qualifications remain.

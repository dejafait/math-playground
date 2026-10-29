# Lemma 468: a uniform moving-anchor negative-witness cutoff

## Hypotheses

Let Xi(z)=xi(1/2+iz) be L018's actual completion. For real a write

    H_a(y)=Xi(a+iy)Xi(a-iy)=sum_(n>=0) D_n(Xi;a)y^(2n),
    t=|a|,    T=2+t.

Assume exactly the external premise retained in L461: OpenAI,
*The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026, Theorem 1.1, specialized to zeta, at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
The [pinned manuscript](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
asserts no zeros in Re(s)>7/8, allows the pole at 1, and does not
exclude the boundary. Its manuscript and formal import closure remain
locally unaudited, as recorded in the
[external-input register](../foundations/2026-10-quasi-riemann-input.md).
This lemma is conditional on that precise premise.

All logarithms are natural. For sufficiently large T put

    L=log log T,    d=L^(-1/2),    e=d^2,
    eta=3/8+d,    R=3/8+2d,    p=eta^2/R^2.

The parameters are fixed during each application at a given T, and
vary only between applications. No nonzero central value or bound on
central multiplicity is assumed.

## Conclusion

There are constants h>0, C0>=1 and T0 such that for every real a
with T>=T0,

    A(a)=h T^(7/2+eta-2d^2) exp(-pi*t/2),
    H_a(eta)>=A(a)>0,
    max_(|y|=R)|H_a(y)| / A(a) <= C0 T^(d+4d^2).       (1)

Every hypothetical nonreal zero a+ib of Xi with T>=T0 therefore
forces D_n(Xi;a)<0 at some integer

    1 <= n <= ceil((3/16+3/sqrt(log log T))log T).       (2)

Increasing T0 is permitted without changing h or C0. All constants
and this single onset are independent of a, b and central multiplicity.
The numerical coefficient 3 is admissible, not optimized; the height
onset is existential and is not numerically evaluated.

This is a REPRODUCTION using the source methods covered by the
[prior SPECIALIZE assessment](../drafts/literature/2026-10-26-moving-anchor-explicit-rate-coverage.md).
It refines L461's fixed-parameter quantifiers; its full local proof
passes the separate critical audit recorded below on 2026-10-26,
without a change to its bound or hypotheses. It supplies no coefficient signs,
effective height overlap, endpoint cutoff with coefficient exactly
3/16, or RH candidate. The external theorem is not audited here.

## Proof

### Uniform logarithm estimate on a large-height family

Take T large enough that 0<d<=1/32 and t>=8. Thus

    3/8 < eta < R <= 7/16 < 1/2.

For every hgt in [t/2,3t/2] center disks at w=2+i*hgt. Use

    r0=1/2,    r1=9/8-d,    r2=9/8-d/2,
    r3=9/8-d/4,    r3-r2=d/4.

The disk of radius r3+d/8 is contained in Re(s)>7/8 and misses
s=1. The premise gives an analytic logarithm f of zeta on this
simply connected open disk. Normalize f(w) by L005's Euler logarithm.
On the connected r0 disk the two logarithms then agree: their
difference is a continuous multiple of 2*pi*i and is zero at w.
Consequently, with fixed constants B0>=1 and B1,

    max_(|s-w|<=r0)|f(s)| <= B0,
    |f(w)| <= B1,

where one may take B0=max(1,log zeta(3/2)) and B1=log zeta(2).
The Euler series is used only at real part at least 3/2.

L320's equation (5), whose integral converges locally uniformly for
Re(s)>0, is

    zeta(s)=s/(s-1)-s integral_1^infinity {u}u^(-s-1)du. (3)

On the closed r3 disk, Re(s)>=7/8 and |Im(s)| is comparable to t.
Since the integral's absolute value is at most 1/Re(s), (3) gives
|zeta(s)|<=B2*T with one constant B2>=1, independent of d and hgt.
Here the distance from s=1 is bounded below by hgt-r3, and t>=8
keeps that distance comparable to t. Thus Re(f(s))<=log(B2*T).

Apply Borel--Caratheodory in its explicit difference form:

    max_(|s-w|<=r2)|f(s)-f(w)|
       <= (2r2/(r3-r2)) (log(B2*T)-Re(f(w))).

The source is K. Ramachandra, *Lectures on the Mean-Value and
Omega-Theorems for the Riemann Zeta-Function*, TIFR/Springer (1995),
Theorem 1.6.1, equation (1.6.1), printed pp. 28-29
([PDF pp. 38-39](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=38)).
The analytic neighborhood and boundary real-part bound required
there were just verified. Since r2<=9/8 and r3-r2=d/4, there is
one B3>=1 such that

    max_(|s-w|<=r2)|f(s)| <= B3*d^(-1)*log T.          (4)

Hadamard's three-circles inequality, in Ramachandra's Theorem 1.5.2,
printed pp. 26-27
([PDF pp. 36-37](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=36)),
now gives, for theta=log(r1/r0)/log(r2/r0),

    max_(|s-w|<=r1)|f(s)|
       <= B0^(1-theta) (B3*d^(-1)*log T)^theta
       <= B4*d^(-1)*(log T)^theta.                    (5)

Its holomorphy hypothesis holds on a neighborhood of the closed r2
disk. If the maximum on r0 vanishes, f is identically zero by the
identity theorem and (5) holds directly. Otherwise the logarithmic
form of the inequality applies. The maximum-modulus principle
identifies disk and circle maxima. The constants in (4)-(5) are
uniform because 0<theta<1, d<1 and B0,B3>=1.

The loss in theta is explicit. Since log(1+x)>=x/(1+x) for x>=0,

    1-theta = log(r2/r1)/log(2r2)
       >= (r2-r1)/(r2*log(9/4))
       >= kappa*d,    kappa=4/(9log(9/4))>0.           (6)

Thus (5) is at most

    B4*sqrt(L)*exp(-kappa*sqrt(L))*log T.

Its ratio to e*log T is B4*L^(3/2)*exp(-kappa*sqrt(L)), which
tends to zero. A single sufficiently large onset therefore ensures
that for every hgt in [t/2,3t/2] and 7/8+d<=sigma<=2,

    |log|zeta(sigma+i*hgt)|| <= e*log T,
    T^(-e) <= |zeta(sigma+i*hgt)| <= T^e.              (7)

Indeed these points lie in the r1 disk and |Re(f)|<=|f|.
This proves both the reciprocal and upper bound with their required
dependence. No fixed-parameter little-o estimate has been substituted
at moving parameters, and nonvanishing alone was not a lower bound.

### A bounded rectangle replaces the compact-height extension

Set

    sigma_plus=1/2+R,    sigma_minus=1/2-R,
    q=7/4+R/2=3/2+sigma_plus/2.

Throughout this argument q stays in a fixed positive compact interval
below 2, and [sigma_minus,sigma_plus] is contained in [1/16,15/16].
The vertical gamma asymptotic

    |Gamma(x+i*v)| ~ sqrt(2*pi)|v|^(x-1/2)exp(-pi*|v|/2)

is uniform for bounded real x; see
[NIST DLMF 5.11.9 and its following uniformity statement](https://dlmf.nist.gov/5.11.E9).
It gives fixed two-sided constants on every compact real-part
interval used below, for both signs of large v. L018's completed
formula, including s(s-1)/2 and pi^(-s/2), therefore implies on
sigma=sigma_plus, for hgt in [t/2,3t/2],

    |xi(sigma_plus+i*hgt)|
       <= B5*hgt^q*T^e*exp(-pi*hgt/4).                (8)

Here (7) applies because sigma_plus=7/8+2d>=7/8+d.
Reflection and conjugation give exactly the same modulus bound at
sigma_minus. All prefactor constants are uniform in d.

A preliminary interior bound is also needed. On
1/2<=sigma<=sigma_plus, (3) gives |zeta(sigma+i*hgt)|<=B6*hgt,
uniformly for the present large positive heights. The completed
formula and the same gamma estimate give

    |xi(sigma+i*hgt)|
       <= B7*hgt^(q+1)*exp(-pi*hgt/4).                (9)

The exponent follows from 2+(sigma/2-1/2)+1<=q+1.
Reflection and conjugation extend (9) to the entire closed strip
sigma_minus<=sigma<=sigma_plus. No zero-free assertion for the
interior is used.

On the closed rectangle

    Q={s: sigma_minus<=Re(s)<=sigma_plus,
            t/2<=Im(s)<=3t/2}

define

    G(s)=xi(s)exp(-i*pi*s/4)(s+2)^(-q).

The analytic power uses the logarithm on Re(s+2)>0, so its modulus
is |s+2|^(-q). Entirety of xi gives holomorphy on a neighborhood
of Q. The exponential cancels gamma decay at these positive heights.
Since |s+2|>=hgt, (8) bounds G by B5*T^e on the two vertical
sides; (9) bounds it by B8*T everywhere on Q, including the two
horizontal sides. Neither bound involves a compact-height minimum.

Put tau=8log(T)/t^2 and apply the maximum-modulus principle to

    G(s)exp(tau*(s-1/2-i*t)^2).

Writing s=sigma+i*hgt, the damping factor has modulus

    exp(tau*((sigma-1/2)^2-(hgt-t)^2)).

On the vertical sides this is at most exp(tau*R^2). On the
horizontal sides |hgt-t|=t/2, so it is at most
exp(tau*R^2)*T^(-2). The boundary bound for the damped function
is consequently B9*exp(tau*R^2)*T^e, with one B9, since
T^(-1)<=T^e. The bounded-domain maximum-modulus principle
(Ramachandra, Theorem 1.5.1, printed p. 26) gives that bound on Q.
If the damped function is constant, its boundary and interior moduli
are equal; thus the same non-strict bound holds in that case as well.

At the smaller rectangle with |hgt-t|<=R, undoing the damping
costs at most exp(tau*R^2). Since tau tends to zero and R is
bounded, the total factor exp(2tau*R^2) is bounded uniformly.
Also |s+2|<=B10*T there, with q bounded. We have proved

    |xi(sigma+i*hgt)|
       <= B11*T^(q+e)*exp(-pi*hgt/4),
    sigma_minus<=sigma<=sigma_plus, |hgt-t|<=R.        (10)

For large t the smaller rectangle lies inside Q. This argument uses
one finite rectangle for each T, without an all-height extension or
interchange of limits. The damping coefficient depends on T but all
resulting constants are uniform.

### Complete complex circle and positive real anchor

Evenness of Xi gives H_(-t)(y)=H_t(y) for every complex y, so it
suffices to estimate H_t. At y=u+i*v, |y|=R, its factors are

    xi(1/2-u+i*(t-v)),    xi(1/2+u+i*(t+v)).

Both arguments satisfy (10). Since t>R, both heights are positive
and (t-v)+(t+v)=2t. Multiplying (10) gives

    max_(|y|=R)|H_a(y)|
       <= B12*T^(7/2+R+2e)*exp(-pi*t/2).              (11)

This estimate covers the whole complex circle, not just real y.
There is no exponential loss from either shifted height.

At the real anchor, L018's reflection and reality yield

    H_a(eta)=|xi(1/2+eta+i*t)|^2.

The real part sigma_eta=7/8+d is in [7/8,29/32]. The lower
bound in (7), the uniform two-sided gamma estimate and the completed
formula give

    H_a(eta) >= h*T^(7/2+eta-2e)*exp(-pi*t/2)>0       (12)

with one h>0. To check the power, |s(s-1)|^2 contributes t^4,
the squared gamma modulus contributes t^(sigma_eta-1), and the
squared zeta lower bound contributes T^(-2e). Hence the combined
power is 3+sigma_eta=7/2+eta. All factors in the completed formula
are finite and nonzero at this point. Conversion from t to T costs
one fixed factor because t/T>=1/2 and the exponent stays bounded.
The pi power and the factor 1/4 also stay between fixed positive
constants. Thus h does not rely on any minimum over bounded heights
or on Xi(a). This proves (12) even at an arbitrarily multiple
central zero.

Dividing (11) by the positive model in (12), and taking
C0=max(1,B12/h), proves (1), since R-eta=d and e=d^2.

### General witness comparison and every prefactor

The external premise, reflection and L018's exact zero correspondence
place all Xi zeros in |Im(z)|<=3/8. For a nonreal zero, conjugation
allows 0<b<=3/8<eta<R at the same real center. Apply the general
part of L266 with F=Xi, anchor eta, lower bound A(a) in (1), and
circle majorant M=C0*T^(d+4d^2)*A(a). Its hypotheses hold pointwise
at this T. Its proof uses d_0=Xi(a)^2>=0 and never divides by it;
there is no dependence on central multiplicity or a positive lower
bound for b. It supplies a negative coefficient at some 1<=n<=K,
where

    K=ceil(Q_T),
    Q_T=((d+4d^2)log T+log(2C0/(1-p)))/(2log(R/eta)).  (13)

In particular the geometric prefactor in (13) has not been omitted.
Because R-eta=d,

    log(R/eta)=integral_eta^R dx/x >= d/R,
    1-p=d*(R+eta)/R^2 >= d/R >= 2d.

Consequently

    Q_T <= (R/2)*(1+4d)log T
                       +(R/(2d))*log(C0/d).           (14)

For d<=1/32 the first coefficient satisfies

    (R/2)*(1+4d)=3/16+(7/4)d+4d^2
                         <=3/16+(15/8)d.             (15)

For the other term use R<=1/2. Since d=L^(-1/2) and log T=exp L,

    log(C0/d)/(d^2 log T)
       = L*(log C0+(1/2)log L)/exp L -> 0.

After one further increase of T0 this gives

    (R/(2d))*log(C0/d)
        <= (1/(4d))*log(C0/d) <= d*log T.             (16)

Equations (14)-(16) imply

    Q_T <= (3/16+(23/8)d)log T <= (3/16+3d)log T.

Monotonicity of the ceiling proves (2), with no additional rounding
term. Every increase of T0 depends only on fixed constants already
constructed, not on the zero's displacement or the value of Xi at
its center. Evenness and the pointwise L266 application include both
signs of a. This completes the conditional proof.

### Scope and comparison with the preserved stops

L461's fixed-parameter constants have not been assumed uniform. The
explicit disk inequality and the bounded rectangle are the necessary
changed-quantifier applications; they justify this reproof of the
known method. L462's stop concerns fixed anchors and fixed cutoffs
below eta/2, and is unchanged. No claim about its moving-parameter
extension is needed here. The correction 3*log T/sqrt(log log T)
is unbounded, so (2) is not an endpoint theorem with bounded additive
error. None of this gives the signs needed to exclude the witness,
an effective common-height onset, or all-degree mixed positivity.

### Separate critical audit — 2026-10-26

The audit under the
[approved source scope](../drafts/literature/2026-10-26-l468-critical-audit-coverage.md)
passes. The following checks concern the local specialization of the
explicit source inequalities, not the external zero-free theorem.
No mathematical error, stronger cutoff or new sign is established by
this audit. The constant-function maximum-modulus case above is made
explicit; it does not change the argument or any estimate.

The open logarithm disk has left edge 7/8+d/8, strictly inside the
assumed zero-free half-plane, and its imaginary parts exceed
t/2-9/8>0. It therefore contains neither a zero nor the pole. The
r3 and r2 closed disks have analytic neighborhoods inside it. On the
r0 disk L005 controls the whole logarithm, not merely its real part;
the agreement of branches follows from their normalized center value.
L320 (5) controls zeta on r3 uniformly in the comparable heights.
The Borel factor is at most 9/d, and the exact three-circles exponent
obeys (6). Thus one sufficient onset condition for (7) is

    B4*L^(3/2)*exp(-kappa*sqrt(L)) <= 1.

The left side tends to zero. This condition holds for every sufficiently
large L, rather than just along a subsequence, and is independent of
the height chosen inside [t/2,3t/2]. The harmless additive center bound
has already been absorbed in B3 before interpolating. Both signs of
Re(f) are controlled; hence the reciprocal bound follows too.

For the rectangle, q lies in (31/16,63/32], and all gamma real parts
used are in fixed compact intervals. L018's reflection and conjugation
turn the left vertical edge into the right edge at the same positive
height. The preliminary bound (9) uses only Re(s)>=1/2 after that
reflection, so it does not inadvertently require interior nonvanishing.
The analytic power has exactly modulus |s+2|^(-q) because q is real.
The sign of exp(-i*pi*s/4) gives modulus exp(pi*Im(s)/4), cancelling
the gamma decay, while the damping has negative height-square sign.
Its horizontal factor is exactly bounded by exp(tau*R^2)*T^(-2).
The O(T) preliminary bound therefore costs only O(T^(-1)) there.
Choosing B9=max(B5,B8) controls all boundary sides by
B9*exp(tau*R^2)*T^e. For large t with tau<=1, undoing damping on
|Im(s)-t|<=R costs, together with the boundary cost, at most
exp(2R^2)<=exp(1/2). This makes the uniform constant in (10)
independent of a compact-height minimum or of d.

On the complex y-circle, the two gamma heights are t-v and t+v,
both in the smaller rectangle and both positive. Their sum is 2t;
thus their exponential factors multiply to exactly exp(-pi*t/2).
The polynomial exponent is 2q+2e=7/2+R+2e. At the real anchor,
the squared gamma power t^(sigma_eta-1) and squared polynomial
power t^4 give t^(7/2+eta). Uniform Stirling supplies a fixed positive
lower constant before the conversion to T, which costs at most a
fixed factor since t/T>=1/2 and 7/2+eta is bounded. Combining this
with (7) proves the positive model A with the same h for all heights.
The quotient exponent is exactly (R-eta)+4e=d+4d^2.

The full proof of L266's general interface was checked: the maximum
modulus principle gives M>=H_a(eta)>=A, Cauchy controls every
coefficient, and p^K<=A(1-p)/(2M) makes its tail-to-finite-sum ratio
at b strictly smaller than p<1. The factor (b/eta)^(2K) is positive
for every b>0 and cancels in that comparison; no uniform lower bound
on b is needed. L018 supplies a nonzero entire real Xi, and the
external premise plus reflection gives the closed bound |b|<=3/8,
which is still strictly below eta. L266 never divides by Xi(a), so
every central multiplicity is included, also when the first several
coefficients vanish. Evenness supplies the negative-center case.

Finally, every term in (13) is positive and the lower denominator
bound 2log(R/eta)>=2d/R has the correct direction. The geometric
prefactor is retained via 1-p>=2d. For d<=1/32, the leading
coefficient in (14) is at most 3/16+(15/8)d. A sufficient condition
for (16) is

    L*(log C0+(1/2)log L)/exp(L) <= 4.

Its left side tends to zero. Hence the audited upper quotient has
coefficient at most 3/16+(23/8)d, below the required 3/16+3d.
Both estimates concern the real quotient before taking its ceiling;
ceiling monotonicity introduces no unaccounted integer error.

Choose one onset above the finitely many thresholds for t>=8,
L>=1024, uniform Stirling, the logarithm condition, tau<=1, containment
of the smaller rectangle and the last displayed condition. The fixed
constants B_j,h,C0 can be chosen before this final enlargement.
Each condition holds for all larger T, so the resulting T0 works
simultaneously for every real center, every allowed displacement and
every central multiplicity. This closes the uniformity audit without
an endpoint claim: the error 3*log(T)/sqrt(log log T) still diverges.

## Mathlib

Full matching coverage and a formal verification of this quantitative
moving-anchor specialization have not been checked; absence is not
asserted. L005 records the supporting
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
The prior assessment inspected
[`Complex.HadamardThreeLines.norm_le_interp_of_mem_verticalClosedStrip'`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Hadamard.html),
which is a supporting strip theorem, not the three-circles inequality
or this witness result. Matching Borel--Caratheodory, analytic-log,
gamma, Cauchy and finite-rectangle API coverage remains unchecked.
No local Lean build or external import-closure verification is claimed.

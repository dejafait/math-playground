# Lemma 454: subendpoint uniform relative Mellin freezing

## Hypotheses

Assume the zeta specialization of OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
Theorem 1.1, at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
The precise citation and verification limits are retained in the
[external-input register](../foundations/2026-10-quasi-riemann-input.md).
The pole at 1 is allowed; no boundary assertion, independent manuscript
audit or local formal import-closure verification is assumed. Use the
separately audited L452 logarithmic-derivative and analytic-log bounds
under this input.

Let r tend to infinity through positive reals, and let m be a positive
even integer satisfying

    31/32 ≤ α:=m/r ≤ 63/64.

Set h=9/2+m/(2r) and a=sqrt(4π²exp(4r)−h²)>0. Define

    S=S_{r,m}(a)=Σ_{j,k≥1}(jk)^(-1/2)
        (1−log(jk)/(2r))_+^m exp(ia log(k/j)),
    c=m/(2r), σ=1/2+c, A=m!/(2r)^m,
    B=|ζ(σ+ia)|².

The sum is finite. All integrals below are ordinary absolutely
convergent integrals; vertical contour integrals are oriented upwards.

## Conclusion

There are fixed C,R>0, independent of r,m in this band, such that

    |S/B−1| ≤ C r^(-1/6)                              (1)

for r≥R. In particular B>0 and, on one uniform eventual ray,

    S ≥ B/2 ≥ (1/2)exp(−C r^(1/3)) > 0.              (2)

The complete contour identity retains both shifted-line residues:

    S=∫_ℝ K(v)F(v)dv+R_p,
    K(v)=A exp(2r(c+iv))(c+iv)^(-m-1)/(2π),
    F(v)=ζ(σ+i(a+v))ζ(σ+i(v−a)),
    R_p=2A Re[exp(2r(1/2+ia))(1/2+ia)^(-m-1)
                         ζ(1+2ia)],
    ∫_ℝ K(v)dv=1,   |R_p|/B≤exp(−r²)               (3)

eventually, after increasing R. This is a local known-method
specialization; originality is not asserted. It supplies an arithmetic
comparison only. No changed-band theta-sector approximation, Laguerre
sign, smaller-index completion, bounded-height extension, mixed
positivity or RH conclusion follows here. The separate critical audit
below validates this written specialization under the stated external
input; it does not verify that input's manuscript or formal import closure.

## Proof

The approved source comparison is
[the subendpoint assessment](../drafts/literature/2026-10-23-subendpoint-relative-mellin-coverage.md).
L303 supplies the scalar inversion and absolutely convergent series
mechanism, L307 the remote-pole bookkeeping precedent, and L330 the
integrated relative-variation mechanism. Their endpoint conclusions
are not invoked outside their domains. The changed line, exponent,
normalization and full tails are justified below. In particular no
Dirichlet or reciprocal Euler series is used at σ<1.

### 1. Uniform analytic inputs and the non-Euler normalization

Here

    31/64≤c≤63/128,
    63/64≤σ≤127/128,
    log a=2r+log(2π)+O(exp(−4r)).                     (4)

The last estimate is uniform because h ranges over a fixed compact
interval. In particular a is uniformly comparable to exp(2r).

L452 (1) gives |ζ'/ζ(σ+it)|≤C(log t)^(1/3), uniformly
on this real-part interval for sufficiently large positive t.
Its proof (8) also gives an analytic logarithm f_t of ζ on the
closed disk of radius R₁=131/128 about 2+it, with

    |f_t(s)|≤C(log t)^(1/3) on that disk.             (5)

Indeed L452's interpolation exponent is strictly less than 1/3.
Every σ+it here lies in that disk, since
|2−σ|≤65/64<131/128. Taking real parts of the actual analytic
logarithm therefore proves both bounds

    exp(−C(log t)^(1/3))≤|ζ(σ+it)|
                         ≤exp(C(log t)^(1/3)).        (6)

These are not continued Euler-series inequalities. At t=a they give
B≥exp(−C r^(1/3))>0. At t∈[a/2,3a/2] they hold with
the same exp(±C r^(1/3)) bounds and one uniform onset.

For all real t, including zero, L452 (4) gives

    ζ(s)=s/(s−1)−s∫_1^∞ {u}u^(-s-1)du, Re s>0,

away from the pole. On the compact σ interval in (4),
|s−1|≥1/128 and the integral is bounded by 1/σ. Hence

    |ζ(σ+it)|≤C(1+|t|) for every real t.              (7)

The same formula bounds ζ uniformly by O_a(T) on the horizontal
segments used below at height ±T when T>2a+2, with real parts of
the zeta arguments between σ and 3/2. Thus it supplies contour
growth as well as the far-tail bound. This elementary formula is
already proved in L452; it is not a new source assertion.

### 2. Inversion and the two crossed poles

Work first at fixed r,m,a with m≥6. L303's scalar inversion, with
exponent m and t=2r−log(jk), gives on Re z=1

    S=A/(2πi)∫_(1−i∞)^(1+i∞) exp(2rz)z^(-m-1)
                       ζ(1/2+z+ia)ζ(1/2+z−ia) dz.   (8)

The absolute Fubini majorant is

    A exp(2r)ζ(3/2)²/(2π)
                  ·∫_ℝ(1+v²)^(-(m+1)/2)dv<∞.

This verifies the specialization at exponent m without assuming that
the original endpoint weights or their tail bound apply here.
The scalar inversion follows also from the inverse Laplace formula
[DLMF 1.14.20](https://dlmf.nist.gov/1.14.E20) for t_+^m/m!,
with transform z^(-m-1) on Re z>0; continuity, piecewise continuous
derivative and exponential growth hold for m≥1.

Shift (8) to Re z=c. The original product is meromorphic, and its
only poles in c≤Re z≤1 are z=1/2+ia and z=1/2−ia.
They are distinct because a>0. The pole at z=0 is not crossed.
The simple zeta pole at 1 has residue 1, as in
[DLMF 25.2(i), 25.2.4](https://dlmf.nist.gov/25.2).
At the upper pole the other factor is ζ(1+2ia); at the lower
pole it is its complex conjugate. Their residues, after multiplication
by A, sum to precisely R_p in (3), with a plus sign for a shift
from the right upward line to the left upward line.

For T>2a+2 the product on either horizontal edge is O_a(T²)
by the formula preceding (7), while z^(-m-1)=O(T^(-m-1)).
All remaining factors and the horizontal lengths are bounded at
fixed parameters. The edges are O_{r,m,a}(T^(1-m)) and vanish
as T→∞. On Re z=c, (7) gives a product O((1+a+|v|)²),
so absolute convergence follows for m>2. Residue theory now proves
the first identity of (3) for every fixed parameter. Uniform estimates
will follow separately, rather than from the fixed-parameter edge
constants. Scalar inversion at t=2r on the positive line c gives
∫K=1 exactly; it requires no zeta expansion on that line.

### 3. Uniform bounds on the changed kernel

Write

    |K(v)|=P₀(1+(v/c)²)^(-(m+1)/2),
    P₀=A exp(2rc)c^(-m-1)/(2π).

Here 2rc=m exactly. Positive-real Stirling
[DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3) therefore gives

    P₀=sqrt(m)/(c sqrt(2π))(1+O(1/m))≤C sqrt(r).      (9)

The error and constants are uniform because m/r and c stay in the
displayed compact positive intervals. For |v|≤c, the elementary
inequality log(1+x²)≥x²/2 at |x|≤1 yields

    |K(v)|≤C sqrt(r)exp(−rv²/4).                     (10)

For this weaker exponent it suffices that
(m+1)/(4c²)≥r/4, which follows from c≤1/2 and m≥31r/32.
For |v|>c set x=|v|/c>1 and use

    (1+x²)^(-(m+1)/2)
       ≤2^(-m/4)(1+x²)^(-m/4-1/2).

For large m the last power is at most (1+x²)^(-2).
Its integral is finite independently of m, giving an outer mass
O(sqrt(r)2^(-m/4)). Fix δ=1/8<c. Splitting the Gaussian
in (10) into two equal factors proves

    ∫_ℝ|K(v)|dv≤C,
    ∫_{|v|>δ}|K(v)|dv≤C exp(−r/512).                 (11)

Indeed δ²/8=1/512, and the outer mass just bounded decays faster,
since (31/128)log 2>1/512. These estimates treat the entire real
line and do not assume K is a positive measure.

### 4. Relative variation on the fixed central window

Let g=ζ'/ζ and M=sup_{|t|≤δ}|g(σ+i(a+t))|.
L452 (1) and (4) imply M≤C r^(1/3). Both positive heights
a±t exceed its fixed onset uniformly. Conjugation gives the same
bound for g(σ+i(t−a)). The complete quotient identity is

    F(v)/B=exp(Q(v)),
    Q(v)=i∫_0^v [g(σ+i(a+t))+g(σ+i(t−a))]dt,
    |F(v)/B−1|≤2M|v|exp(2M|v|), |v|≤δ.              (12)

It follows by logarithmic differentiation and the value one at v=0;
all factors are nonzero under the pinned half-plane input. No
identification of the two factors as conjugates at v≠0 is made.
Using (10), w=sqrt(r)v and p=M/sqrt(r), the central error is at most

    C p ∫_ℝ |w|exp(−w²/4+2p|w|)dw=O(r^(-1/6)).      (13)

For sufficiently large r, p≤1 and this integral is bounded by
the fixed finite integral with p=1 in its exponent. The estimate
is integrated variation, with no supremum-window logarithmic loss.

### 5. All relative tails and the residues

For δ<|v|≤a/2, the two absolute shifted heights are in
[a/2,3a/2]. By (6), conjugation and the lower bound for B,

    |F(v)/B−1|≤C exp(C r^(1/3)).

Consequently (11) bounds this entire part of the relative error by

    C exp(−r/512+C r^(1/3))=o(r^(-1/6)).             (14)

This step uses a fixed δ; it does not multiply a bound
exp(C r^(1/3)) by merely exp(−c(log r)²).

For |v|>b:=a/2, (7) gives |F(v)|≤C v², uniformly even
where one shifted height is zero. From (9), c≤1 and b≥1,

    ∫_{|v|>b}|K(v)|(|F(v)|/B+1)dv
      ≤C sqrt(r)exp(C r^(1/3))
             ·[b^(2-m)/(m−2)+b^(-m)/m]
      ≤exp(−r²)                                     (15)

eventually. For the last inequality, (4) gives log b=2r+O(1),
so the logarithm of the preceding bound is
−2mr+O(r)+O(r^(1/3))+O(log r). Since m≥31r/32,
this is at most −r² for sufficiently large r, uniformly in m.
The estimate retains the full unbounded region, including both
small-shifted-height neighborhoods.

Finally A≤1, since m!≤m^m and m/(2r)<1. L452's elementary
formula at s=1+2ia gives |ζ(1+2ia)|≤C a for a≥1;
there is no encounter with its pole because a>0. Since
|1/2+ia|≥a, each residue in (3), divided by B, has modulus at most

    C A exp(r)a^(-m)exp(C r^(1/3)).

Its logarithm is again −2mr+O(r)+O(r^(1/3)); absorbing the
factor two proves |R_p|/B≤exp(−r²) uniformly. This proves the
last assertion of (3) without discarding a crossed pole or using a
residue-dominance argument.

Combine (3) and ∫K=1 to write exactly

    S/B−1=∫_ℝ K(v)(F(v)/B−1)dv+R_p/B.

Equations (13)–(15) and the residue bound prove (1). Interchanging
j,k in the finite sum proves that S is real. Thus (1), with one
uniform onset, and B≥exp(−C r^(1/3)) prove (2). ∎

L304's coefficientwise loss is not used. L330's old-envelope models
do not satisfy the strengthened fixed-domain input. L335 concerns
fixed r and arbitrarily large heights or arbitrary multiplicative
phases, not the coupled domain (4). L327's obstruction to a
phase-uniform PSD replacement is likewise not contradicted. None of
these historical stops is erased. The independent changed-band sector
and initial low-index gaps remain open.

### Critical audit — 2026-10-23

**Verdict and scope.** Conclusions (1)–(3) pass the separate mathematical
audit on the entire stated band, including its endpoints, with one
uniform eventual onset. No correction or additional hypothesis is
needed. This validates a local reproduction of the assessed methods,
not a result beyond the sources checked. The precise September 30
Theorem 1.1 and pinned commit in the Hypotheses remain an external
assumption with unaudited manuscript/import closure. The approved
[audit coverage](../drafts/literature/2026-10-23-subendpoint-relative-mellin-critical-audit-coverage.md)
is reused; no new source theorem or changed-band sector result is imported.

**Exact inversion and contour.** The Laplace transform of t_+^m/m!
is z^(-m-1) for Re z>0. Multiplication by A=m!/(2r)^m at
t=2r−log(jk) yields precisely the displayed weight, including value
zero at t=0; there is no endpoint half-weight for m≥1. On Re z=1
both Dirichlet factors have real part 3/2. The absolute Fubini
majorant in Section 2 is finite, so the initial identity holds for
the full double sum, not only a truncated expansion. Eventually m≥6
uniformly. On either horizontal edge with T>2a+2 the zeta arguments
have real parts in [σ,3/2] and imaginary parts of absolute size
comparable to T. L452 (4) bounds their product by O(T²); at fixed
parameters the edge integral is O_{r,m,a}(T^(1-m)) and tends to
zero. The shifted vertical integral is absolutely convergent by (7)
for m>2. Thus no uniform-in-parameter contour limit is being inferred
from a fixed-parameter estimate.

The two crossed poles are strictly inside the strip because c<1/2<1.
At z=1/2+ia the pole belongs to ζ(1/2+z−ia), whose residue with
respect to z is one; the other value is ζ(1+2ia). At z=1/2−ia
the residue is the complex conjugate, since A,r,m are real and the
power is an integer. A positively oriented rectangle has the right
edge upwards and left edge downwards, so right integral equals left
integral plus these residues. This checks both the factor two and the
plus sign in (3). The pole at zero is outside. Applying the scalar
inversion alone at t=2r on Re z=c gives ∫K=1 exactly, with the
same A; it uses no Dirichlet expansion on that line.

**Uniform kernel estimates.** The exact relation 2rc=m gives
P₀=m!e^m m^(-m)/(2πc), hence (9) by positive-real Stirling,
uniformly since c∈[31/64,63/128] and m∈[31r/32,63r/64].
The true stationary point of exp(2rz)z^(-m-1) need not equal c;
neither (9) nor exact normalization assumes it does. For |v|≤c,
log(1+(v/c)²)≥v²/(2c²) gives exponent
−(m+1)v²/(4c²)≤−rv²/4. For |v|>c the split in Section 3
uses 1+(v/c)²≥2, leaving an integrable power at least two when
m≥6. Its mass is O(sqrt(r)exp(−(m/4)log 2)). On
δ<|v|≤c, split exp(−rv²/4) into two identical factors;
one is at most exp(−rδ²/8)=exp(−r/512), and the other has
integral O(r^(-1/2)). Since (31/128)log 2>1/512, the outer
mass also fits (11) after absorbing sqrt(r) with the strict exponent
gap. These bounds justify the complete absolute mass and tail in
(11), without interpreting K as a positive measure.

**Normalization and central variation.** The largest distance of
σ+it from 2+it is 65/64=260/256, strictly inside L452's
R₁=262/256 disk. Its actual analytic logarithm therefore supplies
both sides of (6), including the lower bound for B, with constants
independent of σ. This uses L452 proof (8), not a reciprocal Euler
series at σ<1. The derivative estimate L452 (1) covers the closed
σ interval as well. For |t|≤δ, both a+t and a−t are positive
and above the source onset for all sufficiently large r uniformly.
Conjugation identifies g(σ+i(t−a)) with the conjugate of
g(σ+i(a−t)); it does not identify F(v) with a modulus square
away from v=0. Differentiating F/B and matching its value one at
zero proves (12) for positive and negative v. With
p=M/sqrt(r)=O(r^(-1/6))≤1, the absolute central error is
bounded by C p times the fixed finite integral

    ∫_ℝ |w| exp(−w²/4+2|w|) dw.

Thus (13) holds without a supremum-window logarithmic loss. The
fixed width δ is legitimate even though the endpoint of its
pointwise exponential variation bound grows with r: Gaussian
integration, not a uniform smallness claim on that window, is used.

**Complete middle, far and residue contributions.** For every
δ<|v|≤a/2 both absolute shifted heights lie in [a/2,3a/2].
Their logarithms are 2r+O(1) uniformly. Equation (6), conjugation
and the same lower bound for B yield |F/B−1|≤C exp(Cr^(1/3)).
Multiplication by (11) proves (14) on this entire region. The
strictly linear decay −r/512 dominates Cr^(1/3); a shrinking
window with only exp(−c log²r) decay would not justify this step.

At arbitrary real shifted height t, |σ+it−1|≥1/128 and
σ≥63/64. In L452 (4) the integral has absolute value at most
1/σ, so (7) holds uniformly through t=0. For |v|>b=a/2≥1,
it gives |F(v)|≤C v² since a<2|v|. Also
|K(v)|≤C sqrt(r)|v|^(-m-1), using c≤1 in (9).
Integrating these powers over both rays gives exactly the two
terms b^(2-m)/(m−2) and b^(-m)/m in (15), up to one fixed
constant. Since log b=2r+O(1) and m=O(r), the logarithm of
this complete relative bound is at most

    −(31/16)r²+O(r)+O(r^(1/3))+O(log r).

All constants are band-uniform. It is consequently at most −r²
on one eventual ray. This includes the neighborhoods v=±a where
one shifted zeta height vanishes; no large-height estimate is used
there. For the residues, m!≤m^m and m/(2r)<1 give A≤1.
L452 (4) at 1+2ia yields |ζ(1+2ia)|≤Ca for a≥1.
Together with |1/2+ia|≥a and the same B lower bound, the sum
of the two relative residue moduli is at most
C exp(r)a^(-m)exp(Cr^(1/3)). Its logarithm has the same
negative quadratic leading bound, and is eventually at most −r².
Both residues are therefore retained before being bounded; neither
is omitted or used as a positivity-dominating term.

**One onset, reality and remaining gaps.** Take the maximum of the
finitely many thresholds for m≥6, a/2≥max(1,t₀), L452's
logarithm/derivative bounds, p≤1, the estimates (14)–(15) and
the residue estimate. All depend only on fixed band endpoints and
the external input's constants. The exact identity ∫K=1 then
gives the claimed error (1). Increase this same onset so that its
upper bound is ≤1/2. The finite sum is real by exchanging j,k,
and B>0; hence S≥B/2 and (2) follow with a fixed enlarged C.
This proves the uniform quantifiers, without an explicit numerical
onset or any extrapolation from sampled values.

The direct mathematical uses remain scalar inversion/Fubini from
L303, relative variation from L330 and analytic bounds from L452.
L307 and L453 are only method precedents; their conclusions are not
inputs on this band. The recorded L304 coefficient loss, L330
older-envelope models, L335 fixed-r/arbitrary-phase negatives and
L327 phase-uniform PSD obstruction retain their original scopes.
No dependency change is needed. In particular the audit supplies
no theta-sector reduction on this band, additional Laguerre sign,
initial low-index completion, bounded-height result or RH conclusion.

## Mathlib

The full relative comparison and its changed-contour specialization
have not been checked for matching Mathlib coverage; absence is not
asserted. Supporting scalar inversion, residue theory, Stirling and
analytic-logarithm APIs were not checked here. L452 records supporting
Euler-log coverage, but no Euler expansion at σ<1 is used. The pinned
external artifact `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`
is an external supplied result with the register's qualifications,
not a claim of local compilation or Mathlib membership.

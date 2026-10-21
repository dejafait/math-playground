# L082 — Both selected continuum diagnostics are strictly negative

## Hypotheses

Keep L008's actual SU(2) probes and tau=1/16, L080's continuum
diagnostics D_i (i=3,6), and L081's exact rectangular truncation K=96.
The box is (-4,4)^4 with its relative one-form modes, the physical
weight is (x_1+4)u_1, the upper curvature has positive orientation,
and the lower-rooted prefix retains its constant component-1 mode.
Only the probe strain is restricted to Psi_13, using L081's proved
rectangular swap cancellation. No mode or transition coefficient is
deleted according to a numerical threshold.

Import the exact cutoff polynomial residual established in L036,
and precisely L037's saved hexadecimal Fourier table and certified
exact-rule node/weight/cutoff intervals at scale S=10^180. Future use
must match that table or recheck it. Retained tensor arithmetic obeys
L039's explicitly qualified IEEE binary64 addition/multiplication/FMA
model, arbitrary summation order, no overflow, and its stated underflow
allowance. This is an informal computer-assisted enclosure, not a
formal processor or BLAS verification.

## Conclusion

The full continuum diagnostics satisfy

    -237.289643 < D_3 < -237.289642,
     -98.877430 < D_6 <  -98.877429.                       (1)

The total errors against the certified dyadic retained centers are
less than 6.245e-8 and 2.345e-8, respectively. These include spatial
integration, both inverse-weight time integrals, primitive input and
tensor arithmetic, and L081's complete omitted-mode error.

Consequently L080's selected centered circulation/path trace obeys

    lim_(a->0) a^3 F_(i,N)^circ = 2 gamma D_i < 0,

with exactly the positive full-torus constant gamma already specified
there. This proves a nonzero a^-3 coefficient for that selected trace
and rules out an O(N^2) bound for that trace alone. It assigns no sign
or power coefficient to the complete direct first pair or mixed cubic
response: the centered path/path term may cancel it. L079's finer
remainder, other placements/jets, the full logarithm, matching and the
interacting reflected error <=c_box/2 remain open. No Yang–Mills
candidate or discovery beyond the assessed standard methods is claimed.

## Proof

### 1. Reduce every spatial integral to compact-cutoff moments

Put omega=pi/8 and

    F_h(n)=integral_(-3)^3 x^h rho(x) exp(i omega n x) dx.

In L081(4), a row factor is a relative sine/cosine mode, its first
derivative, a constant upper evaluation, or the exact component-1
prefix. For n>0 their formulas are

    v_n(x)=sin(n omega(x+4))/2,
    e_n(x)=cos(n omega(x+4))/2,
    v'_n(x)=n omega cos(n omega(x+4))/2,
    e'_n(x)=-n omega sin(n omega(x+4))/2,
    p_n(x)=sin(n omega(x+4))/(2n omega).

Also e_0=1/sqrt(8), e'_0=0, p_0=(x+4)/sqrt(8).
Upper evaluations are v'_n(4)=(-1)^n n omega/2 and
e_n(4)=(-1)^n/2, with e_0(4)=1/sqrt(8). Each is thus a
finite polynomial-exponential sum. Expand the phase shift exactly
using exp(i n omega*4)=i^n; it requires no approximate trigonometric
phase. For any row product g the coefficient weights give

    integral rho g = sum_g c_(n,h) F_h(n),
    integral f g   = sum_g c_(n,h) F_(h+1)(n),
    integral rho' g = -integral rho g',
    integral f' g   = -integral f g',
    integral f'' g  =  integral f g'',                    (2)

where f=x rho. Every integration-by-parts endpoint term vanishes:
rho and f, with all their derivatives, vanish at ±3 and in a
neighborhood of the integration-box endpoints ±4. The mode products
and prefixes are smooth; a mode's upper evaluation in this product
is a fixed coefficient, not a boundary trace being differentiated.
Finally the M weight hf=(x+4)x rho is handled by multiplying g by
x^2+4x before its moment expansion.

For nonzero modes the row-product frequencies have |n|<=2K=192.
Only the axial M factor contains a prefix; its upper factor is
constant in x_1, so the degree-2/3 moments there have |n|<=K=96.
All other row products have polynomial degree zero. Derivatives in
(2) do not raise polynomial degree, and f shifts it by one. Thus
the complete tensor needs exactly h=0,1, |n|<=192 and h=2,3,
|n|<=96. In particular the constant prefix produces an x^3 rho
moment; it has not been removed as a small-frequency special case.

The implementation represents sums by keys (n,h). Multiplication
convolves these keys, and differentiation replaces x^h exp(i n omega x)
by h x^(h-1) exp(i n omega x)+i n omega x^h exp(i n omega x).
Repeated use of these two identities implements (2) exactly, with
outward interval coefficients. The imaginary interval contains zero
for every real spatial entry; the real component encloses that entry.

### 2. Enclose the additional moments without differentiating rho

For h=0,1 import L037 directly, componentwise, with total complex
errors below 1.565e-13 and 3.333e-13. These bounds include L036's
quadrature error and apply to the exact saved dyadic values, at both
frequency signs. Bounding each real/imaginary error by the complex
error is valid even when the true moment component vanishes by parity.

For h=2,3 reuse the *same exact* 144-point four-panel rule and L036's
proved residual epsilon_rho<3.48e-14 for its degree-200 transition
polynomial. At the reduced frequency range |n|<=192,
|n omega|<=24pi<76. On the Bernstein ellipse of parameter 4 the
phase on a panel of halfwidth d is bounded by
exp(76d(4-1/4)/2). On a transition panel d=1/4 this exponent is
at most 35.625<36; on a core panel d=5/4 it is at most
178.125<179. Using e<3 and L036's Cauchy/Chebyshev estimate, choose
phase approximants of degrees 84 and 284 with errors bounded by

    delta_t=2*3^36/(3*4^84),
    delta_c=2*3^179/(3*4^284).

The transition approximation x^h p(x) times its phase polynomial
has degree <=200+84+h<=287. The core approximation has degree
<=284+h<=287. The standard Gauss–Legendre exactness and positive
weights therefore apply also for h=2,3; the phase approximation is
only auxiliary and need not be computed. Applying L036's inequality
|integral g-Qg|<=2 L sup|g-polynomial| on each panel gives

    E_h=2*3^h[epsilon+(1+epsilon)delta_t]
                      +10*(5/2)^h delta_c,
    epsilon=3.48e-14,
    |F_h(n)-F_h^Q(n)| <= E_h < 7e-14*3^h.                (3)

The last comparisons are exact rational checks in the certificate
generator. The two transition panels have combined length 1, the
two core panels length 5; negative panels use rho's evenness. This
specialization imports L036's verified approximation rather than
reproving it or assuming high-derivative bounds for rho.

Reuse all 288 certified positive-panel node, weight and rho intervals
from L037. Evenness gives, for n>=0,

    F_2^Q(n)=2 sum w x^2 rho(x) cos(n omega x),
    F_3^Q(n)=2i sum w x^3 rho(x) sin(n omega x).

Enclose the trigonometric factors by L037's reduced alternating
Taylor/double-angle algorithm, not machine sine/cosine; add (3)
outward. Negative frequencies are complex conjugates. All 386 new
moment records and 770 imported ones are saved, with exact interval
endpoints. Their parity reduction concerns the exact symmetric rule,
not a presumed symmetry of a floating numerical sum.

### 3. Control both complete inverse-weight integrals

Use L081's F=Delta^-1 exp(-tau Delta). A full retained eigenvalue
has three positive vertex indices and at most one zero edge index,
so

    lambda>27/64,   lambda<=4(K pi/8)^2<K^2<2^14.

For shifted time v=t-tau take the exact 28-point Gauss rule on
[0,2^-14] and on [2^j,2^(j+1)], j=-14,...,7. There are 644 nodes,
and the last endpoint is 256. Let B(lambda) be the exact rule's
weighted exponential sum. Import the standard Gauss–Legendre remainder
theorem with the interval-length coefficient specified in L039(4),

    C_m=(m!)^4/[(2m+1)((2m)!)^3],  m=28.

Its smoothness hypotheses hold for the entire scalar exponential.
On [b,2b] the normalized error is at most
C_m (lambda b)^(2m+1) exp(-lambda b)<=C_m(2m+1)!, using
the positive exponential series. On the initial panel lambda*2^-14<1
makes that normalized error at most C_m. The entire omitted time
tail is bounded by exp(-256*27/64)=exp(-108). Thus

    |lambda B(lambda)-1|<=epsilon_t,
    epsilon_t=C_28[1+22(57!)]+exp(-108).                  (4)

Apply (4) to the product of the two inverse weights. L081 gives
|P_(kl)|<=C_P=1296*1155*3/32 and |(B_i^A)_(kl)|<=C_i,
where C_3=3025 and C_6=820368. Its complete single-label heat sum
is at most 4*12^4. Therefore the difference between D_i^[96]
and its exact spatial/double-time-rule evaluation is at most

    T_i=C_P C_i (4*12^4)^2 (2epsilon_t+epsilon_t^2).       (5)

This estimates the signed trace by its absolute double-mode series;
it controls both tails and their corner, and does not assume a
nonnegative integrand. The spatial errors are separately propagated
below, so no approximate spatial operator norm is a premise of (5).
Outward integer evaluation of exp(-108) and exact rational arithmetic
give T_3<2.197e-12 and T_6<5.957e-10.

### 4. Retain every tensor term and arithmetic error

The generator is
`scripts/combined-ward-response/enclose_continuum_first_pair.py`.
It instantiates L081(3)–(6) with the formulas (2), retaining 12 M,
24 Q_3 and 96 Q_6 terms. Opposing component blocks yield 28 and
72 signed trace products. Algebraically canceling coefficient terms
remain present. There are 26 distinct spatial matrices; all their
enclosed center/radius arrays are saved. Their dimensions are at most
97, including the constant edge mode. Matching matrix factors with
their component heat matrices gives exactly L081(6).

Pi and 1/sqrt(8) are enclosed by L037's Machin and integer-square-root
constructions. The 28 disjoint root brackets have certified opposite
Legendre signs. Degree 28 identifies all roots; the standard positive
weight formula and exact affine maps enclose every time node/weight.
Each of the 62,468 heat entries is enclosed by L039's reduced
alternating exponential series and outward squaring. No machine
exponential, root proposal or approximate normalization is trusted.

Integer intervals are converted to dyadic midpoint-radius pairs only
after exact containment checks. Use L039's proved outward add/product
and dot rules. The dot rule is the specialization of Higham,
*Accuracy and Stability of Numerical Algorithms*, 2nd ed., SIAM (2002),
Lemma 3.1, with at most 2n+2 elementary operations and its conservative
G>10^-12. All coordinate dot inner dimensions are <=97. The final
644-node integral is split into blocks of at most 160 nodes, so every
dot obeys L039's n<=276 hypothesis. The underflow allowance remains
1e-290; all output arrays are finite, with nonnegative radii. Induction
through these actual operations encloses the exact-rule tensor with
the spatial-input errors included.

The certified centers and spatial/arithmetic radii are

    c_3 = -0x1.da944c04ffce3p+7,  r_3 = 0x1.0c2c4587eb9d9p-24,
    c_6 = -0x1.8b827cd87108bp+6,  r_6 = 0x1.889d45c9dde83p-26.

Add T_i and the strict L081 exterior error <4e-15. The total errors
are <6.245e-8 and <2.345e-8, against the initially chosen threshold 1.
Exact rational comparison of c_i±(r_i+T_i+4e-15) with the decimal
endpoints proves (1). In particular neither interval contains zero.

### 5. Full evidence, audit and limits

Reproduce the enclosure and its audit with

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/enclose_continuum_first_pair.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_continuum_first_pair_enclosure.py
```

The complete evidence is

    scripts/combined-ward-response/continuum-first-pair-enclosure-certificate.json
    scripts/combined-ward-response/continuum-first-pair-enclosure-factors.npz
    scripts/combined-ward-response/continuum-first-pair-enclosure-audit.json

The audit checks input identity/hashes, all 1,156 moment records,
all new exact-rule moment evaluations and imported-table error boxes,
all root/weight and mapped-rule records, every heat interval and its
dyadic conversion, complete component-pair coverage, archive finiteness
and nonnegative radii, and exact aggregate inclusion for all 100 signed
terms. It recomputes (4)–(5) and both strict negative signs. Spatial
matrix and tensor multiplication inclusion rely on the generator's
analytic identities and arithmetic induction; the audit does not
independently repeat those BLAS multiplications. This qualification is
part of the conclusion's arithmetic model, not an independent processor
verification claim.

The first audit failed because its heat-argument expression grouped
interval multiplication differently from the generator. Both expressions
enclose the same real number, but one interval need not contain the
other. Matching the generator's exact parenthesization repairs the
comparison; it changes no generator value or mathematical bound.
The final audit passes all records. A separate saved floating check,
`scripts/combined-ward-response/continuum-first-pair-spatial-crosscheck.json`,
compares every spatial matrix with L081's saved direct analytic-coefficient
quadrature. All 26 comparisons pass their stated tolerances. It is an
implementation diagnostic, not an interval inclusion premise.

Finally apply L080's already proved limit and gamma>0. Because (1)
is separated from zero, a^3 F^circ has a strictly negative limit and
F^circ cannot be O(N^2). This interpretation is restricted to that
selected centered circulation/path trace. No bound is inferred for
the complete first pair: simultaneous row centering also changes the
path/path allocation, and cancellation of its a^-3 coefficient must
be tested before drawing a conclusion about the response. All nine
placements and the other response jets remain. Shared quartic groups
must still be compared by subtracting the shared quartic once. The
finer a^2 remainder and logarithm, limiting interacting fields,
reflection positivity, infrared control and finite positive mass
remain unresolved.

## Mathlib

Full matching coverage for this continuous forest-diagnostic enclosure:
not checked. Supporting Fourier integration by parts, Gauss–Legendre
exactness/remainders, Chebyshev/Cauchy approximation, interval arithmetic
and floating-error results: not checked. No matching declaration or
absence claim is asserted. Existing canonical inputs and the precise
standard theorem/Higham citation above are used within their hypotheses;
the certificate is not a Mathlib formalization.

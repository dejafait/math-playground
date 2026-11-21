# C998b: Endpoint budgets and a direct nested Carleman work stop

## Hypotheses

Use exactly C998a's three frozen real columns, exact neutral completion,
full unprojected residuals g_j, and r_j=P0g_j, with a=log(3)/4,
ell=2a, delta=.01, m=286 and J=14. Preserve the pinned652 archive,
all603 candidate interfaces, and every inherited source/core/arithmetic/
unreplayed c_* qualification. No reference, endpoint or free trial
coefficient is changed. Set tau=a*2^-80.

The invocation-start SPECIALIZE assessment655/comparison656 licenses
the present REPRODUCTION of a standard quadrature method. Import
Trefethen, *Approximation Theory and Approximation Practice* (2013),
Chapter19, Theorem19.3, equation(19.8) and its proof, PDFpp153-154 in
the [inspected book-content PDF](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf).
For a function analytic and bounded by M in the Bernstein ellipse E_rho,
rho>1, its (n+1)-point Gauss error on [-1,1], n>=1, is at most
(64/15)M rho^(-2n)/(rho^2-1). The theorem is imported, not reproved.
The assessment inspected its hypotheses and proof; no new source is used.

For the work test specify the following proposed implementation. On
each retained outer formula interval use at least37 Gauss points;
additional endpoint grading or subdivision is permitted. Compute each
Carleman value by direct inner summation on

    [0,tau], [tau,2tau], ..., [a/2,a].                 (1)

For a panel of physical length h use n=32+ceil(1020h), hence n+1
Gauss points. Precompute inner density values, share denominators across
all six parity-column densities, and allow complete reuse at reflected
outer points. The remaining scalar products are accumulated directly for
each density. No fast Cauchy transform, algebraic compression between
densities or special-function evaluation is part of this prescription.
Its declared execution ceiling is100,000,000 real coefficient-times-kernel
contributions, before scalar precision or other action work. This is an
operational limit for this test, not a mathematical complexity threshold.

## Conclusion

For all three columns, the FULL unprojected residual satisfies, with
t=min(x,ell-x),

    |g_j(x)| <= 1408+16 log(2a/t)   almost everywhere. (2)

The two discarded endpoint intervals have squared-mass allowance less
than2^-54 and allowance less than2^-68 for EACH moment against
exp(+/-x/2). Interface neighborhoods specified below have respective
allowances less than2^-87 and2^-97. These bounds include the cross
terms of the full residual; they are not separate-component norm claims.

With exact scalar inputs and exact Gauss nodes/weights, (1)'s full
Carleman truncation error at every real tau<=t<=a is at most

    1296*2^-64 < 2^-53                               (3)

for each parity and column. There are3031 inner nodes. Even after the
specified reuse, the proposed direct nested implementation has at least

    6*(302*37)*3031 = 203210364                      (4)

coefficient-times-kernel contributions, exceeding its declared ceiling.

This is a local NEGATIVE decision for the specified direct summation,
not a negative residual or matrix result. No outer quadrature error,
finite scalar precision, full forcing evaluation or Gram-subtraction
ledger was completed after the work test failed. In particular (3) is
an exact-arithmetic inner truncation bound, NOT a computed value enclosure
or a sufficient full norm certificate. None of the three residual norms
was evaluated, and enclosure width1e-4 remains unpaid. Other degrees,
reorganized evaluators and faster transforms are not ruled out. There
is no necessary complexity lower bound, runtime estimate or new general
quadrature theorem here. The652 uniform-output stop is unchanged.

## Proof

### 1. Frozen envelopes and full pointwise endpoint control

C998a(7) gives F,H,V for f,h,q, also bounding each parity density.
Exact substitution of all frozen dyadics gives F+H<32 and V<16 for
each column. The calculation below independently checks these particular
inequalities against the complete654/655 ledgers and the pinned archive.

The translation part of Tf+T*h is bounded by16(F+H). The entire
continuous forcing is bounded by F+H, using C998a(18), ell<1 and
the L1 bounds. The finite diagonal (D-delta)q is bounded pointwise
by21V, using the coefficientwise bound from C998a Section4. In each
parity, h_m and the full finite E sum have pointwise bounds3.5V and
18V. Reconstruction multiplies their combined bound by at most
sqrt(2), and sqrt(2)*21.5<33. For the singular part,

    |C_end v(t)| <= V log(1+a/t),

so its coefficient1/2 and inverse parity reconstruction give an upper
bound V log(2a/t). Therefore

    |g(x)| <= 17(F+H)+54V+V log(2a/t),

which implies (2). These are bounds on the actual full expression,
not on a forcing prefix or an H1 norm used as a supremum bound.

Put A=1408, V_*=16 and L=log(2a/tau)=81log2<81. For the union E
of the two endpoint intervals, (u+v)^2<=2u^2+2v^2 and the
logarithmic-square integral in C998a Section3 give

    integral_E |g|^2 <= 4tau[A^2+V_*^2(L^2+2L+2)],
    |integral_E g exp(+/-x/2)|
       <= 4tau[A+V_*(L+1)].                          (5)

Here |exp(+/-x/2)|<2 on the full cell. The first line bounds the
square of the complete sum; no log/jump/regular cross term is discarded.
Using a<3/10 and L<81 proves the claimed rational endpoint allowances.

### 2. Interface isolation and surviving intervals

In normalized coordinates x/a, the grid locations are i/286,
i=1,...,571, including the midpoint1. C998a's32 translation events
come in reflected pairs. For n in its16-member P7, one event is

    u_n=4log(n)/log(3)-2b_n,
    b_n=6 if n^2<3^7, and b_n=7 otherwise.             (6)

Choose the member min(u_n,2-u_n) in (0,1). There are285 grid events
and16 translation events strictly in that half, hence302 open formula
intervals before small exclusions. C998a proves exact distinctness;
the rational interval calculation additionally proves every neighboring
gap, including the endpoint gaps, exceeds2^-30 in normalized units.

To describe and verify that calculation without a transcendental oracle,
for 1<=r<=2 put z=(r-1)/(r+1). Its100-term lower bound and upper
remainder for log r are

    2 sum_(k=0)^99 z^(2k+1)/(2k+1),
    0 <= remainder <= 2z^201/[201(1-z^2)].             (7)

This follows from the positive atanh series and bounding every omitted
denominator below by201; convergence is absolute since0<=z<=1/3.
Write n=2^k r and use k log2+log r. Positive interval division in
(6) then yields all locations with widths less than2^-180. The
certificate records every interval and the complete minimum-gap bound.

Expand each location enclosure on each side by2^-120 in normalized
coordinates, also doing so at the exact midpoint. Each full neighborhood
has normalized length less than4*2^-120. The minimum-gap bound ensures
that these neighborhoods are disjoint, outside the endpoint intervals,
and leave all302 intervals on (0,a) nonempty. Their total physical
length is at most603*4*(3/10)*2^-120. On them t>=tau, so (2) gives
|g|<=1408+16*81=2704. Multiplying their length by2704^2 pays full
squared mass; multiplying by2*2704 pays each moment. Exact comparisons
give2^-87 and2^-97 respectively. Reflections use exact symmetry;
uncertain centers are not rounded to a grid location.

### 3. Complete inner quadrature error, including its near-zero panel

Every parity density is a finite cosine sum with frequencies k_n<2040.
Its coefficient absolute sum is bounded by V<16, by the same neutral
completion and normalization estimate as C998a(7). Consequently its
entire extension obeys

    |v(z)| <= V exp(2040 |Im z|).                      (8)

For an inner panel [l,l+h], the affine image of E_2 has leftmost real
part l-h/8 and |Im z|<=3h/8. Every panel in (1) satisfies h<=t+l
for every t>=tau: the first has h=tau,l=0; the others have h=l.
Thus throughout that ellipse,

    |t+z| >= (7/8)(t+l)>0,
    |v(z)/(t+z)| <= (8/7)V exp(3*2040h/8)/(t+l).      (9)

The integrand is holomorphic there, including on a neighborhood of the
closed ellipse. No endpoint singularity or branch is passed through:
the pole -t remains strictly to its left. The imported Gauss theorem
with rho=2, affine factor h/2 and its n+1-point convention yields

    error_panel <= (256/315)V [h/(t+l)]
                            exp(3*2040h/8) 2^(-2n).

Since log2>3/8, n=32+ceil(2040h/2) cancels the exponential factor
and bounds this by V*2^-64. The81 panels cover the ENTIRE input
interval [0,a], including [0,tau]; none of that density is omitted.
Summing proves (3). Input/output scalar uncertainty and numerical node
errors are explicitly outside this truncation estimate.

### 4. Exact work count and stopping decision

The normalized panel lengths are2^-80 twice, then2^-79,...,2^-1.
Interval (7) for a isolates every integer ceil(1020h); summing n+1
gives3031, with all81 degrees recorded. All six frozen parity-column
arrays have127 nonzero free coefficients. This shows that none is an
identically zero parity block; it does not assert rank6 or prohibit
algebraic relations or other methods of evaluating their transforms.

Each of the302 retained left-half formula intervals requires at least
37 distinct real outer nodes under the proposed prescription. Further
subdivision only increases this. Reflection maps the corresponding
right-half queries to the same t values, so count only302*37 distinct
t values, not twice that number. At each one the prescribed direct
evaluator accumulates3031 weighted contributions for each of six
densities. Shared reciprocals and precomputed density values do not
remove these six direct dot products. This proves (4) for this algorithm.

The count omits coefficient generation, scalar certification, outer
squares, the other finite action terms, the complete forcing and the
two projection moments. Even the counted work exceeds the declared
budget. Thus the full implementation is stopped at this stage, rather
than treating the remaining oracle work as free. This is a reason to
seek a different inner evaluator, not evidence against full residual
certification or the actual signed S3 comparison. In particular choosing
a different degree rule is not proved impossible by (4).

Reproduction command:

    python3 scripts/separation-seven/graded-nested-work-657.py

The full certificate is `scripts/separation-seven/graded-nested-work-657.json`.
All124 rational/preservation checks pass, with no failures. It records
the input hashes, exact envelope substitutions, every location interval,
all81 degrees, neighborhood/error allowances and complete work count.
It prints the actual count203210364, required ceiling100000000 and
`actual_norm_intervals: NOT_COMPUTED`. The analytic proof above is not
replaced by these arithmetic checks. This result has not yet had a
separate conceptual audit; its limited route decision makes no RH claim.

## Mathlib

Full matching coverage of this fixed nested quadrature prescription and
its work count was not checked. Unknown coverage is not evidence of
absence. The supporting general quadrature theorem is the precisely
cited Trefethen theorem; elementary logarithmic integration, finite sums
and interval comparisons supply the local specialization.

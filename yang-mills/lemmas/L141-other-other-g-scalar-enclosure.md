# L141 — Complete integer-interval enclosure of the G scalar

## Hypotheses

Import precisely L140(2)--(3)'s scalar and its normalized torus measure:

    g_G=-(1/4) integral XY(X-Y)^2/(X+Y+Z)^2,
    X=2-2cos(theta_2), Y=2-2cos(theta_3), Z=2-2cos(theta_4).

The integrand is assigned value zero at X+Y+Z=0. L140 already proves
absolute convergence, its strict sign and K_(i,G)=g_G B_(i,G).
The downstream scope is SU(2), both actual L010 probes i=3,6, the
straight direction-1 lower-rooted forest, all-face relative fixed links
on D=(-4,4)^4, tau=1/16 and bare small-coupling expansion at fixed
mesh before refinement. No new limit or change of physical form is made.

Import L127 proof section 5's integer interval arithmetic, Machin pi
enclosure and cosine Taylor remainder, and L135 proof sections 1--2's
normalized full-cell inclusion method. Neither source's scalar values
nor its integrand-specific corner bounds are imported. The different
corner bound needed for G is justified below. No physical moment,
machine-trigonometric or IEEE accuracy premise enters this enclosure.

## Conclusion

The complete universal scalar satisfies the strict rational bounds

    -61/1000 < g_G < -43/1000.                             (1)

Its exact saved enclosure has width below 17/1000, against the
precalculation threshold 1/20, and is contained in the proposed
interval (-1/8,-1/100). This replaces L140's less precise scalar
interval (-1/4,0) for future evaluation; the identity is unchanged.

B_(i,G) and hence both actual G signs remain unevaluated. This scalar
alone supplies no sign of L124's other/other sum or compensation with
the mixed group. R and the triplet transverse-H sign, finer scales,
other response jets, finite matching, interacting error <=c_box/2,
continuum axioms, reflection positivity, infrared control and finite
positive physical mass remain unresolved. There is no candidate solution.

## Proof

### 1. Full-domain inclusion and the origin cell

Write L=X+Y+Z and T=XY(X-Y)^2/(4L^2), so g_G=-integral T.
Each angle dependence is even. The normalized torus integral therefore
equals pi^(-3) times the integral over [0,pi]^3, with no omitted region.
For 0<=X,Y,Z<=4 and L>0,

    0<=T<= (X-Y)^2/16 <= L^2/16,                       (2)

because 4XY<=(X+Y)^2<=L^2 and |X-Y|<=X+Y<=L.
Thus T extends continuously by zero at the origin, and (2) bounds
that point and every surrounding cell. This specialization is needed
because L135's E-specific corner formulas do not enclose T.

Partition each true angle interval [0,pi] into n=64 equal intervals.
Every three-dimensional cell has exact normalized measure 1/n^3.
Uncertainty in the stored enclosure of pi affects endpoint values,
not that exact measure. The function X(theta)=2-2cos(theta) is
nondecreasing on [0,pi]. Its outward endpoint intervals consequently
enclose the entire X range of each interval; likewise for Y and Z.

Only cell (0,0,0) contains L=0. Its range is enclosed by
[0,L_upper^2/16], rounded outward. On every other cell the computed
lower endpoint of L is strictly positive, as checked in the calculation.
Use outward interval multiplication and division in the displayed
formula for T. For an interval [a,b], squaring has lower endpoint zero
if a<=0<=b, otherwise min(a^2,b^2); its upper endpoint is always
max(a^2,b^2). Both endpoints are rounded outward. This rule is used
for X-Y as well as L, so cells crossing X=Y retain their zero lower
range. All resulting T intervals are nonnegative. Complete range
inclusion, rather than a midpoint approximation, justifies integration
without a further quadrature-error estimate.

### 2. Certified arithmetic and complete aggregation

The reproduction commands, from the active notebook, are

    python3 scripts/combined-ward-response/enclose_g_scalar.py
    python3 scripts/combined-ward-response/enclose_g_scalar.py --audit

The script reuses L127's scale Q=10^30 and intervals [a/Q,b/Q].
Addition is exact. Multiplication takes the minimum and maximum of
all four endpoint products and rounds outward; division likewise
uses endpoint quotients after checking a positive lower divisor.
Arbitrary-precision integers prevent overflow. Squaring implements
the range rule above. No floating-point value is used for inclusion.

L127 section 5 gives pi=16 atan(1/5)-4 atan(1/239) with respective
60- and 20-term alternating-series enclosures. The stored bounds
satisfy 3<pi_lower<=pi<=pi_upper<22/7. Multiplication encloses
each endpoint angle j pi/64. The cosine polynomial through degree
94 has error bounded by 4^96/96!, because every enclosed angle is
below 4 in absolute value. Its interval recurrence and this remainder
enclose the true cosine. Intersecting cosine with [-1,1] and X with
[0,4] preserves inclusion. At j=0 and j=64 the exact values X=0
and X=4 are used. Thus all 65 endpoint records and all cell ranges
contain their exact values.

Let [l,h] be the exact integer sum of all 262,144 T-cell intervals.
The certificate records

    l=11338850078455782382109710470031292,
    h=15768004584691047255108811921254120,
    q=n^3 Q=262144000000000000000000000000000000.

The full-cell range inclusions and positive exact weights imply

    -h/q <= g_G <= -l/q.                               (3)

Exact rational comparison gives

    -61/1000 < -h/q <= -l/q < -43/1000,
    (h-l)/q < 17/1000 < 1/20,
    -1/8 < -h/q <= -l/q < -1/100.

This proves (1) and the declared thresholds. The approximate printed
interval [-0.060150164,-0.043254280] is for readability only;
(3) and the rational comparisons are the mathematical enclosure.

### 3. Full evidence and limits of the result

The full certificate is
scripts/combined-ward-response/g-scalar-enclosure-certificate.json.
It retains every node and cell including the corner, the exact total,
bounds, proposed thresholds, script/arithmetic hashes and failures.
The saved-record audit is
scripts/combined-ward-response/g-scalar-enclosure-audit.json.
It regenerates every endpoint and all 262,144 cell records, checks
every saved record and the complete sum, and reports zero failures.
The complete bounds, totals, origin cell and failure fields were
inspected. This is a full replay with the same implementation, not
independent arithmetic software or formal verification. The analytic
range proof above supplies the inclusion justification.

This is local reproduction of the previously covered integer-cell
method for the established G integrand, with no originality claim
beyond the checked sources. No Ward or flow theorem is reproved or
used to assign an isolated response coefficient. Both physical inverse
weights, upper cumulative constant, lower constant prefix and full
spectral-tail qualifications of L140 remain for B_(i,G)'s future
evaluation. In particular a negative universal scalar supplies no
actual-probe sign before that signed physical contraction is enclosed.

## Mathlib

Full matching G-scalar enclosure: **not checked**. Supporting normalized
integration, cosine monotonicity/Taylor bounds, interval inclusion,
finite sums and rational comparisons: **not checked**. Unknown
availability is not evidence of absence.

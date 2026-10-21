# L135 — Complete integer-interval enclosures of the two E scalars

## Hypotheses

Use L134's established scalar formulas for L101's E coefficient, with
normalized full-torus measure, and its exact identity beta_E=-1+integral J.
The downstream setting remains SU(2), both actual L010 probes i=3,6,
the straight lower-rooted direction-1 forest, all-face relative fixed links
on D=(-4,4)^4, tau=1/16, and fixed-mesh bare small-coupling expansion
before refinement. This lemma only evaluates the universal constants;
it changes no limit, probe, physical weight or normalization.

Import L127 proof section 5's integer interval arithmetic, Machin pi
enclosure and cosine Taylor remainder. Do not import its midpoint error
or L130/L131's different scalar values. No IEEE accuracy assumption,
physical moment table, axial-tail replacement or actual-probe sign is used.

## Conclusion

The complete L134 constants obey the strict rational bounds

    -903/1000 < beta_E < -871/1000,
    -178/1000 < alpha_E < -143/1000.                    (1)

In particular they meet the proposed containing intervals
(-93/100,-17/20) and (-11/50,-11/100). The achieved full-enclosure
widths are less than 0.032 and 0.034, respectively, compared with the
proposed interval widths 0.08 and 0.11. These are universal scalar
bounds, not a sign of K_(i,E)=beta_E U_i+alpha_E W_i.
The signed actual physical forms U_i,W_i, including W_i's upper axial
tail, and L124's ax,-Q,G,R terms remain unevaluated. No compensation,
finer-scale estimate, interacting bound or Yang--Mills solution follows.

## Proof

### 1. Complete angle domain and the singular cell

Write X=2-2cos(theta_2), Y=2-2cos(theta_3), Z=2-2cos(theta_4),
L=X+Y+Z. Import L134's exact identities

    beta_E=-1+integral J,   alpha_E=-integral A,
    J=X Z (Y+Z)(1-X/4)/L^2,
    A=(X-Y)^2 Z(Z+4)/(8 L^2).                          (2)

The integrals in (2) are normalized torus integrals. Every integrand
is even in each angle, so they equal pi^(-3) times the integral over
[0,pi]^3. Set both functions to zero at L=0. For 0<=X,Y,Z<=4,
L>0, all factors of J,A are nonnegative, and

    J=(XZ/L)((Y+Z)/L)(1-X/4) <= L/4,
    A <= Z(Z+4)/8.                                    (3)

For the first inequality use 4XZ<=(X+Z)^2<=L^2 and the other
two factors at most one. For the second use |X-Y|<=L. Both right
sides tend to zero at the origin, so these bounds include its continuous
value. L134 already establishes absolute integrability and the strict
signs; no numerical exclusion of the origin is needed.

Divide each true-angle interval [0,pi] into n=64 equal parts. Each
three-dimensional cell has exact normalized measure 1/n^3. The
uncertainty in the numerical enclosure of pi affects endpoint-value
enclosures, not this exact weight. The function 2-2cos(theta) is
nondecreasing on [0,pi], so endpoint intervals at j pi/n and
(j+1)pi/n enclose its entire range on the jth part. Use these three
ranges as independent X,Y,Z intervals; no angle region is omitted.

The sole cell containing L=0 is (j,m,p)=(0,0,0). On this entire
cell enclose J,A by [0,L_upper/4] and
[0,Z_upper(Z_upper+4)/8], rounded outward. On every other cell
the computed lower endpoint of L is strictly positive. Evaluate (2)
by interval operations there. For squaring an interval [l,h], use
zero as the lower bound if it contains zero, otherwise min(l^2,h^2);
the upper bound is max(l^2,h^2). Round both bounds outward. This
is needed for (X-Y)^2. The resulting cell intervals include complete
function ranges, so no derivative estimate or quadrature remainder
is required. All positive-divisor conditions are checked in the
calculation, including cells touching a coordinate axis.

### 2. Arithmetic inclusion, full aggregation and precise bounds

Reproduce from the active notebook with

    python3 scripts/combined-ward-response/enclose_e_scalars.py
    python3 scripts/combined-ward-response/enclose_e_scalars.py --audit

The script imports L127's arithmetic primitives from
scripts/combined-ward-response/check_joint_curl_tensor.py. Their
scale is Q=10^30: integers l,h represent [l/Q,h/Q]. Addition
is exact; multiplication and division use all endpoint products or
quotients and floor/ceiling rounding. Every divisor has a positive
lower bound. The square range is as described above. Arbitrary-precision
integers avoid overflow; no floating-point operation enters inclusion.

The Machin formula pi=16 atan(1/5)-4 atan(1/239), with respectively
60 and 20 alternating-series terms and the next-term bounds, gives
3<pi_lower<=pi<=pi_upper<22/7. L127 proves this construction.
Each endpoint angle is enclosed by interval multiplication. The cosine
polynomial through degree 94, equivalently degree 95 with zero odd
coefficient, has absolute remainder at most 4^96/96!, since all enclosed
angles have absolute value below 4. Interval recurrence includes the
polynomial. Intersection of the result with [-1,1], and of X with
[0,4], preserves the true value. The endpoints at angles 0 and pi
are replaced by their exact values X=0 and X=4. Thus all 65 endpoint
records and all cell ranges include their exact inputs.

Let [l_J,h_J] and [l_A,h_A] be the integer sums of the complete
262,144 cell intervals. The stored exact totals are

    l_J=25556077578266510283470393679904205,
    h_J=33689844213729289388003419359912614,
    l_A=37678272342448329130874470582315454,
    h_A=46564520586436529097213864207894278.

With q=n^3 Q=262144000000000000000000000000000000, the range
inclusion and exact cell weights imply

    -1+l_J/q <= beta_E <= -1+h_J/q,
    -h_A/q <= alpha_E <= -l_A/q.                       (4)

Exact rational comparison of (4) gives (1), including its strict
inequalities; their widths (h_J-l_J)/q and (h_A-l_A)/q are
strictly below 32/1000 and 34/1000. The floating decimal summaries
printed by the script do not enter this comparison or the proof.

Full certificate:
scripts/combined-ward-response/e-scalar-enclosure-certificate.json.
It records every endpoint, every cell including the corner, both
totals, exact rational bounds, proposed thresholds and all failures.
The full /bounds, /totals and /cells/0 values were inspected with the
shared JSON inspector. The audit replays every input and cell, verifies
the complete aggregation and exact final bounds, and reports no failures
in scripts/combined-ward-response/e-scalar-enclosure-audit.json.
This is full saved-record replay using the same implementation, not
independent arithmetic software. The analytic range-inclusion proof
above supplies the integration justification.

An earlier uncertified midpoint calculation was used only to choose
a feasible mesh and proposed thresholds. Neither its values nor a
preview of the cell table is proof. The enclosure uses the entire
torus and its corner, with no neglected angle tail. This is local
RESEARCH / REPRODUCTION progress by a standard interval method, not
a claim of originality or a determination of either actual E response.
All physical mode sums, R(x_1)'s retained upper tail, moving-cut
normalization and L134's complete spectral-tail qualifications remain
attached to subsequent evaluation of U_i,W_i.

## Mathlib

Full matching E-scalar enclosures: **not checked**. Supporting interval
integration, cosine monotonicity/Taylor remainder, finite sums and rational
comparisons: **not checked**. Unknown availability is not absence.

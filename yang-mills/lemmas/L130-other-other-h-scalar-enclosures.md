# L130 — Complete integer-interval enclosures of the three H scalars

## Hypotheses

Import L129(1)--(4), its absolute-convergence justification, and its
definitions of h_D,h_X,h_A. Retain that result's scope: SU(2), both
actual L010 probes i=3,6, straight lower-rooted direction-1 forest,
all-face relative fixed-link box D=(-4,4)^4, admitted even N, a=8/N,
tau=1/16, and the bare small-coupling coefficient at fixed mesh before
refinement. Here the integer n=512 is an integration subdivision count,
not the lattice mesh N. No lattice limit is newly taken.

Import L127 proof section 5's integer interval operations, Machin pi
enclosure, and cosine Taylor remainder. The new certificate uses these
same inclusion operations on entire integration cells, rather than
importing L127's midpoint derivative bound for different integrands.

## Conclusion

The three constants obey the rigorous strict bounds

    1/5 < h_D < 3/10,
    1/10 < h_X < 1/6,
    -7/20 < h_A < -1/4.                                  (1)

In particular h_D and h_X are positive and h_A is negative and nonzero.
These are universal torus scalars. They do not establish a sign for
their heat-weighted contractions with either actual probe, or the value
of K_(i,oo)+4 gamma D_i. The antisymmetric scalar tau retains L127's
existing bounds; xi and the five other L124 coefficients remain
unevaluated. No finer-scale/logarithmic estimate, interacting reflected
error <=c_box/2, continuum axioms, reflection positivity, infrared
control or finite positive mass follows.

## Proof

### 1. Enclose the full cells, including the origin

Write theta=theta_2 and phi=theta_4. Divide each interval [0,pi]
into n=512 equal parts and let

    C_(j,m)=[j pi/n,(j+1)pi/n] x [m pi/n,(m+1)pi/n],
    0<=j,m<n.

Each cell has normalized area 1/n^2 in L129(2). Cell boundaries
overlap only on measure-zero sets, so their integral contributions
sum to the full integral. There is no tail or omitted corner region.

For each endpoint j, the certificate encloses theta_j=j pi/n and
X_j=2-2 cos(theta_j) by integer intervals. Since 2-2 cos(theta)
is nondecreasing on [0,pi], an interval enclosing all X values on the
jth part is [lower(X_j),upper(X_(j+1))]. The same construction gives
the Z interval on the mth part. These ranges are contained in [0,4],
using intersection with that known exact range. X_0=0 and X_n=4
are assigned exactly. Thus k=X+Z is in [0,8], and a=1-X/4,
c=1-Z/4 are in [0,1] on every cell.

Only C_(0,0) contains the singular k=0 corner. On that entire cell
let K be the computed upper bound for k. L129(4) implies the valid
enclosing intervals

    F_D in [-4 sqrt(K),4 sqrt(K)],
    F_X in [0,2 sqrt(K)],
    F_A in [1-K/4-3 sqrt(K),1+K/4+3 sqrt(K)].             (2)

All endpoints in (2) are rounded outward by the integer interval rules.
The inequalities include the continuous corner values; no regularity
beyond L129's proved bounds is assumed. On every other cell the
verified lower endpoint of k is strictly positive. Evaluate L129(1)
and (3), retaining exactly their arithmetic expressions, on the X,Z
intervals. Every square root and division then has its required domain.
After computing u0,u1,v0,v1,w, intersect each range with [0,infinity).
This is legitimate because L129(10) represents each as the integral
of a nonnegative function; it is not a sign assumption for F_D or F_A.
Every resulting moment interval is checked to be nonempty.

Denote the resulting three cell intervals by [l_(s,j,m),u_(s,j,m)],
s=D,X,A. They include all integrand values on their cell. Monotonicity
of integration gives, without a midpoint approximation or smoothness
assumption,

    (1/n^2) sum_(j,m) l_(s,j,m) <= h_s
      <= (1/n^2) sum_(j,m) u_(s,j,m).                    (3)

This is the complete integration error control. In particular varying
the uncertain pi interval does not alter the exact normalized cell
weight 1/n^2: the cells are defined with the true pi and only their
endpoint values are enclosed.

### 2. Arithmetic inclusion and complete certificate

Reproduction commands from the active notebook:

    python3 scripts/combined-ward-response/enclose_h_scalars.py
    python3 scripts/combined-ward-response/enclose_h_scalars.py --audit

The implementation imports I, SCALE, atan_bounds and cosine from
`scripts/combined-ward-response/check_joint_curl_tensor.py`. As justified
in L127, with Q=10^30, intervals [l/Q,u/Q] use exact integer sums,
outward floor/ceiling of all four products or quotients, and integer
square roots with an exact square test. Denominators must have strictly
positive lower bounds. Arbitrary-precision integers avoid overflow.

The pi interval uses 60 and 20 alternating-series terms in
pi=16 atan(1/5)-4 atan(1/239), with exact rational bounds satisfying
3<pi_lower<=pi_upper<22/7. Each endpoint angle is enclosed by interval
multiplication. Cosine is evaluated by its polynomial through degree
94 and an absolute remainder at most 4^96/96!, since all enclosed
angles have absolute value below 4. Polynomial interval evaluation
and intersection with [-1,1] are inclusion operations. Thus every
endpoint interval encloses its exact value. These statements import
L127's primitive arithmetic proof, not its different quadrature bound.

The full certificate is
`scripts/combined-ward-response/h-scalar-enclosure-certificate.json`.
It stores all 513 endpoint records, all 262,144 cell records, the three
integer totals, exact rational normalized bounds, and all threshold
failures. The complete bounds from (3) are, with common denominator
q=262144000000000000000000000000000000,

    56790657288618164936088127830880287/q <= h_D
      <= 75330870384970390120505413974846173/q,
    32192412426822424216396911427756429/q <= h_X
      <= 38208403584545924139406170493869209/q.            (4)

For q_A=65536000000000000000000000000000000 they are

    -21784708052367876023803749527041121/q_A <= h_A
      <= -18482555946849456310714766022166529/q_A.        (5)

Exact rational comparison of (4)--(5) with the thresholds proves (1).
Their widths are respectively below 0.071, 0.023 and 0.051, against
required containing-interval widths 0.1, 1/15 and 0.1. The printed
floating-point decimal summaries are not used in these comparisons.
No IEEE or libm accuracy assumption is needed for the certificate.

The audit replays every endpoint, every cell, all three totals and
all final bounds, comparing the complete saved values rather than a
preview. It passes with no failures and writes
`scripts/combined-ward-response/h-scalar-enclosure-audit.json`.
The full selected /bounds and /failures were also inspected using
the shared JSON inspector. This is a complete saved-record replay
using the same implementation, not independent arithmetic software.
The analytic inclusion argument above supplies the integration theorem.

### 3. Relevance and limits

L129 already proved h_X>0. This step adds its magnitude enclosure,
h_D's positive sign and magnitude, and h_A's negative sign and magnitude.
The nonzero anisotropy must therefore remain in the actual contractions.
None of their separate signs determines a signed probe response:
L128 retains different physical bilinears, tau and xi, and L124 retains
five other coefficients. Those contractions and the complete comparison
are still required. This evaluation does not reopen ATTEMPTS/033--035's
failed universal deletion mechanisms.

The unchanged ready EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`
covers this bounded evaluation within the complete other/other target.
This is RESEARCH / REPRODUCTION: exact scalar formulas and primitive
interval machinery are imported, and complete cell integration supplies
the missing numerical bounds. It is local progress using a standard
enclosure method, with no claim of progress beyond the sources checked.

## Mathlib

Full matching H-scalar enclosures: **not checked**. Supporting interval
integration, cosine monotonicity/Taylor remainder, finite sums and
integer rounding: **not checked**. Unknown coverage is not evidence
of absence. The load-bearing proof and full exact certificate are
given here, and no numerical preview substitutes for either.

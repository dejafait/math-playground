# Corollary 426a: opposite conditional signs at the enclosing response endpoints

## Hypotheses

Use exactly L426's conditional angular mean A(g), its matrix P and
prescribed ordered selector, including both equality conventions. Keep
L419's first low/high pair and complementary order, and L425's exact
complementary gaps. Let

    a=164144438496585479013809/1000000000000000000000000,
    b=2496151417412820236290361/62500000000000000000000.

These are the complete `/g_full_range` endpoints in
`scripts/discriminant/bulk-haar-integral-enclosure-188.json`, including
the full-response and fixed-coefficient uncertainty. They are enclosing
bounds, with no assertion that either endpoint is attained by the
actual response. Assume correct execution of Python integer, Fraction
and integer-square-root arithmetic, with the outward operations and
Taylor remainders specified in L426's step-188 proof and L037.

## Conclusion

The complete angular certificates give

    -152385234424669149849/250000000000000000000000
        <= A(a) <= -21013347364350001167/62500000000000000000000
        < -1/3000,

    1/1200000 < 449171242469516857/500000000000000000000000
        <= A(b) <= 282960102104004192103/125000000000000000000000.

Thus A cannot have one strict sign throughout [a,b]. By its continuity
from L426 (17)--(18), it has at least one zero in (a,b). This rejects
only the tested uniform-sign sufficient condition on the full enclosing
interval. It neither signs I nor proves I=0, actual response support at
these endpoints, a transport defect, realization or rejection of L423,
actual clipping, a full-error regulator margin or any RH conclusion.
The separate step-198 critical audit below validates these enclosures
under the stated arithmetic contracts. The original arithmetic replay
alone was not an independent audit.

## Proof

This is RESEARCH / REPRODUCTION / calculation under the prior unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-17-bulk-haar-direct-conditional-sign.md`.
The general inclusion and quadrature methods are known. No progress
beyond the checked sources or mathematical originality is claimed.

**Imported quadrature and exact specialization.** Import the real
trapezoidal rule and its second-derivative remainder from
[NIST DLMF Section 3.5(i), (3.5.1)--(3.5.3)](https://dlmf.nist.gov/3.5.i),
version accessed 2026-10-17. On a closed C^2 cell of angular width h,
the absolute unnormalized error is at most h^3 sup|f''|/12.
For normalized coordinate t=theta/(2pi), a cell of mass m and
h=2pi m consequently has normalized error at most m h^2 sup|f''|/12.
This theorem is applied cell by cell, never across a selector tie.
L426 already proves continuity of A in g and domination for its
response derivatives. No response derivative is needed after the
opposite endpoint signs stop this test.

All numerical interval endpoints are integer multiples of 10^-24.
The implementation imports L426's already justified outward I
operations, P, Machin pi enclosure, sine/cosine Taylor bounds and
negative-exponential routine from
`scripts/discriminant/enclose_bulk_haar_integral.py`. It uses no
binary floating input for a proof decision. Printed decimals serve
only as summaries. The exact rational a, (a+b)/2 and b are converted
outward before evaluation. Source-coefficient and full-response
uncertainty are already inside [a,b]; conditional evaluation at its
fixed endpoints entails no further response truncation. The rounded
endpoint conversion and uncertainty in P, pi and elementary-function
evaluations remain in every retained interval.

**Second angular derivatives and branch validity.** Each real interval
jet is (v,d,e), enclosing a function and its first two ordinary angular
derivatives. Constants have (d,e)=(0,0). Product jets use

    (fg)'=f'g+fg',
    (fg)''=f''g+2f'g'+fg''.

For a strictly positive f and r=sqrt(f), the reciprocal and square-root
jets use

    (1/f)'=-f'/f^2,  (1/f)''=2(f')^2/f^3-f''/f^2,
    r'=f'/(2r),      r''=f''/(2r)-(f')^2/(4r^3).

Negative reciprocal intervals are handled by negation; all divisors
must exclude zero. Squares use the true interval square for their
value and 2ff', 2((f')^2+ff'') for derivatives. Sine and cosine jets
are (sin,cos,-sin) and (cos,-sin,-cos). Thus their derivatives are
with respect to theta, consistent with h in the imported remainder.
For w>=0 the exp(-w) jet is

    (exp(-w), -w'exp(-w), ((w')^2-w'')exp(-w)).

Induction over these exact differentiation identities and outward
interval operations proves enclosure of all three jet components.
For v=P u=(x,y,z), evaluate precisely L426 (17):

    exp(-g t)(g p+g^2 c),
    t=3(x^2+y^2), p=3(y^2+xz), c=-18y^2(x^2+xz).

Here g is constant under angular differentiation and t>=0. The three
state jets are averaged before bounding the absolute second derivative.

On a cell, all three original diagonal gaps must have strict signs.
The lexicographically first low/high pair is then constant. At each
stage, the positive root is (sqrt(off^2+high*low)-off)/high, with
high,low>0; when off>=0 the equivalent rationalized expression
low/(sqrt(off^2+high*low)+off) is used. A zero off-diagonal is harmless.
After the first rotation the ordered complement is (companion,e_k),
and its gaps are exactly (-D_k,D_k), as proved in L425. Both pair
orders, positive roots, radicands and divisors are retained in the
jet computation. Unit-vector coordinate and P-row norm bounds may
intersect only the value component of a jet; the derivative components
are unchanged. This is valid because the exact smooth selected vector
satisfies both the algebraic formula and those independent value bounds.

Any failed gap, radicand or denominator check receives the full bound
|Q|<=(1+sqrt(3g/80))/2 from L426 (13), for its complete angular cell.
Thus no finite neighborhood of a tie is omitted or assigned a smooth
branch. For strict cells, independently intersect the trapezoidal
integral enclosure with the direct interval range times m. Either
bound encloses the same complete cell integral. In particular a very
large derivative bound cannot invalidate that intersection; it merely
fails to improve the direct range on that cell. Endpoint evaluations
also use the full bound if their selector cannot be certified. These
are valid endpoint-value enclosures whenever the enclosing cell is
strict.

**Finite partition, error evidence and opposite signs.** Start with the
whole normalized angular interval [0,1]. Bisect a cell with greatest
maximum contribution width among the three response centers. Each
replacement has exactly the parent's union and mass. The 1582 final
closed cells therefore cover [0,1], with disjoint interiors; shared
endpoints have zero integration measure. Exactly 1558 cells certify
both strict stages. The 24 unresolved cells have total mass 3/32768
and retain the complete fallback. Every state, branch, jet, endpoint
value, second derivative, trapezoidal radius, direct range and final
intersection is stored in
`scripts/discriminant/bulk-haar-conditional-sign-194.json`.

The retained strict-cell width is approximately .000174592 at a and
.002059187 at b. The corresponding unresolved symmetric radii are
approximately .000049368 and .000101798. Arithmetic and fixed-matrix
rounding are included in these widths, rather than assumed negligible
or added twice. The raw sum of second-derivative trapezoidal radii is
large near branch boundaries (about 3379.38 at a and 2.885e9 at b);
these are valid but ineffective upper budgets on those cells. Their
intersections with direct ranges are essential. Trapezoids are narrower
than direct ranges on 1472 strict cells at a and 1338 at b; their
retained widths sum to about .000143958 and .001348441. On the other
86 and 220 strict cells the retained widths sum to about .000030634
and .000710746. Exact allocations are in
`scripts/discriminant/bulk-haar-conditional-sign-error-allocation-194.json`.
No small global angular derivative bound is claimed. The midpoint's
interval, approximately [-.00277618,.00170482], remains inconclusive.
The requested initial radius 1/10000 is not achieved; strict opposite
signs, rather than this requested accuracy, trigger the approved stop.

Exact rational summation of all final lower and upper cell endpoints
gives the two enclosures in the conclusion. A full replay in
`scripts/discriminant/verify_bulk_conditional_sign.py` recomputes every
terminal selector, vector jet, state jet and cell error; compares every
record; checks the complete partition, exact aggregates, rational sign
margins, work limits and stop condition. All 12 checks pass. Its full
result is
`scripts/discriminant/bulk-haar-conditional-sign-verification-194.json`.
This verifies the stored evidence under the stated arithmetic contract;
it does not independently verify Python or replace critical review of
the mathematical implementation.

**Work budget and failures preserved.** There were 43859 callbacks
through the first certified opposite signs, including two early failed
executions (42 callbacks in total). An interval/jet operand dispatch
error was corrected without accepting a numerical result. The first
verification comparison also failed because a Python tuple becomes a
JSON array; its deterministic recovery and the failed comparison cost
60 further callbacks. These failures and recovered counts are preserved
in the two `bulk-haar-conditional-sign-194-*-failed.json` records (the
generator failure record is named `bulk-haar-conditional-sign-194-failed.json`).
The successful complete replay costs 31274 callbacks. Total work is
75193, below 262144; initial work is below 65536. Each selector call
and each state-value/combined-angular-derivative call counts once,
including failed checks and cached results only when actually evaluated.
There are three response centers, 1582 leaves per integral, 24 decimal
places, no response slabs and no response-derivative callbacks. These
meet the assessment caps. No further refinement or transport was
performed after the opposite signs were found.

Reproduction commands:

    python3 scripts/discriminant/certify_bulk_conditional_sign.py
    python3 scripts/discriminant/verify_bulk_conditional_sign.py

The sign change follows additionally by the intermediate value theorem
and L426's entire continuation. The endpoint information alone says
nothing about the prime-Haar weighting between these scales. In
particular the stronger retained enclosure of I from step 190 and all
previous stopped implementations remain unchanged.

### Separate critical audit — 2026-10-17, step 198

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-bulk-haar-core-tail-critical-audit.md`.
No defect was found in the endpoint statement. This validates a local
known-method computation, with no stronger sign bound or novelty claim.
The precise DLMF quadrature input above and L426's compact response
domination are reused; no new source hypothesis is needed.

**Analytic inclusion and literal selection.** The complete base interval
implementation and angular-jet generator were inspected. Integer
floor/ceiling arithmetic encloses rational addition, products and positive
reciprocals; isqrt with an upward increment encloses square roots. The
48-term arctangent sum has positive next remainder, so its one-sided
Machin enclosure has the correct sign before multiplication by -4.
The cosine polynomial has degree 96 and remainder at most 7^97/97!;
the sine polynomial has degree 97 and remainder at most 7^98/98!,
which is smaller. The midpoint argument radius is added using the
unit derivative bound. For the negative exponential, the rounded reduced
argument remains at most 1/8; the degree-18 remainder and interval
squaring enclose the exact value at each endpoint. Monotonicity then
gives the full input interval. These are the explicit integer/Taylor
contracts of L426, not an appeal to unverified floating output or to
L037's distinct Decimal exponential implementation.

L425's positive square-root formula gives exactly the matrix P used
by the generator. Its row norms are sqrt(K_jj). Every first pair in
the saved strict cells is the lexicographically first low/high pair
from the original three gaps. The complementary order is exactly
(companion,e_k); its gaps are (-D_k,D_k), not a newly centered interval
matrix. Both signs of D_k occur and are retained. The positive root
solves high*eta^2+2*off*eta-low=0; the rationalized expression is the
same root. Switching expressions at off=0 changes no derivative.
Strict gaps make every radicand positive and the selected vectors
smooth on the entire closed cell. Coordinate intersections use unit
length and P's row norms only on the value component. Thus they do not
impose false bounds on first or second derivatives.

The product, reciprocal, square, square-root and exponential jet
identities in the proof agree with the implementation. Induction gives
inclusion of ordinary theta derivatives, including the averaged second
derivative of the three state functions. The bound is not a derivative
with respect to normalized t. Consequently the real trapezoidal error
is mass*(2*pi*mass)^2*sup|f''|/12. The closed-cell strict checks justify
its C^2 hypothesis. Endpoint values come from the same literal selector;
if an endpoint check fails, its full fallback still encloses the value.
Intersecting direct-range and trapezoidal integral bounds is valid even
when the latter has a very large error. No finite neighborhood of a tie
is treated as smooth. On unresolved cells the unit-state bound (13)
covers both equality conventions and the full cell mass.

**Complete finite evidence, not a sampled audit.** The complete replay
was run again: all 1582 records, all three response centers, every
vector jet, endpoint, strict-cell derivative/error and fallback agree.
All 12 replay checks pass. Independently of that shared-code replay,
`python3 scripts/discriminant/audit_bulk_core_tail_198.py` reads every
cell as exact rationals and verifies the entire partition, both pair
orders from the saved strict gaps, positive masses, integral/error
inclusion, exact aggregate endpoints and the complete error-allocation
companion. The 1558 strict cells have pair counts 726, 382 and 450
for ((1,0),(0,1)), ((0,2),(1,0)) and ((0,1),(0,1)), respectively,
in zero-based coordinates. The 24 unresolved cells have mass 3/32768.
The exact strict error allocations agree at all three centers, including
the inconclusive midpoint. The final endpoint rational sums are exactly
the conclusion above. No requested radius that failed is relabeled met.

The same audit follows all coefficient endpoints to L422's audited
certificate and its independent audit: S,T,B13,B14 and all six C_j
intervals agree exactly. It checks the literal alpha/theta formulas
with independent Fraction interval operations and re-evaluates all
64 response-head cells, the complete prime-power logarithmic tail,
its residual beyond 200 and its squared-modulus multiplier. Their
minimum/maximum is the saved full [a,b]. This verifies enclosing
support; it gives no endpoint attainability. The actual endpoint inputs
are their exact rational values, converted outward as required.

The complete rational supplement, including all angular aggregates,
is `scripts/discriminant/bulk-core-tail-audit-198.json`. Its eight checks
all pass; failures are empty. The first supplement execution stopped
at an overstrong JSON-object equality: the older audit stores its C_j
bounds separately and omits decimal previews. The exact rational
fields agree after matching that schema. This audit-checker failure is
preserved in `scripts/discriminant/bulk-core-tail-audit-198-failed-provenance.json`;
it accepted no result and evaluated no selector/state callback.

**Limits and work accounting.** The earlier failed executions contribute
42 callbacks and the failed verifier/recovery 60, as retained in their
records. Their sums and the full replay counts agree with the stated
75193 historical total. The new complete replay uses another 31274
callbacks. Shared-code replay plus the manual inclusion proof and
separate rational checks is the audit evidence; no independent proof
of Python or independent implementation of every jet is claimed.
The entire continuation from L426 justifies the intermediate-value
conclusion on (a,b). Nothing here determines the prime-Haar weight
between endpoints, I's sign, or any RH sign/exclusion range.

## Mathlib

Full matching coverage of this selector-specific conditional endpoint
certificate has not been checked. The general real quadrature and
continuity theorems are standard inputs, with the quadrature citation
above. Supporting interval, derivative or integration results would
not alone establish these finite branch and error checks. No Lean
verification or absence claim is made.

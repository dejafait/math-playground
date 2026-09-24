# Endpoint aggregate-region sweep test — 2026-09-24

Gap and target: the endpoint arithmetic margin at the prescribed
a_n=sqrt(4π²exp(4r)−25), r=2n, and the lower Laguerre signs
needed by the global witness argument remain unproved. Test the Haar
measure of L342's larger sufficient negative region, swept by the
prime-logarithm flow for time exp(2r). A bound strictly below one
would rule out uniform return at this scale for the aggregate region
itself. This could stop a return mechanism before further investment;
it would leave visits in the particular coupled interval, transfer to
a_n, and signs outside the sufficient region unresolved. If the
exponential-moment and time-grid bound does not fall below one, this
test alone supplies no obstruction or recurrence theorem.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md
and the global DAG before choosing work, and inspected the existing
changes. L340 obstructs an absolute Fourier certificate, L341 treats
only the smaller coordinate box, and L342 strictly enlarges that box
to B_r(θ)≤sqrt(r)/32. A covering deficit for a subset does not prove
one for this superset. The recorded search found no aggregate-region
measure bound. The new ingredient is a lower-tail exponential moment
on a thick shell of primes, followed by a Lipschitz time grid, instead
of the box's face-volume argument. The September 21 admission condition
is superseded by GOAL.md; its evidence and unfinished work are retained.

Unfinished reasoning saved before completing the proof: put L=sqrt(r)
and restrict the nonnegative budget to exp(4L)<p≤exp(6L). Mertens'
reciprocal-prime asymptotic from L338 and partial summation should give
shell weight at least L/6 eventually, since
2(exp(−2)−exp(−3))>1/6. Each shell weight is at most
48L exp(−4L). Under Haar measure, X_p=1−cos θ_p are independent,
with mean one and second moment 3/2. For λ=exp(4L)/(96L), the
quadratic exponential bound should give
E exp(−λ d_r(p)X_p)≤exp(−5λ d_r(p)/8), hence
μ{B_r≤L/16}≤exp(−exp(4L)/2304). L342's total weight bound
gives a flow derivative at most 42r eventually, so a grid of spacing
1/(1344L) enlarges the original threshold only to L/16. Its size
is at most 1+1344HL; log H=2r+O(1) should be negligible relative
to exp(4L). Check the strict shell constant, all endpoints, the
finite product moment, sweep covering, density and fixed-r quantifiers
before concluding. Zero consecutive unresolved exploration turns
precede this test.

Result: [L343](../lemmas/L343-endpoint-aggregate-region-return-obstruction.md)
proves the saved estimate. For all sufficiently large r, uniformly
over H≥0, the swept measure is at most
(1+1344H sqrt(r))exp(−exp(4sqrt(r))/2304). At
log H=2r+O(1) this is at most exp(−exp(4sqrt(r))/4608),
strictly below the required threshold one. Forward-orbit density
then gives arbitrarily late empty translated intervals of length
exp(2r) for each fixed large r. A length working for every translate
must instead satisfy log H≥exp(4sqrt(r))/4608. This weaker
exponential rate than L341's box estimate still exceeds 2r by a
diverging factor and now applies to the larger aggregate region.

WHY IT FAILS: the [canonical proof](../lemmas/L343-endpoint-aggregate-region-return-obstruction.md)
shows that the aggregate constraint still requires a large lower-tail
deviation of the independent Haar angles on a thick prime shell.
Its tiny measure survives the polynomial-size time mesh times H,
so the swept region cannot cover the torus on the coupled scale.
Density forces actual empty translated intervals. This stops uniform
return to the aggregate sufficient region itself, independently of
the Fourier certificate and without inferring a superset obstruction
from the old box. It does not rule out a visit in a specified interval
or negative values outside this sufficient region.

Assessment: NEGATIVE; stop uniform aggregate-region return at this
scale. Zero consecutive unresolved exploration turns; no RH candidate.
No arithmetic sign at a_n, Laguerre sign or zero-exclusion range
changes. The endpoint margin, low-index signs and global mixed
positivity remain unproved. The reason for the following direction
is to test the actual discrete coupled heights instead of recurrence
from arbitrary starting phases. L332's reduced-ratio expansion and
L333's continuous averages do not estimate the dyadic discrete mean
of |R_(2n)(a_n)|²; the search found no such result. A bound o(1)
would supply positive endpoint margins for a density-one subset of
those pairs, still leaving every exceptional pair and the remaining
low indices unresolved. It is an intermediate target, not an assumed
cancellation theorem. The sole concrete current action is in PROGRESS.md.

Verification: checked Stieltjes endpoints and the uniform o(L)
prime error, the strict shell constant, the finite exponential moment,
the enlargement from L/32 to L/16 on the entire continuous sweep,
closedness, translated forward density and the fixed-r quantifiers.
Seven exact rational checks passed for the shell slack, moment
exponent, time-grid budget and final rate. The proof needs no prime
table, numerical return calculation or new computational script.
Mathlib coverage is not checked; the inherited Mertens citation and
its supporting-only qualification are retained. The new DAG row
contains only genuine mathematical inputs; the overview records the
new obstruction without removing any inactive branch. All pre-existing
changes and unfinished work are preserved.

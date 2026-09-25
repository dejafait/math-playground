# Two-coordinate omissions via sparse affine lifting

Date: 2026-09-25. This is one bounded continuation of quotient geometry in
the frozen model, not a candidate solution of the grand challenge.

## Gap, target, and discriminating test

Gap: L005 determines only the one-coordinate-omission cell. L004's
certificate bound on wider cells need not be attainable, so it does not
determine the exact field-size threshold or maximal safe radius.

Intermediate target: establish E_C(delta)=3/q for 2/n<=delta<3/n when
1<=k<=n-6. Its downstream use is the exact safety condition q>=3/epsilon
on this cell, and a test of whether sparse error representatives force all
bad challenges to share one affine line. Wider cells, the sharp overall
threshold, and the ABF26 event, field-size, and endpoint correspondence
remain unresolved.

Test: rule out four bad challenges by lifting three quotient intersections
to error vectors of weight at most two; then construct three challenges
with the original same-support failure event. Continue if both the upper
bound and attainment survive. Abandon the formula if a fourth bad challenge
occurs under its hypotheses. Compare with epsilon=2^-128 and with L004's
existing sufficient interval, not just with its certificate count.

Redundancy: L005 uses independence of three coordinate images, which does
not directly control planes. Neither L003 nor L004 enforces compatibility
between the error representatives for distinct challenges. The stopped
endpoint and single-field disproof transfers are not reopened. The
[official statement](https://proximityprize.org/) was reread on this date;
its preliminary target and the qualifications in foundations/ are unchanged.
No new claim about the unread ABF26 definition is made. This step starts
with zero consecutive exploration turns.

## Saved unfinished reasoning

For each bad gamma choose a matching codeword and an error e_gamma of
weight at most two. Fix two distinct bad parameters and interpolate their
error vectors to an affine vector-valued function e(gamma). For any third
bad parameter, e_gamma-e(gamma) is a codeword supported on the union of
three sets of size at most two. The root bound gives minimum distance at
least seven, so this difference must vanish. Thus every bad parameter is
represented by the same sparse-coordinate affine function, supported on
at most four coordinates in total.

If its total active coordinate set has size three or four, weight at most
two requires respectively one or two coordinate zeros. Each active affine
coordinate has at most one zero, suggesting at most three bad parameters.
If the total active set has size at most two, closeness alone holds at every
parameter; the same-support failure requirement must instead force a zero
of some nonconstant coordinate. This case needs explicit care.

For attainment, use three coordinates with values gamma-alpha_i for three
distinct field elements alpha_i, and zero elsewhere. At each alpha_i the
error has weight two, while the direction has weight three. The minimum
distance condition should prevent the direction from agreeing with a codeword
on the same support. The argument may extend uniformly to r omissions when
3r<=n-k; that extension is part of the same lifting test if its small-active-
support case can be proved without an additional premise.

This reasoning is unfinished. No general upper bound or complete challenge
candidate is being asserted by this draft checkpoint.

## Completed assessment

The lifting test succeeds, including its small-active-support case. The
full statement and proof are in
[L006](../lemmas/L006-sparse-affine-lifting-sharp-error.md). The same argument
works for every integer r>=1 with 3r<=n-k, giving the exact error (r+1)/q
on r/n<=delta<(r+1)/n. This is one uniform completion of the proposed
two-coordinate test, not a separate research branch. The key point when
the active coordinate set has size at most r is that failure on the chosen
support forces a nonconstant coordinate to vanish there. Closeness alone
would falsely count every parameter in that case.

The exact two-omission safety condition is q>=3*2^128. For length 16,
L004 permits 8,6,7,9 challenges at dimensions 8,4,2,1, whereas the sharp
count is three. The uniform extension determines the cells through r=42
at n=256,k=128, still short of L004's sufficient interval delta<90/256.
It does not identify a general maximal radius or certify ABF26's event.

The original-event check passed 5,897 pairs across four parameter sets,
including F_8, r=3, codeword translations, lines through a codeword, zero
quotient directions, and families supported on at most r coordinates.
For the F_7 constant code, 4,909 of these cases exhaust sparse endpoint
support shapes and nonzero values up to coordinate permutations. The other
pair tests are deterministic samples and explicit cases, not exhaustive
maximizations. The proof, not sampling, gives the general upper bound.
An algebraically checked excluded F_7 example at n=5,k=1,r=2 has four
bad challenges; it does not settle the first excluded distance n-k=5.

Proof review checked that the radius permits every support of size at least
n-r, that two codeword translations preserve the event, that each lifted
discrepancy has weight at most 3r, and that the attaining direction fails
on the very support of agreement. The coordinate root count works in
every characteristic and does not assume an attained real-radius maximum.
Only the root bound, linear algebra, and finite counting enter the new
proof; earlier lemma mentions are comparisons. Mathlib coverage is not
checked. The new DAG row therefore has no lemma inputs.

Outcome: ADVANCE, with zero consecutive exploration turns. The new reason
to test the boundary is precise: once 3r reaches the minimum distance,
a nonzero codeword can obstruct the common affine lift. The first uncovered
cell at smooth length 16 and rate 1/2 is r=3, with minimum distance nine.
The sole concrete next action is recorded in PROGRESS.md. No complete
challenge candidate has appeared, and STATUS remains IN_PROGRESS.

# Union-five triangle recovery application

Date: 2026-10-11. Gate-approved target: Bound the number of additional
recoveries by twelve for a gated L057 triangle containing two distinct
full-weight additional recoveries whose supports have union size five.
Reuse the supplied SPECIALIZE assessment; this is one research attempt,
classified REPRODUCTION. No external source refresh is necessary.

Main gap: the uniform triangle twelve bound. This concentrated-support
case is independently useful even without universal pair extraction.
Other triangle patterns, other local triples, extraction and challenge
definitions remain unresolved. ATTEMPTS/007's stopped generator does
not prohibit reuse of its upper bound; ATTEMPTS/025–026 are preserved.

## Saved applicability reasoning and test

Essential inputs are L015 and audited L057, with L010/L041 supplying
their inherited kernel, distance, nonpersistence and three base events.
All labels lie in the fixed H and all weights/finite parameters lie in
F_(97^20). For two full additional errors e,f at distinct finite
parameters u,v, the five-set A=supp(e) union supp(f) gives
sigma(b_*)=(sigma(f)-sigma(e))/(v-u) in U_A and
sigma(a_*)=sigma(e)-u sigma(b_*) in U_A. L057 supplies the nonzero
Hankel determinant and all nonpersistent locator hypotheses of L015.

Every admitted relaxed L057 recovery is an original finite same-support
bad event, including zero recovered weights and both-zero lifts. The
change from mu to T is injective on its eligible finite domain. Count
distinct T, not four-support witnesses. Its three full base parameters
are distinct, finite and excluded from the additional set. Hence
L015's total-B bound yields additional count at most 5+M(A)-3.

Continue if a complete configuration census and full orbit coverage
certify M(A)<=10. The stored value six is not yet a premise of this
attempt. Checking a stored maximal line alone is inadequate. Independently
count lines through every configuration point using normalized affine
directions (all points have coordinate zero equal to one), compare every
line-size histogram with a fresh original Plucker census, and verify
all 4,368 five-sets are covered once. Save complete per-orbit evidence.
Any failed coverage, histogram or bound obligation must be recorded
without claiming the target false. No additional triangle sweep is planned.

## Completion

The saved reasoning above preceded the completed census. Canonical
[L069](../lemmas/L069-five-label-triangle-recovery-bound.md) now contains
the full conditional proof and verification specification. All 273
original producer records replay identically. A different all-anchor
direction census independently reproduces every complete histogram,
covering all 4,368 five-sets, 14,819,805 original unordered pairs and
29,639,610 independent directed differences, with no failure. Orbit
maxima are five in 265 orbits and six in eight. Thus M(A)<=6 against
the required ten; the total bad bound is eleven, giving eight additional
recoveries against required twelve. No actual-pencil audit is needed.

Full evidence is `scripts/coefficient-feasibility/five-coordinate-complete-census-audit.json`
with complete producer replay, all per-anchor histograms and independently
constructed point/support records at its cited artifact paths. Original
certificates were preserved. Both-zero lifts, lower-weight recoveries,
arbitrary extension-field charts and parameter deduplication are retained
by applying the total-B bound before removing exactly three base events.

Outcome: ADVANCE, RESEARCH, REPRODUCTION. This validates an existing
finite claim and supplies its conditional application; no originality
or progress beyond the checked sources is asserted. The stronger eight
bound is a local partial result pending separate critical audit, not a
uniform triangle count or complete candidate. Mathlib remains not checked.
The next scope requires separate approval before critically auditing L069,
its L015/L057 applicability and all-orbit census. No universal union-five
pair extraction is assumed or attempted. Other triangle families, other
patterns, extraction and challenge-definition gaps remain unresolved.

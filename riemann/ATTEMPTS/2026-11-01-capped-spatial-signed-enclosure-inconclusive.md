# Capped carrier-centered spatial enclosure — inconclusive

The exact SPECIALIZE target from
[the source assessment](../drafts/literature/2026-11-01-spatial-signed-entry-enclosure-scope.md)
received one concrete calculation. No canonical lemma was established.
The retained attempt and application obligations are in
[the working record](../drafts/heat/2026-11-01-spatial-signed-enclosure-working.md).
Full coefficients, elementary data, attempts, partial records and input
hashes are under `scripts/heat/spatial-signed/`, with final manifest
`certificate.json` and record-only verification `ledger-check.json`.

WHY IT FAILS: the procedure exhausted exactly 2^28 scalar interval
operations at cutoff 691087, after 50975 evaluated/started Taylor enclosures plus two empty-cell tests (50977 total cases).
It did not cover the prescribed interval through N=691260. An absolute
fixed-grid representation first amplified tiny coefficient rounding;
normalizing the eta coordinate improved that defect within the same
cumulative caps but did not recover the remaining operation budget.
Producer records for the first 82 nonempty cutoff cells satisfy their
strict scalar comparisons; they have not received an independent
coefficient/remainder audit. The 923 successful ledger checks establish
record ordering, dimensions, hashes, thresholds and accounting only.
Thus this outcome is INCONCLUSIVE, not a lower bound for the actual
cost, a collision, or a general impossibility theorem. Both uniform
charges and the full entering-pair error remained in the test. Park
this precise capped estimator; no adjacent endpoint, larger cap or
precision replay is a continuation authorized by this outcome.

The main all-height sign gap, zero-time transfer and imported manuscript
audits remain open. The separate central boundary-flux nomination is
uncovered and must receive literature review before any derivation.

# Index-four successor table: exact-arithmetic verifier startup failure

2026-10-18, step 329. The single combined construction/replay stopped
before independent product checks. The complete failure and evidence
paths are in [the attempt record](../drafts/2026-10-18-index-four-table-attempt.md).
No successor-table lemma is established. Production output remains
unverified and every original is preserved.

## WHY IT FAILS

The verifier's matrix arithmetic leaves untouched zeros as Python ints.
Its original-scale reconstruction divides those entries with `/`,
creating floats; the next exactness test calls `.denominator` and stops.
All 2304 independent original-H product checks are missing. This refutes
the completion of this execution, not the multiplier identification or
the existence of an integral table. Retire the run without retry or
in-place repair. A separately assessed replay-only target may use the
preserved production output and explicit Fraction reconstruction; it
must still check every product, transport, identity and lattice index.
The historical ATTEMPTS/041/042 stops and all unfinished work remain.

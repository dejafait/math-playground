# Approved finite Gilbert attempt — working checkpoint

Target is exactly the saved SPECIALIZE assessment
`drafts/literature/2026-10-10-four-column-gilbert-certificate.md`.
The main gap is arbitrary-center 67/68-agreement safety; this test
addresses only whether an ordinary packing lower certificate can
exceed the L041/L042-derived benchmark 19800269675 after adjoining
L043's imported 107^5 quartic graphs.

Planned exact counting: fix a block of decreasing profile a in its
first s columns. For a second block, record its sizes u_i in these
columns and the decreasing profile c in the other 9-s columns.
Count every outside-column placement and point choice. In each fixed
column count intersection j by C(a_i,j)C(107-a_i,u_i-j), multiply
the generating polynomials, and retain total intersection at least
five. Aggregate by the second block's profile. This counts the closed
neighborhood, including the block itself. Column/point permutations
prove dependence on profile only, without symmetry of a packing.

Pending: prove and evaluate that count, maximum-degree Gilbert
rounding, all eighteen single-profile certificates, and independent
small-parameter direct checks. No bound has yet been computed.
Continue only if baseline plus an individual valid certificate is
strictly above 19800269675; otherwise park this greedy prescription.
Do not sum profile certificates. Two extra points, actual-label
transfer, cross-core consistency and common-center RS realization
are not part of this attempt. L043/L044 stops remain preserved.

Initial independent audit reconstructed all 1620 conflict histogram
cells and all large-instance certificates without discrepancy. Its
five small-case universe checks incorrectly compared combination order
with increasing binary-mask order. Preserve that failed run in
`scripts/finite-packing/four-column-gilbert-audit-initial-order-failures.json`;
correct only the order-insensitive comparison and rerun. The complete
small-case histograms already agreed. This is a checker-order bug,
not a counting discrepancy; final validation remains pending.

Completed: the corrected audit passes all 1102 checks. Canonical
proof, exact table, citations and limitations are in L045; the full
certificates retain every conflict contribution and every small-case
vertex. Best added certificate is 233020777, giving total
14258538084 below strict required 19800269676. This prescribed
certificate is parked. No further mathematical target is approved
in this turn; the separate column-aware syndrome source target is
REVIEW_REQUIRED.

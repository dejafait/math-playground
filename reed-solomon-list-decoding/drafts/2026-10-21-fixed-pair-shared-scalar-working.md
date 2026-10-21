# One prescribed shared-scalar construction — work in progress

Step rsld-2026-10-21-394-fixed-pair-shared-scalar-construction.
Approved target: Test exact-N feasibility with L098's pair marginals fixed, all original triple scalar constraints and contractions retained, and PSD constraints omitted.
Prior gate: `drafts/literature/2026-10-21-fixed-pair-cardinality-scalar-feasibility.md`, SPECIALIZE, step 393.

The main gap is arbitrary-center safety at 68/67 agreements. Test only the
specified distinct-triple support with sorted distances (i,68,68),
5<=i<=68; other distinct values zero. Inputs: L001,L021–L023,L098,L105,
foundations/04,12,13. L098's audited normalization and contractions are
imported, not reproved. No cross-notebook input or fresh source work.
A complete witness would stop scalar-only exclusion at these pairs.
Failure parks this construction and leaves unrestricted feasibility open.

Preserve all earlier files, ATTEMPTS/081–082,088 and the exhausted
translated-pole route. One lexicographic rational elimination, nonpivots
zero, no search/optimizer/rounding/restart, followed by complete independent
original-coordinate substitution. Caps and incomplete state will be saved
at `scripts/finite-support/fixed-pair-shared-scalar-*`. Reconstruct pairs
from L021's exact primal data and compare against L098's certificate;
check original source equalities with invariant t-s. The construction
and independent eight-region verifier each have at most 1501000 entries,
combined 20000000 presentations, 69 equations, 1024 free classes,
5000000 elimination updates, 900 seconds, 1 GiB declared memory,
256 MiB output and 262144-bit rational components.

No feasibility, rank or mathematical outcome is claimed at this checkpoint.

## Completed bounded attempt

The sole run completed and the independent full verification passed.
[L106](../lemmas/L106-restricted-shared-scalar-support-obstruction.md)
contains the full proof, exact input conventions, rational sign and source
citations. Its 64-class contraction system has one signed solution;
exactly the nonnegativity row (68,68,68,0) fails. All 69 contractions
and every other original scalar row pass. Full lossless lift and
independent evidence are in `scripts/finite-support/fixed-pair-shared-scalar-results.json`
and `scripts/finite-support/fixed-pair-shared-scalar-verification.json`.
No cap or implementation failure occurred. This is an informative
NEGATIVE for this support, not unrestricted infeasibility or a new RS
boundary. Park the construction under ATTEMPTS/089; no enlargement,
parameter scan or numerical restart. A separate L106 critical-audit
scope is proposed with REVIEW_REQUIRED; it is not approved here.

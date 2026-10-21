# Fixed-head balanced limit critical audit — step 74

Work in progress under the prior SPECIALIZE assessment
`literature/2026-10-11-mollified-balanced-limit-audit.md`.
The exact target is the critical audit of L398 at fixed N, actual
Y=H^(1/100), both diagonals, all response twists, ordinary jets through
order two per side and both sharp endpoints. Direct inputs: L390 and
L395. The main mixed-positivity gap and the complete signed mean are not
being addressed by an assembly in this step.

Initial checks: the four squarefree local cases give (1); its numerator
vanishes at zero shifts exactly for a nonzero response valuation
difference, without dividing by a possibly vanishing numerator. The
unmodified product has nonnegative double Dirichlet exponents and
summable weighted absolute local mass, supporting (4). The combined
scalar generator is equivalently cosh((a+b)/2) +
[4/(3 vartheta)+vartheta ab/5] integral_0^1 exp((1/2-v)(a+b)) dv;
its ordinary jet signs give the stated rational combination.

Pending checks: full contour containment and tails for (6), coupled
Mellin error and reflected diagonal, source Section 6 height range, and
absolute endpoint bumps. The arbitrary-weight phrasing must be restricted
to heights comparable to H where the stated source estimate applies.
No audit acceptance is recorded yet. Continue only with normalized
O_N(1/log H) error and absolute small-bump envelopes at both boundaries;
otherwise isolate a proof failure without deciding the actual mean.

## Completed audit

The fixed-N limit passes; the full mathematical audit is in canonical
L398, section “Separate critical audit — 2026-10-11, step 74”. It
justifies the omitted compact shifted-height neighborhood and checks
the source's height condition directly on [H/2,4H], including the two
small endpoint bumps at T=2H without changing Y. The scalar differentiated
smooth formula bounds each bump absolutely by O(H/log H); L395's
whole-interval estimate is not substituted for that bound. Every
response twist, both diagonals and ordinary order two per side retain
one normalized O_N(1/log H) error. No mathematical failure was found.

The exact rational script was rerun with zero failures, and the complete
generating polynomial and jet entries were inspected using the scoped
JSON inspector. It checks algebra only. L397's cited source paragraph
was read solely to trace the already assessed reciprocal bound; no L397
mathematical conclusion is an input to L398, and the DAG is unchanged.

Outcome ADVANCE: the missing analytic justifications have been supplied
and the fixed-N input is validated, as local REPRODUCTION of known tools,
not progress beyond the sources checked. Actual task proof_audit. The
complete signed physical mean and sequential N-limit are not derived
here. Their proposed assembly is outside the audit's approved scope;
the exact continuation has a separate REVIEW_REQUIRED assessment.

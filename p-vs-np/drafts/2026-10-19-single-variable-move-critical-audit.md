# Single-variable move critical audit — step 347

Approved target: critically audit L089's single-variable-move witness,
including its ordered-state invariant, exact merge reception, both
original-factor orientations and full-bit bound in pre-witness M.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-19-single-variable-move-obdd-audit.md`.
This is RESEARCH / proof_audit / REPRODUCTION; no new source search or
claim of originality is intended.

Checkpoint before writing the final verdict: the complete L089 proof,
L088's single-swap correction and relevant independent audit, L026
(4)–(12) and injectivity, L071's post-compilation value/K/W graphs and
audited degree/copying interface, and L087's original B/M convention
have been checked. Histories 342/345 and Attempt 030 retain the relevant
comparison and independent stop. No supplied startup file was reloaded.

The proposed audit finds no state failure: at stage t each postponed-x
tag is an ordered pair of original V_t states. At the next crossing its
two children are original V_(t+1) states. Exact pair merging preserves
both ordered summands, and every incoming bit edge must remain. The
leftmost boundary/root and canonical-terminal cases are included. Both
W+fJ and W+Jg retain the original ordered product. Remaining work at
this checkpoint is to finish the explicit record/degree accounting and
put the complete audit and verdict in canonical L089.

The main gap is unrestricted SAT decision/separation. This intermediate
target validates or repairs only the restricted formal-witness interface;
it may support later supplied-order-pair constructions. Continue if the
exact two identities, stated path degree and one original-M bound survive;
repair or narrow on a concrete failure. Arbitrary-order W₂, general ER
data availability and SAT transfer remain independent unresolved steps.

## Completion

The full all-size audit is now canonical in
[L089](../lemmas/L089-single-variable-move-obdd-product-affine-abp-witness.md),
separate critical audit — step 347. It finds no substantive defect and
leaves all hypotheses, identities, dependencies and bounds unchanged.
The original-M copying and actual path-degree checks survive, including
all independent local graph copies, retained snapshots and repeated full
dictionaries. This is an informal verification ADVANCE / REPRODUCTION,
not a stronger result or progress beyond the sources checked. No
mathematical script, finite graph certificate or implementation is claimed.

The next proposed scope deletes a supplied logarithmic-size variable set
from both orders to obtain a common subsequence. It is a target only;
no multi-variable state bound, recombination or witness is derived here.
Its new assessment is REVIEW_REQUIRED and requires a separate
literature-only turn. The completed L089 audit remains independent of
that future approval.

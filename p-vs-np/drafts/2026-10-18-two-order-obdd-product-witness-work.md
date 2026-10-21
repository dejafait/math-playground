# Step 337 — bounded two-order witness specialization, work checkpoint

Approved target and coverage: the unchanged SPECIALIZE assessment in
`drafts/literature/2026-10-18-two-order-obdd-product-witness-burden.md`.
Main gap: unrestricted SAT. Intermediate target: the conditional implication
from one polynomial alternative Boolean/commutator witness bound on two
strictly differently ordered dense OBDDs to NP=coNP. Downstream use:
diagnose the formal-witness burden when relaxing common-order suppliers.

Proposed application of the inspected occurrence-splitting mechanism:
append fresh clauses (u OR v), (NOT u OR NOT v) to arbitrary width-three F;
split every literal occurrence into its own original variable. Clause-order
testing and original-variable-group consistency testing each have constant
width. At the four appended occurrences the orders read u1,v1,u2,v2 and
u1,u2,v1,v2, so they are strictly distinct without ignored dummy variables.
Dense failure states avoid early terminals. Empty clauses force failure;
the appended pair is satisfiable independently of F.

Completed in `lemmas/L087-two-order-obdd-product-witness-bound-consequence.md`:
both explicit width-three transition systems, strictly different orders,
exact suffix-to-path graph reception, ordered product, M and |G| bounded
by fixed multiples of (|F|+2)^3 before H, and the promise-free verifier
using L041's audited arbitrary-affine-graph component. Under the single
unproved witness polynomial this proves the conditional NP=coNP burden.
This is reproduction/specialization of the known mechanism, without a
certified originality claim. No universal witness bound, constructor or
main-problem candidate is claimed. L042 is a scope comparison, not a
proof input; Attempt 030 and all unfinished files remain intact.

The unchanged assessed target is retained for a separate critical audit
of L087, especially its width-three schedules, the appended order gadget,
exact free-ring product, pre-witness ledger and PIT receiving model.
Narrow or repair on an essential failed interface. General ER data,
alternative-certificate bounds and unrestricted SAT remain unresolved.

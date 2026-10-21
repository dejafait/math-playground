# Step 340 — nearby-order witness construction in progress

Approved target and source scope: unchanged
`drafts/literature/2026-10-18-near-order-obdd-product-witness.md`
(SPECIALIZE saved before this invocation). Main gap: unrestricted SAT
decision/separation. This step tests only the prescribed logarithmic
adjacent-transposition restriction and the exact original product fg.

Candidate calculation, not yet independently audited: for a dense
two-level block testing x then y, write its four grandchildren w_ab.
Replace each top state u by a y-state with two fresh x-states (u,b),
whose a-successor is w_ab. Every literal commutator
e_a(x)e_b(y)+e_b(y)e_a(x) equals xy+yx. Thus a graph retaining the
old prefix, four parallel commutator-placeholder edges from u to w_ab,
and the old suffix should witness the exact root difference. No path
unfolding or recursive witness multiplication is needed.

If N counts all states including unused states and terminals, a swap
changes N to N+2A−B≤3N, where A,B count the two old layers. Hence at
d≤floor(log₂ M) swaps every N is at most M³; the aggregate diagrams
and correction graphs have a geometric-series bound in original M.
Remaining check: import the exact L026/L071 common-order W graph for
the first diagram and the final reordered second diagram, then compose
H=W+f(sum of swap corrections). Charge every independent local block,
complete dictionaries, dense references and source names. Boolean-zero
must identify only the common-order P with zero, not fg with zero.

Continue if both formal identities and one fixed full-bit polynomial
follow. An identity failure or superpolynomial copying stops this
construction, not the witness-existence target. L087's unrestricted W₂,
arbitrary ER data, availability and SAT transfer remain unresolved.
Attempt 030's independent availability obstruction is unchanged.

Completion: the all-size construction and full ledger are now canonical
in [L088](../lemmas/L088-near-order-obdd-product-affine-abp-witness.md).
The swap graph uses O(N_t) records, the total reordered state count is
at most (3/2)M³, and the independently copied common-order graph fits
O(M⁷) records. A full-bit K(M+2)^9 bound is proved informally. No
mathematical script or finite certificate was needed or claimed.
Independent critical audit remains pending; the candidate calculations
above are preserved as the work checkpoint, not a second proof.

# L084 audit work — step 327

Approved target: the unchanged SPECIALIZE target in
`literature/2026-10-18-repeated-square-data-critical-audit.md`.
Main gap: unrestricted SAT decision/separation; arbitrary ER data remains
an independent representation gap. This audit tests the family-specific
supplier, for reliable conditional reception by L037.

Checkpoint before final write-up: L083's actual core/accumulator order
gives a_i=P_min(i+1,n) on every assignment, including falsifying ones.
The two-state diagrams retain dead states, both transitions and all levels;
terminal complementation agrees formally with exact signed wrappers by
L026. Its increasing-multilinear identification applies to the auxiliary
product and output, not to the unreduced operand product. L071's graph
component needs only those diagrams and keeps the factors in their stated
order. No treewidth hypothesis is removed from its whole theorem.

Independent ledger check: q=4(n+1), p=O(16(n+1)); each pair state's
constant number of independent K/value factors costs O(q), so each H
costs O(pq). The 2H outputs, value copies, auxiliary P, temporary K,
diagrams and associations fit O((T+n+2)(n+1)^2+n^2+1) records using
the explicit-record inequalities n<=T and 2H<=T. A dictionary per
exported root adds O((S+2H)T^3)=O(T^4); it is not already paid by
L071's single dictionary. A path exiting after n-s pair levels has
degree at most n-s+2s-1<=2n-1. Originals and signed values have degree
at most n. No failed obligation has been found. Final canonical audit
and checkpoint are still to be written; this note is not a replacement
for the canonical proof or a machine certificate.

Continuation test: accept the existing statement only with all identities,
root associations, copies and degree charges; repair or withdraw it on a
specific failure. Preserve Attempts 019–020/029. No mathematical script,
new source search, new lemma or cross-notebook input is needed.

# Step 349 — small deletion set, preserved checkpoint and completion

The approved target and SPECIALIZE coverage are unchanged from
`drafts/literature/2026-10-19-small-deletion-set-order-pair-witness.md`.
This is one RESEARCH / proof_attempt. No candidate for P versus NP is
asserted. Preserve Attempt 030 and all existing unfinished work.

Proposed exact lift: in a partially restricted original diagram, cut at
the next deleted variable z. For each cut state u let p_u be the original
prefix path sum and a_u,b_u its two successor suffixes. Then
h=sum_u p_u((1+z)a_u+z b_u), and h_0=sum_u p_u a_u,
h_1=sum_u p_u b_u. L035 on the x-only graphs p_u,z supplies C_u.
Thus sum_u C_u(a_u+b_u) should substitute to
h+(1+z)h_0+z h_1. It vanishes at zero placeholders. This is a graph cut,
not an unfolding into complete paths; prefixes may have coincident roots.

Use one fixed order of the supplied deletion set. Multiply this correction
on the left by each partial indicator and sum over internal assignment-tree
nodes. The intended telescoping endpoint is h plus its full ordered
indicator/cofactor interpolant. Every node uses a restriction of the
original diagram, never a previously generated placeholder graph in L035.

Still to complete: exact telescoping proof, common-order branch reception,
L072 recombination, original-product recovery and an explicit full-bit
ledger in original M and 2^k, including empty and constant cases. Continue
only if all of these close; an unchecked lift or ledger is not a result.

## Completion

The canonical all-size informal proof is now in
`lemmas/L090-small-deletion-set-order-pair-affine-abp-witness.md`.
It closes the lift, ordered recombination and original-product identities,
with one bound K(2^k+1)²(M+2)^12 and hence K'(M+2)^14 under the supplied
cutoff. The pre-invocation assessment was reused without further browsing.
No mathematical script or finite certificate execution was needed or
claimed. The new formal lift and aggregate specialization are local
progress, not certified originality or a result on unrestricted SAT.
A separate critical audit is proposed, with its new scope marked
REVIEW_REQUIRED; this turn does not approve or perform that audit.

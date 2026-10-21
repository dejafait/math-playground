# Opposite-order witness attempt — step 361

Approved target: the exact TARGET in
`drafts/literature/2026-10-20-opposite-order-obdd-product-witness.md`.
Main gap: unrestricted SAT decision/separation. Intermediate target:
original-fg Boolean/commutator witnesses for opposite-order dense
width-three OBDDs, polynomial in L087's unchanged pre-witness M.
Downstream use: an order-change interface beyond L092's logarithmic
block enumeration; arbitrary-order W₂ and general ER data remain open.

Checkpoint before full write-up. For a suffix g_u with edge recurrence
g_u=sum_e l_e g_v, let R_u=rev(g_u), represented by reversing original
edges with scalar-terminal source connectors. Test
J_u=sum_e(l_e J_v+C_e), C_e=L035(l_e,R_v), terminal J=0.
Substitution should give g_u+R_u, with recursive witnesses multiplied
only on the left. All C_e inputs are x-only. A first-exit graph realizes
this recurrence without unfolding. The opposite-order R_root can be
normalized into L085's weighted common-order receiver by absorbing
terminal scalars into its new root's first outgoing edges. Then test
H=W+f J_root with W(B)=f R_root+P and ordered-multilinear P=0.

Continue only after proving every identity, terminal normalization,
original-B dictionary reception, independent-copy/bit-time and path-degree
bounds in original M. Abandon this mechanism if those obligations force
uncontrolled two-sided witness copying or a non-original L035 input.
No success is inferred from this checkpoint. L035's full proof and L085's
weighted recurrence/first-exit construction were read; L026's injectivity
and L087's exact B/M conventions were checked. Attempts 018/030 do not
obstruct this supplied-input target. Existing notebook changes are retained.

Completed step 361: the formal identities, graph reception and original-M
ledger are now in canonical L093. This draft remains a checkpoint of
the attempt, not an independent proof. The result awaits a separate
critical audit under the new REVIEW_REQUIRED assessment.

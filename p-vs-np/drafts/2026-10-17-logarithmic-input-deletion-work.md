# Step 276 — deletion-set construction work

The supplied SPECIALIZE assessment is reused on its exact target. Main gap:
unrestricted SAT decision/separation. The intermediate test is complete L037
data under the logarithmic original-input deletion promise; arbitrary ER,
formula-only bounds and SAT transfer remain independent gaps.

Checkpoint before completing the proof: replace each removed input-to-gate
operand occurrence by a fresh constant leaf for each assignment alpha.
Retain removed-input root associations through isolated constant vertices.
Leaf attachments preserve width two. Use only L071's circuit compilation
and L026 graph construction, not a purported restricted ER refutation.

Let e_alpha be the ordered product of deleted-input literals and let
f_(v,alpha) be branch representatives. Proposed final values are
sum_alpha e_alpha f_(v,alpha), retaining exact originals and signs through
formal identities. L026/L071 on the small common-order indicator diagrams
give Q_(alpha,beta)(A)=e_alpha e_beta+delta_(alpha,beta)e_alpha.
For a definition with branch operands a_alpha,b_beta, the proposed correction
to the product is the sum over alpha,beta of

    e_alpha W(a_alpha,e_beta) b_beta
       + Q_(alpha,beta) a_alpha b_beta.

Adding sum_alpha e_alpha H_(i,alpha) should give the exact defect. Every
factor in these expressions is independently bounded; there is no recursive
use of a glued witness. Remaining checks for this attempt are full ordered
cancellation, original/signed root identification, all-root branch framing,
every copy and dictionary cost, and pre-substitution degrees. Continue only
if one fixed polynomial in T and 2^k covers the complete data and bit time.
No sufficiency claim is made by this unfinished checkpoint.

Inputs read: complete L071/L026/L035 proofs, L037 receiving conventions and
composition cases, the prior treewidth assessment and witness assessments,
Attempts 019–021 and history 274. These stops concern different promises
or prescribed outputs. No cross-notebook inputs or new source search.

Completion: the proposed identities and all-size ledger are now proved in
canonical `lemmas/L072-logarithmic-input-deletion-affine-abp-data.md`.
The final construction uses L026 indicator corrections and L035 directly;
L036 enters only inside downstream L037. It does not need a new arbitrary
Boolean-zero witness. Outcome ADVANCE in the restricted local interface,
with no certified originality and separate critical audit still required.
This draft preserves the unfinished checkpoint, not an alternative proof.

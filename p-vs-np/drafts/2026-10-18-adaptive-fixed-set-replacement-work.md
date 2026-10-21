# Step 316 — Fixed-set replacement work

The gate-approved target is the exact TARGET in
`drafts/literature/2026-10-18-adaptive-tree-fixed-set-premise-comparison.md`.
The ordinary SAT gap remains open; this step tests whether adaptivity
helps L081's particular unsimplified structural promise. A successful
replacement would redirect discovery toward fixed deletion sets without
supplying any set or tree for arbitrary ER.

Candidate: take the queried set D on a shortest leaf path of depth d.
Topological induction should give U_v(D,alpha)=U_v\D, independently of
alpha. The maximum counted-path recurrence then depends on D alone.
The selected leaf's promise therefore transfers to every assignment on
D. Fullness and minimal leaf depth imply at least 2^d original leaves,
so the complete fixed-order assignment tree has 2^d<=M leaves.

Continue only if both assertions hold with original T/k, scalar zero
products retained, all roots/signs/operand occurrences, and M=1 and
unequal depths included. A failure of this candidate would not refute
the existential target. Do not infer |D|<=k for unrestricted M, construct
new formal witnesses, or claim arbitrary-ER existence. Relevant source
coverage and prior failures are already assessed; no fresh source search
or mathematical script is needed. Full proof will be canonical in L082;
this note preserves the attempt rather than serving as proof evidence.

Completed: the candidate succeeds. The complete support/path induction,
finite-tree count and cardinality qualification are now in canonical
L082. Its separate critical audit remains pending; no mathematical
script was necessary. No failure or abandoned attempt is recorded.

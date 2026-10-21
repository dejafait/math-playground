# Signed-AND degree attempt — saved reasoning

The gate-approved target is the exact TARGET in
`drafts/literature/2026-10-17-signed-and-syntactic-degree-affine-abp-data.md`.
The main gap is unrestricted SAT decision/separation; the immediate intended
use is to supply L037 data when the exact value DAG's syntactic degree D is
polynomial in the actual binary ER length T. General polynomial D is not
assumed. Attempts 016/020 remain intact and do not refute this syntax-specific,
T+D-charged criterion.

Candidate structural argument, saved before final verification: evaluate
every syntactic-degree-zero node topologically as a scalar in F₂. For each
positive-degree root, unfold positive-degree nodes only and replace each
degree-zero child by its computed scalar leaf. The positive-node skeleton
has unary signed/mixed-product nodes, binary products with two positive
children, and original-variable leaves. Positive degrees are conserved at
unary nodes and add at binary nodes. It therefore has exactly d original
leaf occurrences for root degree d. Each root-to-leaf path has at most S
nodes because the original DAG is acyclic. Counting ancestor/leaf incidences
bounds its positive occurrences by Sd; at most one scalar leaf per positive
internal node gives at most 2Sd formula nodes. A zero-degree root costs one
scalar leaf. Retain both product factors and their order, even when one
computed scalar is zero; no semantic-degree or Boolean simplification enters
the bound.

Pending checks at this save: full original-name/dictionary copying ledger,
all L037 input promises, D=0, all unused roots and deterministic bit time.
Use imported Raz–Shpilka Lemma 2 Step 1, PDF p.5 for tree-to-graph conversion;
do not reprove its general theorem. H_i=0 is justified only by exact formal
AND values. Continue on a fixed polynomial full-bit/time bound in T+D+2;
abandon this criterion only on a qualifying bounded-D exact-syntax
counterexample. The final canonical proof, if completed, will supersede
this scratch reasoning without deleting it.

Completion note, step 292: the pending ledger and receiver checks are now
written in canonical L076, `lemmas/L076-signed-and-syntactic-degree-affine-abp-data.md`.
The all-root full-bit bound is K(T+D+2)^4, with conservative deterministic
bit time K'(T+D+2)^12; d=max(1,D), h=1 and all unused roots are included.
This is a completed informal structural attempt, not an independent audit,
an originality certification or a polynomial-D theorem for arbitrary ER.

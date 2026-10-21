# Small-support construction — saved attempt

Step 296 works only on the unchanged SPECIALIZE target in
`drafts/literature/2026-10-17-small-support-affine-abp-data.md`.
The main gap is unrestricted SAT decision/separation; the immediate gap
is polynomial-in-T complete L037 data for general supplied ER. The target
restricts every extension, including unused ones, to at most
k=floor(log₂(T+2)) distinct reachable original variables, ignoring signs.

Candidate: compute these sets by topological union in the canonical value
DAG. For each extension independently enumerate all assignments to its
support, evaluating the source DAG with other originals zero. Induction
on syntactic support ensures that this table is the correct all-assignment
Boolean function. Use one global original-variable order. At level j of
its complete diagram retain exactly the assignment to support variables
preceding j; querying an irrelevant variable has equal successors.
There are at most 2^k states per level. Last-level transitions use the
table to select constant terminals. n=0 is scalar evaluation.

Pending: verify every diagram transition and support-independence case;
import L026's exact H identities and L071's post-compilation affine graphs
without its treewidth compiler. Its audited R=B(n+1)^2(w+2)^3+n^2+1
ledger should give R=O((T+2)^6), E=O((T+2)^7), independently of exact
syntactic degree. Check all separate roots, dictionaries and deterministic
bit time. Continue if both formal identities and a single polynomial in T
survive; stop/narrow if a semantic oracle, implicit graph, incompatible
orders or uncharged copying is required. General ER coverage, formula-only
bounds, W/V/U, every-certificate hardness and SAT transfer remain open.
L027/Attempt 019 and L033/Attempt 020 are preserved stops on broader inputs.
L076 is a comparison, not an input. No cross-notebook result is used.

Completion, step 296: canonical
`lemmas/L077-small-syntactic-support-affine-abp-data.md` now contains the
all-size support/dependence proof, complete prefix-state diagrams, imported
formal reception and full graph/dictionary ledger. The constructed data
have E_ABP=O((T+2)^7), conservative bit time O((T+2)^16),
d=max(1,n), h=max(1,2n−1). This is an informal REPRODUCTION, with a separate
critical audit pending; this saved attempt does not audit its completion.

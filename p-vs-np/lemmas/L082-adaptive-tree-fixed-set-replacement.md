# L082 — Fixed sets replace adaptive trees for the unsimplified support promise

## Hypotheses

Use L081's finite canonical signed value DAG G and its original length
T=2+|F|+|pi|. Put k=floor(log₂(T+2)). Retain every original/scalar/absent
base, signed wrapper, ordered AND operand occurrence, repeated operand
and unused definition. Supports are singleton originals, empty
scalar/absent bases, inheritance at signs and union at ANDs. An AND is
counted exactly when both actual operand supports have cardinality
greater than k. The promise is at most k counted ANDs on every
source-ancestry path from every root.

Supply an L081-admissible finite full binary original-input query tree
with M leaves: both bit children are present at each query, no original
is queried twice on any root-to-leaf path, and every leaf restriction
satisfies the promise at this unchanged T and k. Restriction replaces
each queried original occurrence by its assigned scalar, retains its
own root association and every other node/operand position, and performs
no Boolean simplification. In particular a product by zero is retained.
The assignments and tree are explicit; there are no implicit paths.

## Conclusion

Let d be the minimum root-to-leaf query depth, and let D be the queried
set on any leaf path of depth d. Then |D|=d and

    2^|D| <= M.                                             (1)

For every assignment alpha:D→{0,1}, the unsimplified residual G_alpha
satisfies the same all-root counted-path promise at the original T/k.
Consequently the full assignment tree querying D in one fixed order
has at most M leaves and is itself L081-admissible. This includes M=1,
unequal leaf depths, all-original queries and M>T+2.

If M<=T+2, then |D|<=k, so D also meets L080's set-cardinality
requirement. For general M, only |D|<=floor(log₂ M) is asserted; the
whole theorem L080 is not invoked outside its stated cardinality range.

This is a structural comparison for an already supplied tree. It does
not supply a polynomial-size tree or a small set for arbitrary ER, a
new receiver or formal H identity, a formula-only bound, or a SAT
decision/separation result. The separate step-318 critical audit below
finds no substantive defect and changes no hypothesis or bound.
POTENTIALLY_NEW records only the prior search comparison; it
does not certify originality.

## Proof

**Scope and source comparison.** The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-18-adaptive-tree-fixed-set-premise-comparison.md`.
The exact residual definitions and leaf promise are those of L081.
The following elementary inductions establish the additional comparison;
they do not reprove the ABP receiver or a general backdoor theorem.

For contrast, Ordyniak, Schidler and Szeider, *Backdoor DNFs*, JCSS 144
(2024), 103547, sections 2.2–2.5 and Observations 1–2, pp.2–3,5,
[published paper](https://eprints.whiterose.ac.uk/id/eprint/213187/7/1-s2.0-S0022000024000424-main%20%281%29.pdf),
give the union of a backdoor tree's queried variables as a strong set,
with at most M−1 variables. Their restriction simplifies CNFs, so it
does not imply the bit-independence used here or (1). No theorem from
that paper is used as a premise. The inspected binary-tree/Kraft
terminology likewise supplies no needed theorem: the particular
leaf count below has a direct finite induction. Attempts 019–020 stop
other representation routes and are not reopened by this comparison.

**Supports depend on the queried set, not its assigned bits.** Let U_v
be the original syntactic support at an associated source node v. Fix
any set D of originals, without imposing a size bound. For any assignment
alpha on D, write U_v^alpha for the support at the corresponding
retained node or associated scalar root in G_alpha. Then

    U_v^alpha = U_v \ D.                                   (2)

Induct in an acyclic source order. An original x_j in D is replaced by
a scalar of empty support, and {x_j}\D is empty. Every occurrence and
its own associated root satisfy this statement. An original outside D
keeps support {x_j}. Scalar and absent-variable bases retain empty
support regardless of their scalar value. A sign wrapper inherits its
predecessor's support, even when it complements a scalar, so (2) passes
through that wrapper. At an AND with actual ordered operands a,b, the
new support is

    (U_a\D) union (U_b\D) = (U_a union U_b)\D.

This remains the rule when an operand evaluates to zero, when operands
repeat, and when a node is unused by the proof. These are all node
types, proving (2) at every root and retained operand occurrence.
Distinct replacement scalar leaves all have the same empty support;
their multiplicity does not affect (2).

To verify that supports suffice for the actual path promise, let
b_v^alpha be the maximum number of counted ANDs on a source-ancestry
path starting at the associated root v of G_alpha. Such paths are
finite because the DAG is acyclic. A base has b=0; a sign has its
predecessor's b. At an AND the exact recurrence is

    b_v^alpha = c_v(D) + max(b_a^alpha,b_b^alpha),
    c_v(D) = 1 if |U_a\D|>k and |U_b\D|>k, else 0.          (3)

Indeed each path counts the starting AND if it is counted, then follows
one of its actual operand occurrences. Both choices remain present
even for repeated operands or scalar-zero products. Isolated associated
scalar roots have b=0 and create no additional counted path. Equation
(2) gives the stated indicator. Topological induction in (3) therefore
shows that b_v^alpha is independent of alpha for every v. It follows
that if one assignment on D meets the all-root bound b_v<=k, then
every assignment on D meets it, with the identical original cutoff.
This is not an assertion about semantic support or simplified residuals.

**Shortest-path set and its assignment reception.** Choose a shortest
root-to-leaf path in the supplied adaptive tree and let alpha_* be its
leaf assignment. Its d queries are distinct by pathwise nonrepetition,
so its queried set D has |D|=d. The leaf hypothesis gives b_v^alpha_*<=k
for every associated root. The previous paragraph transfers that
inequality to every assignment alpha on this same D. No consistency
with any other adaptive path is required: the assignment alpha_* is
used only as one accepted assignment on D, and the support recurrence
then supplies all others.

**Full-tree count.** There is no leaf at depth less than d. Thus every
node at depth j<d is internal and has exactly two distinct children.
Induction starting with the root gives exactly 2^j nodes at every
depth 0<=j<=d. Each node at depth d has at least one leaf descendant,
since the tree is finite; their subtrees are pairwise disjoint. Hence
M>=2^d, proving (1). This argument does not require equal leaf depths.

List D in the selected path's order and construct its full assignment
tree, querying the jth listed variable at every node of depth j−1.
Each root-to-leaf path queries all d distinct variables, and its leaves
are in bijection with the 2^d assignments on D. Every such assignment
was shown to satisfy the unchanged promise. This proves the claimed
replacement, not merely a successful assignment or a union-set bound.

When M=1 the original full tree is a single leaf: d=0, D is empty,
and the replacement is the same one-leaf restriction. If all originals
are queried, every residual support is empty, so (3) gives zero counted
ANDs. The proof otherwise uses neither M<=T+2 nor a depth upper bound
of k. Under the additional inequality M<=T+2, (1) gives

    |D| <= floor(log₂ M) <= floor(log₂(T+2)) = k.

For M>T+2 this last comparison is unavailable; the replacement still
has at most M leaves but need not meet L080's logarithmic-cardinality
premise. L081 can receive the full fixed-order tree under its own
hypotheses. No new construction or bound for its receiver is claimed.

**Separate critical audit — step 318, 2026-10-18.** This is an informal
all-size verification under the prior EXPLORE audit assessment
`drafts/literature/2026-10-18-adaptive-fixed-set-replacement-critical-audit.md`.
It reproduces and checks the argument, rather than claiming a further
theorem or certified originality. The step-315 source comparison remains
adequate: the contrasted CNF backdoor observation is not a premise, and
no external Kraft theorem or receiver construction is needed.

The exact source interface is L081's hypotheses. In particular,
restriction changes original leaves into scalars but does not discard
signs, ANDs, roots, or operand choices. A replacement occurrence and a
deleted original's separately associated scalar root have empty support
and zero path count. They therefore receive the same pair of invariant
values even when their graph vertices differ. Unqueried originals have
singleton support and zero path count; original constants and absent
nonextension bases have empty support and zero path count. These exhaust
the bases, including bases which occur only as associated roots.

At a sign, both invariants pass through its predecessor regardless of
the bit value or the sign. At an ordered AND, support is the union of
the two operand supports, and a path chooses precisely one operand
after possibly counting that AND. Thus (2) and (3) hold simultaneously
in source order. In the repeated-operand case the two occurrences give
equal values and their maximum remains that value; they are not treated
as two successive counted nodes. A zero operand still leaves the other
ancestry choice present. Even a semantically constant expression with
nonempty syntactic support retains that support. These observations
rule out accidental semantic simplification in the induction. The same
induction applies to unused definitions because it ranges over the whole
source DAG, not merely the final proof ancestry. Every possible start
root is covered. Scalar duplication or isolation adds only zero-count
paths, so it cannot invalidate the all-root conclusion.

Fixing D consequently fixes both operand support sizes at each AND and
the entire maximum-count recurrence. The actual assignment at the
chosen leaf satisfies the promise by hypothesis. It is used only to
certify this fixed recurrence once; no assumption that another assignment
would follow the same adaptive query path is made or needed. This checks
the quantifier passage from one accepted assignment on D to every
assignment on D, while keeping the original T and k.

For the leaf budget, finiteness guarantees a minimum depth d and at
least one leaf. Full binary branching and absence of earlier leaves
give exactly 2^d nodes at depth d. Each has a leaf descendant, and
distinct such nodes have disjoint descendant sets because the input is
a tree. Hence M>=2^d even if some leaves occur much deeper. Pathwise
nonrepetition makes the selected path's query count exactly |D|, not
merely an upper bound on that cardinality. Both properties would need
rechecking for a compressed DAG or a nonfull query tree, neither of
which is admitted here.

The constructed fixed-order tree has all 2^d assignments, two distinct
bit children at each query, and no repeated original on any path. Its
residual at each leaf is precisely the unsimplified restriction already
covered by the induction. It has 2^(d+1)-1<=2M-1 explicit nodes and uses
original input names already present in the supplied tree. Thus it can
be written explicitly and satisfies L081's tree hypotheses. L082 claims
nonincrease of the leaf count, not nonincrease of an arbitrary full-bit
encoding B or of every receiver parameter.

For M=1, a finite full tree can have no internal node (an internal node's
two subtrees each contain a leaf); the empty set and one-leaf replacement
are valid. Unequal depths were handled in the depth-d descendant count.
If D contains every original, each support is empty and every counted
indicator is zero, including at retained products and signed roots.
For every M the proved numerical conclusion is |D|<=floor(log₂ M).
Only after adding M<=T+2 may one compare this with k and apply L080's
whole fixed-set theorem. When M>T+2, L082 makes no assertion that
|D|<=k, nor that |D|>k; that range simply lacks the stated sufficient
comparison. L081 still receives the replacement under its own explicit
tree hypothesis. This verifies the cardinality qualification without
reopening L080's algebraic proof.

No substantive error, missing premise, or bound repair was found.
L081 remains the direct mathematical input; L080 is referenced only for
the expressly qualified downstream interface. The audit changes no
argument or DAG edge. It supplies no fixed set or polynomial tree for
arbitrary ER, no finder or formula-only bound, and no SAT transfer.

## Mathlib

Full matching coverage has not been checked. No Mathlib absence claim
or formal verification is made. The elementary support and finite-tree
arguments above are written out; the ABP machinery is not reproved.

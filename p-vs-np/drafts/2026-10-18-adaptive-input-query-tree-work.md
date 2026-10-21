# Adaptive input-query tree attempt — step 312

Approved target and prior coverage:
`drafts/literature/2026-10-18-adaptive-input-query-tree-data.md` (SPECIALIZE).
The main gap remains unrestricted SAT; the nearer gap is arbitrary-ER
L037 data. This attempt concerns only the supplied explicit adaptive tree.
Downstream use would be a restricted data supplier polynomial in T+B.
Continue only with exact base/sign identities, formal pair corrections,
both H identities and a complete independent-copy polynomial; abandon the
mechanism if it needs a generic Boolean-zero witness or union-set enumeration.

Checkpoint before completing the proof: exact original interpolation has
a subtree induction. For a variable fixed above a subtree, every leaf
value is that scalar; otherwise induction returns the original variable,
unless this node queries it, in which case its children return 0 and 1.
The local partition sum is formally 1 in each case.

Pair plan: distinct leaves diverge at a shared query j. Their path words
are P l_(j,0) U and P l_(j,1) V (or the reversed signs). Move the second
j factor left across U P, paying each adjacent literal exchange, then
replace the opposite pair by its Boolean placeholder. For a diagonal
pair, move the repeated first factor next to its first occurrence,
contract its square with a Boolean placeholder, and repeat in the same
path order. No canonical-order target should be substituted silently.
The full contextual telescoping and polynomial ledger remain to be written.

L080's audited circuit-only leaf component uses no bound on deletion-set
size beyond its separate branch enumeration: each supplied leaf has
O(T) scalar-replaced nodes and unchanged k, so its per-leaf p(T) budget
should apply. This reception still needs an explicit hypothesis check.
L072's recombination is received only after its formal premises hold.
Relevant existing stops 019–020 concern universal OBDD width and degree-only
identical-output conversion; neither supplies nor refutes this tree premise.
No script or finite preview is being used as proof. All prior work is preserved.

Completed outcome: the full proof and qualifications are canonical in
`lemmas/L081-adaptive-input-query-tree-affine-abp-data.md`. Its leaf
reception checks that L080's per-leaf bounds do not use the logarithmic
deletion-set cardinality. Exact subtree interpolation and contextual
telescoping establish the adaptive interfaces, and independent graph
copies give one polynomial in T+B. Symbolic discriminators cover the
previously proposed boundary cases. No finite computational test was
needed or claimed. The new separate-audit assessment is REVIEW_REQUIRED;
this construction is not its own critical audit or a main-goal candidate.

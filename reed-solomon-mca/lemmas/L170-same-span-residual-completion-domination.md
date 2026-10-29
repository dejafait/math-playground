# L170 — Same-span residual completion domination

## Hypotheses

Use precisely L109's original 756 six-by-21 blocks N_a over F_97 for
S=(1,8,12,18,22,27,33) and J=(47,50,64,70,75,79,85,89,96).
Labels are ordered first by the increasing two-subset I of S, then by
the increasing two-subset K of J; A_a=I_a union K_a. No mandatory pair,
symmetry identification or coding converse is assumed. Put H=S followed
by J as the ordered sixteen-coordinate list.

A history T is an increasing list of distinct labels whose supports are
pairwise linear (intersection size at most one), whose integer coordinate
degrees d_h(T) are at most four, and whose whole-block row span
W(T)=sum_(a in T) row(N_a) has dimension less than 21. Let last(T)=-1
for the empty history. Define the **entire** candidate set

    B(T)={a>last(T): dim(W(T)+row(N_a))<21,
          |A_a intersection A_b|<=1 for every b in T,
          d_h(T)<4 for every h in A_a}.

Let U,T be such histories with

    W(U)=W(T), |U|=|T|, d_h(U)=d_h(T) for every h in H,
    B(U) subset B(T).

Ranks and spans here concern the original blocks, including every
deficient rank and optional zero-increment additions. The finite
occurrence assertion below concerns only the frozen complete `nodes` in
`scripts/pair-free-envelope/cover.json`, not its frontier or partial scans.

## Conclusion

Every feasible deficient increasing completion X of U is also a
completion of T, with the same added labels and final cardinality. This
holds over every extension field of F_97. It preserves existence of a
completion of any prescribed cardinality, including twelve; it does not
preserve an arbitrary coding gate or assert equality of labeled families.

For the frozen histories, the bounded comparison below independently
verifies 29124 strict-inclusion pairs and 26205 equal-candidate pairs
among the first 100000 of 360214 eligible unordered node-ID pairs.
There are 31 verified acyclic domination arrows whose two endpoints
are branching states. Thus the required occurrence threshold of one
nontrivial comparison between distinct histories is met. Only this
prefix was compared; no assertion of global absence or complete pruning
is made about the remaining pairs.

No node or frontier record was deleted. No new block-rank test was
performed. Neither a smaller complete cover nor a capacity bound of
eleven for all families follows; all 1665 original frontier obligations
remain. This is a local specialization of known state dominance, not a
claim of progress beyond the checked general dominance literature.

## Proof

### Known input and specialization

Use the semantic completion comparison in Kuroiwa–Beck,
*Domain-Independent Dynamic Programming*,
[arXiv:2401.13883v5, section 3.3.1, Definitions 14–15 and Theorem 5,
pp.12–13](https://arxiv.org/pdf/2401.13883v5).
The general theorem has finite/acyclic/Principle-of-Optimality
hypotheses; it does not identify a sufficient notebook state. The
following argument supplies the specific completion map and an acyclic
policy explicitly rather than assuming that equal spans identify states.
Troels Martin Range, *Exploiting Set-Based Structures to Accelerate
Dynamic Programming Algorithms for the Elementary Shortest Path Problem
with Resource Constraints*, Discussion Paper 17/2013,
[sections 3–4.1, Dominance 1–2, pp.4–6](https://www.sdu.dk/-/media/files/om_sdu/institutter/ivoe/disc_papers/disc_2013/dpbe17_2013.pdf),
retains unavailable-set information as well as resources. This is why
B-inclusion, including ordering and selected-support conflicts, is kept.
The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-28-residual-domination-offline-test-review.md`.

### All completions, including future conflicts

A completion X of U is a possibly empty increasing list such that U
followed by X is increasing, pairwise linear, degree at most four and
has deficient final span. Every a in X lies in B(U): the single-block
span W(U)+row(N_a) is contained in the deficient final span, and the
order, individual compatibility and residual degree conditions follow
from feasibility. Therefore X subset B(T).

The strict cutoff in B(T) puts every label of X after T and outside T.
Each such support is compatible with every selected support of T.
All mutual support intersections within X are unchanged. At every h,

    d_h(T)+d_h(X)=d_h(U)+d_h(X)<=4.

Finally the two final spans are equal:

    W(T)+sum_(a in X) row(N_a)=W(U)+sum_(a in X) row(N_a).

Thus T followed by X is feasible and deficient. Every prefix has
degrees bounded by the final degrees, inherits linearity and increasing
order, and has span contained in that deficient final span. This also
establishes the sequential completion, not merely eligibility of the
first child. Equality |T|=|U| preserves final cardinality. Empty X and
zero-increment blocks satisfy the same argument without division.

All original matrices are over F_97. Equality of their base-field spans
extends to any extension field, and their ranks are invariant under
extension by vanishing and nonvanishing minors. No rational descent of
a decomposable vector is used. The proof concerns the support/rank
relaxation; no statement about weights, projection ranks, chart gates
or the original challenge is transported.

### Representatives and unresolved obligations

For a strict B-inclusion allow an arrow from the smaller B to the
larger B. For equal B retain only the arrow from the larger node ID to
the smaller. Every arrow strictly decreases (-|B|,node ID) in
lexicographic order, so no directed cycle exists. Choosing, for each
source with arrows, its target of least potential yields a finite chain
ending at a node having no selected outgoing arrow. Completion
preservation composes along the chain. All arrows preserve history
cardinality; ordinary child edges increase it, so adding child edges
cannot create a cycle either.

This is a policy for possible future deletion, not permission to declare
the terminal representative solved. Its entire residual search must be
covered or excluded by an existing verified capacity certificate.
Every retained branch keeps its unresolved descendant obligations.
In particular equal states cannot both be deleted without retaining a
representative. No actual deletion or tree reconstruction is part of
this certificate.

### Frozen finite occurrence and complete evidence

The full producer and independent certificates are respectively
`scripts/residual-domination/comparison.json` and
`scripts/residual-domination/verification.json`.
They contain all groups, every recomputed complete candidate list,
every tested pair with both inclusion flags, all acyclic arrows and a
representative policy with explicit residual obligations. Input SHA-256
digests bind the two read-only pair-free certificates and the unchanged
assessment. The independent verifier also checks the prior verifier
source hashes and that both frozen inputs retain their original bytes.

The producer reconstructs incidence from the lexicographic product of
two-subsets, represents label sets by bit masks and computes B from
the complete saved extension increments, order cutoff, support
compatibility and saturated coordinates. The independent verifier
reconstructs incidence from all four-subsets having two coordinates in
S and two in J. A label conflicts with a selected support precisely
when it lies in a bucket for one of that support's coordinate pairs;
the verifier removes these buckets and all saturated-coordinate
buckets from the saved deficient extension envelope. This recovers
every candidate set by a different finite set calculation.

Both methods exclude frontier states. Every included node has all 756
saved increments; the verifier checks all saved span kernels, ranks and
increments against the prior independent verification, whose complete
cover hash and zero-failure report are retained. It does not recompute
any rank or finish an untested prefix. Grouping uses the exact canonical
kernel, cardinality and sixteen residual degrees. Distinct canonical
span identities are checked against the saved verification. The producer
orders node pairs by nested node IDs; the verifier independently merges
the groups' ordered pair streams. Both compare the same first 100000
eligible pairs and test both directions. Every arrow's hypotheses,
strict potential, full representative chain and unresolved obligation
are checked independently.

There are 102667 complete nodes, 33145 groups (18726 non-singleton),
360214 eligible pairs and 100000 tested pairs. Of these, 29124 have
strict inclusion and 26205 have equal B sets. The resulting 81534 true
directed inclusions reduce to 55329 arrows under the acyclic equality
policy. Of these 31 have a branch source and branch target. The chosen
policy has 13997 sources and 4906 distinct terminal representatives;
these are offline relation counts, not an achieved cover-size reduction.
The independent verifier reports zero failures.

For an explicit strict example, node 22 has history
(0,51,98,141,275,340) and B={391,392,395}; node 934 has history
(0,51,98,177,275,304) and B={356,391,392,395}. Both use saved span 16
and degree vector (4,3,1,2,1,1,0,1,1,2,2,2,1,2,1,0).
Thus node 934 represents completions of node 22. Both are already
capacity leaves; this example alone would not demonstrate branch reuse.
For that, the independently saved `branch_arrow_nodes` give the equal-B
arrow 4851 to 1006: their distinct histories are respectively
(0,51,99,175,318) and (0,51,98,177,318), both use span 274, have equal
degrees and identical complete 70-label B sets. Both are branch nodes.
The full 70-label sets and all remaining arrows are in the certificates;
their actual search obligations have not been discharged by this test.

Reproduction commands, from this notebook:

```bash
make -C scripts/residual-domination compare
make -C scripts/residual-domination verify
```

The original combined block-test cap remains exhausted. These commands
only process saved incidence and rank values, with zero new matrix
operations. The finite occurrence test satisfies its continuation test
but leaves uniform exclusion, representation and challenge identification
unresolved. Same-step independent checking is complete; a separate
critical audit of this new specialization remains pending.

## Mathlib

Full matching coverage for this history-specific dominance criterion
and finite certificate has not been checked. No Mathlib theorem is
asserted absent, and no formal verification is claimed. The mathematical
argument is the explicit finite completion map above, with precise
general state-dominance citations and reproducible local evidence.

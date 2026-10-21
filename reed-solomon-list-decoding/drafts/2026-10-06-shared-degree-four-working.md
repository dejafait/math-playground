# Shared degree-four extension — bounded construction attempt

The approved target is unchanged: determine whether L028's outer f,F
admits the specified shared degree-four extension. Inputs read: L027,
L028, L029, foundations/07 and foundations/08; prior EXPLORE assessment
is drafts/literature/2026-10-06-shared-degree-four-moment-extension.md.
ATTEMPTS/019–020 remain stopped. No further literature is needed for
this fixed-witness test under the saved scope.

Construction to test: replace the seven auxiliary evaluation elements
{0,...,6} in L028 by seven distinct elements of F_137 for which the
root quadratics of every matching of three disjoint pairs are linearly
independent. L028's size and pair counts use only distinctness, so
would be unchanged. Three distinct quadratic graphs with empty triple
intersection and pair intersections of size two would force precisely
a dependence among such root quadratics. If the finite condition holds,
every relabeled packing would avoid the entire incidence pattern,
independently of actual determinant labels. Its indicator distribution
would then provide common moments of all degrees.

This is an unverified construction proposal, not an extension claim.
Test all 105 matchings of six points of a candidate seven-set, retaining
the exact determinants; use at most 1000 deterministic candidate sets.
Success requires a proof of unchanged first/second moments and all-core
edge avoidance, not just a successful determinant search. If no set is
found, record failure of this ansatz only. The sufficient cap below
1532496, global realizability, safety at 67/68 agreements and ABF
equivalence remain independent unresolved questions.

## 2026-10-07 attempt checkpoint

The fourth candidate in the bounded deterministic search is
{16,64,70,102,112,118,121} in F_137. All 105 required determinants
are nonzero, and the monic-polynomial root histogram gives L028's
unchanged neighbor counts. Full evidence is saved in
scripts/finite-support/shared-degree-four-results.json. Before claiming
an extension, finish the symbolic check that pairwise overlap roots
are disjoint when the triple intersection is empty, and that the
permutation average preserves every prescribed moment of size <=2.
This checkpoint preserves unfinished reasoning; the canonical completed
result, if established, will be L030.

Completed later in the same attempt: L030 now contains the full proof
of disjoint evaluation-root pairs, all-core edge avoidance, unchanged
pair moments and one finite representing distribution. The exact
certificate passed all nine arithmetic checks. The diagnostic is stopped
as recorded in ATTEMPTS/021; independent critical audit is the sole next
action in PROGRESS.md. The unfinished checkpoint above is preserved as
the record of the attempt, not an additional unresolved mathematical claim.

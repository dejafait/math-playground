# Full allocation cyclic-order rigidity — source assessment

TARGET: Test whether the endpoint/domain/J system with L055's fixed pairs and all nonnegative integer b_i summing to 9250245 forces literal cyclic order among all permutations of the intact rows with a_i=2+18b_i.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Focused prescribed-block, cyclic-guard, affine-ordering and exact-budget web queries; narrow local comparison of L051/L055/L069/L072/L073, ready October 14/16 assessments and Attempts 026–031 found no inspected theorem deciding simultaneous full allocation and order.
SOURCE_EVIDENCE: Reopened published Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and essential induction pp. 228–229, Lemma 4 and exchange proof p. 230; Kubo–Makino–Sakamoto (ISAAC 2024), scalar objective and Theorems 1/3 definitions/statements pp. 44:2–44:4; reused ready proof-case, extremal-word and DLMF assessments.
COMPARISON: Formal affine machinery applies, but scalar ordering and rotation extrema supply no simultaneous own-input guard verdict; C073a/C073b fix literal order, and L069/L072 fix narrower supports. L073 supplies an arbitrary-tail monotonicity precedent that must be matched to the proposed prefixes separately.
GAP: Full-simplex cyclic-order rigidity is unproved; a separate attempt must justify allocation-uniform product control, domain-valid prefix comparisons, rotation and complete first-displacement coverage, or certify a nonliteral feasible tuple.
REASON: Essential source scope is now assessed; approve one separate bounded SPECIALIZE attempt on exactly TARGET, importing affine machinery and deriving only the full-allocation applicability/comparisons. No rigidity verdict or new inequality is established in this literature turn.
SCOPE: Exactly TARGET with the 25 L055 indexed pairs, intact outgoing rows, integer b_i>=0 of total 9250245, real s>=540/11, every exact endpoint and own-input non-strict J guard including closure; no distinguished large-tail row, H/seed, minimum-location, integrality, actual-word or primitive/count-ray premise.
LITERATURE_REASON: The saved REVIEW_REQUIRED target combines arbitrary allocation with arbitrary order, outside prior ready scopes; this one changed-hypothesis comparison is essential despite the literature balance target.

The original proposal below is retained as the scope and motivation from
step 265. Its pending-review language describes that proposal; the separate
comparison at the end completes source coverage for a later attempt only.

The proposed system uses the same 25 indexed J_i,H_i pairs and budget
as C073a. Choose an arbitrary permutation pi of {0,...,24}, carrying
each allocated a_i with its indexed pair. At chronological position k
require a real input s_k>=540/11, closure s_25=s_0, and

\[
s_{k+1}=2^{-a_{\pi(k)}}\left((27/16)^{J_{\pi(k)}}
(3/2)^{H_{\pi(k)}}s_k-(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11,
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\]

The question is whether every feasible order is a cyclic rotation of
0,1,...,24. There is no fixed large-tail row, assumed minimum location,
H/seed condition, integer realization or primitive/count-ray premise.
Repeated junction values remain allowed. This statement defines a
target; it supplies no feasible tuple or new implication.

The main gap is universal eventual descent. A positive order result
could allow rotation into C073a's literal scope, and later an actual-word
application; those assemblies are not part of the present step. Even
that restricted exclusion would leave other pairs, unrestricted cycles,
entry and divergence unresolved.

Potential inputs for review are L055's indexed pairs and invariant
counts, L069's cyclic-product and first-displacement method, L072's
narrower changed-support comparison, L073's literal support result,
and audited C073a/C073b as downstream uses. These are candidate inputs,
not an asserted dependency graph. L051 supplies the endpoint/J
definitions. Inspect only the relevant passages after comparing their
scopes. Do not transfer a negative shifted offset from tail 2 or tail 20
to arbitrary tails, or assume a formerly distinguished large-tail row
remains large. Any proposed tail comparison must justify the sign of
the quantity being divided before using monotonicity. No such comparison
has been derived in this audit turn.

Continue toward a separately approved bounded mathematical test only
if the literature comparison supports an allocation-uniform cyclic-root
bound and a concrete first-displacement comparison, or identifies a
stronger applicable known theorem. A feasible nonliteral cyclic tuple
would refute rigidity; a failed sufficient margin would stop only that
comparison. If neither an applicable theorem nor a justified test is
available, record the exact missing premise and choose a different
independently testable target under the bounded-exploration rules.
Preserve the two literal rational witnesses and Attempts 026–031;
their real-feasibility and modular-diagnostic stops are not reopened.
Full matching Mathlib coverage remains unchecked.

## Separate source comparison — step 266, 2026-10-17

### Primary results and limits of applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published PDF](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
section 2, equations (2)–(4), Lemma 2, pp. 228–229, gives the real affine
composition of a finite binary word and its nonzero-denominator fixed
point. Read the length-one and appended-zero induction; appended one is
stated analogous. This is the eligible import, with no integer-realization
inference. Lemma 4, p. 230, compares numerators of distinct words with equal
length/one count under every-prefix count domination; its finite exchange
proof was read. Equal totals alone do not supply that premise. Reuse the
previously inspected Lemma 5/Corollary 1 rotation-extremum comparison in
[step 254](2026-10-16-arbitrary-tail-literal-early-support.md).

Kubo–Makino–Sakamoto, *Composition Orderings for Linear Functions and
Matrix Multiplication Orderings*, ISAAC 2024, 44:1–44:14,
DOI 10.4230/LIPIcs.ISAAC.2024.44,
[published PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol322-isaac2024/LIPIcs.ISAAC.2024.44/LIPIcs.ISAAC.2024.44.pdf):
read the fixed-real-input scalar objective, angle/collinearity/potential
identity definitions and all three cases of Theorem 1, pp. 44:2–44:3;
read the adjacent-interval neighborhood definition and Theorem 3's
local/global minimum equivalence, p. 44:4. Reuse the case-(i)/(ii) proof
inspection in [step 222](2026-10-14-last-pair-permuted-j-feasibility.md).
Case (iii)'s omitted proof/full-version lead remains unimported and
nonessential: no optimizer or local/global theorem is used here. Positive
slopes cover both contracting and expanding affine maps, but scalar
optimality is not simultaneous intermediate-guard feasibility at a cyclic
root. No ordering conclusion for the present rows is inferred.

Reuse [step 246's comparison](2026-10-16-earlier-recipient-all-order-j-feasibility.md)
of Fernandez–Ibanez, arXiv:2607.24844v1, Theorem 7.3 and Theorems 8.1/8.2
with inspected proofs. Those scalar rotation extrema and actual-periodic-word
statements do not supply this prescribed-block guard theorem. The supporting
theory is not independently audited and no result from that lead is imported.
Reuse step 254's DLMF 4.5.1/4.2.19/4.6.4 scope and L055's established
outward rational logarithm certification method if a later calculation
needs it; a new tuple or bound still needs complete evidence. General
affine coding or logarithm-series reproof is unnecessary. Full matching
Mathlib coverage is unchecked; no absence claim is made.

The formal-word hypotheses match the existing finite endpoint templates
of L051/L055. L055's complete indexed table and count-dependent positive
Lambda enclosure are eligible inputs; L073 already records the full
simplex's total-tail accounting. The later attempt must explicitly match
these facts under permutation before using denominator/product assertions.
The real affine identity supplies neither the lower domain nor any J
guard, and the old order-dependent root bound is not an imported bound
for new allocations.

Reopened [MathPrize's page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07: the ordinary map x/2 for even x and 3x+1 for odd x
must reach 1 for every positive integer. This is the unchanged exact
target; reward adjudication is not a mathematical input.

### Discovery, duplicates and preserved stops

Queries actually run in this review:

- `Collatz rational cycles prescribed blocks permutation even exponents fixed sum inequalities cyclic order`
- `Collatz affine maps order allocation exponents "rigidity" cycles`
- `"Collatz" "9250245"`
- `Collatz "prescribed" "cyclic" "inequalities" rational cycles`
- `"Composition Orderings" "cyclic" constraints Collatz`

The exact-budget query was also checked separately and returned no results.
Broader queries surfaced the primary 1997 paper, known cycle bounds,
informal discussions and claimed solutions. No inspected matching theorem
was found; failed discovery is not evidence of novelty. The unread
high-cycle, generalization and intercept-coverage leads recorded in step
254 remain nonessential for this real endpoint/guard question, so they
are not source blockers or inputs.

Read L051's definitions, L055's full indexed table/counts, L069's product,
rotation and first-displacement proof, L072's hypotheses and corresponding
prefix proof, and L073's hypotheses, product and first-recipient comparison.
L069's preceding literal rows have tail 2; L072's have tail at most 20.
Their negative shifted-offset estimates therefore cannot simply be assumed
for arbitrary allocated tails. Neither statement decides the full simplex.
L073 covers arbitrary allocation only in literal order. Its proved
tail-monotonicity comparison on the lower domain is a concrete precedent
to test in a later attempt; this review does not extend its conclusion or
derive a replacement prefix estimate. C073a/C073b remain downstream
literal-order exclusions, not order-rigidity inputs.

Read Attempts 026–031. L055's full real witness stops excluding the
unchanged real system outright. L057/L058/L060/L061 stop the recorded
prime-five/two-prime diagnostics, while L062 rejects one different order
by its own J guard. None supplies a nonliteral feasible tuple for this
full-simplex question or prohibits a guard-based order test. Preserve
both rational witnesses and all stops; no modular route is reopened.
The supplied overview/DAG and narrow October 14/16 assessment search
showed only the narrower stated scopes, not a duplicate full-allocation
order theorem. No cross-notebook theorem is used.

### Approved bounded mathematical continuation

Permit one later SPECIALIZE attempt on exactly TARGET. L055 supplies
the indexed pairs and certified Lambda bounds, L051 the endpoint/J
definitions, L069 the minimum-product/first-displacement method, and
L073 the established domain-sign and tail-comparison precedent.
L072 is a narrower comparison, not an exclusion to transfer. Any resulting
proof must cite the general affine identity rather than reprove it.

The concrete test is to check whether L069's cyclic-product control and
first-displacement scheme can be justified uniformly over the full simplex
using L073's domain-valid tail monotonicity, with every comparison sign
and intermediate-domain premise explicit. Seek a strictly rejecting
own-input J margin at every possible first displaced row after a justified
rotation. Do not infer a bound for arbitrary tails from an old negative
offset, assume row 24 remains large-tailed, or assume which row carries
the minimum. No uniform comparison or margin is proved in this review.

A proof must cover the entire integer allocation simplex and every
intact cyclic order, retaining all 25 endpoints, both cyclic cuts and
own-input pairings. Alternatively, one specified allocation and nonliteral
cyclic order with an exact factored root, certified full domain and all
25 non-strict J guards refutes rigidity. Numerical survival is only a
candidate. A failed sufficient margin stops that comparison alone; save
its exact failed premise/value and reassess rather than assert feasibility
or enlarge the target. This is one bounded test, not a new exploration
budget or a mandate to generate a lemma.

A positive result could later rotate an all-order tuple into C073a's
literal scope and support an actual-word exclusion; those assemblies
require their own review. Other pair tables, unrestricted cycles, entry,
divergence and universal eventual descent remain independent gaps.
Outcome EXPLORATION records completed source comparison and an actionable
test, not mathematical progress beyond the sources. No lemma, mathematical
script, DAG or PROOF was changed.

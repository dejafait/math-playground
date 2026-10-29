# Residual-history domination — completed source comparison

TARGET: Assess residual-history domination for identical spans as a replacement for the capped pair-free traversal.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 538 searched state/resource/elementary dominance, exact packing and Reed–Solomon overlap; inspected the primary sources and scoped local records listed below. No matching instance-specific pruning theorem was located; no novelty follows.
SOURCE_EVIDENCE: Kuroiwa–Beck, arXiv:2401.13883v5 (12 March 2026), section 3.3.1, Definitions 14–15 and Theorem 5, printed pp.12–13; also inspected v3 Theorem 5's full feasibility cases. Range, Discussion Papers on Business and Economics 17/2013, sections 3–4.1, printed pp.4–6, Dominance 1–2. Beck et al., CP 2025 article 5, section 4.1 Example 6, printed pp.5:5–5:6. Direct links and qualifications below.
COMPARISON: Standard state dominance requires preservation of complete solution extensions, objective and solution length; resource dominance alone omits unreachable choices. These sources permit investigating a conservative same-span residual-state specialization, but do not prove candidate-set inclusion sufficient for this notebook or promise compression.
GAP: Prove or refute the proposed local criterion and test whether it occurs among saved complete histories. No histories have been compared, merged or discarded; no twelve-row bound follows from this review.
REASON: Essential general dominance coverage is now accessible and inspected. A later bounded applicability proof and offline comparison are justified; mathematical derivation and implementation are deliberately deferred to a separately approved turn.
LITERATURE_REASON: New hypothesis-sensitive pruning mechanism, prompted by the capped traversal's many separate histories sharing relatively few spans; generic closure coverage does not approve it.

## Completed review — step 538

Main gap: uniform twelve-row exclusion for the fixed L109 partition.
Intermediate target: a sound comparison of complete residual problems at
identical whole-block spans. Its downstream use would be to compress a
later cover, without identifying C152a's unspecified pair. Representation,
coding gates and challenge identification remain independent gaps.

### Primary statements and scope

1. Ryo Kuroiwa and J. Christopher Beck, *Domain-Independent Dynamic
   Programming*, accepted manuscript, [arXiv:2401.13883v5](https://arxiv.org/pdf/2401.13883v5),
   12 March 2026, section 3.3.1, Definitions 14–15, Theorems 4–5,
   printed pp.12–13 (PDF pages 13–14). State dominance quantifies over
   every solution of the dominated state, requires an at-least-as-good
   solution of the other state, and does not permit a longer continuation.
   Approximate dominance must be a preorder implying this semantic
   relation on reachable states. Theorem 5 assumes a finite, acyclic
   DyPDL model satisfying the Principle of Optimality. Its value inequality
   is not a test for those hypotheses or for dominance itself. Read its
   feasible/feasible and infeasible-dominator proof cases; the
   [v3 statement and proof](https://arxiv.org/html/2401.13883v3#S3.SS3.SSS1)
   also explicitly treat an infeasible dominated state. Read v5's preceding
   positive-reward counterexample to value-only pruning and Appendix A's
   base/non-base and removed/not-removed open-state cases (printed
   pp.44–46). These explain why an actual retained representative is
   necessary. No notebook transition model is proved here.

2. Troels Martin Range, *Exploiting Set-Based Structures to Accelerate
   Dynamic Programming Algorithms for the Elementary Shortest Path Problem
   with Resource Constraints*, Discussion Papers on Business and Economics
   17/2013, 16 October 2013, [university primary PDF](https://www.sdu.dk/-/media/files/om_sdu/institutter/ivoe/disc_papers/disc_2013/dpbe17_2013.pdf),
   sections 3–4.1, printed pp.4–6 (PDF pages 5–7). Read the path/resource
   setup, the restriction to separable nondecreasing resource extension
   functions, and Dominance 1–2. For paths at the same terminal vertex,
   cost/resource comparison alone is insufficient: elementary dominance
   additionally requires inclusion of the dominating path's unreachable
   set in the dominated path's unreachable set. The source explicitly
   explains the missing-extension failure of resource-only deletion.
   This is primary coverage of a labeling method, not a theorem about
   whole-block rank or our support conflicts. No performance guarantee
   transfers from its experiments.

3. J. Christopher Beck, Ryo Kuroiwa, Jimmy H. M. Lee, Peter J. Stuckey
   and Allen Z. Zhong, *Transition Dominance in Domain-Independent Dynamic
   Programming*, CP 2025, LIPIcs 340, article 5, 5:1–5:23,
   [published primary PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol340-cp2025/LIPIcs.CP.2025.5/LIPIcs.CP.2025.5.pdf),
   DOI 10.4230/LIPIcs.CP.2025.5. Read section 2's finite/acyclic/optimality
   assumptions, Definitions 1–2, Proposition 3's statement and section 4.1
   Example 6 (pp.5:3–5:6). Example 6 shows that imposing both directions
   of a tie can remove every choice. This is a qualification for future
   representative selection. Transition dominance differs from comparing
   states; Proposition 3 is not imported as our history-pruning theorem.
   Its full appendix proof is not claimed as an essential imported input.

Ibaraki, *The Power of Dominance Relations in Branch-and-Bound Algorithms*,
JACM 24(2) (1977), 264–279, DOI 10.1145/322003.322010, is an unread
historical lead: the publisher PDF returned HTTP 403. No theorem from it
is used. It is not essential given the accessible primary state-dominance
coverage above. Full matching Mathlib coverage was not checked.

### Proposed specialization, not an established rule

The precise future test compares two saved complete feasible histories
T and U with the same entire span W, equal selected cardinality and
equal sixteen-coordinate residual degree vectors. Test the proposed
direction "U can be represented by T" only when B(U) is a subset of
B(T), with the complete original B lists, including ordering. No
implication from these conditions to safe pruning is asserted this turn.

The later applicability proof must cover **every** completion, not just
one next row. It must separately verify selected cardinality, all integer
capacities, compatibility with selected supports, conflicts among future
supports, original increasing order, optional zero-increment labels,
deficiency after every extension, and all field extensions of F_97.
It must explain how any retained representative's search obligation is
discharged; mutually equivalent histories cannot all be deleted. No
relabeling of supports, rank-only transport or enlarged coding domain
is covered. This is ordinary specialization of known dominance methods,
not a proposed creative theorem about MCA.

Compare at most 100000 distinct unordered history pairs, in increasing
node-ID pair order within equal-(span,cardinality,residual-degree)
groups, testing both inclusion directions for each pair. Use only fully
materialized `nodes` in the frozen `cover.json`; `frontier` records and
partial extension vectors have no complete residual problem here. Report
all group/pair counts and whether the pair budget exhausts the eligible
list. No new rank test, resumed traversal or cap reset is authorized.
Any proposed deletion requires a separately checkable certificate and
an acyclic representative policy, after the proof. An offline count alone
does not establish a smaller complete cover.

Continue this mechanism only if the universal applicability argument
passes and at least one nontrivial comparison is independently verified.
Otherwise stop this conservative replacement on the tested saved domain;
a partial pair scan cannot prove global absence of domination. Even a
positive test establishes neither sufficient compression nor uniform
capacity <=11. A later traversal would need a fresh, explicitly assessed
budget and cover invariant; the original cumulative cap remains exhausted.

### Duplicate, failure and search record

Read L169's hypotheses and descendant/ordered-history/capacity argument
through its dual construction, the pair-free pre-run invariant, its
result's cap qualifications and the ready pair-free assessment. Scoped
searches of the closure working record, original closure assessment,
ATTEMPTS/041,043,048,055 and histories 536–537 found no established
residual domination rule. ATTEMPTS/048 was read in full: equal pair ranks
do not identify kernels or give transport. Its stop is not a ban on the
different history-sensitive proposal. L169's span cache and closure
enumeration coverage remain reusable; they do not supply this rule.
Read only the saved producer's serialization and complete-node construction
to locate the necessary future fields; no certificates were sampled as
mathematical evidence and no scripts were run or edited.

Queries (2026-10-28):

- `Ibaraki 1977 dominance relations branch and bound algorithms dominance theorem pdf`
- `dynamic programming dominance same state remaining resources feasible extensions dominance theorem label setting primary`
- `"Feillet" "2004" "dominance" pdf elementary shortest path`
- `"domain-independent dynamic programming" "dominance" theorem pdf`
- `"Ibaraki" "Power of Dominance" filetype:pdf`
- `"Domain-Independent Dynamic Programming" Kuroiwa Beck arxiv`
- `"The Power of Dominance Relations" Ibaraki pdf 264`
- `"set packing" "dominance" "partial solutions" resources conflicts`
- `"Reed-Solomon" "span" "dominance" packing`
- `"branch and bound" "identical" "residual" dominance conflict`

Other search leads (scheduling packing, residual conflict cuts and
hitting-set compression) were not inspected at theorem level and supply
no coverage or obstruction here. An accidentally opened unrelated arXiv
record 2401.13896 was immediately excluded; the inspected DIDP identifier
is 2401.13883. No failed search establishes originality.

## Original intake, preserved

The main gap remains uniform twelve-row exclusion for L109's fixed
partition. The intermediate target proposed for the next turn is a source
comparison for history-sensitive domination **within an identical whole-block
span**. A sound criterion might permit a smaller cover; it need not resolve
the rank/incidence question. This is a proposal, not a derived criterion.

Retain L109's 756 original blocks and the arbitrary-extension rank problem;
all supports are optional, pairwise intersections are at most one, and
ordinary integer degrees are at most four. L169 remains fixed-pair only.
No rank-only transport, symmetry, closure-only descendant pruning or coding
converse may be added. The cap evidence must remain intact, and the original
attempt's counters may not be restarted or silently extended.

Compare exact standard terminology and primary theorems for dominance in
finite packing/branch-and-bound problems with the complete residual state:
selected cardinality, coordinate capacities, individually admissible labels,
mutual support conflicts and the increasing-order restriction. Inspect the
load-bearing hypotheses and proof cases, not just solver descriptions.
No order between residual states is asserted in this intake. Check duplicates
in the existing closure working record and assessments; retain all recorded
counterexamples and rank/gate failures.

Continue only if the comparison identifies a precise independently testable
criterion whose later proof or imported theorem covers these residual states.
Otherwise reject this replacement and select an independently specified
target. No claim of novelty or of a faster complete calculation follows
from the observed history/span ratio. Full matching Mathlib coverage is
not checked. No cross-notebook input is proposed.

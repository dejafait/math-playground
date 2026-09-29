# Paired-state backward transitions: literature assessment

TARGET: Derive the backward transition rules for (z,y)=(4y+1,y) from L011, retaining their one-block depth offset, and test whether they force descent below one of the two original starting values.
CHECKED: 2026-09-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searches on 2026-09-26 for Collatz inverse parity vectors, pruned inverse trees, 4n+1 coalescence, non-descending first merges, and equal-total-stopping-time clusters; queries and follow-up reading are recorded below.
SOURCE_EVIDENCE: Read Rozier (2019), Lemma 1 and Theorem 1, pp. 2–4, https://math.colgate.edu/~integers/t8/t8.pdf; Andaloro (2000), Lemmas 2–4 and the remark after Theorem 1, pp. 74–75, https://www.mathstat.dal.ca/FQ/Scanned/38-1/andaloro.pdf; Monks et al., arXiv:1204.3904v2, sections 4–5, https://arxiv.org/pdf/1204.3904v2; LaDue, arXiv:1709.02979v3, Theorems 3.2 and 4.1 and Corollary 4.3, pp. 4–5, https://arxiv.org/pdf/1709.02979v3.
COMPARISON: Exact parity-word arithmetic and the 4y+1 coalescence identity are covered; the inspected results do not supply descent relative to both original starts for the four-block alphabet with L011's one-block offset.
GAP: Determine whether compatible earlier prefixes can compensate the forced contractions while both histories retain their separate non-descent inequalities; neither coalescence nor uniqueness of an endpoint for a fixed infinite reverse word answers this.
REASON: Reuse the cited formulas and L010's exact block inverses; the justified specialization is their coupling with maximal-block indices and two original starting thresholds, not a reproof of inverse arithmetic or coalescence.

## Hypotheses

The target is unchanged from the checkpoint at turn start. Use the positive odd
histories and exact maximal-block alphabet {(1,1),(2,1),(3,1),(1,2)} of
L010 and L011. Each history starts above 1, and every endpoint must stay
at least as large as that history's own start. This is not monotonicity
between consecutive endpoints.

In L011's first-merge notation, z is at index r-2 in one history, while y
is at index r-1 in the other, with z=4y+1, y=1 modulo 3, and r>=4.
The two original starts are independent thresholds; neither may be
replaced by z, y, or a common minimum. The required unresolved assertion
is that every proposed distinct-suffix merge violates at least one of
those two original-threshold inequalities.

The main gap remains universal eventual descent. A useful intermediate
result would constrain compensating prefixes at arbitrary depth, with a
possible downstream use in proving restricted suffix rigidity. Even
complete rigidity would still leave a fixed-start bound on non-descent
depth and the treatment of other block types unresolved.

## Conclusion

The literature assessment is ready for a subsequent research invocation
under SPECIALIZE. It does not establish the proposed descent assertion.
Only the standard machinery is imported by the citations below; no new
transition system, inequality, counterexample, or lemma was derived in
this literature-only turn. The completed-step classification is
NOVELTY_UNCHECKED: no originality claim is made for the unresolved part.

The current achieved bounds remain those already recorded: analytical
suffix rigidity through three blocks, and an exact finite screen through
six. The required restricted conclusion concerns every depth, so neither
bound reaches it. Repeating the elementary merging identity would not
improve either bound.

## Proof

This section records precise inspected citations and scope comparisons,
not a proof of the target. Statements below retain their sources' domains
and time conventions.

### Parity-word arithmetic

Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers
and Euclidean Embedding*, INTEGERS 19 (2019), A8, published 2019-02-01:
[sections 1–2, Lemma 1, its proof, and Theorem 1, pp. 2–4](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
These statements were read anew, extending the earlier portfolio audit.
For the same shortcut map used locally, each binary word of length j
determines exactly one starting residue class modulo 2^j. Lemma 1's
proof gives the affine iterate identity; Theorem 1 gives a complementary
inverse congruence. These cover the standard finite-word machinery.
They do not assert a size comparison for two different words or histories.
Section 3.2, Corollary 2, p. 6, was also inspected: its infinite inverse
series is a statement in the 2-adic integers, not a guarantee of a positive
integer realizing an infinite history.

### The specific 4y+1 relation

Paul Andaloro, *On Total Stopping Times Under 3x+1 Iteration*, Fibonacci
Quarterly 38(1) (2000), 73–78, final revision September 1998:
[definition on p. 73, Lemmas 2–4 on p. 74, and remark after Theorem 1 on p. 75](https://www.mathstat.dal.ca/FQ/Scanned/38-1/andaloro.pdf#page=2).
The paper uses the odd-only map A(x)=(3x+1)/2^v_2(3x+1), called T there.
Its p. 75 remark explicitly states A(4x+1)=A(x) for odd x and explains
that the coalescence in Lemmas 3–4 does not assume convergence to 1.
Lemma 2 equates the odd-only total stopping times of x and 4x+1 for
odd x other than 1. This is the closest exact coverage of the pair
relation. Neither that identity nor the smaller comparison start in
Lemma 4 supplies an earlier iterate below each history's original start.
Odd-only stopping time and the notebook's maximal-block depth must remain
distinct. Only the stated 4x+1 identity is imported from the remark;
its other affine-interaction assertions are not used here.

### Inverse trees and the direction of uniqueness

Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, and Maria Monks,
*Strongly Sufficient Sets and the Distribution of Arithmetic Sequences
in the 3x+1 Graph*,
[arXiv:1204.3904v2, 2012-04-20](https://arxiv.org/pdf/1204.3904v2)
(published in Discrete Mathematics 313 (2013), 468–489).
Read the back-tracing definitions and admissibility discussion in section
4, p. 7; section 5.1, Theorem 5.1 and Corollary 5.2, p. 11; and Lemma
5.4 with proof, pp. 12–13. The basic inverse maps are 2x and (2x-1)/3
with their admissibility conditions. Theorem 5.1 says one infinite
reverse parity word containing infinitely many odd steps determines at
most one 3-adic endpoint. It does not give a unique reverse history for
one endpoint. Lemma 5.4 bounds the limiting upper fraction of odd reverse
steps by log_3(2); it is not a finite-prefix bound relative to two starts.
Section 5.3, Theorem 5.7, pp. 15–16, was also read: every infinite
reverse path avoiding multiples of 3 visits 2 modulo 9. None of these
statements imposes the local alphabet, offset, and two threshold conditions.

### Related finite coalescence criteria

Mark D. LaDue, *Clusters of Integers with Equal Total Stopping Times in
the 3x+1 Problem*,
[arXiv:1709.02979v3, 2017-11-15](https://arxiv.org/pdf/1709.02979v3).
Read sections 2–4, especially Theorems 3.2 and 4.1 and Corollary 4.3,
pp. 4–5. For odd m=2^p(2q+1)-1>1, these identify equality of the
(p+2)-step shortcut iterates of m and m-1 exactly when p and q have the
same parity. Corollary 4.3 gives equal total stopping times under its
additional cutoff. This is a finite coalescence criterion for a specified
adjacent pair, not a condition excluding arbitrary compensated prefixes
at a common maximal-block depth. It is a comparison source, not an
additional premise for the proposed descent assertion.

As a redundancy check, also read section 2, Theorem 1 and Corollaries
1–2 of Michael R. Schwob, Peter Shiue, and Rama Venkat,
[*Novel Theorems and Algorithms Relating to the Collatz Conjecture*](https://onlinelibrary.wiley.com/doi/10.1155/2021/5754439),
published 2021-09-18, article 5754439. Corollary 2 states
C(8j+5)=4C(2j+1) for the unshortened Collatz map, called T there.
This supports the same familiar pair mechanism; its counting convention
does not resolve the maximal-block offset or original thresholds. No
global convergence or peak-value claim from that paper is imported.

## Mathlib

Full paired-state non-descent statement: **not checked**. Supporting
parity-vector, inverse-iteration, and coalescence results: **not checked**.
No Mathlib theorem name or direct library link was verified, and no
absence from Mathlib is asserted. The direct links above are mathematical
sources, not evidence of library coverage.

## Search record and source limits

Representative exact queries used on 2026-09-26:

- `Collatz inverse tree nondecreasing trajectories backward parity vector Terras Everett`
- `Collatz inverse tree Wirsching Lagarias pruned tree`
- `Collatz "4n+1" "inverse"`
- `Collatz "4x + 1" "inverse"`
- `Collatz "merging" "stopping time" trajectories`
- `Collatz "non-descending" "merge"`
- `Collatz "first merge" backward`
- `Collatz "sufficient sets" Monks Snaith`
- `Garner 1990 Collatz trajectories 2n+1 Andaloro stopping times`
- `"On total stopping times under 3x+1 iteration" pdf`

The searches led to the primary papers read above. Rozier's reference
to Andaloro was followed to the journal scan; the inverse-tree search
was followed to the Monks manuscript and its version record; the
coalescence search was followed to LaDue's theorem rather than stopping
at the abstract. The author-hosted Monks copy at
https://mathematicalgemstones.com/maria/papers/mmmm.pdf was also read;
page numbers above refer to the 35-page v2 manuscript, not the journal
pagination.

Wirsching's *The Dynamical System Generated by the 3n+1 Function*,
Lecture Notes in Mathematics 1681 (1998), and Garner's *On Heights in
the Collatz 3n+1 Problem*, Discrete Mathematics 55 (1985), 57–64, remain
unread primary references identified through the inspected papers.
Their full coverage is not asserted or excluded. No conclusion here
requires a theorem available only in those unread sources: the finite
formulas and pair identity are accessible in the primary statements
actually inspected. Other search hits, including purported full
solutions, were discovery leads only and are not evidence of coverage.
The bounded search did not establish a match for the full target; it
does not establish novelty.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
page dated 2021-07-07, was rechecked on 2026-09-26. Its requirement is
still convergence to 1 for every positive integer under the unshortened
map. Existing conventions and the Tao comparison in foundations are
retained; no density-one conclusion is upgraded to the universal target.

## Relevance, redundancy, and continuation test

The local overview, DAG, L002, L010, L011, their relevant histories,
the saved non-descending suffix test, and Attempt 008 were inspected.
L010 already supplies the exact inverse branches; deriving them again
would be redundant. Its unrestricted multiple histories refute the
old unique decoder but do not decide the stricter two-threshold question.
L001–L004's bounded-window obstructions and L008's boundary-error
obstruction remain in force. This review does not reopen those proposals.

The justified remaining work is to couple the existing inverse branches
on the pair from L011, keeping original starts and block indices as part
of the state. A useful test must yield either an order restriction on
admissible compensating prefixes that applies to an unbounded family,
or a rigorously admissible pair of distinct-suffix histories satisfying
both non-descent conditions. The latter would stop the proposed
all-depth rigidity repair. An invariant or smaller-depth reduction that
also preserves both thresholds would justify continuing; no complete
route to universal descent is required to investigate such an input.
Mere coalescence, finite-depth agreement, or a contradiction obtained by
comparing with z and y instead of the original starts is insufficient.

This completes one LITERATURE step, reported as EXPLORATION, with one
consecutive exploration turn used and at most two remaining without an
advance or informative negative result. The continuation assessment is
complete, and the same concrete target is retained for the next
invocation. No research calculation follows this review in this turn.

# Expander-family internal-deletion threshold — source comparison

TARGET: Determine whether L031's used expander family admits L073's logarithmic positive-internal deletion promise, by bounding the minimum deletions needed for residual treewidth at most two.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 283 searched expansion/treewidth, subdivision/deletion and balanced-separator statements; read the primary statements and operation proofs specified below and searched the exact local expander/treewidth records for duplicates. No exact signed-ER deletion theorem was located; no novelty inference.
SOURCE_EVIDENCE: Gurski–Weishaupt arXiv:2406.08985v1 Theorems 17–18/24–25/27 and Corollaries 22/26, pp.8–13; Marx ToC 6 (2010) Lemma 3.2(b), pp.92–93; Böttcher et al. arXiv:0910.3014v1 Definitions 1–3/Theorem 4 and footnote 1, pp.2–3; Dvořák–Norin arXiv:1408.3869v2 introduction/Theorem 1, pp.1–2. Read L031's exact gates and encoding, L030's expansion hypotheses, L071/L073's full-graph conventions and L032's comparison statement.
COMPARISON: Standard subdivision, subgraph, vertex-deletion and separator inputs cover the graph-theoretic machinery; the remaining specialization is the exact signed-gadget identification and quantitative comparison in the unchanged supplied proof encoding, not a new general treewidth theorem.
GAP: No lower bound on the positive-internal deletion number, minor model in the full signed graph, finite-size expansion constant or logarithmic-threshold comparison is proved in this literature turn; these are the approved next mathematical obligations.
REASON: Essential coverage for the changed structural target is now adequate for one bounded application of known results; L030's OBDD hardness is neither needed nor sufficient for this graph test.
SCOPE: L031's actual full signed value graph, including shared originals, all gate/sign roots and unused vertices; only positive internal extension vertices may be deleted; compare the minimum with floor(log₂(T+2)) for its full supplied proof length T.

The main gap remains unrestricted SAT decision/separation; the nearer gap
is unrestricted ER-to-affine-ABP data existence. The intermediate target
tests the coverage of L073's sufficient structural promise. A negative
answer would stop this family application and distinguish it from L032's
existing alternative circuit data; it would not exclude alternative ABP
data, other certificates or other proofs. This is one literature-only
step, with no lemma, mathematical script, new derivation or argument change.

## Local statement and duplicate/failure comparison

L031 assumes a supplied finite simple n-vertex graph, n≥2, maximum degree
at most a fixed Δ≥3, and external vertex expansion at least a fixed
0<ε<1 for every set of size at most n/2. It does not select an expander
algorithmically. Its displayed circuit has the original inputs x_v,
positive gates p_i iff x_(u_i) AND x_(v_i), signed alias r_1=NOT p_1,
the q_i conjunction chain, repeated-operand positive root h, and the
separate positive accumulators a_k. Both σ choices retain these definitions
and change the signed units/accumulator operands. There are 4m positive
extensions. These are recorded facts from L031, not a new minor proof.

Use L071's full signed graph convention as received by audited L073:
shared original vertices, constants, all positive extension AND vertices,
required NOT vertices, unused roots and actual signed operands. Treewidth
forgets wire multiplicity only; no original identification, sign removal
or Boolean simplification is authorized. L031's explicit length is
T=2+|F|+|π|, with R_*=22m+n+2, L=ceil(log₂(R_*+2)) and
T≤128(R_*+n+3)L. This upper bound and 2m≤Δn are available for the
later threshold comparison; T must not be replaced by a chosen padding.

Searched the local expander assessments/history 058–069 and the treewidth
assessment/source review for `incidence graph`, `subdivis`, `deletion
number` and balanced-separator/internal-deletion terms: no prior proof of
this structural threshold was found in those paths. Attempts 019–021 were
read: they stop universal OBDD width, degree-only identical-output ABP
conversion and a prescribed pair-table conversion, respectively. They do
not determine this deletion number. L032's hypotheses/conclusion and exact
root description were read only as the alternative-data comparison. No
cross-notebook input is used. Historical stops and unfinished work remain.

## Inspected source inputs

1. Frank Gurski and Robin Weishaupt, *The Behavior of Tree-Width and
   Path-Width under Graph Operations and Graph Transformations*,
   [arXiv:2406.08985v1](https://arxiv.org/pdf/2406.08985v1), 13 June 2024.
   Finite simple undirected graphs are specified in §2.1. Theorems 17–18
   (pp.8–9) give tw(J)−1≤tw(J−v)≤tw(J) and the reverse insertion bounds.
   Corollary 22 (p.10) gives subgraph monotonicity. Theorem 24 (p.11)
   gives contraction monotonicity; Theorem 25 (pp.11–12) preserves treewidth
   under subdivision; Corollary 26 (p.13) gives tw(I(J))=tw(J) for the
   graph obtained by subdividing every edge. Theorem 27 (p.13) records
   minor monotonicity. Read their proofs: remove/add a vertex in bags;
   merge adjacent endpoints in bags; for subdivision distinguish forests
   from width at least two and attach a three-vertex bag in the latter
   case. Only these known treewidth statements are to be imported, not
   reproved. The publisher URL returned HTTP 429; the complete versioned
   author preprint was accessible, so this is not an essential blocker.

2. Dániel Marx, *Can You Beat Treewidth?*, Theory of Computing **6**
   (2010), 85–112, [journal PDF](https://www.theoryofcomputing.org/articles/v006a005/v006a005.pdf),
   §3.1, pp.92–93, Lemma 3.2(b). For any finite graph J of treewidth at
   most t and any W⊆V(J), there is S⊆V(J), |S|≤t+1, such that every
   component C of J−S has |C∩W|≤|W|/2. S may meet W. Read the preceding
   definition and both lemma parts; only (b) is needed. Its citation is
   Reed (1997) and Flum–Grohe §11.2, not a proof printed in this paper.
   No claim of having read those antecedents is made.

3. Julia Böttcher, Klaas P. Pruessmann, Anusch Taraz and Andreas Würfl,
   *Bandwidth, expansion, treewidth, separators, and universality for
   bounded degree graphs*, [arXiv:0910.3014v1](https://arxiv.org/pdf/0910.3014v1),
   16 October 2009, pp.2–3, Definitions 1–3, Theorem 4 and footnote 1.
   Their external-neighborhood ε-expander convention matches L030/L031.
   Separations partition vertices into A,B,S; no A–B edge is allowed.
   Their main separation-number statement uses 2/3 balance for every
   subgraph; the footnote records the underlying 1/2 version. Theorem 6
   is an upper bound from boundedness, not a direct lower-bound theorem
   for the notebook gadget, and is not to be reversed. The inspected
   preprint contains a later internal date; citations here bind to its
   arXiv version and numbering, not inferred journal pagination.

4. Zdeněk Dvořák and Sergey Norin, *Treewidth of graphs with balanced
   separations*, [arXiv:1408.3869v2](https://arxiv.org/pdf/1408.3869v2),
   20 December 2018, introduction pp.1–2 and Theorem 1. Theorem 1 is
   tw(J)≤15 sn(J), where sn tests every subgraph. This opposite-direction
   theorem is not needed for a lower bound. Its introduction also records
   the weighted separator implication from small treewidth with 2/3
   balance. Do not confuse that normalization with Marx's componentwise
   half-balance. No remaining sections of this paper are claimed inspected.

Bodlaender's *A tourist guide through treewidth* (1993) was consulted only
at the minor-theory/algorithm passages returned by targeted retrieval; it
is not an essential theorem input. Robertson–Seymour's original *Graph
Minors II* was located bibliographically but not read. Its results are
not given an invented theorem number. No primary source inspected states
the complete signed-ER-family threshold. Exact graph identification and
the expansion/counting specialization still require a mathematical step.

## Search record and approved difference

Discovery queries included `treewidth balanced separator k+1 vertices
expander treewidth primary paper`; `treewidth vertex deletion inequality
tw G minus S treewidth S separator expanders`; `treewidth expander
subdivision deletion`; `treewidth vertex deletion k+1 expansion`;
`Bodlaender tourist guide treewidth lemma 1 minor separator pdf`;
`expanders treewidth epsilon separator pdf`; and `treewidth expander
3+epsilon`. Source follow-ups searched the exact titles *On Balanced
Separators, Treewidth, and Cycle Rank*, *Graph minors. II. Algorithmic
aspects of tree-width*, *Bandwidth, expansion, treewidth* (with authors),
and *The Behavior of Tree-Width and Path-Width* (with arXiv), plus
`tw(G-v) tw(G) lower bounds vertex addition treewidth`. Search hits on
deletion approximation, cycle rank and other models were leads, not
imported theorems. No failure to find an exact match establishes novelty.

Approve a REPRODUCTION attempt on exactly TARGET. First verify the
candidate incidence-subgraph identification using L031's actual p_i
adjacencies inside the unchanged full signed graph, paying attention to
shared originals and both σ choices. Then apply the cited graph-operation
and balanced-separator inputs, using the given external expansion to seek
an explicit bound on deletions. The multi-vertex deletion specialization,
finite-size component-union count, constants, and comparison with
floor(log₂(T+2)) are tasks for that separate turn; none is proved here.
No generic treewidth algorithm, expander generator or simulation reproof
is needed. A short applicability/counting argument is necessary because
the cited statements do not mention these ER gates or their binary T.

Continue if the graph identification and an explicit separator estimate
give a test at the logarithmic threshold. A bound c_ε n−O(1) with
c_ε>0 is a useful sought threshold, not an established result. An eventual
superlogarithmic lower bound stops L073 on this supplied family only.
A valid deletion construction within the threshold instead demonstrates
coverage. If neither follows, retain the exact failed applicability or
counting obligation rather than substituting OBDD hardness. Independent
gaps remain: arbitrary ER data, formula-only bounds, W/V/U and SAT transfer.
Mathlib coverage of this full specialization and the supporting theorem
names is not checked; no absence claim is made.

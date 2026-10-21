# Treewidth-two extension data — source comparison

TARGET: Test whether treewidth at most two of the full signed extension-value DAG suffices for polynomial-full-bit L037 data from a supplied ER refutation.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact bounded-treewidth circuit/OBDD, all-output and noncommutative-witness queries below located known single-output compilation and a completeness correction; local treewidth/pathwidth search found only this proposal and history/270, with no completed local structural theorem.
SOURCE_EVIDENCE: Read Jha–Suciu ICDT 2012 Definitions 2.2–2.4, Lemma 2.12 and its section 4 proof, Corollary 2.14 and its proof/order construction (PDF pp.4,6–7,9); Amarilli–Bourhis–Senellart arXiv:1604.02761v1 Definition 6.4/Lemma 6.6 and complete Appendix A proof (PDF pp.15–16,28–29); de Colnet–Ordyniak–Szeider AI 351 (2026) Proposition 2, section 3.1 and Lemmas 4–5 (PDF pp.3–5). Reused previously inspected Raz–Shpilka graph composition coverage.
COMPARISON: Known compilation gives polynomial-size Boolean OBDDs for a fixed bounded-treewidth circuit output. L026 supplies formal relations as shared circuits from a common-order all-root family; L037 requires affine ABPs. Unrelated per-root orders or treating L026 circuits as ABPs do not fill the complete interface.
GAP: Justify a common polynomial-width complete OBDD family for all required roots on the full graph, then realize L026's particular representative/K/W recurrences by explicit affine ABPs with one aggregate polynomial full-bit bound; neither difference is proved by this review.
REASON: Primary component hypotheses and essential compilation cases are accessible and compared; the remaining differences are concrete applicability and representation tests, rather than missing essential source coverage. Authorize one bounded specialization attempt, without asserting sufficiency or novelty.
SCOPE: Width-at-most-three F and supplied signed-AND ER as in L025/L037; treewidth at most two of the underlying undirected full signed value DAG, including shared original-variable vertices, constants, all extension nodes and required exact complement nodes, with repeated edges treated as one undirected adjacency. Charge all roots and original names in T.

## Relevance and scope

The main gap remains unrestricted SAT decision/separation. This intermediate
target tests a restricted sufficient condition for the missing complete
L037 data. If successful, it could feed L037's conditional certificate
assembly. Arbitrary ER representation, formula-only bounds, ER boundedness,
W/V/U and unrestricted SAT transfer remain independent gaps. There is no
main-problem candidate and no cross-notebook input.

The original 2026-10-16 REVIEW_REQUIRED proposal is preserved as the unchanged
TARGET and SCOPE. Its missing-coverage diagnosis described the state before
this review, not a negative mathematical result. Readiness changes here;
the mathematical argument in PROOF.md and DAG.md does not.

Reconfirmed the [Clay primary problem page](https://www.claymath.org/millennium/p-vs-np/)
on 2026-10-17: ordinary P versus NP remains its stated unsolved problem.
Reuse foundations/01-model-and-target.md's precise Cook official-description
section 1 definitions; no prize-adjudication premise enters the target.

## Search and inspected primary results

Queries actually issued were:
- `bounded treewidth Boolean circuits OBDD polynomial size common variable order theorem`;
- `Jha Suciu circuits treewidth OBDD bounded treewidth 2012`;
- `"OBDDs, SDDs, and circuits of bounded width" pdf`;
- `"bounded treewidth" "noncommutative" "IPS"`;
- `"bounded treewidth" circuits "OBDD" "outputs"`;
- `"OBDD" "commutator" witness algebraic`.

Search hits are discovery only, not proofs or novelty certification.

**Jha–Suciu.** Abhay Jha and Dan Suciu, *On the Tractability of Query
Compilation and Bounded Treewidth*, ICDT 2012, DOI
[10.1145/2274576.2274603](https://doi.org/10.1145/2274576.2274603),
[author PDF](https://homes.cs.washington.edu/~suciu/file38_paper.pdf),
Definitions 2.2–2.4, Lemma 2.12, Corollary 2.14, section 4.
An expression DAG uses AND/OR/NOT and one shared input vertex per variable.
Corollary 2.14 gives width at most n^(2^((k+1)2^(k+1))) for an expression
tree decomposition of width < k, in its decomposition-induced order.
The order uses first-encounter variables and a largest-child-first in-order
traversal. Read the separator residual-function argument and all three
traversal cases: largest child, current bag, later child with halved
variable count. These are Boolean representation results, with no formal
axiom witnesses. The single-output statement does not explicitly provide
the present all-root/common-order interface. Respect its strict width
convention. The EPWD label following Corollary 2.14 is a typographical
label, not a pathwidth hypothesis replacing its tree-decomposition statement.

**Amarilli–Bourhis–Senellart.** Antoine Amarilli, Pierre Bourhis and Pierre
Senellart, *Tractable Lineages on Treelike Instances: Limits and Extensions*,
[arXiv:1604.02761v1, 10 April 2016](https://arxiv.org/abs/1604.02761v1),
[inspected author long-version PDF](https://pierre.senellart.com/publications/amarilli2016tractable_long.pdf),
Lemma 6.6, PDF p.16 and Appendix A pp.28–29. For every fixed circuit
treewidth k, an equivalent OBDD can be computed in time O(|C|^c), for
c depending on k. The proof builds the decomposition order and merges
equivalent prefix valuations level by level. Equivalence is tested with
two restricted copies sharing remaining inputs, an output-disagreement
gadget and a width-at-most-2k+5 decomposition obtained from corresponding
bags. Bounded-treewidth satisfiability then decides equivalence. All these
cases were read. Appendix A's initial constant-width shorthand omits the
input-size exponent: its subsequent pair count |C|^f(k) and the cited
Jha–Suciu result explicitly use polynomial width. Do not import constant
width from that sentence. This is an algorithmic Boolean compilation
input, not an arithmetic-ABP or free-ring witness theorem.

**Completeness correction.** Alexis de Colnet, Sebastian Ordyniak and
Stefan Szeider, *OBDDs, SDDs, and circuits of bounded width: Completeness
matters*, Artificial Intelligence 351 (2026), 104458, DOI
[10.1016/j.artint.2025.104458](https://doi.org/10.1016/j.artint.2025.104458),
[published repository PDF](https://eprints.whiterose.ac.uk/id/eprint/234745/9/1-s2.0-S0004370225001778-main.pdf),
Proposition 2 and section 3.1/Lemmas 4–5, PDF pp.3–5.
Proposition 2 gives same-order completion in O(n|B|) time with width at
most n times the old width. Section 3.1 identifies a defect in the
OBDD-to-bounded-pathwidth direction for incomplete OBDDs; the corrected
converse requires completeness. The forward pathwidth-to-complete-OBDD
statement is retained in Lemma 5. This rules out silently identifying the
width conventions. It is not an obstruction to polynomial-size complete
OBDDs from fixed bounded treewidth. The later SDD lower-bound proof is not
needed or imported.

The obsolete repository `/1/main.pdf` URL and one publisher fetch failed;
the current published `/9/1-s2.0-S0004370225001778-main.pdf` worked. All
essential passages above were accessible. No persistent source blocker
remains. Later structured d-DNNF/TDD papers surfaced as unread leads; their
stronger representation claims are not used or essential to this test.

## Local duplicates, failures and representation difference

Read L025's complete receiving hypotheses, L037's hypotheses and graph
operations, L070's supplied-C hypothesis, and the complete L026 construction.
The local treewidth/pathwidth search in assessments, foundations, attempts
and history found only this proposal and history/270. That bounded search
does not certify originality. Existing unfinished work is preserved.

L026 already proves the ordered-multilinear output identification and both
formal local identities from supplied common-order diagrams, with
d=max(1,n), h=max(1,2n-1) and an explicit aggregate circuit ledger. Reuse
those identities rather than reprove Boolean product/equivalence or claim
semantic agreement implies arbitrary free-ring equality. Its K recurrence
(6), paired-state W recurrence (8), and separate-root accounting are the
precise material relevant to an ABP realization. Its conclusion is a
circuit bound; arithmetic gates are not extra extension vertices.

Reuse the ready assessments `2026-10-05-obdd-reduced-data.md`,
`2026-10-07-alternative-abp-commutator-witnesses.md` and
`2026-10-07-alternative-affine-abp-certificate-assembly.md` in this
directory. In particular, Raz–Shpilka, *Deterministic Polynomial Identity
Testing in Non Commutative Models*, [author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Definition 1/Lemma 2 Step 1, PDF pp.4–5, covers serial/parallel graph
composition with separately supplied operands. No fresh primary reread or
general circuit-to-ABP theorem is needed or asserted.

Read Attempt 019 and L027's hypotheses/conclusion: every-order HWB width
stops the unrestricted supplied-proof promise, without a treewidth-two
promise. Read Attempts 020/021: degree control and supplied ABPs do not
give a blanket same-output conversion or a small prescribed pair table.
Their evidence remains valid. They do not establish a lower bound for
L026's particular suffix recurrences. L070 requires C before supplying its
zero-extension data, so cannot supply existence here. Serializer stops
025–027 concern another target and are not reopened.

## Approved bounded specialization test

Retain exactly TARGET. Essential local inputs are L025, L026 and L037;
L070 and the stops are comparisons, not missing-existence premises. The
primary compilation statements and reused graph-composition coverage
support this proposed test, with no construction proved here:

1. Test a single decomposition-induced order for all required signed values,
   retaining the full graph and original shared input vertices. Justify
   applying the single-output residual bound when the designated output
   changes, or supply a bounded-width output-marking reduction. Unrelated
   per-root orders are insufficient. Handle constants, unused roots,
   repeated operands, disconnected parts, n=0 and variables absent from
   individual output cones. Do not change traversal weights per output
   without a common-order proof.
2. Once common-order diagrams are justified, use L026's existing formal
   identities and test an explicit ABP realization of its particular value,
   earlier-variable/suffix K and paired-state W networks. The candidate
   mechanism is one-sided acyclic recurrence propagation with independently
   copied local suffix/multiplier blocks using the inspected serial/parallel
   operations. This is a proposed mechanism, not a demonstrated conversion
   or an appeal to closure of arbitrary circuits under conversion.
3. Charge decomposition/compilation, completion, every required graph,
   copied correction block, original dictionary/axiom position, exact signed
   wrapper and separately written root in one fixed polynomial in T. Bound
   pre-substitution degrees and deterministic bit time. Supply exactly
   H_i(x,0)=0 and H_i(x,A)=r_i+r_a r_b in the free F₂ algebra.

Continue if this gives complete polynomial-full-bit L037 data, or a rigorous
intermediate interface removing one named gap while leaving the other
explicit. Narrow or abandon the sufficiency mechanism if common-order
control needs growing treewidth, or witness graphs require recursive path
unfolding, unbounded history states, circuit-valued edges, or only Boolean/
commutative rather than formal equality. One small final-output OBDD does
not pass. No new lemma, specialization proof, mathematical script or
numerical test was performed this turn.

Mathlib matching coverage: **not checked**, with no absence claim. The
review establishes supporting source coverage and a concrete mathematical
test, not treewidth-two sufficiency or progress beyond the checked sources.

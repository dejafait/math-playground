# Logarithmically many common variable blocks — completed comparison

TARGET: Construct an original-M polynomial Boolean/commutator affine-ABP witness for a Boolean-zero product of two supplied dense width-three OBDDs whose distinct orders permute at most floor(log₂ M) supplied nonempty common contiguous blocks while preserving every internal block order.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 356 searched block-permuted OBDD conjunctions/reordering, noncommutative witnesses and stronger different-order ROABP results; compared the ready two-block, near-order, single-move, small-deletion and graph-commutator assessments plus Attempts 018/030. Exact queries, inspected primary passages and unread leads are recorded below; no full-target match or novelty certification was obtained.
SOURCE_EVIDENCE: Reuse step 352's inspected Bryant §4.3, LTW Lemmas 3.6–3.7 and Raz–Shpilka Lemma 2 Step 1 coverage; read GKST's author-hosted CCC'15 manuscript §2.1 and §3 Theorems 3.1–3.2 pp.4,9–12 with dependency-verification cases, and Gurjar–Korwar–Saxena ToC 13(2) (2017) §§2.1–2.2, Lemma 3.5/Theorem 3.6 and Theorem 4.9 pp.4–5,9–10,15. Direct URLs and receiving qualifications follow.
COMPARISON: L091 covers two blocks with constant multiplicities; L026/L071 and L035 provide the unchanged common-order and original-only commutator graph interfaces. Inspected ROABP results provide commutative identity tests or hitting sets, not original-fg Boolean/commutator witnesses; every-order small-width representation is an extra hypothesis. No inspected theorem supplies the growing-block aggregate bound.
GAP: Test an exact block-boundary expansion and additive original-only factor corrections with a uniform full-bit/time/path-degree ledger in original M; all dependence on the growing block count must be controlled without iterating a fixed polynomial with an input-dependent exponent. No such construction or bound is established here.
REASON: Essential component coverage and the new target-specific comparison support one bounded proof attempt on unchanged TARGET. The block-count and copying estimates are explicit research obligations, not assumed results; no essential unread source is used. This literature-only turn approves scope, not mathematics.
SCOPE: Two explicit dense deterministic width-at-most-three OBDDs, same complete named alphabet, distinct orders permuting b supplied common nonempty contiguous blocks with identical internal orders, 2≤b≤floor(log₂ M), unbounded block lengths, Boolean-zero original fg promise, free F₂ identities, original B/dictionaries and pre-witness M of L087; explicit acyclic affine-edge witnesses only.

## Preserved proposal

The following proposal and working checkpoint describe the startup state.
Their REVIEW_REQUIRED and unfinished-review descriptions are superseded
by the completed comparison below, without establishing any mathematics.

This is a proposed research target, not a theorem, ready assessment or
newly derived construction. Use the exact original alphabet, B and
pre-witness M of L087. Each supplied block occurs once in each order,
contiguously and with the same internal variable order; the two block
permutations differ. Both diagrams are explicit dense deterministic
width-at-most-three inputs, including redundant/unreachable states and
scalar terminals. The number of nonempty blocks is between two and
floor(log₂ M); block lengths have no further bound. The Boolean-zero
product is a promise, not a supplied decision procedure.

The sought output retains the original ordered fg, has H(y,0)=0 and
H(y,B(y))=fg, and has one fixed full-bit polynomial in original M,
with polynomial bit construction time and pre-substitution path degree.
No such conclusion is established here. A possible line to assess is
cutting at the common block boundaries and charging exact factor
corrections; no identity or favorable count is inferred by iterating
L091. A bound exponential in a block length, or a polynomial whose
exponent grows with the block count, would not meet this target.

Essential possible inputs are L091's audited two-block case, L026's
ordered product identities and injectivity, L035's original-only
commutator witness, L071's post-compilation graphs only, and L087's B/M.
Do not use L071's whole compiler without its treewidth hypothesis.
Check stronger known results and local L088–L090 restrictions as well
as Attempts 018/030; prior stops neither prove nor refute this target.
Read primary hypotheses and essential cases before approving the scope.
No cross-notebook input is proposed. Mathlib coverage is not checked.

Its plausible use is a restricted W₂ witness supplier allowing a growing
number of order discontinuities. Arbitrary-order W₂, availability of
general ER data, bounds solely in CNF length and SAT transfer remain
unresolved even on success. Continue only if a source comparison makes
an exact uniform-polynomial test ready; otherwise record the specific
overlap, missing source or obstruction and choose a materially different
test. Approval and any mathematical attempt must occur in separate turns.

## Step 356 — source-review working checkpoint

The unchanged target is under literature-only review. The full L091
construction/audit and L087's B/M conventions have been read; existing
two-block, small-deletion and graph-commutator assessments are available
for reuse. Attempts 018/030 are preserved. No growing-block identity or
copy bound has been derived. Discovery located the primary GKST sum-of-
ROABPs PIT paper; its exact hypotheses and relevant proof scope still need
inspection before comparison. This working checkpoint is not approval.

## Completed source comparison — step 356, 2026-10-19

### Gap, relevance and scope

The main gap remains a deterministic polynomial-time SAT algorithm or a
proof excluding every such algorithm. Rechecked Stephen Cook's official
[Clay description, §1 pp.1–2](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf)
on 2026-10-19: the target is ordinary deterministic versus nondeterministic
polynomial-time language recognition. This does not change the audited
local conventions in `foundations/01-model-and-target.md`.

The intermediate target is exactly TARGET above. Its plausible downstream
use is a restricted W₂ witness supplier with an input-dependent number of
order discontinuities. It neither supplies arbitrary-order W₂ nor removes
the independent general-ER-data and SAT-transfer gaps. M remains L087's
original input length, excluding H and degree parameters. The supplied
block partition is part of the promise; this review asserts no finder for
such partitions and no semantic test of the Boolean-zero promise.

### Discovery, primary reading and reuse

Actual queries included `OBDD block permutation variable order bounded
width conjunction satisfiability blocks`, `noncommutative IPS OBDD
commutator block variable order algebraic branching program`, `"OBDD"
"block" "permutation" conjunction`, `"read once" "algebraic branching"
"different orders" sum`, `"Characterizing Propositional Proofs" "3.7"`,
`Gurjar Korwar Saxena Thierauf identity testing sum read once oblivious
ABPs 2015 2017 pdf`, `OBDD block sifting quantitative statements width
permuting blocks bounded width`, `"noncommutative" "OBDD" "witness"
block`, and `"OBDD" "block permutation"`. Searches located leads; their
snippets do not establish theorem applicability or originality.

1. Gurjar–Korwar–Saxena–Thierauf, *Deterministic Identity Testing for Sum
   of Read-Once Oblivious Arithmetic Branching Programs*,
   [author-hosted 24-page CCC'15 manuscript](https://www.cse.iitb.ac.in/~rgurjar/papers/sumROABP.pdf),
   accessed 2026-10-19, §2.1 p.4 and §3 pp.9–12. Read Theorems 3.1–3.2,
   the dependency construction, verification, final scalar comparison and
   recursive sum case. Over a field F, a sum of c n-variate width-w
   ROABPs of individual degree d has whitebox PIT time
   w^{O(2^c)}(nd)^{O(c)}. Orders may differ. The proof verifies coefficient
   dependencies by common-order linear combinations and single-ROABP
   zero tests. This is commutative polynomial identity testing for sums,
   not Boolean-zero product testing or construction of a free-placeholder
   ideal witness. No extraction theorem or conversion of the present fg
   to that input class is supplied. This is a comparison, not a theorem
   imported as a solution of TARGET; its field-operation complexity also
   does not supply the requested complete bit ledger.

2. Gurjar–Korwar–Saxena, *Identity Testing for Constant-Width, and Any-Order,
   Read-Once Oblivious Arithmetic Branching Programs*, Theory of Computing
   13(2) (2017), 1–21, DOI 10.4086/toc.2017.v013a002,
   [published primary PDF](https://www.theoryofcomputing.org/articles/v013a002/v013a002.pdf).
   Read §§2.1–2.2 pp.4–5, Lemma 3.5/Theorem 3.6 pp.9–10 with their
   recursive-map/field-size conditions, the characteristic-two failure
   example p.9, and Theorem 4.9 p.15. Theorem 3.6's known-order hitting
   set assumes characteristic zero or at least nd w^{log n}; it does not
   apply over F₂ here. Section 2.2.2 defines the other class by existence
   of a width-w representation in **every** variable order; Theorem 4.9
   gives hitting-set size (ndw)^{O(log log w)} for that class. This is
   stronger representation information than two supplied orders, and
   supplies no formal Boolean/commutator witness. No specialization or
   proof of its hypotheses is claimed. The remaining concentration proof
   is not needed or imported for this hypothesis mismatch.

Reuse the adequate completed comparison
`drafts/literature/2026-10-19-two-block-order-pair-witness.md` rather than
repeat its source retrieval. Its inspected primary inputs are Bryant,
*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE TC
35(8) (1986), §4.3 author-restored pp.12–14
([PDF](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf)); Li–Tzameret–Wang,
*Characterizing Propositional Proofs as Non-Commutative Formulas*,
arXiv:1412.8746v4 (11 September 2015), Lemmas 3.6–3.7 pp.17–18
([PDF](https://arxiv.org/pdf/1412.8746v4)); and Raz–Shpilka,
*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author manuscript, Lemma 2 Step 1 pp.5–6
([PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)).
The ready graph-commutator assessment
`drafts/literature/2026-10-07-alternative-abp-commutator-witnesses.md`
retains all essential base/addition/ordered-product and context cases.
Bryant supplies common-order Boolean Apply, LTW a formula-input
commutator witness with size at most |P|²|Q|², and Raz–Shpilka independent
serial/parallel graph composition. F₂ is compatible with LTW, with minus
equal to plus. No path unfolding is licensed by the formula bound.
These unchanged component statements require no new reproof.

The unread Meinel–Slobodová block-sifting paper, Meinel–Theobald
quantitative book passages and Bollig–Löbbing–Wegener local-change paper
retain the access/scope qualifications in the two-block assessment.
Their statements are not assumed absent, weaker or impossible; none is
an essential input to the independent proof test below. Other search
hits, including bounded-width circuit/OBDD representation comparisons,
were not inspected as theorem inputs. No essential source blocker was
identified. Refresh coverage before relying on an unread lead.

### Local inputs, duplicate checks and preserved failures

Read L091's complete proof and separate step-355 audit, L087's exact
alphabet/B/M hypotheses, L026's ordered injectivity and equations (4)–(12),
and L071's post-compilation value/K/P/W construction and aggregate ledger.
L035's statement/graph factorization and ready literature assessment cover
the original-only commutator interface. Their roles are unchanged:

- L091 is the audited two-block case. Its constant term/copy multiplicities
  do not prove a uniform bound when the number of boundaries grows.
- L035 receives x-only affine ABPs, including constants and zero graphs.
  A recursively constructed placeholder witness cannot be passed to it
  as an original-only factor. Independent graph copies must be paid.
- L026/L071 correct synchronous products within one common order and use
  injectivity only on its increasing multilinear space. Their recurrences
  have no ER or original-clause input; subset-alphabet reception still
  requires renaming into the complete original B dictionary. Use only
  L071's post-compilation component, retaining the treewidth hypothesis
  on its separate whole compilation theorem.

Reused L088/L089/L090 scope comparisons in the near-order, single-move and
small-deletion assessments. A logarithmic number of blocks does not itself
meet their displacement or deletion hypotheses. Long internal blocks are
allowed here; no reduction to those promises is established. A conclusion
for arbitrary distinct orders is not imported from L087's conditional
NP=coNP burden. No full growing-block duplicate was found in these scoped
records, which is not a novelty claim.

Attempts 018/030 were read and preserved. Repeating scope approval alone
is not mathematics; the present changed-target comparison has new source
evidence and leaves a concrete proof test. Attempt 030 stops universal
faithful common-order value availability, whereas these diagrams are
already supplied and the output may be an alternative witness. Its
obstruction remains valid without refuting this target. No cross-notebook
result or sibling proof was read. Mathlib coverage is **not checked**,
not absent; no theorem is added to a canonical lemma in this turn.

### One authorized proof test and stopping criterion

Keep TARGET unchanged for the next invocation after the supervisor's
separate approval. Test cutting both original diagrams at **all** supplied
block boundaries and using original-only factor exchanges plus within-
block synchronous corrections. This is a proposed extension of the
audited component method, not an identity, state-count theorem, favorable
term count or construction proved here. Do not iterate L091's completed
polynomial bound with a growing exponent.

The discriminating resource test is whether an explicit additive assembly
can have full cost at most C^b(M+b+2)^c for absolute C,c, or another
explicit bound proved to be one fixed polynomial in original M at the
given cutoff. This expression is a **sought sufficient threshold**, not
an achieved estimate. Prove the complete intermediate multiplicities,
every independent surrounding-factor copy, local correction, dictionary,
name, root/reference and construction operation. An M^{Theta(b)} or
block-length-exponential estimate does not meet the target. Do not assume
all intermediate reordered diagrams have bounded width.

Continue only with an explicit acyclic affine-edge H satisfying both
H(y,0)=0 and H(y,B)=original fg formally, together with polynomial
construction bit time and pre-substitution path degree in original M.
Any ordered-multilinear residual must first be proved to lie in one
common block-concatenated order; Boolean vanishing alone does not give a
free-ring zero identity. Include arbitrary block permutations, singleton
and long blocks, redundant/unreachable states, repeated successors,
scalar-terminal normalization, constants, zero/no-path factors and every
independent graph occurrence. No semantic promise tester is supplied.

On an explicit ordered-identity failure or an unavoidable excessive cost
for this construction, preserve the evidence and stop or change this
mechanism; neither failure would refute all possible alternative witnesses.
If a new essential theorem/interface is needed, set REVIEW_REQUIRED before
dependent mathematics. Arbitrary-order W₂, general ER data, formula-only
bounds and unrestricted SAT decision/separation remain unresolved even
on success.

Completed step: LITERATURE / literature_comparison / NOVELTY_UNCHECKED,
outcome EXPLORATION. This fresh comparison supplies EXPLORE scope and an
actionable uniform-cost test, without establishing a witness or progress
beyond the checked mathematics. No lemma, mathematical script, DAG edge
or PROOF argument changed. Mathematical exploration usage stays one
since step 353; this literature review neither spends nor resets it.

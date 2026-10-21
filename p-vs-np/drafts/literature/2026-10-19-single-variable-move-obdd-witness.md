# Single variable move: source comparison

TARGET: Assess source coverage for polynomial-full-bit Boolean/commutator affine-ABP witnesses of Boolean-zero products of two dense width-three OBDDs whose orders differ by moving one variable an arbitrary distance, retaining the original fg and pre-witness M.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 343 searched single-variable OBDD movement, sifting size bounds, local-order changes and noncommutative/commutator reordering certificates; inspected primary Bryant cofactor/Apply/reduction cases and Rudell swap/sifting passages, and reused the recorded formal-correction comparison. Exact queries and access limits appear below.
SOURCE_EVIDENCE: Bryant, Graph-Based Algorithms for Boolean Function Manipulation, IEEE TC 35(8), 677–691 (1986), author-restored https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf §§1.1,4.2–4.5 pp.3,10–16, Table 1 correction p.9 and p.14 correction; Rudell, ICCAD 1993 pp.42–47, §§4.1,4.3 pp.44–45 at the primary scan below; reused Tzameret arXiv:1004.2159v2 Definition 3.1, Lemma 3.4/Claim 3.5 pp.7,9–10 and the inspected LTW/FSTW comparison.
COMPARISON: Known sources supply Boolean cofactoring, memoized combination, structural node sharing and local swapping; local L088 supplies exact swap correction. No inspected theorem supplies the full arbitrary-distance single-move affine-ABP witness statement. Sifting's stopping cutoff and formula-size commutation do not prove that statement. This is source coverage for a specialization test, not an established extension or certified novelty.
GAP: Prove a fixed-polynomial aggregate state/copying bound for one arbitrary-distance move, justify each chosen sharing/reduction step for the ordered free-ring representatives, and combine exact corrections with the common-order product interface while retaining original fg and pre-witness M.
REASON: Essential component coverage suffices for one independently testable state-sharing/correction attempt; its new applicability and accounting obligations remain unproved. The separate ready-continuation assessment names that mathematical target and requires supervisor approval before research.

## Original proposal — historical source gate

The following proposal is preserved. Its REVIEW_REQUIRED and missing-coverage
language describes the initial gate; the completed comparison below supersedes
that gate without establishing the proposed witness theorem.

This file proposes a target; it derives and approves no mathematical
result. The exact next action is the source assessment in TARGET.

Keep L087/L088's two explicit dense deterministic input OBDDs of
nonterminal width at most three, on the same named alphabet over F₂.
Obtain π from ρ by deleting one named variable and reinserting it at
any position, preserving the relative order of all other variables.
Allow either direction and zero displacement; impose no logarithmic
displacement bound. Retain the separately ordered representatives f,g,
their original product fg, the Boolean-zero promise, the full original
Boolean/commutator tuple B and original pre-witness M. The contemplated
output remains an explicit acyclic affine ABP H with H(y,0)=0 and
H(y,B)=fg, bounded by one fixed polynomial in M. No width promise for
an intermediate representation or semantic-promise tester is supplied.

The main gap is still unrestricted SAT decision/separation. A successful
restricted witness construction could extend the common-order product
interface to some order pairs outside L088's proven distance bound.
It would supply neither diagrams for arbitrary ER nor arbitrary-order
W₂, and would not supersede Attempt 030's availability obstruction.

Essential prospective local inputs are L088's audited correction and
original-product composition, L026's exact common-order identities and
injectivity, L071's post-compilation graph component only, and L087's
encoding conventions. Their availability does not prove the missing
single-move representation or correction bound. The previous nearby-order
assessment retains the primary sources, access qualifications and unread
Bollig–Löbbing–Wegener quantitative lead; that lead is not an input.

The review should search exact and stronger single-variable reordering
results, inspect their primary hypotheses and relevant proof cases,
and distinguish Boolean representation bounds from exact noncommutative
correction bounds. Reuse source coverage where it actually applies.
Continue to mathematics only if the essential coverage supports a
concrete construction/test with one polynomial in original M; otherwise
record the precise uncovered obligation or obstruction and choose an
independently testable target. No path-unfolding bound, arbitrary-order
supplier or witness existence is assumed. Mathlib coverage of this
changed target is not checked. This is not a ready continuation.

## Completed comparison — step 343, 2026-10-19

**Relevance and exact scope.** The main gap is unrestricted SAT decision
or separation, including the absence of a general ER data supplier.
The intermediate target remains exactly the proposed single move, in
either direction and including zero displacement, for the original two
dense width-at-most-three diagrams. A successful witness construction
would extend a restricted formal-correction interface beyond L088's
logarithmic adjacent-distance promise. It would supply neither diagrams
for arbitrary ER nor arbitrary-order W₂. No smaller intermediate width,
semantic tester, treewidth premise or certificate finder is assumed.

**Search performed.** Queries included `OBDD moving single variable
arbitrary position size polynomial bound sifting Bollig Löbbing Wegener
local changes`, `"OBDD" "single variable" "size" reordering`,
`"noncommutative" "OBDD" commutator witnesses`, `"On the effect of local
changes" ordering pdf`, `OBDD sifting "quadratic" "variable"`,
`OBDD "moving" "one variable" size bound`, `"OBDD" "single variable"
"polynomial"`, `"OBDD" "commutator" "reordering"`, `"On the effect of
local changes" "quadratic"`, and `"OBDD" "shift" "size" "variable"
Bollig Löbbing Wegener`. Some returned unrelated material. No search
snippet is theorem evidence and no failed search establishes novelty.
The explicit cofactor/reduction/Apply algorithms were inspected instead
of treating practical sifting descriptions as a quantitative theorem.

**Primary Boolean operations.** Randal E. Bryant,
[*Graph-Based Algorithms for Boolean Function Manipulation*](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
IEEE Transactions on Computers 35(8), 677–691 (1986), author-restored
28-page copy retrieved 2026-10-19: §1.1 p.3 fixes a common order and
states Shannon expansion. Section 4.4 p.15 redirects every reference to
the selected cofactor, including a root reference; reduction follows.
Section 4.3 pp.12–14/Figure 6 treats terminal pairs, equal indices,
unequal indices and repeated pair calls. Its memo table bounds distinct
pair states by the product of input graph sizes. Section 4.2 pp.10–11/
Figure 4 handles equal children and equal child-ID pairs. Table 1's
update p.9 corrects reduction-time factors; p.14 rejects the proposed
input-plus-output linear bound. We use conservative polynomial costs.
Section 4.5 p.16 states the ternary ITE/cofactor formulation and restricts
when direct syntactic replacement respects ordering. These are Boolean
operations; they do not certify our original ordered noncommutative
polynomial or its affine-ABP correction. Their applicability to the
single-move layout, density and witness ledger still needs proof.

**Primary reordering and its qualification.** Richard Rudell,
[*Dynamic Variable Ordering for Ordered Binary Decision Diagrams*](https://www.larshj.dk/PUMA/references/Dynamic%20variable%20ordering%20for%20ordered%20binary%20decision%20diagrams%20-%20p42-rudell.pdf),
ICCAD 1993, 42–47, §4.1 p.44: rechecked the four-cofactor swap,
missing-test case, degenerate/existing children and retained references.
Section 4.3 p.45 describes moving one variable through the order with
the others fixed. Its twice-original-size cutoff terminates a search
direction; it is not a bound for reaching every prescribed position.
The swap count alone cannot certify total graph size. No optimal-order
claim or unrestricted intermediate-size bound is imported.

Bollig–Löbbing–Wegener, *On the effect of local changes in the variable
ordering of ordered decision diagrams*, IPL 59(5), 233–239 (1996),
[DOI](https://doi.org/10.1016/0020-0190(96)00119-6), remains an unread
quantitative lead: the publisher preview exposes the abstract, not the
needed theorem/proof. It is not an input or an essential blocker for
the component-based test below. No sharper bound is attributed to it.

**Exact correction coverage reused.** Tzameret,
[*Algebraic Proofs over Noncommutative Formulas*](https://arxiv.org/pdf/1004.2159v2),
v2 (1 August 2010), Definition 3.1 p.7 and Lemma 3.4/Claim 3.5 pp.9–10,
was already inspected in the nearby-order assessment. Its polynomial
formula-size commutation proof and single-occurrence context rule do
not bound an unfolded shared diagram. Reuse that assessment's LTW
Lemmas 3.6–3.7 and FSTW Propositions 4.5–4.6 comparison, with the same
formula-size and commutative-model qualifications. No general commutation
theorem needs reproof. The missing specialization is its graph-size
reception, not the validity of those source results.

**Local duplicates and failures.** Reviewed histories 338–340 and
Attempt 030; read L088's construction through its original-product
composition, L026 (4)–(12), L071's post-compilation W/value component
and corresponding audit passage, and L087's hypotheses and M/B
conventions. L088's audited local swap correction and additive
telescoping are available, but its aggregate size proof assumes
logarithmically many swaps. Merely iterating its factor-three estimate
across the whole alphabet supplies no required polynomial bound.
This is a limitation of that estimate, not a lower bound for the new
target. L026's injectivity is confined to a common increasing-multilinear
subspace. L071's whole treewidth theorem is not invoked. Attempt 030
stops universal common-order faithful-value availability, independently
of this supplied-pair witness test. None of these records is a completed
duplicate of the arbitrary-distance single-move statement.

**One approved specialization test, still unproved.** Use cofactor or
structurally identified states to try to control a single-variable
adjacent-swap sequence. Seek an aggregate bound of the form
sum_t size(E_t) <= K(M+2)^c for absolute K,c, including all retained
states, or an equally explicit direct correction graph with that
full-bit threshold. This is a sought bound, not a result of this review.
Any sharing or reduction between swaps must preserve the exact ordered
representative, or have its own paid correction; Boolean equivalence
alone does not suffice. The planned attempt must explain why its
state descriptors stay in a fixed-polynomial universe rather than
assuming that a small final Boolean graph controls the intermediate
graphs. It must handle either movement direction, unreachable states,
repeated successors, unused originals, constants and endpoint cases.

Then reuse L088's exact correction/original-product interface and the
existing common-order product component. Require both H(y,0)=0 and
H(y,B)=fg formally for the original separately ordered f,g, with one
polynomial in pre-witness M paying all independent graphs, full original
dictionaries, names, edges and references. No path unfolding or recursive
polynomial exponentiation is licensed. Any use of a cofactor/Apply graph
in that interface needs an explicit applicability argument; a citation
to its Boolean function alone cannot fill the free-ring obligation.

Continue if that one mechanism yields the exact identities and fixed
full-bit polynomial. Abandon or narrow this mechanism on an explicit
sharing/identity failure or evidence that its proposed state/copying
ledger is superpolynomial; a failed loose estimate is not nonexistence
of alternative witnesses. The arbitrary-order, representation-availability
and SAT gaps remain separate. No new identity, lemma, intermediate-width
bound, mathematical script or theorem is derived here. Full matching
Mathlib coverage is not checked; no absence claim is made.

**Decision and continuation.** SPECIALIZE approves component coverage
for one bounded mathematical attempt with these unresolved obligations.
The exact research action and unchanged input scope are saved separately
in `drafts/literature/2026-10-19-single-variable-move-obdd-construction.md`.
That newly written ready assessment receives separate supervisor
approval next turn. This completed literature review is EXPLORATION /
NOVELTY_UNCHECKED, not a mathematical advance or a theorem import.
Mathematical EXPLORATION usage remains zero. PROOF.md, DAG.md, lemmas/
and mathematical scripts are unchanged by this step.

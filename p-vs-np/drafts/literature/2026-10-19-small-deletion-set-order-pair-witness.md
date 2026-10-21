# Small deletion set in two supplied orders: completed source comparison

TARGET: Test whether Boolean-zero products of two dense width-three OBDDs whose orders agree after deleting a supplied set of at most floor(log₂ M) variables admit polynomial-full-bit Boolean/commutator affine-ABP witnesses retaining the original fg and pre-witness M.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 348 searched OBDD order-deletion/reordering, backdoors/conditioning, longest common subsequences and noncommutative OBDD/Shannon witnesses; compared L026/L035/L071/L072/L087–L089 and Attempt 030. No inspected full target match; queries and boundaries below, without a novelty claim.
SOURCE_EVIDENCE: Bryant IEEE TC 35(8), 677–691 (1986), annotated author copy §§1.1,4.4 pp.3,15; Rudell ICCAD 1993, 42–47, §4.1 p.44; Li–Tzameret–Wang arXiv:1412.8746v4 Lemmas 3.6–3.7 pp.17–18; Tzameret arXiv:1004.2159v2 Definition 3.1/Lemma 3.4/Claim 3.5 pp.6,9–10; Bova–Slivovsky DOI 10.1007/s00224-016-9715-z §3.4 Lemma 12/Theorems 13–14 PDF pp.11–13. Direct primary PDFs inspected; reuse ready L035/L072 assessments for graph composition and unchanged component coverage.
COMPARISON: Boolean restriction and formula commutator corrections are known; L072 supplies paid indicator orthogonality/recombination for changed interpolants, and L026/L071 supply common-order branch-product corrections. None alone recovers unchanged free polynomials f,g. L088/L089 have narrower displacement hypotheses; CNF deletion distance has different inputs and supplies no free-ring witness.
GAP: Test explicit original-OBDD-to-ordered-cofactor-interpolant corrections, then reception by existing branch-product/recombination components, with both formal identities and one fixed full-bit polynomial in original M and 2^|D|. The lifts, aggregate bound and exact original-product assembly remain unproved.
REASON: Essential restriction, commutation, branch-product and graph-composition coverage is ready. The missing original-polynomial lift is the mathematical specialization to test, not an assumed theorem or essential unread source. Approve one bounded attempt on unchanged TARGET; derive nothing in this literature-only step.
SCOPE: Original two explicit dense deterministic width-at-most-three diagrams, same named alphabet, free F₂ ordered representatives f,g, Boolean-zero fg promise, supplied deletion set of size at most floor(log₂ M), remaining orders identical, original complete B and pre-witness M from L087; explicit acyclic affine-edge witnesses only.

## Preserved startup proposal

The following proposal is retained as provenance. Its future-review and
missing-coverage statements describe invocation start; the completed review
below supersedes them without establishing the proposed mathematics.

The main gap remains unrestricted SAT decision/separation. The proposed
intermediate target could extend the verified restricted order-pair
interface toward larger explicitly supplied classes. Arbitrary-order W₂,
general ER data availability and SAT transfer would remain unresolved
even if this target succeeds. Attempt 030 remains an independent stop
on a different universal representation premise.

Essential already established inputs available for comparison are L089's
single-variable audit, L088's single-swap graph, L026's exact suffix
identities/injectivity, L071's post-compilation graph component only, and
L087's B/M convention. Local indicator/recombination results such as L072
are possible leads whose applicability to this target has not been
checked; they are not assumed mathematical inputs. No cross-notebook
input is proposed. Mathlib matching coverage remains unchecked.

The next turn must assess exact/stronger known results, relevant local
duplicates and failures, and primary theorem hypotheses before any
mathematical attempt. It may approve only a concrete mechanism supported
by essential coverage. Continue toward a witness only with a justified
prospect of both formal identities and one fixed full-bit polynomial in
the original M. Reject or narrow a proposed mechanism on an explicit
ordered-identity failure or a demonstrated excessive representation cost;
this would not show that every alternative witness is large. No
multi-variable lemma, state bound or construction is derived or approved
in this proposal.

## Completed comparison — step 348, 2026-10-19

LITERATURE / literature_comparison / NOVELTY_UNCHECKED, outcome EXPLORATION:
this is a new bounded comparison, not a theorem or an unchanged repeat
approval. No lemma, mathematical script, witness construction or size
proof is written. Mathematical exploration usage stays zero after step 347;
literature does not spend or renew that calculation budget.

### Discovery and primary sources

Queries included `OBDD variable order agree deleting k variables reordering
size conditioning`, `noncommutative IPS OBDD Boolean commutator witness
restriction Shannon expansion`, `"OBDD" "commutator" witness`,
`"OBDD" "variable order" "backdoor" conditioning`, `"OBDD" "reordering"
"2^k"`, `"OBDD" "orders" "deleting" variables`, `"noncommutative" "OBDD"
"Shannon" certificate`, and `"OBDD" "longest common subsequence"`.
No inspected result supplied the exact free-placeholder witness target.
Search hits on other reordering measures and OBDD proof systems remain
unread leads, not theorem inputs or evidence of an impossibility result.

- Bryant, *Graph-Based Algorithms for Boolean Function Manipulation*,
  IEEE TC 35(8), 677–691 (1986),
  [annotated author-restored PDF](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
  §1.1 equation (1), printed p.3, and §4.4, printed p.15. Read the Shannon
  statement and complete restriction algorithm: root/child references,
  selected successors, reduction and simultaneous restrictions. It supplies
  Boolean cofactor construction with linear graph work, not a free-ring
  equality between an original representative and a front-indicator
  interpolant. The formal lift and its cost remain research obligations.
- Rudell, *Dynamic Variable Ordering for Ordered Binary Decision Diagrams*,
  ICCAD 1993, 42–47,
  [primary scan](https://www.larshj.dk/PUMA/references/Dynamic%20variable%20ordering%20for%20ordered%20binary%20decision%20diagrams%20-%20p42-rudell.pdf),
  §4.1, printed p.44 (PDF p.3). Read the complete four-cofactor replacement,
  equal/existing child-node cases and reference-dependent deletion; also
  retrieved the page image. This local Boolean operation does not bound
  all snapshots for several long moves. L089's audited single-move bound
  cannot be iterated with an unstated constant-width premise. No new
  multi-variable width estimate is inferred here.
- Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative
  Formulas*, [arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4),
  Lemmas 3.6–3.7, printed pp.17–18. Read both statements and all context,
  scalar/variable, addition and multiplication cases. Lemma 3.7 supplies
  a commutator-placeholder formula vanishing at zero and evaluating to
  PQ−QP, of size at most |P|²|Q|², for formula inputs; Lemma 3.6 places a
  correction in a formula context. F₂ is compatible, with minus equal to
  plus. The bounds are in formula size, not arbitrary graph encoding, and
  neither lemma states the desired interpolation lift.
- Tzameret, *Algebraic Proofs over Noncommutative Formulas*,
  [arXiv:1004.2159v2](https://arxiv.org/pdf/1004.2159v2), Definition 3.1,
  Lemma 3.4/Claim 3.5, printed pp.6,9–10. Inspected the definition and
  complete addition/product commutation proof with the single-occurrence
  context condition. Polynomial NFPC proof sequences over any field do
  not themselves supply one graph-sized free-placeholder witness. No
  proof-sequence extraction theorem is assumed.
- Bova–Slivovsky, *On Compiling Structured CNFs to OBDDs*, Theory of
  Computing Systems 61, 637–655 (2017), DOI 10.1007/s00224-016-9715-z,
  [published article PDF](https://d-nb.info/1119846765/34), §3.4, PDF
  pp.11–13. Read the deletion definition, Lemma 12 and complete proofs of
  Theorems 13–14. Lemma 12 bounds CNF subterm width by 2^k times residual
  width with deleted variables first. Theorem 14 requires a deletion-closed
  CNF class with constructive few subterms and an FPT deletion-set
  algorithm. Deleting CNF variables/clauses differs from deleting names
  from two permutations. These results supply Boolean representations,
  not corrections retaining original free polynomials. They are comparison
  results, not imported theorems on this target. The PMC browser check
  blocked one access route; the relevant primary PDF was accessible, so
  there is no essential source blocker.

Reuse the ready L035 assessment
`drafts/literature/2026-10-07-alternative-abp-commutator-witnesses.md` for
Raz–Shpilka Lemma 2 Step 1's independent-copy serial/parallel graph
operations, and the L072 assessment
`drafts/literature/2026-10-17-logarithmic-input-deletion-data.md` for
unchanged restriction/recombination source coverage. No general
circuit-to-ABP, small-formula unfolding or Boolean-zero witness theorem is
an input. Mathlib matching coverage remains not checked, not absent.

### Local comparison and retained stops

Read L026's ordered injectivity and (4)–(12), L071's post-compilation
value/K/W construction and copying interface, L072's indicator and ordered
recombination proof/ledger, L035's receiving statement, L087's B/M,
L088's exact swap graph/common-order recovery, and L089's single-move
statement/structural proof and imports. Reuse step 347's independent
critical-audit verdict; this is not a second audit.

L026/L071's diagram recurrences have no ER-inference or original-clause
input; subset-variable placeholder reception still needs an applicability
argument. L072 already pays for indicator orthogonality and noncommuting
branch factors, even across different branch orders. Its representatives
are chosen interpolants, however; it does not identify them formally with
independently supplied f,g. That is why this target is not already L072.
L035 accepts explicit x-only affine ABPs including constants and arbitrary
endpoints. It supplies local commutations, not an interpolation rule.

L088 assumes logarithmic total adjacent distance; L089 one displaced
variable. Neither covers the current supplied set. L071's treewidth
compiler is unnecessary and cannot be invoked without its premise.
Attempt 030 still stops universal polynomial faithful common-order
value-graph availability; these two diagrams are supplied, so this target
makes no such availability claim. The overview's L033/L034 fixed-output
obstructions and L087's conditional NP=coNP burden remain independent;
none is an all-witness obstruction under this small-set promise. No
sibling notebook or cross-notebook theorem was read.

### Approved bounded attempt and discriminating test

Keep TARGET exactly unchanged. Select conditioning with formal lifting
and ordered recombination for one attempt. This is a proposed mechanism,
not a derived result. Use one fixed order of D and explicit restricted
input diagrams with the common induced order outside D. Import cofactor
operations, then justify exact dense/free-polynomial reception rather
than reprove Boolean restriction as a discovery.

The first unresolved subtarget is an explicit correction L_f evaluating
to f plus its ordered indicator/cofactor interpolant, and likewise for g,
with both corrections vanishing at zero placeholders. This is a sought
identity, not an established lemma. Test a one-sided state recurrence or
marked-edge graph using original cofactors and paid local commutator
blocks; do not pass a recursively generated placeholder witness to the
x-only interface of L035. If the lifts succeed, test their reception by
L072's indicator-product corrections and L026/L071's common-order branch
product component, retaining original factor order and original fg.
L072's whole ER/treewidth theorem is not applicable verbatim; justify the
component specialization completely.

Continue only with H(y,0)=0 and H(y,B)=fg formally, and one fixed full-bit
polynomial in original M and 2^|D| that charges every independently copied
graph, branch, indicator, correction, dictionary, name and reference. It
must specialize to a polynomial in original M at the supplied logarithmic
cutoff; M^|D| or a branch-dependent exponent is insufficient. A degree
bound from actual pre-substitution graph paths suffices; preserving L089's
sharper degree is not part of TARGET. Include empty D, no remaining
variables, constants, repeated successors, unreachable states and both
original factor positions.

Abandon or narrow this mechanism on an explicit failed ordered identity
or a demonstrated excessive representation/copy cost. A witness only for
changed interpolants misses the target; a failed construction does not
refute every alternative witness. New essential missing coverage requires
REVIEW_REQUIRED before researching the uncovered change. This assessment
supplies no semantic zero tester or general intermediate-width theorem.

The plausible downstream use is a larger restricted order-pair witness
interface alongside L088/L089. Arbitrary-order W₂, general ER data
availability and unrestricted SAT decision/separation remain open even
if this attempt succeeds. This source review claims no mathematical
progress beyond the inspected literature.

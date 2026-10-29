# Unary-product sparse quotient — bounded source comparison completed

TARGET: Construct a scalar simulation chain between independently built unary products FG and GF with total support and summed intermediate graph size <=C*(g(FG)+g(GF)) for an explicit universal C, without materializing a Cartesian cut table, or exhibit a failed equation or size obstruction for the proposed quotient.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 526 searched the exact unary product/support claim, conjugacy, sparse minimization, degree homogenization and strong shift equivalence; exact queries and access results are in drafts/2026-10-26-unary-product-source-review-work.md. Scoped local comparison retained L112/Attempt 047 and reused step 524; no full quantitative match or general impossibility was established.
SOURCE_EVIDENCE: Reuse the inspected Ésik–Maletti/Sakarovitch/Kiefer/Mohri inputs from steps 519/520/524 and L110/L111. Fresh primary reading: Lombardy–Sakarovitch 2022 Definitions 3.1/3.3, Proposition 3.5 with both proof directions, Theorem 3.12 with proof and Remark 3.14; Chatterjee–Kumar–Volk ITCS 2024 Definition 2.7/Lemma 2.8; Bhargav–Dwivedi–Saxena 2025 Lemma 2.2 and full degree-copy/constant-shortcut proof; Chen arXiv:0710.3746v3 definitions, Proposition 3/Theorem 1 and relevant factorization proof; Almagor et al. CONCUR 2026 §2, Theorem 3/Corollary 15 with its shared-stem proof. Exact versions, pages and primary links below.
COMPARISON: Field-valued qualitative simulation is covered. Functional minimal quotients are attached to each automaton, not just its series; degree-copy homogenization has degree-dependent size and changes the representation. The inspected unary tropical normal form has a quadratic bound in a different semiring; polynomial-ring shift equivalence does not supply boundary-preserving scalar maps. None of these inspected statements supplies the required linear support plus summed occurrence-graph bound for the independent endpoints.
GAP: No direct quotient states, boundary/constant/letter maps, universal C, or quantitative obstruction for this product pair is established. Raw constant/letter intertwining and right-closed unary equivalence must be distinguished before a compression argument. No novelty or impossibility for all chains is inferred from this bounded review.
REASON: Accessible primary coverage now separates qualitative equivalence, functional quotients, degree expansion and the exact quantitative gap sufficiently for one bounded mathematical attempt on the unchanged target. Optional inaccessible characteristic-zero leads are not prerequisites and are parked; import the ready general inputs without reproving them.
LITERATURE_REASON: The target changes to direct products of arbitrary unary DAG operands and a quotient built without Cartesian cuts; possible unary compression/conjugacy results and their sparse realization bounds were not inspected in the prior general Dcomm review.
SCOPE: The unchanged target is ready for a separately invoked bounded attempt using explicit acyclic singleton graphs and scalar F₂ maps, fixed independently supplied operands and serial-product recipes. First check the exact raw versus right-closed simulation obligations; then test a directly built quotient without cut-table or degree-table preprocessing assumed free. No finite job receiver, row-space search, cap/format change, complete-path enumeration or historical recovery is covered.

The proposal text below is preserved from step 525. Its pending-source
phrases describe the state before this review; the completed comparison at
the end supersedes those phrases, without supplying states or maps.

The main gap is uniform worst-case P versus NP. This target is a necessary
commuting sector of the local fourth-comparison problem, not a new route
to unrestricted complexity separation. With unary original operands all
L035 (2) central lists are literally empty, while the independent products
still need an equality certificate. A suitable direct chain could handle
that sector before considering selected noncommuting pairs. It would not
resolve the mixed-letter case, actual-byte/occurrence binding or total costs.

Use normalized unary affine operands: singleton labels are scalar one or
one original x, after within-label zero deletion. Allow branching, parallel
occurrences and F₂ cancellation, empty and unequal path lengths, no-path
graphs, disconnected components and coincident/nonextremal roots. In
particular a unique consumed degree at each vertex is **not** a hypothesis.
Unused alphabet/dictionary entries remain separately bound where required.
Products are the independent three-connector wrapped products specified in
L110 §21. Their full preclosure vertices, edges and singleton-label entries
define the denominator; operands and endpoints cannot be padded or replaced
by a canonical expansion to enlarge that denominator.

L112 supplies the new obstruction and the exact allowed path subfamily.
L035/L036/L110 fix the graph and operand recipes; L111 supplies the checked
closure subargument, not a Dcomm core isomorphism. L097/L108 input and
caller qualifications remain if this is later applied to the fixed job.
No cross-notebook input is proposed.

The planned comparison should inspect primary hypotheses and constructive
cases for sparse equivalence/conjugacy of unary weighted automata, unary
polynomial product realizations and degree quotients, including stronger
known quantitative conclusions and obstructions. These are **search leads**,
not inspected theorems or claims of novelty. Reuse the assessed general
sources; do not re-browse them just to repeat qualitative soundness.
Polynomial-degree or rational-function semantics alone do not settle a
linear scalar support bound, and an expanded dense coefficient/map table
must be charged if used.

A candidate refinement is a quotient formed directly from operand structure,
possibly sharing unary degree frontiers before generating cut pairs. This
is a proposal, not constructed mathematics. Branches with unequal prefix
degrees must be handled explicitly, rather than silently treating every
vertex as homogeneous or encoding whole paths. If source coverage supports
that proposal, first specify its states and maps and check every oriented
boundary/transition equation and right closure; count repeated intermediates,
map support, boundaries, indices and graph checking work. A concrete failing
equation or superlinear necessary count rejects only that proposed quotient.
An unfinished map remains unfinished, not a negative result.

The continuation test is an explicit universal linear ledger for the exact
product endpoints, or a fully specified obstruction to the proposed family.
The direct unary primitive is distinct from rerunning the stopped full cut
table; it must not materialize that table as an uncharged preprocessing
step. Full matching Mathlib coverage is not checked. This assessment is not
ready and approves no new derivation in step 525.

## Completed comparison — step 526, 2026-10-26

This is one LITERATURE / EXPLORATION / NOVELTY_UNCHECKED step. No new
lemma, mathematical script, quotient construction or counterexample was
produced. The target is unchanged. The sources below provide adequate
coverage for a bounded EXPLORE attempt, not a certification of originality.

### Local overlap and retained failures

Read L112's hypotheses, conclusion and §1 construction, L110 §§3–4, the
step-524 cancellation assessment, Attempt 047 and histories 524/525; search
those exact paths plus the earlier ancestry assessment. L112's unary path
obstruction concerns distinct cut-index states. It is not a lower bound
for arbitrary direct maps. L111's ancestry hypothesis is not available for
independent FG/GF products. L035/L036 retain operand semantics and L110
§21 the complete product recipe; their already assessed uses are unchanged.
Steps 519/520/524 and the October 25 coefficient assessment cover general
soundness, qualitative existence and right closure. No stopped receiver or
historical accounting route is reopened. No local duplicate supplies this
direct quotient in the paths checked; no global absence is claimed.

The exact discovery queries, candidate selection and access limitations
are saved in [the source-review notes](../2026-10-26-unary-product-source-review-work.md).
Only the primary passages listed below are treated as inspected evidence.

### Inspected primary results and scope differences

**Lombardy–Sakarovitch**, *Morphisms and Minimisation of Weighted Automata*,
Fundamenta Informaticae 186(1–4) (2022), 195–218,
[journal PDF](https://fi.episciences.org/9972/pdf), Definitions 3.1/3.3,
Proposition 3.5 and Theorem 3.12/Remark 3.14, pp.200–205. Read both
directions of the congruence criterion and the complete coarsest-congruence
proof: it uses amalgamation and representative-selection matrices, and
equality of transition sums into each class and final weights within it.
The hypotheses allow arbitrary semirings, hence F₂. This supplies a known
criterion for a proposed **functional** quotient, not its existence for
any two equivalent representations. The minimal quotient belongs to the
input automaton; it is not a canonical representative of its series.
Therefore this theorem does not authorize identifying independently built
endpoints by equality of their unary polynomials. It also does not replace
the explicit edge-occurrence, acyclicity or scalar-support ledger here.
No functional-to-arbitrary-scalar converse is imported.

**Chatterjee–Kumar–Volk**, *Determinants vs. Algebraic Branching Programs*,
ITCS 2024, LIPIcs 287, article 27,
[primary proceedings copy](https://d-nb.info/1367164834/34), Definition 2.7
and Lemma 2.8, p.27:7. Over a field, degree-d component extraction from
an ABP of size s and width w has a homogeneous ABP of size at most
s(d+1) and width at most w(d+1). Their size counts vertices. This is an
inspected statement, with its proof not given there. It gives neither
linear size independent of degree nor scalar maps to the original
occurrence graph. No reproof or exact-target application is attempted.

**Bhargav–Dwivedi–Saxena**, *Lower bounds for the sum of small-size
algebraic branching programs*, TCS 1041 (2025), 115214, accepted
28-Mar-2025, [author-hosted journal PDF](https://bhargavcs.github.io/files/sum-abp-lb.pdf),
Lemma 2.2 and full proof, p.6. Read the degree-copy stage for each vertex,
both constant-degree-preserving and linear-degree-increasing edge cases,
and the constant-edge shortcut stage. The final paragraph explicitly
keeps multiple output vertices, collecting each degree's component.
Their starting definition is a layered affine ABP and size counts vertices;
the construction uses degree-indexed copies, rather than assigning a
single consumed degree to each original vertex. Neither its width bound
nor its semantic reconstruction supplies the requested scalar map support
and summed occurrence-graph cost for fixed, possibly unlayered endpoints.
The constant-shortcut stage changes edge labels/incidence and is not a
free operation in this notebook's ledger. This is comparison evidence,
not an imported stronger single-output or linear-cost theorem.

**Chen**, *On Algebraic Shift Equivalence of Matrices over Polynomial
Rings*, [arXiv:0710.3746v3](https://arxiv.org/pdf/0710.3746v3), version
23-Oct-2007 (the PDF title page separately prints 28-Oct-2018), definitions
pp.1–2, Proposition 3 p.3, its reconstruction pp.5–6 and Theorem 1/proof
pp.2,6. Theorem 1 assumes a non-nilpotent square matrix over D[x], D a
principal ideal domain, and reaches a nonsingular matrix through full-rank
factorizations; the proof separately treats a zero terminal factor.
F₂ is a PID, but polynomial-ring factors need not be scalar maps and the
matrix relation alone has no designated initial/final vector conditions.
No support or transition-occurrence bound in our denominator is stated.
Thus exchanging matrix factors in this sense is not an exact-target
commutation certificate. No boundary-preserving specialization or reproof
of this theorem is undertaken.

**Almagor–Jecker–Mazowiecki–Orlikowski–Purser–Sinclair-Banks**,
*Representing One Letter Weighted Automata over the Tropical Semiring*,
CONCUR 2026, LIPIcs 391, article 10, published 24-Aug-2026,
[primary PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol391-concur2026/LIPIcs.CONCUR.2026.10/LIPIcs.CONCUR.2026.10.pdf),
§2 pp.10:3–4, Theorem 3 p.10:6, Corollary 15 and its complete shared-stem
proof p.10:10. For trim unary (Z∪{∞},min,+) automata, Corollary 15 gives
an equivalent Chrobak-form automaton with at most 3|Q|² states/transitions,
computable in polynomial time; its construction merges common initial
stems of the deterministic components. This is a precise unary compression
result, but uses minimum-weight semantics, not F₂ path parity. The
inspected proof gives no F₂ scalar simulation or linear endpoint-bound
certificate. Its bounds cannot be imported here. Empty-word and trimming
conventions also differ from the fixed arbitrary-root recipe.

### Reusable imports, optional unread leads and the bounded test

Reuse Ésik–Maletti's 2010 author manuscript Definition 3.1/Theorem 4.2 and
Sakarovitch's 19-Sep-2008 Theorem 24 at the exact primary URLs/passages in
the step-524 assessment. They already cover scalar equations and
qualitative chains over F₂; L110 §4/L111 §§4,7 cover finite right closure.
No qualitative theorem is reproved or relabeled as a sparse-size result.
Conjugacy imposes equations on each transition letter. Constant-edge
elimination and a raw per-label intertwiner are distinct source contracts;
the next attempt must check the precise raw constant and letter equations
it proposes as well as its right-closed equations. Closed unary equality
alone is not a cited theorem supplying a raw intertwiner. This is a source
scope warning, not a derived endpoint obstruction.

Kostolányi's *Determinisability of unary weighted automata over the rational
numbers*, [TCS 898 (2022), 110–131](https://doi.org/10.1016/j.tcs.2021.11.002),
remains an optional lead: the publisher's indexed primary text exposed
§2.2/Lemma 2.3, Proposition 2.4, Remark 2.6 and §6, but direct retrieval
failed and equations were incomplete. No theorem or quantitative conclusion
is imported from that preview. The related polynomial-ambiguity paper's
publisher page supplied only a subscription preview. Its full theorem and
proof remain unread. Characteristic-zero determinization is not an
essential input to testing explicit F₂ maps with ready soundness coverage;
these access leads are parked, not repeatedly retried. Spectral approximate
minimization and ambiguity-testing discoveries are likewise not imported.

The review found no matching theorem in the passages inspected. That is
neither a new lower bound nor evidence that the target is original. No
unread theorem is an assumed dependency. Full matching Mathlib coverage
is not checked; the assessed general algebra remains supporting coverage.

Continue with one direct construction/equation test on the unchanged
normalized unary product family. First fix all oriented boundary, raw
constant/letter and closure equations and test whether the proposed maps
meet them; no equivalence-to-conjugacy inference is free. A genuine quotient
must specify states/maps directly and handle mixed prefix degrees, parallel
cancellation, constants, empty paths, no-path graphs, disconnected states
and arbitrary roots. All repeated intermediates, support, boundary/index
data and graph-checking work must be counted. Continue only on a checked
universal C ledger, or a refined explicit map with a discriminating test;
abandon that proposal on a fully exhibited failed equation or superlinear
necessary count. An unfinished map is unfinished, not an impossibility.
No all-cuts or all-paths intermediate may be hidden before quotienting.
The downstream use and all unresolved independent gaps remain those in
the original proposal. Separate supervisor approval of this freshly ready
assessment precedes a new research invocation; no mathematics occurred in
this literature-only step.

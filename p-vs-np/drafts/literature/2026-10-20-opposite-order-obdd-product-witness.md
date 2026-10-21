# Opposite-order product witnesses — source comparison

TARGET: Test whether Boolean-zero products of two dense width-three OBDDs in exactly opposite variable orders admit polynomial-full-bit Boolean/commutator affine-ABP witnesses retaining the original fg and pre-witness M.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 360 searched exact/opposite/reverse-order OBDD conjunction, bounded reverse width and noncommutative reversal/commutator witnesses; inspected local L026/L035/L071/L085/L087 interfaces and Attempts 018/030. Queries and source-access limits are recorded below; no full-target theorem or novelty certification was found.
SOURCE_EVIDENCE: Reused inspected Bryant (1986) §4.3, LTW arXiv:1412.8746v4 Lemmas 3.6–3.7 and Raz–Shpilka component coverage from the L092 assessment; newly read Raz–Shpilka author manuscript Definition 1 and Lemma 2 Step 1 pp.4–5. L085 weighted paired-recurrence and its step-331 audit supply a local component, not an imported full-target theorem. Rabin–Scott primary text remained unread and is optional, unused coverage.
COMPARISON: L088–L092 order promises do not cover unbounded reversal. Bryant supplies Boolean common-order Apply; LTW gives formula-input corrections, not arbitrary-ABP full-bit bounds; Raz–Shpilka gives ordered path semantics/composition, not a reversal witness. L035 and L085 offer explicit original-only correction components for testing a weighted reversal approach without deterministic reordering.
GAP: Prove or obstruct a polynomial-full-bit original-only correction between a supplied graph polynomial and its word reversal, then receive the reversed weighted graph in the common-order product component while retaining original fg, original B and pre-witness M. Reversal semantics, graph realization, both identities and complete original-M ledger remain proof obligations.
REASON: Target-specific discovery plus inspected reusable graph components support one bounded proof attempt on unchanged TARGET. No inaccessible theorem is required by the proposed direct graph test; optional automata reversal is parked. This approval establishes scope only, with no new mathematical result.
LITERATURE_REASON: The changed hypothesis is complete reversal of an unbounded variable list, without a logarithmic block or deletion promise; existing component sources do not establish coverage of the required formal reversal correction.

The main gap remains unrestricted SAT decision/separation. The proposed
intermediate target is a restricted W₂ supplier for exact opposite orders.
Its plausible downstream use is a representation interface for order
changes not controlled by L092's block enumeration. Arbitrary-order W₂,
general ER-data availability, formula-only bounds and SAT transfer remain
independent unresolved obligations. This is only a proposed target, not
a conclusion about its difficulty, feasibility or novelty.

Retain L087's complete original B and pre-witness M, two explicit dense
deterministic width-at-most-three diagrams on the same complete named
alphabet, and the exact original product fg. The second order reverses
the first; q≥2 ensures distinct orders. Retain arbitrary redundant tests,
repeated successors, unreachable states and scalar terminal records.
Boolean vanishing is a promise, not a procedure supplied to the
constructor. The sought output is an explicit affine F₂ graph H with
both formal identities H(y,0)=0 and H(y,B)=fg and a fixed polynomial
full-bit bound in the original M, with uniform construction cost if a
constructor is proposed. Do not substitute equality merely on Boolean
assignments for either free-algebra identity.

Essential prospective local inputs are L026's ordered identities and
injective subspace, L035's original-only commutator graphs, L071's
post-compilation graph component, L087's receiving conventions and
L092's audited boundary/sorting construction as a scope comparison.
L090 and Attempts 018/030 are duplicate/failure comparisons, not assumed
mathematical premises. No cross-notebook input is proposed. Full matching
Mathlib coverage is not checked.

The original proposal requested a source-review-only turn (completed below). Search exact/standard terminology
for conjunction of opposite-order OBDDs, reverse-order branching
program products and noncommutative reversal/commutator certificates;
inspect primary hypotheses and essential cases before deciding whether
known results import, specialize or leave a bounded mathematical gap.
Check that a Boolean conjunction algorithm, a transpose/reversal
representation or a PIT theorem actually supplies the formal witness
interface before treating it as coverage. These are search leads, not
claims that such theorems exist or suffice.

Continue only with an inspected theorem covering the exact target or
adequate component coverage for one explicit discriminating test of
the missing correction. Record a scope mismatch or source blocker
precisely; do not manufacture a lemma or claim novelty from a failed
search. No mathematics on this new target was undertaken in step 359.

## Completed comparison — step 360, 2026-10-20

The proposal above is preserved as context; its former REVIEW_REQUIRED
status is superseded by this EXPLORE assessment. The exact TARGET and
its hypotheses have not changed. No new identity, lemma, graph algorithm
or favorable resource bound was proved in this literature-only turn.

### Gap and relevance

The main gap remains unrestricted SAT decision/separation. The target is
a restricted W₂ supplier for complete opposite orders; success could
supply an interface beyond logarithmic block enumeration. General ER
data, arbitrary-order W₂, formula-only bounds and SAT transfer remain
independent gaps. The audited official target version is retained in
`foundations/01-model-and-target.md`; step 356 reconfirmed Cook's official
§1 pp.1–2 on 2026-10-19. No target-definition change requires a new audit.

### Discovery and sources actually read

Queries included `OBDD opposite reverse variable orders conjunction
satisfiability polynomial time`, `noncommutative IPS reverse order
branching programs commutator certificates`, `OBDD reverse variable
ordering width 2^w reversal`, `ordered binary decision diagram reversal
width reverse order subset construction`, `"OBDD" "opposite orders"`,
`"OBDD" "reversal"`, `"OBDD" "reverse order" width`, and
`"noncommutative" "reversal" "commutator" polynomial certificate`.
A final algebraic-reversal search mostly returned unrelated univariate
reversal/factorization leads. None of these search results establishes
absence, novelty, a matching theorem or an obstruction.

Reuse the primary-theorem assessments in
`drafts/literature/2026-10-20-logarithmic-block-permutation-critical-audit.md`
and `drafts/literature/2026-10-18-common-order-weighted-value-data.md`.
These already inspect Bryant's common-order Apply, LTW's formula-input
Boolean/commutator corrections and the commutative FSTW weighted-roABP
corrections. Their target-specific limitations are unchanged: Boolean
semantics alone does not supply a free-ring witness, formula unfolding
may be exponential in graph size, and commutative factor moves cannot
be imported into this free algebra. No reproof of those source theorems
is authorized or needed.

New primary reading: Ran Raz and Amir Shpilka, *Deterministic Polynomial
Identity Testing in Non Commutative Models*, undated 16-page
[author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Definition 1 printed p.4 and Lemma 2 Step 1 printed p.5. Definition 1
specifies adjacent homogeneous-linear layers, singleton source/sink
layers and ordered path multiplication. Step 1 explicitly allows the
intermediate unlayered constant-edge model and separate-operand serial
and parallel composition, including scalar/variable leaves. This is
component coverage, not a theorem asserting polynomial formal reversal
corrections. The no-free-term hypothesis belongs to Lemma 2's final
homogeneous-output conversion; the proposed test uses only Step 1's
composition, not that conversion. Scalar/zero cases must still be paid
and justified locally. No PIT theorem is used to manufacture witnesses.

The Rabin–Scott 1959 primary scan was located at
[the Scott archive](https://github.com/CMU-HoTT/scott/blob/main/pdfs/1959-Rabin-Scott-finite-automata.pdf).
The raw PDF was rejected by the web reader as application/octet-stream;
local curl failed DNS resolution; alternate primary URLs did not load.
No theorem or proof from it was read, imported, or used to assert a
reverse-width bound. Park this optional automata lead. The selected test
uses explicit weighted graphs and direct proof obligations instead of
requiring deterministic subset conversion. Thus this access failure is
not missing essential coverage or a reason to repeat source retrieval.
Other snippets, course notes and search-result claims remain unused.

### Local comparison and precise scope of reuse

L087 supplies the exact dense width-three inputs, complete B/dictionaries
and pre-witness M. L026's increasing-multilinear injectivity is available
only after establishing a single common word order. L035 receives
original-variable affine graphs, including zero/no-path polynomials,
constants and arbitrary endpoints; no placeholder-bearing recursive
witness may be passed as its operand. L071 supplies its post-compilation
graph component only, without waiving its whole theorem's treewidth
hypothesis.

The newly relevant local component is L085's **weighted paired
recurrence**, equations (2)–(5), its acyclic first-exit realization and
step-331 audit. Read its full input/conclusion, representatives,
earlier-variable correction, paired recurrence and graph realization,
including the audit's scalar-terminal versus semantic-cancellation
qualification. The recurrence supplies formal product correction to an
increasing-multilinear residual for arbitrary explicit common-order
layered affine labels a+b*y_k and scalar terminals, not merely two
successor deterministic diagrams. This is a component written in L085's
proof, not permission to invoke the entire ER-data theorem without its
ER/fidelity hypotheses. A next proof must justify the component's use
on the particular supplied graphs and pay every independent occurrence
in the present M. In particular it must verify root/sink conventions,
scalar normalization, absent paths, parallel edges and cancellations.

L090's small deletion set and L092's logarithmic block partition cannot
be presumed for a full reversal; their recorded proofs are comparisons,
not duplicates establishing this target. L087's arbitrary distinct-order
NP=coNP consequence does not automatically specialize to opposite orders:
its constructed order pairs have no established reversal promise.
Attempt 030 obstructs universal faithful common-order value availability,
not this restricted supplied-input alternative-witness target. Attempt
018 stops unchanged approval repetition, not this changed-hypothesis
review. No cross-notebook input is used. Full matching Mathlib coverage
is not checked; no absence claim is made.

### One authorized bounded test, with no asserted construction

Next perform exactly TARGET as one RESEARCH / proof_attempt, classified
POTENTIALLY_NEW only in the limited sense that the checked comparison
found no full match. Test a direct weighted word-reversal interface:
seek a commutator-only correction to a supplied x-only graph's word
reversal, using L035 on original-only factors and one-sided propagation
of recursive witness states. Investigate a graph obtained by reversing
edges/terminals as the common-order weighted receiver input. Prove its
semantics explicitly; do not identify word reversal with equality in
the free ring or assume it is a deterministic OBDD. Then test reception
of L085's existing paired component and L026's injectivity under the
Boolean-zero promise. This paragraph specifies a mechanism to test, not
an algebraic recurrence, theorem, established composition or bound.

Continue only if an explicit acyclic affine graph establishes both
H(y,0)=0 and H(y,B)=the original fg, with one fixed polynomial full-bit
bound in original M, a justified bit-time bound if a constructor is
claimed, and a polynomial pre-substitution path-degree bound including
cancelling paths. All graph copies, terminal normalization, complete
names/B/placeholder dictionaries, connectors and references must be
charged. Retain redundant/unreachable states, duplicate successors,
zero labels and scalar terminal cases without semantic deletion.

Abandon this specific mechanism if the correction requires recursive
witnesses on both sides with uncontrolled duplication, any L035 call
receives placeholders, the residual fails the single ordered-multilinear
hypothesis, or a demonstrated graph/bit bound is superpolynomial in
original M. Record an actual obstruction rather than declaring failure
from a suspected cost. A conditional intermediate result may be useful
without resolving independent ER/SAT gaps. Do not claim arbitrary-order
W₂, a Boolean-zero promise tester, certified originality or a complete
solution. Any newly established lemma requires a later separate audit.

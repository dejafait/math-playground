# L110 — Separate fixed-job coefficient certificate: soundness and accounting

## Hypotheses

Work over the exact field F₂ and free associative polynomial algebras. Fix
the step-493 job at `scripts/four-rule-extraction/output-493/restricted-boolean.json`,
field `jobs[7]`, together with its maps and the matching
`output-493/restricted-interior-bound.json` and
`output-491/retained-interior-bound.json` in the same directory. Fix also
`output-489/inputs/proof.jsonl`, `output-489/inputs/request.json`, source record
78, translation event 2642 and Boolean-input event 2643. These are literal
immutable inputs, not caller-selectable equivalent formulas. The source has
212 records and the retained SHA256 is
`f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e`.
The alphabet order is [y5,y4,y3,y2,y1,y0], with the entire supplied dictionary
(six Boolean and fifteen pair-once commutator placeholders), including unused
entries. Scalars, original letters and placeholder positions are disjoint
types. Scalar one is not an alphabet letter. All names, trees, roots, label
entries and occurrence indices retain their original types and order.

The following is a specification for a **separate** certificate interface,
not an implemented checker. Acceptance is conditional on actually checking
every binding, transport, structural and coordinate obligation below from
those fixed bytes. In particular a prior receipt, hash, rank answer or PIT
answer is not an oracle. The caller-path and SHA engineering assumptions of
L108 §§11,13 remain if that file-loading boundary is used. Mathematical
soundness below assumes equality of the actual input bytes; a digest alone
does not prove that equality against an unbounded adversary.

Use the exact graph/path semantics of L035, L036 and L038: finite explicit
acyclic graphs, affine labels, ordered products, empty path 1, and sum with
F₂ multiplicity. Allow constants, zeros, parallel cancellation, no paths,
empty alphabets and nonextremal or coincident designated roots. No Boolean
quotient, randomized evaluation, implicit coefficient oracle or formula-size
promise is admitted.

## Conclusion

The finite checks specified below imply, for the **unchanged** job-7 graph W
and the independently specified marked expression R,

    W = R,       W(x,0) = R(x,0) = 0,
    W(x,A) = R(x,A) = fg+gf.                              (1)

Here f,g are the ordered original-only job operands and R is precisely L035
(2)/(4), not a reference obtained by reading W's internal graph. All
equalities are formal polynomial identities in their respective alphabets.
Structural checks separately retain every selected occurrence, copy and
connector and establish the one-placeholder path property before parity
reduction. Coefficient equality itself certifies none of these structural
facts or any literal propositional inference.

This is a reproduction/specialization of known finite weighted-automaton
semantics and coordinate checking. It supplies a sound conditional interface
and a resource ledger, not an accepted certificate, a construction algorithm
with fitting coordinate bounds, or a new PIT theorem. Section 9 now measures
the mandatory transport/framing; actual ranks, complete coordinate evidence
size and full fixed-job feasibility remain unknown. No old complete-word contract passes
by this result. Section 10 finds an omitted source-reference work class in
the measured preflight; §11 exhausts that phase's inline-comprehension class
and finds another 673 omitted visits. Section 24 closes the terminal audit
with administrative acceptance **NOT ESTABLISHED**: finite wire counts and
conditional constructor correspondence survive, but the selected-work
subtotals do not establish complete preflight execution within its ceilings.
Full Boolean/K/H/nonzero-fJ reception, later jobs, certificate
availability and uniform P versus NP remain open.

## Proof

### 1. Imported inputs and why this specialization is needed

Import Stefan Kiefer, *Notes on Equivalence and Minimization of Weighted
Automata*, arXiv:2009.01217v1, 2 September 2020,
[§§1–3, Propositions 1.1, 2.1, 2.2, Theorem 2.3 and Proposition 3.1,
pp.1–5](https://arxiv.org/pdf/2009.01217v1). Over an arbitrary field the word
coefficient of an automaton (alpha,M,beta) is alpha M(w) beta, including
M(empty)=I. Direct sums give differences; the forward space is transition
invariant; §3's coordinate equations transport all words. Only this exact
algebra is imported. The notes' default rational-arithmetic complexity is
not an F₂ bit bound or a finite job-size guarantee.

For finite constant edges import the acyclic case of Mehryar Mohri,
*Generic Epsilon-Removal and Input Epsilon-Normalization Algorithms for
Weighted Transducers*, IJFCS 13(1):129–143 (2002),
[author manuscript, Definitions 4–5/Theorem 1 and both remaining-path cases,
pp.4–6; acyclic discussion pp.10–11](https://cs.nyu.edu/~mohri/pub/ijfcs.pdf),
and the [Handbook author manuscript §6.1, (28)–(31), pp.21–23](https://cs.nyu.edu/~mohri/pub/hwa.pdf).
The fully acyclic case uses finite sums over any semiring. No completeness
or infinite-sum structure on F₂ is assumed. Manuscript revision dates beyond
the bibliographic information above are unestablished.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-job7-coefficient-certificate-soundness.md`.
It reuses step 496's exact source/duplicate comparison and Attempts 042–045.
L038 supplies affine splitting, endpoint wrappers, word gadgets and right
constant-closure transport; L055 §§2–3 is a comparison with a *left* closure
and exact-length basis interface, not an additional premise here. The checks
below specialize those semantics to the fixed independent reference and a
finite evidence format. The short invariant argument is included to justify
using a sufficient closed family rather than silently claiming a basis.
No homogeneous-layered algorithm or coefficientwise tensor product is used
for polynomial concatenation.

### 2. Binding and structural reception, independent of parity

Retain bounded immutable source/request bytes, freshly run their literal
checker with the original endpoint/alphabet/dictionary, and compare every
retained source field type-sensitively as in L108 §§11,13. Recheck record 78,
the two complete events and their source/formula/graph correspondence, not
just their indices. Normalize event 2643 exactly as in L036: preserve the
original dictionary, discard outgoing sink edges only under its suffix
convention, and split affine entries over F₂. The resulting normalized graph
must equal the retained input, including all records and roots. Regenerate
the ordered L036 job list (5)–(9) from this graph; job 7 must be its
sum-commutator at vertex 6 with outgoing edge occurrences [0,5].

Independently check the whole-operand restrictions against those regenerated
original-only operands: compute reachability including the empty path, check
all retained/deleted vertex and edge indices, injective maps, roots and
literal copied labels. Let F,G denote the resulting two whole-restricted
original-only operands, and f,g their polynomials. The path bijection in
L097 §22 identifies them with the untrimmed job operands, with ordered
products and multiplicities intact. These are not restrictions inferred
from W. Compare the matching inventories completely on this job's fields.

Enumerate every edge pair of F,G, including pairs with zero central label.
Recompute L035 (2) using the typed original indices and their full ordered
affine labels. Enumerate the contributing label-entry pairs before parity
reduction; retain repeated central occurrences and reject missing, extra or
reordered prescribed occurrences. Literal-empty central lists alone may be
omitted. Check all four entry-to-exit restrictions of every selected pair
against F,G by the same reachability test, retaining distinct copies.
Exhaust every copied vertex/edge range and check every internal copied edge,
central edge, exterior connector and root, with no overlaps or leftover
records. This is the complete structural procedure in L097 §§22–23, not
acceptance of `output-495/structure.json` as its substitute.

In addition, propagate sets of placeholder counts along the **structural**
singleton-edge DAG, starting with {0} at the entry; union at merges and add
one on placeholder edges. Zero scalar labels do not delete occurrences from
the original structural graph: if a more general retained representation
contains them, check its paths before algebraic zero deletion separately.
For the fixed graph all labels are
singletons. At its output require a subset of {1}, and check each copied
block structurally too. This includes parallel occurrences that later cancel.
It proves the one-placeholder assertion on all accepting paths, vacuously
when there are none. No coefficient matrix is used for occurrence reception.

The recorded structural result is 37,050 pairs, 120 selected lists, 480 copies
and 35,762+45,702=81,464 records. These are identification/check expectations
from L097 §23; no new run of those checks is asserted here. The complete
`output-495/reception.failure.json` was inspected: completed_modes is empty,
complete_reference_received is false and forward_position is null. No raw
reference or arithmetic verdict is imported from that failed process.

### 3. Independent ordered reference and four comparisons

Build R from **F,G and their original edge lists**, never from a path table,
coefficient table, branch list or internal copy of W. For each pair
e:u→v in F, d:a→b in G, use the expression

    F[sF,u] G[sG,a] T(e,d) G[b,tG] F[v,tF],               (2)

where T is recomputed by L035 (2). Sum in edge-list pair order. Use four
fresh disjoint **unrestricted whole-operand** copies per non-literal-empty
central list, with the indicated designated roots, and constant connectors
and fresh common roots as in L035. Thus R has no internal-copy pruning and
is independent of the changed W. Check the entire generated reference
against that recipe, including its empty pair-sum case (two roots, no edges).
Reference construction may use the already checked whole-operand maps; it
may not use W's 480 internal restriction maps as reference truth.

L035's disjoint-graph transport proves that this graph is exactly (2)
summed over pairs. Nonextremal roots are harmless: a path leaving a copy's
exit internally cannot return to its connector in a DAG. Coincident roots
have exactly their empty path; no-path factors give zero. The factors are
in F-prefix/G-prefix/central/G-suffix/F-suffix order. No tensor/Hadamard
product or commuting of original letters is permitted. Omitting a literally
empty central list removes a zero factor, not a semantically selected path.

Apply L038's local transports independently to W, R and the necessary
operand products. The modes are:

* free: alphabet = all six originals and all 21 distinct placeholders;
* zero: delete placeholder singleton edges, leaving originals/constants;
* axiom: replace each placeholder occurrence by disjoint word gadgets for
  its exact supplied dictionary polynomial, with the original letter order.

All dictionary entries, even unused ones, are checked. Affine splitting is
checked by collecting every entry's parity, constants separately. A zero
label has no normalized edge. An empty word gadget is a constant-one edge;
a zero word list adds none; parallel word occurrences retain their parity.
Each gadget has fresh interiors, its old endpoints and no other incidence.
Check those facts and every edge against the independently regenerated
bounded axiom tree. This is a local substitution check, never a PIT verdict.

Using disjoint serial/parallel copies, independently build the original-only
graph P for fg+gf, with two separate ordered products FG and GF. Check every
copy and connector against F,G. The same designated-root argument proves
its semantics, including constants, empty paths and zero factors.

Require a separate zero certificate for each difference

    Dfree = Wfree + Rfree,   Dzero = Wzero + Rzero,
    Daxiom = Waxiom + Raxiom,   Dcomm = Raxiom + P.         (3)

Characteristic two makes plus the difference. For each comparison use the
disjoint union of its two operand graphs, with injection row eta having a 1
at each designated entry and final column theta a 1 at each designated exit.
The two copies are disjoint even if their bytes agree. This preserves the
sum of their outputs without new cross edges. A supplied topological
permutation must be checked as a bijection and checked on every edge.

L035 (2) gives Rzero=0 because every term has its central placeholder factor.
Acceptance of all four differences therefore yields (1). The Dcomm check
is deliberately retained despite L035's theorem; checking substituted
commutators alone would leave the free-polynomial comparison unchecked.

### 4. Exact graph actions, with no stored dense closure oracle

Fix any one of (3). Let N be its disjoint-union vertex count, q its entire
mode-alphabet size, E0 its constant adjacency and E_a its letter adjacency,
with parity of all parallel entries. These matrices are mathematical
notation; the certificate need not store them. In a checked topological
order E0 and E_a are strictly upper triangular. Write

    K = I+E0+...+E0^(N-1),
    alpha = eta K,    M_a = E_a K,    beta = theta.         (4)

This is L038's **right** closure. By finite constant-segment decomposition,
the word coefficient is alpha M_(a1)...M_(al) beta. A path has a unique
constant segment before its first letter and after each letter. All sums
are finite and all ordered letters remain in their path order. For the
empty word this is eta K theta, not eta theta. No length homogenization,
last-row-vanishing assertion or L055 left-closure convention is substituted.

Here is an explicit, completely checked implementation of the linear actions
appearing in (4). For a bit row z, set v=z. Sweep vertices in the verified
topological order, and for **each** constant edge occurrence u→vtx XOR the
current bit at u into the bit at vtx. The resulting row, denoted C(z), is
the unique solution v=z+vE0: coordinate j depends only on earlier
coordinates and the fixed z_j. Since E0^N=0 this solution is zK. This also
proves exactness with parallel cancellation, nonzero injections at internal
vertices, no paths and coincident designated roots.

For a letter a, initialize z=0 and XOR the input row's bit at u into z_vtx
for every a-labelled edge occurrence u→vtx. Then return C(z). This is
exactly row E_a K. Compute alpha=C(eta) in the same way. No multiplication
or closure answer supplied by a prover is trusted. All edge sweeps include
zero contributions and every occurrence; omitting a scan because an
unchecked coefficient is zero is forbidden. This is the existing finite
topological evaluator specialized to bit rows, with its invariant justified
here to make the implicit operator checkable. No claim of a new algorithm
or a small live rank is made.

### 5. Dimensioned coordinate evidence and soundness

For comparison k supply r=r_k with 0≤r≤N and the exact bit arrays

    B: r by N,       c: 1 by r,
    T_a: r by r for every one of the q letters.            (5)

Require all of the following equalities coordinate by coordinate over F₂:

    c B = alpha,      B M_a = T_a B  (every a),
    B beta = 0.                                         (6)

Compute every row on the left of the middle check by the graph action in
§4, and every row on the right by the supplied T_a and B with exact XOR/AND
arithmetic. Compute initial coordinates and all r final inner products
directly. Compare every coordinate; no sampled rows, floating point rank,
prover-returned transition matrices or trusted identity flag is admitted.

The row span of B contains alpha by the first equation and is closed under
every M_a by the second. More explicitly, for any word w=a1...al,

    alpha M_w = c T_(a1)...T_(al) B.

For l=0 this is cB=alpha. If it holds for w, multiply on the right by M_a,
use BM_a=T_aB, and associate the finite scalar matrix products. This is
Kiefer §3's coordinate word argument. Multiplication by beta and the last
equation in (6) give zero for every word, including the empty word. The
word-coefficient semantics in §4 therefore proves formal zero of this
comparison. Apply this separately to all four comparisons in (3).

**A true basis is not a checking requirement.** B may have zero, repeated or
dependent rows, and need not be exactly the reachable space. Equations (6)
alone prove the one-way implication. Conversely, if the difference series
is zero, its reachable row space has dimension ≤N; any basis of it gives
(5)–(6) by Kiefer §§2–3. This is only qualitative existence and does not
supply a finite-size fitting certificate or a constructor run. No rank or
Gaussian-elimination verdict is needed by this verifier.

If r=0, the matrices have their stated empty dimensions: cB is the zero
N-row, all transition/final equations are vacuous and alpha must actually
be checked to be zero. This certifies no nonzero alpha. If N=0 in an abstract
zero automaton, r=0 and its series is zero; fixed graph inputs still require
valid roots, so the job representations have positive N. If q=0 there are
no transition equations, but the initial and final checks still imply
alpha beta=0, the only word coefficient. Zero beta is harmless. Neither
constants nor a zero reachable space license skipping input/transport checks.

### 6. Evidence bytes, retained data and complete work ledger

Fix the following possible wire format so that a size claim cannot silently
hide coordinate or framing costs. This is a specification, not permission
to change any existing serializer. All integers below are unsigned 64-bit
little-endian, checked for range before allocation; fixed record caps make
this restriction harmless for contemplated inputs. The bundle has eight
magic bytes `J7F2C001`, a comparison count (must be 4), length B_bind and
the B_bind binding bytes, then length B_trans and the B_trans transport bytes.
Those two byte sections retain the full fixed input bytes and manifest,
and all generated graphs, maps, dictionaries, gadget/copy attributions and
topological orders used above, respectively. Lengths, file names, all
nested framing and quoted strings belong to their actual byte counts.
Use strict bounded schemas with no duplicate/extra fields, noninteger
indices, floats or unconsumed bytes; no digest replaces necessary bytes.

Next, for each of the four comparisons in fixed order, store its index,N,q,r
(32 bytes), then B, c, and the entire list of T_a as three separately packed
bitstrings in row-major and alphabet order. Their byte lengths are inferred
from their checked dimensions; terminal padding bits must be zero. No other
matrix is supplied. Reject trailing bytes. Thus the exact bundle length is

    B_wire = 32+B_bind+B_trans
           +sum_k [32+ceil(r_k N_k/8)+ceil(r_k/8)
                         +ceil(q_k r_k²/8)].              (7)

The logical coordinate-bit count is

    P_bits = sum_k (r_k N_k+r_k+q_k r_k²).                 (8)

All four B,c,T sets are included simultaneously, even when checks run
sequentially. No completed mode is dropped from the evidence ledger.
Graphs and input bytes retained in two sections are charged twice when
actually copied. Also charge every checkpoint, receipt, failed write prefix,
temporary persisted artifact and simultaneous replacement file in the
aggregate evidence-byte count B_saved; a proposed full write is sized before
opening and its first rejected prefix recorded. The complete accepting
receipt, including all counters, must itself fit. Old output archives are
preserved; the new run's evidence cannot pretend a raw reference survived.

For graph costs record per input/reference/mode graph its vertices, edges,
affine-label entries before splitting, normalized edges/gadget interiors,
root/name/dictionary bytes and full encoded bytes. Record the sum across
all simultaneously stored/generated graphs as well as every per-graph
maximum. Repeated reference copies and Dcomm's two products are charged;
these are not free expressions. All input, source, tree, dictionary, label,
record and byte guards remain at their original values. In particular each
explicit graph must fit 2,000,000 records and label entries, and B_saved
must fit 200,000,000 bytes; record the generated aggregate too. More restrictive
new limits may be chosen before a later experiment, never inferred after it.

For arithmetic checks the exact numbers of scalar coordinate comparisons
are N_k initial, q_k r_k N_k transition and r_k final per comparison. Let
m0_k be the number of constant edges and mL_k the total letter-edge count
in that checked disjoint graph, retaining occurrences. Beyond validation,
one alpha sweep uses N_k bit initializations and m0_k XORs. All B-row letter
actions together use q_k r_k N_k zero initializations,
r_k mL_k letter-edge XORs and q_k r_k m0_k closure XORs. Computing cB,
all T_a B and B beta naively uses respectively r_k N_k,
q_k r_k² N_k and r_k N_k AND/XOR pairs, with their accumulator
initializations and coordinate comparisons also charged. The eta injections
and final-column construction are charged, including duplicate positions
if a different representation ever allows them. No constant-time
unbounded-vector XOR is assumed.

This describes every algebraic loop; zero coefficients are allowed without
removing their loop/inspection cost. Bit-vector packing operations, edge
and alphabet iteration, copying and zeroing scratch rows, dimension parsing,
topological validation and integer index arithmetic are separate costs.
For example the algebraic bit operations, initializations and comparisons
above are bounded by

    16 sum_k (q_k+1)(r_k+1)²(N_k+m0_k+mL_k+1).            (9)

The factor is deliberately loose; it is not a measured running time. Charge
index operations in a bit model with their actual bit lengths (at most 64
for dimensions; accumulated counters may be longer), not at unit cost.

The live-data ledger retains the wire bytes, all decoded or copied input
and transport data, all four coordinate arrays and completed receipts.
Report their actual stored bits/bytes separately. A direct checker needs,
in addition, at most four N_max-bit arithmetic scratch rows (input action,
letter accumulation/closure, coordinate combination and alpha), and the
graph/topological/index/loop/counter storage. If all coordinates are decoded
into separate bit arrays, add P_bits to the retained wire data; if views are
used, explicitly verify and report that representation. Charge temporary
decoding and receipt replacement peaks. This specifies an abstract bit/byte
ledger, **not** an assertion about Python object overhead or total interpreter
memory. A later implementation must measure or bound those separately if
it claims them. The new bit/coordinate measures are not stored_words,
polynomial_words or multiplication_pairs of the failed word receivers.
Their old guards stay unchanged; no old-contract pass is claimed when those
word operations are not performed.

For complete verifier work report the sum of the following disjoint ledgers:
input read/parse/literal checking; complete inventory, reachability and copy
reception; reference construction and all transport validation; the exact
coordinate loops above; all allocation/initialization/index work; and all
serialization, sizing, hashing and receipt I/O. Charge all failed and partial
work too. Structural reachability may use bit transitive closure, but every
word-sized/bit-sized operation in it must be counted according to the chosen
bit model. No theorem above bounds the full source checker or interpreter
by (9). Its other costs are explicit ledger components, not zero costs.
Neither timings nor a preview of a log prove receipt of all coordinates.

**Concrete later preflight.** Without any path-word expansion or coordinate
search, independently regenerate the graph/reference recipes, count every
generated graph/mode dimension N_k,q_k, B_bind and B_trans, and size all
framing. Tabulate (7)–(9) as functions of proposed r_k in [0,N_k], and the
full-rank worst case. Check the fixed graph/byte limits first; if the fixed
transport alone fails, abandon this format before arithmetic. If only the
worst case fails, record that fact without concluding that the actual ranks
fail. Any later row search must be bounded by declared storage/work limits
for this new interface, fixed in its ready assessment before execution.
No such numerical new-work limit or row search is authorized by this lemma.
An oversized candidate must stop with its full failure ledger, not change
caps, release required evidence, skip modes or assert acceptance by parity.

### 7. Scope, limitations and continuation test

The certificate implication closes the approved specification target only.
No implementation, new graph, received mode, rank measurement, evidence-size
measurement or finite cap pass has been produced in this step. Equations
(7)–(9) give a checkable later preflight rather than a feasibility theorem.
The unpruned independent reference may itself be too large. A symbolic
polynomial bound is not evidence that this fixed instance fits.

Continue only after a separate critical review of the independent binding,
right-closure/empty-word convention, all four coordinate implications and
the complete ledger, followed by separately approved bounded preflight.
Reject this specification if that review finds that it needs an unchecked
coefficient/transport oracle, omits a mode/empty word/ordered factor, uses
parity for literal-copy reception, or leaves a necessary cost uncharged.
Any correction belongs here with the precise surviving gap recorded.

Attempts 042–045 remain stopped in their original scopes. This result neither
reruns them nor replaces their accepting predicates. Jobs 8–244, whole-run
evidence, complete Boolean/K/H/nonzero-fJ, trusted paths/SHA provenance, total
interpreter resources, general certificate availability, L087 W₂ and
unrestricted ER/Frege or SAT remain independent unresolved requirements.
No complete solution or UNVERIFIED CANDIDATE resolution is proposed.

### 8. Separate critical audit — step 500, 2026-10-25

**Hypotheses and verdict.** This audit addresses exactly the prior SPECIALIZE
target in `drafts/literature/2026-10-25-job7-coefficient-contract-critical-audit.md`.
It retains §§1–7's conditional acceptance hypotheses, F₂, explicit acyclic
graphs, typed complete dictionary, immutable fixed inputs and unchanged caps.
The precise Kiefer/Mohri imports are those in §1; their inspected coverage is
reused, without importing rational-arithmetic bounds as bit bounds. No new
mathematical mechanism, source theorem, implementation or finite preflight is
introduced. No substantive defect was found in the conditional implication
or its symbolic ledger. This establishes reviewed local soundness, not an
accepted fixed-job certificate or progress beyond the source mathematics.

**Binding audit and evidence boundary.** The source, request, event and job
checks are premises that must actually be discharged. A self-consistent
pair of altered trace files would not discharge the required correspondence
to the fixed source/formula. The actual byte identity in the hypotheses,
fresh literal checking and complete regeneration in §2 remain necessary;
the old receiver's hashes and `structure_received` flag cannot replace them.
The typed dictionary includes Boolean placeholder display names equal to
original names; using the display string as a generator would be unsound.
Its actual positions, original indices and scalar tag must be kept distinct.

For indexing, record 78 means zero-based index 78 **after** the JSONL header,
physical line 80 of the retained source. The parser explicitly separates
`header, *records` before indexing. The complete selected row is an axiom
`or(not(A), A)` and event 2642's formula is its second operand A; physical
line 79 is an association record and must not be substituted. The complete
request, row, translation formula/reduced tree and translation graph were
inspected, as were the exact saved job kind, vertex and edge-occurrence
fields. They identify the sum job at vertex 6 on [0,5]. This is inspection of
the specified input boundary, not a fresh replay of all 212 literal records,
both full events, all operand maps or W's copied edges. The selected-map and
inventory previews were navigation only and establish no structural result.
The old source receipt and its limits were inspected as recorded data, not
accepted as current authorization or recomputed measurements.

Read the entire `scripts/four-rule-extraction/output-495/reception.failure.json`:
it records `accepted_fixed_job=false`, an empty `completed_modes`,
`complete_reference_received=false`, `forward_position=null`, and zero
forward metrics. Its failure is the first rejected proposed aggregate prefix,
200,000,001 against 200,000,000 bytes. The full actual proposed file size is
not recorded. Thus no completed coordinate mode, raw reference or equality
can be inherited from this receipt. Counts in §2 remain L097 §23's recorded
expectations; this audit does not newly certify its 480-copy finite result.
Attempts 042–045 retain exactly their previous scope and evidence.

The structural predicate itself is sufficient. The whole-operand reachability
maps must first be recomputed from regenerated L036 operands, independently
of W. L097 §22's bijections preserve original edge occurrences and ordered
labels, including empty and absent paths. All four internal restrictions
are then checked against these operands, and every prescribed range,
connector and central occurrence is exhausted. Merely checking a polynomial
cannot satisfy any of these tests. The set propagation in §2 uses union,
not F₂ addition: an induction by the last edge gives exactly the possible
placeholder counts of structural paths from the entry. Hence cancellation
cannot hide a zero- or two-placeholder accepting path. For an original-only
copied factor the corresponding output counts are {0} or empty; the {1}
condition is for the assembled W. Zero-labelled structural occurrences are
retained in this test, as expressly required before algebraic normalization.

**Independent reference and transport audit.** R's branch list is enumerated
from F,G, rather than obtained from W's selected maps. Its copies are whole
unrestricted operands, with the endpoints and order in (2). Each accepting
path selects exactly one branch and one central occurrence. Disjoint copies
allow independent subpaths; an internal departure from a copy's exit cannot
return to the connector in a DAG. Coincident endpoints contribute precisely
the empty path and absent paths contribute zero. This verifies the hypotheses
of L035's marked-edge transport and L097's restriction argument, without
assuming coefficient equality. A literal-empty central list supplies no path;
a nonempty list whose terms cancel must still be structurally received.

The local splitting, endpoint and word-gadget proofs in L038 apply before
any IPS identity hypothesis: only its local graph transports are used here,
not its ER conclusion with unproved certificate premises. Substitution is
an algebra homomorphism on the typed free alphabet. Fresh word interiors
and unchanged endpoints preserve ordered products even when words repeat,
are empty, or have zero total parity. The empty word is a constant edge;
the empty word *list* supplies no edge. Acyclicity is checked anew, not
deduced from numerical vertex labels. P uses disjoint FG and GF products;
there is no coefficientwise-product or commutativity assumption.

For each disjoint comparison graph, eta and theta select its two respective
entries and exits. Disjointness prevents cross terms even if copies have
identical bytes. The four zero conclusions are exactly Wfree=Rfree,
Wzero=Rzero, Waxiom=Raxiom and Raxiom=P. The independent construction gives
Rzero=0 because every term has its central placeholder. These implications
give all of (1). Dzero and Dcomm are deliberately redundant with other
mathematical information; that is no permission to remove their required
evidence, checks or resource charges.

**Right closure and coordinate audit.** In topological order each coordinate
of the constant sweep receives its original z-coordinate and every preceding
constant-edge contribution. Once its outgoing edges are swept its value is
final, so v=z+vE0. Nilpotence gives the unique solution v=zK. In particular,
multiple injections, parallel edges and interior roots do not require an
extremal-root assumption. A letter sweep followed by this constant sweep is
z E_a K, not z K E_a. Splitting a path into constant segments gives the
coefficient eta K E_a1 K ... E_al K theta, including eta K theta for l=0.
This checks both trailing closure and the empty-word coefficient.

All matrix products in (6) have the stated dimensions. From cB=alpha and
BM_a=T_aB, associativity gives alpha M_w=cT_w B by induction on word length;
postmultiplication by beta then gives zero because B beta=0. Dependence of
B's rows affects uniqueness of coordinates, which is never used. Conversely,
for a zero series each reachable row alpha M_w annihilates beta, and a basis
of their span gives the claimed qualitative existence by Kiefer §§2–3.
It gives neither measured r nor a construction within the stated caps.
For r=0, cB is the zero N-row and the initial check cannot be dropped. For
q=0 only the empty word remains and cB beta=0 still proves it. For N=0 the
abstract zero automaton is covered; fixed rooted inputs cannot have N=0.
Zero beta, no paths, cancelling paths and coincident roots cause no division,
rank assumption or exceptional unproved case.

**Independent accounting audit.** The outer header has eight magic bytes
and three eight-byte integers (comparison count and two section lengths),
giving 32. Each comparison has four eight-byte integers, another 32.
Packing B, c and the *whole* T list into three separate strings gives exactly
the three ceilings in (7). Packing every T_a separately would be a different
format and would require more padding. All four comparisons and all unused
alphabet positions remain charged. Dimensions and their products must be
computed without modular integer overflow before any length or allocation
test; a future implementation is not licensed to infer this from u64 fields.

For one comparison, count an AND and an XOR as two scalar operations, and
each initialized or compared coordinate as one. Using in-place constant
closure, the displayed algebraic loops in §6 have subtotal

    S = 3N + m0 + 3qrN + r mL + qr m0
        + 4rN + 2qr²N + 2r.

The initial/transition/final comparisons contribute N+qrN+r. The remainder
comes from one alpha sweep, all letter actions, and the cB, T_aB and B beta
products with their accumulators, exactly as specified in §6. Let
U=(q+1)(r+1)²(N+m0+mL+1). The N coefficient
3+3qr+4r+2qr² is at most 3(q+1)(r+1)²: separately,
3+4r≤3(r+1)² and 3r+2r²≤2(r+1)². The m0 and mL
coefficients and constant term satisfy 1+qr≤(q+1)(r+1)²,
r≤(q+1)(r+1)² and 2r≤(q+1)(r+1)². Thus S≤3U.
Even materializing eta/theta by 2N zero initializations and at most four
injections adds at most 4U. Equation (9)'s factor 16 therefore covers these
algebraic counts, including r=0 and q=0; it is not a full-verifier bound.
Index arithmetic, packing, scanning, copying and allocation remain in the
separate nonarithmetic ledger rather than becoming free operations.

Four N_max-bit arithmetic scratch rows suffice for the specified direct
evaluation: one optional unpacked B row, one letter accumulator with closure
in place, one coordinate-combination accumulator, and alpha. Initial and
final vectors may be read from the two designated root positions; they need
not be two additional live dense scratch rows. If an implementation retains
their dense versions, it must charge them as additional retained data or
reuse scratch after the initial check. All B,c,T arrays are retained in the
wire and charged again if decoded; graph/index/topological storage, scalar
accumulators and counters are separate. This establishes the abstract scratch
claim, not an object-memory bound for any programming language.

The ledger includes full binding/transport bytes, every independent R and P
copy, mode graphs, disjoint comparisons, occurrence maps, dictionary and
topological data, simultaneous evidence, failed prefixes and replacement
peaks, receipts and their I/O. Its six work categories also include fresh
source checking, reachability, construction and complete structural reception.
These are reporting obligations, not supplied numerical bounds; a later run
that omits them fails this contract. Per-graph records/labels and aggregate
saved bytes have their stated thresholds; aggregate graph counts must also
be reported. Neither (7)–(9) bounds the full checker/interpreter, establishes
cap fit, or changes the stopped word-receiver measures.

**Decision and remaining limitations.** The proof audit passes at the
conditional specification level. No argument repair, new lemma or dependency
is needed. Independently bound finite transport, framing and graph dimensions
remain a legitimate discriminating preflight: fixed transport failure rejects
this explicit format; a worst-case coordinate-size failure alone says nothing
about actual reachable ranks. That distinct target still needs separate
scope approval before execution. No actual certificate, new graph, rank,
full equality or implementation is supplied by this audit. All independent
limitations in §7, including whole Boolean/K/H/nonzero-fJ reception and the
unrestricted P-versus-NP gap, remain. Full matching Mathlib coverage is still
not checked; no absence or machine-verification claim is made.

### 9. Fixed explicit transport preflight — step 502, 2026-10-26

**Hypotheses and status.** This is one finite REPRODUCTION implementation of
the exact SPECIALIZE target saved before invocation in
`drafts/literature/2026-10-25-job7-coefficient-transport-preflight.md`.
All hypotheses of §§1–8, the original CAPS, the literal source, job 7,
dictionary, occurrence lists and ordered products are unchanged. Reuse the
precise primary citations and qualifications in §1 and the separate algebraic
audit in §8; no theorem is reproved and no new algebraic mechanism is used.
This section records a measured representation/preflight result. Section 10
finds incomplete administrative coverage in its separate critical audit;
the reported measurements are preserved, but no complete audit pass follows.
It does not accept any coordinate evidence
or equality in (1)/(3), and does not pass a stopped complete-word contract.

**Fresh finite construction and checks.** Run, only in a clean reproduction
workspace where `scripts/four-rule-extraction/output-502/` does not exist,

```text
PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/preflight_job7_transport.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/check_job7_preflight_accounting.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/check_job7_inventory_fields.py
```

All three programs refuse overwriting their outputs; do not remove the retained
run to reproduce it. The first program pins every original CAPS value,
checks strict UTF-8 round trips, reruns the unchanged immutable-byte literal
engine, and checks every source/request field against the bytes bound here.
The source has 212 accepted records, tree depth 19 and 13,018 aggregate
request/source tree nodes, below 10,000, 64 and 100,000 respectively.
Record 78 is physical line 80. The ordered six-name alphabet and all 21
dictionary entries are retained, including unused entries.

No polynomial expansion is used even to check the input translation. The
program independently recursively reconstructs its scalar-reduced syntax
and disjoint serial/one-plus graph, then compares every record of event
2642 and event 2643 against it. Its truth-translation conventions are the
same fixed L108 conventions: true maps to 0, false to 1, negation to one
plus the child, and ordered disjunction to ordered product. The reductions
use only scalar zero/one laws. The resulting graph and its L036 normalization
both have 154 vertices and 199 edges. Regenerating the complete ordered
L036 list identifies job 7 as the sum job at vertex 6, edge occurrences
[0,5]. Its original operands each have 155 vertices and 200 edges.

Whole-operand reachability includes the empty path; the two independently
regenerated restrictions have respectively (147,190) and (151,195)
vertices/edges. Original-only labels, roots, injective maps and retained/
deleted occurrences are compared completely with both inventories. The
37,050 edge pairs are enumerated, including literal-empty central lists;
the 120 selected lists retain their order and multiplicity. All 480 internal
copies, their ranges, maps, literal edges, four exterior connectors per pair
and central occurrences are checked with complete partition exhaustion.
Every fixed copy has distinct roots and an entry-to-exit path. The structural
placeholder-count propagation at W's sink is {1}, before cancellation.
W again has 35,762+45,702=81,464 records.

R is independently enumerated from F,G's entire original edge lists, with
four fresh whole-operand copies for each nonempty central list in (2)'s
order; W's selected-copy maps are not used to select/reference its interiors.
It has 71,522 vertices and 93,000 edges. Every whole copied edge and each
connector/central edge is checked. P uses two independently copied ordered
products FG and GF, including all serial/parallel connectors; its graph has
602 vertices and 780 edges. All six W/R local-mode graphs and all four
disjoint comparison graphs are explicitly allocated and retained. Local
reception exhausts every word gadget/edge/range; zero substitution deletes
only placeholder edges. No IPS extra +1 edge is introduced. Each graph's
topological order is checked as an injective exhaustive permutation and on
every edge. The separate mode alphabets retain unused names. The comparison
graphs are disjoint unions with two explicit eta/theta positions, rather
than identifying their designated roots.

**Exact frozen representation.** The manifest resolves the assessment's
wording discrepancy: its "seven" fixed files enumerate six. The binding
array contains those six in the prescribed order, followed by both essential
event files, for eight path/raw-text pairs. Their original raw bytes total
54,036,413; the escaped JSON binding section has

    B_bind = 57,478,400 bytes.

All eight are included before any fit claim. The complete old output-495
failure is consumed: no completed mode, complete surviving reference or
forward position is imported. No old receipt or digest is an equality oracle.
L108's trusted engine/path/SHA boundary qualifications remain in force.

The transport object's frozen key order is `format`, `alphabet`, `dictionary`,
`symbol_transport`, `source_binding`, `whole_operand_maps`,
`selected_occurrences`, `reference_copies`, `product_copies`, `base_graphs`,
`mode_transports`, `comparisons`. Graphs retain the existing explicit
vertices/source/sink/ordered-edge-list schema; tokens are interpreted by
the complete typed scalar/original/placeholder transport, never conflated
by spelling. The base array includes F,G,W,R,FG,GF,P; the mode array includes
the six separate W/R modes; each of the four comparisons stores its own
full graph, copies, mode alphabet, eta/theta and topological order.
Attributions and maps are explicit; none is a substitute for a copied graph.
The full dictionary appears once at this transport level; repetitions in
the literal binding bytes and nested graphs/maps are charged again there.

The chunk serializer recursively emits compact JSON with ensure_ascii=True,
UTF-8 and no trailing newline. Object/list punctuation and key order are
explicit. A long string is emitted as one opening quote, consecutively
escaped 65,536-character pieces with their outer quotes removed, then one
closing quote. JSON's escaping is characterwise, so this equals the full
escaped string, including backslashes and control characters. Induction on
the finite JSON object therefore identifies the concatenated chunks with
the specified compact encoding. Every chunk's full byte length is counted
before any rejected suffix could be written. No second whole serialized
binding or transport object, large payload file or failed prefix is saved.
The full transport count, including every repeated comparison copy, is

    B_trans = 63,886,102 bytes.

`scripts/four-rule-extraction/output-502/preflight.json` retains the complete
per-graph/counting ledger, framing, stage times, item counters, input metrics,
all four dimensions and symbolic endpoints. Its graph table has 17 explicit
base/mode/comparison graphs, totaling 825,812 vertices and 1,067,955 edges
(1,893,767 records); this sum is not a per-graph cap. The maximum individual
graph has 247,186 records and 139,422 label entries, each below 2,000,000.
The four additional small input-graph ledgers and independently recomputed
framing/endpoint arithmetic are in `output-502/accounting-check.json` in
the same directory. Their bytes were already included in the complete
sections; this supplemental ledger creates no additional transport copy.
A final narrow `output-502/inventory-fields.json` supplement checks repeated
source/target/job identity fields, both whole-map list lengths, every selected
pair's central metadata in both inventories, exact four-copy list lengths
and type-sensitive metric fields. These unused metadata fields were omitted
from the main program's explicit comparisons; its original run and receipt
are preserved, and only these supplementary checks are added.

The exact comparison dimensions, retaining parallel occurrences, are:

| comparison | N | q | m0 | mL |
| --- | ---: | ---: | ---: | ---: |
| Dfree | 107284 | 27 | 127542 | 11160 |
| Dzero | 107284 | 6 | 127542 | 10920 |
| Daxiom | 107764 | 6 | 127542 | 11880 |
| Dcomm | 72364 | 6 | 86158 | 7982 |

With independent integers 0≤r_k≤N_k, substitute these four rows into
(7)–(9), retaining all four coordinate arrays simultaneously. At r_k=0
the exact wire baseline is

    32 + B_bind + B_trans + 4·32 = 121,364,662 bytes.

This is a size baseline, not a valid rank-zero certificate. At r_k=N_k
the wire size is 65,220,461,539 bytes and P_bits is 520,792,775,000.
The full-rank endpoint exceeds 200,000,000 bytes; it says nothing against
the unknown actual ranks. The (9) bounds at the zero and full endpoints are
184,059,344 and 2,004,404,443,690,552,400 algebraic bit operations. These are
loose algebraic upper bounds, not measured work or the administrative
item-visit metric. Four separately rounded scratch rows cost 53,884 bytes.
Separate decoded coordinate arrays add P_bits bits to retained wire data;
graph/index objects, raw input buffers, decoding and receipt peaks remain
separate live-data categories, as (7) does not bound interpreter memory.

**Evidence/work qualifications.** The primary run takes about 40.64 seconds,
including fresh literal checking, and reports 60,624,737 instrumented item
visits. Supplementary accounting adds 579,346 and complete inventory-field
checking adds 14,180,926 reported visits, totaling 75,385,009 below
100,000,000. The two supplements take about 0.13 and 5.38 seconds respectively;
their timers and failed preliminary metadata read are distinct from the
primary timed run. Input character scans, UTF-8, parsing/I/O,
source-engine timing, graph generation/checks, reachability bit-operation
bounds, topology, serialization and counter/index lengths are separately
recorded; this is not a total interpreter-work proof. The largest graph
index needs 17 bits. Process memory is an observation in the receipt, not
a proved memory bound. No word multiplication, coordinate search, dense
constant closure or path expansion occurs.

One supplementary loader first incorrectly used the strict mathematical
input parser for an administrative receipt containing timing floats. It
stopped before graph checks. Its failure is preserved in
`output-502/helper-first-read.failure.json`; only administrative metadata
loading was corrected. Original fixed-input parsing remained strict; no
proposed transport is decoded by this preflight (see §22). The primary
preflight was not rerun or overwritten. This failure is
not a mathematical cap obstruction.

The actual retained output receipts, all three programs and generated compilation
bytecode total 158,027 bytes, all within the predeclared 1,000,000-byte receipt
reserve. No receipts are replaced; no payload/temporary/failed-prefix files
exist. Even charging those retained programs plus the entire reserve again,
the conservative remaining coordinate-byte allowance is 77,477,311 bytes.
The exact final saved-artifact total and reserved allowance differ because
the latter deliberately retains the full scheduling reserve. The proposed
mandatory wire plus actual run artifacts is 121,522,689 / 200,000,000 bytes.
Old archives remain read-only; proposed binding wire bytes charge their new
literal copy, while actual raw/decoded input memory is separately reported.
No total live-memory cap fit or exact Python-object size is asserted.

The primary program reports mandatory transport/framing fit. Section 10's
separate audit finds an incomplete work ledger and therefore leaves the
preflight audit unfinished. It does not refute those byte measurements or
prove a cap overflow. Actual rows/ranks and all equalities are unknown,
and every broader limitation in §7 remains.
Mathlib's full matching coverage remains not checked. There is no new DAG
input, candidate P-versus-NP argument, or claim of progress beyond the
unchanged known graph/coordinate semantics.

### 10. Separate implementation audit: omitted reference selections — step 504

**Hypotheses.** Keep the exact §9 inputs, representation, original CAPS and
the prior SPECIALIZE scope in
`drafts/literature/2026-10-26-job7-transport-preflight-critical-audit.md`.
This is a REPRODUCTION proof audit, using its ready source comparison and
§1's existing algebraic citations. No new algebraic result or representation
is introduced. The fixed runtime reports Python 3.15.0. The assessment's
[official sys.settrace source](https://docs.python.org/3.15/library/sys.html#sys.settrace)
rendered 3.15.1, not an exact patch-version match; runtime behavior below is
checked locally, not inferred from that later documentation.

**Conclusion.** The original observer omits a class of **212 source-record
reference selections** actually performed by the unchanged literal checker.
Its reported 75,385,009 item visits therefore do not constitute the required
complete administrative ledger. This rejects the coverage claim, not the
transport encoding or its measured byte fit. No corrected complete work
total, cap overflow, full transport audit, coordinate evidence or equality
is established. The broader audit is unfinished.

**Proof and finite evidence.** In `scripts/parity-four-rule/checker.py`,
`_check_stream` line 90 constructs `p = [fs[j] for j in refs]` after checking
the source record's references. Each iteration retrieves a previous source
formula and appends that selected object to the list. This is a separate
record-selection/allocation/index operation from checking each reference's
type and range, and from parsing or traversing the current formula. Section
6's ledger and the preflight's cumulative traversal rule must account for
this work, even though the selected objects already exist.

The original `observe_source` in `preflight_job7_transport.py` charges, in
this checker module, calls named `tree`, `nodes`, `variables`, `<genexpr>` or
`<listcomp>`, and line 76 of `_check_stream` once per source record. It does
not charge line 90. The actual runtime executes the list comprehension in
the `_check_stream` frame, without a `<listcomp>` call. Thus neither the
record hook nor any comprehension-call hook charges these selections.
There is no post-check adjustment for them: the primary program records the
observer total, and both supplements count their own new inspections only.
Earlier/later inspection of the same reference is a different traversal;
such charges cannot be silently reassigned to cover this missing class.

The audit program `scripts/four-rule-extraction/audit_job7_source_observer.py`
calls the original observer unmodified at every event. It checks the fixed
checker's AST to identify the single comprehension and its line, observes
the next line after its completion, and checks that every selected object
is literally `fs[j]`. It visits all 212 completed reference lists, compares
their entire ordered (record,reference) sequence to an independent strict
parse of the immutable source, and checks the input bytes before and after
the call. The full ordered 212-element sequence, not a sample, survives in
`scripts/four-rule-extraction/output-504/source-observer-lines.json`, field
`complete_reference_selections`; that complete value was inspected. Its
count is also independently determined by the accepted primitive arities:
77 cuts give 154 selections, 18 expansions give 18, 35 associations give 35,
5 contractions give 5, and 77 axioms give none, totaling 212.

The observation records 424 line events on the comprehension line, with
zero original item charges and no comprehension call events there. It
reproduces the primary receipt's **entire** `source_observer` dictionary:
101,874 generator calls/resumes; 239 request-loop, 13,018 check-tree-loop,
13,123 tree-call, 212 source-record, 12,919 variables-call, 12,919 nodes-call
and 13,018 size-depth-loop charges, totaling 167,322. The fixed source again
passes the unchanged literal checker: 212 records, 101,314 source bytes,
2,947 request bytes, depth 19 and 13,018 aggregate input-tree nodes. These
are bounded by the original guards. The omitted class is therefore a defect
of the original accounting, not a changed source or altered rule checker.

Adding just this class to the reported total gives 75,385,221, still below
100,000,000. This is only a **partial augmented ledger**, not a corrected
total or a lower bound on total interpreter work. Other comprehension,
parse, comparison, copy, supplement, failed-work and bit/index costs remain
to be reconciled. In particular the omission cannot be dismissed because
this one partial correction is small compared with the remaining allowance.

**Failed probe and audit resources.** The first opcode probe received no
opcode events in this runtime configuration and failed its complete-list
comparison. It establishes no reference-selection result. Its full receipt
`output-504/source-observer-audit.json` and exact program snapshot
`output-504/initial-audit-program.py` are preserved. The successful line
probe is the separate file above; no failure was overwritten. The two
receipts record respectively 1,721,672 and 1,723,629 audit event/item charges
(sum 3,445,301), and about 0.77 and 0.79 seconds. These counters include
trace events and independent JSON/source/reference walks, not total Python
work; bounded character scans, AST inspection and receipt I/O remain
separate. No graph regeneration, path/word expansion or coordinate work
occurs. The program, initial snapshot and both complete receipts total
31,607 bytes, below the unchanged 1,000,000-byte reserve. Source/raw/decoded
objects and trace callback storage are retained in memory; no exact total
interpreter-memory bound is claimed. All original outputs remain unchanged.

The successful probe refuses to overwrite its receipt. To reproduce in a
fresh isolated notebook copy, first create the empty directory
`scripts/four-rule-extraction/output-504`, then run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_job7_source_observer.py`.
The preserved initial failure is not needed to establish the successful
line-event witness. A fresh reproduction's event counts may differ with
tracing/environment; all sequence, literal-binding and observer checks must
pass anew. This witness uses no output-495 reference or forward mode.

**Remaining scope and Mathlib.** Step 504 stops the full-pass assertion at
this concrete coverage failure. It statically inspected all three §9
programs, but did not independently regenerate every transport, remeasure
the complete binding/transport byte sections, or finish every schema and
live-data check. Equations (7)–(9) and §8's conditional algebra are unchanged.
The reported §9 counts remain measurements awaiting those remaining checks.
A corrected, complete ledger and the remaining finite audit are required
before a coordinate experiment can be proposed. No new literature or
mechanism is required for corrections inside the unchanged approved scope;
none is performed or preapproved here outside that scope. Full matching
Mathlib coverage is not checked. This is informative negative implementation
evidence, not a mathematical discovery beyond the imported sources, a proof
lower bound, or progress resolving unrestricted P versus NP.

### 11. Source-wrapper inline-comprehension coverage — step 505

**Hypotheses.** Keep the fixed inputs, original CAPS, representation and
ready SPECIALIZE audit scope of §§9–10. This is one further subcheck of the
same REPRODUCTION proof audit, using §1's precise source imports and §10's
locally checked Python 3.15.0 tracing boundary. No algebraic theorem is
reproved. All original programs and outputs remain unchanged. The local
functions actually entered by `p.request` followed by `p.input_bounds` are
the scope of the exhaustive claim below; standard-library internals,
generators, other source work and later transport stages are outside it.

**Conclusion.** Six source-wrapper inline comprehensions perform **673
additional uncharged item visits**, distinct from §10's 212 reference
selections. The complete inline list/set/dict comprehension class in these
two entered local modules therefore has 885 omitted item visits. A repair
only at the literal checker's reference-selection line is insufficient.
This extends the administrative coverage failure, not a graph, byte-count,
equality or cap failure. The full audit and corrected complete total remain
unknown.

**Proof and complete finite evidence.** The audit program
`scripts/four-rule-extraction/audit_job7_source_comprehensions.py` reads the
two local modules' complete ASTs, pins the seven expressions below and their
owning functions, and records every function entered in those modules during
the original source-check phase. Intersecting the complete inline-comprehension
inventory with those entered functions gives exactly these seven expressions.
The unused `symbol_map` and `fixture_endpoint` comprehensions are retained
in the AST inventory and excluded only because those functions are not entered.
No `<listcomp>`, `<setcomp>` or `<dictcomp>` frame is observed. The original
observer is called unmodified at every trace event.

| module/function and line | consumed items | completed outputs | line events | original charges |
| --- | ---: | ---: | ---: | ---: |
| parameterized_input/request 152: Boolean expected set | 6 | 1 | 7 | 0 |
| parameterized_input/request 174: parsed source lines | 213 | 1 | 214 | 0 |
| parameterized_input/input_bounds 209: source formulas | 212 | 1 | 213 | 0 |
| parameterized_input/input_bounds 210: formula sizes/depths | 213 | 1 | 214 | 0 |
| parameterized_input/input_bounds 211: placeholder names | 21 | 1 | 22 | 0 |
| parameterized_input/input_bounds 217: required-bound map | 8 | 1 | 9 | 0 |
| checker/_check_stream 90: source references | 212 | 212 | 424 | 0 |

The item counts do not rest merely on interpreting line-event totals.
An independent strict parse supplies all 213 source lines (header plus
212 records) and the request. On the next statement after each comprehension,
the observer checks its **entire completed collection**. It checks the
six-member Boolean set against the fixed alphabet; every parsed source
record and header against that independent parse; the full formula list
against the request goal followed by all record formulas; every size/depth
pair against an independent explicit stack traversal; every placeholder
name in order, with the original alphabet prefix retained; and every one
of the eight required-bound entries against the complete checked metric
key set and original CAPS. At a following statement that is itself an
inline comprehension, its repeated line events do not repeat the completed
output inspection. The separate complete line totals still check the single
invocation count. For the reference lists, it checks all record IDs 0–211
in order, every reference index against the independent source parse, and
that each selected formula is the actual `fs[j]` object. Every collection
has the stated number of checked completions and line events equal to its
consumed items plus invocations.

These visits are separate operations from parsing a selected line, traversing
a selected formula, or checking reference validity. For example the 213
size/depth list selections do not disappear because the 13,018 internal
stack-node visits were charged. The original source observer charges neither
these comprehension lines nor their absent call frames; the set/dict cases
also have no matching name in its comprehension-call filter. There is no
post-check adjustment in the original program. Later supplements count
their own new traversals, not these actual source-phase collection operations.
The six new counts sum to 6+213+212+213+21+8=673; together with §10 they give
885. Both immutable input byte strings are checked before/after the call,
the complete request and records agree, and the unchanged literal engine
again accepts all 212 records with §10's exact receipt and input bounds.

The **entire** original `source_observer` dictionary reproduces §10's
167,322 charges. Adding this inline class gives a source-phase subtotal of
168,207. Adding it once to the original three-run total gives
75,385,894 / 100,000,000. In particular do not add 885 to §10's already
augmented subtotal and count the 212 selections twice. This remains a
**partial augmented ledger**, not a corrected complete total. No conclusion
about total interpreter work follows from these item units.

The complete evidence is
`scripts/four-rule-extraction/output-505/source-comprehensions.json`:
`complete_comprehension_table`, `full_local_ast_inventory`,
`entered_local_functions`, all `completed_source_record_ids`, the literal
receipt, input bounds, original observer and audit budget were inspected
in full. All sequence/output/inventory/count tests pass. The bounded audit
records 1,828,155 event/item charges against 100,000,000 and approximately
3.87 seconds against 900. The complete receipt (7,867 bytes) plus program
(15,440 bytes) totals 23,307, below the 1,000,000-byte reserve inside the
200,000,000 evidence-byte cap. No payload, temporary or replacement file is
written. The budget explicitly counts trace events and independent AST,
JSON, tree, comparison and collection items; input/source scans, parsing,
loading and receipt encoding remain separate bounded byte work. This is
not an exact interpreter-work or memory bound. No graph generation, word
evaluation or coordinate experiment occurs; original archives are preserved.

To reproduce, use an isolated copy in which output-505 does not exist and
run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_job7_source_comprehensions.py`.
The program refuses output overwrite and checks all original CAPS anew.
Trace/AST source positions and runtime behavior are explicitly pinned;
different code/runtime requires the complete checks to pass anew. The
same full source inputs and primary receipt are required. The audit's
receipt is administrative metadata, so its timing float is not permitted
as mathematical transport input by this program.

**Remaining scope and Mathlib.** This result requires broader wrapper
coverage than a one-line reference hook repair. Other explicit/implicit
source operations, parser/read and bit/index work, supplemental and failed
work, all independent transport regeneration/schema/encoding and live-data
checks remain unreconciled. The preserved metadata-parser failure states
that no graph/item walk began; that does not mean its read/parse work was
zero. Neither §9's wire measurements nor any equality or rank is separately
audited here. No new mechanism or target is selected. Full matching Mathlib
coverage is not checked. This is additional finite negative implementation
evidence, not progress beyond the imported algebraic sources or toward an
unrestricted complexity separation.

### 12. Entered explicit source-loop reconciliation — step 506

**Hypotheses and scope.** Keep §§9–11's immutable inputs, original CAPS,
Python tracing qualifications and unchanged ready SPECIALIZE implementation
audit. This is REPRODUCTION under the same approved target. Reuse §1's
precise graph/coordinate citations and §§8,10's qualifications; no algebraic
result is reproved. The exhaustive claim here concerns only explicit
`For`/`While` loops in functions actually entered in `parameterized_input.py`
and the literal checker during `p.request` followed by `p.input_bounds`.
Generators, implicit collection operations and standard-library internals
are outside this class. No graph regeneration or coordinate work is done.

**Conclusion.** The strict duplicate-key hook performs **730 additional
uncharged key-pair item visits**. These are distinct from §11's 885 inline
visits. All entered explicit local loops are reconciled below. The strict
parser also performs exactly **104,048 character-scan iterations** in this
source phase. The original receipt expressly assigns character scans to
separate byte/time work, so those iterations are **not added** to its
administrative item metric. The partial augmented source-phase and original-
three-run item totals are 168,937 and 75,386,624 respectively; neither is a
complete verifier ledger.
This supplies further finite evidence against completing the ledger by
inline-comprehension hooks alone, not a byte overflow or equality verdict.

**Proof and complete finite checks.** The audit program
`scripts/four-rule-extraction/audit_job7_explicit_source_loops.py` inventories
both complete local ASTs. A loop belongs to its innermost containing function,
so `input_bounds` does not misattribute the nested `size_depth` loop. The
intersection with all actually entered local functions is exactly the eight
rows below. The inventory retains loops in the unentered `symbol_map`,
`write_json` and `fixture_endpoint`; their exclusion uses the full entered
function set, not a hand-selected subset. Each row's body-entry trace count
agrees with an independently computed input count. The original observer
is called unmodified at every trace event and its charge increment is
recorded at each of these body-entry sites.

| module/function; body line | body entries | original item charges | accounting |
| --- | ---: | ---: | --- |
| parameterized_input/no_duplicates; 49 | 730 | 0 | 730 missing key-pair visits |
| parameterized_input/parse; 67 | 104048 | 0 | separate character-scan work |
| parameterized_input/check_tree; 104 | 13018 | 13018 | charged |
| parameterized_input/request alphabet; 140 | 6 | 6 | charged |
| parameterized_input/request placeholders; 156 | 21 | 21 | charged |
| parameterized_input/request records; 181 | 212 | 212 | charged |
| parameterized_input/size_depth; 203 | 13018 | 13018 | charged |
| checker/_check_stream; 76 | 212 | 212 | charged |

The independent parser uses `json.loads` with its own bottom-up object hook,
not `p.parse` or `p.no_duplicates`, on the complete request followed by every
source line. It records all ordered pair lists and resulting objects. During
the actual original source phase, every one of the 214 strict-parse returns
is checked against its complete independently decoded input and output, in
order. Every one of the 236 duplicate-hook returns is checked against the
complete ordered pair list and output object, also in order. All expected
returns occur and no extra return is allowed. Thus a trace count alone is
not being used as evidence of a completed parse or hook output.

The request's 21 placeholder objects have four pairs each, its dictionary
has two, and its outer object has five. The source header has three and each
of 212 records has three. Their total is
21·4+2+5+3+212·3=730. These are new actual parsing operations; visits to
the resulting objects elsewhere do not charge them. The observer has no
`no_duplicates` loop hook, no matching call hook, and no post-check correction.
The later supplements count their own inspections, not these source-phase
hook visits. All 730 are therefore absent from the stated item ledger.

The complete strict-parse sequence contains 2,947 request characters and
101,101 source-line characters, totaling 104,048; its per-call character
and UTF-8 lengths are all inspected. This counts the explicit pre-JSON
nesting scan, not JSON decoding or UTF-8 work. The original receipt's
`accounting` field states: “JSON character scans/UTF-8/I/O and Python
internals are separately byte/time work”. Accordingly these scan counts
supply a separate work component, not a correction of the item ceiling.
In particular adding 104,778 to §11's item total would mix the two metrics.

Independent stack traversals of the goal and every source formula give
13,018 nodes, explaining both tree-loop rows. Complete request/source
outputs, both input byte strings before/after, the 212-record literal
acceptance and all input bounds check. The entire original observer again
equals §11's dictionary, totaling 167,322 charges. Hence the new partial
item totals are 167,322+885+730=168,937 for the source phase and
75,385,009+885+730=75,386,624 across the original three runs. No previous
212-visit correction is added twice. Other generator, implicit comparison,
allocation, parsing, failure and supplement costs remain unaccounted here.

**Preserved evidence, repairs and bounds.** The first probe stops before
tracing because its AST string pins omit tuple parentheses produced by
`ast.unparse`. Its exact program and failure receipt are preserved in
`scripts/four-rule-extraction/output-506/initial-audit-program.py` and
`scripts/four-rule-extraction/output-506/explicit-source-loops.json`.
It incurs 56,553 audit event/item
units, not zero work. Correcting only those pins gives a complete successful
loop count in
`scripts/four-rule-extraction/output-506/repaired/explicit-source-loops.json`, with exact
program snapshot alongside. That receipt initially lumps the character
scans with missing items. This metric interpretation is superseded, without
deleting its evidence, by the final program and
`scripts/four-rule-extraction/output-506/reconciled/explicit-source-loops.json`:
only the 730 key pairs
are added to the item total; the 104,048 scans are explicitly separate.

The full parse/hook sequences, full AST inventory, entered functions,
observer, literal acceptance and budget were inspected in the first
successful receipt. The final run reexecutes their complete checks; its
loop table, scopes, bounds and corrected totals are inspected. The saved
`scripts/four-rule-extraction/output-506/reconciled/receipt-reception.json`
additionally checks equality
of all eight complete parse/hook/inventory/observer/acceptance/bounds/budget
values across the two successful runs, as well as the corrected arithmetic.
Its exact small comparison command is retained in the tool transcript.
It is not a sample or hash-based comparison.

Each successful run records 1,856,194 event/item audit units. Including the
failed probe gives 3,768,941 / 100,000,000 across these three instrumented
runs; their measured durations total less than seven seconds / 900.
The small final cross-receipt comparison is separate bounded receipt work,
not included in that instrumentation count. The complete preserved probes,
program snapshots, current program and receipts total 100,034 bytes against
the 1,000,000-byte reserve inside 200,000,000 aggregate evidence bytes.
No payload or temporary replacement file is written. These are finite
audit event/item and artifact measures; source/module reads, parsing,
receipt encoding/comparison, bit/index costs and Python allocation are not
claimed to have a total interpreter bound.

To reproduce the final program, use an isolated copy retaining both prior
probe artifacts but without `scripts/four-rule-extraction/output-506/reconciled`, and run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_job7_explicit_source_loops.py`.
The program refuses output overwrite, carries both prior instrumented
probe costs and all retained artifacts, and checks unchanged CAPS. The
separate receipt-reception check requires the completed final receipt.

**Remaining scope and Mathlib.** The entered explicit-loop class and §11's
inline class are reconciled; the source phase as a whole is not. Generator
resumptions, implicit traversals/comparisons, duplicate parsing elsewhere,
read/parse internals, failed/supplement work, independent full transport
regeneration, schemas, bytes and live peaks remain open. No measured byte
claim is refuted here, no administrative cap is shown to overflow, and no
rank, coordinate or equality is accepted. This is local implementation
progress only, not mathematics beyond the imported sources or progress
toward an unrestricted separation. Full matching Mathlib coverage remains
not checked.

### 13. Source generator yields and resumptions — step 507

**Hypotheses and scope.** Keep §§9–12's fixed bytes, original CAPS,
unchanged ready SPECIALIZE audit scope and Python 3.15.0 runtime boundary.
This REPRODUCTION uses §1's precise imported sources without reproving
algebra. The class checked here is all **yielded values and resumptions**
of generator expressions in local functions entered during `p.request`
followed by `p.input_bounds`. This is not a count of all generator internals:
nested outer iteration, slicing, allocation, set insertion/union, comparisons,
UTF-8 work and other implicit operations retain separate work obligations.

**Conclusion.** There are exactly 17 entered generator-expression sites,
44,548 complete invocations, 57,326 yielded values and 44,548 normal
exhaustions. Every yield matches an independently reconstructed value.
Each invocation has one original observer charge for every yielded value
and one for its terminal resumption. These partition all **101,874** original
`<genexpr>` charges. There is **no additional omitted yielded-item class**
at these sites. Do not add 57,326 again, or subtract the 44,548 terminal
charges: the latter are actual observed resumptions. The partial augmented
source/three-run item totals remain 168,937 and 75,386,624. The earlier
1,615 omitted visits and separate 104,048 character scans are unchanged.
This rules out another yield-hook correction; it does not finish source,
generator-internal or complete preflight accounting.

**Proof and finite verification.** The program
`scripts/four-rule-extraction/audit_job7_source_generators.py` inventories
both entire local ASTs and intersects the inventory with every entered
local function. It retains 19 generator expressions; only the two in
the unentered `exact_equal` helper are excluded. The complete checked table
is below; distinct columns separate the two expressions on line 213.

| module/function; line | invocations | yielded values | original charges |
| --- | ---: | ---: | ---: |
| checker/tree; 18 | 2639 | 5278 | 7917 |
| checker/variables; 31 | 10322 | 12707 | 23029 |
| checker/nodes; 35 | 10322 | 12707 | 23029 |
| checker/_check_stream alphabet types; 69 | 1 | 6 | 7 |
| checker/_check_stream alphabet names; 71 | 1 | 6 | 7 |
| checker/_check_stream references; 84 | 212 | 212 | 424 |
| parameterized_input/check_tree; 115 | 10403 | 12805 | 23208 |
| parameterized_input/request digest; 133 | 1 | 64 | 65 |
| parameterized_input/request names; 141 | 6 | 12 | 18 |
| parameterized_input/request commutator pairs; 153 | 1 | 15 | 16 |
| parameterized_input/request dictionary types; 161 | 21 | 36 | 57 |
| parameterized_input/request references; 184 | 212 | 212 | 424 |
| parameterized_input/size_depth; 207 | 10403 | 12805 | 23208 |
| parameterized_input/input_bounds depth; 213, column 30 | 1 | 213 | 214 |
| parameterized_input/input_bounds nodes; 213, column 66 | 1 | 213 | 214 |
| parameterized_input/input_bounds names; 216 | 1 | 27 | 28 |
| parameterized_input/input_bounds bounds; 218 | 1 | 8 | 9 |

An independent full JSON decode supplies the immutable request, header and
212 records. Explicit stacks reconstruct the LIFO tree-extension sequences,
all formula sizes/depths and the left-to-right syntax-leaf sequence. For
checker `variables` and `nodes`, an independent bottom-up stack computes
each child's variable set and node count from the original JSON trees;
preorder stacks then specify each generator's invocation/yield sequence.
The oracle never calls these checked tree/variable/node functions. The
remaining sequences come directly from all digest/name characters, ordered
alphabet pairs, dictionary originals, references and independently computed
input metrics. All 44,548 invocation lists and 57,326 expected values are
consumed and compared in full, not sampled or reduced to hashes.

The observer calls the original `observe_source` unchanged at every event.
A code object's first usable source position identifies its unique AST
site, including the two line-213 sites. Frame identities track simultaneous
recursive generators. Each `call` must increment the original counter by
exactly one. Every `YIELD_VALUE` return must equal the next independent
expected value with its complete type and contents, including all child
trees and sets. The only other allowed return is normal `None` exhaustion
with no expected suffix; exceptions, extra calls/yields and suspended frames
fail. Thus the observed runtime relation is exactly
resumptions = yielded values + complete invocations at every site. Each
yield has its own preceding charged resumption, so it cannot be a missing
yielded-item visit. This argument says nothing about additional operations
between those events, especially the nested outer loop on line 153.

The entire original observer dictionary equals the original preflight's
dictionary, totaling 167,322 charges. Complete returned request/records and
raw bytes match the independent decode. All eight input metrics and their
original limits match. The complete literal receipt is independently
reconstructed from the source: 212 records, 12,919 formula nodes, 101,314
bytes and rule counts 77 axiom, 77 cut, 18 expansion, 35 association and
5 contraction, with the retained SHA. Byte equality before/after is checked
separately; the digest does not replace any content comparison.

**Evidence and preserved failure.** Complete successful evidence is
`scripts/four-rule-extraction/output-507/repaired/source-generators.json`.
Its entire generator table, AST inventory, entered functions, original
observer, audit budget, literal receipt and input bounds were inspected.
All sequence, exhaustion, charge, input and receipt tests pass. The initial
run had already passed generator checks but requested a nonexistent
`literal_check` field from the original preflight receipt. Its exact program
and failed receipt remain in `output-507/initial-audit-program.py` and
`output-507/source-generators.json`. No mathematical mismatch follows from
that interface failure. The final program instead reconstructs the receipt
from the input and writes only to the fresh `output-507/repaired` directory.

The failed and successful probes consume 2,407,729 and 2,407,741 selected
audit event/item units, totaling **4,815,470 / 100,000,000**. Their measured
durations sum to less than three seconds / 900. Preserved failure, program
snapshot, current program and final receipt total **49,634 bytes** against
the 1,000,000 reserve inside 200,000,000 aggregate evidence bytes. No payload,
temporary replacement or bytecode is written. These units count trace
events and explicit independent AST/JSON/tree/expected-value/comparison
checks; module loading, parsing, reads, oracle container construction,
receipt encoding, index/bit operations and interpreter overhead are not
claimed as an exact total-work or memory bound.

For reproduction use an isolated copy preserving the two initial failure
artifacts but without `scripts/four-rule-extraction/output-507/repaired`,
then run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_job7_source_generators.py`.
The program refuses overwrite, includes the preserved failed-probe units
and artifacts, and checks unchanged CAPS. No production source is modified.

**Remaining scope and Mathlib.** The ready audit continues with implicit
operations, including generator-internal work, and original failed/supplement
accounting. Full parser/read/bit/index, transport/schema/byte/live-peak
verification and all coordinate/equality obligations remain open. The old
partial item total is neither increased by already charged yields nor
accepted as complete. No byte overflow, fitting rank, equality, unrestricted
complexity advance or new algebraic result is claimed. Full matching Mathlib
coverage remains not checked.

### 14. Non-source parser loops and isolated failed load — step 508

**Hypotheses and scope.** Retain §§9–13's fixed inputs, original CAPS and
unchanged ready SPECIALIZE transport-audit assessment. This REPRODUCTION
uses §1's imported mathematics and the assessment's inspected official
Python JSON documentation; no algebraic theorem is reproved. The claim is
about the retained three preflight/supplement programs' explicit direct
parse/metadata calls **outside** `p.request`/`p.input_bounds`. Section 12's
730 source-phase pairs and 104,048 source-phase character scans are excluded.
The original primary program is bound by the manifest's source digest;
complete current program snapshots are preserved for all three programs and
`parameterized_input.py`. No digest substitutes for comparing input contents.

**Conclusion.** Those successful calls perform **482,352 additional
uncharged duplicate-key pair visits**. The augmented original-three-run
partial item count is therefore

    75,386,624 + 482,352 = 75,868,976 < 100,000,000.

This remains an incomplete ledger, not a total verifier-work bound. The
successful strict parses additionally scan **109,721,129 characters** in
the pre-decoder nesting loop. Character scans are a separate measure under
the original receipt's explicit qualification, not item units; exceeding
100,000,000 in this different measure does not prove an item-cap failure.
The preserved failed receipt's isolated strict load is reproducible: it
scans all **18,861 characters**, completes **zero** duplicate-key hooks and
rejects `0.22600599999714177`. This reproduces a nonzero-work failure, but
the original failed program was not preserved. Its entire historical work,
including any work before/after that load, is **UNKNOWN** and is not silently
assigned zero. No byte error, cap overflow, rank or equality follows.

**Proof and finite verification.** Inspect the complete parse-call AST
census in `scripts/four-rule-extraction/output-508/parser-ledger.json`.
The primary program's binding loop explicitly calls `p.parse` on each of
its eight binding files except `proof.jsonl`, hence seven strict parses.
Its source phase is separately traced only later. The accounting supplement
calls its administrative `metadata` helper on `preflight.json` and
`manifest.json`, then `p.load` on event 2642 and the retained-interior
inventory. The inventory supplement loads `accounting-check.json` through
its own metadata decoder and strictly loads the three archive inventories.
These are fifteen successful calls. Calls inside `p.request` are excluded
by scope, not asserted absent; they are already covered in §12. JSON
serialization calls are not decoding calls. The census has no other explicit
`p.parse`, `p.load` or `json.loads` call in these three programs.

`p.parse` first decodes UTF-8, traverses every character to check nesting,
then calls `json.loads` with `p.no_duplicates`, integer-length checking
and float/nonfinite rejection. Every successful scan, and the reconstructed
failure before its decoder rejection, therefore reaches the full text
length. Metadata decoders skip that nesting scan but still call the
same duplicate-key hook. The hook explicitly loops over every supplied
object pair and inserts it into its result. Those traversals are separate
from subsequent walks of the already decoded object. At all the selected
original call sites no source observer is enabled, and the hook has no
`Run.tick`/supplement-visit adjustment. The accounting supplement's walk
increments only its own `visits` after loading; the inventory supplement's
`Run.walk` also starts after loading. Thus neither charges these parse-time
pair traversals. No previous source correction includes these calls.

The full per-call counts and complete aggregate groups were inspected:

| successful original call group | calls | pair visits | strict scan characters |
| --- | ---: | ---: | ---: |
| primary binding | 7 | 233047 | 53935099 |
| accounting metadata (report and manifest) | 2 | 828 | 0 |
| accounting strict event and prior inventory | 2 | 15520 | 1862904 |
| inventory metadata receipt | 1 | 59 | 0 |
| inventory strict archives | 3 | 232898 | 53923126 |
| total | 15 | 482352 | 109721129 |

For example the three large archives have respectively 119,055, 98,331
and 15,512 pairs; their later strict reloading repeats the operations and
must be charged again. The request's binding parse has 91 pairs; its later
source-phase parse is a distinct operation already counted in §12. There
is no duplicate addition of either that source visit or §10's 212 selections.

The audit program `scripts/four-rule-extraction/audit_job7_parser_ledger.py`
independently decodes each complete raw input with its own duplicate-key
hook and applicable numeric restrictions, retaining the ordered key list
for every hook invocation. It then calls the original strict parser or
exact selected metadata-decoder recipe. An audit-only wrapper around
`p.no_duplicates` compares every invocation's length and every ordered key
with the independent sequence, then invokes the original unchanged hook.
Every expected invocation occurs and none extra is allowed. Every complete
successful decoded output is compared recursively, with exact types and
all list/dictionary/scalar values. Thus checking key sequences does not
replace checking values. Raw input bytes are compared before/after every
call; the original files and programs are never changed. This check is
independent of the custom nesting scan and hook, but reuses Python's JSON
decoder; it is not an audit of the C decoder's implementation or operation
count. The character totals follow the inspected explicit scan, not an
inference that every decoder operation is one scan iteration.

For the isolated failed load the independent decoder rejects the exact
saved float token, and the original strict parser raises the exact saved
`Rejected` message with no completed hook. The pre-decoder scan has already
finished. Matching this failure establishes its reproducibility on retained
bytes; it cannot reconstruct the unpreserved historical failing program.
In particular the zero *completed hook* count says nothing about work the
C decoder did on the incomplete outer object before rejecting that token.
The script labels its failure-inclusive item subtotal conditional; it
happens to equal the successful partial subtotal because this reconstructed
failure completes zero pair visits. Neither subtotal includes a complete
historical failed-work cost. No original command was rerun.

**Audit evidence, bounds and reproduction.** All fifteen output comparisons,
all 59,877 hook invocations and their full ordered key checks pass, together
with the separately reproduced failure. The complete per-call/group/AST
census and budget are in
`scripts/four-rule-extraction/output-508/parser-ledger.json`; all these
load-bearing fields, source snapshot identities and qualifications were
inspected. The successful probe uses **46,537,381 / 100,000,000** selected
audit units: 64,143 source-snapshot bytes, 13,232 AST nodes, 17,013,975
independent integer-token checks, 482,352 independent pair checks, 59,877
original-hook invocations, 482,352 key comparisons and 28,421,450 complete
value comparisons. Its measured duration is about **22.55 / 900 seconds**.
This is an audit-event/item measure, not a bound on the reproduced parser's
character iterations, C-decoder, UTF-8, I/O, hashing, allocation, receipt
encoding or bit/index/interpreter work. These remain separately qualified.

The four source snapshots, new audit program and full receipt total
**84,151 bytes**, below the 1,000,000-byte reserve inside the unchanged
200,000,000-byte evidence cap. No payload, bytecode or replacement file is
written. To reproduce use an isolated notebook copy without `output-508`
and run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_job7_parser_ledger.py`.
It refuses output overwrite, pins original CAPS, records a failed receipt
on a caught mismatch, and does not invoke any original preflight command.

**Remaining scope and Mathlib.** The stated explicit parser-call class is
reconciled; the source-phase partial count stays 168,937. Implicit source
operations (including the nested generator's outer iteration and set/copy
work), decoder/UTF-8/read/bit/index costs, complete historical failure and
supplement work, full graph/copy/reference/schema/byte/live-peak audit and
all coordinate/equality obligations remain open. Withhold complete ledger
and transport acceptance. The unchanged ready audit can test those remaining
operations; no mathematical format rejection or unrestricted complexity
progress has been established. Full matching Mathlib coverage remains
not checked.

### 15. Nested outer selections and variable-set operands — step 509

**Hypotheses and scope.** Retain §§9–14's fixed source/request, all original
CAPS, Python 3.15.0 and the unchanged ready SPECIALIZE transport-audit
assessment. This is a REPRODUCTION proof_audit, reusing §1's precise source
imports and the assessment's tracing qualifications; no algebraic theorem
or new representation is introduced. The checked classes are request line
153's nested generator's outer alphabet selections and the literal checker's
`variables` calls, complete ordered child-set operands and returned sets
during the unchanged `p.request` source phase. Other set constructions,
comparisons, serialization and C internals are outside these classes.

**Conclusion.** The nested generator consumes **six additional uncharged
outer alphabet occurrences**, including the last name with an empty suffix.
Its fifteen yielded pairs and sixteen resumptions remain exactly the
already reconciled §13 class; neither is added again. The new partial
augmented source and original-three-run item subtotals are respectively

    168,937 + 6 = 168,943,
    75,868,976 + 6 = 75,868,982 < 100,000,000.

These are not complete work totals. All **12,919** `variables` inputs and
returns, and every ordered child-set return, match an independent
occurrence-based oracle. The complete logical set-volume ledger is:

| class | count |
| --- | ---: |
| nonconstant leaf singletons | 2597 |
| empty constant-leaf sets | 0 |
| internal union calls | 10322 |
| child-set arguments across those calls | 12707 |
| member occurrences across the child-set arguments | 18247 |
| member occurrences across internal union outputs | 16247 |

A member occurring in two arguments counts twice in the input volume.
These set volumes are **not** asserted counts of hash probes, set-table
slots, memory copies, C-loop iterations or bit operations. They are retained
as a separate logical measure and are **not added** to the item subtotals.
Implementation-level set costs remain UNKNOWN. No complete ledger,
transport acceptance, byte error, cap overflow, equality or rank follows.

**Proof: nested generator.** In `parameterized_input.py`, request line 153
updates `expected` from
`(('commutator',(x,y)) for i,x in enumerate(alphabet) for y in alphabet[i+1:])`.
The six names, in order, are `y5,y4,y3,y2,y1,y0`. The outer iteration consumes
each name once; its inner suffix lengths are 5,4,3,2,1,0. Thus there are six
outer item selections and fifteen yielded pairs. The zero-length final
suffix does not remove its outer selection. These are distinct operations
from constructing/yielding the ordered pairs and resuming the generator.

The audit pins this complete AST expression and the entire `variables`
body before tracing. It enables opcode events only for this nested
generator's actual runtime code. Its two `FOR_ITER` instructions have offsets
20 and 56; offset 30 is the first instruction after unpacking the successful
outer `(i,x)`, immediately before loading `alphabet` for the suffix. Every
visit there checks `i` against the next expected index and `x` against the
corresponding immutable input name. All six complete selections and suffixes
are saved in `outer_selections`. The trace observes seven outer iterator
attempts, twenty-one inner attempts (fifteen successful and six exhaustions),
all fifteen ordered yielded pairs and one normal terminal return. There are
exactly sixteen generator resumptions, each with one original observer
charge; all opcode, line and return events there have zero original charges.
The entire original observer dictionary still matches §10, including all
101,874 generator charges and the 167,322 source-phase total.

Section 13 already assigns these sixteen resumption charges to the fifteen
yielded values and terminal resumption. The six outer name selections are
an additional consumed-alphabet class, like the explicit request alphabet
loop but at a different use site. There is no observer hook for the nested
outer iteration, no additional charge at its successful-unpack site and no
later adjustment for it. All six therefore extend the partial item ledger;
do not reassign existing resumption charges or recount the fifteen pairs,
§§10–12's 1,615 corrections or §14's 482,352 parser pairs. Suffix copying,
iterator/enumerate allocation and actual set-update work are not thereby
charged or bounded.

**Proof: complete variable-set reception.** The literal checker's full
`variables` body returns an empty set for constants, a singleton for other
string leaves, and `set().union(*(variables(c) for c in t[1:]))` for an
internal node. It is called on every source formula in source order. The
audit independently decodes all immutable source/request bytes, rejecting
duplicate keys, then constructs an occurrence tree for each formula. It
uses no original `tree`/`variables` function, no child-set unions and no
identity-based merging. It reconstructs tuple syntax and a six-bit mask:
constants have mask zero, original name number i has mask 2^i, and an
internal mask is the bitwise OR of its ordered children's masks. Induction
on the explicitly checked formula syntax identifies the mask's set bits
with precisely its original names: negation retains names and ordered
disjunction takes their union. This is only an independent finite oracle
for the existing source interface, not a new algebraic input.

The oracle is enumerated in preorder, separately for every occurrence of
every formula. On every actual `variables` entry the trace compares the
entire ordered input tuple/string with the next oracle occurrence; missing
or extra calls reject. On return it requires an actual set of strings and
compares all sorted returned names with the mask's complete name list.
A LIFO stack receives every child return and compares the complete ordered
child-set lists with all oracle child masks at the parent's return. Thus
matching only cardinalities or root sets cannot pass. All 12,919 entries
and returns complete, no frame is left active, and there are no exceptions.
The observer charges exactly one call per tree occurrence; this does not
establish the cost of any union's internal implementation.

The receipt retains all 212 per-record ledgers and all 53 occurrence types
`(arity,mask,ordered child masks)` with multiplicities. Every per-record
ledger accumulated from actual returns equals its independently constructed
oracle ledger. Summing those complete entries yields the table above.
There are 7,937 unary and 2,385 binary occurrences, so the argument count is
7,937+2·2,385=12,707=12,919−212, independently consistent with the forest of
212 rooted source trees. Child-set member volume is the sum of the child
mask popcounts over all these occurrences, not the popcount of an aggregate
OR. Internal output volume is the corresponding sum of parent popcounts.
Adding the 2,597 singleton outputs gives 18,844 total returned members,
all compared by the trace. In particular shared names and repeated source
formulas have not been counted just once. No claim that Python must perform
one item visit per logical member is used: specialized set copying/table
scans may have a different implementation-level cost.

**Evidence and resource qualifications.** The program
`scripts/four-rule-extraction/audit_job7_implicit_source.py` checks the full
returned request, records, immutable input bytes, literal receipt and all
independently reconstructed input bounds. The source has 212 accepted
records, 12,919 formula nodes and 101,314 bytes; the goal adds 99 nodes,
giving the existing 13,018-node total and maximum depth 19. The six-name
alphabet, all 21 dictionary entries and every original cap are retained.
The original observer is invoked unchanged at every trace event. Only
`p.request` and `p.input_bounds` are run; no original preflight command or
graph/word/coordinate operation is invoked. Complete source snapshots for
the original primary program, input helper and literal checker, plus the
exact audit program at invocation, survive in `output-509`. The primary
source digest matches the original manifest and the helper bytes match
`output-508`; complete source-text/input-byte equality is also checked before/after
the run. Hashes do not replace any mathematical comparison.

The full receipt is
`scripts/four-rule-extraction/output-509/implicit-source.json`. All complete
new outer selections, yielded pairs, opcode/call counters, the 53-type
census, aggregate counts, snapshots, bounds and failure list were inspected;
every per-record/input/output comparison is performed by the saved program.
There are no failures. Selected audit item/event units are
**2,354,574 / 100,000,000**, including 1,696,547 trace events, 276,871 complete
value comparisons and 18,844 returned-member comparisons; the receipt gives
every other selected category. Measured duration is about **0.85 / 900
seconds**. Program, snapshots and receipt total **143,052 bytes**, below
the 1,000,000-byte reserve inside the unchanged 200,000,000-byte cap.
These selected audit units do not bound the reproduced program's C/decoder,
read/UTF-8/hash/allocation/index/bit work or total interpreter resources.

For reproduction use an isolated notebook copy without `output-509` and run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_job7_implicit_source.py`.
It refuses overwrite, pins CAPS/runtime/source bodies, checks the event/item
budget before each selected unit and checks time periodically and before
receipt writing. A caught mismatch saves its traceback and current budget;
original archives are never overwritten. The finite evidence reserve includes
the invocation snapshot as well as the live audit program. No replacement
payload or bytecode is written.

**Remaining scope and Mathlib.** Nested outer selections and logical
variable-set operands are reconciled only in the stated sense. Other source
set constructions (`fields`, repeated alphabets and expected/seen sets),
container/equality/serialization costs, actual set implementation work,
decoder/read/bit/index costs, complete original failed/supplement work and
full independent transport/schema/framing/byte/live-peak audit remain open.
In particular original historical failure work remains UNKNOWN; this run
does not reconstruct it. Withhold full preflight acceptance and coordinate
experiments. All prior source/scan corrections and failure evidence remain
unchanged. This is local finite audit evidence, not progress beyond the
imported algebra or a result on unrestricted P versus NP. Full matching
Mathlib coverage remains not checked.

### 16. Remaining source set operands and typed encodings — step 510

**Hypotheses and scope.** Retain §§9–15's immutable source/request, original
CAPS, Python 3.15.0 and unchanged ready SPECIALIZE transport-audit assessment.
This REPRODUCTION proof_audit reuses §1's mathematical imports and the
assessment's inspected JSON/tracing documentation. No new algebra, encoder
format or source theorem is proposed. The checked classes are non-variable
built-in `set` calls in `p.fields`, `p.request` and checker `_check_stream`,
the stored request dictionary sets, and every `p.typed` call. Section 15's
variable unions, prior parser/loop classes and the checker's default JSON
roundtrip are not recounted or certified by these checks.

**Conclusion.** All **236** schema calls return successfully on their full
independently bound inputs; all **1,114** selected built-in `set` calls have
the expected operands; all **213** actual `check_tree` alphabet sets and
**86** dictionary-state checkpoints match their complete expected contents.
All **50** `p.typed` arguments and complete results match an independent
restricted-domain encoder. Their outputs total **3,994 ASCII bytes**.
The selected set constructors have **4,661 logical input-member occurrences**.
These are finite interface checks, not implementation-level operation counts.

There are zero original observer charges at the constructor CALL opcodes,
or at any event inside `fields` and `typed`. This supplies a further precise
witness to missing direct source-set/serialization accounting. It does not
show that one item unit must be added per call, operand member or output
byte. The partial source/original-three-run item subtotals therefore remain
**168,943 / 75,868,982**. Actual set-table, hash, split, comparison, sorting
and encoder costs remain UNKNOWN; complete administrative acceptance stays
withheld. No overflow, byte error, rank or equality follows.

**Proof: source binding and constructor census.** The program
`scripts/four-rule-extraction/audit_job7_source_sets_serialization.py`
independently decodes the complete original request and all 213 source
lines, rejecting duplicate keys. Full preflight/helper/checker source bytes
equal the preserved §15 snapshots; the preflight digest also matches the
original manifest. Sources and raw inputs are checked unchanged after the
run. Digests do not replace full input/argument comparisons.

An AST census identifies every named `set(...)` expression in the three
selected functions, excluding `variables`. Runtime opcode tracing maps each
CALL's full source position to that census; no original function is replaced.
At each selected CALL it receives the complete dictionary-key/list operand,
or reconstructs the exact `keys.split()` list from the checked `fields`
argument, or records the empty operand. `_check_stream`'s full decoded header
and each record equal the independent raw-byte objects; helper schema entries
are likewise checked in complete call order. The observed groups are:

| function/site | calls | logical input members |
| --- | ---: | ---: |
| fields 31, `set(x)` | 236 | 730 |
| fields 31, `set(keys.split())` | 236 | 730 |
| request 143, distinct alphabet | 1 | 6 |
| request 144, goal alphabet | 1 | 6 |
| request 154, empty seen/names | 2 | 0 |
| request 185, source alphabet | 212 | 1272 |
| checker 66, header keys | 1 | 3 |
| checker 71, distinct alphabet | 1 | 6 |
| checker 79, record keys | 212 | 636 |
| checker 82, variable-test alphabet | 212 | 1272 |
| total | 1114 | 4661 |

The 236 schema calls consist of request, dictionary, 21 placeholders, header
and 212 records. Their key counts sum to 5+2+21·4+3+212·3=730.
Every schema argument equals its independent expected object and every
required-key list equals that object's keys as a set. Each actual call
returns None without an exception. Every `check_tree` entry receives the
exact independent formula and a set containing precisely the six names;
all goal/source entries occur. Temporary constructor results are not
inspected on the interpreter stack: the proof uses the pinned expressions,
their complete inputs, ordinary built-in set semantics, successful program
conditions and, where retained, the checked stored sets. It does not claim
an independent implementation audit of Python's set operations.

The table excludes the checker's 213 three-key set literals and the
request's initial Boolean set comprehension. Their contents follow the
unchanged expressions; they must not silently disappear from future C-work
accounting. The initial Boolean set is checked before update. Complete
`expected`, `seen` and `names` contents are then checked at all 22 dictionary
loop-header visits, before each of 21 name additions, before and after each
of 21 association additions, and at the final coverage comparison: 86
checkpoints. Expected associations are independently enumerated by the six
single names and index pairs i<j. At placeholder index j, `names` contains
exactly the preceding j names before its addition and j+1 afterwards;
`seen` similarly changes from j to j+1 at its addition. Each comparison is
of full sorted contents, not cardinalities alone. The two final sets contain
all 21 associations/names. No update/yield, nested outer selection or union
volume from §§13,15 is added again.

**Proof: typed serialization.** Complete execution order is two dictionary
alphabet encodings, two polynomial encodings per placeholder (42), four
header alphabet/goal encodings, and two final-endpoint encodings: 50 calls.
For every call the audit compares the full argument with the independent
expected value; for every return it compares the entire resulting string
with its own encoder. The observed domain consists solely of lists and
strings whose characters lie in ASCII 32–126 and exclude quote/backslash;
the independent encoder checks this restriction at every character. It
surrounds each string by quotes and joins recursively encoded list children
with commas inside brackets. Therefore there are no unhandled escapes,
non-ASCII characters, object key ordering, scalar types or whitespace cases
in this domain. Induction over these actual finite lists/strings proves
that this is exactly the compact `ensure_ascii=True` encoding used by
`p.typed`; `sort_keys=True` has no effect because there are no dictionaries.
This justifies the specialized comparison without reproving a general JSON
encoder theorem. All 50 full strings agree, with aggregate ASCII/UTF-8
length 3,994. This receives these fixed calls only; it neither validates the
large transport chunk encoder nor bounds C-encoder/sorting/allocation work.

The original observer remains active unchanged at every trace event. Its
entire dictionary and 167,322 source-phase total equal the original receipt.
Opcode-site charges are zero for all 1,114 constructors; all call/line/return
charges inside `fields` and `typed` are zero. The observer has no hook for
these functions or C constructor/serializer loops. These facts identify
missing direct coverage, not the exact internal work or a new additive item
correction. Already charged surrounding traversals retain their earlier
interpretation; logical set volumes and JSON output lengths remain separate.

**Evidence, bounds and reproduction.** The full receipt is
`scripts/four-rule-extraction/output-510/source-sets-typed.json`, with every
constructor operand, schema call, dictionary checkpoint and typed argument/
result, complete AST/group census, original counters, runtime and bounds.
The full group/census/charge/budget fields were inspected; a read-only
postrun reconciliation checks all schema entries, typed results, set-group
totals and dictionary states, not sampled entries. No failures occurred.
The main probe uses **2,088,718 / 100,000,000** selected audit item/event
units and about **1.47 / 900 seconds**. Its program, invocation snapshot,
three source snapshots and receipt total **304,510 bytes**, below the
1,000,000-byte reserve inside 200,000,000. These are the probe's selected
units, not a total bound including C internals, pre/postrun tool reads,
the uninstrumented postrun reconciliation or interpreter/bit/index work.
No fresh graph regeneration or original preflight command is invoked.

For reproduction use an isolated notebook copy without `output-510` and run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_job7_source_sets_serialization.py`.
It refuses overwrite, retains all original caps, checks the selected budget
before each charged unit, checks time periodically/before writing, and saves
a complete traceback and partial new ledgers on a caught mismatch. There
are no failed prefixes from this invocation and no payload/bytecode writes.

**Remaining scope and Mathlib.** This is local finite source-interface
evidence and a further administrative-coverage negative, with no progress
beyond imported algebra. Actual set/container/equality/serialization costs,
the checker default roundtrip, read/decoder/hash/bit/index work, complete
historical failure/supplement work, full independent graph/copy/reference/
dictionary/gadget/comparison reception, strict transport schemas, byte/framing
and live peaks remain open. Temporary set outputs are qualified above.
Coordinates, all equalities, later jobs and all unrestricted complexity
gaps remain unresolved. Full matching Mathlib coverage is not checked.

### 17. Checker default JSON interfaces — step 511

**Hypotheses and scope.** Retain §§9–16's complete immutable source/request,
original CAPS, Python 3.15.0 and unchanged ready SPECIALIZE critical-audit
assessment. This REPRODUCTION proof_audit uses the existing §1 imports and
the assessment's inspected JSON/tracing documentation; no mathematical
theorem is reproved. It checks the default JSON roundtrip in the actual
`check_bytes` invocation and every default `json.loads` call made directly
by the literal checker. Previously received strict helper parses, typed
encodings, loops and sets are not recounted. Legacy `check(path,expected)`
is not invoked or certified. Nothing here receives the transport encoder.

**Conclusion.** The fixed invocation makes exactly **one default dump and
214 default loads**, all returning their complete expected values. The
roundtrip encodes the actual non-leaf request goal to **818 ASCII bytes**,
decodes it to the same complete JSON tree, normalizes it, and passes the
correct tuple/string tree to `_check_stream`. The other 213 decodings receive
the exact binary source lines: header and all 212 records, retaining LF
framing. Their full inputs/outputs agree with independently parsed original
bytes. Aggregate default-decoder input length is

    818 + 101,314 = 102,132 ASCII bytes.

All observed call/line/return events inside these selected `dumps`/`loads`
functions have **zero direct original observer charges**. That supplies a
further finite administrative-coverage witness; encoder/decoder C work,
allocations and actual comparison costs remain UNKNOWN. These logical byte
volumes are neither item-visit corrections nor measured C-operation counts.
Partial source/original-three-run items stay **168,943 / 75,868,982**.
No full administrative acceptance, byte error, overflow, rank or polynomial
equality is established. P versus NP and the independent gaps of §7 remain open.

**Proof: immutable binding and independent finite parsing.** The program
`scripts/four-rule-extraction/audit_job7_default_json.py` preserves complete
preflight/helper/checker source snapshots, compares their bytes with §16's
snapshots, checks the preflight digest against the original manifest, and
checks all source/input bytes unchanged after execution. It executes only
the unchanged `p.request` and `p.input_bounds` under observation, not the
original full preflight. The actual `check_bytes` entry must receive precisely
the independently read immutable source bytes, the complete request goal
and the unchanged 2,000,000-byte source cap. Digest checks supplement these
full comparisons rather than replacing them.

An independent recursive parser, which never calls `json.loads`, consumes
the entire request and each of the 213 binary source lines. It accepts only
ASCII whitespace, strings of ASCII characters 32–126 without backslashes,
unsigned decimal integers without leading zeros, lists and dictionaries
with unique string keys; all other lexical cases and trailing characters
are rejected. It checks the original JSON-depth ceiling before descent.
This restricted domain suffices for every complete actual input. Each
successful string branch consumes its opening/closing quotes and all
interior characters; each number branch consumes exactly its digits;
list/object branches enforce every colon, comma and closing delimiter
and recursively receive every value. Thus structural induction over the
successful parses identifies their objects with these exact finite JSON
texts. This is a finite-domain applicability check, not a replacement
general JSON theorem or a claim about Python decoder internals.

The independent goal encoder accepts only the actual string/list domain,
checks every string's safe ASCII characters excluding quote/backslash,
quotes strings and joins array children with default `, ` separators.
No dictionary, number, escape or non-ASCII case occurs in the goal. Induction
over its finite arrays proves agreement with default JSON encoding on this
domain. The observed complete encoder string equals that independent
string, of length 818; the compact typed encodings in §16 are a different
interface. A separate recursive formula normalizer checks `not`/`or` arities
and legal leaves and returns ordered tuple/string trees. The actual goal
has 99 formula nodes. Its result is compared type-sensitively with the
actual normalized `_check_stream` argument; no leaf-goal assumption is used.

**Proof: complete interface order and default arguments.** Observation
selects Python `json.dumps`/`loads` frames whose immediate caller is the
original checker file. All encoder defaults are checked, including
`skipkeys=False`, `ensure_ascii=True`, `check_circular=True`, `allow_nan=True`,
`sort_keys=False`, None class/indent/separators/default and empty keyword
arguments. All decoder hooks/class are None and its extra keyword arguments
are empty. The complete selected sequence is:

1. `check_bytes` line 53 dumps the complete request goal.
2. That same line loads exactly the entire returned string.
3. `_check_stream` line 65 loads the exact complete binary header line.
4. `_check_stream` line 78 loads each of the 212 complete binary record
   lines, in original order, without removing their LF terminators.

Each entry records its whole argument and defaults, each return records
its whole result and compares it type-sensitively with the independent
expected value. Frame identities pair all entries/returns; exceptions or
extra/missing calls reject the check. The decoded roundtrip is observed
entering `tree`, and the independently normalized result is observed
entering `_check_stream`. All 215 returns occur and no selected frame is
left pending. The returned request, raw bytes and all rows equal the
independent originals; the literal receipt accepts 212 records and retains
the original source digest and caller binding. This receives interfaces,
not a separate proof of every checker primitive or internal JSON operation.

The original source observer is called unchanged at every trace event. Its
entire dictionary agrees with the original preflight receipt and its total
is again 167,322. The selected `dumps`/`loads` call/line/return deltas are
all zero: the observer filters checker/helper events, not these JSON frames.
Already charged surrounding tree calls retain their previous meaning.
Absence of direct charges does not quantify unobserved C loops, imply an
additive correction per call/byte, or show that all surrounding work is free.

**Failure preservation and complete evidence.** The first probe incorrectly
assumed the goal was the leaf `false` and stopped before observation. Its
full program and failure survive in `output-511/default-json.json` and its
adjacent program snapshot: 234,432 selected units, 28,851 charged program/
snapshot/receipt bytes. This is a probe error, not a source/contract failure.
The corrected program uses the complete independent formula normalizer and
fresh `output-511-repaired`; it does not overwrite the failed evidence or
change production sources, CAPS, representation or accepting predicates.

Complete successful arguments, strings, decoded objects, defaults, callers,
returns, charges, source snapshots and bounds are saved in
`scripts/four-rule-extraction/output-511-repaired/default-json.json`.
Including the failed probe it reports **2,275,836 / 100,000,000** selected
audit units and **414,532** charged evidence bytes. The separate program
`scripts/four-rule-extraction/check_job7_default_json.py` reads **every**
interface record and compares every original framed input, full output,
default, caller, index and return flag. It uses `ast.literal_eval` as a
separately implemented parser for the already established actual lexical
domain; it does not claim general equivalence of Python literals and JSON.
It also checks all source snapshot bytes, complete observer/default-charge
dictionaries, caller digest, deliveries and budget sums. Its full PASS
receipt is `output-511-repaired/receipt-check.json`; there are no additional
failures or rejected writes. Across both probes and this reconciliation the
selected total is **2,569,598 / 100,000,000** units, about **0.86 / 900**
measured seconds and **443,441** charged program/snapshot/receipt bytes,
below the 1,000,000-byte reserve inside 200,000,000. Evidence charging
conservatively retains the initial probe's executable-program allowance
even though its old version now survives only as its saved snapshot.

These selected ledgers include the saved failed probe, corrected probe and
reconciliation. They exclude uninstrumented C/parser/encoder, hashing,
allocation, tool reads, I/O and bit/index/interpreter costs; those are not
asserted zero or bounded by this timing. No fresh graph generation,
coordinate search, path-word operation, payload file or bytecode is produced.
To reproduce, use an isolated notebook copy without either output-511
directory. Preserve the corrected program separately, install the saved
initial snapshot at `scripts/four-rule-extraction/audit_job7_default_json.py`
and run it there; then restore and run the corrected program at that same
path, followed by the reconciliation. Use `PYTHONDONTWRITEBYTECODE=1`.
Every output is exclusive and the failure remains a required input to the
corrected run's cumulative accounting.

**Remaining scope and Mathlib.** This is local finite interface reception
and further quantified missing direct observer coverage, with no progress
beyond imported algebra. Actual C/container/equality/serialization work,
read/hash/bit/index costs, complete historical failure/supplement work,
full independent graph/copy/reference/dictionary/gadget/comparison reception,
strict transport schemas, byte/framing and live peaks remain unresolved.
Default JSON argument/result uncertainty is removed only for these actual
calls; its internal cost remains UNKNOWN. Coordinates, all equalities,
later jobs and unrestricted complexity gaps remain open. Full matching
Mathlib coverage is not checked.

### 18. Literal formula-comparison operands and Boolean delivery — step 512

**Hypotheses and scope.** Retain §§9–17's fixed immutable source/request,
original CAPS, Python 3.15.0 and unchanged ready SPECIALIZE transport-audit
assessment. This REPRODUCTION proof_audit reuses §1's precise mathematical
imports, L108 §13's immutable-byte boundary and the assessment's inspected
tracing qualifications. No algebraic theorem is reproved. The selected
class consists of both `_check_stream` endpoint comparisons and all executed
formula equalities in its primitive predicates. Scalar tag/operator tests,
set/container operations, helper comparisons, JSON internals and the legacy
path checker are outside this class. This is a finite operand/result audit,
not a fresh acceptance proof for arbitrary checker inputs.

**Conclusion.** All **291** executed selected comparisons receive their
complete correct operands and Boolean results, and all **212** primitive
predicates return true. The two endpoint inequalities are false; all 289
primitive formula equalities are true. Selected comparison-opcode events
have **zero direct original observer charges**. A full structural reference
comparator visits **23,631 paired nodes**, and the two complete operand
volumes sum to **47,262 nodes**. Here a tuple and each of its entries,
including operator-name strings, are nodes; this is not the checker's
formula-node convention. These are explicitly defined logical volumes,
not actual C tuple/string comparisons, hash probes, interpreter instructions
or additive corrections to the original item ledger. The source and
original-three-run partial item subtotals remain **168,943 / 75,868,982**.
Actual C comparison costs remain UNKNOWN. No complete transport acceptance,
byte error, cap overflow, coordinate rank or polynomial equality follows.

**Proof: complete operand binding.** The audit program
`scripts/four-rule-extraction/audit_job7_source_equalities.py` compares the
entire preflight/helper/checker sources with the received step-511 snapshots,
preserves fresh snapshots and checks the original manifest's preflight
digest. It independently reads the full immutable source/request, checks
their caller digest, and compares complete `ast.literal_eval` and JSON
parses with duplicate-key rejection. It rechecks the actual no-backslash
ASCII lexical domain and string/unsigned-integer/list/object value domain.
On this domain these parser syntaxes have the same strings, integer values
and container structure; no general Python-literal/JSON equivalence is
assumed. An independent recursive normalizer checks every formula's
operator/arity and converts it to tuple/string syntax, without invoking
the checker's `tree`. Each row's actual normalized formula, selected
reference formulas, reference indices and primitive tag equal these
independent immutable inputs in full, in source order. The normalized
caller goal and the complete header-normalization return are also received.

The ten-site AST census comprises checker lines 73, 92 (the formula
comparison), 94, 96, 98 (the formula comparison), 100, 105, both formula
comparisons on 110, and 118. Lines 94/96 have no executions on this source.
Each full AST source position matches precisely one runtime `COMPARE_OP`
instruction. At every executed selected opcode, a restricted operand
expression interpreter reads names, constants, tuple construction and
subscripts from actual frame locals. The header's call operand uses its
already observed complete `tree` return, not another call to `tree`.
The same operand expressions on independent source/reference environments
give type-sensitive, fully compared equal values. There is no evaluation
of arbitrary code or access to an interpreter value stack.

**Proof: receiving actual results.** After the selected opcode, the trace
allows only `COPY`, `TO_BOOL` and `EXTENDED_ARG` before the result is either
stored in `ok` or consumed by `POP_JUMP_IF_FALSE`. For a store, the next
opcode event reads the actual Boolean local; for a conditional jump, the
next opcode offset identifies whether its false target was taken. Every
result agrees with the explicit structural reference comparison, negated
for the endpoint inequalities. No selected result remains pending, and
an unexpected intermediate instruction, exception, missing/extra call or
non-Boolean delivery rejects the probe. At each row's `if not ok`, the
actual value is independently received as true, in complete record order.
This checks actual branch/store delivery rather than inferring success
solely from a final receipt or recomputing a hypothetical predicate.

The complete execution groups are:

| site | comparisons | left operand nodes | right operand nodes | reference paired nodes |
| --- | ---: | ---: | ---: | ---: |
| header endpoint, 73 | 1 | 180 | 180 | 180 |
| axiom, 92 | 77 | 4234 | 4234 | 4234 |
| expansion, 98 | 18 | 1708 | 1708 | 1708 |
| contraction, 100 | 5 | 1098 | 1098 | 1098 |
| association, 105 | 35 | 4073 | 4073 | 4073 |
| two ordered cut comparisons, 110 | 154 | 12158 | 12158 | 12158 |
| final endpoint, 118 | 1 | 180 | 180 | 180 |
| total | 291 | 23631 | 23631 | 23631 |

All operands are equal as tuple/string values, including the endpoints
whose comparison operator is inequality. The reference comparator recursively
compares types, lengths and every paired tuple entry without identity
shortcuts, so its paired-node count equals either full operand volume here.
Python's actual C comparator can use different short circuits and identity
tests. The stated logical counts therefore give no actual C operation total.

The original observer is called unchanged at every event. Its complete
dictionary matches step 502 and its source total remains 167,322. It has
no opcode charge or explicit formula-comparison loop charge: every selected
opcode delta is zero. Already charged source-record/tree/reference visits
retain their earlier meanings. This is further evidence against treating
the original observer as a total-work bound, not a justification for adding
23,631 or 47,262 to its item subtotal.

**Failure, independent reconciliation and bounds.** The first probe enabled
opcode tracing only at the selected frame's call event. It received all 212
primitive outcomes but zero comparison-opcode records and correctly rejected
its own completeness assertion. Its original program, complete failure and
partial census survive in `scripts/four-rule-extraction/output-512/`:
**2,079,438** selected units and **104,038** charged bytes. This is an audit
instrumentation failure, not a checker or transport counterexample. The
corrected program follows the prior probes by reasserting opcode tracing
on selected frame events, uses fresh `output-512-repaired`, and preserves
the first attempt's selected work/time/evidence in its cumulative ledger.
No production source, cap or accepting predicate changes.

The complete successful receipt, including every full operand, Boolean
delivery, AST/opcode census, outcome, group and original observer, is
`scripts/four-rule-extraction/output-512-repaired/source-equalities.json`.
The separate `check_job7_source_equalities.py` reconstructs the full ordered
291-record sequence directly from immutable source formulas and references,
using list encodings of the received tuple/string domain and direct
rule-specific operand constructors, not the probe's expression interpreter
or any checker function. It compares every operand/result/delivery flag,
all 212 primitive outcomes, complete groups, volumes, source snapshots,
caller digest, original observer and selected budget sums. Its complete
`receipt-check.json` is PASS. Neither record sampling nor a receipt preview
is used to establish the result.

The failed probe, corrected probe and reconciliation together use
**4,637,294 / 100,000,000** selected item/event units, approximately
**1.65 / 900 seconds**, and **504,635** charged executable/snapshot/receipt
bytes below the **1,000,000-byte** reserve within the unchanged
**200,000,000-byte** evidence allowance. The charge conservatively retains
the first executable allowance even though that old version now survives
as its saved snapshot. No payload, bytecode, graph or word file is written.
Uninstrumented parser/C, allocation, hashing, I/O, tool-read and bit/index/
interpreter work remains unbounded by these selected counters or timings.

For reproduction use an isolated notebook copy with neither output-512
directory: preserve the corrected program, run the initial saved
`output-512/audit-program.py` version at the original audit-program path,
then restore and run the corrected version followed by the reconciliation.
Use `PYTHONDONTWRITEBYTECODE=1` and preserve the required failed output.
All writes are exclusive; complete caught failures are retained.

**Remaining scope and Mathlib.** This is finite administrative evidence,
with no progress beyond the imported algebra. Formula operands/results are
received only for this invocation. Source helper/container/hash/read costs,
actual comparison and all other C/bit/index costs, complete historical
failed/supplement work, independent graph/copy/reference/dictionary/gadget/
comparison regeneration, strict transport schemas, byte/framing and live
peaks remain unresolved. Coordinate evidence, all polynomial equalities,
later jobs, whole Boolean/K/H/nonzero-fJ, availability, L087 W₂ and
unrestricted ER/Frege/SAT remain open. Full matching Mathlib coverage is
not checked. Withhold full acceptance and continue only the approved audit.

### 19. Remaining scalar-helper arguments and normal returns — step 513

**Hypotheses and scope.** Retain §§9–18's immutable source/request, exact
CAPS, Python 3.15.0 and unchanged ready SPECIALIZE transport-audit assessment.
This REPRODUCTION proof_audit uses §1's precise imported mathematical
results and the already inspected JSON/tracing documentation. It checks
all actual calls to the helper module's `require`, `bound`, `name` and
`integer` during the original `request` followed by `input_bounds`.
Previously received parser, tree, set, JSON and formula interfaces remain
inputs; their internal costs are not newly certified. No general theorem
is reproved, production code changed or graph/coordinate/word run invoked.

**Conclusion.** Every selected helper call returns normally with the
specified result. The complete counts are:

| helper | calls and matched returns | received argument/result |
| --- | ---: | --- |
| `bound` | 39,918 | every ordered (actual, key, stage) equals the independent input-derived sequence; returns None |
| `require` | 68,518 | every actual condition is the Boolean True; returns None |
| `name` | 2,642 | every ordered name equals its independent input-derived value; returns None |
| `integer` | 212 | every ordered argument equals the corresponding source reference; returns True |

All 111,290 call/return pairs are matched, with no pending frames, extra
arguments or failures. Every selected call, line and return event has zero
direct original observer charges. The original source observer's entire
dictionary and 167,322 total are unchanged. These are logical dispatches,
not actual internal operation counts or automatically additive item visits.
The partial source/original-three-run item totals stay **168,943 /
75,868,982**. There is no new byte error, cap overflow, rank/equality verdict
or result beyond the imported mathematics. Full acceptance remains withheld.

**Proof: fixed bytes and independent argument construction.** The program
`scripts/four-rule-extraction/audit_job7_source_helpers.py` checks complete
preflight/helper/checker source bytes against the preserved §18 snapshots,
retains new complete snapshots, and additionally checks the original
preflight manifest digest. It independently loads the original request and
all 213 physical source JSON lines, rejects duplicate keys, compares every
decoded value with `ast.literal_eval`, and checks the caller digest. It
checks full source/input bytes unchanged after the actual invocation too.
Digests supplement, rather than replace, complete value/byte comparisons.
The decoder is a reused interface, not a new proof about its C internals.

The independent bound plan follows the pinned helper's source order:
request read/stat bounds and JSON nesting; alphabet length and names; goal
tree; dictionary cardinality and placeholder names; first source read/stat;
header and all record parses; each record's references, tree and aggregate
node bound; and the second source read/stat. `input_bounds` adds no calls
to `bound`, `name` or `integer`; its single `require` is still received.
No caller-controlled alternative path or legacy checker is substituted.

For nesting, the plan verifies all actual characters are ASCII printable
characters or tab/CR/LF and that no backslash occurs. Toggling quote state
at every quote therefore identifies exactly the string intervals. Brackets
inside strings have no effect; each opening bracket/brace outside them
increments the independent depth and generates the next expected nesting
bound; each closing delimiter decrements it. Complete decoded JSON values,
final depth zero and unquoted termination retain the successful syntax
boundary. This finite no-escape specialization justifies this simpler
scanner; it is not a general replacement parser. There are exactly 11,020
container openings over the request, header and all records.

For each formula the plan recursively visits children in reverse order,
starting at depth one. This equals the original `check_tree` LIFO order:
its children are pushed in forward order and therefore popped in reverse
order, with each complete child subtree exhausted before the next. Induction
over the finite formula establishes equality of the visit order, depths
and running local node count. Each visit supplies its depth and local node
bounds; each leaf supplies its original name and UTF-8 name-byte bound.
The actual `not`/`or` arities and leaf alphabet are independently checked.
After each source tree, its node count is added to the retained goal/source
aggregate, generating the next expected aggregate bound. Ordered reference
arguments are enumerated directly from each immutable row; every one is
an integer between zero and that row's index minus one.

The complete bound groups are:

| resource/stage | calls | actual range | required maximum |
| --- | ---: | ---: | ---: |
| request stat/read, each | 1 | 2,947 | 2,000,000 |
| source stat/read, each | 2 | 101,314 | 2,000,000 |
| JSON nesting | 11,020 | 1–19 | 160 |
| alphabet length | 1 | 6 | 256 |
| name bytes | 2,642 | 2–4 | 4,096 |
| formula depth | 13,018 | 1–19 | 64 |
| local formula nodes | 13,018 | 1–234 | 100,000 |
| dictionary cardinality | 1 | 21 | 32,896 |
| aggregate goal/source nodes | 212 | 105–13,018 | 100,000 |

The two read rows represent six bound calls, not three. Total names are
2,615 formula leaves plus six alphabet entries plus 21 placeholder names.
The 13,018 formula nodes comprise 2,615 leaves and 10,403 internal nodes.
These are input-derived checks of existing quantities, not fresh additive
source-item charges; parser/tree traversal coverage remains as qualified
in earlier sections.

**Proof: every actual delivery and its coverage boundary.** An AST census
retains every direct call site for the four helper names in the complete
unchanged helper source, including unexecuted sites. The tracer sees all
actual frames with that file and one of the selected function names. At
each call it requires exactly one matching source call-site interval,
records caller/function/line counts, and retains the live frame pairing.
`bound`, `name` and `integer` arguments must equal the next independent
expected value type-sensitively and in full; exhaustion, extra calls and
wrong types reject the receipt. Every `require` condition must be exactly
True as a Boolean. For requirements invoked by `bound`, the entire
diagnostic dictionary must equal its caller's actual stage, actual, limit
and resource. Other requirement expressions are received as actual Boolean
arguments; this is not an independent rederivation of every upstream
predicate or its internal work. On each normal return the frame must match
an active call and return None, or True for `integer`. Exceptions reject
the probe. At completion every argument sequence and call frame is exhausted.

The unchanged original observer is invoked at every trace event. Its helper
call/line/return deltas are all checked separately and are zero: its filters
do not charge these functions. Already charged surrounding loops/generators
and argument-evaluation traversals keep their prior meanings. In particular
the 39,918 nested `require` calls made by `bound` are included in the 68,518
total requirements; they are not another item correction. Receipt of these
interfaces neither measures C/container/read/hash work nor converts helper
dispatches into a bit-model bound.

**Independent reconciliation, evidence and limits.** The full aggregate
receipt and all executable/source snapshots are in
`scripts/four-rule-extraction/output-513/`; the receipt is
`source-helpers.json`. Full argument sequences need not be stored as another
large log: the unchanged raw inputs and saved executable reconstruct every
expected value, and the actual complete sequence is compared during the
run. The receipt retains every caller-site count, bound group's actual and
required range, name frequency, all 212 integer arguments, returns, direct
charges, original observer, budgets and failure list. No sample is used.

The separate `check_job7_source_helpers.py` reconstructs aggregate counts
by another method. It traverses decoded JSON values to count containers and
their maximum depth, rather than scanning characters; it recursively visits
formula children in forward order to count sizes, depths and leaf-name
frequencies, rather than reproducing the LIFO sequence. The no-escape input
domain and successful parse justify equating container counts to the earlier
scanner's bound invocations. It reconstructs every actual caller-site count
from those counts and the fixed source control flow, every bound group's
range, full name frequencies and ordered reference list. It compares all
call/return counts, the complete original observer, charges, snapshots,
retained qualifications and budget sums. The complete `receipt-check.json`
is PASS. This reconciliation checks the summary of the exhaustive observed
sequence; it does not retrospectively observe a new execution.

The probe uses **2,435,489** selected units; the independent reconciliation
adds **349,493**, for **2,784,982 / 100,000,000**. Total conservatively
charged programs, snapshots and receipts are **126,038 / 1,000,000 bytes**
inside the unchanged **200,000,000-byte** evidence allowance. Measured
time is below **2 / 900 seconds**. No failure, payload, bytecode or replacement
file is produced. Read/parser/C, allocation, serializer, hashing, tool-read,
I/O and bit/index/interpreter work remain outside these selected counters
and timing is not an operation bound.

For reproduction use an isolated notebook copy without `output-513`, with
the unchanged inputs and §18 snapshots. Run, with
`PYTHONDONTWRITEBYTECODE=1`, first
`python3 scripts/four-rule-extraction/audit_job7_source_helpers.py`, then
`python3 scripts/four-rule-extraction/check_job7_source_helpers.py`.
Writes are exclusive, caps/runtime/source bytes are pinned, selected units
and times are checked, and caught failures preserve full tracebacks and
partial new ledgers. Original archives are never overwritten.

**Remaining scope and Mathlib.** Close this scalar-helper interface subtask
only. Do not subdivide it into more interface probes: actual internal costs
and incomplete historical failed/supplement work remain open and are parked
while the approved audit proceeds to independently test transport and bytes.
Full graph/copy/reference/dictionary/gadget/comparison regeneration, strict
transport schemas, byte/framing and live peaks remain unfinished. Actual
ranks/coordinates, all polynomial equalities, later jobs, full Boolean/K/H/
nonzero-fJ, availability, L087 W₂ and unrestricted ER/Frege/SAT remain open.
This is local finite administrative evidence; full matching Mathlib coverage
is not checked. There is no new mathematical dependency or P-versus-NP claim.

### 20. Independent complete JSON sizing and endpoint framing — step 514

**Hypotheses and scope.** Reuse the unchanged ready SPECIALIZE assessment
`drafts/literature/2026-10-26-job7-transport-preflight-critical-audit.md`,
the eight fixed binding inputs, original CAPS, and §6's format. This is
REPRODUCTION / proof_audit. The graph constructor is reused, not independently
proved correct here. The separate encoding/counting test supplies a finite
input toward the audit, not full transport reception or an equality verdict.
Primary citations and qualifications remain §1; no algebraic theorem is
reproved. The implementation source is the Python JSON documentation
identified, with its patch-version limitation, in the approved assessment.

**Complete count and correspondence of measured objects.** The audit program
`scripts/four-rule-extraction/audit_job7_wire_encoding.py` regenerates the
unchanged primary constructor in fresh `output-514-repaired/regenerated/`.
Its original serializer still measures all sections. At each of B_bind and
B_trans, a separate recursive traversal receives every container, key and
value and rejects types outside dict/list/string/int/bool/null, with string
keys. A separate `json.JSONEncoder(ensure_ascii=True, separators=(',', ':'),
allow_nan=False, check_circular=True).iterencode(value)` then visits the
complete same object. Every emitted fragment is checked to be ASCII, and
its full character length is added. ASCII makes that length exactly its
UTF-8 byte length. No prefix, digest or sample substitutes for the remaining
fragments. Encoder traversal/punctuation are independent of `Run.chunks`;
the implementations share Python's scalar escaping routines, so this is
not an independent proof of the JSON runtime itself.

By the encoder's compact-JSON semantics, each count includes all object/list
punctuation, names, escaped literal contents and repeated objects. The
original chunk encoder in §9 uses the same semantics: characterwise escaping
allows its consecutive string pieces to be concatenated inside one quote
pair. Thus the counts compare two implementations of the specified
representation, without assuming that its graphs satisfy their mathematical
recipes. The independent complete counts are:

| section | JSON nodes | encoder fragments | bytes |
| --- | ---: | ---: | ---: |
| B_bind | 25 | 33 | 57,478,400 |
| B_trans | 11,841,414 | 17,744,250 | 63,886,102 |

All raw binding entries total 54,036,413 bytes. The program compares the
complete regenerated raw-binding ledger, both section sizes, all 17 graph
ledgers, all sections in order, both dimension records, framing, both complete
endpoint records, scratch/buffer sizes, CAPS and completed-check descriptions
against output-502. Comparisons are recursive and type-sensitive, with exact
list lengths. This validates reproducibility of those measured objects;
agreement between users of the same constructor cannot independently prove
graph/copy/reference/dictionary/gadget correspondence. Neither payload is
persisted. No coordinate arrays are constructed.

**Framing and arithmetic.** The audit independently forms and round-trips a
32-byte `<8sQQQ` little-endian header: magic `J7F2C001`, comparison count 4,
B_bind and B_trans. The lengths delimit the intervening payloads in §6;
packing the fixed fields together here tests their sizes/ranges, not a
complete wire decoder. Four separate `<QQQQ` headers store their ordered
index,N,q,r, each 32 bytes and round-trip checked. All four dimension records
in §9 are used, with exact count/order and no truncated zip. For each rank
endpoint it uses quotient/remainder division by 8 to round rN, r and qr²
separately. Summing these three sizes plus each header is precisely (7);
summing their unrounded arguments is (8). All four arrays remain included.

At zero ranks this gives 32+128+57,478,400+63,886,102 = **121,364,662**
wire bytes, zero coordinate bits and (9)'s **184,059,344** operation bound.
At r_k=N_k the complete per-row sizes, initial/transition/final comparison
counts and all totals equal §9's saved endpoint: **65,220,461,539** bytes,
**520,792,775,000** bits and **2,004,404,443,690,552,400** for (9).
Four separately rounded N_max-bit scratch rows cost **53,884** bytes.
The zero-rank expression is not a valid certificate. The full-rank wire
exceeds 200,000,000; actual ranks and fitting coordinates remain unknown.
No padding validation, rejection of trailing bytes, strict transport schema
or coordinate verification is tested by packing headers alone.

**Failure, work and evidence.** The initial audit loader applied the strict
value-domain traversal to an administrative timing float and stopped after
102 selected units. Its full program snapshot and failure are preserved in
`scripts/four-rule-extraction/output-514/`. The repaired program accepts
floats only in administrative receipt traversal; the payload traversal stays
strict. The repaired run uses a fresh directory and carries those 102 units,
the failed elapsed measurement and all failed evidence bytes forward.

`output-514-repaired/wire-audit.json` records PASS after **62.39 / 900**
measured seconds including that failure. Its **90,213,461** selected units
are 60,624,737 original instrumented visits plus 29,588,724 auxiliary units:
102 failed-load units, 11,843,435 JSON nodes (including metadata), 896 full
receipt-comparison nodes, 17,744,283 encoder fragments and eight endpoint
rows. `check_job7_wire_encoding.py` independently compares every saved named
receipt field, all count/endpoint summaries and budget sums, and checks the
complete original program snapshot against its manifest hash/current bytes.
This engineering hash check is subject to §1's trusted-path/SHA limitations;
it is not mathematical input-byte equality against an unbounded adversary.
Its 887 recursive comparison nodes give **90,214,348 / 100,000,000** selected
units. Complete result: `output-514-repaired/receipt-check.json`.

Both authored programs, their output snapshots, unchanged tool snapshots,
initial failure, regenerated receipts and both final audit receipts cost
**192,000 / 1,000,000** reserved bytes. Proposed baseline plus all these
audit artifacts is **121,556,662 / 200,000,000** bytes. No large payload,
bytecode, temporary replacement, failed payload prefix or coordinate file
is saved. The independent encoder checks **121,364,502** ASCII characters
separately from selected item units. Its largest fragment has **41,326,714**
characters (B_bind), versus at most 66 for B_trans. This materially larger
temporary string is retained as a live-peak obligation; a fitting saved-byte
ledger does not bound it together with raw/decoded graphs or interpreter
objects. Original observer omissions and all internal C/container/read/hash/
serialization/bit/index work remain outside a complete bound. Selected-unit
guards do not turn those UNKNOWN components into a full work-cap pass.
Original-three-run partial items remain 75,868,982 and partial source items
168,943; this fresh audit's counters do not repair the historical ledger.

For reproduction use an isolated notebook copy retaining the fixed input
archives, output-502 and the preserved failed output-514, but with no
output-514-repaired. With `PYTHONDONTWRITEBYTECODE=1`, run first
`python3 scripts/four-rule-extraction/audit_job7_wire_encoding.py`, then
`python3 scripts/four-rule-extraction/check_job7_wire_encoding.py`.
Both refuse overwriting their receipts; audit failures retain partial counts
and traceback. No original program, receipt, production rule or cap changes.

**Conclusion and remaining scope.** This establishes the independent finite
payload counts and framing arithmetic, local progress within existing
semantics rather than a new algebraic discovery. Close this byte-count
subtest. Full independent graph correspondence, strict transport schemas,
live peaks and administrative coverage remain unfinished. No coordinate
experiment is admitted. All equalities, later jobs, Boolean/K/H/nonzero-fJ,
availability, L087 W₂ and unrestricted ER/Frege/SAT gaps remain. Mathlib's
full matching implementation coverage is not checked; no DAG input changes.

### 21. Static constructor-to-recipe correspondence — step 515

**Hypotheses and conclusion.** This is REPRODUCTION / proof_audit under the
unchanged ready SPECIALIZE assessment
`drafts/literature/2026-10-26-job7-transport-preflight-critical-audit.md`.
Retain §§1–3's eight literal binding inputs, exact F₂ semantics, full typed
dictionary, job 7 and every cap. The claim audited here is conditional:
if the fixed primary program and its inventory supplement complete their
stated exact comparisons on those inputs, the generated graphs, maps and
attributions implement §§2–3's recipes. This is a source-level proof of that
implication, independent of the serializer and graph-size receipts. It is
not an independent new execution on all input records, an arbitrary-input
transport decoder, or a received coordinate/equality certificate.

The reviewed source is `scripts/four-rule-extraction/preflight_job7_transport.py`,
lines 164–311 and 410–650, with `parameterized_input.py`, lines 118–168,
and `check_job7_inventory_fields.py`'s complete inventory comparisons.
Direct `cmp` checks, both exiting 0 with no differing byte, identify the
current primary and input-helper sources with their complete snapshots in
`scripts/four-rule-extraction/output-514-repaired/`. This uses literal source
equality, not hash equality. Provenance back to the older execution and
actual input-byte binding retain §§1,9,20 and L108 §§11,13's engineering
qualifications; these comparisons do not prove that an arbitrary historical
process executed the claimed source. No constructor, source engine, original
receipt or cap is changed or rerun here.

**Inputs imported, rather than reproved.** L035 (2)/(4) specifies the central
label and ordered marked-edge expression; L036's normalization and (5)
specify the job operands. L097 §22 supplies the arbitrary-root restriction
path bijection, including coincident/no-path roots; L038's edge-replacement
passage supplies the local substitution argument. Those existing proofs
were read at their relevant full passages. The primary theorem imports and
their restrictions remain §1 (Kiefer, arXiv:2009.01217v1, Propositions
1.1/2.1/2.2/3.1 and Theorem 2.3, pp.1–5; Mohri, IJFCS 13(1),
Definitions 4–5/Theorem 1, manuscript pp.4–6 and acyclic case pp.10–11).
No PIT or pruning theorem is reproved. The following code induction is
necessary because repeated consumers of one constructor do not verify its
correspondence with those inputs. Attempts 044–045 remain stopped at their
different complete-word/raw-reference interfaces.

**Primitive copies and syntax.** `append_edge` creates a new label list.
`copy` takes the current vertex count h as offset, allocates exactly the
child's vertex count, and appends precisely [h+u,h+v,label] for every child
edge in order. Its two half-open ranges exhaust that new allocation, and
its designated entry/exit are h plus the requested child roots. The child
is not mutated. Consecutive copies therefore have disjoint vertex ranges
and preserve all parallel-edge occurrences and label multiplicities.
`product` starts with fresh roots 0,1; after each fresh copy it appends the
connector from the previous exit (initially 0) to the new entry, then ends
with the final exit-to-1 connector. There are no other inter-copy edges.
The designated-root argument in L035 consequently gives the ordered product,
including a coincident child root, a no-path child and an empty child list
(the last case gives the single constant edge and polynomial 1).

Induction on the checked source tree proves `translation` uses the fixed
truth translation: true/false give 0/1, an original gives its alphabet index,
negation gives 1+child, and ordered disjunction gives the ordered product.
Its scalar reductions use only 0a=a0=0 and 1a=a1=a, and scalar negation is
addition of 1 in F₂. It never recognizes a nonscalar polynomial as zero.
Induction on the reduced syntax then proves `translated_graph` uses the
corresponding zero/one/original graph, the preceding ordered product, or a
fresh parallel constant-one branch and child copy. Every generated edge is
a singleton original or constant, all exterior roots are fresh, and all
copies are disjoint. The exact comparisons with both event graphs identify
the whole generated graph, not only its polynomial.

The normalization loop deletes outgoing sink edges and collects parity
separately within each remaining affine label. This is exactly L036's
normalization; the fixed translated graph already has singleton labels.
Distinct original edge occurrences are not canceled against one another.
The job loops visit vertices in numeric order and each vertex's outgoing
edge occurrences in normalized list order, first all product jobs and then
all index-ordered pairs. Product operands are the one-edge atom and H rooted
at the edge head. Pair operands are separate H graphs with one fresh source
and the selected prefix edge. Thus they are precisely L036 (5)'s operands.
Exact comparison of [index,vertex,kind,edge_occurrences] fixes job 7 and its
ordered pair. No Boolean witness graph is used as an original operand.

**Reachability and every restricted copy.** `validate` topologically orders
the structural graph. In reverse order `reachability` sets bit u and unions
the already computed rows for every outgoing edge. Induction in that order
therefore makes bit v equivalent to the existence of a structural u-to-v
path, including the empty path. Labels and parity play no role in this
recurrence. `cut` retains precisely s-reachable/t-reaching vertices and
every edge occurrence with s-reachable tail and t-reaching head, in original
edge order. Its sorted vertex list and inverse dictionary give mutually
inverse injective maps on the retained vertices. In a DAG those edge
conditions also imply both endpoints are retained: concatenate the three
subpaths through the edge; a repeated vertex would give a directed cycle.
If there is no path it retains the distinct roots and no edges. If s=t,
reflexive reachability puts it in the path case and acyclicity leaves exactly
the single root, no edges and the empty path. Thus this code implements
L097 §22's path restriction in every endpoint case, without a nonzero-label
or noncancellation assumption.

For each whole operand the exact comparison includes the original graph,
restricted graph, both maps, retained edge indices and no-path flag.
The inventory supplement requires exactly two restrictions and compares
their entire lists in all three inventories, closing the primary `zip`'s
possible extra-suffix omission. Both operands are therefore fixed before
the selected-pair loop; they are not inferred from W.

`central` enumerates each ordered pair of entries of the two edge labels,
adds one pair-once token exactly when both are originals of distinct
indices, and preserves repetitions. Constants contribute none; sorted
indices name the pair but do not reorder any word factor. This implements
L035 (2). The Cartesian edge-pair loop visits all pairs, omitting only a
literally empty central list. Exact selected-list comparisons and the
supplement's exact lengths/fields preclude omitted or extra selected pairs.
For each pair the four cut specifications are, in order, F-prefix,
G-prefix, G-suffix, F-suffix. Full metadata comparisons identify every
retained/deleted occurrence, and each copied edge is checked against its
fresh offset. The four connectors and all central edges are compared in
full. The monotonically advanced vertex/edge cursors end at W's exact
vertex/edge counts and roots 0,1, so there are no unaccounted records or
overlapping copies. The four path-bijection inputs are exactly those used
in L097 §22, with L035's factor order intact.

For the separate structural count, every W label is explicitly required to
be a singleton. In topological order, each state's set is the union of all
counts along incoming structural paths; addition of one occurs exactly on
a typed placeholder edge. Induction proves this statement even for paths
that later cancel. Requiring states to be contained in {0,1} and the sink
in {1} therefore proves the stated one-placeholder property, vacuously if
there is no accepting path. It is not inferred from a surviving monomial.

**Independent R and ordered P.** The reference loop enumerates F and G's
edge lists again; it reads neither W's edges, its selected list nor its
internal restriction maps. For every nonempty recomputed central list it
allocates four full copies, with designated roots in exactly (2)'s order.
These copies retain all of F/G, including edges irrelevant to those roots.
The primitive copy invariant and the four explicit connectors give precisely
L035 (4). Nonextremal exits cannot create an extra accepting route: after
leaving one internally a path cannot return to that exit in a DAG. Empty
or no-path factors retain their prescribed semantics. In the empty pair-sum
case the common roots have no edges and polynomial zero. The later pass
checks every copied edge and connector; its data were generated from these
independent whole-operand loops, not an oracle taken from W.

`product([F,G])` and `product([G,F])` separately allocate FG and GF. The
factor-by-factor check exhausts their ranges, every copied edge, each serial
connector and the final connector. A further pair of fresh copies attaches
them in parallel to P's common roots. By the primitive invariants there are
no shared interiors or residual records: P computes fg+gf in that order,
with independent choices for repeated factors. The reference and product
postchecks need not by themselves accept arbitrary copy metadata: the
fresh-construction invariant supplies the range and exhaustion facts here.

**Typed dictionary and all local transports.** The request checker requires
all n+n(n−1)/2 entries, exact association to the original alphabet order,
distinct typed associations and exact word lists x_ix_i+x_i or
x_ix_j+x_jx_i. `symbol_map` reserves `1`, then distinct `x` tokens, then
distinct Boolean/pair tokens mapped to placeholder positions. Display names
are not used as algebra tokens; display-name collisions cannot conflate
these types. All entries, including unused ones, remain in the transport.

`local` visits every input edge and its odd-multiplicity tokens. An original
or constant survives in all modes. A placeholder survives in free mode,
adds no edges in zero mode, and in axiom mode expands to its full dictionary
word list. Each nonfinal letter creates one fresh vertex; the final letter
lands on the old head. Fresh indices start at the old vertex count, strictly
above both old endpoints, so the `dest != cv` test cannot accidentally reuse
an old endpoint. Each word has its own interiors, allocated monotonically,
with no extra incidence; its edges have exactly the word's original order.
An empty word adds a constant edge and an empty word list adds none.
Repeated words remain separate paths. The attribution records every odd
token, including a deleted zero-mode placeholder with empty ranges.
The second traversal checks its start/end ranges and every word edge and
exhausts the output; the first traversal supplies complete attribution
enumeration. L038's local replacement proof therefore applies. There is
no extra IPS +1 edge in these comparisons. All six mode graphs are
explicitly stored; aliases in the construction are not a wire-size discount.

**All four comparisons and topology.** The fixed four-row loop selects
Wfree/Rfree, Wzero/Rzero, Waxiom/Raxiom, and Raxiom/P. Starting at vertex
count zero, `copy` allocates two disjoint complete graphs and no connectors.
Eta and theta list exactly both transported entries/exits. Disjointness
makes their two positions distinct even when a child's roots coincide;
the graph's auxiliary single source/sink fields do not replace eta/theta.
Its weighted output is consequently the sum of the two operand outputs,
including both empty-word contributions. Free mode lists all six originals
and all 21 typed placeholders; the other modes list all six originals.
Constants are excluded from these alphabets and unused letters are retained.
All generated graphs have singleton labels: this follows from the syntax,
copy, W singleton check and gadget invariants, so the reported constant/
letter edge counts have the coefficient-action meaning required by §4.
`validate` alone would not establish this fact for arbitrary affine input.

Finally, `validate` checks graph fields, integer endpoints, declared label
tokens and acyclicity. Its Kahn order contains each vertex once: each enters
the queue only when its nonnegative remaining incoming-edge count becomes
zero (or initially is zero), with parallel edges decremented separately.
The explicit position-array check excludes repetition and verifies every
edge points forward; length n then gives a bijection. Every base, mode and
comparison graph stores its checked order. The frozen transport collects
all seven base graphs, six mode graphs and four comparisons with the checked
maps, attributions, dictionary and binding, in its prescribed field order.
Thus all graph constructions in the conditional claim are accounted for.

**Result and limits.** The static recipe obligation is discharged for the
fixed generator, conditional on the literal input/comparison hypotheses
above. No mismatch was found. This is new local audit evidence for existing
mathematics, not a new algebraic identity or complexity result. The inspected
complete saved inventory and step-514 reconciliation receipts retain their
own successful/limited claims; they are not substituted for this proof.
No expensive regeneration, new numerical experiment, coordinate array or
payload file is produced here. Previous measured sizes/counters do not
become new measurements or total bounds by this audit.

Strict acceptance of arbitrary proposed graph/map/gadget/comparison JSON
is still unproved. In particular generated range/partition invariants used
above are not a substitute for a decoder rejecting extra/mistyped data,
truncating zips or bogus attributions. No such full decoder is implemented
by the primary sizing program. Live peaks, including §20's large temporary
fragment, and complete administrative/internal/failed work remain open.
Coordinate ranks, fitting evidence and finite equality acceptance are still
unreceived; all later-job, Boolean/K/H/nonzero-fJ, availability, L087 W₂ and
unrestricted ER/Frege/SAT gaps remain. Full matching Mathlib coverage of
this implementation specialization is not checked. No DAG inputs change.

### 22. Strict-schema boundary and concrete postcheck witnesses — step 516

**Hypotheses and conclusion.** This REPRODUCTION / proof_audit uses the
unchanged ready SPECIALIZE assessment
`drafts/literature/2026-10-26-job7-transport-preflight-critical-audit.md`.
Retain the exact eight binding paths, source, job 7, F₂ semantics, dictionary
and CAPS of §§1–9. The question is whether the fixed preflight enforces
§6's strict mathematical schemas on an arbitrary proposed transport, as
distinct from §21's conditional proof of its generated objects. It does
not implement that receiving interface. Moreover, the existing product,
gadget and comparison postchecks alone accept the particular malformed
metadata below. This is informative NEGATIVE evidence against a schema-pass
interpretation, not against the generated graphs, their measured sizes,
the conditional soundness theorem, or the feasibility of the format.

**Source boundary and existing inputs.** The full primary program and both
step-502 supplements were reviewed at their parsing, field, equality and
collection checks. The relevant helper is `parameterized_input.py`'s
`fields`, `parse`, `request`, `symbol_map` and scalar-type checks. Literal
`cmp` checks of the primary and helper against their
`output-514-repaired/` snapshots both exit 0. This is source identity, with
§21's unchanged historical-execution qualifications. No original preflight,
archive, graph recipe or source engine is rerun or modified.

The known algebra is imported by the precise Kiefer/Mohri citations in §1;
no word-space theorem or graph transport is reproved. Section 21 already
proved the conditional generator correspondence and warned that it was
not a decoder. The new evidence here locates actual insufficient subchecks
and gives complete finite witnesses, rather than repeating that warning.
Attempts 044–045 concern stopped word/raw-reference receivers and supply
no proposed-transport acceptance input. No new literature scope is needed.

**Complete field-family distinction.** The following is a static audit of
the actual source paths, not a claim that sampled tests prove all schemas.

| Object/obligation | Enforced or generated boundary |
| --- | --- |
| Fixed raw inputs | Primary lines 365–395 check bounded strict UTF-8 and parse seven non-JSONL bindings; `p.request` separately checks all source lines. `p.parse` rejects duplicate keys, floats/nonfinite numbers, excessive nesting and oversized integer tokens. It allows Boolean/null values; field schemas must still reject them where indices are required. No proposed B_trans section is loaded. |
| Request/alphabet/dictionary | `p.request` checks exact request/dictionary/entry fields, ordered distinct names, all n(n+1)/2 typed associations and exact ordered polynomials. The transported copies come from that checked object. |
| Translation events and normalized graph | Event field sets are exact. Regenerated syntax/graphs and normalized graph are compared with `R.eq`, which first checks exact Python types, then complete keys/list lengths and all values. This rejects extra/mistyped mathematical fields in those comparisons, conditional on completion. |
| Whole restrictions | Each saved complete restriction is `R.eq` to the regenerated original/trimmed graphs, maps, retained indices and Boolean no-path flag. The inventory supplement requires exactly two and compares entire lists in all three inventories, closing the primary zip's length gap. |
| Selected occurrences/W | Job and selected field sets are checked; the 120 ordered identities, exactly four internal maps per selection, full regenerated metadata, copied edges, connectors and W partition are checked as in §21. The supplement checks repeated identities and exact metric types. These are checks on job 7's used mathematical fields, not a blanket schema check of all other archived jobs. |
| Every explicit graph | `validate`, lines 227–263, requires exactly vertices/source/sink/edges, positive exact-int vertex count, exact-int roots/endpoints in range, list edges of length three, list labels and declared string tokens, record/label/name caps and acyclicity. It generates and verifies its own topological permutation. It does not take a supplied permutation as an argument. |
| Independent R/copy maps | The constructor supplies all reference entries, four copies and fresh exhaustive ranges. Lines 531–542 check copied edge content, dimensions and connector content, but no exact field schema for incoming reference metadata exists. Generated invariants in §21 supply enumeration and range partition. |
| Ordered FG/GF/P maps | Two products and their two factors each are constructed internally. Lines 543–561 postcheck them using ordinary equality for factor map ranges/roots and selected lookups for P; they do not uniformly require exact index types or map keys. |
| Six modes/gadgets | `local` generates every attribution, its field set and mode. Its second pass, lines 596–614, checks range starts/ends, word edges and exhaustion; it uses direct input-edge indexing and only the first two range entries, with no attribution-field schema. Generation supplies complete attribution enumeration. |
| Four comparisons | Fixed loop lines 623–642 creates exactly the four comparisons, two disjoint copies each, eta/theta, full mode alphabet and its checked cardinality, and a newly generated checked topology. Lines 633–636 only postcheck the zipped copied edges; supplied comparison fields, map cardinality, eta/theta or topology have no decoding/validation entry point. |
| Outer transport | Lines 644–650 construct all twelve keys/values and check their key order against LAYOUT. No proposed object is passed to a recursive transport schema. Counting checks generic JSON-domain values, which is weaker than index/map/gadget schemas. |
| Wire/coordinate framing | No complete J7F2C001 decoder, terminal-padding check, trailing-byte check or coordinate receiver is implemented here. Section 20's header round trips and byte counts do not implement these checks. |

In particular a strict generic JSON parser cannot fill the missing
field-specific checks. Boolean `false` is valid JSON and remains a Boolean
after parsing; it must not be accepted as an integer index under §6.

**Finite witnesses and their full verification.** The audit program
`scripts/four-rule-extraction/audit_job7_schema_boundary.py` never invokes
the preflight `main`. It parses the unchanged primary source and compiles
the exact existing AST nodes for lines 543–555, 596–614 and 633–636.
It supplies tiny fixtures to those original blocks, without inserting
new validation statements. The complete selected source, every fixture,
return/rejection and counter is retained in
`scripts/four-rule-extraction/output-516-repaired/schema-boundary.json`.
Its complete `/cases` and `/selected_source_blocks` values were read with
the JSON inspector's `--full`; a preview is not the evidence used here.

Let A have vertices 0,1, roots 0,1 and the edge [0,1,[x1]], and B the same
graph with label [1]. Their actual token strings are `x1` and `1`, with
symbol declarations original index 0 and scalar one. The unchanged
`product([A,B])` produces six vertices and these five edges in order:

    [2,3,[x1]], [0,2,[1]], [4,5,[1]], [3,4,[1]], [5,1,[1]].

Its first factor map is vertex_range=[2,4], edge_range=[0,1], entry=2,
exit=3; its second is [4,6], [2,3], 4,5. GF has the same ranges with the
two factor labels reversed. Present both complete products and maps to the
original lines 543–555, changing only FG's first edge_range to [false,1].
The range comparison is ordinary list equality: `False == 0`, so it passes.
The remaining range/root comparisons and every exact edge/connector test
see unchanged values. The full FG/GF block therefore returns successfully,
despite the noninteger range index. A separate trial adds an `unexpected`
field to that map; no checked lookup sees it, so it also returns. The
control with edge_range=[0,1,0] is rejected by the list-length-sensitive
ordinary equality. These are three distinct recorded tests with valid
complete-product fixtures, not claims about an absent outer receiver.

For a local free-mode witness use z=out=A and one attribution with
token=x1, vertex_range=[2,2], edge_range=[0,1]. Change its input_edge from
0 to false. Direct list indexing selects the same edge; both partition
tests, the single original edge comparison and complete exhaustion pass.
In a separate trial retain input_edge=0 and add both an unexpected field
and a third edge_range entry 99. Only range entries 0 and 1 are examined,
so that full postcheck also passes. The wrong-end control [0,2] fails at
`local partition end`. These modifications cannot arise from the fixed
constructor, whose correct field types and range lengths remain proved
in §21. They show why that constructor invariant is essential.

For the comparison subcheck use the disjoint union of A and B, with four
vertices and edges [0,1,[x1]], [2,3,[1]]. Its true copy maps are [0,2]/[0,1]
with entry/exit 0/1 and [2,4]/[1,2] with entry/exit 2/3. Delete the second
map: the exact lines 633–636 check only the first zipped pair and return.
Alternatively keep both maps but replace the first vertex-range end by
null and edge-range end by the string `unchecked`; neither end is read by
that block, so it still returns. Both complete fixtures are recorded.
These statements concern that precise copied-edge subcheck, not the full
surrounding comparison constructor or any hypothetical complete receiver.

All 25 trials match their recorded expectations. Graph controls reject
extra fields, Boolean vertex counts/roots/endpoints, a float root, negative
root, unknown/nonstring token and a cycle. Valid singleton, empty affine
label, multi-entry affine label and coincident-root graphs are accepted.
Those last cases are allowed by the graph semantics; they are not schema
bugs. They also confirm that `validate` alone does not establish normalized
singleton metrics: its empty-label graph reports letter_edges=1, and its
label [1,x1] graph reports constant_edges=0. The fixed singleton invariants
in §21, rather than arbitrary affine-graph acceptance, justify the measured
m0/mL meanings. A control using `R.eq([0],[False])` rejects, so these findings
do not impugn the type-sensitive whole/internal-map comparisons.

**Failures, resources and result.** The first harness stopped before any
fixture or trial because it expected three selected local AST statements;
the two assignments on physical line 596 are separate AST nodes, making
four. Its original program and explicit failure receipt remain in
`scripts/four-rule-extraction/output-516/`. No archive or production code
was changed. Only the harness assertion was corrected; the repaired run
uses fresh `output-516-repaired/` and preserves the failure. Initial selected
and fixture visits are zero; its elapsed/import/AST/internal work is UNKNOWN
and is not silently reset to zero or included in a total bound.

The repaired probe reports 332 selected-check item visits plus 46 fixture
construction visits, hence 378 against 100,000,000, and about 0.00832 seconds
against 900. These are narrow measurements, excluding parsing/AST/import,
serialization/I/O, uninstrumented operations and interpreter costs; they
do not repair any historical administrative ledger. The archived initial
and repaired programs/receipts total 32,625 bytes. Including the separate
working audit program gives 41,715 bytes, below the 1,000,000 reserve and
200,000,000 evidence allowance; `wc -c` checked all five complete files.
No payload, coordinate arrays, overwritten receipt or failed payload prefix
is produced. Existing output-502–514 measurements remain unchanged.

Thus schema coverage has a precise negative boundary: generated-output
correspondence and exact wire sizing survive, while a strict arbitrary
proposed-transport schema pass is unavailable. Do not interpret the primary
receipt's `complete_transport_checks=True` as that pass. No production
acceptance rule or format was repaired. Live allocation/decoding peaks,
complete work, an implemented strict receiver, actual ranks/coordinates and
all equality receipts remain open, along with every broader gap in §7.
Full matching Mathlib coverage of these implementation checks is not
checked; no absence claim or new DAG input follows.

### 23. Static live-data lifetimes and the unimplemented decoding peak — step 517

**Hypotheses and scope.** Inspect the unchanged
`scripts/four-rule-extraction/preflight_job7_transport.py`, its two step-502
supplements, `parameterized_input.py`, the invoked literal checker, and
`audit_job7_wire_encoding.py`/`check_job7_wire_encoding.py`. This is a static
successful-control-flow audit of those sources, using the archived finite
measurements already qualified in §§9,20. It is not a fresh execution,
allocation measurement, exact-version interpreter proof, or independent
provenance check. The ready assessment is
`drafts/literature/2026-10-26-job7-transport-preflight-critical-audit.md`.
No proposed transport receiver is supplied (§22).

**Conclusion.** The following retention claims follow from explicit source
references, independently of object-size estimates. The primary receipt's
`buffer_peak_bytes=83667` measures one emitted byte fragment, not the live
encoding footprint. Its `raw_bound_input_bytes=54036413` is a sum of eight
file lengths, not a measurement of simultaneous raw byte buffers. Its
`decoding_peak` field is a specification of a possible future receiver,
not an observed execution phase. Neither it nor §20's largest string
fragment establishes a numeric Python live-memory bound. The source retains
the additional families below; a byte-for-byte total remains UNKNOWN.
These findings qualify the resource ledger without refuting the wire counts
or exhibiting an overflow of the evidence-byte cap.

**Proof: input lifetimes.** In `main` lines 365–375, `binding` retains all
eight decoded texts, while `objects` retains seven separately parsed JSON
trees; the proof JSONL is excluded from that dictionary. `text` and the
last `obj` remain aliases to already retained objects. The eight lengths,
read in full from `output-502/preflight.json`'s `raw_binding_manifest`, are
38,500,512; 13,564,301; 1,858,313; 101,314; 2,947; 1,433; 4,591; and
3,002 bytes, in `BIND_PATHS` order. Their reported sum 54,036,413 describes
input byte lengths. It is not a string-storage measurement. The loop
rebinds `raw` on each iteration; it never puts the eight raw byte objects
in a collection. During a new read the preceding `raw` can still be live
until assignment. During `p.parse(raw)`, the caller's retained `text` and
raw bytes coexist with the parser's UTF-8 decode and constructed JSON;
the parser takes raw bytes, not the caller's text. Its duplicate-key hook
constructs `out` while its input pair collection is still in scope.
Decoder and allocator internals are additional, unbounded costs here.

At the binding `R.count`, all texts and seven objects have been loaded;
the final event's raw byte buffer is still bound. The subsequent assignment
`req,raw,rows,checked=p.request(...)` retains that caller buffer while
evaluating its right side. Inside `p.request`, the freshly parsed request,
source bytes, split-line byte strings, parsed header/records and the
second-read source buffer coexist at literal-check invocation. The literal
checker additionally retains its `BytesIO` stream, header/current JSON row,
normalized formula tuples in `fs` and recursive checking temporaries.
Whether its stream or decoder makes additional internal copies is not
settled by this source audit. On successful return, `main` retains the
fresh request, immutable source bytes, strict parsed rows and checker receipt;
the earlier request in `objects` is still present too. `input_bounds`
temporarily adds tree-reference and size/depth collections. The physical-line
comparison also evaluates two `splitlines` expressions and a new source
read, with the left selected line retained during evaluation of the right.
None of these is represented by a count of the largest serialized chunk.

**Proof: construction roots and aliases.** The first five families below
remain reachable in `main` during final transport sizing and its receipt
write. The last row adds metadata, including endpoint objects constructed
after sizing. This is a family-level inventory, not an object-size census.

| Retained roots | Consequence for an allocation ledger |
| --- | --- |
| `binding`, `objects`, `cert`, `inv`, `prior`, `failed`, `tr`, `event`, fresh `req`, source `raw`, `rows`, `checked` | Whole archives, including jobs other than job 7, remain reachable. Job-7 graph totals do not count all decoded archive storage. The short names alias entries of `objects`; they are not extra full archive copies. |
| `reduced`, `regenerated`, `h`, `jobs`, `operands`, `maps`, residual loop values | All 245 job recipes remain in `jobs`. `dict(h,source=...)` shares the edge list; sum-job `h['edges']+[...]` creates a new outer list sharing old edge objects. Whole-map `original`/`trimmed` entries and F/G bases reuse roots. Counting every reference as a deep copy overcounts; omitting the outer lists undercounts. |
| `reaches`, final `specs`/`reach`, `selected`, final cut metadata | The two whole-operand reachability integer tables survive all selected-copy checks. `specs` borrows them. A cut output copies selected edges/label lists; its temporary child graph is not retained merely because its edges were checked. The complete whole-operand tables are not the four arithmetic scratch rows in §6. |
| W's `order`, `states`, `adj` | The structural pass retains a set for each vertex and adjacency entries with placeholder increments. Later `validate(w,...)` creates a separate topological-order list for the W base entry; the earlier `order` is still bound. Temporary arrays inside each validator are additional during that call. |
| `reference`, `refmaps`, `fg`, `gf`, `comm`, copy/product maps, `bases`, `base_entries`, `modes`, `byname`, `comparisons`, `transport`, `all_entries` | All seven base, six mode and four comparison graph entries coexist. Entry lists/dictionaries and `byname` often alias graphs. In contrast `copy` appends new edge and label lists into its destination, so comparison/product graph copies cannot be erased by treating their recipes as shared expressions. |
| `R.graphs`, `R.sections`, counters, dimensions, endpoint/result/receipt dictionaries | These are further metadata and index/counter storage. `R.graphs` contains metrics, not a replacement for the graph objects above. The result dictionaries reuse some metadata collections, rather than duplicating every value. |

`reachability` also has its own topological order and adjacency while
constructing its returned integer table. The two temporary whole-operand
tables passed directly to `cut` need not remain reachable after those calls;
they must not be counted as permanently retained merely because later
`reaches` constructs new tables. Similarly `validate`'s adjacency, indegrees,
queue and position array need simultaneous accounting during validation,
but are not returned along with its order. These distinctions use explicit
return values and references, not an assumption that the allocator returns
unreachable storage to the operating system. The table supplies concrete
missing allocation categories, not a claim to bound every C allocation.

**Proof: serializers and phases.** In `Run.count` lines 142–159, `chunk`
and its UTF-8 `data` coexist. Advancing its generator can retain the prior
iteration's `data` while producing the next string; encoding that string
evaluates a new bytes result before rebinding `data`. Recursive `chunks`
frames retain their container/string arguments. For strings its expression
at line 136 slices the input, serializes the slice, and slices off quotes;
the final emitted byte length does not account for all those temporaries
or encoder work. `serialized_buffer_peak` takes only `max(len(data))`.
Thus even a correct 83,667-byte measurement is not a peak-memory upper bound.

The independent `AuditRun.count` first completes `super().count`, then walks
the same object and invokes `iterencode`. Its `piece` is a string; this loop
checks ASCII and takes its length, without converting the whole piece to a
second UTF-8 bytes buffer or concatenating all pieces. The complete saved
`/counts` rows (§20) show B_bind's largest piece has 41,326,714 characters,
and B_trans's largest has 66. The large binding piece coexists with binding
texts/decoded archives and the suspended encoder, whose detailed internal
allocations remain unbounded here. It occurs at the early `B_bind` call,
before literal checking and graph regeneration. No source reference saves
that large piece through the later B_trans call. Therefore adding its size
to all subsequently generated graphs as an asserted simultaneous peak
would be unjustified. Conversely the later B_trans encoder does operate
while the retained construction families in the table are live.

The outer step-514 audit retains five decoded old receipts during the
regeneration. It loads the fresh final receipt only after `original.main`
returns. Normal return removes the main-frame roots, but proves neither
immediate allocator reclamation nor a process-memory decrease. The two
step-502 supplements are separate invocations: their decoded event/prior
or three-inventory trees cannot be added to the primary's objects as an
observed simultaneous process peak. Within each invocation those trees
coexist with its metadata and receipt serialization. Every `json.dumps(...)
.encode()` receipt write has string/byte evaluation temporaries; repeated
fixed-point sizing in the inventory supplement and reconciliation checker
can retain the preceding `raw` while evaluating its replacement. An exclusive
file open prevents overwriting saved evidence, not allocation overlap.

Finally no primary or step-514 path constructs the complete B_bind/B_trans
wire buffer, packs actual coordinate arrays, decodes a full proposed bundle,
or allocates the proposed four arithmetic rows. `R.binding` and `R.transport`
are lengths. Endpoint arithmetic uses hypothetical ranks and lengths. Thus
`live_ledger.decoding_peak` describes a future implementation obligation;
it is not a measured maximum or a source-level bound on an existing decoder.
The primary's archived `observed_ru_maxrss=1118912512`, with its recorded
macOS-byte qualification, is a historical process high-water observation,
not attribution to one phase or an independently reproduced bound. In
particular 200,000,000 is the evidence-byte allowance, not a specified
interpreter-memory ceiling; this observation is no evidence-cap failure.

**Result and remaining test.** Close the static lifetime-identification
subtest with an informative negative: the fragment/raw-sum/decoding fields
cannot certify live peak fit, and their precise boundaries are now explicit.
Keep numeric decoding/interpreter peaks UNKNOWN, rather than rerunning an
expensive sizing experiment or inventing a receiver to measure them. The
wire/framing result and conditional constructor proof survive. No coordinates,
equality verdict, complete work ledger, total-resource certificate or general
complexity result follows. The remaining administrative audit must distinguish
proved selected-unit claims from unbounded read/decoder/allocator/bit/index,
historical-failure and receipt costs before declaring any full audit pass.
No mathematical script or DAG edge changes in this static step.

**Mathlib.** Full matching implementation/lifetime coverage is not checked;
no absence claim is made. This is REPRODUCTION of a finite implementation's
reference and control flow, with no progress claimed beyond the source
mathematics already imported in §1.

### 24. Terminal administrative-claim disposition — step 518, 2026-10-26

**Hypotheses.** Retain the fixed inputs, CAPS, encoding and prior SPECIALIZE
assessment used in §§9–23. This is a static REPRODUCTION conceptual audit
of the original acceptance branches and saved ledger meanings. The finite
results in those sections retain their qualifications; no original command,
count, schema fixture or source-interface probe is rerun. Section 1's precise
Kiefer/Mohri imports remain unchanged. No additional algebraic theorem is
needed, and no new equality is asserted.

**Conclusion.** Close this audit with the following disposition:
**qualified wire-size and constructor claims survive; complete administrative
preflight acceptance is NOT ESTABLISHED**. This is a terminal finding about
the saved experiment, not an instruction to keep recovering unavailable
historical work. It is neither an observed cap overrun nor a rejection of
the mathematical format. In particular `MANDATORY_TRANSPORT_FITS`,
`complete_transport_checks=True`, and the supplements' `PASS` values do not
jointly imply the complete acceptance obligations of the approved scope.

**Proof: what the status branches actually test.** Inspect
`scripts/four-rule-extraction/preflight_job7_transport.py`, especially
`Run.tick`, `Run.timer`, `save_small` and the final part of `main`.
`tick` bounds its own incremented integer at 100,000,000; it does not count
an operation with no call/observer charge. After graph generation, sizing
and symbolic endpoints, `main` sets both positive flags. Its remaining
mandatory-size test compares the zero-rank wire baseline, already saved
output bytes and the 1,000,000-byte reserve with 200,000,000. Exceptions
inside that block change the flags, but successful passage adds no test
of omitted work, historical failures, strict proposed-wire reception or
numeric live peaks. Indeed the same update explicitly sets
`exact_total_interpreter_bound=False` and keeps equality acceptance false.

The accounting supplement explicitly labels itself
`separate_critical_audit=False`. It checks the primary status, selected
arithmetic/graph values, its counted walks and saved artifacts. The inventory
supplement also sets that flag false, carries forward the reported item
integer, adds its own walk/equality charges and checks the result. Neither
contains an added charge or bound for the missing work classes identified
in §§10–19. Therefore composing these programs' positive flags cannot
complete those missing premises. The known source/parser omissions alone
already refute interpreting the original counter as an exhaustive count
of its declared explicitly traversed item classes.

There is a separate, concrete timing boundary. In the primary, the saved
`elapsed_seconds` is sampled before the final `result.update`, final
receipt serialization, `save_small` write and stdout emission. The accounting
supplement samples `supplement_seconds` while constructing its receipt,
before encoding, writing and printing it; its final checks are byte/item
checks, not a full-invocation timer. The inventory supplement samples its
receipt time before its fixed-point receipt sizing loop; it performs a
later 900-second check, but still before the final file write and print.
The saved durations are respectively 40.642286416998104,
0.12803358400196885 and 5.375180584000191 seconds. Their sum is about 46.15
seconds, but it measures these three recorded intervals only. It does not
measure the omitted tails, imports before their timers or the unpreserved
failed helper invocation. Thus a complete failure-inclusive elapsed bound
cannot be deduced from these values. No claim is made that any omitted tail
actually exhausted the remaining time.

**Complete claim-to-obligation comparison.** The following ledger keeps
different units and invocations separate. These are retained results, not
fresh measurements in this step.

| Claim/category | Supported value or status | Exact limitation |
| --- | --- | --- |
| Fixed explicit graphs and frozen wire | §§20–21: 121,364,662-byte baseline; maxima 247,186 records and 139,422 labels versus 2,000,000 each | Constructor correspondence is conditional on its fixed inputs and successful complete comparisons. Baseline is not a certificate. |
| Full-rank endpoint | §20: 65,220,461,539 bytes versus 200,000,000 | Rejects only this endpoint; actual ranks/coordinate fit remain unknown. |
| Original three successful runs' reported items | §9: 75,385,009 versus 100,000,000 | Source and non-source parser omissions are not included. |
| Corrected selected item classes | §§10–19: source 168,943; three-run subtotal 75,868,982 | A partial augmented ledger, not an upper bound on all required items or work. |
| Parse/serialization scans | §§12,14: 104,048 source and 109,721,129 non-source scan characters; §20: 121,364,502 independent-encoder ASCII scans | Different measures and executions; neither add them to item counts nor infer an item-cap failure. |
| Reachability and index fields | Original receipt: 608 shifts, 785 ORs, 288,307 shift-and-tests; 86,450,864 local bit-operation upper bound; maximum counter/index lengths 26/17 bits | A local logical ledger and operand-length data, not costs for every index, allocator, parser, container or interpreter operation. |
| Source/checker interfaces and internals | §§15–19 receive specified operands, return values and encodings | Actual internal costs, read/UTF-8, allocation, hashing, bit/index work and receipt I/O lack a complete disjoint bound. |
| Original helper failure | §14: selected strict load scans 18,861 characters before rejecting the recorded float | False `graph_checks_started`/`item_walk_started` flags are not zero total work; the historical program and complete duration/work are unavailable. |
| Original saved evidence | §9 and final inventory receipt: 158,027 bytes; baseline plus these artifacts 121,522,689 | Fits the 1,000,000-byte reserve and 200,000,000-byte allowance for this artifact set, not a full accepting bundle or live memory. |
| Independent sizing audit | §20: 90,214,348 selected units; 192,000 saved bytes; baseline plus that set 121,556,662 bytes | Fresh selected ledger; does not repair original historical work. Its receipt explicitly sets `full_transport_audit` and `total_work_bound` false. |
| Schema probe | §22: 378 selected/fixture units; 41,715 saved bytes | Initial failed harness elapsed/internal work is UNKNOWN; its receipt sets `complete_administrative_ledger` false. |
| Arbitrary proposed-transport reception | §22: absent; particular isolated postchecks accept malformed metadata | Generated-object invariants justify their own objects only. No strict complete wire or coordinate decoder is supplied. |
| Live memory and decoding | §23: retention/alias/phase families identified; numeric peaks UNKNOWN | Chunk maxima/raw-file sums are not live upper bounds; `decoding_peak` concerns an unimplemented receiver. No interpreter-memory ceiling of 200,000,000 was specified. |

For the selected item budget let U denote additional required item charges
not yet reconciled, without adding scans or other different units. Even
granting the retained partial subtotal, acceptance would require
75,868,982+U <= 100,000,000, hence U <= 24,131,018. No such upper bound is
provided by the receipts. Nonnegativity and remaining headroom establish
neither fit nor overflow. The analogous missing historical/tail duration is
also not bounded by its successful intervals. This identifies the missing
premise rather than replacing an unknown by zero.

The 77,477,311-byte conservative coordinate allowance in the final original
inventory receipt is likewise only arithmetic: 200,000,000 minus baseline,
158,027 artifacts and an additional full 1,000,000 reserve. It does not
construct B,c,T, validate their equations, or pay unlisted future artifacts.
Separate later audits have separate artifact sets and selected ledgers;
their maxima and counts are not measurements of one simultaneous run.
Any future experiment must declare its own complete retained inputs/evidence
and work budget. No claim here excludes those bytes merely because they
were written by an earlier turn.

The load-bearing saved fields used above were read completely with
`../scripts/loop/inspect_json.py --pointer ... --full`: original status,
completion/accounting/live/timing/index/reachability fields; both supplements'
timings, counters and final byte/allowance fields; the helper failure flags,
error and repair; the independent sizing reconciliation's selected totals
and false full-audit/total-bound flags; and the schema receipt's complete
initial-failure record and false complete-ledger flag. Earlier finite proofs
are reused for their closed subtests, not reestablished from previews.

**Disposition and mathematical relevance.** The original preflight plan
explicitly makes missing instrumentation an unfinished preflight. The
unbounded selected-item and historical-failure components are sufficient
to withhold that administrative pass. Absence of a total interpreter bound
alone would not refute the narrower byte-count claim: the original scope
already distinguished those notions. Strict reception and numeric live
peaks remain independent obligations for a future claimed full receiver.
Close this audit without a coordinate-execution authorization, preserve all
original/repaired evidence and park the historical-completion route. An
independently assessed symbolic mechanism may be investigated without
pretending this old experiment passed. Later jobs, all coordinates/equality
receipts, Boolean/K/H/nonzero-fJ, general availability, L087 W₂ and uniform
worst-case P versus NP remain unresolved.

**Mathlib.** Full matching coverage of this finite control-flow/accounting
audit is not checked. No new mathematical dependency, algebraic discovery,
finite replay, script or certificate is supplied. This is an informative
negative about the inference from saved acceptance flags to a complete
administrative pass, not a lower bound or counterexample to P versus NP.

## Mathlib

Full matching theorem/finite-encoding coverage: **not checked**. No absence
claim is made. Kiefer's cited word-space and coordinate statements, Mohri's
finite acyclic semantics and the existing local graph transports are the
mathematical inputs; the fixed-input receiving and resource contract is
written out above. This is local specification progress, classified
REPRODUCTION, with no claim of progress beyond the known source mathematics
or of certified originality.

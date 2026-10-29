# L108 — Right-multiplier extraction for the complete literal-OR rules

## Hypotheses

Work over the free associative algebra F₂⟨y₁,…,yₙ⟩. Supply a nonempty
explicit acyclic propositional proof π, written as a sequence of full
ordered formula trees and backward references, with designated final
formula T. The only connectives are primitive ∨ and ¬, with constants
true and false. Every formula variable belongs to the supplied original
alphabet y; unused alphabet entries and unused proof lines are allowed.
The proof is assumption-free. Its axiom schemes and inference rules are
exactly:

- ¬A∨A, and the two locally added ground axioms true and ¬false;
- expansion: from A infer B∨A;
- contraction: from A∨A infer A;
- association: from A∨(B∨C) infer (A∨B)∨C;
- cut: from A∨B and ¬A∨C infer B∨C.

Arguments are arbitrary formula trees in this language. Matching is
literal syntactic matching, including the order and bracketing shown.
There are no assumption, extension, renaming, substitution-inference,
modus-ponens or rewriting rules. Proof reuse uses backward references.

Supply the complete unchanged original dictionary B with independent
free placeholders σᵢ and τᵢⱼ for all i<j, with substitution

    σᵢ ↦ yᵢ²+yᵢ,       τᵢⱼ ↦ yᵢyⱼ+yⱼyᵢ.

Include all original names, placeholder names, axiom polynomials and
their ordered associations. Fix an ordinary explicit binary encoding and
put Q=2+|π|+|alphabet|+|B with its placeholder dictionary|, before any
output graph is built. All written trees, reference and name bits count.
Define the ordered translation by

    tr(yᵢ)=yᵢ,  tr(false)=1,  tr(true)=0,
    tr(¬A)=1+tr(A),        tr(A∨B)=tr(A)tr(B).

An affine ABP means an explicit finite acyclic graph with affine edge
labels over F₂, ordered path products, and designated endpoints; empty
paths contribute 1. No circuit-valued edges or implicit graph is allowed.

## Conclusion

A deterministic construction produces an affine ABP K over precisely
the original alphabet and dictionary, satisfying the formal identities

    K(y,0)=0,                  K(y,B(y))=tr(T).

Its full binary size is at most C Q¹⁴ for a fixed encoding-dependent C,
and its construction takes deterministic polynomial bit time in Q.
No proof-tree unfolding, Boolean-equivalence test or PIT is required.
The output may retain unused graph components and the full dictionary.

This is an informal specialization/reproduction of known extraction and
graph-composition machinery with changed exact rule identities. The separate
step-428 critical audit below found no substantive defect within these
hypotheses; no all-size verified implementation or certified originality is claimed.
It supplies extraction from a supplied legal proof only. It
does not prove constant-bearing template completeness, repair the old
source system, or establish L097/L098/L106 composition, short source
proofs, M-only witness bounds, arbitrary ER data or any SAT conclusion.

## Proof

### 1. Sources, scope and received correction components

Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley (1967),
§2.6 p.21 specifies the propositional axiom and four rules above;
§3.1, Tautology Theorem (Post), p.27, proof pp.28–30, gives completeness
([primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf)).
The constant axioms are local additions, not attributed to that source.
Completeness is background motivation, not a premise needed for extracting
from a supplied legal proof. In particular, no claim about constant-bearing
template existence is inferred here from that theorem.

Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional
Proofs as Non-Commutative Formulas*, SIAM J. Comput. 47(4), 1424–1462
(2018), [DOI](https://doi.org/10.1137/16M1107632), is the extraction
comparison. In the assessed
[40-page author manuscript](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
Definition 1.3 p.6 and Theorem 3.1/Lemma 3.3 pp.13–14 give the translation
and formula extraction with three axiom schemes/MP after tree-like
conversion, over Q or a prime field. The revision date of this manuscript
is not established. We do not import its tree-ancestry bound for this DAG
or its axiom cases for the four changed rules. The saved step-425
assessment covers these source passages and the specialization below.

Use L035 for original-only affine graphs u,v to obtain W(u,v), with
W(u,v)(0)=0 and W(u,v)(B)=uv+vu. Retain its full pair-once commutator
dictionary, adding the unused Boolean entries of B. Use L036 on an
original-only affine graph u to obtain H(u), with H(u)(0)=0 and
H(u)(B)=u²+u. These inputs may be zero or constant and include their full
dictionaries. Their respective full size bounds are O(E⁴) and O(E⁶),
with deterministic polynomial construction time for full input E. The
sharper logarithmic bounds are unnecessary here. The constructions are
received with their audited qualifications, not reproved.

We adapt the right-transition design described in L097 §4, but prove its
receiving graph identities below for these different rules. No use is
made of L097's unsupported source-template completeness or its overall
conclusion. The additional proof is necessary because the inspected LTW
cases do not establish the exact four rule recurrences or their common
multiplication orientation.

### 2. Original-only graphs and the exact local identities

Every tr(A) used below has an original-only graph with O(|A|+1) records.
To see this without expanding words, use a two-vertex edge graph for an
atom or scalar, disjoint series composition for an ordered product, and
disjoint parallel composition with a constant-one branch for 1+u.
Fresh exterior endpoints and constant-one connectors give every graph
distinct source/sink, with no incoming source or outgoing sink edges.
Each syntax node contributes O(1) new records and copies each child
occurrence once. The zero scalar can be a graph with no path. Formula
arguments are trees, so this is linear in their written occurrences.
All copied variable names and dictionaries are charged in §4.

For a proof line i let Pᵢ be its translated formula. Write a=tr(A),
b=tr(B), c=tr(C) for the actual argument translations at that line.
These letters denote original-only polynomials, never earlier witnesses.
Define witnesses inductively by the following recurrences. Every W or H
occurrence is a newly constructed independent correction block.

**Propositional axiom.** Set Kᵢ=H(a). Its substituted value is
a²+a=(1+a)a=tr(¬A∨A), in the free algebra. Its zero-placeholder value
is zero by L036.

**Ground axioms.** Set Kᵢ=0, represented by distinct endpoints with
no accepting path. The two translated conclusions are respectively 0
and 1+1=0. Keep the full dictionary even though the graph uses no symbols.

**Expansion.** For premise j:A, set

    Kᵢ=Kⱼ b+W(a,b).

At B this is ab+(ab+ba)=ba=tr(B∨A). No factors have been commuted
without a correction. Both summands vanish at zero placeholders.

**Contraction.** For premise j:A∨A, set

    Kᵢ=Kⱼ+H(a).

At B this is aa+(aa+a)=a. Both summands vanish at zero placeholders.

**Association.** For premise j:A∨(B∨C), set Kᵢ=Kⱼ.
The translated premise is a(bc), the conclusion (ab)c; these are equal
by associativity of the free algebra. This identifies polynomials only:
the input proof still contains and checks the two exact formula trees.
Zero-placeholder vanishing is preserved.

**Cut.** For premises j:A∨B and h:¬A∨C, set

    Kᵢ=Kⱼ c+Kₕ b+(1+a)W(b,c).                         (1)

The first two substituted terms are abc+(1+a)cb=abc+cb+acb.
The local correction substitutes to

    (1+a)(bc+cb)=bc+cb+abc+acb.

Adding the displayed words in characteristic two cancels abc, cb and
acb in pairs, leaving exactly bc=tr(B∨C). This calculation is a formal
identity for arbitrary noncommuting a,b,c; no Boolean reduction or
commutation of a witness is used. At zero placeholders both earlier
witnesses and W(b,c) vanish, so (1) vanishes as well.

Each earlier witness in these recurrences receives only a right
multiplier: b, c or 1. The sole displayed left multiplier (1+a) is part
of a separately constructed local seed, whose W inputs are b and c,
both original-only. The same is true of every other correction call.
The formulas and identities include arbitrary constants, empty alphabets,
zero translations and cancellations. Coincident premise indices cause
no algebraic difficulty: both summands are retained with multiplicity.

### 3. One acyclic graph, with no ancestry copying

Equivalently each recurrence has the form

    Kᵢ=Zᵢ+sum over incoming rule occurrences (Kⱼ Rⱼᵢ),

where Zᵢ is the local seed (H(a), zero, W(a,b), H(a), zero,
or (1+a)W(b,c), in the cases above), and each Rⱼᵢ is an
original-only graph for b,c or 1. There are at most two incoming rule
occurrences per line and at most one correction block per line.

Create a fresh source s and distinct vertices vᵢ for all proof lines.
Attach one disjoint graph for Zᵢ from s to vᵢ using constant-one
connectors whenever a seed is retained. A zero seed may be represented
by a disconnected two-vertex graph or omitted; it adds no accepting
path. For each incoming occurrence j→i attach its own disjoint graph
Rⱼᵢ from vⱼ to vᵢ. For multiplier 1 a single constant-one edge
suffices. Cut's local seed is a series product of a graph for 1+a and
the independently built W(b,c); it has no entry from a proof vertex.
All internal block vertices are fresh. Parallel transitions, including
ones with equal premise indices, are kept separately.

The correction graphs from L035/L036 are acyclic. If necessary give
any supplied correction block a fresh exterior entry/exit and constant
connectors. A path leaving its designated exit along an internal edge
cannot return to exit without a cycle, so these wrappers preserve its
path polynomial even with nonextremal or coincident designated roots.
In the outer graph each block is traversed only in its stated direction.
Every proof transition increases its proof-line index. A cycle within
a block is impossible, and a cycle through different proof vertices
would require indices to decrease. The source has no incoming edge.
Thus the complete graph is acyclic.

Every s-to-vᵢ path ends either through its seed attachment or through
one of its incoming transitions, with ordered product equal to an
s-to-vⱼ path product followed by a path product of Rⱼᵢ. Disjoint
block interiors make these alternatives exhaustive and disjoint as
paths, even when their contributions cancel as polynomials. Therefore
the path sum obeys exactly the displayed recurrence. Induction on i,
using §2, proves both formal identities at every proof vertex.
The designated output is the final-line vertex. There is no accepting
path starting independently of a seed. No recursively expanded Kⱼ
is copied, and outgoing transitions do not change a path sum ending
at vⱼ. Unused proof lines may be retained without changing this argument.

### 4. Full size and construction-time ledger

All source line counts, written syntax occurrences and name lengths
are O(Q); the full supplied alphabet and dictionary each have size O(Q).
There are O(Q) local correction calls and O(Q) transition occurrences.
Even when counted independently at each use, each original-only argument
or multiplier tree used in one block has O(Q) nodes, with at most a
constant number of copies needed in that block.

The tree construction in §2 has O(Q) vertices/edges per such graph.
Copying a written name pessimistically costs O(Q) bits per occurrence;
binary endpoints cost O(log(Q+2)) bits. Retaining the entire dictionary
in each separate correction input costs O(Q). Thus the full input E
to every L035 or L036 call is at most C₀Q², including both operands
when applicable, all roots and framing. No bound on recursively
generated witnesses is used in this estimate.

L035 then gives at most C₁Q⁸ full bits for a W block and L036 at most
C₂Q¹² for an H block. Cut adds one O(Q²)-bit original-only prefix;
other seed and transition connectors add only O(Q²) bits per line.
Summing all independent blocks, including unused ones, costs O(Q¹³)
bits before final global renumbering. Their total record and label-entry
counts are bounded by the same quantity. A global vertex identifier
has O(log(Q+2)) bits since there are O(Q¹³) records. Replacing every
local reference by a global reference and allowing this logarithmic
factor even on the whole preceding bound gives O(Q¹³ log(Q+2)),
hence at most C Q¹⁴ full bits. Retaining every intermediate dictionary
copy would already fit the estimate; the final output uses one unchanged
B with the original ordered associations and names. Local references
are relocated to those entries, never to fresh algebraic variables.
Root records, all connectors and the original-name dictionary are paid.

For bit time, syntactic rule checking and argument extraction require
only comparisons of written trees and backward references, polynomial
in Q. The formula graph construction is explicit serial/parallel
copying. Each L035/L036 construction takes a fixed polynomial in its
full input E≤C₀Q²; there are O(Q) such calls. Their sum is a fixed
polynomial in Q. Global renumbering, dictionary matching and writing
the O(Q¹⁴)-bit output likewise take polynomial bit time using even
straightforward explicit scans. There is no monomial, assignment or
complete proof-path enumeration in this algorithm.

This meets the required fixed-polynomial threshold for the supplied
proof. The exact word expansions in §2 and the all-size path/ledger
arguments are the mathematical checks for this step; no finite program
test or verified implementation is claimed. The source-template and
downstream composition gaps named in the conclusion remain independent.

### 5. Independent all-size critical audit — step 428, 2026-10-23

This audit receives the exact hypotheses above and the previously audited
L035/L036 contracts. It reuses the step-425 primary-source comparison;
no completeness theorem is needed to validate extraction from a supplied
legal proof. It establishes no stronger conclusion and runs no finite
implementation. The source-template failure in L107 and Attempt 036 is
not a premise of, or repaired by, this extractor.

**Rule and substitution check.** Treat a,b,c as arbitrary elements of
the original free algebra, without Boolean reduction. The propositional
axiom has translation (1+a)a=a+a², exactly L036's target. The two ground
axioms translate to 0 and 1+1=0. Expansion gives ab+(ab+ba)=ba;
contraction gives a²+(a²+a)=a. Association uses only the associative
algebra law, with the syntactic premise and conclusion still checked
separately. For cut the three contributions, in their written order, are

    abc,       cb+acb,       bc+cb+abc+acb.

Every word other than bc occurs twice, so the sum is bc. In particular,
the correction prefix stays to the left of W(b,c), whereas both earlier
witnesses stay to the left of their right multipliers. None of these
checks interchanges factors or uses an identity of placeholder witnesses
as an input to L035. All H operands and both operands of every W are
original-only graphs obtained directly from actual argument trees.
Adding unused Boolean entries to L035's framing does not change its
polynomial or identities; the pair-once tau positions agree with B.

Under zero-placeholder substitution every seed is zero, including the
cut seed (1+a)W(b,c); by induction every incoming K_j R_ji is zero.
Under B substitution the preceding ordered calculations identify the
same recurrence with the translated conclusion of each rule. These are
two homomorphisms of free algebras, not evaluations on Boolean assignments.
They remain valid for zero or scalar argument polynomials and an empty
alphabet. No nonzero-polynomial or path-existence promise is introduced.

**Graph check.** A syntax-tree induction pays each child occurrence once:
an atom/scalar uses constant size, a negation uses one parallel scalar
branch and constant-size framing, and an OR uses ordered series
composition and constant-size framing. It gives O(|A|+1) graph records
without distributing a product over a sum or expanding paths. This
construction can always use distinct exterior endpoints.

For an imported correction block, the wrapper has its only external
entry at its designated start and its only external exit at its
designated end. A complete traversal is therefore exactly a designated
path of that block. A path that passes its end but continues internally
cannot return to take the exit connector in a DAG. When the designated
endpoints coincide, the empty internal path is received once; no positive
length return path is possible. Dead vertices and no-path blocks add no
accepting traversal. This also justifies the serial cut prefix, including
constant or cancelling factors, without deleting any necessary paths.

Independently check global acyclicity by projecting any proposed cycle
that meets proof vertices onto its successive such vertices. A completed
transition goes from j to i with j<i. A seed can be entered externally
only from s, which has no incoming edge. Thus no such projected cycle
exists; a cycle meeting no proof vertex would lie inside an acyclic
block. Fresh block interiors prevent all other cross-block connections.

Every accepting path starts through exactly one seed attachment. Its
last arrival at v_i is through that line's seed or one specific incoming
rule-occurrence block. In the latter case splitting at v_j gives exactly
an s-to-v_j path followed by a designated R_ji path. Conversely every
such pair concatenates legally: freshness and increasing indices prevent
any repeated vertex. This is a bijection of paths before cancellations.
Distinct incoming occurrences remain distinct choices even if their
labels or premise vertices agree. Finite distributivity gives exactly
Z_i+sum_j K_j R_ji, with multiplicity. Outgoing transitions cannot change
a path sum ending at v_i. Retaining unused lines, even lines later than
a selected output, adds no paths back to that output. There is no direct
source-to-output edge bypassing the seeds. Sharing consequently changes
neither substitution identity and never copies a prior witness graph.

**Independent original-input ledger.** Let N be the number of supplied
lines. Explicit encoding gives N≤cQ and at most 2N transition occurrences.
Every individual written argument has at most cQ syntax nodes and name
bits bounded by cQ. A constant number of original-only argument copies
therefore has O(Q) records and at most O(Q²) full bits, including all
local endpoints and the complete O(Q)-bit dictionary. This bounds each
correction call's actual full input by E≤c₀Q², before any witness is
constructed; extra unused original symbols are already in that charge.

The imported O(E⁴) and O(E⁶) bounds pay, respectively, O(Q⁸) and
O(Q¹²) full bits per W or H call, including their own internal copies.
There is at most one call per line. All cut prefixes, transition graphs,
exterior wrappers and proof vertices add O(Q³) bits in aggregate.
Thus the disjoint block encodings total at most c₁Q¹³ bits. In particular
their total records and label entries are at most c₂Q¹³. Dense global
vertex and dictionary references need at most c₃ log₂(Q+2) bits each;
all original long names remain in their charged dictionaries, rather
than being reintroduced at every dense reference. Relocating every
reference, retaining even all intermediate dictionaries, and writing
the roots and output framing costs at most c₄Q¹³ log₂(Q+2)≤C Q¹⁴
for Q≥2. The required exponent therefore survives in the unchanged Q.

If d bounds the fixed polynomial construction-time exponents in L035
and L036, all calls together take O(Q^(2d+1)) bit operations up to a
fixed constant. Tree matching, graph copying, explicit dictionary scans
and reference relocation add a fixed polynomial in Q and output length.
The audit uses no efficiency claim for free-word expansion, assignment
enumeration or path enumeration. No newly generated object enters Q.

**Verdict and limits.** No substantive algebraic, endpoint, sharing or
encoding defect was found. Both formal identities and the C Q¹⁴ full
bound pass this independent all-size informal audit, conditional on the
stated L035/L036 inputs. No theorem statement, recurrence, construction
or exponent required repair. This validates a local supplied-proof
receiver, not a new discovery beyond the inspected sources or a complete
P-versus-NP argument. Constant-bearing template completeness,
L097/L098/L106 composition, actual occurrence/original-Q integration,
short proofs, M-only bounds, universal W₂, arbitrary ER data and SAT
remain unresolved. No implementation or Mathlib result was verified.

### 6. Bounded serialized exercise reception — step 449, 2026-10-24

This is a finite implementation reproduction of §§2–3, using the existing
L035/L036 constructors and the unchanged step-448 SPECIALIZE assessment.
It changes no hypothesis, recurrence or all-size bound. The supplied input
is exactly `scripts/parity-four-rule/output-goal-directed-447/checker-exercise.jsonl`,
SHA256 `9265d9b95dac5d2c1dcb549722b412454380b21b11d7d116e93cde479b558d7c`:
nine legal assumption-free records over the ordered alphabet A,B, ending
at the exact tree A∨¬A. Both ground axioms and all four rules occur.
Lines 3–4, which contain B, are unused by the final cut; they are retained.

Reproduce with `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/emit.py`,
then `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/receive.py`
and `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/mutations.py`.
The complete certificate, unchanged source copy, per-block/per-root free-word
polynomials and mutation certificates are in
`scripts/four-rule-extraction/output-449/`. `certificate.json` writes the
full A,B dictionary with σ_A, σ_B, τ_AB, their ordered axiom polynomials,
the collision-free dense-name transport, every seed/transition graph,
all block intervals/attachments and nine indexed source-line roots.
No original name or unused dictionary entry is deleted.

The emitter uses actual ordered trees to build original-only correction
arguments; imported witnesses are never correction operands. It attaches
independent seeds and right-multiplier blocks to shared proof vertices,
retaining cut's left prefix only inside its seed. The receiver imports
neither emitter nor correction evaluators. It reuses the unchanged literal
source checker, validates exact source/dictionary/transport and graph schema,
rejects bool-as-int indices, checks acyclicity and the complete fresh block
partition/connectors, and reconstructs argument translations independently.
Backward ordered free-word arithmetic checks every block's zero/substituted
identity and every transition's original-only free polynomial, then both
formal identities at all nine roots. This verifies the saved finite objects;
it is not a general efficient PIT algorithm or a separate critical code audit.

Declared caps precede execution: 2,000,000 vertices plus edges,
200,000,000 certificate bytes, 1,000,000 intermediate polynomial words,
word length 256, 100,000,000 multiplication pairs per complete reception,
and 20,000,000 accumulated stored polynomial words per root traversal.
Construction preflights copied-record counts. The certificate has 7,443
vertices, 8,333 edges and 151,816 bytes. Reception uses 35,457 multiplication
pairs, at most four words in a polynomial, word length four and 4,223
stored words; no cap is exhausted. All 15 blocks and nine roots pass.

The complete final free polynomial is σ_A; its zero substitution is 0,
and its axiom substitution is A+A², exactly tr(A∨¬A). The B-containing
line-3 root has free polynomial
τ_AB+Aτ_AB+σ_A B+τ_AB A; it substitutes to BA+BA².
Deleting that seed's tau labels instead gives AB+A²B at line 3 while
the final root still passes. The receiver rejects this damaged unused
branch. This is a discriminating test of the required all-line coverage,
not a new mathematical obstruction.

All 22 expected certificate corruptions and 20 preserved malformed-source
cases reject. One added pair of identical A label entries cancels in F₂
and correctly remains accepted; this is not counted as a missed mutation.
Full results are `reception.json` and `mutation-results.json` in the output
directory. No new lemma, certified originality, library preparation,
all-size executable efficiency, source-proof availability, L106 integration,
universal W₂, arbitrary ER data or SAT consequence is established. A separate
critical audit of the implementation and saved evidence was pending at step 449;
§7 records its separate finite verdict.
In this fixture the cut seed is formally zero and σ_B is unused: retaining
their records does not test a nonzero cut correction or a B-Booleanity seed.

### 7. Separate finite code/evidence audit — step 451, 2026-10-24

**Scope and inputs.** This audit uses the unchanged step-450 SPECIALIZE
assessment and the precise citations and local contracts in §1. It audits
the complete `emit.py`, `receive.py`, `mutations.py`, the used graph-copy,
normalization, Booleanity and marked-edge constructors, and the literal
source checker. It receives exactly §6's source SHA, nine records and full
A,B/σ_A,σ_B,τ_AB dictionary. No library synthesis, additional fixture or
new theorem is undertaken. L107's old source interface and the bounded
preparation failures in Attempts 037/038 remain outside this audit.

**Source, graph and arithmetic inspection.** The source checker compares
literal ordered trees for each of the four rules, enforces each arity and
strictly earlier integer references, and checks both ground axioms and the
final tree. Direct inspection of the nine records confirms these matches:
two propositional axioms, both ground axioms, two expansions, association,
contraction and cut. The source contains 42 formula nodes and 644 bytes.
The extractor's translation uses disjoint ordered products for OR and a
constant-one parallel branch for negation. The marked-edge constructor
copies the four factors in L035's order; the Boolean constructor normalizes
labels, removes outgoing sink edges and realizes L036's suffix recurrence.
Every correction operand is an original-only formula/suffix graph.

The complete serialization retains vertices 0 through 9 as source and
line vertices, with all 15 block interiors partitioning [10,7443) and
all edge intervals partitioning [0,8333). Each block's last two edges are
exactly its prescribed entry/exit connectors; every other edge stays
inside its fresh interval. The receiver checks these facts, the complete
original-only transition labels, exact argument trees and each parent
index, in addition to acyclicity and all nine roots. Thus a seed has its
only outside entry at the source, while a transition enters from its
specified earlier proof vertex. This realizes §3's right-multiplier
recurrence without an unaccounted cross-block path. Cut's prefix is
confined to its local seed. Full dictionary equality and the literal
dense-name transport preserve all associations, including unused σ_B.

The receiver uses backward ordered word-set arithmetic and imports no
emitter or correction evaluator. Its source checker is shared, so source
reception is not implementation-independent at that layer: the exact
rule comparisons were inspected directly. The general source checker
alone does not reject duplicate JSON keys; the finite receiver additionally
pins the raw source SHA and reparses with a duplicate-key hook. The outer
certificate uses that hook as well. Integer fields use exact types.

The separate `scripts/four-rule-extraction/audit.py` defines forward FIFO
topological propagation and integer coefficient accumulation reduced
modulo two. This arithmetic calls neither imported evaluator; separate
replay/rebuild phases do import the receiver and emitter modules. It reads
every serialized edge and recomputes all free, zero and axiom-substituted
polynomials at all nine roots and in all 15 blocks. Every complete polynomial
and target agrees with `output-449/reception.json`; this includes canceled
paths, empty words, unused lines, and the internal contraction correction.
The backward receiver's saved polynomials, metadata and stable counters
also replay exactly; transient word counts are qualified below.
Rebuilding in `output-451/rebuilt/` reproduces the complete
151,816-byte certificate byte for byte, including all graph records and
construction counters: 18 commutator calls and a conservative maximum
preflight charge of 15,782 records. Those counters are constructor reports,
not independently authenticated by merely receiving their integer fields;
the rebuild and inspected preflight formulas justify them for this fixture.

**Detected reception defect and repair.** Before repair, comparing the
`source_check` dictionaries by Python equality accepted `1` instead of
the Boolean `true`, `true` instead of the integer rule count 1, and `9.0`
instead of the integer record count 9. This follows from Python's numeric
equality and is reproduced separately for all three fields. It violates
exact typed retention of the checker evidence, although the actual source
is still checked and all graph identities remain valid. The pre-repair
receiver and complete accepted mutations are preserved in `output-451/`.
The repaired receiver compares canonical sorted JSON serializations of
the freshly computed and retained checker evidence; these three typed
values then differ and reject. Duplicate certificate keys also reject.
No graph, dictionary, recurrence, original certificate or source was changed.

**Complete finite evidence and bounds.** Reproduction command:
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit.py`.
All 22 saved certificate rejections and 20 saved source rejections replay
with their exact reasons; complete mutation differences and source texts
are retained in `output-451/mutation-replay.json`. The identity-neutral
pair of A label entries remains accepted. Independent forward evaluation
of the damaged unused seed reproduces failure at line 3 and success at
line 8, confirming that a final-root-only test would miss this corruption.

The unchanged graph uses 15,776 vertices-plus-edges against 2,000,000
allowed and 151,816 bytes against 200,000,000 allowed. The full receiver
uses 35,457 multiplication pairs against 100,000,000, four polynomial
words against 1,000,000, word length four against 256, and 4,223 accumulated
table words against 20,000,000. The independent forward audit, including
its unused-branch check, uses 26,554 pairs, four words, length four and
3,334 stored table words under the same caps. Its different traversal
and shared all-root forward table explain the different counters; equality
of these two implementations' counters is neither expected nor asserted.
No cap is increased. All 50 output-449 files retain their original bytes.
Complete results, polynomials, code/input hashes, repaired-type tests and
actual/required bounds are in `scripts/four-rule-extraction/output-451/`.

An intermediate audit-harness run required exact equality of the damaged
branch's transient word maximum and failed; its report remains in
`output-451/audit-failure.json`. The receiver iterates salted-hash word
sets, so parity cancellation can give different transient maxima while
the completed polynomials agree. Eight fixed hash seeds 0–7, recorded with
the complete test program and polynomials in `hash-order-diagnostic.json`,
give maxima 2 or 3 for that probe, always the same 1,316 multiplication
pairs, maximum word length 3 and 541 stored words. Seed 0 reproduces the
saved maximum 3. The corrected audit compares every complete polynomial
and the stable counters, records both transient maxima and verifies the
unchanged cap; it does not demand identical transient set iteration.
This was an audit-harness overconstraint, not failed polynomial evidence.

**Verdict and limits.** The saved finite algebraic certificates and the
repaired strict receiver pass this separate audit. The detected flaw was
in evidence typing, not the formal identities or L108's abstract theorem.
This supplies independent local verification and a reception repair, not
mathematics beyond the checked sources. The cut seed is zero and σ_B is
unused; no nonzero-cut or B-Booleanity implementation coverage follows.
Finite word expansion has no asserted all-size polynomial-time bound.
Prepared libraries, general short source proofs, L106 integration, M-only
bounds, universal W₂, arbitrary ER data and unrestricted SAT remain open.

### 8. Nonzero cut and used B-Booleanity finite fixture — step 453

This specializes the same hypotheses and constructions under the unchanged
step-452 SPECIALIZE assessment. It adds finite implementation coverage,
not a new theorem or certified originality. The exact supplied source is
`scripts/four-rule-extraction/nonzero-source.jsonl`, independently pinned
in the emitter, receiver and forward check to SHA256
`004ca652885f26286b576af5b923b89bac8f1f933dedc9c6b800677c564f9335`.
Its alphabet is the unchanged ordered A,B and its exact final tree is
`A∨(¬B∨B)`. All nine zero-based records are as follows; parentheses are
literal trees, not implicit associativity rewrites.

| Line | Formula | Justification |
| --- | --- | --- |
| 0 | ¬A∨A | axiom with argument A |
| 1 | ¬B∨B | axiom with argument B |
| 2 | true | ground axiom |
| 3 | ¬false | ground axiom |
| 4 | ¬¬A∨(¬B∨B) | expansion of line 1 by ¬¬A |
| 5 | (¬B∨B)∨(¬B∨B) | expansion of line 1 by ¬B∨B |
| 6 | ¬B∨B | contraction of line 5 |
| 7 | (¬¬A∨¬B)∨B | association of line 4 |
| 8 | A∨(¬B∨B) | cut of lines 0 and 4, pivot formula ¬A |

This table manually checks every literal inference separately from the
shared source checker. In particular line 4's left argument is exactly the
negation of line 0's left argument. Lines 2,3,5,6,7 remain unused by line 8.
No assumption, double-negation rewrite or completeness theorem is used.
The full source has 46 formula nodes and 682 bytes. The complete ordered
σ_A, σ_B, τ_AB dictionary, axioms and dense-name transport are retained.

Reproduce, in order, with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/emit_nonzero.py`,
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/receive_nonzero.py`
and `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/check_nonzero.py`.
The fixture-specific emitter and receiver copy the audited §7 interfaces
with only their source SHA, source/output paths and receiving goal changed.
The fixed nine-root/count/sink bindings and strict typed evidence checks
remain. The receiver imports no constructor or correction evaluator.
The forward check independently uses FIFO integer-coefficient accumulation
modulo two, rather than the receiver's backward symmetric-difference
arithmetic. It compares the complete free/zero/substituted polynomials
at all nine roots and all 15 blocks, including unused ones. The independent
arithmetic is reused from §7, not a new all-size identity-testing claim.

Write σ=σ_A, ρ=σ_B and τ=τ_AB, as independent noncommuting placeholders.
The complete final free polynomial, regrouped without changing order, is

    K = σ(B+B²)+ρ A²+(τ+Bτ+τB)A+A(τ+Bτ+τB).

Its zero-placeholder substitution is zero; its axiom substitution is
AB+AB², exactly tr(A∨(¬B∨B)). Every term in this displayed free polynomial
occurs in the complete retained root-9 evidence.

**Load-bearing contributions.** Block 12 is line 8's cut seed. Its actual
arguments have translations a=1+A, b=A, c=B+B². The free seed and its
substitution, checked completely by both arithmetic implementations, are

    D_cut = Aτ+ABτ+AτB,
    D_cut(B) = A²B+ABA+A²B²+AB²A.

The four displayed original words are distinct, so this value is nonzero.
The seed is attached directly to the final root, with unit continuation;
its entire final contribution is exactly D_cut, not merely a reachable
graph component. Block 1 is line 1's B-Booleanity seed. Its free value is
ρ, and the two used right multipliers, from line 1 to 4 to 8, are A,A.
Its exact final contribution is therefore ρ A², substituting to
BA²+B²A², again two distinct original words. This identifies the selected
σ_B-dependent component by its block provenance, without conflating it
with σ_B occurrences in unused seeds.

In separate saved diagnostic copies, erase τ_AB entries only inside the
cut seed, or σ_B entries only inside block 1. Source, dictionary,
connectors, partition and all other graph records stay fixed. Strict
reception rejects at `block 12 substituted identity` and `block 1
substituted identity`, respectively. Independent full-graph evaluation
also gives changed final substituted values

    AB+AB²+A²B+ABA+A²B²+AB²A          (cut seed deleted),
    AB+AB²+BA²+B²A²                   (selected σ_B deleted).

Both differ from AB+AB², and the corresponding local line roots fail.
The check subtracts the complete changed graph polynomial from the
accepted graph polynomial in all three modes, retaining all other seeds
and cancellations. Full polynomials, intervals, mutations and exact
provenance are in `scripts/four-rule-extraction/output-453/contributions.json`
and `mutation-results.json`. An initial connector-disable diagnostic also
failed the final identity but was rejected earlier at connector syntax;
its results and program are preserved in `output-453/connector-diagnostic/`.
The final diagnostics above delete internal seed labels and reach the
intended block identity tests.

**Actual versus required resources.** The certificate has 8,247 vertices,
9,330 edges (17,577 total against 2,000,000) and 169,647 bytes against
200,000,000. The complete receiver uses 45,038 multiplication pairs against
100,000,000, at most nine polynomial words against 1,000,000, word length
four against 256, and 4,223 stored table words against 20,000,000. The
independent forward check, including the two complete deletion diagnostics,
uses 54,530 pairs, at most nine words, length four and 4,438 stored words,
under the same caps. The construction preflight maximum is 17,583 records;
all 14 commutator calls satisfy their exact retained-copy counts. No cap
is raised. Full actual/required bounds, code hashes and certificate digest
are in `output-453/verification.json`; complete independent and receiver
polynomials are in `independent-polynomials.json` and `reception.json`.

All 24 expected certificate corruptions reject, including both deletions,
dictionary/transport/provenance defects, bool/float indices, all three
typed-evidence aliases and duplicate JSON keys. Fourteen mutations of this
actual source reject, covering every rule, references, names and endpoint.
A pair of identical A label entries cancels and correctly stays accepted.
All 67 previously existing files in outputs 449/451 keep their recorded
hashes; original programs and archives are unchanged.

This establishes the approved finite discriminators under the supplied
contracts and bounds. The separate step-455 audit of these changed bindings,
diagnostic programs and complete evidence is recorded in §9. It supplies no
library preparation, all-size executable efficiency, general short proofs,
L106 integration, M-only bound, universal W₂, arbitrary ER data or SAT
decision/separation. Full Mathlib coverage remains unchecked as below.

### 9. Separate nonzero-fixture critical audit — step 455, 2026-10-24

**Scope and source use.** This audit uses the prior step-454 SPECIALIZE
assessment, the exact hypotheses of §8, and the precise citations and
audited L035/L036 contracts in §1. It audits the complete fixture-specific
emitter, strict receiver and forward diagnostic, together with their used
literal source-checker and correction/copy interfaces. No theorem is
reproved, new fixture introduced or all-size implementation claim made.
Attempts 037/038 remain parked preparation failures; the previous §7
audit's zero cut and unused σ_B did not certify these changed contributions.

**Source and graph authorization.** Direct comparison of all nine records
with the literal rules confirms the §8 source table. In line 8 the cut's
first left argument is ¬A and its second left argument is exactly ¬¬A;
the right arguments are A and ¬B∨B. This uses no double-negation rewrite.
Line 7 associates line 4 in the permitted direction; line 6 contracts
the two identical copies in line 5. Lines 2 and 3 are precisely the two
local ground axioms. Their shared software checker is therefore supported
by direct syntactic inspection, not counted as two independent checkers.
Raw source SHA, ordered A/B alphabet, literal goal and complete dictionary
match their independently pinned receiver values.

The complete received graph has source/line vertices 0 through 9, fresh
block interiors partitioning [10,8247), and edge intervals partitioning
[0,9330). Every interior edge stays inside its own block. Each block's
last two edges are its prescribed entry/exit connectors, so earlier roots
enter only their corresponding right multipliers; a seed enters only
from vertex 0. Every reference is strictly backward. Acyclicity, exact
arguments, transition labels and the full partition are checked on the
actual serialization. Cut's A prefix lies inside block 12, not on an
incoming earlier-witness edge. Imported constructors copy L035's four
subgraphs in the required order and L036's independent suffix blocks;
every correction operand remains original-only. Constants, dead paths,
cancellations and unused lines are retained.

**Complete arithmetic and contribution check.** The inspected backward
receiver and forward FIFO integer-coefficient evaluator use different
propagation directions and arithmetic representations. Neither imports
the other's polynomial evaluator. Replaying both reads every graph edge,
checks every one of the nine roots and 15 blocks in free, zero and full
substitution modes, and compares the complete saved polynomials. All agree.
The final free polynomial has exactly the nine words displayed in §8's K,
and its substituted value is exactly AB+AB², with zero-placeholder value 0.

The full cut seed is Aτ+ABτ+AτB. Substituting τ=AB+BA gives
A²B+ABA+ABAB+AB²A+A²B²+ABAB; the two ABAB occurrences cancel,
leaving exactly A²B+ABA+A²B²+AB²A. Its only continuation is the final
unit connector. For block 1 the entire seed is ρ; the only route from
line 1 to the final line goes through line 4 with right multipliers A,A.
Its whole final contribution is therefore ρA², substituting to BA²+B²A².
The other uses of line 1 terminate at unused roots and do not alter this
contribution. Both substituted word lists are nonempty and have distinct
words; this is formal nonvanishing, not Boolean evaluation or reachability.

The complete serialized differences independently confirm that cut deletion
changes only the tau labels at edges 9179 and 9268, inside block 12's
interior; selected Boolean deletion changes only the sigma_B label at edge
29, inside block 1. All other labels, metadata, vertices and connectors
are identical. Thus every other seed contribution is retained. Each
damaged graph is fully reevaluated in all three modes. Subtracting it from
the accepted graph gives exactly the preceding local/final contributions,
and its final substituted polynomial differs from AB+AB² by that nonzero
contribution. Strict reception rejects at the respective block 12 and
block 1 substituted-identity tests. The older connector diagnostic instead
changes edge 9315 from [1] to []; its final identity also fails, but its
receiver rejection is at connector syntax. It is preserved separately
and is not used as the internal-deletion evidence.

**Reconstruction, typing and bounds.** Rebuilding with the inspected
emitter reproduces all 169,647 certificate bytes, including every graph
record and construction counter. The 14 commutator calls verify their
exact copied-record counts before output; maximum construction preflight
is 17,583 records, below 2,000,000. Constructor counters are advisory in
the receiver: their values are authenticated here by the rebuild and
inspected counting formulas, not merely by accepting their integer types.

All 24 saved certificate rejections and 14 saved source rejections replay
with identical complete mutation bytes, edit lists and reasons. The
identity-neutral duplicate-A variant is accepted. Exact-type checks reject
Boolean/float indices and counters; canonical JSON comparison rejects all
three numerical aliases in source evidence. Duplicate certificate keys
reject, and the fixed source is SHA-pinned and reparsed with duplicate-key
rejection. This audits this finite receiver, not unrestricted safety of
the shared source checker on arbitrary inputs.

| Resource | Actual | Unchanged cap |
| --- | ---: | ---: |
| Final graph vertices plus edges | 17,577 | 2,000,000 |
| Certificate bytes | 169,647 | 200,000,000 |
| Polynomial words | 9 | 1,000,000 |
| Word length | 4 | 256 |
| Multiplication pairs, backward / forward with deletions | 45,038 / 54,530 | 100,000,000 per check |
| Stored table words, backward / forward | 4,223 / 4,438 | 20,000,000 per traversal |

Extra instrumentation also measures every unreduced forward Counter before
parity cancellation: at most nine words of length four, within the same
caps. Counts apply to the specified traversals, not total process memory
or an aggregate budget over all separate mutation checks. Transient
backward set maxima need not be invariant under hash iteration; complete
polynomials and stable counters are compared, and all maxima are capped.

Reproduce with `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_nonzero.py`.
Full polynomials, rebuild, mutations, code hashes, exact differences,
actual/required bounds and the preservation manifest are in
`scripts/four-rule-extraction/output-455/`. All 127 tracked input/archive
files, including outputs 449/451, all of output 453 and its initial
connector diagnostic, retain their original bytes.

**Verdict and limits.** No substantive defect was found in this changed
finite implementation or its algebraic evidence; no original program,
certificate, rule, identity or resource cap required repair. This is new
local verification evidence under the inspected contracts, not a theorem
beyond those sources or certified originality. The finite code and word
expansion do not establish an all-size executable efficiency theorem.
Prepared libraries, general short source proofs, L106 integration, M-only
bounds, universal W₂, arbitrary ER data and unrestricted SAT remain open.

### 10. Bounded parameterized supplied-proof implementation — step 457

This REPRODUCTION implements §§1–3 under the pre-existing step-456
SPECIALIZE assessment; it proves no new algebraic statement or stronger bound.
The primary sources and their qualifications remain those in §1. The new
programs are `scripts/four-rule-extraction/parameterized_input.py`,
`emit_parameterized.py`, `receive_parameterized.py` and `test_parameterized.py`.
They preserve the old programs and every archive in outputs 449/451/453/455.

**Exact bounded interface.** The caller separately selects the source file and
an `L108-request-v1` manifest containing its expected SHA256, exact goal tree,
ordered alphabet and full dictionary. Neither authorization is recovered from
a candidate certificate. The source must be nonempty `literal-four-rule-v1`,
with the exact seven tags and literal rules in the hypotheses. Complete raw
source text, all source roots and all unused names/records are retained.
Dictionary entries may occur in any caller-supplied order; each Boolean and
each index-increasing pair occurs exactly once, with its exact ordered words.
Placeholder display names are distinct among placeholders. Typed namespaces
permit a placeholder display name also to be an original display name.

Internal constructor tokens x1,…, b:i and t:i:j are relocated through the
checked complete symbol table into `['original',i]` and `['placeholder',j]`,
where j is the unchanged caller dictionary position. Scalar one is the
separate `['one']` tag. Thus original display `1` is never a scalar; atomic
strings `or` and `not` remain distinct from connective arrays. Original-only
checks precede every correction call; independent cut occurrences and all
source lines are traversed without set deduplication or ancestry copying.
The L035 exact-copy preflight precedes its internal loops; remaining graph
copies, prefixes, graph allocations and connectors have record preflights.

Both input paths have a 2,000,000-byte cap. Duplicate keys, noninteger JSON
numbers, excessive lexical nesting and malformed types are rejected before
rule checking; strict backward references exclude bool-as-int aliases.
Further fixed limits are JSON depth 160, formula depth 64, aggregate
source/request formula nodes 100,000, source records 10,000, originals 256,
dictionary entries 32,896, name bytes 4,096, total graph label entries
2,000,000 and label width 1,024. A dictionary cardinality check precedes
quadratic association construction. Certificate and evidence output stream
to capped files, retaining an explicit partial artifact on failure. These are
bounded serialization limits, not hypotheses added to the all-size theorem.
The six earlier diagnostic caps remain unchanged.

**Independent reception and complete evidence.** The receiver imports neither
emitter nor correction constructor/evaluator. It shares only strict input
reception, symbol indexing and the literal source checker. It type-checks all
graph labels/endpoints before adjacency allocation, verifies acyclicity and
complete fresh block partitions/connectors, and reconstructs every block's
arguments and right multipliers from the actual source. Backward free-word
F₂ arithmetic checks the seed zero/substituted contracts, all original-only
transitions, and both formal identities at every indexed source root. Type-
sensitive evidence comparison avoids numeric aliases and a second serialized
copy of the candidate. The saved certificate digest refers to the exact
bytes parsed. Exact-word diagnostics can reject large legal inputs at their
caps and are not the theorem's polynomial-time construction algorithm.
Constructor counters are reported bounded claims, not independently measured
construction cost; these caps do not bound all interpreter memory or work.

Reproduce with `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/test_parameterized.py`.
The complete accepted certificates, caller manifests, source bytes and every
root/block's free/zero/substituted/target polynomial are in
`scripts/four-rule-extraction/output-457/`. Its `summary.json`,
`accepted-cases.json`, `regressions.json`, `mutation-results.json` and archive
hash manifests retain full actual/required bounds and exact rejection reasons.
Six accepted inputs check 35 roots: both old nine-line sources, an eleven-line
reordered five-original source including `1`, `x1`, atomic `or`/`not` and an
unused name, empty/singleton alphabets, and a constant cut with an unused
original. Caller dictionaries reverse the constructor's usual ordering and
use colliding original/placeholder display names. All 192 complete old/new
root/block polynomial comparisons agree after typed dictionary transport.

There are 47 expected rejections and one correctly accepted neutral duplicate-
label cancellation. Rejections include source/request/dictionary substitutions,
duplicate keys, bool/float aliases, lost unused records, malformed graph
provenance, cycles, literal-rule defects and declared cap stops. Erasing the
nonzero cut seed or used Booleanity seed rejects at the exact block substituted
identity. The direct L035 preflight rejects 4,000,010 required records against
2,000,000 before copying. No accepted example exhausts a cap. Their maxima are
17,689 records / 2,000,000; 223,971 certificate bytes / 200,000,000; 45,260
multiplication pairs / 100,000,000; nine polynomial words / 1,000,000; word
length four / 256; and 4,223 stored words / 20,000,000. All 176 files in the
four older archives retain their hashes. Full input metrics and final script
hashes are recorded, rather than inferred from previews.

This is finite implementation evidence for the already audited supplied-proof
argument. The changed generic code and evidence await a separate critical
audit; no all-size code/resource guarantee, efficient general free-word verifier,
source-proof availability, library preparation, downstream integration,
M-only bound, universal W₂, arbitrary ER data or SAT conclusion is certified.

### 11. Separate parameterized code/evidence audit — step 459, 2026-10-24

**Hypotheses and scope.** Receive exactly §10's bounded supplied-proof
interface and the unchanged step-458 SPECIALIZE assessment. The mathematical
inputs are audited L035/L036 and §§1–5; precise primary citations and their
qualifications remain in §1. No completeness theorem, library search, new
algebraic identity or stronger resource theorem is imported. Caller-selected
source/request paths are trusted. SHA256 collision resistance is an engineering
provenance assumption for the second source read, not a mathematical proof of
byte identity against an unbounded adversary.

**Shared input review.** The complete `parameterized_input.py` was reviewed
separately from its consumers. Bounded reads precede JSON parsing; lexical
nesting excludes quoted brackets and respects escaped quotes. Duplicate keys,
floats/nonfinite numbers and excessive integer strings reject. Exact schemas,
tree arities, alphabet membership, formula/node limits and strictly backward
integer references precede the literal checker. That checker receives all
seven exact primitive tags, actual arguments and final endpoint. Neither
Boolean equivalence nor rebracketing participates. The request pins the source
SHA, alphabet, goal and dictionary. The certificate must retain exact source
text and type-sensitive freshly checked evidence; its digest cannot authorize
itself.

The old checker reopens the source and its resulting digest is compared with
the caller digest. An intercepted second read containing a legal whitespace
change rejects specifically as `source changed during checking`, with the
original file untouched. A valid singleton certificate also rejects against
the old-nonzero caller paths, at `source retention`. Complete evidence and
assumptions are in `scripts/four-rule-extraction/output-459/authorization-checks.json`.
The second checker read does not repeat the byte/depth preflight. An actively
changing source can consume resources before rejection; no total hostile-race
parsing/work guarantee is claimed. This qualification does not authorize
changed bytes or alter the fixed-input finite verdict.

**Typed transport and rule blocks.** Dictionary validation receives exactly one
Boolean entry per original and one commutator per alphabet-index pair i<j,
distinct placeholder names, and the exact ordered words. Caller list positions
are unchanged. An independently reconstructed token table maps scalar one to
its separate tag, x_i to original index i, and b:i/t:i:j to the caller's actual
placeholder position. Display names `1`, `x1`, atomic `or`/`not`, and overlapping
original/placeholder names therefore do not conflate formal generators. In the
singleton `1` case the free output is σ₀, the zero output is 0, and substitution
gives y₀+y₀². Empty alphabets, unused names/roots and reversed dictionary order
are retained in the complete evidence.

Both programs implement §2 exactly: H(a) for axiom/contraction, W(a,b) for
expansion, zero ground/association seeds, and (1+a)W(b,c) for cut. Earlier
witnesses receive only right multipliers b,c,1. The actual source supplies
every argument; original-only checks precede correction calls and transition
reception excludes placeholders. The receiver checks all roots and block
occurrences, contiguous fresh partitions, internal edges, exact connectors,
typed endpoints and acyclicity. Both cut references are traversed separately.
Identical cut references cannot form a legal finite literal instance: the
shared premise would require A=¬A. The malformed same-reference case rejects;
no accepted same-reference fixture is claimed.

**Independent full arithmetic.** Reproduce with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_parameterized.py`
and
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_parameterized_input.py`.
The main audit preserves outputs 449/451/453/455/457 and writes output-459.
Its new forward evaluator uses disjoint integer ranges for originals and
placeholders, integer coefficient accumulation and reduction modulo two. It
imports neither receiver arithmetic nor correction code. A topological edge
sweep starts with the unit at the entry and appends each affine-label word
on the right. Induction on the topological order sums precisely all paths
to each vertex. The existing receiver instead prepends labels to backward
suffix tables. Every complete free/zero/substituted polynomial and every
separately translated target is compared, at every root and block. These
are formal free-word checks, not Boolean evaluation or selected-word previews.

All six inputs pass: 35 roots and 56 blocks yield 364 full polynomial
comparisons. Complete original receiver evidence replays; only the known
set-order-dependent transient word maximum may differ within the fixed cap,
while stable counts and all words must agree. Before executing the test driver,
its OUT is redirected to `output-459/replay`. Rebuilt sources, requests and
certificates are byte-identical; complete construction reports agree after
path relocation. All 192 earlier-fixture comparisons and 47 rejection verdicts
and reasons replay. Complete mutation artifacts match, and the neutral repeated
label remains accepted with independently identical polynomials at all roots.

Both nonzero seed erasures are independently checked through the final root.
Write x=y₀,z=y₁ in the old-nonzero case; the final substituted polynomial is
xz+xz². Erasing the cut placeholders changes it by
x²z+xzx+x²z²+xz²x; erasing the used Booleanity placeholders changes it by
zx²+z²x². Each difference consists of distinct free words and is nonzero.
Complete original/altered/difference polynomials are in
`output-459/erasure-effects.json`; the receiver rejects at substituted block
identities 12 and 1 respectively.

**Bounds and provenance.** Review checks the exact L035 preflight of
2+2p(v_F+v_G) vertices and 2p(m_F+m_G)+4p+q edges, where q counts unequal
nonconstant label pairs, before its internal copy loops. Serial/Boolean copies
reserve connector slack; translation/prefix and outer attachments have guards.
Dictionary cardinality precedes quadratic association construction; graph/label
checks precede adjacency allocation; streamed output is capped. These guards
bound the indicated objects, not all live Python data, already evaluated
function arguments or interpreter work. Constructor counters remain claims
about the instrumented construction, not independently certified global cost.

Saved accepted maxima remain 17,689 records / 2,000,000; 223,971 bytes /
200,000,000; 45,260 multiplication pairs / 100,000,000; nine words / 1,000,000;
length four / 256; and 4,223 backward table words / 20,000,000. The independent
forward maxima are 27,505 multiplication pairs, nine unreduced counter words,
length four and 4,484 stored words against the same caps. Different traversal
storage counts are not equated. Full input metrics and required bounds remain
on disk. No accepted cap is exhausted. Deliberate stops remain failures,
including the 4,000,010-record L035 preflight against 2,000,000.

All four step-457 script hashes match its manifest. The narrowly used literal
checker, Boolean constructor and marked-edge constructor match their recorded
step-453 hashes; these are not silently treated as unpinned dependencies.
Current code/audit hashes are recorded. All 282 files across the five archives
are unchanged, including the 176 files in the four older archives. Full
evidence, bounds and the empty failure list are in
`scripts/four-rule-extraction/output-459/verification.json`.

**Verdict.** No substantive literal, transport, algebraic or archival defect
was found in this bounded audit. No production code, recurrence, theorem or DAG
input needed repair. This supplies new local verification evidence for §10,
not mathematics beyond the inspected sources. All-size executable guarantees,
source-proof availability, library preparation, downstream occurrence composition,
an M-only bound, universal W₂, arbitrary ER data and unrestricted SAT remain
open. Full matching Mathlib coverage remains unchecked. Attempts 037/038 and
all earlier stop evidence are preserved.

### 12. Immutable-byte checker and bounded equality guard — step 466, 2026-10-24

**Scope and hypotheses.** Under the prior SPECIALIZE assessment
`drafts/literature/2026-10-24-immutable-byte-literal-checker-interface.md`,
this step repairs only §11's second-read parsing boundary. The mathematical
theorem, primitive rules, supplied-proof hypotheses and correction inputs
L035/L036 remain unchanged. Reuse §1's precise Shoenfield (1967), §2.6,
pp.21–22 citation and the assessment's inspected official Python binary-stream
specification. No theorem is reproved. The actual interpreter is Python 3.15.0;
the earlier documentation assessment inspected the rendered 3.15.1 documentation.

**Implementation and applicability argument.** The complete old checker body,
apart from expected-tree normalization and opening the stream, is moved into
`_check_stream`. Its abstract syntax tree equals the corresponding old body,
including all seven rule cases, literal argument comparisons, exception handling,
endpoint checks, raw-byte hashing and receipt fields. The legacy `check(path,
expected)` still normalizes the expected tree before opening a binary file and
executes that body. New `check_bytes(raw, expected, byte_limit)` accepts exactly
immutable `bytes` and a nonnegative integer limit (excluding bool), rejects
oversize before normalization/parsing, and creates its own private `io.BytesIO`.
Both wrappers therefore use binary LF framing without reserialization. This
factors an existing syntactic checker; it imports no completeness claim.

`parameterized_input.request` keeps its existing strict capped first read,
caller SHA, JSON/schema/depth/reference checks, full alphabet/dictionary and exact
header/endpoint preflight. Its second read uses the same bounded reader, requesting
at most 2,000,001 bytes and rejecting if the result exceeds 2,000,000. It compares
all second-read bytes with the retained first bytes. In-cap differences reject
as `source changed during checking`; overflow rejects at the byte cap. Replacement
bytes are never parsed. Only the first bytes enter `check_bytes`, under the
unchanged cap; the receipt is still bound to the original caller SHA. Direct
equality removes reliance on digest comparison for this particular cross-read
equality check, while other provenance bindings retain their SHA assumptions.
The generic emitter/receiver and occurrence `bind_K` comparisons are unchanged.

**Complete finite evidence.** Reproduce with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/test_immutable_bytes.py`.
Baseline code, complete receipts, malformed streams, regenerated certificates,
all root/block polynomials, exact failure reasons and preservation hashes are in
`scripts/four-rule-extraction/output-466/`. `engine-comparison.json` records the
full engine AST comparison. `checker-tests.json` compares old path, new path and
byte receipts for all six retained step-457 fixtures, covering every primitive
tag, both constants, repeated premise uses, unused lines and unusual legal names.
All complete receipts agree, with source byte maximum 824 against the caller cap
2,000,000. All record and dictionary positions survive request reception.

Six framing tests compare the same three interfaces. LF (682 bytes), CRLF (692),
missing final LF (681) and an internal CR used as JSON whitespace (683) accept
with their distinct raw-byte digests. A blank line and replacing LF delimiters
by lone CR reject identically. Seven primitive corruptions plus separate header
and final-endpoint defects reject identically. Eight type/limit tests reject
before the engine, including overflow, bool/float/negative limits, bytearray,
memoryview, string and a bytes subclass. These tests cover the declared examples;
the AST comparison, rather than finite sampling alone, supports rule retention.

`guarded-reads.json` retains all five complete interceptions. The stable case
checks object identity with the first 682-byte read and forbids any path open
inside the byte checker. A legal whitespace replacement (683 bytes), deeply
nested replacement (322 bytes) and malformed replacement (8 bytes) reject by
equality; an oversized replacement (2,000,001 bytes) rejects against 2,000,000.
Every source read requests exactly cap+1, there are exactly two source opens,
and neither the strict parser nor the checker receives changed replacement bytes.
The whitespace interception preserves §11's recorded rejection message.

The existing generic test driver is redirected to `output-466/replay`, leaving
all prior outputs untouched. Its six inputs/35 roots and 192 earlier-fixture
polynomial comparisons pass; all six source/request/certificate triples are
byte-identical to step 457. All 47 expected rejections, their exact reasons
(after output-path relocation), and neutral duplicate-label acceptance replay.
These include strict references, duplicate keys, malformed rules, caller/header/
dictionary defects and caps. A valid foreign singleton certificate still rejects
against the old-nonzero caller at `source retention`. Complete evidence is in
`regression-comparison.json` and `replay/`; it is read in full by the comparisons,
not checked by previews. All 885 previously pinned files across outputs
449/451/453/455/457/459/461/464 retain their hashes.

**Verdict and limits.** This is a local implementation repair and regression
result, not mathematics beyond the assessed sources or certified originality.
Its changed boundary and test harness await a separate critical audit. The byte
cap does not establish total interpreter work/memory, bounded filesystem latency,
an atomic snapshot or rejection of changes occurring after the second read.
The legacy path API remains uncapped for legacy callers. Trusted caller paths
and SHA assumptions for other bindings persist. No valid occurrence endpoint
proof or complete positive H composition is supplied; proof availability,
M-only bounds, universal W₂, arbitrary ER data and unrestricted SAT remain open.
Attempts 036/037/038 remain parked. No mathematical dependency or argument changes,
so DAG.md and PROOF.md are unchanged this step. Full matching Mathlib coverage
remains not checked.

### 13. Independent immutable-byte boundary audit — step 468, 2026-10-24

**Hypotheses and sources.** This is the exact finite audit approved before
invocation in `drafts/literature/2026-10-24-immutable-byte-checker-critical-audit.md`.
It receives §12's implementation and §10's caller-selected bounded interface,
with trusted caller paths and the remaining SHA provenance assumptions.
Reuse §1's Shoenfield, *Mathematical Logic* (1967), §2.6 pp.21–22 literal
rules, separately added constant axioms, and audited L035/L036 corrections.
The official Python binary I/O, IOBase.readline and BytesIO specifications at
https://docs.python.org/3/library/io.html and bytes.splitlines at
https://docs.python.org/3/builtins/stdtypes.html#bytes.splitlines are the
previously inspected API inputs. Runtime is Python 3.15.0; the assessment
recorded rendered documentation 3.15.1. No source theorem certifies this
implementation. No completeness result or new algebraic lemma is used.

**Conclusion and independent code review.** No substantive defect was found
in this finite boundary and retained caller-authorization audit. The old checker
and request snapshots are pinned to the actual/recorded hashes in step 464's
`dependency-preservation.json`, not merely accepted as baselines because of
their filenames. All unchanged generic dependencies and all four occurrence
modules still match the audited hashes. All three current step-466 files match
its recorded implementation hashes.

The entire checker, request module, old checker and test harness were read.
The full checker module, after removing only the new io import and two functions
and restoring the old check function, has exactly the old AST. Thus the engine
test does not overlook changes to tree normalization, variable collection,
node counting or other module definitions. The old check body consists of
expected-tree normalization, two initialization statements, a binary-file with
block, and final endpoint/receipt statements. The harness compares precisely
the two initializations, complete with-body and final statements to the new
helper; no literal rule branch is omitted. Separate wrapper AST comparison
checks normalization followed by opening the binary path and calling the helper.
Closing the ordinary binary file now follows helper completion; no mutable
caller stream is admitted by either public interface. This is not a claim
about arbitrary monkey-patched file objects or resource-exhaustion exceptions.

The byte wrapper first requires exact bytes and an exact nonnegative int limit
(not bool), and rejects overflow before expected normalization or stream parsing.
It then performs the same normalization and creates private BytesIO. For fixed
bytes, LF-delimited chunks agree with the old binary file; the unchanged engine
therefore checks the same seven directed rule cases, ordered arguments,
backward references and endpoints and accumulates the same full receipt. It
does not substitute splitlines framing. Strict caller preflight still uses
splitlines, so an internal CR accepted as checker JSON whitespace need not pass
that stronger caller preflight. This existing distinction is retained.

The complete request diff changes only the former path checker call and its
comments: read the second bytes with the existing bounded reader, compare them
to the retained first bytes, and call check_bytes on the first object under
the unchanged cap. The reader checks stat size, requests cap+1, then checks
returned length. A changed in-cap second read exits before either parser sees
it; an oversized read exits at the byte cap. There is no fallback or third source
open. Unchanged digest/header/goal/reference/dictionary preflight and final
receipt-SHA binding remain necessary. Exact equality removes SHA dependence
only for this cross-read comparison.

**Complete replay and authorization evidence.** The audit program is
`scripts/four-rule-extraction/audit_immutable_bytes.py`; run from the notebook
root with `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_immutable_bytes.py`
in a workspace where output-468 does not yet exist. It deliberately refuses
to overwrite its output directory. The original harness is reused for its
reviewed cases, with output redirected; its hard-coded regression path is not
used. Independent receipt reconstruction uses explicit LF segmentation, counts
raw formula nodes/tags and hashes complete original bytes without checker helpers.
The fresh generic driver compares full saved results with only output-path
relocation, including complete construction/reception JSON and all polynomial
words. No transient counter exception was needed in this run.

All six fixture receipts, six framing cases, nine primitive/endpoint failures,
eight preparse type/cap failures and five intercepted-read cases match the full
step-466 evidence. Ten accepted fixture/framing receipts are independently
reconstructed. Every intercepted read requests 2,000,001 bytes against the
2,000,000-byte acceptance cap. The stable 682-byte object is exactly the first
read and is parsed without path opens. Replacements of 683, 322 and 8 bytes
reject by equality; 2,000,001 bytes reject by cap. Replacement bytes never enter
the strict parser or checker. Accepted fixture source maximum is 824 bytes.

The six regenerated source/request/certificate triples are byte-identical to
both steps 457 and 466. Complete reception agrees at 35 roots and 56 blocks;
all 192 earlier-fixture polynomial comparisons, 47 rejection reasons and the
neutral duplicate-label acceptance replay. Maxima remain 17,689 graph records
against 2,000,000, 223,971 certificate bytes against 200,000,000, 45,260
multiplication pairs against 100,000,000, nine words against 1,000,000,
length four against 256, and 4,223 stored words against 20,000,000.

Generic reception still compares full source text, original caller SHA, freshly
checked typed receipt, complete ordered dictionary and symbol map. Its foreign
singleton certificate rejects at source retention. The whitespace interception
matches step 459's full original/replacement hashes, two reads and exact reason.
Occurrence reception separately retains K's checked certificate digest and
bind_K's comparisons against the ORIGINAL context, as specified in L097 §9.
Four focused bind_K units on a generic fixture reject changed text, changed
digest, reversed dictionary and a foreign certificate with the same step-464
reasons. These units do not execute a positive occurrence endpoint/composition.
Old source hashes alone were not used to certify the changed shared boundary.

Full receipts, module comparisons, authorization results, replay artifacts and
actual/required bounds are in `scripts/four-rule-extraction/output-468/`.
`verification.json` records no failures; all 1,014 protected files (the prior
885-file manifest plus the step-466 archive) retain their hashes. No production
code, extraction identity or mathematical DAG input changed.

**Qualification.** This is independent local verification evidence, not a new
result beyond the assessed mathematics. No total interpreter work/memory,
filesystem latency or atomic snapshot bound follows; later path changes are
unobserved, and legacy path checking remains uncapped. Trusted paths and other
SHA bindings persist. Positive occurrence reception, proof availability, M-only
bounds, universal W₂, arbitrary ER and unrestricted SAT remain unresolved.
Attempts 036/037/038 remain parked. Full matching Mathlib coverage is not checked.

## Mathlib

Full matching theorem, explicit graph construction and binary ledger:
**not checked**. No absence claim is made. The relevant formal operations
are free-associative-algebra addition/multiplication over F₂, acyclic
path sums and induction. The precise source comparisons and imported
local correction hypotheses are stated above. This result is not a
candidate resolution of P versus NP.

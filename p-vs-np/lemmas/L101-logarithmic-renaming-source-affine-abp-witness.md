# L101 — Globally logarithmic renaming gives an exact occurrence witness

## Hypotheses

Work over F₂. Supply an explicitly written occurring-variable CNF F of
width at most three, with its actual clause/literal order and connective
trees, and exactly L087's occurrence pair D,E, provenance and complete
dictionaries. Retain its occurrence alphabet y, ordered representatives
f=r_D, g=r_E, Boolean/commutator list B and pre-witness length M.

Supply an assumption-free proof π ending in exactly ¬F in L097/L098's
fixed three-scheme Frege presentation with MP and the ground axioms true
and ¬false, augmented only by renaming inferences. A renaming line i
has an earlier parent p(i), an explicitly written simultaneous
variable-to-variable map ρ_i fixing unlisted variables, and formula
A_i=ρ_i(A_p(i)). All formulas, scheme-instantiation records, names,
maps and references are explicit and charged. Every variable appearing
in any proof formula, instantiation record or map belongs to V=Var(F).
Maps may be noninjective. There are no assumptions, extensions or
formula-valued substitution inferences. Use the fixed nonduplicating
abbreviations for implication and conjunction.

Fix the original length before any transformation:

    Q=2+M+|F|+|π|.

Let r count all renaming inference lines in the written π, including
unused ones. Assume r≤floor(log₂ Q). This is a global count, not a
maximum along a single ancestry path. Intermediate formula depth and
proof reuse are unrestricted.

## Conclusion

There is a deterministic construction of an explicit acyclic affine-F₂
ABP H using only the unchanged y and B placeholders such that

    H(y,0)=0,                    H(y,B(y))=fg

as formal free-algebra identities. Full binary output length and bit
construction time have one fixed polynomial bound in the original Q.
For example the loose received ledger below gives |H|≤K Q^840.

This is a restricted supplied-proof result. Short-proof availability,
a bound in M alone, general renaming normalization, arbitrary ER data,
universal W₂ and unrestricted SAT decision/separation remain unproved.
The separate step-396 all-size informal critical audit below finds no
substantive defect in the normalization or composed ledger. No
implementation, verified proof strings or certified originality is
claimed. This is not a candidate resolution of P versus NP.

## Proof

**Coverage, imports and the point of the specialization.** Reuse the
pre-invocation EXPLORE assessment
`drafts/literature/2026-10-20-logarithmic-renaming-source-supplier.md`,
whose COVERED_TARGET is this construction/test. The exact parameterized
supplier was not established by its inspected sources. We prove the
missing bounded normalization, then apply the whole ordinary-proof
theorem L098 only after its no-renaming hypothesis is satisfied.

The primary extraction input received inside L098 is Fu Li, Iddo
Tzameret and Zhengyu Wang, *Characterizing Propositional Proofs as
Non-Commutative Formulas*, SIAM J. Comput. 47(4) (2018), 1424–1462,
[DOI](https://doi.org/10.1137/16M1107632), [40-page author revision](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
Definition 1.3 p.6 and Theorem 3.1/Lemma 3.3 pp.13–14, as inspected
in the saved assessment (revision date unestablished). We retain L098's
received L097 correction of the Boolean/commutator seeds and its explicit
ground-constant cases. Ordered tree-to-graph conversion is received there
from Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non
Commutative Models*, [author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Lemma 2 Step 1 p.5. No new extraction proof or PIT input is needed.

The Buss July 3, 2002 manuscript *Some Remarks on Lengths of Propositional
Proofs*, [§8 Theorem 15/Corollary 16/Lemma 17, pp.22–24](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/proplengths/paper.pdf),
was compared in the assessment; its SF/EF simulations do not supply this
ABP ledger. The normalization below is necessary to justify applicability,
not a claimed reproof of those stronger-system simulations. L099's map
reception and Attempts 020/032/033 are checked comparisons, not additional
mathematical premises: no arithmetic witness is renamed in this construction.

**1. Ordered contexts and their exact syntactic invariant.** Number the
source formulas A_1,…,A_N in their given order and let R be the set of
renaming-line indices, |R|=r. Every premise index is strictly smaller
than its conclusion index. For a subset S⊆R, write its elements in
strictly decreasing order s_1>…>s_t and define

    σ_S=ρ_s1∘ρ_s2∘…∘ρ_st,             σ_∅=id_V.

Composition means ordinary function composition: the rightmost map
acts first. Maps are extended simultaneously to formulas, fixing
connectives and constants. They need not commute or be injective.

A request (i,S) has S⊆R∩{i+1,…,N} and asks for an ordinary
assumption-free derivation of σ_S(A_i). Start with every request (i,∅),
including unused source lines; this deliberately retains their work too.
Close the request set under these operations:

* For an axiom line, request no parents.
* For MP at i from j:A and h:A→A_i, request (j,S) and (h,S).
* For renaming at i, request (p(i),S∪{i}).

Every new request satisfies the stated index condition. In the third
case i is less than all members of S, so
σ_(S∪{i})=σ_S∘ρ_i. Consequently its parent's requested formula is
σ_S(ρ_i(A_p(i)))=σ_S(A_i), exactly as a written formula, including
all parentheses, signs and constants. This is not Boolean equivalence.
At MP the two requested formulas are σ_S(A) and
σ_S(A)→σ_S(A_i), again syntactically the required pair.

Memoize requests by the exact pair (i,S), with S stored as a bit vector
indexed by the r original renaming lines. Do not identify contexts by
their action on formulas and do not expand proof ancestry into a tree.
Since source indices strictly decrease on every request edge, this
finite request graph is acyclic. There are at most

    T_req=N·2^r                                             (1)

requests, each with at most two parent requests. Indeed each descending
path can encounter a given renaming line at most once and always in
decreasing order, so its subset fixes its composite even when maps do
not commute. Different MP paths with the same pair share one request.
Repeated premise references retain both premise positions; no parity
cancellation of proof requests is performed.

**2. Materialize an ordinary proof, without a renaming rule.** Process
the requests in increasing i (any order within one i). Maintain the
index of a written ordinary proof line with the requested formula.

At a scheme instance A_i=η_i(A_scheme), write the scheme instance
(σ_S∘η_i)(A_scheme), where the notation denotes applying σ_S
to every formula argument in the supplied instantiation record. This is
a valid ordinary axiom, even when distinct variables are identified.
At a ground true or ¬false axiom, write that same ground axiom. At MP,
write σ_S(A_i) with the already stored two earlier ordinary references.
At a renaming request, write no inference: store the line index already
obtained for (p(i),S∪{i}). Section 1 proves that the indexed formula
is exactly the requested one. This reuse of an identical proved formula
adds neither a substitution rule nor an assumption.

Induction on i proves the invariant and validity of every written line.
All variables stay in V, and all constants are fixed. Each request emits
at most one line. In particular (N,∅) yields a line with exactly ¬F.
If it is not the last written line, append a copy of that line's ordinary
axiom or MP record, using its existing earlier references. This is valid
and makes the conclusion literally last; it adds at most one line, with
no search for a proof. Call the resulting ordinary proof π°.

Starting every (i,∅) keeps each original axiom line, including every
later or unused axiom. Every additional axiom context requested by the
construction is materialized as well. An axiom in a different context
is not discarded because its B image cancels with another axiom. In
the later extraction all axiom lines of π° receive the usual seeds.
Thus this construction never isolates L100's initial-seed aggregate or
sets later seeds to zero. It need not reproduce the literal arithmetic
output of the original renaming extractor; the required output is any
witness with the prescribed two endpoints.

**3. Full normalization ledger in original Q.** Let fixed encoding
constants be absorbed into c. Counts of source lines, syntax nodes,
variables, map entries and the length of any original name are ≤cQ.
Formula argument records in a scheme instance are part of this input.
A total map V→V can be stored with ≤cQ² bits using original names,
including identities on unlisted variables. Composing such tables never
creates a new variable name. A renamed formula or instantiation record
has the same number of connective and leaf occurrences as its source,
and ≤cQ² full bits when every leaf is pessimistically charged cQ bits.
The constant-size scheme identifier and premise references add only
O(log(T_req+2)) bits per output record.

Apply the promise only now: 2^r≤Q, so T_req≤cQ². All subset keys,
request edges and alias references fit O(Q³) bits under a deliberately
loose charge of Q bits per identifier/key. Keeping a separate total map
for every request costs O(Q⁴) bits. All written proof lines and complete
instantiation records cost O(Q⁴) bits before final framing. The full
ordinary source dictionary, reference relocation, length fields and
optional complete original-input retention fit

    |π°|≤c_0 Q⁵.                                         (2)

This counts independently written occurrences, not shared syntax DAG
nodes. No intermediate or output size is used to redefine the cutoff.

For a fully explicit polynomial-time implementation, first validate the
source axiom/MP/map records by comparisons of their written trees and
complete name tables; inference checking needs no semantic tautology
test. Compute the request closure with a list-based cache. At most
O(Q²) insertions/lookups scan at most O(Q²) existing keys of O(Q)
bits, costing O(Q⁵) bit operations. Store total maps at request creation;
even naive name-table composition with triple scans costs O(Q³) per
request, hence O(Q⁵) in aggregate. Formula replacement, scheme-record
copying and validation can use similarly bounded scans. Topologically
ordering by i, resolving aliases, and writing every record/reference
are polynomial operations on these explicit lists. Allowing further
quadratic scans of the O(Q⁴)-bit unframed records gives the conservative
uniform bound

    time_normalization≤c_1 Q⁸.                           (3)

The Q⁵ framed output can be streamed from those records; a quadratic
scan of that larger serialized output is not required by the algorithm.
All constants are fixed by the encodings, independent of F, π, r.
No factor depending exponentially on anything besides r is used.

**4. Occurrence transport and both exact endpoints.** Now π° meets
every source-proof hypothesis of L098: it is ordinary, assumption-free,
has the same ground constants and schemes, and ends in the unchanged
actual ¬F. Its intermediate formulas may have arbitrary depth, as L098
permits. Apply L098 to this proof and the original supplied occurrence
pair, with its complete original B and provenance.

To make the map interface explicit, let θ(x)=r_x be the chosen first
occurrence of x. Every already materialized formula σ_S(A_i) is sent
to θ(σ_S(A_i)). Its variables have representatives because they remain
in V. Scheme instances and MP pairs remain valid under this one
whole-proof substitution, also for noninjective σ_S. There is no
attempt to push a source renaming directly through all distinct
occurrence names, or to assume θ commutes with such a renaming.
No map on nonrepresentative occurrence names is needed: the source
renaming rules have been eliminated before θ is applied.

L098's audited actual-tree guard construction uses all occurrences to
prove the consistency-guarded implication to θF. It combines this with
the transformed ordinary proof to prove ¬G, where G=C∧U, v(C)=f,
v(U)=g̃. Uniform propositional complementation of every occurrence
variable in this entire ordinary proof is sound for its axiom/MP lines,
fixes both ground constants, and has translated endpoint

    tr((¬G)[¬y/y])=v(G)=f g̃.

This is the received leaf/constant/connective identity of L098, not a
substitution of complements into the desired target fg. Its corrected
generic extraction retains every seed of that ordinary proof and gives
K(y,0)=0 and K(y,B)=f g̃. Its pair-only tester correction gives
J(y,0)=0 and J(y,B)=g+g̃, in the actual group order, including
singleton groups. Thus the received output H=K+fJ satisfies

    H(y,0)=0,
    H(y,B)=f g̃+f(g+g̃)=fg.

Only the unchanged occurrence/placeholder alphabet is exported. No
Boolean vanishing in two different orders was promoted to formal zero.
Nonlinear placeholders, cancellation, full repeated dictionaries and
fresh exterior graph endpoints are covered by L098's receiver.

If F has an empty clause, L098 instead returns its distinct-endpoint
no-path zero graph: f=0 formally for the actual tester. Variable-free
unsatisfiable inputs are included in this case, with the gadget and
dictionary retained. A satisfiable empty conjunction cannot meet the
valid-source-proof hypothesis: ordinary Frege and variable renaming
preserve tautologies. The normalization itself also works for empty V,
where every map is the identity. These cases require no new premise.

**5. Composed output and time bounds; stopping comparison.** The
receiver's new input size is

    Q°=2+M+|F|+|π°|≤c_2 Q⁵.

This auxiliary size is only an argument to L098, never a renaming
budget. L098's complete graph bound |H|≤c(Q°)^168 consequently gives

    |H|≤K Q^840.                                         (4)

Let d≥6 be the fixed bit-algorithm exponent for L098's received
L035/L036 blocks. Its bound c(Q°)^[12 max(30,2d+2)], together with
(3), gives a fixed original-input bound

    time_total≤K' Q^[60 max(30,2d+2)].                   (5)

The receiver explicitly charges all copied seeds and MP transition
graphs, occurrence guards, tester correction, original/axiom/placeholder
dictionaries and global graph identifiers. Thus (4)–(5) bound full
explicit length and writing time, not only counts of distinct contexts.
Actual accepting-path degree is at most the output edge count; no
semantic degree estimate or implicit circuit-valued label is used.

Both the endpoint and polynomial-ledger thresholds are met informally.
L099's unrestricted 2^n copying obstruction remains valid; imposing
r≤log₂ Q makes this permitted exponential factor polynomial, without
recomputing Q after expansion. L100's isolated-output lower bound and
Attempt 020's general circuit-to-ABP stop are untouched. No universal
availability of such restricted proofs is inferred. The independent
critical audit below checks this normalization and its receiver
composition without making a claim about arbitrary SF, EF or SAT.

**Independent critical audit — 2026-10-21, step 396.** Use the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-21-logarithmic-renaming-supplier-critical-audit.md`.
L101 is the object of this audit. Receive the separately audited L098
theorem with its exact hypotheses and ledger, and L087's actual pair,
B and M. The corrected generic L097 component is received inside
L098; its resolution-input theorem is not a new premise. The precise
primary sources cited above and the saved step-393/395 comparisons
are reused, without a new source theorem or an originality assertion.

1. **Request closure and map order.** For every request (i,S), each
   element of S exceeds i. At MP both predecessor indices are below i,
   so keeping S preserves this property. At a renaming line the new
   member i exceeds p(i) and is smaller than every old member of S.
   Thus the decreasing list for S∪{i} is precisely the decreasing list
   for S followed by i. With the stated rightmost-first convention,
   σ_(S∪{i})(x)=σ_S(ρ_i(x)) for every x∈V, hence on every formula
   tree. This checks the order of composition without commuting maps
   or choosing an inverse. Identified variables and fixed points do
   not change the identity.

   Every request edge strictly lowers its first coordinate, including
   an MP edge that leaves its context unchanged. There is no cycle,
   no repeated renaming index on a path, and no need to remember a
   path in addition to its ordered subset. Two paths to the same
   (i,S) request exactly the same formula even for noncommuting maps.
   Keeping different subsets distinct is safe overcounting when their
   maps happen to agree. The closure of all N empty-context requests
   is a subset of {1,…,N}×2^R and therefore has at most N2^r states
   and twice as many predecessor positions. This includes all unused
   source lines; the bound does not assume final-output reachability.

2. **Ordinary proof and aliases.** Induct in increasing source index,
   storing for each processed request the index of an actually written
   axiom or MP line. For a scheme instance, applying σ_S to each
   supplied argument tree gives a legal instance of the same fixed
   scheme. This operation is simultaneous; replacement names are not
   renamed repeatedly within one substitution. Ground true and ¬false
   stay fixed. For MP the images of its two earlier formulas remain
   exactly the antecedent and implication required for the image of
   the conclusion, including the chosen connective abbreviations.

   At a renaming request, its predecessor has smaller source index
   and has already stored an actual written index. Copy that index,
   rather than storing a pointer to another unresolved request. The
   composition identity in item 1 proves equality of the two requested
   formulas as written strings. Thus even a chain consisting entirely
   of aliases ends at an ordinary axiom/MP record; it cannot hide a
   renaming rule in the result. Repeated MP predecessor positions
   remain two references and are not cancelled.

   The stored index for (N,∅) has formula exactly ¬F. If other requests
   were written after that record, copying its axiom/MP justification
   at the end is legal: every premise of the original record was
   earlier than it, hence is still earlier than the final copy. Axiom
   instantiation records are copied as well. This adds at most one
   record, not a proof-ancestry tree or a new inference rule. All
   variables remain in V. The empty V case has only the identity map
   and the same constant/alias argument.

3. **All seeds and the exact receiver.** Every original axiom has its
   own (i,∅) request and is materialized even if it is unused. Each
   required nonempty-context axiom is materialized too, without testing
   whether its eventual seed equals or cancels another seed. L098's
   whole-proof occurrence substitution and complementation apply to
   all these records and to the optional final copy. Its extraction
   attaches a seed to every resulting axiom line, including zero seeds
   for the two ground axioms. Unused seed components may be unreachable
   from the final output; they remain paid explicit records. No initial
   sector is selected and no later seed is set to zero by this audit.

   The normalized proof is assumption-free and ordinary, and ends in
   the original actual-tree ¬F. Its arbitrary formula depth and repeated
   lines are allowed by L098. The supplied pair, occurrence provenance
   and B have not been transformed. Choosing θ(x) as the original
   first occurrence is therefore valid for every normalized variable.
   The received formulas are θ(σ_S(A_i)); equality with a composition
   in the opposite order is neither needed nor asserted. In particular
   no source map has to act on nonrepresentative occurrence names.

   Under this precise reception, L098 supplies K(0)=0,
   K(B)=f g̃, J(0)=0 and J(B)=g+g̃. Its complemented propositional
   endpoint is tr((¬G)[¬y/y])=v(G), not fg with its variables
   complemented. The ordered output K+fJ thus has zero-at-zero and
   B-image f g̃+fg+f g̃=fg in the free F₂ algebra. The correction
   includes singleton groups; omitting it would already be wrong
   there. The corrected L097 seeds receive original-only arguments,
   not recursive witnesses, as required inside L098. Nothing here
   invokes Boolean-to-formal injectivity on a different-order product.

   With an empty clause, L087's D root remains in the failure state
   until its scalar-zero terminal. Induction on its suffix recurrence
   gives f=0 formally, and L098's distinct-endpoint no-path graph
   satisfies both identities while keeping the entire dictionary and
   gadget. A variable-free unsatisfiable CNF has an empty clause.
   The empty conjunction cannot have the assumed proof: fixed axioms
   and MP are sound, and variable-to-variable substitution, injective
   or not, preserves a tautology. These exhaust the exceptional cases.

4. **Independent original-input accounting.** Let W be the actual
   number of requests. The explicit input bounds N, |V|, every source
   formula/record node count and every original name length by cQ.
   The promise is used once: W≤N2^r≤cQ². Every output formula or
   scheme-argument record has the same tree occurrences as its source
   and at most cQ² restored-name bits. Even treating every request as
   a separately written record gives O(Q⁴) such bits. The optional
   final copy costs O(Q²). References to written records have
   O(log(Q+2)) bits, irrespective of proof reuse or alias-chain length.

   For an explicit bit algorithm, first index V by dense identifiers
   and convert each given map to a total table, defaulting to identity
   on unlisted entries. Sorting is unnecessary: bounded scans of the
   explicit input suffice. Cache keys consist of a source index and
   an r-bit subset. The W keys and their at most 2W edges fit O(Q³)
   bits with the loose Q-bit identifier allowance. During request
   generation an MP edge copies its current total table, while a
   renaming edge composes it on the right with the source table.
   Per-request tables, even with original names restored, fit O(Q⁴)
   aggregate bits. Equality of maps reached in different ways follows
   from item 1, so cache merging needs no semantic equivalence test.

   A list cache uses O(W²Q)=O(Q⁵) bit operations. With dense indices,
   a table composition can be performed by scanning a table for each
   of at most cQ entries, using O(Q³) bit operations even without
   constant-time array access. At most 2W requests/edges pay these
   compositions and copies. Initial name indexing, source syntactic
   validation, tree substitution and instantiation checks have similarly
   bounded explicit scans; no tautology search is performed. Processing
   requests in increasing source index gives resolved aliases directly.
   All construction scans can be bounded by a quadratic scan budget
   of the O(Q⁴)-bit working records, namely O(Q⁸) bit operations.
   Dictionaries, length fields, reference framing and optional input
   retention fit the stated |π°|≤c₀Q⁵; streaming them costs at most
   that many additional bit operations. No quadratic rereading of a
   Q⁵-bit serialized proof is required. This verifies the stated
   normalization time as well as polynomiality in principle.

   Finally Q°=2+M+|F|+|π°|≤c₂Q⁵ is the receiver's input length.
   Its bound c(Q°)^168 becomes KQ^840. Writing
   e=max(30,2d+2), the receiver time c(Q°)^(12e) becomes
   K'Q^(60e); this also dominates the normalization Q⁸ bound.
   The fixed d≥6 belongs to the received bit algorithms and does
   not depend on this proof or its number of renamings. The receiver
   charges independently copied seed/transition/correction graphs,
   all repeated dictionaries and final global identifiers. Actual
   accepting-path degree is bounded by the explicit affine DAG's edge
   count, including cancelling paths. Neither Q° nor the output size
   is used to enlarge the original renaming cutoff.

The audit finds no substantive defect and changes no hypothesis,
identity, bound, construction or direct DAG input. It establishes a
checked local conditional interface, classified as a reproduction
audit, not a new extraction theorem or certified novelty. No executable
normalizer, complete proof stream or machine-checked proof was tested.
Attempts 020/032/033 remain valid: this result neither converts arbitrary
shared circuits nor compresses the stopped isolated seed aggregate, and
its global renaming restriction is not supplied for arbitrary short
proofs. Short-proof availability, M-only bounds, universal W₂, arbitrary
ER data and unrestricted SAT decision/separation remain unresolved.

## Mathlib

Full matching coverage for the parameterized Frege normalization,
occurrence-witness supplier and complete binary/time bound: **not
checked**. No absence or formal-verification claim follows. This is an
informal specialization using the precise received sources above; no
mathematical program or finite certificate experiment is claimed.

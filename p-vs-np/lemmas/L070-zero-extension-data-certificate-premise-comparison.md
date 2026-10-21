# L070 — Zero-extension data and the proof-relative ABP certificate premise

## Hypotheses

Work in the free associative algebra over F₂ with exactly the ER/CNF,
original axiom list A, independent placeholder and explicit affine-ABP
conventions of L037, retaining all L025 supplied-data requirements. In
particular F has width at most three, π uses fresh acyclic signed-AND
extensions, sorted-set clauses, weakening and selected-pivot resolution,
and T=2+|F|+|π| is full binary length. Only the occurring original variables
are free x generators; absent nonextension proof variables map to zero.
Original clause falsity products retain their ordered factors, Boolean
axioms and pair-once commutators retain their positions, and equal axioms
have separate independent placeholders.

For the conditional construction, supply an explicit acyclic affine-F₂
ABP C with C(x,0)=0 and C(x,A(x))=1 as formal identities. Its graph can have
nonextremal endpoints, dead records, parallel or zero edges, constants,
unequal path lengths, mixed affine labels, arbitrary nonlinear placeholder
paths and cancellation. Full |C| includes its alphabets and axiom framing.
Set Q=2+T+|C|+|A|, with repeated framing charged again. No algorithm finding
C from π, fidelity, or efficient promise test is assumed.

## Conclusion

From this supplied C one can construct all L037 data on the natural signed
value DAG of π with every unsigned extension representative equal to zero.
Every original x and constant retains its exact representative and every
signed-complement node satisfies its exact complement identity. With fixed
encoding constants K, the complete aggregate data satisfy

    S ≤ K(T+1),  d=1,  h=max(1,V_C+1) ≤ K(Q+2),
    E_ABP ≤ K(Q+2)^6.

Here V_C is the vertex count of the supplied C. The data can be written in
deterministic polynomial bit time in Q, with every root separately written
and every repeated dictionary paid. The loose sixth-power bound is not an
optimality claim.

For canonical polynomial-size original-axiom framing, the following three
proof-relative existential premises are equivalent: one fixed polynomial
in T bounds a valid C for every valid supplied (F,π); one fixed polynomial
in T bounds all S,E,d,h for some L037 data for every such pair; and the same
data premise with unsigned extension representatives prescribed to be zero.
Each premise allows a different fixed polynomial, chosen before (F,π).
None is established here, and none asserts a finder from π. In particular
this conditional comparison supplies no unrestricted SAT result, ER
boundedness, formula-length-only bound, faithful values or Boolean-only
relations. The separate critical audit on 2026-10-16 (step 270), recorded
below, found no substantive defect within these hypotheses.

## Proof

**Scope and known inputs.** The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-16-nonfaithful-zero-data-diagnostic.md`.
Reuse its source and duplicate checks. The certificate definition is
[Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, arXiv:1412.8746v4, Definition 1.2, PDF p.6](https://arxiv.org/pdf/1412.8746v4).
Ordered independent serial/parallel graph composition is the operation in
[Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative
Models*, Lemma 2, Step 1, author manuscript p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Only that graph operation is used, not the whole lemma's homogeneous-output
conclusion or zero-free-term hypothesis. The applicability check below
covers affine labels and arbitrary designated endpoints. L037 supplies the
already established data-to-certificate implication; its assembly is not
reproved. L048 is used only for full graph/dictionary conventions, not its
formula-bound premise. This result is a local conditional specialization,
classified REPRODUCTION without certified originality.

**Natural signed DAG and representatives.** Create original base nodes and
constant 0,1. In definition order create each unsigned extension node, with
its two actual earlier signed operands; create a negative signed node when
needed, after its underlying unsigned/base node and before its first use.
One such node per required negative literal suffices. All values needed by
proof literals are associated with these nodes, including final negative
values not used by definitions. A nonextension variable absent from F is
associated with constant zero, and its negative value with its complement.
The name-to-value map retains every actual proof name; no new independent x
generator is introduced. This is topological because definitions are fresh
and acyclic. It adds no unrelated AND nodes.

Assign x_i to its original node, 0 and 1 to constants, and 0 to every
unsigned extension node. Assign 1+r_a to every negative signed node with
underlying value r_a. Thus every representative is one of 0,1,x_i,1+x_i,
and has a two-vertex single-affine-edge graph of degree at most one. In
particular the negative of a zero extension is 1, not 0. The node for an
extension remains distinct from the constant node despite equal
representative polynomials. There are at most a constant times T original,
extension and required signed nodes and name associations, since their
names/occurrences are written in F or π.

**Every local relation.** For an actual unsigned AND node i with its ordered
signed operands a,b, use independent copies to form

    H_i(x,t) = C(x,t) r_a(x) r_b(x).

Both identities hold in the free ring, without commutation:

    H_i(x,0) = 0 r_a r_b = 0,
    H_i(x,A(x)) = 1 r_a r_b = r_i+r_a r_b,

because r_i=0. They cover repeated, complementary, constant and zero
operands without simplification or Boolean evaluation. Exact signed nodes
need no H of their own in L025/L037. We impose neither a relation saying
0=r_a r_b formally nor all-assignment fidelity. The nonzero local defect
is discharged by the supplied C, using all allowed original placeholders.

Realize the product with a whole disjoint copy of C followed by independent
two-vertex operand graphs and constant-one connecting edges. Any accepting
path must reach C's designated exit and then traverse both operand graphs
in order. An internal path that leaves the designated exit cannot return
to take the connector, because C is acyclic. Hence only paths ending at
that exit contribute, even if it has outgoing edges or the entrance has
incoming edges. These statements also hold for operand blocks. Dead
records can remain. No placeholder-free path or nonlinear sector is
removed: cancellation at t=0 is a polynomial identity of the whole copy.
The construction therefore preserves arbitrary cancellation in C.

With coincident endpoints an acyclic C has only its empty accepting path
and polynomial 1, contradicting C(x,0)=0; with no accepting path it has
polynomial 0, contradicting C(x,A)=1. Such graphs cannot satisfy the supplied
certificate hypotheses. Their receiving conventions introduce no extra
case that needs a certificate constructor. With no extension definitions,
no H is required and the base/signed data alone meet the promises. Empty
original clauses, zero original variables, unused graph symbols and absent
auxiliary proof variables do not change any construction or identity.

**Degree and full-bit ledger.** A path of C has at most V_C−1 edges; an
expanded word from affine labels therefore has length at most V_C−1.
Finite cancellation cannot increase degree. Appending the two affine
operand blocks bounds the formal degree of every H_i by V_C+1, before any
axiom substitution. This includes nonlinear placeholder sectors. Use d=1
and h=max(1,V_C+1); the zero polynomial causes no degree convention issue.
No assertion about semantic degree after axiom substitution is needed.

Here is a conservative aggregate binary bound without unit-cost names.
The number of source names, abstract nodes, root associations and operand
references is O(T+1). Every raw proof/original name has length at most T;
the complete A and its placeholder names are already paid in Q. Generate
new internal vertex identifiers densely; no new long symbol payload is
required. In each output graph copy the complete original dictionary and
original axiom/placeholder framing, including unused permitted entries;
this costs O(Q+1) bits per copy before reference relocation. One copy of C
and two operand graphs have O(Q+1) explicit records and O(Q+1) total input
payload bits. Relocating identifiers, writing lengths/root references and
retaining all payloads costs at most K(Q+2)^2 bits per graph, using the
loose bound log(K(Q+2)^2)≤K'(Q+2). Do not share C across separately written
H roots. There are O(T+1) relations and representatives in total. Writing
all graph packages, repeated dictionaries, raw node-name associations,
abstract edges, roots and the explicit d,h parameters therefore costs at
most K(Q+2)^4 bits, and hence the claimed sixth-power allowance. Each
operation is a bounded copy, dense renumbering or source-name lookup on
these explicit lists; direct polynomial-time implementations suffice. No
path expansion, identity testing or promise verification is performed.

**Existential quantifiers.** For the standard fixed positional-placeholder
naming, complete A has length at most K(T+2)^3: at most O(T) original clauses
have at most eight word occurrences of length at most three each; there
are O(T²) Boolean/commutator positions, and original raw names have at most
T bits. Dense positional placeholders and framing fit the same bound.
This is also the framing accounting used in L048. If arbitrary extra
placeholder payloads are supplied instead, |A| must stay in Q; no bound
solely in T is asserted for uncharged arbitrary framing.

Suppose first ∃p ∀valid(F,π) ∃C with |C|≤p(T). Fix a polynomial majorant
b(T+2)^e with b≥1 and e≥3, independently of the pair. The framing bound
then gives Q≤K_b(T+2)^e. The constructed zero-extension data have S,E,d,h
bounded by one fixed polynomial, for instance after enlarging its constant
K_b'(T+2)^(6e). This proves the prescribed-zero data premise. That premise
immediately implies the unrestricted-data premise, since it adds a
restriction. Conversely, fix a common polynomial bound on S,E,d,h in T
under the unrestricted-data premise. L037 yields a certificate with full
length O(N^8 log(N+2)), N=2+T+S+E, hence one fixed polynomial in T. This
uses precisely L037's complete data promises, verified above in the
conditional construction. All three are existential size statements;
polynomial transformations on supplied inputs do not select inputs from
π. No exponent or constant depends on the particular pair.

The continuation test succeeds as a premise comparison and rejects the
zero-data proposal as an unconditional existence argument: the supplied
C remains inside each constructed nontrivial H_i. This does not prove that
every witness must literally contain C or that other constructions are
impossible. It identifies equivalent universal size obligations, leaving
the original certificate/data existence gap unresolved. L034's fixed-output
stop and L039/L040's faithful-value conditions are neither weakened nor
used as existence inputs.

**Independent critical audit, 2026-10-16 (step 270).** The prior EXPLORE
assessment `drafts/literature/2026-10-16-zero-data-comparison-critical-audit.md`
covers exactly this audit. Reuse the primary statements and graph cases
cited above; neither source is treated as an import of the whole comparison.
L037 is the mathematical input for the reverse implication. L025 specifies
the complete receiving promises; L048 supplies encoding context only. The
following checks do not reprove L037 or supply a certificate from ER.

For the receiving DAG, process the written extension definitions in order.
Every operand is either an original variable, a constant, an absent
nonextension variable mapped to 0, or an earlier extension, with its actual
sign. A required negative value can be inserted immediately after its base
node and before its first use; adding other required negative proof literals
at the end introduces no backwards edge. Distinct extension nodes remain
distinct even when their representative polynomials coincide. Name
associations for absent proof variables point to the constant value; they
do not add a free generator. Thus the graph has the base values, every
extension and every required signed value, with earlier operands as L025
requires. Its size is O(T+1). The four possible representative polynomials
are 0,1,x_i,1+x_i, so they have degree at most one and exact signed
complements. In particular a negative extension has value 1. Internal
vertices of representative ABPs are not extra abstract AND nodes.

For every actual AND node, substitution is an algebra homomorphism fixing
the x-only factors. Therefore the two substituted polynomials of the whole
H_i are respectively (C(x,0))r_a r_b=0 and
(C(x,A))r_a r_b=r_a r_b=r_i+r_a r_b. No factors exchange positions.
Repeated operands give the ordered square; complementary original operands
can give a nonzero free-ring polynomial and are not cancelled using Boolean
semantics. If an operand is zero, the product is zero; if both operands are
1, H_i has precisely C's polynomial. These cases need no extra witness.
Exact signed nodes require no relation H of their own. All witnesses use
only original placeholders, but may use clause placeholders and any number
of them on a path. This verifies every local promise without fidelity.

Independently, contract each of the three disjoint product blocks to its
block index. Every external edge increases that index, so the composed
graph is acyclic. An accepting path must use the first connector and then
the second connector, exactly once each. Its three intervening segments
are paths between the designated endpoints of their respective blocks.
Conversely every such triple gives exactly one accepting path, because the
copies are disjoint. A path that leaves a designated exit internally cannot
return to use its connector in a DAG. Incoming edges at a designated
entrance cause no additional entry from another block. Thus finite
distributivity gives C r_a r_b with the stated order, parallel-edge
multiplicities and cancellation. No dead records or placeholder-free paths
need be deleted. With equal endpoints, a block contributes its empty path
and hence 1; this is incompatible with C(x,0)=0 for the supplied C. A
no-path C contributes 0 and fails C(x,A)=1. These inconsistent certificate
cases are excluded by the identities, not by an unmentioned endpoint
normalization. Zero operand graphs remain valid product blocks.

Every C path uses at most V_C-1 edges, and each affine label contributes at
most one letter to a word. The two operand edges add at most two letters;
constant connectors add none. Consequently every H_i has degree at most
V_C+1 in the independent x,t before substitution, even if cancellations
substantially lower its actual degree. This verifies h=max(1,V_C+1), with
V_C=O(|C|+1), and d=1. No syntactic degree assumption on a circuit or
post-substitution degree estimate is used.

For an independent full-bit check, there are O(T+1) output graphs and
O(T+1) abstract records and name associations. Each graph has one complete
copy of the permitted original/placeholder dictionary and A, even when its
polynomial is x-only or zero. These dictionaries and their unused entries
cost O(Q+1) input payload bits. A relation additionally copies all of C's
explicit records once, and adds two constant-size affine graphs and their
connectors. Representative graphs are smaller. Preserve raw original and
proof names, including repeated occurrences; only internal vertex and
dictionary references are densely relocated. In one output graph there
are O(Q+1) records, total source payload O(Q+1), and each new reference or
length field has O(log(Q+2)) bits. The conservative K(Q+2)^2 per-graph
bound therefore holds without unit-cost names. All separate roots repeat
this charge, rather than sharing a C copy between different H_i.
The abstract/name map costs at most O((T+1)^2) even with raw names per
association; d,h and roots add O((T+1)log(Q+2)) bits, retaining the possible
dependence on an arbitrarily large supplied C. Summing gives
at most K(Q+2)^4 bits, within the claimed K(Q+2)^6. Direct scans, string
comparisons, copying and dense relocation take polynomial bit time in Q;
no promise test, path expansion or search for C is hidden in this bound.

Canonical framing is polynomial independently of C: if n original names
and m clauses are written, n,m=O(T). There are at most 8m clause-word
occurrences and 24m clause-symbol occurrences, 2n Boolean words with 3n
symbols, and n(n-1) commutator words with 2n(n-1) symbols. Empty words
still have records. Every original payload has at most T bits, while dense
placeholder positions, role indices, counts and lengths require
O(log(T+2)) bits each. Thus full A, including its dictionaries and ordered
positions, has at most K(T+2)^3 bits. Equal axiom polynomials keep separate
positions and symbols; this count never identifies them. Arbitrarily
chosen extra payloads are outside this canonical size statement and remain
charged in Q in the conditional construction.

Finally fix p before any valid pair (F,π). A fixed majorant b(T+2)^e,
e≥3, absorbs p and canonical A; hence Q≤K_b(T+2)^e and one fixed
K_b'(T+2)^(6e) bounds all constructed S,E,d,h. This proves the
prescribed-zero premise with the required quantifier order. It implies the
unrestricted-data premise by inclusion. Conversely fix its common
polynomial q first and choose a fixed polynomial r(T)≥2+T+2q(T), r(T)≥2.
L037 receives precisely these complete data and gives length
O(r(T)^8 log(r(T)+2)), bounded by a fixed polynomial, for example a constant
times (r(T)+2)^9. This is an existential implication for each supplied
proof, allowing different data and certificates for different pairs. It
does not select witnesses from π, bound π by |F|, or invoke any faithful,
Boolean-only, W/V/U or ER-boundedness premise.

If there are no extension definitions, no H is required; all base/signed
data still meet L037, which applies to the supplied refutation. With no
original variables, A and its written clause positions are still retained.
An empty original clause supplies its formal constant-one axiom without
changing the argument. An empty clause list cannot admit a valid refutation
in this setting; the all-valid-pair quantifier supplies no such obligation.
Unused permitted symbols, zero/dead edges and absent auxiliary variables
are covered by the same framing and identities. No load-bearing error or
bound repair was found. This is verification of a conditional local
comparison, not new mathematics beyond the checked sources or an advance
on the missing certificate existence premise. The argument and direct
mathematical inputs are unchanged; prescribed-output stops remain intact.

## Mathlib

Full matching result and explicit encoding theorem: **not checked**; no
absence claim. Supporting algebra and graph composition are justified
above, with the precise primary comparisons linked in the proof. No
Mathlib theorem is imported. The separate informal audit above checks the
stated comparison, not an executable or Lean certificate. This is not a
candidate resolution of P versus NP.

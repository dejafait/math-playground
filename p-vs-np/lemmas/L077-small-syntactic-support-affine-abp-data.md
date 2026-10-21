# L077 — Small syntactic support supplies affine-ABP data

## Hypotheses

Use L037's width-at-most-three original CNF F and valid fresh acyclic
signed-AND ER refutation pi, with actual binary length T=2+|F|+|pi|.
Retain its original ordered clause/Boolean/pair-once commutator axiom list
A(x), independent placeholders t, and free associative algebra over F₂.
There are n distinct original variables occurring in F, n≤T. Nonextension
proof variables absent from F have positive value zero.

The canonical value DAG has the original generators, constants, every
positive extension with its two actual ordered signed operands, and both
signs of every proof variable. Include unused extensions. An alias adds
no operation; a signed node complements its positive node. There are
S=O(T) abstract nodes. Define the syntactic original support U_a by
U_(x_j)={x_j}, empty support for scalar/absent base nodes, U_(-a)=U_a,
and U_i=U_a union U_b at an extension i with operands a,b. Thus support
counts distinct reachable original generators, ignores signs and does
not discard dependencies because a Boolean function happens to simplify.

Put k=floor(log₂(T+2)). Assume |U_i|≤k for every positive extension,
including unused ones. This is a restriction on the supplied proof, not
a promised semantic-support oracle or a bound inferred for arbitrary ER.
Exact unreduced syntactic degree is unrestricted.

## Conclusion

There is a deterministic construction of all L037 data with

    S=O(T),  d=max(1,n),  h=max(1,2n−1),
    E_ABP≤K(T+2)^7,  bit time≤K'(T+2)^16,                 (1)

for absolute constants K,K' depending only on a fixed explicit encoding.
Every separately written representative is an x-only affine-edge ABP;
originals/constants have their exact prescribed values, signed roots are
exactly 1+r_a, and all values are faithful on every original Boolean
assignment. Every AND relation is an explicit affine-edge ABP satisfying

    H_i(x,0)=0,       H_i(x,A(x))=r_i+r_a r_b             (2)

as formal free-algebra identities. Relations use only original Boolean
and commutator placeholders. The bounds include separate graph copies,
all unused roots, original names, node/root associations and complete
original-axiom dictionaries, even if repeated per output. Degrees in (1)
are before axiom substitution. No exact syntactic degree parameter enters
the bounds.

Consequently L037 supplies an original-axiom affine-ABP certificate C
with C(x,0)=0 and C(x,A)=1, full bits O((T+2)^56 log(T+2)), complete
pre-substitution degree O((T+2)^56), and polynomial bit construction time.
This is a restricted sufficient condition, classified REPRODUCTION under
the prior SPECIALIZE assessment. It is not a main-problem candidate or
certified originality. The separate step-298 informal critical audit below
found no substantive defect and changes neither the theorem nor its bounds. General
ER data, formula-only bounds, W/V/U, every-certificate hardness and
unrestricted SAT decision/separation remain open.

## Proof

**Scope and imported components.** The pre-existing assessment is
`drafts/literature/2026-10-17-small-support-affine-abp-data.md`.
The Boolean representation input is Randal E. Bryant,
[*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE TC
35(8), 677–691 (1986), author-restored §1 equation (1) and §2
Definitions 1–2, PDF pp.3–4](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf).
Use its ordered Shannon representation and assignment-path semantics;
reduction is unnecessary. For irrelevant-variable tests the supporting
completion result is Alexis de Colnet, Sebastian Ordyniak and Stefan
Szeider, [*OBDDs, SDDs, and circuits of bounded width: Completeness
matters*, Artificial Intelligence 351 (2026), 104458, §2.3 and
Proposition 2, PDF pp.3–4](https://eprints.whiterose.ac.uk/id/eprint/234745/9/1-s2.0-S0004370225001778-main.pdf).
Its dummy-node discussion permits equal-successor tests, including root
and terminal gaps. The explicit prefix-state implementation below keeps
the sharper width count directly; no general completion theorem is
reproved or claimed as new.

Import L026's ordered representatives, exact signed identities and formal
H identities, and L071's independently described post-compilation graph
construction, headed “Explicit value and earlier-variable graphs” and
“Explicit paired-state W graphs”, including its step-274 audit. That
component receives any complete common-order diagram family and realizes
the identical L026 polynomials. Its proof and record bound use only those
diagrams after compilation, not treewidth. We do not apply L071's whole
treewidth-two theorem, its compiler, decomposition or selector construction.
The task here is to construct its diagram inputs from reachable support
and pay the complete bit/time specialization. No witness recurrence is
reproved.

**Support extraction and truth tables.** Parse original names once and
densely index them in one fixed order y_1,...,y_n, for example increasing
encoded identifier order. Compute every U_a topologically as an n-bit
vector using the displayed singleton, inheritance and union rules. Fresh
acyclic definitions guarantee this order exists even when both operands
are the same earlier literal. Computing all supports costs O(S(n+1))
bit-vector operations at the bit-entry level, apart from polynomial name
parsing. This also checks the promise without solving semantic support.

For any abstract node a, its recursively evaluated Boolean value depends
only on the assignment restricted to U_a. Induction proves this claim:
an original uses its sole coordinate; scalar/absent bases use none;
complement preserves the dependence set; AND uses only the union of the
two operand sets. This statement retains repeated and signed operands,
and applies to unused nodes. It asserts dependence containment, never
minimality. It is a Boolean evaluation statement, not a free-polynomial
identification.

For each positive extension i independently enumerate the 2^|U_i|
assignments sigma to U_i. Evaluate the entire source value DAG in
topological order, giving originals outside U_i value zero and retaining
the specified absent-variable convention. Record the value at i as
f_i(sigma). The dependence induction shows that this is its value under
every full original assignment extending sigma. Other nodes may depend
on originals outside U_i; their zero-specialized values still give the
correct value at i. No evaluation of an exponentially long formal word
or exact syntactic degree is required. There are at most T extensions,
2^|U_i|≤2^k≤T+2 evaluations per extension, and O(T) Boolean operations
per source evaluation, so O((T+2)^3) indexed Boolean operations suffice
for these tables. The stored table bits total O((T+2)^2).

**One complete global order.** Suppose n≥1. For i let I=U_i in the fixed
global order. At level j, 1≤j≤n, introduce a state for every assignment
alpha to I intersect {y_1,...,y_(j−1)}. The root at level 1 has the empty
assignment. Every level-j state queries y_j. On branch b, extend alpha
by y_j=b if y_j belongs to I, and otherwise retain alpha unchanged. If
j<n, go to the unique state at level j+1 with that assignment. If j=n,
the assignment now covers I; go to the terminal with bit f_i(alpha).
Both constant terminals are explicit, even if one is unreachable.

Thus each nonterminal level has at most 2^|I|≤2^k states. Every full
assignment follows a unique path which retains exactly its queried
support coordinates, and ends at its correct table value. Irrelevant
queries have equal successors, as allowed by the completion input.
Keeping states even after all relevant coordinates have been queried
fills terminal gaps without extra width. The construction is a dense
complete deterministic OBDD in the single global order, with O((n+1)2^k)
records per extension. It does not choose root-specific variable orders.
When I is empty the same construction has one state per level and a
constant table. No irrelevant original is removed from the universe.

If n=0, evaluate every source node as a scalar, give each root its exact
scalar graph, use exact signed wrappers and distinct-endpoint zero H
graphs. Their scalar defects vanish formally, so (2) holds, with d=h=1.
This also covers unused roots and empty original clauses. Henceforth
assume n≥1. Put w=2^k≥1. L026 supplies complementary-terminal auxiliary
signed diagrams and its width-two original-variable/width-one constant
diagrams. Let v=w+2; every auxiliary diagram has width at most v. Actual
signed outputs are the disjoint graph for 1+r_a, rather than a presumed
free Boolean identification. There are O(T+n+2) diagrams and roots in all.

**Formal reception and affine graphs.** The constructed output diagrams
compute the source extension functions on every assignment. Therefore
each agrees with the AND of its actual signed operand functions, exactly
the promise required by L026. That result supplies the degree bounds in
(1) and both formal identities (2). In particular, the auxiliary paired
product and the output representative agree in the increasing multilinear
subspace for this same global order; L026's injectivity in that subspace
justifies their free-algebra equality. Boolean agreement of arbitrary
free polynomials is never used. Originals retain x_j exactly, constants
retain 0,1, and absent nonextension variables retain zero. All signed
operands, including complementary or repeated ones, meet L026's cases.

Use the cited L071 component to write affine graphs for these identical
polynomials. Value graphs have affine edges 1+y_j and y_j. Its K graph
switches once from an earlier-variable commutation region to a value
suffix. Its W graph stays in a same-level operand-pair region until one
exit into a disjoint local correction block. These are the already
proved polynomial realizations of L026 (4), (6), (8), not generic
circuit-to-ABP conversion. Every correction factor is independently
copied; pair-to-pair edges implement recursive left multipliers. No
path unfolding, circuit label or return to a recursive pair region is
introduced. Equality of graph polynomials is established before any
substitution by that component, so it preserves both identities (2),
not only Boolean values. Value and witness path degrees are bounded by
n and 2n−1 respectively, as checked in L071's audit. Constants, equal
successors and zero terminal graphs retain its endpoint conventions.

**Aggregate encoding and deterministic time.** Set U=T+2,
B=T+n+2, q=(n+1)v and

    R=B(n+1)^2 v^3+n^2+1.

The imported component writes O(Bq) value/signed/base records,
O(T(n+1)^2v^3) records for all independently rooted H graphs, and
O(T(n+1)v^2) auxiliary product records. Optional reusable K templates
cost O(Bnq); all K copies inside H have already been paid separately.
Associations and alphabet positions cost O(B+n²). Thus O(R) pays the
whole explicit collection, without sharing between separate outputs.
All support-based input diagrams also fit this bound.

Here n≤T, B=O(U), w≤U, v=O(U), so q=O(U²) and R=O(U^6).
Each graph edge has at most two nonzero affine terms. Dense references
cost O(log(R+2)) bits; original names, symbol positions and source
associations cost at most O(T) bits per occurrence. The full original
axiom list/dictionary has O(T³) bits in L037's convention. Even writing
that dictionary afresh with each of the O(B) output graphs adds only
O(U^4). Therefore the component's graph bound gives

    E_ABP=O(R(T+log(R+2))+B T³)=O(U^7).

Root tables, terminal labels, order lists, support vectors and source
associations are explicitly paid. Original clause placeholders remain
in the dictionaries even though H does not use them. No uncharged
external alphabet or sparse identifier lookup is needed.

For a conservative bit-time implementation, supports, table evaluations,
prefix-state diagrams and all graph copies use O(U^6) indexed elementary
operations, by the preceding counts and the component's explicit
state/pair/copy loops. Each operation uses boundedly many lookups and
integer/name writes of at most O(U) bits; indices themselves have
O(log U) bits. Retain only O(U^7) bits of source, temporary tables,
templates and output. Even implementing each lookup by a complete
sequential scan costs O(U^7) bit steps; ordinary arithmetic and copying
can be bounded by an additional O(U²) factor per elementary operation.
This yields O(U^15), hence the stated conservative O(U^16) bound after
parsing, promise checking and output framing. This deliberately coarse
bound requires neither random-access unit-cost arithmetic nor an
efficient semantic-function test. No oracle or exact degree enters it.

Finally the source associations form L037's acyclic abstract DAG with
S=O(T), and every required r and H has just been supplied and charged.
Its N=2+T+S+E_ABP is O(U^7). Substituting into its existing O(N^8 log(N+2))
encoding and O(N^8) complete-degree conclusions proves the stated
certificate bounds. Its polynomial-time receiver composes with (1).
This is a proof-relative restriction, not a formula-length-only bound.

**Boundary and relevance checks.** Exponential exact degree is compatible
with the promise: repeatedly defining z_1 iff x AND x and z_(j+1) iff
z_j AND z_j keeps support {x} and gives exact free word degree 2^j.
The construction uses reduced diagram values and never corrects that
exact word to its reduced representative. L076's T+D criterion thus
does not provide this T-only estimate by itself. This is a boundary
example, not certificate hardness. L027/Attempt 019 concerns arbitrary
many-input extension values; L033/Attempt 020 concerns identical outputs
of arbitrary arithmetic circuits. Those stops are preserved and do not
refute this support-restricted, reduced-representative construction.

The required threshold is one fixed polynomial in actual T, achieved
here as O((T+2)^7) for data under the explicit support promise. Nothing
establishes that promise for arbitrary ER. This coherent all-size
specialization uses known representations and existing local witnesses;
no numerical experiment or mathematical script is needed. The construction
step requested a later audit of the support-independence bridge, complete
order, graph reception and full ledger before relying on this result
beyond the present informal construction record.

**Separate critical audit — step 298, 2026-10-17.** This audit uses the
unchanged SPECIALIZE scope in
`drafts/literature/2026-10-17-small-support-data-critical-audit.md`.
It checks the complete argument above against L026's hypotheses and
identities, L071's post-compilation construction and step-274 audit, and
L037's receiving statement. Existing primary-source coverage is reused;
no broader compilation theorem, new identity or implementation is claimed.

The dependence induction holds for every source node, not just the
extension currently being tabulated: two assignments agreeing on U_a
give the same value at a. At an AND node they agree on each operand's
support because both are contained in its union. Complement and repeated
operands preserve this implication. Thus completing a support assignment
by zeros is legitimate even though unrelated nodes in the full evaluation
can change when the outside coordinates change. Topological evaluation
does not unfold repeated ancestry. Positive original variables have
singleton support; absent proof variables and scalar constants have empty
support under the receiving convention. No minimal-support test is used.

For a diagram root i put I=U_i and let
m_j=|I intersect {y_1,...,y_(j-1)}|. Level j has exactly 2^m_j listed
states, all encoding distinct assignments to these queried support
positions. A relevant query extends that assignment by its branch bit;
an irrelevant query preserves it. This lands in the next listed state
when j<n. At j=n the updated assignment covers I and indexes the table,
so both last-level transitions are defined, including when y_n is in I.
The invariant along a full assignment path is its restriction to those
m_j positions. It proves the promised all-assignment function and bounds
every nonterminal level by 2^|I|≤2^k≤T+2. Even if support is exhausted
early, states persist to level n; neither an early terminal nor a new
variable order is introduced. Empty support has m_j=0 throughout.
Original-variable and constant auxiliary diagrams fit width v=w+2.
No reachability pruning removes unused extension roots or dictionary names.

The exact formal interface is essential. Each supplied output diagram
computes the Boolean AND of the actual signed operands on the same full
original universe. L026 identifies its ordered increasing multilinear
representative with the auxiliary paired product P, using injectivity
only in that subspace. Its complementary-terminal diagrams equal the
actual written 1+r_a wrappers formally, so using auxiliary signed operands
in W needs no additional witness. L071's value, K and W graphs have
precisely L026's recurrences before substitution. A K path switches once
to a value region; a W path exits the pair region once into a disjoint
ordered correction block. Neither can return. Equal successors retain
parallel edges and their multiplicities. Therefore both identities (2)
hold with the original independent placeholders, including repeated,
complementary and constant operands. This component invokes no selector
or treewidth premise; L071's full structural theorem is not being applied.

For n≥1, a value path over s remaining levels has degree at most s. A K
path has an affine prefix, one commutator placeholder and a value suffix,
again totaling at most s. A W path traversing n−s pair levels before its
local exit has degree at most (n−s)+(2s−1)≤2n−1; unit connectors add zero.
At the last level the K-terminal paths cannot accept and the Boolean
correction has degree at most one. Original roots and signed sum wrappers
obey d=max(1,n). For n=0, all roots are scalar evaluations with exact
complements, every defect is the scalar zero, and each H is a zero graph
with distinct endpoints. This avoids an accidental empty accepting path
and works with empty clauses, absent base variables and unused roots.

Independently count the actual objects with U=T+2. There are O(U) diagrams
and output roots, n+1=O(U), v=O(U), q=O(U²), and at most O(U³) pairs in
one definition. Each pair's constant number of local factors costs O(q)
records with independent copies. Thus one H costs O(U⁵), and all H cost
O(U⁶). All value/signed roots and input diagrams cost O(U³); auxiliary P
graphs cost O(U⁴); optional K templates cost O(U⁴). Associations and
alphabet positions are smaller. These bounds account for every separate
output, without sharing a correction factor across files. Support vectors
and tables use O(U²) bits; state annotations of length at most O(U) are
also below the final allowance.

Each affine edge has at most two terms. Graph references need O(log U)
bits; even verbatim original names and associations need at most O(U)
bits per occurrence. O(U⁶) records therefore cost O(U⁷) bits. Repeating
the O(T³)-bit complete axiom dictionary at each of O(U) output graphs
adds O(U⁴), within the same bound. Temporary K templates may reference
the explicitly retained collection dictionary. They are not additional
separately exported outputs. Clause placeholders remain paid although
unused by H. No framing or original-name cost is omitted.

The bit-time claim also survives an explicit coarse implementation.
Support unions, O(U²) source evaluations of O(U) gates each, prefix-state
generation, pair enumeration and fixed-factor graph-copy loops take at
most O(U⁶) record-level operations. Copying a factor iterates over its
already charged records; no operation enumerates all accepting paths.
Repeated dictionary writes add at most O(U⁴) elementary bit writes.
All source, support/table, diagram, template and output storage together
fits O(U⁷) bits. Lookups and renumbering can scan this entire store per
operation. Counters, names and annotations have O(U) bits or less; allowing
an additional O(U²) factor covers arithmetic, comparisons and field copies.
This gives O(U⁶ U⁷ U²)=O(U¹⁵), hence the stated O(U¹⁶) bound with parsing
and framing. The proof is an existence bound for a deterministic bit
algorithm, not a measured implementation time or a unit-cost RAM claim.

Finally S=O(T), both formal H identities, exact base/sign values and full
framing meet every stated L037 data premise. Its N=2+T+S+E_ABP is O(U⁷),
so its existing bounds give O(U⁵⁶ log U) bits and O(U⁵⁶) complete degree.
Its polynomial bit-time construction composes with the checked data
constructor. No certificate search or formula-only bound is inferred.
The audit establishes the reliability of this restricted input, with no
substantive defect, stronger theorem or progress beyond the checked
representations claimed. General support/data bounds, W/V/U,
every-certificate hardness and unrestricted SAT transfer remain open.

## Mathlib

Full matching support-to-L037 theorem, ordered free-algebra witnesses and
binary/time bounds: **not checked**; no absence claim. The exact primary
Boolean citations are Bryant §1 equation (1)/§2 Definitions 1–2 and de
Colnet–Ordyniak–Szeider §2.3/Proposition 2 above. Formal witness identities
are imported locally from L026, and affine graph realization from the
specified audited component of L071; their broader source assessments
are reused, without asserting a fresh primary-source read. L037 is used
only after its complete data hypotheses have been verified. This is
REPRODUCTION, not a claim of progress beyond the checked literature.

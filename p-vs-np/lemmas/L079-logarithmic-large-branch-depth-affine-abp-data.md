# L079 — Logarithmic large-operand branching depth supplies affine-ABP data

## Hypotheses

Use L037's width-at-most-three original CNF F and valid ER refutation pi,
with fresh acyclic definitions i iff a AND b on actual ordered signed
earlier operands, sorted-set clauses, weakening and selected-pivot
resolution. T=2+|F|+|pi| is the actual binary length, including names and
references. Retain its ordered original-clause falsity products, Boolean
axioms x_j²+x_j and pair-once commutators x_j x_l+x_l x_j as A(x), with
independent placeholders t. Work in the free associative algebra over F₂.
There are n≤T distinct originals occurring in F; nonextension proof
variables absent from F have positive value zero.

The canonical abstract value DAG has S=O(T) nodes: originals, scalar
bases, every positive extension, and exact signed nodes. Include unused
definitions and both signs. Aliases add no operation. Define syntactic
supports U_v by singleton originals, empty scalar/absent bases, inheritance
at signs, and union of the two operand supports at an AND. These are
reachable-original sets before Boolean simplification.

Put k=floor(log₂(T+2)). Call a node small if |U_v|≤k and large otherwise.
An AND is counted when BOTH actual operand supports have size greater
than k. Assume every path following source operands toward bases, from
any node including unused definitions and signs, encounters at most k
counted ANDs. Repeated operands retain their two occurrences. No global
diagram-width, exact unreduced-degree or treewidth bound is assumed.

## Conclusion

There is a deterministic construction of all L037 data with

    d=(S·2^k+1)(k+1),        h=max(1,2n−1),
    E_ABP≤K(T+2)^7,          bit time≤K'(T+2)^16.          (1)

Constants depend only on the fixed explicit encoding. All representatives
are Boolean-faithful x-only affine-edge ABPs; originals/constants are
exact and signed roots are exactly 1+r_v. Every AND has an affine ABP H_i
using only original Boolean/commutator placeholders with formal identities

    H_i(x,0)=0,          H_i(x,A(x))=r_i+r_a r_b.          (2)

The degree bounds are before axiom substitution. All separate roots,
signs, unused definitions, ordered operand occurrences, associations and
complete repeated original-axiom dictionaries are included. The chosen
values have paid formula trees of aggregate size O(S(S+1)2^(2k)).

L037 consequently supplies an original-axiom affine-ABP certificate with
both IPS identities, full bits O((T+2)^56 log(T+2)), complete degree
O((T+2)^56) and deterministic polynomial bit construction time. These
are bounds in supplied proof length, not original formula length alone.

This is an informal restricted sufficiency construction. The separate
step-306 critical audit below finds no substantive defect within these
hypotheses and changes no bound. POTENTIALLY_NEW means only that the prior source
assessment established no full match; originality is not certified.
Arbitrary ER data, formula-only bounds, W/V/U, every-certificate hardness
and unrestricted SAT decision/separation remain unresolved.

## Proof

**Scope and imported components.** The prior EXPLORE assessment is
`drafts/literature/2026-10-17-logarithmic-large-branch-depth-data.md`.
The changed step is the paid unfolding count under the counted-path
promise. Reuse L078's audited small-cone construction, including L077's
support/table/complete-diagram components, L026's local formal identities
and increasing-multilinear identification, and L071's audited
post-compilation affine graphs. Only those components are used: the
whole one-small-operand, whole-small-support and treewidth-two theorems
are not applied with weakened hypotheses. L076 is not an input.

The Boolean representation source is Randal E. Bryant,
[*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE TC
35(8), 677–691 (1986), author-restored §1 equation (1), §2 Definitions
1–2, PDF pp.3–4](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf).
For already paid formula trees import Ran Raz and Amir Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
undated 16-page author manuscript, §2.1 and Lemma 2 Step 1, PDF
pp.4–5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Its leaf, parallel-sum and ordered-serial-product cases give linear graph
size over F₂ with constants and mixed degree. The full lemma's later
zero-free-term hypothesis is not needed for this Step 1 conversion.
These imported constructions are not reproved or claimed as new; the
new count pays their formula input before invocation.

**Promise checking and globally consistent values.** Compute all supports
topologically by bit-vector union/inheritance. Compute b(v), the maximum
number of counted ANDs on a path from v, by zero at bases, inheritance
at signs, and

    b(i)=1_{|U_a|>k and |U_b|>k}+max(b(a),b(b)).          (3)

Thus max_v b(v)≤k checks the precise all-root promise in polynomial time.
The counts are at most S; no exponentially large integers are generated.
Support containment along operand edges implies that every predecessor
of a small node is small, and a small-output AND has two small operands.
Originals are small since T≥2 implies k≥1.

Fix one order y_1,...,y_n of originals. For each small positive extension,
enumerate assignments to its support and evaluate the source Boolean DAG
with outside originals set to zero. L077's support-dependence induction
applies to the entire source DAG without a size restriction: agreement
on U_v implies agreement at v. Hence these at most 2^k table entries
give the correct value under every completion, even when unrelated large
nodes depend on other originals.

Use L078's paid complete Shannon formula Q_i in the inherited support
order for that table. On m support variables it has 8·2^m−7 nodes and
syntactic degree at most m, lies in the increasing multilinear subspace
of the global order, and has the correct Boolean evaluations. Empty
support gives its scalar table. Set r_i=Q_i at small positive extensions,
retain exact original/scalar bases, and at every signed node use the
actual wrapper 1+r_v. Consequently every small root has a paid formula
of size at most M=10·2^k and syntactic degree at most k. This is precisely
the small-root component established and audited in L078; its argument
uses no promise on unrelated large ANDs.

At a large positive extension define r_i=r_a r_b with the supplied
operand order. Large signs again use 1+r_v. Recursively substituting
these equations until a small node gives a definite finite formula for
each root separately. Different occurrences, including repeated operands,
receive distinct copies. Boolean faithfulness follows topologically from
the small tables, exact bases, complementation and ordered products.

**Paid large-node unfolding.** Consider one large root. In its expansion
keep only the occurrences of large source nodes, with edges to their
large operand/predecessor occurrences. This is a rooted occurrence TREE:
sharing in the source never identifies two expanded occurrences. A large
sign has exactly one large child. A large AND has zero, one or two large
children; the last case is exactly a counted source AND. No large base
exists. Along any root-to-leaf path the source nodes follow actual
predecessor edges without repetition, by acyclicity, so the path has at
most S vertices. It also has at most k two-child vertices by the promise.

A finite rooted tree with outdegree at most two and at most b two-child
vertices along each path has at most 2^b leaves. To verify the needed
bound without bounding ordinary depth, suppress all one-child vertices.
If no split remains there is one leaf. Otherwise each of the two subtrees
below the first split has at most b−1 further splits per path; induction
gives at most 2^(b−1)+2^(b−1)=2^b leaves. This argument includes unequal
branch depths and the b=0 case. Every vertex lies on a root-to-leaf path;
summing the lengths of all such paths therefore bounds the total number
L of large occurrences by

    L≤S·2^k.                                             (4)

Repeated or complementary large operands are allowed now: both children
are distinct occurrences, and their common parent consumes one counted
branch on either path. Reconvergence in the source cannot defeat (4),
because the counting takes place in the expanded occurrence tree.

Let a be its number of AND occurrences and z its number of sign
occurrences, so L=a+z. The number of operand/predecessor slots is 2a+z.
Exactly L−1 of these slots are edges within the large tree. Every other
slot attaches one small formula. Thus the number of small attachments is

    2a+z−(L−1)=a+1≤L+1.                                (5)

Each AND adds one multiplication node. Each sign adds a plus node and
a scalar leaf, at most two nodes. Paying M for every attachment, without
sharing any of them, gives tree size

    M(L+1)+2L
      ≤10·2^k(S·2^k+1)+2S·2^k
      ≤12(S+1)2^(2k).                                   (6)

Already-small roots satisfy (6) directly. There are S roots, hence the
aggregate paid-tree size O(S(S+1)2^(2k)). At a product syntactic degrees
add, and a complement adds no degree. The degree of any large-root tree
is therefore at most k times the number of small attachments, at most
k(S·2^k+1)≤d. This bounds the chosen representatives, not unreduced
source polynomials or their degrees inside a small cone.

All formula operands retain their actual side and association. Only
complement additions occur above the cutoff tables, so there is no
uncounted addition that branches into two large expressions. As a
boundary check, with no counted vertices the large tree is a chain,
L≤S, recovering L078's single-chain estimate before the coarser (6).
For k allowed splits the extra factor is at most 2^k≤T+2, not an
iterated factor S at each split.

Apply the imported formula-to-graph conversion independently to every
paid tree. Its constant/variable edges and unit connectors preserve the
exact free polynomial and do not increase path degree beyond the tree's
syntactic degree. Fresh distinct terminals are available, including for
zero/scalar trees. Thus the same aggregate record bound and d apply to
the actual value graphs. No mixed-side skew-circuit-to-ABP theorem or
general degree-only circuit conversion is invoked.

**Exact local witnesses.** At every large positive extension the choice
r_i=r_a r_b is a formal identity, regardless of whether it is counted.
Take H_i to have distinct endpoints and no accepting path. Both (2)
hold with zero polynomial. No Boolean reduction or commutation is used
at these gates, even with identical operands.

For a small-output definition both operands are small. Use L077's
complete prefix-state diagrams only for small positive tables, and
L026's trivial original/scalar diagrams and complemented-terminal signed
copies. They all use the same global original order and all n levels,
including irrelevant equal-successor tests and terminal gaps. Each has
width at most v=2^k+2. No diagram for any large root is needed.

Each small table formula and its diagram polynomial lies in the same
increasing multilinear subspace and has the same Boolean evaluations.
L026's injectivity on that subspace identifies them formally. Its base
identification gives exact originals/scalars, and its complement identity
identifies signed diagrams with the actual 1+r_v wrappers. Thus the
diagram roots are precisely the chosen small operands and output as
free polynomials, not just equal Boolean functions.

For this small-output definition, L026's local paired-state recurrence
(7)–(9) constructs P and W, with W(x,0)=0 and
W(x,A)=r_a r_b+P. Its P is increasing multilinear and computes the
pointwise product of the two operand functions. That function is the
small output's table, so the same injectivity gives P=r_i. Hence the
W root supplies exactly (2). This uses L026's proved local interface on
these three diagrams; it does not assert a diagram family for all large
outputs. Ancestor-closure also ensures no hidden large input to a small
output has been omitted.

Use L071's audited post-compilation value/K/W/P graph component to write
that identical W polynomial as an affine-edge ABP. Its pair-state region
has only left-multiplied recursive transitions and a one-way exit into
independently copied K/value blocks. It uses O((n+1)²v³) records per
definition, with no return to a recursive pair state from a correction.
Its before-substitution path-degree bound is 2n−1: a path with s levels
remaining on exit has prefix degree at most n−s and correction degree
at most 1+2(s−1), totaling at most n+s−1. Both formal identities are
preserved because this is equality of free polynomials before substitution.
The audited component covers constants, coincident successors, repeated
and complementary operands, with their displayed factor order retained.

If n=0, every node is small; evaluate all tables as scalars, keep exact
signed wrappers and use zero H at every definition. The defects vanish
as scalar identities, and d,h≥1 suffice. Empty clauses and unused
definitions do not change any of these obligations.

**Complete degree, bit and time ledger.** Put U=T+2. Then S=O(U),
n+1=O(U), 2^k≤U and v=O(U). Equation (6) gives O(U^4) total value
formula/graph records. In particular d=O(U² log U), a fixed polynomial;
h=O(U). All roots are paid separately, including both signs and unused
definitions.

The unchanged small-root component has O(U) diagrams with O(U²) records
each. There are at most T small-output definitions, each with O(U^5)
witness records, so all H total O(U^6). Large-output zero H add O(U)
records. Auxiliary P graphs cost O(T(n+1)v²)=O(U^4); optional
earlier-variable K templates cost O(U(n+1)²v)=O(U^4), with every copy
inside H already counted in the O(U^6). These are temporary components,
not extra independently exported roots. Supports and small table bits
fit O(U²). State annotations, source associations and common-order lists
fit the aggregate O(U^6) record allowance. No dense-diagram path expansion
is used; only the separately bounded value trees are unfolded.

Every edge has at most two affine terms. Dense references cost O(log U)
bits and restored original names/associations at most O(U) bits per
occurrence. The complete ordered width-three-clause/Boolean/pair-once
dictionary costs O(T³) bits in L037's convention. Repeating it with each
of O(U) separately exported value/H graphs adds O(U^4), retaining unused
clause entries. Independent renumbering and full root framing are also
charged. Thus O(U^6) records give E_ABP=O(U^7), proving (1).

For an explicit coarse bit-time implementation, support computation and
(3) are polynomial topological loops. At most O(U²) table evaluations
each visit O(U) source nodes. Traverse the paid trees by occurrence;
O(U^4) visits suffice and recursion depth is at most S plus table depth.
Diagram generation, state-pair loops, K templates and all individual
correction-record copies use O(U^6) elementary indexed record operations,
as in the unchanged audited component. Counters and dense references have
O(log U) bits. Source, temporary and final storage fit O(U^7) bits. Even
replacing every indexed access by a sequential scan of that storage and
allowing an additional O(U²) per operation for binary arithmetic, names
and writing gives O(U^15), within the stated O(U^16) bound including
parsing, promise checking and repeated dictionaries. No unit-cost copy
of an unbounded graph, semantic-support oracle or general identity test
is assumed.

All L037 premises are now met: the actual acyclic associations, exact
bases/signs, every formal local relation, d,h≥1 and complete E_ABP.
Its parameter N=2+T+S+E_ABP is O(U^7), giving the downstream bounds in
the conclusion. These are conditional on the structural promise, not
on a bound for every ER proof or a finder for short proofs.

**Threshold and limitations.** The sought threshold was one fixed
polynomial in actual T for all separate values, witnesses, degrees and
bit time; (1) meets it under the stated counted-path promise. Attempts
019–020 retain their unrestricted-width and general same-output stops.
No large-root diagram, polynomial unreduced degree or arbitrary skew
conversion was used. The claim expands a sufficient representation
class, not an unrestricted ER/SAT argument. No finite experiments or
mathematical scripts are claimed as verification. A separate critical
audit must check the occurrence-tree count, exact small-root reception
and complete ledger; this construction turn is not that audit.

**Separate critical audit — step 306, 2026-10-18.** The pre-existing
SPECIALIZE assessment is
`drafts/literature/2026-10-18-logarithmic-large-branch-depth-critical-audit.md`.
Its approved task is this audit of the existing construction. Reuse the
inspected Bryant and Raz–Shpilka components at the precise locations
cited above; neither supplies the changed occurrence bound. The earlier
pending-audit statements describe the construction step and are superseded
by this section. This is an all-size informal proof audit, not a new
representation theorem, finite experiment or formal verification.

First check that the proposed cutoff is well defined on the actual
source. Every operand support is contained in its AND output support,
and every sign has its positive node's support. Thus small cones are
ancestor-closed, with no large predecessor hidden under a sign. Equation
(3) counts a gate once on each path traversing it, including when both
operand references are equal; it does not count the total number of
counted vertices in the DAG. Computing maxima topologically checks the
stated all-root promise, including unused definitions. Syntactic support
containment is sufficient here; no minimal semantic support is needed.
L077's dependence induction applies to all source nodes, so zero-filling
outside a small support gives its correct table under every completion,
even though unrelated large nodes may change.

For one large-root occurrence tree, unary vertices include every sign
and every AND with one large operand. Two-child vertices are exactly
the counted ANDs; a zero-child large vertex must be an AND with two
small operands, since bases are small and signs inherit support. After
suppressing unary vertices, induction on the remaining branching budget
gives at most 2^k leaves. Each leaf-to-root path follows strictly earlier
source nodes and has at most S vertices. Associate each occurrence with
any leaf below it; it belongs to that leaf's root path. Hence the union
of these paths has at most S times their number of leaves, proving (4)
without asserting that the source DAG itself is a tree. Reconvergence,
unequal branch depths and repeated or complementary large operands do
not change this argument. A repeated large operand creates two copied
children and consumes a counted gate on either path. Aliases introduce
no extra operation or branching.

Independently count the attachment slots. With a AND occurrences and z
sign occurrences, L=a+z and there are 2a+z slots. The large tree uses
exactly L−1 of them as internal edges. Thus exactly a+1 slots attach
small formulas; the scalar summand of a sign is paid among its two
added nodes, rather than as another operand slot. For a small positive
table on m variables, the two distinct Shannon children and seven other
nodes give 8·2^m−7 nodes. An actual sign adds two nodes, and all small
base/sign cases fit M=10·2^k. Consequently

    size ≤ 10·2^k(S·2^k+1)+2S·2^k
         ≤ 12(S+1)2^(2k).

The last inequality has positive slack for 2^k≥1. Every attachment is
independently copied, including repeated occurrences in the same root;
summing over S roots pays independent output files as well. Each
attachment has syntactic degree at most k, so every root has degree at
most k(a+1)≤k(S·2^k+1)≤d. This argument retains each multiplication's
side and association, including alternating sides. It bounds chosen
cutoff formulas, not the source's unreduced syntactic degree. Raz–Shpilka
Step 1 receives only these paid trees; sum branches select one summand,
ordered product paths concatenate factors, and unit connectors add no
degree. Its graph conversion therefore preserves both formal polynomials
and the displayed path-degree bound. No unrestricted skew conversion is
being inferred.

Next check the exact small-output receiver. Each small table's complete
prefix-state diagram has at most 2^k states at each of the n global
levels: relevant tests extend the recorded assignment and irrelevant
tests keep it. Equal-successor tests fill all gaps, including after the
last support variable and for empty support. All roots use the same
global order. The table formula and the diagram polynomial both lie in
L026's increasing-multilinear subspace and agree on every Boolean input;
its proved injectivity gives equality in the free algebra. Trivial
diagrams give the prescribed original/scalar polynomials. Complementing
terminals gives exactly 1+r, so the auxiliary signed operand diagrams
equal the actual chosen signed wrappers, although their graph encodings
are different.

For a small-output AND both operands are small. L026's P for those exact
signed operands is increasing multilinear in that same order and agrees
with the output table. Therefore P=r_i formally. Its W identity is then
exactly W(x,A)=r_a r_b+r_i, and its independent zero-at-zero induction
gives W(x,0)=0. No Boolean-to-free inference is used for a large root.
L071's post-compilation graph computes this same W before substitution:
the pair-region edges implement only the two left recursive multipliers;
its three exit blocks are e_0 K_0(v_0+v_1),
e_1 K_1(v_0+v_1) and b(u_0+u_1)(v_0+v_1), in exactly that order.
Each exit enters disjoint factors and can never return to a pair vertex.
K switches once to a value region, and neither K nor W terminals accept.
Thus no entire recursive W is copied and no placeholder-free empty path
is introduced. Both identities in (2) survive the graph realization.
At a large-output AND, r_i is the formal ordered product r_a r_b even
when both operands are small or equal. Its distinct-endpoint zero H
therefore satisfies both identities directly, without a diagram for i.

For n≥1 a value path over s suffix levels has degree at most s, as does
a K path over those levels: one placeholder replaces one query factor.
A W path exiting with s levels remaining has at most n−s prefix degree
and correction degree 1+2(s−1), totaling n+s−1≤2n−1. At s=1 the K
corrections have no accepting paths and the Boolean block has degree at
most one. Constants and unit connectors add no degree. These are bounds
before axiom substitution and even before path cancellation. Repeated
successors retain separate edges; complementary/repeated operands retain
the four ordered terms in L026's proof. Empty support uses a constant
table and complete redundant tests. When n=0 there are no large nodes:
all values and products are scalar polynomials, exact signed wrappers
remain scalar, and every distinct-endpoint zero H has the required zero
defect. The stated d,h≥1 cover this branch. Empty original clauses and
unused definitions do not remove any output or dictionary obligation.

Finally independently substitute U=T+2. S=O(U), n+1=O(U) and
v=2^k+2=O(U). All paid value trees and converted graphs total O(U^4)
records. One H has O((n+1)v²) pair vertices and O((n+1)v) independently
copied factor records at each, hence O(U^5) records. At most O(U) such
outputs give O(U^6) records. O(U) small diagrams cost O(U^3), auxiliary
P graphs cost O(U^4), and optional K templates cost O(U^4); copies of
their records inside H are already charged in O(U^6). Zero relations,
signs, root framing, source associations and original alphabet positions
fit the same allowance. Temporary templates are not additional required
exports, and no complete diagram paths are enumerated.

Dense references use O(log U) bits, every edge has at most two affine
terms, and even verbatim original names and state/source annotations
cost at most O(U) per record. Thus graph data cost O(U^7) bits. The
complete width-three clause/Boolean/pair-once dictionary has O(T³) bits;
repeating it in O(U) separate value/H exports costs O(U^4), not an
uncharged shared input. This includes unused clause entries. The chosen
d is O(U² log U) and h=O(U), both polynomials in original T.

The coarse bit-time implementation also survives. Supports and all
small table evaluations need O(U^3) indexed operations, paid tree visits
O(U^4), and graph/template/pair/correction copies O(U^6) record operations.
Each graph copy visits its individual records. Source, temporary and
output storage together fit O(U^7) bits. Replacing indexed access by a
scan of this storage, with another O(U²) per operation for counters,
names, annotations and writing, costs O(U^15), within the stated
O(U^16) including parsing, promise checking and dictionaries. No operation
copies an arbitrarily large graph at unit cost.

All L037 receiving hypotheses are therefore met, with its unchanged
N=2+T+S+E_ABP=O(U^7). Its O(N^8 log(N+2)) full-bit and O(N^8) degree
bounds give exactly the stated O(U^56 log U) and O(U^56) conclusions.
Direct mathematical inputs and the DAG are unchanged. The audit finds
no substantive defect or theorem/bound repair. Attempts 019–020 remain
stops for their different unrestricted promises. This is new local
verification of a restricted input, without a claim of mathematics
beyond the checked sources or certified originality. Arbitrary ER data,
formula-only bounds, W/V/U, every-certificate hardness and unrestricted
SAT decision/separation remain unresolved. No scripts, proof strings or
finite-test certificates were needed or verified.

## Mathlib

Full matching support-sensitive theorem and complete data construction:
**not checked**; no absence claim. Supporting mathematical inputs are
the precisely cited Bryant and Raz–Shpilka constructions and the local
audited components identified above. The prior comparison found no
inspected full-statement match. This is not certified originality or
formal verification.

# L078 — One small-support operand supplies affine-ABP data

## Hypotheses

Use L037's width-at-most-three original CNF F and valid fresh acyclic
signed-AND ER refutation pi. Let T=2+|F|+|pi| be the actual binary length,
including names and references. Retain the ordered original-clause,
Boolean and pair-once commutator axiom list A(x), with independent
placeholders t, over the free associative algebra over F₂. There are n
distinct originals occurring in F, n≤T. A nonextension proof variable
absent from F has positive value zero.

The canonical abstract value DAG contains originals, scalar bases, each
positive extension with its two actual ordered signed operands, and both
signs of every proof variable. Include unused definitions. Aliases add no
operation; signed nodes complement their positive nodes. Write S=O(T)
for its number of nodes. Use L077's syntactic supports: originals have
singleton support, scalar/absent bases have empty support, signs inherit
support, and U_i=U_a union U_b at the definition i iff a AND b. These
are reachable original-variable sets before Boolean simplification.

Put k=floor(log₂(T+2)). Assume that at EVERY AND definition at least one
of |U_a|,|U_b| is at most k. The small operand may be on either side,
and that side may change between gates. No whole-root support, degree,
treewidth or common-order-width bound is assumed for large roots.

## Conclusion

There is a deterministic construction of all L037 data with

    d=(S+1)(k+1),       h=max(1,2n−1),
    E_ABP≤K(T+2)^7,     bit time≤K'(T+2)^16.                 (1)

Constants depend only on the fixed explicit encoding. Every separately
written value is an x-only affine-edge ABP, faithful on every Boolean
assignment. Originals/constants retain their prescribed values and
signed roots are exactly 1+r_a. Every AND has an affine-edge ABP H_i with

    H_i(x,0)=0,       H_i(x,A(x))=r_i+r_a r_b               (2)

as formal free-algebra identities. H uses only Boolean/commutator
placeholders; complete original-clause dictionaries remain included.
Degrees in (1) are before axiom substitution. All roots, signs, unused
definitions, associations, independent copies and repeated dictionaries
are charged. In fact all representatives have paid formula trees of
aggregate size O(S(S+1)2^k).

Applying L037 gives an original-axiom affine-ABP certificate with both IPS
identities, full bits O((T+2)^56 log(T+2)), complete pre-substitution
degree O((T+2)^56), and deterministic polynomial bit construction time.
This is an informal restricted sufficiency result. Its separate step-302
critical audit below found no substantive defect in the stated theorem
or bounds. Classification POTENTIALLY_NEW for the construction means only
that the prior search did not establish a full matching theorem; originality is not
certified. It establishes no unrestricted ER data premise, formula-only
bound, W/V/U, every-certificate hardness or SAT decision/separation.

## Proof

**Scope and imported components.** The prior EXPLORE assessment is
`drafts/literature/2026-10-17-one-small-operand-affine-abp-data.md`.
Import ordered Shannon representation from Randal E. Bryant,
[*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE TC
35(8), 677–691 (1986), author-restored §1 equation (1) and §2
Definitions 1–2, PDF pp.3–4](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf).
Import paid formula-to-graph conversion from Ran Raz and Amir Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
undated 16-page author manuscript, §2.1 and Lemma 2 Step 1, PDF
pp.4–5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Only its scalar/variable, parallel-sum and ordered-serial-product cases
are used, before homogenization. They admit constants and mixed degree
over F₂. The full lemma's later zero-free-term requirement is not invoked.
Neither standard construction is reproved here.

Use L077's audited support-evaluation and complete-diagram components,
L026's increasing-multilinear identification and formal pair witnesses,
and L071's audited post-compilation value/K/W/P graph component. The last
component realizes L026's identical polynomials for supplied diagrams;
it does not require treewidth after those diagrams are supplied. We do
not apply L071's whole structural theorem or L077's whole-root theorem
to the present proof. The difference requiring proof is a globally
consistent representative choice, its paid formula presentation and
local witness reception under the operand-only promise. L076's T+D
bound and mixed-side skew-to-ABP conversion are not inputs.

**Small representatives.** Call a source node small if |U_a|≤k, and
large otherwise. Fix one order y_1,...,y_n of all original names. Compute
every support by topological bit-vector union and inheritance; this
checks the promise in polynomial time. Support is monotone toward a
descendant: if a node is small, all its ancestors are small. This follows
from containment in a union and equality at a sign. In particular, a
small-output AND has two small operands. Originals and scalar bases
are small since k≥1.

For each small positive extension i, enumerate all assignments to U_i,
evaluate the source DAG with outside originals zero, and record its bit
table f_i. L077's support-dependence induction applies to every source
node without a size bound on the other nodes: the value at i depends only
on U_i. Thus the table is correct for every completion to the original
universe, even though large unrelated roots can change. There are at
most T·2^k table entries, each found by O(T) Boolean gate evaluations.
No exact high-degree polynomial or minimal semantic support is computed.

For U_i={z_1,...,z_m} in the inherited global order, write the complete
ordered Shannon FORMULA for this table, denoted Q_i. At a table prefix
its expression is (1+z_j)Q_0+z_j Q_1; at a full assignment it is the
recorded scalar. Both children are written as distinct occurrences.
For m=0 the formula is just the table's scalar. The size recurrence is
L(0)=1 and L(m)=2L(m−1)+7, whence L(m)=8·2^m−7. Its syntactic degree
is at most m. Its polynomial lies in the increasing multilinear subspace
for the fixed global order, and its evaluations are f_i. This uses the
imported Shannon representation; the explicit count pays its tree input.

Set r_i=Q_i at small positive extensions. For original generators use
the literal x_j, and for scalar/absent bases use their prescribed scalar.
For EVERY signed node use the actual formula 1+r_a, including when a is
small. Thus a small signed representative has size at most 8·2^k+2 and
degree at most k; original/signed-base cases satisfy the same allowance.
These signs need not be separately reconstructed from their truth tables.
They are increasing multilinear and have the complemented evaluations.

**Large representatives and copying.** At a large positive extension i,
set r_i=r_a r_b with the actual left/right operand order. At a large
signed node use 1+r_a as prescribed. These equations, together with the
small table cutoffs, define paid trees independently for every root by
recursively substituting operands until reaching a small node.

In this recursion a large AND has at most one large operand by the
promise; a large signed node has one large predecessor. Hence the
large-node occurrences of a single expanded tree form a single chain.
Its length is at most S, because predecessor indices strictly decrease.
If both operands of a large AND are small, that chain ends with two
small attachments. Otherwise each large AND attaches one small formula
and continues on its sole large operand. Consequently there are at most
S+1 small attachments. A signed operation adds its plus node and scalar
leaf, at most two nodes; an AND adds one multiplication node. Put
M=10·2^k, which covers every small formula including sign wrappers.
For every root its tree size is bounded by

    (S+1)M+2S ≤ 12(S+1)2^k.                              (3)

A root already small satisfies (3) directly. Summing over all S roots
gives the aggregate bound in the conclusion, without inter-root sharing.
Every small attachment has syntactic degree at most k. A complement
adds no degree and a product adds the degrees of its two children, so
each such tree has degree at most (S+1)k≤d. This bounds the CHOSEN
representatives, not the exact unreduced source polynomials. In
particular, repeated large operands cannot occur at an admitted AND:
their two support sizes would both exceed k. Repeated small operands
are allowed and their copies are fully charged.

The chain argument retains both multiplication sides in their actual
positions. It uses that complement is the only addition above the table
cutoffs; arbitrary additions of two large expressions are not present.
It invokes no noncommutative mixed-side skew equivalence. Applying the
imported conversion to these already paid trees gives O(S(S+1)2^k)
aggregate graph records. The disjoint sum/product conversion preserves
formal polynomials, with constant edges and fresh distinct endpoints;
unit connectors add no degree. Thus the same d bounds path degrees.

All representatives are Boolean-faithful: at a small positive root this
is the source table, at a base it is the prescribed value, at a sign it
is complementation, and at a large AND it follows inductively from the
two earlier operands. No consistency is imposed between a small table
and an exact unreduced high-degree expression in the free algebra.
The local witnesses below supply exactly the necessary consistency.

**Local witness reception.** At a large positive extension i the defining
choice is the formal equality r_i=r_a r_b. Set H_i to a zero graph with
distinct endpoints and no accepting path. Both identities (2) hold
formally; no commutation or Boolean reduction occurs at this gate.

At a small positive extension i, both actual signed operands a,b are
small. Construct complete diagrams for all small positive tables in the
single global order, using L077's prefix-state component: at level j a
state records the assignment to U_i intersect {y_1,...,y_(j−1)}; relevant
queries extend it and irrelevant queries have equal successors. All n
levels are retained, including after support is exhausted. There are at
most 2^k states per level. Include the trivial original/constant diagrams
and complementary-terminal signed copies. This construction needs small
support only for each table it actually receives. No diagram is supplied
or assumed for any large root.

Every resulting L026 diagram polynomial is increasing multilinear in the
global order. For a small positive root its evaluations equal those of
Q_i, which is in that same subspace. L026's injectivity therefore gives
formal equality of their polynomials. It also identifies trivial diagram
roots with exact originals/constants. Signed diagrams equal 1 plus their
positive diagram polynomial by L026's complement identity, so they are
formally equal to the actual signed wrappers used in our trees.

For each small-output definition the three relevant diagrams compute
its output and its two actual operands, and their Boolean functions
satisfy the defining AND on all original assignments. L026's local
paired-state construction thus supplies H_i=W_(a,b) satisfying both
identities (2): the paired product P is equal to r_i in the increasing
multilinear subspace, and the operand representatives just identified
are the actual r_a,r_b. This application is to the local recurrence and
its proved identity, not to a purported diagram family for all large
outputs. The small subcollection is ancestor-closed, although the local
recurrence needs only these particular diagrams.

L071's audited post-compilation graph component writes the identical
W polynomial as an affine ABP. Its pair region has only left-multiplied
recursive transitions and a one-way exit into independently copied K
and value correction blocks. Its equality before substitution preserves
both formal identities, not only Boolean evaluation. The degree before
substitution is at most 2n−1, as in its audited path-degree count.
Repeated/complementary operands, equal successors, constants and empty
supports are covered by those identities, with no simplification of
their actual order. All labels use original x and original placeholders.

If n=0 all nodes are small, every table is a scalar, and all signed
values and products agree as field elements. Use distinct-endpoint zero
H throughout, with d,h≥1. This separate case avoids requiring positive
diagram depth. Empty clauses and unused definitions alter none of the
arguments or output obligations.

**Complete aggregate ledger.** Put U=T+2 and v=2^k+2=O(U), and assume
n≥1 for these counts. There are O(U) small table/auxiliary diagrams,
each with O((n+1)v)=O(U²) records. Supports and table bits use O(U²)
space. Equation (3) gives O(S(S+1)2^k)=O(U³) total value formula and
value graph records, including both signs and every unused root.

For each small-output definition L071's component uses
O((n+1)²v³) records for H, independently copying all its correction
blocks. There are at most T such definitions, so all H cost O(U⁶)
records; the zero H for large outputs add O(U). The auxiliary paired
product graphs cost O(T(n+1)v²)=O(U⁴); optional earlier-variable K
templates cost O(U(n+1)²v)=O(U⁴). No template is an implicit output
label, and every copy placed in H is already charged. Associations,
terminal tables, common-order lists and alphabet positions fit within
these bounds. There is no complete-path enumeration for any dense diagram.

The entire graph collection therefore has O(U⁶) records. Labels have
at most two affine terms. Dense references cost O(log U) bits, and
restored original identifiers/associations at most O(U) bits per
occurrence. The complete original-axiom dictionary costs O(T³), under
L037's width-three clause and pair-once convention. Repeating it with
each of O(U) exported value/H graphs adds O(U⁴) bits, including unused
original-clause entries. Hence E_ABP=O(U⁷), as claimed. Source framing,
separate root renumbering and complete signed outputs are included.

For a conservative bit-time bound, support computation, O(U²) table
evaluations of O(U) source nodes, writing the paid trees, diagram
generation, state-pair loops and all component copying use O(U⁶)
elementary record operations. This counts copying by records written,
not by a unit-cost whole-graph operation. Retain O(U⁷) bits of source,
temporary templates and final outputs. Implement every indexed access
by a sequential scan of that storage if necessary, with a further
O(U²) allowance per operation for binary arithmetic, names and writes.
This gives O(U^15), absorbed by the stated O(U^16) bound including
parsing, promise checking and framing. No semantic-support oracle,
exponential integer or general polynomial identity test is required.

The source associations give S=O(T); (1) and (2) meet every L037
receiving premise. Its parameter N=2+T+S+E_ABP is O(U⁷), giving the
stated downstream certificate bounds. Its own polynomial-time receiver
composes with this construction. These are bounds in supplied proof
length T, not solely in formula length.

**Relevance and limitations.** The required threshold was one fixed
polynomial in T for all roots and witnesses; (1) meets that threshold
under the operand-only promise. Large roots need not be increasing
multilinear or have small diagrams. Boolean-to-formal identification is
used only at small roots, never at those large roots. Exact unreduced
degree may be exponential within a small cone and is not a charged
parameter. Attempts 019–020 retain their unrestricted width and general
same-output conversion stops; neither conversion is used here. No
condition is supplied making arbitrary ER satisfy the operand promise.

This is an all-size informal proof. No mathematical script or finite
test is claimed as verification. The separate critical audit below
checks the single-chain count, exact table/diagram/sign identification,
local scope of witness import and complete bit-time ledger.

**Separate critical audit — step 302, 2026-10-17.** This audit uses the
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-17-one-small-operand-data-critical-audit.md`.
The primary representation coverage recorded above and in step 299 is
reused. The audit reads L026's local formal identities, L071's audited
post-compilation graphs, L077's audited support/diagram components and
L037's receiving statement. It does not apply the whole treewidth or
whole-root-support theorems with weakened hypotheses. The conclusion
and constants' scope are unchanged; this is verification of an existing
restricted input, not a new theorem or certified originality.

First, support containment is syntactic and applies to every operand
occurrence. If an AND output is small, both operands are small. A sign
has exactly its positive node's support. Therefore all predecessors of
a small node are small, irrespective of Boolean cancellations. The
support-dependence induction in L077 needs no size bound and applies
to the entire source DAG: agreement on U_a suffices for agreement at a.
Consequently the zero-filled evaluations used for a small table are
correct even when unrelated large nodes change under another completion.
Each evaluation is topological Boolean computation, not formal source
unfolding. Absent nonextension variables are scalar zero, including
when they occur only in the proof; their signed values are exactly one.

For a table on m ordered support variables, its fully written Shannon
formula has two independently written children and seven other nodes:
the plus and two leaves of 1+z, the two multiplication nodes, the other
z occurrence and the outer plus. Hence L(m)=2L(m−1)+7 with L(0)=1
indeed gives 8·2^m−7 nodes. Each variable is earlier than every variable
in either child. Thus every word is increasing and multilinear and the
syntactic degree is at most m, even for constant tables. Actual signs
add a plus and scalar leaf rather than identifying formulas syntactically
with separately tabulated complements. The bound M=10·2^k covers these
two nodes, original/signed-original leaves and scalar bases. Here T≥2,
so k≥1 and original singleton supports are small.

Independently inspect one large-root expansion. At each large AND at
most one operand is large; a large sign has one large predecessor.
Following those predecessors gives a chain in the acyclic source, of
length ell≤S. A large sign cannot be its bottom vertex because its
predecessor has the same support. Its bottom large AND has two small
operands. If there are a AND vertices on the chain, it has a+1 small
attachments: one at each continuing AND and two at its last AND. This
is at most S+1. Every sign adds two nodes and every AND adds one, so
the total is at most (S+1)M+2S≤12(S+1)2^k, including all attachment
copies. Already-small roots obey the same bound directly. Summing over
all S roots proves the stated aggregate size without cross-root sharing.
The small operand's side may change at every gate: substitution keeps
the written left/right order and never rotates or commutes a product.
The only additions outside attachments are complements, which do not
duplicate the continuing large expression. This is why a general
mixed-side skew-circuit assertion is neither needed nor inferred.

Each attachment has syntactic degree at most k; signs take a maximum
with zero and products add degrees. Thus a root has degree at most
(S+1)k≤d. The imported paid-tree conversion preserves each ordered
polynomial and cannot increase this path-degree bound: sum paths select
one branch, product paths concatenate the two factors, and unit edges
have degree zero. Faithfulness follows separately from the small tables,
exact bases/signs and the ordered large AND recursion. Nothing equates
these representatives with the unreduced source polynomials.

Next inspect the small-output formal interface. For each small cone
I, a level-j diagram state records the assignment to
I intersect {y_1,...,y_(j−1)}. A relevant query extends that record by
its branch bit and an irrelevant query preserves it. At the last query
the record covers I and indexes the table. These are precisely L077's
complete-prefix transitions, with at most 2^|I|≤2^k states per level,
even when I is empty or its last variable precedes y_n. No early
terminals or differing root orders are introduced. Original/constant
auxiliary diagrams fit width v=2^k+2.

For each small root, the diagram polynomial and its chosen table formula
are in L026's same increasing-multilinear subspace and have identical
Boolean evaluations. L026's injectivity therefore identifies them as
free polynomials. Trivial diagrams identify exact original/scalar bases;
complementing terminals identifies signed diagrams with the actual 1+r
wrappers formally. These equalities justify using the diagram operands
inside the witness recurrence, though their graph encodings differ from
the paid-tree value outputs. For a small-output definition, L026's pair
polynomial P computes the Boolean AND of these actual signed operands.
It too is increasing multilinear in this order, so P=r_i formally.
This use of injectivity is confined to small outputs and their operands.

L026's W identity then has exactly the required right side r_a r_b+r_i.
L071's graph implementation computes that W before substitution: K
switches once into a value region, and W traverses its pair region then
exits once into one disjoint correction block. At current query y_j its three ordered blocks
are e_0 K_0(v_0+v_1), e_1 K_1(v_0+v_1), and
b_(y_j)(u_0+u_1)(v_0+v_1). There is no return to the pair region, and
terminal pair vertices do not accept. Thus the graph's recurrence is
the same formal polynomial, not just a Boolean equivalent. Every
accepting correction contains a placeholder; H(x,0)=0 follows as well
as the substituted identity. At a large output r_i=r_a r_b by the
chosen definition, so its distinct-endpoint zero graph gives both H
identities immediately, without an auxiliary output diagram.

In a suffix of s levels a value path has degree at most s. A K path's
affine prefix, one placeholder and following value suffix also total at
most s. A W path exiting with s levels left has an initial n−s affine
prefix followed by a correction of degree at most 1+2(s−1); its total
is at most n+s−1≤2n−1. Unit connectors contribute zero. This checks
pre-substitution degrees of the actual witness graphs, including
constant edges, not only their evaluated polynomials. At s=1 terminal
K graphs have no accepting path and the Boolean block has degree at
most one. Hence h=max(1,2n−1) is sufficient.

Repeated or complementary large operands would both have support larger
than k and are excluded by the promise. Repeated or complementary small
operands are admitted; their independently copied occurrences and signed
wrappers remain present. L026's four-term product identity retains their
order and multiplicities, including coincident successors. A large
output with two small operands is permitted and is exactly the bottom
case in the chain count; its relation is zero by formal definition.
Unused roots are counted throughout. Empty support gives constant tables
and valid complete diagrams when n≥1. For n=0 all supports are empty,
all source values are scalars and each defect is scalar zero, so the
separate zero-H construction needs neither positive-depth diagrams nor
nonexistent Boolean/commutator axioms. Exact signed wrappers retain
degree zero. Empty original clauses affect neither case.

Finally put U=T+2. There are O(U) source/output roots, O(U) diagrams,
n+1=O(U), and v=O(U). The paid value trees and their graphs total O(U³)
records. One small-definition pair region has O((n+1)v²)=O(U³)
vertices. At each vertex its constant number of independent factors
costs O((n+1)v)=O(U²), so one H has O(U⁵) records and all H have
O(U⁶). No full W is copied at a recursive transition. Auxiliary P
graphs and optional K templates each total O(U⁴); copies taken from
templates into H are already included in the O(U⁶) count. Zero H for
large outputs, state annotations, source associations, signed roots,
and alphabet entries are also covered. Templates are temporary objects,
not additional independently exported roots with uncharged dictionaries.

Each edge has at most two affine terms; its dense references cost
O(log U) bits and even verbatim source names/associations cost O(U)
per record. Thus the graph collection costs O(U⁷) bits. The ordered
width-three clause, Boolean and pair-once commutator dictionary costs
O(T³) bits; explicitly repeating it with O(U) value/H exports adds
O(U⁴). This retains unused clause placeholders and all original names.
No graph copy or symbol occurrence requires sharing across output files.

The deterministic time claim admits the stated coarse implementation.
Support/table computation uses O(U³) elementary indexed operations;
tree traversal writes all counted occurrences; diagram, pair, template
and correction-copy loops take O(U⁶) record operations in total. A copy
iterates over individual records rather than being one operation on an
arbitrarily large graph. Dictionary writes fit O(U⁴) bit operations.
Source, temporary and final storage simultaneously fit O(U⁷) bits.
Replacing every indexed operation by a sequential scan of that storage,
and allowing O(U²) more for names, counters, annotations and writes,
costs O(U⁶ U⁷ U²)=O(U¹⁵), within O(U¹⁶) including parsing/framing.
This is an all-size bit-algorithm bound, not a measured runtime.

With S=O(T) and E_ABP=O(U⁷), L037 receives exact bases/signs, every
local H identity, d,h≥1 and complete explicit framing. Its parameter
N=2+T+S+E_ABP is O(U⁷), giving O(U⁵⁶ log U) certificate bits and
O(U⁵⁶) complete degree by its existing theorem. The polynomial-time
constructions compose. No stronger formula-length-only estimate follows.

The audit finds no substantive defect or required theorem/bound repair.
No new mathematical script, finite certificate or proof strings were
needed or verified. Direct mathematical inputs remain unchanged.
Attempts 019–020 remain valid stops for their different promises.
Arbitrary ER data, formula-only bounds, W/V/U, every-certificate hardness
and unrestricted SAT transfer remain unresolved.

## Mathlib

Coverage: **not checked** for the full operand-restricted construction,
its free-algebra witnesses or full encoding/time bound. No matching
Mathlib theorem or absence claim is asserted. The inspected primary
supporting references and their exact component scope are stated above;
the prior assessment supplies no full theorem matching this package.

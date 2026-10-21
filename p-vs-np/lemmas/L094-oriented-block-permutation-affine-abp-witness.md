# L094 — Original-product witnesses for independently oriented blocks

## Hypotheses

Use L087's free associative F₂ algebra and two explicitly supplied dense
deterministic OBDDs D,E of nonterminal width at most three, on the same
complete named alphabet of q≥2 variables. Their full orders are strictly
different. Let f,g be their exact ordered representatives, with original
edge labels 1+x and x and Boolean terminal scalars. Retain redundant
tests, parallel occurrences, duplicate successors, unreachable states
and all original terminal records. Assume f(a)g(a)=0 on every Boolean
assignment a. This is a promise, not an algorithmic test.

Supply nonempty ordered lists A₁,…,A_b partitioning the alphabet, such
that D's order is A₁···A_b. Supply a permutation π and an orientation
bit for each block, such that E's order is the concatenation, in order
π, of either A_j or its reversed list. Thus every block is contiguous
in both input orders. Require

    1 ≤ b ≤ floor(log₂ M).

Here M is exactly L087's 2 plus the full binary length of the original
diagrams, orders, original-name dictionary, complete Boolean/commutator
list B and its placeholder dictionary, including axiom words and framing.
It excludes all witnesses and degrees. In particular B contains
x_i²+x_i and x_i x_j+x_j x_i for the original named alphabet, with
placeholders σ_i and τ_ij. No new alphabet is introduced.

The supplied annotation uses boundary positions in D, the permutation
of block indices and b orientation bits, in ordinary explicit binary
encoding. It has O(q log(q+2)) bits; alternatively listing the blocks by
indices into the input order has the same bound. It does not redefine M
or its cutoff. No uncharged padded or implicit annotation is an input.
The constructor verifies this syntactic partition/order promise.

## Conclusion

There is a deterministic construction of an explicit acyclic affine-F₂
ABP H in original variables and the original B placeholders satisfying
the formal identities

    H(x,0)=0,                       H(x,B(x))=original fg.

For absolute encoding-dependent constants K,K', the full output and
retained intermediates have at most

    K 9^b (M+b+2)^12 ≤ K'(M+2)^16

bits, and construction takes at most K'(M+2)^48 bit operations. Every
accepting path contains exactly one placeholder edge and has at most
2q−1 nonconstant factors before substitution. This includes structural
paths with a zero contribution or contributions that cancel.

This is an informal restricted witness supplier. The separate step-367
critical audit below finds no substantive defect. No implementation,
finite graph verification, partition
finder or certified originality is claimed. Arbitrary-order W₂, general
ER data availability, formula-length-only bounds and unrestricted SAT
decision/separation remain unresolved. It is not a main-problem candidate.

## Proof

**Ready coverage and imports.** The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-20-oriented-block-permutation-witness.md`.
Use L092's boundary factorization and additive stable sorting, L093
parts 1–2 for its nonzero reversal correction, L085's weighted paired
recurrence and first-exit graph, L035's original-only commutator graph,
L026's increasing-multilinear injectivity, and L087's B/M convention.
These components have their separate informal audits. Neither whole
zero-product theorem L092/L093 is applied to a block. No ER/fidelity
hypothesis from L085's whole theorem is needed for its explicitly
stated two-operand recurrence.

The primary supporting sources already inspected in that assessment are
Li–Tzameret–Wang, *Characterizing Propositional Proofs as Non-Commutative
Formulas*, arXiv:1412.8746v4 (11 September 2015), Lemmas 3.6–3.7,
printed pp.17–18 ([primary PDF](https://arxiv.org/pdf/1412.8746v4)),
and Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non
Commutative Models*, 16-page author manuscript, Definition 1 p.4 and
Lemma 2 Step 1 p.5
([primary PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)).
The former covers formula commutator witnesses over F₂, where minus
equals plus; L035 supplies the graph-input result without formula
unfolding. The latter supplies disjoint serial/parallel graph operations
in its intermediate constant/linear-edge model. Its homogeneous
normalization and zero-free-term hypothesis are not used. No matching
full oriented-block theorem was found in the assessment. The new work
is the nonzero component reception and combined original-input ledger,
not a reproof of either source theorem or a novelty certification.

**Boundary factors and original-factor sorting.** Write t_j=|A_j|.
Choose independently a state at each of D's b−1 block boundaries and
at each of E's b−1 block boundaries. Call these tuples α,β. Each cut
is at a nonterminal level of width at most three, so the number N of
tuple pairs is at most 9^(b−1). For b=1 each tuple is empty and N=1.
Unreachable cut states are included.

For each α, let d_j be D's block diagram with root the selected incoming
state (D's root in its first block). Give its final states scalar 1 at
the selected outgoing cut state and 0 elsewhere; in D's last block use
the original terminal scalars. Define e_j from E and β in E's traversal
order in precisely this fashion. Its internal order may be reversed.
Assign cut indicators before merging equal scalar terminals. Preserve
every edge occurrence, redirecting last edges to the corresponding
0/1 terminal; keep the original input records separately. Working
block diagrams then have O(t_j+1) records. This normalization preserves
each last recurrence and every preceding ordered polynomial, including
unreachable roots, zero values and cancellations.

L092's boundary proof uses only contiguity, not agreement of internal
orders: original paths have unique boundary states and matching block
subpaths concatenate in original traversal order. Consequently here
it gives, as free-algebra identities,

    f=Σ_α d₁···d_b,             g=Σ_β e_{π(1)}···e_{π(b)}.   (1)

Scalar cut indicators enforce the specified intermediate state; each
queried edge belongs to exactly one block. This proof partitions paths;
the constructor enumerates boundary tuples, never paths. All factors
are original-only affine graphs, made ordinary designated-output ABPs
by fresh scalar terminal edges.

Fix α,β and abbreviate its product term by

    V=d₁···d_b e_{π(1)}···e_{π(b)}.

Use L092's stable adjacent sorting by block index on this list of 2b
original factors. It has fewer than 2b² exchanges and ends at
d₁e₁···d_b e_b, preserving d_j before e_j. At an exchange L a c R
to L c a R, L035 applied to the two original-only factors supplies
T(0)=0 and T(B)=ac+ca. Independent serial copies form L T R.
Summing these branches gives

    K_sort(0)=0,       K_sort(B)=V+d₁e₁···d_b e_b.          (2)

This import requires no common internal order: L035 accepts arbitrary
original-only affine DAGs. All commutator placeholders are mapped to
their original B positions. The algorithm changes only the list of
original factors; no accumulated correction is ever a commutator input.

**Receiving nonzero oriented blocks.** Fix j and write t=t_j. If E
preserves the internal order, let v_j=e_j with its own weighted layered
graph and let J_j be a distinct-endpoint zero graph. If it reverses
the internal order, use L093 parts 1–2 on this normalized block diagram:
v_j=rev(e_j), with an explicit weighted layered graph in A_j's order,
and a correction J_j such that

    J_j(0)=0,                         J_j(B)=e_j+v_j.       (3)

Here rev reverses words and fixes scalars. The imported construction
reverses the original edges and attaches a scalar source edge to every
old terminal. For layered reception it absorbs that scalar into the
first reversed edge: a new root has one edge s_t l_e to the old tail
of each last edge e ending at scalar terminal t. All reversed original
edges are retained; old terminals are unreachable at the new first
level. At the new final level only the old designated root has scalar
1. All other old first-level states have scalar 0. Thus its designated
paths reverse exactly the original root-to-terminal paths contributing
to e_j. The graph is weighted, not necessarily deterministic. All
labels remain affine in the variable assigned to their new level.

For clarity about the component's scope, at an old edge e:u→w its
local correction is L035(l_e,rev(e_w)), containing only original-only
operands. The first-exit recurrence is
J_u=Σ_e(l_e J_w+C_e), with zero terminal J. L093 proves (3) by
backward induction before using any zero-product hypothesis. Its
terminal proof uses only that a scalar is fixed by rev. Indicator
scalars and arbitrary chosen incoming boundary roots therefore meet
the same hypotheses. No blockwise Boolean vanishing is assumed.

Although L093's whole statement has q≥2, these parts also receive
t=1 explicitly: every child is a scalar, e_j is affine in one letter,
and rev(e_j)=e_j. Set J_j=0. The normalized reversed graph then has
one layer of edges from the fresh root to old first-level states,
with scalar 1 at the selected root and 0 elsewhere. Its path sum is
exactly the original selected-root affine polynomial. This verifies
the singleton extension of the component, without invoking the whole
theorem outside its range. Either orientation flag is valid on a
singleton. Scalar zero endpoints are retained, not divided out.

The two graphs d_j,v_j are now explicitly layered in the same internal
order, with scalar terminals and labels a+b x_k at each level. They
meet exactly L085's paired-component hypotheses, including weighted
parallel edges, dead states and cancellation. That component supplies
an original-only increasing-multilinear residual P_j and a witness W_j
with

    W_j(0)=0,                         W_j(B)=d_j v_j+P_j.   (4)

P_j evaluates to d_j(a)v_j(a) on every Boolean assignment. Its paired
transition for labels a+b x and c+d x is
ac+(ad+bc+bd)x; its terminal scalar is the product of the two input
terminal scalars. W_j has those paired transitions but nonaccepting
terminal pair states, and exits once into the local K or Boolean
correction of L085 (4). All K inputs are original-only suffixes of
d_j paired with a single original variable. This receives the
unchanged original B dictionary and needs neither ER data nor a
zero residual. Use the scalar-terminal zero shortcut only at actual
terminals, retaining the marked-edge graph for cancelling suffixes.
Omit local exit blocks whose scalar coefficient is zero, as permitted
by L085. Original and paired zero-labeled edges may still be retained;
each actual correction exit has its explicit K or σ placeholder edge.

Define by independent graph sums and products

    U_j=W_j+d_j J_j.

Equations (3)–(4), with the displayed multiplication order, give

    U_j(0)=0,                         U_j(B)=d_j e_j+P_j.   (5)

The two d_j v_j terms cancel adjacently in the sum; there is no
commutation of J_j through any factor. For a singleton, writing the
resulting scalar-coefficient polynomials as d_j=a+b x and e_j=c+d x
gives P_j=ac+(ad+bc+bd)x and U_j(B)=bd(x²+x). Thus the residual
may be nonzero, including when both inputs are 1; the interface still
holds. This calculation checks precisely the endpoint/singleton
reception, rather than imposing a hidden zero-product condition.

**Global additive reduction and vanishing.** For this tuple pair take
the sum K_reduce of independently copied branches

    (P₁···P_{j−1}) U_j (d_{j+1}e_{j+1}···d_b e_b),
    for j=1,…,b.                                         (6)

Empty contexts are scalar-one graphs. Consecutive stages replacing
d_j e_j by P_j from left to right cancel additively under (5), giving
K_reduce(0)=0 and
K_reduce(B)=d₁e₁···d_b e_b+P₁···P_b. Together with (1)–(2), the
disjoint sum H of all K_sort+K_reduce over α,β has

    H(0)=0,            H(B)=fg+R,
    R=Σ_(α,β) P₁···P_b.                                  (7)

Each P_j uses only increasing multilinear words in A_j. The blocks
are disjoint and every summand puts them in D's order, so the entire
R is increasing multilinear in that single full order. On scalar
assignments reversal preserves evaluation, hence v_j(a)=e_j(a).
Equation (4) then makes each summand evaluate to the scalar product
of its d/e factors. Scalars commute, so (1) gives R(a)=f(a)g(a)=0.
L026's injectivity in this established ordered-multilinear subspace
implies R=0 formally, proving the original-fg identity. No individual
summand or block is claimed zero. Without the Boolean-zero promise
the same constructor gives exactly (7), with a possibly nonzero R.

All graph sums/products above use fresh disjoint copies and forward
unit connectors, with fresh sum source and sink. A zero graph has
distinct endpoints and no path. There are no cross-copy edges except
the displayed connectors. Leaving a component's designated exit
internally cannot later return to its exit in an acyclic graph. Thus
even nonextremal designated endpoints yield exactly the stated ordered
products. The first-exit regions inside J_j,W_j likewise have no
return edges. The assembled graph is acyclic with no extra empty path.

**Independent copies in original M.** Put m=M+b+2. Then b≤q≤M and
m≤2(M+2). Original names have at most M bits, and the complete B/name
package costs at most M. The annotation costs O(m²) bits; order and
partition checks use only bounded scans/comparisons of those records.
Original input records, including isolated terminal records, are kept
once. Scalar normalization scans them and retains only two scalar
types per working block, preserving every transition occurrence.

For one tuple pair the 2b original block graphs have O(q+b)=O(m)
records in total. Each reversal normalization has O(m) records and
at most two entries per affine label. A complete reversed suffix copy
also has O(m) records. The L093 component counts O(m) C_e blocks,
each with O(m) marked choices and O(m) records per choice: J_j has
O(m³) records. This includes independently copied reversed graphs;
it is not a recurrence unfolded over paths.

For a fixed j the L085 paired region has O(m²) states and outgoing
edge-pair occurrences. Each local K copy has O(m²) records, and its
other original-only suffix factors have O(m) records. Thus W_j has
O(m⁴) records, P_j has O(m²), and U_j has O(m⁴). Keeping every
separately constructed reversed suffix, C_e, K, J, W, U and P, as
well as the copies incorporated in these outputs, stays within these
orders per j: each such object is generated in one of the counted
loops, with no recursive copying of previously assembled witnesses.

There are b reduction branches. In each, the earlier P factors have
at most O(b m²)=O(m³) records and the later original factors have
O(m). Thus all reduction contexts and local outputs cost O(m⁵)
records per tuple, or O(m⁶) bits before global renumbering, even
repeating the full original dictionary with each primitive graph copy.
Indeed the number of primitive copies is no larger than a constant
times the charged record count. This explicitly pays the larger
weighted P contexts rather than retaining L092's width-nine shortcut.

Each sorting call has original-only inputs of O(m) records and full
length O(m²), including the original complete dictionaries. L035's
O(E⁴) full bound gives O(m⁸) bits per call; there are fewer than
2b² calls. All contexts, temporary factor lists and separately retained
outputs fit O(m^10) bits per tuple. Repeating B with its four primitive
copies per marked edge pair is also covered: there are O(m³) such
records per call and O(M) dictionary bits per copy, below O(m⁸).
No sorting call receives an earlier witness or weighted residual P.

Before global renumbering, the aggregate bound is C N m^10. Dense
global references have O(log(N m^10+2))=O(b+log(m+2)) bits. Paying an
additional factor m against all prior bits, and another for framing,
connectors, association lists and retained metadata, gives

    S=K 9^b m^12.                                         (8)

This count includes an optional explicit serial/parallel graph for R,
which uses O(N b m²) records. No semantic-zero test or representation
of R by its monomial expansion is needed. The original cutoff gives
9^b≤M^(log₂9)≤(M+2)^4, so (8) is at most K'(M+2)^16.
No witness-dependent quantity has entered M or the cutoff.

For time, enumerate boundary tuples, sort at most 2b factors per tuple,
and generate graphs by scans, finite edge/pair loops and record copying.
One sorting call enumerates O(m²) edge pairs and O(m) copied records
per pair, with constant-size central label lists. Reversal and paired
components use the explicitly counted O(m³) and O(m⁴) record loops.
Across the at most O(b²) calls and b block/reduction operations, even
O(m²) extra scan/bookkeeping operations per copied record are within
O(m⁸) operations per tuple. Parsing and checking the annotation and
initial terminal tables are smaller. The total number of these
operations is O(N m⁸), hence O(S). On buffers bounded by S bits,
ordinary list scans, copying, identifier comparisons and binary counter
arithmetic cost at most O(S²) per operation. Consequently time is
O(S³)≤K'(M+2)^48, with absolute constants. This deliberately loose
bound uses no path/assignment/monomial enumeration, PIT oracle or
unit-cost operation on an unbounded identifier.

**All-path degree and edge cases.** Each original block path has at
most t_j nonconstant factors, as does its normalized reversal and P_j.
L093's J_j path has at most t_j−1: its original recurrence prefix
exits into a single-edge/suffix commutator, where two marked variable
labels are replaced by one placeholder. At t_j=1 J_j has no path.
L085's W_j has path degree at most 2t_j−1. Thus U_j has the same
bound, including its d_j J_j branch, and every accepting U_j path
has exactly one placeholder.

For a sorting exchange, L035 replaces two marked original variable
edges by one placeholder and keeps their four subpaths. Those
subpaths concatenate through each marked edge to actual input paths,
since an overlap would create a cycle. Adding the other original
factor occurrences therefore gives degree at most 2q−1. For a
branch (6) the degree is at most

    Σ_(i<j)t_i+(2t_j−1)+Σ_(i>j)2t_i ≤ 2q−1.

All exterior factors are original-only and each correction path has
exactly one placeholder. Unit/scalar connectors add no degree; retained
original/paired zero labels cannot increase these counts. The
argument concerns every structural accepting path before cancellation.
It covers unreachable cuts, duplicated successors, absent accepting
paths, zero scalar endpoints and semantically constant nonterminals
without replacing those nonterminals by scalars. The b=1 empty-tuple
case is included; distinct full orders then require actual reversal
of the non-singleton full list. No empty block is admitted.

The continuation threshold is met informally: both identities retain
original fg, all costs are polynomial in unchanged M, and no forbidden
blockwise-zero premise or witness-valued commutator input is used.
Attempts 018/030 remain unchanged: this construction assumes the two
diagrams and the order annotation, and supplies no universal faithful
common-order value representation or SAT consequence. The new assembly,
singleton specialization and full ledger are checked separately below.

**Separate critical audit — step 367, 2026-10-20.** The unchanged
pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-20-oriented-block-witness-critical-audit.md`.
This verifies the existing informal result, not a stronger theorem,
implementation or certified originality. The primary component citations
and their qualifications above are reused. Full matching Mathlib coverage
remains not checked. Neither whole zero-product theorem is applied to
a block, and formula-input size bounds are not asserted for graphs.

At every internal cut both diagrams are at a nonterminal level, with at
most three states. Internal orientation does not affect this count.
The two independent boundary tuples therefore have at most 9^(b−1)
choices together. Assigning indicator terminals before merging scalar
types preserves the last recurrence at each state and inductively every
earlier polynomial, including an unreachable selected root. Matching
block subpaths concatenate to exactly one original path with exactly
one tuple. Wrong-boundary paths retained structurally have scalar zero.
Finite distributivity proves (1), with each query edge in exactly one
factor, without any path enumeration by the constructor. Last-block
normalization uses the original terminal bits. Only working terminals
are merged; all original terminal records remain paid in M. Each
working block has O(t_j+1) records because its nonterminal width is
bounded and its terminal scalar types number at most two.

Stable sorting never exchanges equal block keys, so d_j remains before
e_j. At every exchange both L035 operands are the original-only block
graphs. Its four-copy marked-edge formula substitutes to ac+ca with
the indicated external L,R still in their original product order.
The sum of exchange branches cancels each interior list product twice,
proving both parts of (2). Neither an accumulated correction nor P is
passed to L035. Empty contexts and zero/no-path factors satisfy these
same identities. Pair placeholders are mapped by original names, not
by either traversal order.

For reversal, fix the selected incoming root first. A reversed path to
that old vertex corresponds to exactly one original path starting there.
Leaving the selected output internally cannot lead back to it in a DAG.
Each new first edge is indexed by an original last-edge occurrence
and includes its terminal scalar exactly once. Old terminals are
unreachable from the new root. The final scalar is 1 only at the old
selected root and 0 at the other old first-level states. Extra paths
to those zero endpoints may exist but contribute zero. Hence v_j
computes rev(e_j) formally, preserving parallel and cancelling paths.
For t=1 the new edges go directly to old first-level states, and the
final scalar selects exactly the selected root's original outgoing
occurrences. Every word then has length at most one, so rev(e_j)=e_j
and the distinct-endpoint zero J_j is valid. This receives both flags
and every scalar endpoint without dividing by a scalar.

For a nonsingleton block, check L093's first-exit recurrence before any
vanishing premise. At an edge with label l and child suffix e_w,
the substituted summands are l(e_w+rev(e_w)) and
l rev(e_w)+rev(e_w)l. Their sum is l e_w+rev(e_w)l.
Summing proves e_u+rev(e_u); scalar terminals start the induction
because a scalar plus its reversal is zero. Every local commutator
receives only l and the original-only reversed suffix graph. A path
follows original recurrence edges and exits once into that correction,
with no return. This proves (3) at arbitrary selected roots without
a blockwise zero assumption or witness-valued commutator operand.

The normalized d_j,v_j meet L085's displayed paired-component scope:
one common variable order, affine scalar-coefficient edge labels,
explicit parallel/dead paths and scalar terminals. For one edge pair
write l=a+bx, m=c+dx, h=ac+(ad+bc+bd)x and let F,G be the child
suffix polynomials. With K(B)=Fx+xF, its exact local identity is

    l F m G = h F G + bd(x²+x) F G + d l K(B) G.

Indeed Fm=mF+dK(B) and lm=h+bd(x²+x). These two equalities
justify all factor movements and the displayed order. Paired terminal
P is the product of terminal scalars; paired terminal W is nonaccepting.
The child recurrence gives (4), both at zero placeholders and at B.
Only actual scalar terminals use the path-free K shortcut; cancelling
nonterminal suffixes keep L035's graph. At t=1 both child suffixes
are scalars, leaving precisely the bd σ correction after summing
the edge pairs. Collecting d_j=a+bx, e_j=c+dx gives the written P_j
and bd(x²+x), including constant and zero endpoint cases.

Adding d_j J_j to W_j cancels d_j v_j in the same multiplication
order, proving (5). To check (6), put Q_j=d_j e_j. Its jth substituted
branch is (P₁···P_{j−1})(Q_j+P_j)(Q_{j+1}···Q_b).
Those are two consecutive stages of left-to-right replacement; all
interior stages cancel twice. Each branch separately vanishes at zero
placeholders. Combining this telescope with (1)–(2) gives (7) with
exact original fg. Every P_j has only increasing multilinear words
within A_j, and every product uses D's block order. Thus all of R
lies in that one increasing-multilinear subspace. At Boolean scalars
P_j=d_j v_j=d_j e_j. Scalar commutativity, not a free-ring factor
exchange, identifies R(a) with f(a)g(a). Only at this point does L026
give R=0 formally. No individual block or tuple summand is set to zero.

These identities describe the complete graphs. Serial factors have
disjoint vertices and only forward connectors through their designated
outputs. Leaving an output internally cannot reach its connector again
without a cycle. Local J,W exits enter disjoint correction regions and
then their fresh output, never another correction or the recurrence
region. Zero graphs have distinct endpoints and no path. Hence no
extra empty or cross-branch path is introduced. Optional retained P,R
graphs are separate objects, not accepting branches of H.

For an independent resource check use m=M+b+2 throughout. Original
record counts, names and complete dictionaries are bounded by M;
b≤q≤M and the explicit annotation costs O(q log(q+2))≤O(m²).
Contiguity/orientation checks scan those supplied lists and do not
find a partition. For one tuple normalized original blocks total O(m)
records. A reversed suffix costs O(m). Each C_e has O(m) marked
choices and O(m) records per choice; O(m) original edge occurrences
give O(m³) for J. Independently retained C_e and suffix intermediates
fit the same bound. There are O(m²) state pairs and outgoing edge
pairs in a paired component. Each independent K has O(m²) records;
other suffix factors cost O(m). Thus W,U cost O(m⁴) per block and
P costs O(m²), including all retained local intermediates. Copying an
object into its parent while retaining the original costs a constant
factor at that counted stage, not a recurrence over complete paths.

Each of b reduction branches contains at most b earlier P copies,
costing O(bm²), later original factors costing O(m), and one U of
O(m⁴). The total is O(m⁵) records. Repeating the full M-bit
dictionary with every primitive copy and paying name/label payload
gives O(m⁶) bits before global renumbering. A sorting call has
O(m²) edge pairs and O(m) copied records per pair, with bounded
central-label lists. Its full input length is O(m²), so the weaker
L035 bound O(E⁴) pays O(m⁸) bits per call. Fewer than 2b² calls
plus contexts give O(m¹⁰) per tuple. Separately retained outputs
and contextual copies change only the constant. Per-call primitive
dictionary copying costs at most O(m⁴), already within that bound.

All tuple pairs therefore cost O(Nm¹⁰) bits before global references,
where N≤9^(b−1). A global identifier needs
O(b+log(m+2))≤O(m) bits. The two additional m factors in (8)
pay this and full framing/metadata, including an optional separate R
graph with O(Nbm²) records. Thus S≤K9^b m¹². Applying
m≤2(M+2) and 9^b≤M^(log₂9)≤(M+2)^4 gives the stated fixed
K'(M+2)^16 bound, without inserting any witness data into M.

For time, sorting generates O(m³) graph records per call, hence
O(m⁵) per tuple over its O(b²) calls. Block outputs and reduction
copies also total O(m⁵) records. Paying O(m) dictionary payload
per primitive copy and O(m²) additional scan/bookkeeping iterations
still gives O(m⁸) iterations per tuple. Boundary enumeration, terminal
scans and annotation checks are smaller. There are consequently
O(Nm⁸)≤O(S) iterations. Buffers have at most S bits; O(S²) bit
operations per iteration covers repeated scans, comparisons, copying,
renumbering and binary counters. This yields O(S³)≤K'(M+2)^48,
without semantic testing or path/assignment/monomial enumeration.

Finally consider structural accepting paths, including zero-contribution
and cancelling paths. In a C_e with s remaining block levels, two
marked variable edges are replaced by one placeholder, giving degree
at most s−1. Its original recurrence prefix then gives at most
t_j−1 in J_j; at a scalar suffix there is no such path. In W an
exit at s remaining levels has degree at most
1+(s−1)+(s−1)=2s−1, through either K or σ. The preceding pair
prefix contributes at most one factor per earlier level, so W has
degree at most 2t_j−1. The d_j J_j branch has at most
t_j+(t_j−1) factors. All such accepting paths use exactly one
placeholder. Omitted scalar-zero exits cause no exception; retained
zero-labeled transitions satisfy the same level bounds.

In a sorting branch, L035's four subpaths concatenate through each
marked edge to an actual path in its original block DAG; an overlap
would form a cycle. Replacing the two marked variable edges by one
placeholder and adding all exterior original factors gives at most
2q−1 factors. A reduction path has at most
Σ_(i<j)t_i+(2t_j−1)+Σ_(i>j)2t_i≤2q−1. Exterior factors
are original-only; scalar/unit connectors contribute neither degree
nor placeholders. Wrong-boundary zero paths, duplicate successors,
cancelling paths and inaccessible selected roots obey these same
counts. For b=1 the empty tuples are valid and distinct full orders
force actual reversal of the non-singleton list. No empty block is used.

Verdict: no substantive defect found in the nonzero reception, both
identities, original dictionaries/cutoff, retained-copy ledger, bit time
or all-path degree bound. No mathematical repair, additional dependency,
new lemma or finite graph test is required. This audit verifies the
conditional informal supplier only; annotation availability for arbitrary
pairs, arbitrary-order W₂, general ER data and unrestricted SAT remain
open. Attempts 018/030 and unfinished work retain their original scope.

## Mathlib

Full matching coverage for the oriented-block witness and its explicit
bit/time/path-degree bounds is **not checked**, not asserted absent.
The cited primary sources cover formula commutators and graph composition;
the named local results supply the nonzero graph components. This is
local progress beyond the full-statement coverage found in the ready
assessment, without certified originality or a P-versus-NP resolution.

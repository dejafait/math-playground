# L092 — A witness for logarithmically many permuted variable blocks

## Hypotheses

Use L087's free associative F₂ algebra, two supplied explicit dense
deterministic width-at-most-three OBDDs D,E on the same complete named
alphabet, their ordered representatives f,g, and original complete
Boolean/commutator axiom list B with its placeholder dictionary. Width
bounds nonterminal levels. Retain redundant tests, repeated successors,
unreachable states and all scalar terminal records. Only the last level
has terminals. Assume fg(ε)=0 on every Boolean assignment ε; this is a
promise, not a supplied semantic test.

Supply disjoint nonempty variable lists A₁,…,A_b partitioning the
alphabet. D's order is A₁···A_b, and E's order is
A_{π(1)}···A_{π(b)} for a nonidentity permutation π. Each block retains
exactly the same internal variable order. Put t_j=|A_j| and q=Σ_j t_j.
There is no bound on an individual block length. Suppose

    2 ≤ b ≤ floor(log₂ M).

Here M is precisely L087's 2 plus the full binary length of the original
two diagrams, both orders, original-name dictionary and complete
B/placeholder dictionaries, including axiom words and framing. It
excludes witnesses and degree parameters. The supplied block boundaries
and permutation can be recorded by O(q) indices into the already supplied
orders, each of O(log(q+2)) bits, hence O((M+2)²) additional bits. They
do not redefine M. There are no additional mathematical inputs hidden
in that block description.

## Conclusion

One can deterministically construct an explicit acyclic affine-F₂ ABP H
using only original variables and the original B placeholders, with

    H(y,0)=0,                  H(y,B(y))=original fg

as formal free-algebra identities. For absolute constants K,K', its
complete output and retained intermediate encoding have at most

    K 9^b (M+b+2)^12 ≤ K'(M+2)^16

bits. Construction takes at most K'(M+2)^48 bit operations after
enlarging the absolute constant. Every accepting path has
pre-substitution degree at most 2q+1. Complete original dictionaries
are retained even for a zero output.

This is an informal restricted supplier toward W₂. The separate step-359
critical audit below finds no substantive defect in the identities or
stated bounds. No implementation, finite graph verification,
semantic promise tester, partition finder or certified originality is
claimed. Arbitrary-order W₂, general ER data availability, bounds solely
in CNF length and unrestricted SAT decision/separation remain open.

## Proof

**Coverage and imports.** The prior EXPLORE assessment is
`drafts/literature/2026-10-19-logarithmic-block-permutation-witness.md`.
Use L026 (4) for ordered representatives, (7)–(9) for common-order
product correction and its increasing-multilinear injectivity argument.
Use only L071's post-compilation value/K/P/W graphs realizing those
same polynomials, not its treewidth compiler. L035 supplies original-only
graph commutator witnesses with both formal identities. L087 supplies
the original B and M conventions. L091's audited two-block cutting,
terminal normalization and graph reception are reused below; its
constant-multiplicity polynomial bound is not iterated.

The underlying standard inputs are Bryant, *Graph-Based Algorithms for
Boolean Function Manipulation*, IEEE TC 35(8) (1986), §4.3,
author-restored pp.12–14
([primary PDF](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf)),
for common-order Boolean Apply; Li–Tzameret–Wang, *Characterizing
Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4
(11 September 2015), Lemmas 3.6–3.7, pp.17–18
([primary PDF](https://arxiv.org/pdf/1412.8746v4)), for formula-input
Boolean/commutation witnesses; and Raz–Shpilka, *Deterministic Polynomial
Identity Testing in Non Commutative Models*, author manuscript,
Definition 1/Lemma 2 Step 1, pp.4–5
([primary PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)),
for independently copied serial/parallel graphs. The graph-sized
formal corrections are the indicated canonical local inputs, not an
unpaid unfolding of formula witnesses. The additional argument here is
the simultaneous boundary expansion, additive assembly and uniform
growing-b resource ledger. No inspected source supplies that full target;
this does not certify novelty. No known component theorem is reproved.

**All-boundary expansion.** Let I_k be D's level immediately after
block A_k, for 1≤k<b. Let J_ℓ be E's level immediately after block
A_{π(ℓ)}, for 1≤ℓ<b. These are nonterminal levels, with cardinality
at most three. Enumerate tuples

    α∈I₁×···×I_{b−1},       β∈J₁×···×J_{b−1}.

There are at most

    N=9^{b−1}

pairs of tuples. More precisely the actual count is the product of the
displayed level cardinalities, and is no greater than N. All subsequent
cost estimates use this upper bound. Include unreachable states.

For a fixed α define a dense block diagram for d_j on A_j. Its root
is D's original root if j=1, and α_{j−1} otherwise. It retains all
transitions inside this block. If j<b, its last-level terminals have
value 1 at α_j and 0 at all other states of I_j; if j=b use the
original Boolean terminal values. Thus d_j is a polynomial depending
on α, whose notation suppresses that dependence. Define e_{π(ℓ)}
from E and β in exactly the same way, in E's traversal order.

At each internal cut assign the indicator bits before merging equal
scalar terminals. Merge original terminals by their actual bit for a
last-block factor. This is L091's terminal normalization: it preserves
each last-level recurrence and hence every earlier free polynomial.
It gives each working block diagram O(t_j+1) states/edges, even if
the original input contains many isolated terminal records. All original
records remain retained as input data. A factor may start at an
unreachable state or have no accepting path. It still has a complete
width-three block diagram, with a designated root and scalar terminals.

Every original root-to-terminal path has a unique state at every cut.
Conversely block subpaths with fixed matching boundary states concatenate
uniquely to such a path. Within each original DAG this concatenation
advances strictly through the levels. Finite distributivity, preserving
the original label order, therefore gives

    f=Σ_α d₁···d_b,
    g=Σ_β e_{π(1)}···e_{π(b)}.                         (1)

This partitions paths only in the proof; the algorithm enumerates
boundary states, never complete paths or internal assignments. In
particular each label on the last test before a cut belongs to the
preceding block, and each label on the first test after it belongs to
the next block, with none lost or duplicated. Constant label terms and
all parallel edges are retained. Scalar terminal values occur only at
the ends indicated above. The indicator terminal values on intermediate
factors introduce no additional variables.

Fix a pair (α,β). Its term in the product expansion is

    V=d₁···d_b e_{π(1)}···e_{π(b)}.                     (2)

Every factor in (2) is original-only, represented by L071's affine
value graph on its own block. None contains a placeholder.

**Additive sorting, with no recursive witness inputs.** Regard (2) as
a list of 2b labeled factors; a factor from block j has key j. Stable
adjacent inversion sorting gives a sequence of lists, starting with
(2) and ending with

    d₁e₁ d₂e₂ ··· d_b e_b.                             (3)

Stability puts d_j before e_j: they appeared in that order in (2), and
equal keys are never exchanged. Each exchange reduces the inversion
count by one, so there are at most binomial(2b,2)<2b² exchanges. This
algorithm and count depend on block keys alone, not on graph functions
or intermediate OBDD width.

At an exchange write the current product as L a c R and the next as
L c a R. Here a,c are the two current original-only block factor
graphs, and L,R are serial products of the other original-only block
factors in their current order. Apply L035 to independent copies of
a,c to obtain T with

    T(y,0)=0,            T(y,B)=ac+ca.

Rename its pair placeholders into their positions in the complete B
dictionary. Reversing an original identifier order does not change the
commutator polynomial in characteristic two. Make the branch L T R
using independent copies of every context factor and T. It vanishes
at zero placeholders and substitutes to the sum of the two consecutive
products. Empty L or R is the scalar-one graph. Summing all these
branches gives K_sort, with

    K_sort(y,0)=0,
    K_sort(y,B)=V+d₁e₁···d_b e_b.                       (4)

The intermediate products telescope additively in the free algebra.
Only the original factor list is updated after an exchange. No T,
contextual branch or accumulated witness is ever passed as an input to
L035, and no intermediate reordered OBDD is constructed.

**Additive within-block corrections.** For each j, the supplied block
diagrams d_j,e_j have the same internal order and width at most three.
Construct their synchronous product P_j (width at most nine) with the
product of the two scalar terminal values. L026 (7)–(9) and L071's
post-compilation pair graph supply U_j with

    U_j(y,0)=0,          U_j(y,B)=d_j e_j+P_j.           (5)

These recurrences require only the two operand diagrams, not an ER
proof or a separate promised output diagram. Each block Boolean/pair
placeholder is renamed into its original full B position. Thus (5)
is an identity in the full free alphabet, including unused dictionary
entries. P_j is original-only and increasing multilinear on A_j.

For completeness the graph reception used here has O(t_j+1) pair
vertices; a path leaves the pair region once into one of its three
local correction blocks. These consist of the two literal/K/suffix-sum
blocks and the Boolean-placeholder/two-suffix-sums block. K switches
once into its value region; it contains no recursive U copy. With
width three fixed, each local block has O(t_j+1) independently copied
records. Consequently U_j has O((t_j+1)²) records and P_j has
O(t_j+1). This is the audited L091 reception of the existing L026/L071
construction, retaining all factor orders and the zero terminal case.

Form the disjoint parallel sum K_reduce of the b branches

    (P₁···P_{j−1}) U_j (d_{j+1}e_{j+1}···d_b e_b).     (6)

Every occurrence is separately copied. Substitution in the jth branch
is the sum of the two consecutive stages replacing d_j e_j by P_j
from left to right. Cancellation between these stages gives

    K_reduce(y,0)=0,
    K_reduce(y,B)=d₁e₁···d_b e_b+P₁···P_b.              (7)

This identity neither commutes a U_j with another factor nor feeds it
to an original-only constructor. Combining (4) and (7), the graph
K_{α,β}=K_sort+K_reduce satisfies

    K_{α,β}(y,0)=0,
    K_{α,β}(y,B)=V+P₁···P_b.                           (8)

**The residual and the original output.** Let H be the disjoint sum of
all K_{α,β}. Use fresh common entrance/exit vertices and unit connectors
for all sums/products, with no other cross-component edges. In
particular no zero graph gains an empty accepting path. These are
acyclic affine-edge compositions. Equations (1), (2) and (8) give

    H(y,0)=0,             H(y,B)=fg+R,
    R=Σ_(α,β) P₁···P_b.                                (9)

Every P_j word is increasing multilinear in A_j; all blocks are disjoint
and occur in the order A₁···A_b in every residual summand. Thus the
entire R lies in this single increasing-multilinear subspace, including
the empty word. For a Boolean assignment, each P_j evaluates to
d_j e_j by the synchronous product semantics. Scalar multiplication
commutes, so for each tuple pair

    (P₁···P_b)(ε)
      =(d₁···d_b e_{π(1)}···e_{π(b)})(ε).

Summing and using (1) gives R(ε)=f(ε)g(ε)=0. L026's injectivity on
the just-established single ordered-multilinear subspace gives R=0
formally. Equation (9) now proves the required original-fg identities.
No injectivity is claimed for V, fg, a witness, an individual residual
summand, or arbitrary Boolean-zero free polynomials. In fact the
construction can be executed without the zero promise and then gives
the exact identity H(B)=fg+R; the promise is used only to prove R=0.

**Uniform original-input ledger.** Put m=M+b+2. Nonempty blocks imply
b≤q≤M, hence m≤2(M+2), and each original written identifier has at
most M bits. Normalize working terminals as above, using scans of the
original O(M)-bit records and retaining all of them. The block metadata
fits O(m²) bits. For each tuple, all 2b factor graphs together have
O(q+b)=O(m) records; one independent context of current factors or
earlier P factors also has O(m) records. Individual labels have at most
one original symbol and a constant term. Copying original names literally
and the full original dictionaries gives at most O(m²) bits per such
factor/context. No external dictionary or sparse identifier is free.

Each L035 invocation has two original block factor inputs with combined
full length at most c m², including complete original-name and
commutator dictionaries, for an absolute c. Its O(E⁴) full bound is
therefore O(m⁸). There are fewer than 2b² such invocations per tuple,
each used once in a separately copied context. There is no nested
invocation on their outputs. Each U_j has O((t_j+1)²) records, at most
O(m³) bits with literal original names/dictionaries; each P_j and
external context has O(m²) bits. There are b correction branches (6).
Every local K/value factor copy in each U_j has already been charged
in its quadratic record count; even copying full dictionaries at each
local block adds at most O(m²) bits per U_j. All temporary factor,
P,U,T copies and the O(b²) intermediate factor lists may be retained.

Thus before final global renumbering the full aggregate encoding is
at most C N m^10 bits. There are O(N(b²+b)) branch occurrences, not
M^{Theta(b)} branches. Dense global names and endpoint references need
O(log(N m^10+2))=O(b+log(m+2)) bits. Paying an additional factor m
against every prior bit and charging all sum/product connectors, root
references, full output dictionaries and framing gives at most

    S=C' 9^b m^12                                           (10)

bits for the complete output plus retained intermediate data. The
unused extra power absorbs small inputs, headers and counters. This
also permits every independently exported component to repeat the full
original B dictionary. The only exponential here is in b, never a
block length, and no completed polynomial bound is iterated b times.

Here is an explicit operation bound, so time is not inferred from
output size alone. Resolve original references by scans of the input;
create all factors by loops through levels/states, with scalar-terminal
redirect tables; enumerate the finite cut-state tuples lexicographically.
Stable sorting needs O(b²) swaps and at most O(b²) list comparisons
per tuple by an ordinary insertion/bubble implementation. Each T call
enumerates O(m²) edge pairs and copies four O(m)-record value graphs
per pair. Its input edges have at most one original-symbol term, so
each central placeholder list has at most one entry; constant-only
edges give none. Even allowing O(m) table scans per copied record and
further O(m²) slack for temporary bookkeeping is at most O(m⁶)
record/table operations per T. Across O(b²) calls this is O(m⁸)
per tuple. Constructing each U_j directly from O(t_j) pair states
and O(t_j)-record local blocks, with the same scan allowance, and
copying all exterior contexts, product graphs and factor-list snapshots
are also within O(m⁸) per tuple. Initial scans and block verification
fit this bound. Completed T/U branches are copied with consecutive
dense identifiers and additive offsets, with counters charged as bit
work. There are no path, monomial or assignment enumeration loops.

The total number of these record/table operations is at most C N m⁸,
which is O(S). On explicit lists of total length bounded by (10), each
such operation can conservatively be performed in O(S²) bit steps:
scans, string comparisons/copies and elementary binary counter operations
suffice, even without fast lookup. This yields O(S³) bit time and does
not assume a RAM operation on an unbounded integer or a semantic oracle.
Finally, at the original cutoff

    9^b ≤ M^{log₂9} ≤ (M+2)^4,
    S ≤ C''(M+2)^16,            S³ ≤ C'''(M+2)^48.          (11)

The constants in these inequalities are absolute. M was fixed before
any witness or degree data and was never enlarged to absorb the output.

**Path degree and edge cases.** A d_j/e_j path has degree at most t_j;
a P_j path has degree at most t_j. In a nonempty L035 central branch,
the two marked variable-bearing input edges are omitted from their
prefix/suffix paths and replaced by one placeholder edge. L035's DAG
factorization ensures the prefix and suffix in each input concatenate
through its marked edge to an actual block path; an overlap would
make a cycle. Thus the T path degree is at most t_a+t_c−1. The exterior
current factors use each of the other original block occurrences once,
giving complete sorting-branch degree at most 2q−1. Constant-only
marked labels have no central edge and no accepting path. Retained
dead internal records do not change this accepting-path argument.

L071's U_j paths have degree at most 2t_j−1, including all pair-region
prefixes before a local correction. In (6) an earlier P uses at most
t_i and a later pair at most 2t_i. Consequently a reducing branch has
degree at most

    Σ_(i<j)t_i +(2t_j−1)+Σ_(i>j)2t_i ≤ 2q−1.

Unit connectors and scalar-one empty contexts have degree zero. The
claimed 2q+1 bound is therefore conservative before substitution or
cancellation. Fresh endpoints give a zero graph no accidental empty
path. A path leaving a designated internal exit cannot return to it
and use its connector in an acyclic component, so unused outgoing
edges introduce no extra completed paths.

Singleton or arbitrarily long blocks, arbitrary π, redundant tests,
unreachable boundary tuples, repeated successors, scalar constants and
zero/no-path factors all satisfy the same construction. No nonterminal
is replaced by a scalar merely because its Boolean function is constant;
only actual scalar terminals are merged. Equal-successor literal edges
remain separate. The nonidentity permutation and nonempty blocks ensure
strictly distinct complete orders. Attempts 018/030 remain independent:
this is neither repeated coverage approval nor universal availability
of small faithful common-order value graphs. L088–L090 are scope
comparisons, not mathematical inputs. This supplies a restricted
informal witness construction, not W₂ for arbitrary orders or a
resolution of P versus NP. Its full all-size argument is checked in the
separate audit below; no computational check is claimed.

**Separate critical audit — step 359, 2026-10-20.** The pre-invocation
EXPLORE assessment is
`drafts/literature/2026-10-20-logarithmic-block-permutation-critical-audit.md`.
This is RESEARCH / proof_audit / REPRODUCTION of the existing construction.
The essential inputs are L026 (4), (7)–(12) and ordered injectivity,
L035's four-copy marked-edge construction and actual loops, L071's
post-compilation value/K/P/W graphs and path analysis, L087's original
B/M, and L091's terminal normalization and same-block reception.
Their precise primary supporting citations and limitations are given
above and in the unchanged assessment. No further theorem, treewidth
compiler, semantic tester or computational certificate is used.

At every internal boundary all paths are at the first level of the next
block, so that level is nonterminal and has at most three states. The
preceding test's labels belong to the preceding factor; the next test's
labels belong to the next factor. For a fixed tuple, the indicator
terminal kills precisely the subpaths ending at a different boundary
state. Concatenating the remaining subpaths reconstructs one original
path and one tuple, and conversely every original path has that tuple.
Terminal-one paths contribute their ordered label products and
terminal-zero paths contribute zero. This proves each equality in (1)
by finite distributivity, including affine constant terms, repeated
successors and parallel edges. No path count is used as an algorithmic
cost. The two boundary choices are independent: their combined count
is the product of 2b−2 level cardinalities, at most 9^(b−1), not merely
the number of tuples for one diagram.

The indicator assignment precedes terminal merging on every truncated
factor. Merging by bit then preserves each last-test recurrence and,
inductively, its root polynomial. On a last block, the original terminal
bits give that same statement. Thus arbitrary isolated terminal records
are paid once in the original input, while every working factor has
O(t_j+1) records. Unreachable chosen states can have nonzero suffixes;
the proof retains them and their incoming indicator factors. It does
not assume their suffixes vanish. Singleton blocks still have one test
between their designated boundary endpoints, and no boundary can move
a test into both adjacent factors.

For a tuple pair let V_r denote the ordered product after r stable
inversion exchanges. Equal-key factors are never exchanged, so the
final product is precisely d₁e₁···d_b e_b, with d_j before e_j.
There are at most binomial(2b,2) exchanges. In an exchange L a c R,
L035's F-prefix, G-prefix, central placeholder, G-suffix, F-suffix order
substitutes to ac+ca when F=a and G=c. Consequently the contextual
branch substitutes to V_r+V_(r+1), without commuting either context.
Summing cancels every interior V_r twice and proves (4). Both inputs
to every invocation are unchanged original-variable factors; earlier
witnesses are only summed, never used as commutator inputs. Every
branch vanishes at zero placeholders separately. Empty contexts are
unit graphs and do not alter these identities.

Within block j, both diagrams have the identical t_j-variable order.
The synchronous P graph has at most nine states per nonterminal level
and scalar terminal products. Its correction graph has O(t_j+1) pair
vertices. At a pair vertex its three exits implement exactly the two
literal/K/suffix-sum terms and the Boolean/two-suffix-sums term of
L026 (8); pair edges implement the two recursive left multipliers.
Each exit uses independent O(t_j+1)-record local factors. K switches
once to its value region and never invokes U. No local block returns
to the pair region. Thus the graph has O((t_j+1)²) records and computes
the exact recurrence, including zero W at every terminal pair. This
receives (5) without any ER output diagram, extension fidelity premise
or treewidth hypothesis. Renaming into original B preserves every
identity; a reversed pair name has the same substituted commutator in
characteristic two, and unused dictionary entries are retained.

Write Q_j=P₁···P_j d_(j+1)e_(j+1)···d_b e_b, including j=0,b.
The jth branch of (6) substitutes to Q_(j−1)+Q_j in precisely that
order. Hence (7) holds, and adding (4) gives (8). Summing over all
tuple pairs yields (9) with the original fg. At zero placeholders
each U branch and each sorting branch is zero independently of the
Boolean-zero promise. All products and sums use disjoint copies and
fresh distinct sum endpoints, so these polynomial operations introduce
neither a cross-branch path nor an accidental empty accepting path.

Each P_j uses only increasing multilinear words in A_j. Disjoint
alphabets and the fixed block order put every summand of R in the
same increasing-multilinear space A₁···A_b. On a Boolean assignment,
P_j evaluates to d_j e_j; scalar commutativity, then (1), gives
R(ε)=f(ε)g(ε). The promised zero and L026's injectivity therefore
give R=0 formally, including its constant coefficient. No individual
summand need vanish. No injectivity is applied to fg, a witness or
an unsorted product. This is the only use of the semantic promise.

Here is an independent accounting of the growing multiplicities.
Put m=M+b+2 and N=9^(b−1). For one tuple pair, all 2b working factors
and each current context use O(q+b)=O(m) records and O(m²) bits with
literal original names and full dictionaries. One L035 input pair has
full E≤c m², so its complete output has O(m⁸) bits by the existing
O(E⁴) bound. There are O(b²) calls, each copied a constant number of
times if both its template and contextual occurrence are retained.
All contexts add O(b²m²) bits. The b reducing branches add at most
O(bm³) bits for U copies and O(bm²) for P/context copies. Local K/value
copies are already inside the quadratic U record count. Repeating the
entire original B dictionary at each of its O(t_j+1) local blocks costs
O((t_j+1)M)≤O(m²) per U. The O(b²) factor-list snapshots have O(b³)
entries altogether; even literal names/indices fit O(m⁴) bits. Tuple
counters, all factor/P/U templates and retained original data fit these
allowances. Therefore C N m^10 bounds the aggregate before final
renumbering, including every independent occurrence.

There are only O(N(b²+b)) final branches and O(b) exterior factor
occurrences per branch. All such connectors fit the previous coarse
count. A dense global reference has O(log(Nm^10+2))=
O(b+log(m+2)) bits. Multiplying the earlier bit bound by m pays that
reference cost even against every old bit; another power covers headers,
output dictionaries and framing. This verifies (10) with absolute
constants and without assuming free sharing. Since b≤q≤M and
9^b≤M^(log₂9)≤(M+2)^4, m≤2(M+2) gives the stated exponent 16.
The input M is never redefined using output size or degree.

The operation count has its own justification. Normalize terminals and
resolve supplied names by scans of the O(M)-bit input; enumerate cut
tuples lexicographically, not paths. Per tuple, insertion sorting uses
O(b²) comparisons/swaps and O(b³) work even if every full list is saved.
A T call enumerates O(m²) pairs of edges in its two working graphs.
Each pair copies four O(m)-record graphs and examines at most one
variable-label pair: all original factor edges have at most one
nonconstant term. Resolving endpoints by O(m)-entry scans gives
O(m⁴) record/table operations. The stated additional m² bookkeeping
slack yields O(m⁶) per call and O(m⁸) for all calls. Constant-only
edges produce no central entry. U construction enumerates O(t_j+1)
pair states and builds a constant number of O(t_j+1)-record local
graphs per pair; summing these and all context/template copies also
fits O(m⁸) per tuple with the same scan allowances. Copies of complete
T/U graphs use dense identifiers plus offsets; they require no search
over all global paths or prior witnesses. Input/block validation fits
the same bound. Across N tuples the operation count is O(Nm⁸), hence
O(S) for S in (10). All stored strings and counters fit O(S) bits;
allowing O(S²) elementary bit steps for any one such scan/copy/comparison
or counter operation is sufficient. Thus O(S³) and the exponent 48
follow from actual loops, independently of the output-size inference.
No truth-table, monomial or semantic-zero computation is hidden here.

Finally consider an actual accepting path, even if its contribution
cancels with another path. A block value path has at most t_j
variable-bearing edges. In T, the central placeholder requires two
variable-bearing marked edges. For each original input, its chosen
prefix and suffix concatenate through the marked edge to an original
accepting block path: a forbidden overlap would be a directed cycle.
Deleting those two edges and adding one placeholder gives degree at
most t_a+t_c−1. Adding the other 2b−2 factor occurrences gives at
most 2q−1. Empty central lists have no accepting path; constant or
zero polynomials with cancelling paths are not discarded semantically.
For U_j, a pair prefix of length t_j−s followed by a correction at s
remaining levels has degree at most (t_j−s)+(2s−1)≤2t_j−1. The K
subpath bound holds structurally because it changes region exactly once.
Together with the earlier P factors and later original pairs, this
gives Σ_(i<j)t_i+2t_j−1+Σ_(i>j)2t_i≤2q−1. Unit connectors and empty
contexts add zero degree. Retained outgoing edges at an internal exit
cannot reach that exit's connector again without a cycle. These are
path bounds before substitution or cancellation, so the claimed 2q+1
bound holds in all the required degeneracies.

The audit finds no substantive defect or required change to the
construction, hypotheses or bounds. Its outcome is EXPLORATION: new
all-size checking evidence, not a repaired mathematical error, improved
theorem, implementation check or certified original discovery. The
bounded test is satisfied for this restricted supplier. Arbitrary-order
W₂, general ER data, formula-only bounds and unrestricted SAT remain
unresolved; Attempts 018/030 and other unfinished results are unchanged.

## Mathlib

Full matching coverage for the logarithmic-block free-algebra witness,
graph construction and binary ledger is **not checked**, not asserted
absent. Supporting mathematical inputs and precise primary citations
are stated above. Classification: POTENTIALLY_NEW under the prior
EXPLORE assessment, meaning that its recorded comparison did not supply
a full match, not certified originality or a new known component result.
The separate step-359 audit is REPRODUCTION under its prior EXPLORE
assessment; it does not change the Mathlib coverage statement.

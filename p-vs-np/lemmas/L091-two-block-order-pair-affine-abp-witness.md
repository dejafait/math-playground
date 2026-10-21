# L091 — A witness for two exchanged variable blocks

## Hypotheses

Use L087's free associative F₂ algebra, explicit dense deterministic
width-at-most-three OBDDs D,E, original representatives f,g, and complete
Boolean/commutator axiom list B with its original placeholder dictionary.
The alphabet is the disjoint union of two supplied nonempty lists
A=(a₁,…,a_r) and C=(c₁,…,c_s). Here C names the second variable block;
it is not a certificate, and B continues to mean the axiom list. The
two orders are exactly A·C and C·A, preserving the internal list orders.
Both r and s may be unbounded; put q=r+s.

Retain precisely L087's M: 2 plus the full binary length of the two
diagrams, orders, original-name dictionary and complete B/placeholder
dictionaries, including axiom words and framing. M excludes all witnesses
and degree parameters. Unreachable states, repeated successors, redundant
tests and Boolean terminal labels are permitted. Only the last level has
terminals. Assume fg(ε)=0 for every Boolean assignment ε. This is a
promise, not a provided semantic zero test.

## Conclusion

There is a deterministic construction of an explicit acyclic affine-F₂
ABP H using only the original variables and B placeholders, with

    H(y,0)=0,                 H(y,B(y))=fg

as identities in the free algebra. For absolute constants K,K' its full
encoding is at most K(M+2)^9, and its construction time in bit operations
is at most K'(M+2)^18. Thus one fixed polynomial bounds both in the
unchanged original M. Every accepting path has pre-substitution degree
at most 2q+1; constants and unit connectors have degree zero. Complete
original dictionaries are retained, even for a zero output.

This is an informal restricted witness construction. The separate step-355
critical audit below finds no substantive defect and clarifies terminal
normalization and the bit-time ledger; no implementation or finite graph
verification is claimed. Its source comparison does not certify originality. It extends
the restricted interfaces toward L087's W₂ premise, but supplies neither
arbitrary-order W₂, general ER data availability, an unrestricted SAT
algorithm nor a separation. It is not a main-problem candidate.

## Proof

**Imports and their scope.** The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-19-two-block-order-pair-witness.md`. L026 gives
the exact ordered representatives, common-order product correction and
injectivity on increasing multilinear words. L071's post-compilation
value/K/P/W construction realizes those identical polynomials as affine
graphs; only that component is used. No treewidth or compilation theorem
from L071 is asserted without its hypotheses. L035 gives a graph-sized
commutator witness for two supplied original-only affine ABPs, including
zero and constant factors. L087 fixes the receiving dictionaries and M.

The supporting literature is Bryant, *Graph-Based Algorithms for Boolean
Function Manipulation*, IEEE TC 35(8) (1986), §4.3, author-restored
pp.12–14 ([primary PDF](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf)),
for common-order Apply; Li–Tzameret–Wang, *Characterizing Propositional
Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4 (11 September
2015), Lemmas 3.6–3.7, pp.17–18
([primary PDF](https://arxiv.org/pdf/1412.8746v4)), for formula commutation;
and Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non
Commutative Models*, author manuscript, Lemma 2 Step 1, p.5
([primary PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)),
for separate-graph composition. The graph-sized formal corrections are
the cited local results, not consequences of Boolean Apply alone or of
unpaid formula unfolding. Their known component constructions are reused;
the block-cut assembly and original-input ledger below are the additional
argument needed for this target.

**Exact cutting at the two boundaries.** Let I be D's set of states
immediately after the r A-tests, and J be E's set of states immediately
after the s C-tests. Since the blocks are nonempty these are nonterminal
levels, with |I|,|J|≤3. Include unreachable states. For i∈I define u_i to
be the representative of D's A-prefix with terminal value 1 at boundary
state i and 0 at every other boundary state. Define v_i to be the
representative of the C-suffix rooted at i, with D's original terminals.
For j∈J define w_j from E's C-prefix by the analogous indicator terminal
rule, and z_j from E's A-suffix rooted at j.

These are dense width-at-most-three diagrams on their respective blocks.
Relabeling and merging indicator terminals changes no transitions before
the cut. Each is an explicit copy of at most the original diagram plus
constant framing. Its affine value graph uses edges 1+y and y for the
two branches, with a unit edge from each value-1 terminal to a fresh
sink and none from value-0 terminals. This is L071's value component.
All four types of factor are original-only.

Every full root-to-terminal path crosses its boundary exactly once.
Partitioning this finite set by that state, and using distributivity with
the original factor order, gives the free-ring equalities

    f=Σ_(i∈I) u_i v_i,             g=Σ_(j∈J) w_j z_j.       (1)

This proves exact equality, before any Boolean substitution. The path
partition is a proof device only: the construction copies graphs and
does not enumerate paths. Alternatively (1) follows by substituting the
suffix polynomials into the finite prefix recurrence and distributing.
Zero or unreachable indicator factors cause no exception.

**Blockwise normalization.** Fix i,j and suppress these indices briefly.
The pair u,z has common order A, and v,w has common order C. Let P_ij be
their synchronous product representative on A and Q_ij that on C. A
product state records one state of each diagram, so there are at most
nine states at any block level. Its terminal value is the product of
the two original terminal bits. This explicitly defines P,Q even when
the Boolean-zero promise is false.

Apply L026 equations (7)–(12) and L071's post-compilation W graph to
these two diagram pairs. They provide independently written graphs
U_ij,V_ij with the exact identities

    U_ij(y,0)=V_ij(y,0)=0,
    U_ij(y,B)=u_i z_j+P_ij,
    V_ij(y,B)=v_i w_j+Q_ij.                                 (2)

Their alphabets are the respective blocks. Map each block Boolean or
commutator placeholder to its original B position; this is injective
renaming into the full free alphabet, preserving both identities. The
identifier order for a commutator may differ from its block order:
over F₂ both orientations have the same axiom polynomial. Retain all
unused full-alphabet entries too. No original clause placeholders occur.
P and Q are original-only, increasing multilinear in A and C respectively.

For explicit receiving details, L071's pair region advances one level
along its two literal edges. Each pair has three local correction blocks:
the two literal-times-K-times-suffix-sum blocks and one Boolean-placeholder
times-two-suffix-sums block. Every factor occurrence is independently
copied. A path leaves the pair region once and never returns. This graph
therefore realizes L026's recurrence, rather than merely a circuit for
it. With a block of length t and operand width three, a pair region has
O(t+1) records and each local block O(t+1) records, hence O((t+1)²)
total records. The product graph P or Q has O(t+1) records. This component
requires neither an extension-output diagram nor an ER proof: (2) is
L026's product identity with its explicit synchronous representative.

**Restoring the original factor order.** Form the original-only serial
graph F_ij for v_i w_j using disjoint copies. Apply L035 to F_ij and a
separate graph for z_j. Write the resulting commutator-only graph T_ij.
It satisfies

    T_ij(y,0)=0,
    T_ij(y,B)=v_i w_j z_j+z_j v_i w_j.                      (3)

Crucially no U,V or other placeholder-containing graph is passed as an
original-only argument to L035. Construct H as the disjoint parallel sum
of the following three serial products for each of the at most nine i,j:

    u_i T_ij,               U_ij v_i w_j,                P_ij V_ij.  (4)

Use independent copies at every occurrence, constant-one connectors,
and fresh common entrance/exit vertices. Serial products preserve the
displayed order. All internal component edges remain affine. These
disjoint compositions are acyclic, and every accepting path traverses
exactly one summand and its factors in sequence. Distinct fresh sum
endpoints preclude an unintended empty path. No sharing across separate
two-sided contexts is assumed.

At zero placeholders every summand in (4) vanishes. After B substitution
its three values, in the displayed order, are

    u_i v_i w_j z_j + u_i z_j v_i w_j,
    u_i z_j v_i w_j + P_ij v_i w_j,
    P_ij v_i w_j + P_ij Q_ij.

The two middle pairs cancel in F₂ with exactly these factor orders.
Consequently, by (1),

    H(y,B)=fg+R,            R=Σ_(i,j) P_ij Q_ij.            (5)

Every word in R is increasing and multilinear in the single order A·C:
the variable blocks are disjoint and each P precedes its Q. On a Boolean
assignment, ordinary scalar multiplication commutes, and the synchronous
product semantics give

    R(ε)=Σ_(i,j) u_i(ε)z_j(ε)v_i(ε)w_j(ε)=f(ε)g(ε)=0.

L026's injectivity on this precise ordered multilinear space yields
R=0 in the free algebra. We do not infer that arbitrary Boolean-zero
free polynomials are formally zero, or that individual summands are zero.
There is no need to decide which factors vanish. Equations (4)–(5) now
give both required identities while retaining the original fg.

**Full original-M ledger and construction.** Put m=M+2, so q≤m and every
original name has at most m bits. The number of factor diagrams is at
most 2|I|+2|J|≤12. Merge equal scalar terminals in each working copy,
retaining the original records separately, as detailed in the audit
below. Each working factor has O(q+1) states/edges; dense references and even
writing every original name at every occurrence give at most O(m²) bits
per independently encoded factor, with its full dictionary. All graphs
for products v_i w_j and for z_j, plus complete original alphabet and
commutator dictionaries, therefore have combined L035 input length
E_ij≤c m², for one absolute c. This parameter is bounded in M before
any witness is constructed; it is not a replacement definition of M.

L035 supplies each T_ij with O(E_ij⁴)≤O(m⁸) full bits. There are at most
nine such graphs and no nested call to that construction. Each of the
at most eighteen U,V graphs has O((q+1)²) records; labels have bounded
many terms. Paying up to m bits per original name/placeholder name and
binary graph references gives O(m³) bits each. The at most eighteen P,Q
graphs have O(q+1) records each. Keeping every factor, P,Q, local template
and unused input state as auxiliary data still fits these bounds.

All occurrences in (4) are separately copied. There are at most 27 sum
branches, a constant number of graph occurrences per branch, and only
constant-many new connectors per occurrence. Fresh global references
have O(log m) bits, because the total number of records is O(m⁸).
Even charging this logarithmic factor against every previously written
bit gives a conservative O(m⁹) bound for H and retained auxiliary data.
Each independently exported component may additionally carry the full
original B and original-name/placeholder dictionaries of O(M) bits;
their number is constant. If these dictionaries are also copied with
each local correction block, there are O(q) such blocks per U or V, so
their O(qM) extra bits remain below the stated bound. Root references,
orders, terminal values, isolated records, all labels and framing are
included. No block assignment list or path list is written.

For time, use explicit list representations, append-only graph copying,
linear-scan dictionary lookup, and elementary binary renumbering. Prefix
cuts require scans of the input; synchronous pairs and local blocks use
at most quadratically many block states. In L035 the two inputs here
have O(q) edges and bounded-term labels, so at most O(q²) edge pairs
are enumerated, with four O(q)-record factor copies per pair and a bounded
number of central placeholder terms. Thus its explicit loops are
polynomial in m without a promise oracle. All construction stages can
be performed using at most a quadratic number of bit operations in a
constant multiple of the conservative O(m⁹) complete intermediate/output
budget: scans, finite table comparisons and string copies suffice, and
there is no search or nontrivial arithmetic on longer integers. This
gives the stated O(m¹⁸) common bound. The semantic promise is used only
in proving R=0, never as a step of the construction.

For path degree, u,z use at most r variable-bearing edges and v,w at
most s. L071 bounds U paths by 2r−1 and V paths by 2s−1. A nonzero
central term in L035's T marks one variable-bearing edge in v_i w_j
and one in z_j; its four subpaths omit those two edges and insert one
placeholder. Prefix/suffix paths within each input concatenate through
the marked edge in its DAG. Their total degree is therefore at most
2s+r−1 (the weaker bound 2s+r+1 would also suffice). Multiplication
by u_i gives at most 2q−1. The other branches have bounds
(2r−1)+2s and r+(2s−1), respectively. In particular 2q+1 is a uniform
conservative bound, valid before cancellation. Unit connectors add zero;
zero labels add no nonzero contribution. The graph-size bound also
independently bounds every path degree by its vertex count.

**Degenerate cases and limitations.** A singleton block still has a
nonterminal start and a terminal cut, and all formulas above apply.
Repeated successors remain separate literal edges and retain their F₂
multiplicities; constant functions and unreachable states require no
semantic simplification. No-path factors give zero via distinct-endpoint
graphs. Terminal products are scalars, and the L026 W terminal is zero;
we do not drop witnesses on a nonterminal merely because its Boolean
function is constant. Every copied graph has a fresh sink, so serial
composition introduces no accidental return or empty accepting path.
These points include constant and zero suffixes without a hidden
nonzero-path assumption. The two nonempty blocks ensure the original
orders differ, as L087 requires.

L088–L090 are comparison results only, not inputs: no sequence of
potentially growing adjacent-swap snapshots or assignment enumeration
is used. Attempt 030's universal value-availability obstruction remains
independent. This proof treats exactly the two-block restriction and
does not infer a bounded number of such blocks for arbitrary permutations.
The all-size identities and ledger are the evidence for this informal
result. The separate audit below checks cutting, factor order, injectivity
and full copying/time accounting without an implementation claim.

**Separate critical audit — step 355, 2026-10-19.** This audit uses the
previously ready EXPLORE assessment
`drafts/literature/2026-10-19-two-block-order-pair-critical-audit.md`.
It reproduces the verification of the stated construction, not a new
block-witness theorem or a claim of originality. L026 (4)–(12), L035's
four-copy marked-edge construction, L071's post-compilation value/K/P/W
graphs and their audit, and L087's B/M conventions are the exact inputs.
The supporting primary sources and their limited roles are cited above;
no new source, semantic identity test or treewidth compiler is used.

At D's cut, the rth test's edges terminate at level r, which is still
nonterminal in D because s≥1. In the truncated prefix these very states
become terminals. Thus the last A label belongs to u_i and the first C
label belongs to v_i, with neither omitted nor duplicated. The same
check at E's level s puts its last C label in w_j and first A label in
z_j. For any fixed original accepting path there is exactly one cut
state. Conversely a prefix ending at that state concatenates with each
suffix starting there, uniquely, since levels increase. The artificial
indicator terminal contributes precisely 1 at that state and 0 at the
others. Distributivity therefore gives (1) in the free ring, including
every affine constant term, without expanding paths in the algorithm.
This also checks r=1, s=1 and the case r=s=1. Unreachable states can
have nonzero suffixes, but their prefix polynomials are zero; they are
retained rather than assumed to have zero suffixes.

Here is an explicit terminal convention for the ledger. If width three
bounds only nonterminal levels, a supplied encoding can contain more
than O(q) isolated terminal records. Before making working factor
copies, replace all scalar terminals by at most two terminals, labeled
0 and 1, redirecting each last-level edge to its original bit. In a
prefix apply this operation only *after* assigning the indicator bits
for its chosen boundary state. Two parallel literal edges are retained
when their targets coincide. Every last-level suffix recurrence is
unchanged, and backward induction preserves every preceding free
polynomial. Thus working factors really have O(q+1) records under either
width convention. Retain the complete original records as O(M) auxiliary
input data; no claim of O(q) for arbitrarily many supplied isolated
terminals is needed. This makes explicit the scalar-terminal merging
implicit in the graph copies, without changing the theorem, M or bound.

For (2), both operand pairs have the same respective block order and
width at most three. Their terminal products are scalar products, so
the terminal W value is zero even when the terminal product is one.
The paired graph realizes L026 (8) by its unique exit from the pair
region, with two separate eK blocks and the Boolean block. Every K
operand is a strictly later suffix; it switches once to a value region.
There is no recursive W copy inside a correction block. This verifies
the O((t+1)²) record count and both formal identities for a t-variable
block independently of any promised ER output. Renaming its original
Boolean/pair placeholders to the full B dictionary preserves the free
identities; in F₂ reversing the identifier orientation leaves
a c+c a unchanged. Extra unused dictionary entries do not change them.

In (3), v_i w_j is a serial product of original-only graphs, and z_j
is original-only too. L035's suffix order is G-suffix then F-suffix;
with F=v_i w_j and G=z_j this yields precisely the two words of (3).
Neither U nor V is an input to that invocation. Set u=u_i, v=v_i,
w=w_j, z=z_j, P=P_ij and Q=Q_ij. Substituting into each branch of (4)
gives respectively uvwz+uzvw, uzvw+Pvw, and Pvw+PQ. Addition cancels
uzvw and Pvw twice, leaving uvwz+PQ. Summing and using (1) establishes
(5) with the original fg, not gf or a reordered substitute. At zero
placeholders the same three branches vanish separately by the zero
identities of T,U,V, regardless of the Boolean-zero promise.

The order in the residual is crucial: every P word uses A once in its
given order, every Q word uses C once in its given order, and all P
factors stand to the left of Q. Disjointness of the blocks places the
entire sum R in one A·C increasing multilinear space, including the
empty word. Scalar evaluation gives R(ε)=f(ε)g(ε)=0. L026's injectivity
then applies to R as a whole. It is not applied to an individual PQ,
to uvwz, or to a general Boolean-zero free polynomial. The construction
can still be run on a nonzero input product; its proved identity there
is H(B)=fg+R, so no unmentioned semantic tester is hidden in the proof.

For a separate cost check, normalize terminals as above and use dense
working references while preserving the full original dictionaries.
There are constantly many factor graphs with O(q+1) records and at
most one nonconstant original per edge label. Copying original names
literally and retaining B costs O(m²) bits per factor, so E_ij=O(m²)
is a valid pre-witness L035 input bound. L035 then gives O(m⁸) full
bits per T, with at most nine T invocations. Each U,V has O((q+1)²)
records, O(m³) bits, and at most O(q+1) independently copied local
blocks. Each P,Q has O(q+1) records. Every use in the 27 or fewer
branches is copied separately, and auxiliary copies/dictionaries add
only the previously charged constant multiplicities or O(qM) per U,V.
Renumbering all those records needs O(log m) bits per reference. Paying
this factor even against all old bits gives O(m⁹) complete output and
intermediate storage. Normalization retains O(M) original records once;
it does not redefine M to include the witnesses or a degree parameter.

The time bound does not follow from output size alone. One concrete
implementation first scans and validates the O(M)-bit original records,
constructs the scalar-terminal redirection tables, then constructs all
working graphs by explicit loops. A T invocation enumerates O(q²)
edge pairs, copies four O(q)-record graphs per pair, and examines at
most one nonconstant label pair per edge pair. Constant-only edges
give an empty central list. A W invocation enumerates O(q) pair
states and builds constantly many O(q)-record K/value blocks for each;
these are built directly from their suffix diagrams, never recursively
by copying previously exported witnesses. Synchronous products also
have only O(q) pair records. A linear scan through a component's O(q)
reference table for each copied record gives at most O(m⁴) record/field
operations altogether, including input/terminal scans with the coarse
q≤m bound. Final branch copies of a completed T use its dense consecutive
identifiers with a fixed additive offset, not a linear search through
its larger reference table; counter addition is charged as bit work.
Arbitrary supplied identifiers can be resolved by scanning
the original O(M)-bit input; global names use binary counters of
O(log m) bits. Each such operation, including comparison, lookup,
append and copying, can conservatively be executed in O(m⁹) bit
operations by scans of the above complete storage budget. Thus even
this deliberately inefficient algorithm costs O(m¹³), which is within
the asserted O(m¹⁸); no tighter theorem bound is claimed. There are
no path, assignment or monomial enumeration loops and no oracle calls.

For path degree, at a W state with h remaining levels a local block
has degree at most 2h−1. A preceding pair prefix has at most t−h
variable edges; its complete path degree is at most t+h−1≤2t−1.
This proves the U,V path bounds even for paths whose contributions
cancel. In T, a nonempty central label marks one variable-bearing edge
of F=v_i w_j and one of G=z_j. Its F-prefix and F-suffix concatenate
through the marked edge to an actual F path; otherwise a repeated
vertex would make a cycle. The same holds in G. Those two deleted
degree-one edges are replaced by one placeholder. Since F paths have
degree at most 2s and G paths at most r, the T bound is 2s+r−1.
After the exterior u, the first branch has degree at most 2q−1; the
other bounds are 2r−1+2s and r+2s−1. All are at most 2q+1, before
substitution or cancellation. Empty central lists have no accepting
path, so a zero central expression does not invalidate the count.

Finally, distinct fresh endpoints exclude accidental empty acceptance
for zero factors. Every local graph is acyclic, and inter-copy edges
go only forward. L035's retained unused internal edges cannot provide
a second exit path: leaving a designated exit and returning to its
connector would create a cycle. Scalar terminals, repeated successors,
constant functions and disconnected states therefore need no unproved
nonzero or reachability promise. A semantically constant nonterminal
is not silently assigned the scalar-terminal W value.

The audit finds no substantive defect and no change to either identity
or stated bound. Terminal normalization and the explicit operation
count clarify the implementation-free all-size ledger. This is new
informal checking evidence, classified REPRODUCTION with outcome
EXPLORATION, not a new theorem, improved bound, executable verification
or certified originality. Arbitrary-order W₂, general ER data and SAT
remain unresolved; Attempts 018/030 remain intact.

## Mathlib

Full matching coverage, the block specialization and the explicit binary
ledger are **not checked**. No absence claim is made. The primary
supporting results and exact versions are cited above; none is asserted
to state the full two-block witness theorem. The construction's original
classification is POTENTIALLY_NEW under the prior EXPLORE comparison, meaning only that
the checked comparison found no full match, not certified originality.
Step 355's separate audit is REPRODUCTION under its ready EXPLORE assessment.

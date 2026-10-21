# L075 — Affine-ABP data for every unchanged expander root

## Hypotheses

Use exactly L031's supplied finite simple graph on n>=2 vertices, its fixed
expansion/degree parameters, ordered m>=1 edges, either sigma in {0,1}, original
unit CNF F, signed-AND ER refutation pi and actual binary length
T=2+|F|+|pi|. Use L032's unchanged free noncommutative F₂ representatives,
including both signs of every original and extension variable, constants and
every accumulator. In particular, h has the ordered formal value R_m R_m;
original contradictory units are not substituted in any representative.

Use L032's explicit abstract value DAG and its original axiom list A: the n+1
original clause falsity polynomials, n Boolean polynomials and n(n−1)/2
commutators, each with its own independent placeholder. Every AND relation
H_i is zero. Graphs are explicit finite acyclic affine-edge ABPs in L037's
model; an empty accepting path has value one. Charge all independently
written graphs, root associations, labels, names and complete axiom framing.

## Conclusion

There is a deterministic construction of all L037 representative and H_i
graphs with the exact formal values of L032 and aggregate full-bit length

    E_ABP = O((n+m+2)³ log(n+m+2)) = O((T+2)³ log(T+2)).

The constants are absolute for the fixed encoding below. Construction time
and aggregate bit length are both at most K(T+2)^8 for one fixed K. The
receiving parameters remain S=2n+8m+2, d=m²+7m−1 and h=1. Thus L037 supplies
an original-axiom affine ABP C with C(x,0)=0 and C(x,A)=1, with polynomial
full-bit length, complete pre-substitution degree and construction time in T.
No treewidth/deletion promise is used.

This is a family-specific REPRODUCTION/application of formula-to-graph
conversion and the existing conditional receiver, without certified
originality. The separate informal critical audit below found no substantive
defect in this specialization; no formal verification is claimed. It does not convert
L032's optional prescribed pair/Boolean/defining-clause witness polynomials,
establish arbitrary ER data or a formula-length-only certificate bound, or
resolve W/V/U, every-certificate hardness or unrestricted SAT.

## Proof

**Imported conversion and the specialization to be paid.** Use Ran Raz and
Amir Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative
Models*, author-hosted 16-page manuscript (no printed revision date),
[Lemma 2, Step 1, PDF p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
The complete scalar/variable, sum/parallel and ordered-product/serial cases
were inspected in the reused assessments identified by
`drafts/literature/2026-10-17-expander-exact-root-affine-abp-data.md`.
They convert a supplied arithmetic formula tree to a linear-record graph,
allowing constants and unequal path lengths before homogenization. The
homogeneous-component theorem's zero-free-term hypothesis is not invoked.
F₂ is an allowed field, and the intermediate graph is an allowed L037 ABP.
No PIT theorem or unrestricted circuit-to-ABP conversion is imported.

What remains is the family's formula-occurrence and complete encoding bound.
Use scalar and variable leaves of size one, and charge one for each binary
sum or product. Each use of a child tree is an independent occurrence. In
particular, a complement is written as 1+P with size |P|+2, even if subsequent
formal cancellation could shorten it. No distributive expansion into words
is performed.

**Every circuit-root occurrence.** Put P_i=x_(u_i)x_(v_i). L032's exact roots
are

    R_1=1+P_1,    R_i=R_(i−1)(1+P_i) (2<=i<=m),
    P_h=R_m R_m.

Expand only the references in these displayed expressions to formula trees,
preserving factor order and their indicated bracketing. Then |P_i|=3 and
|1+P_i|=5. Induction gives

    |R_i|=6i−1,                 |P_h|=12m−1.                 (1)

Indeed the first size is five, and each subsequent product adds five plus
one. The h formula uses two separate R_m trees plus its product node.
The positive circuit gates g_1,...,g_(2m) are the m edge gates, q_i=R_i
for 2<=i<=m, and h. Their total positive-tree size is

    C_m=3m+sum_(i=2)^m (6i−1)+(12m−1)
       =3m²+17m−6.                                         (2)

The empty sum at m=1 is zero, and (2) then counts sizes 3 and 11.

The actual signed units eta_k from L031 determine U_k. At the consistent
evaluation assignment s_0, every p_i is false, every existing q_i is true
and h is true. Thus exactly the m edge-gate eta_k are negative. At s_1,
all p_i are true, every existing q_i is false and h is false. Thus exactly
(m−1)+1=m of the eta_k are negative. These observations select signs only;
they do not restrict the variables in the arithmetic roots. With U_k the
unchanged signed representative of eta_k, in either case

    sum_(k=1)^(2m) |U_k| = C_m+2m = 3m²+19m−6.             (3)

For example, when m=1 the U list is (1+P_1,P_h) at sigma=0 and
(P_1,1+P_h) at sigma=1. The repeated product in P_h is retained in both.

**Every accumulator, both signs and separate outputs.** The anchor A_0 is
x_1 at sigma=1 and 1+x_1 at sigma=0, of size at most three. The exact
accumulator is A_k=A_(k−1)U_k. Expanding the earlier A occurrence once gives

    |A_k|=|A_0|+sum_(j=1)^k (|U_j|+1)
           <=3m²+21m−3=:B_m,       1<=k<=2m.               (4)

This is a tree statement: all occurrences of a U_j within different A_k
are separately paid. There is no recursive squaring of an accumulator.
Also B_m>=21 at m>=1, so this bound is positive at the boundary. At m=1
the last accumulator sizes are 21 and 19 at sigma=0 and sigma=1,
respectively, without any Boolean simplification of h.

For each of n originals, independently writing its positive and negative
trees costs 1+3=4 occurrences. For an extension whose positive tree has
size a, the two separately written signs cost a+(a+2)=2a+2. There are
2m circuit and 2m accumulator variables. Include the two constant trees.
The aggregate number L of occurrences in all S representative trees is
therefore bounded by

    L <= 4n+2C_m+8m+4m B_m+2
       = 4n+12m³+90m²+30m−10
       <=128(n+m+2)³.                                      (5)

For the last inequality put r=n+m+2>=5. The positive terms are at most
12r³+120r²+4r<=37r³, since 120/r+4/r²<=25. The displayed 128r³ is
conservative. This estimate covers all unused roots and both
signs, not only roots occurring at the final output. The alias R_1 is
already the complement of p_1 and creates no extra abstract node.

All trees compute the identical formal representatives by substitution
of definitions in their actual order. Their internal syntactic degrees
are unchanged by copying. L032's proved bound d=m²+7m−1 consequently
applies; it is not being used to infer small formula size.

**Graph records and zero relations.** Apply the imported conversion to
each of the S trees separately. It can use distinct terminals at every
formula occurrence. In its scalar/variable case there are two vertices
and at most one labeled edge; an addition uses two fresh terminals and
four constant-one connectors to its two disjoint children; a product
uses one constant-one connector between disjoint children. Thus at most
2L vertices and 4L edges suffice in aggregate. These counts are the local
record ledger for the imported conversion, not a new representation
theorem. A zero scalar edge can be omitted. Constants and single x labels
are affine, and all connector labels are one. Disjoint children and the
series/parallel construction preserve acyclicity, the empty-word terms
and the ordered polynomial without homogenizing or enumerating paths.

For each of the 4m AND nodes, independently supply two isolated distinct
vertices as the H_i graph, with the designated source and sink different.
There is no accepting path and hence its polynomial is zero. A coincident
source and sink would have an unwanted constant empty path and is not
used. These graphs add 8m vertices, no edges and their root records.
The constant-zero representative can use the same two-vertex no-path
construction in its own separate copy. All S representative graphs and
4m relation graphs are separately numbered and separately written.
Their total vertex/edge count is O((n+m+2)³) by (5).

**Full dictionaries, bit cost and construction time.** Set r=n+m+2. The
abstract DAG has S=2n+8m+2=O(r) nodes and O(r) signed/AND associations,
including the two constants. Each proof variable has its actual dense
identifier at most n+4m, and the associations record the two ordered
operand nodes for every AND and the underlying node for each sign.
This framing costs O(r log r) bits.

There are a=n+1+n+n(n−1)/2=O(r²) original axioms. Use their actual ordered
list, with separate placeholders named by list position. Each has a
constant-size polynomial description over dense original indices, so
the complete list, original names, placeholder names and alphabet framing
cost O(r² log r) bits. No extension axiom or auxiliary symbol is substituted
for an original axiom. Clause placeholders unused by the zero H graphs
remain explicitly in the list. Even if this entire dictionary is repeated
for each of the S+4m=2n+12m+2=O(r) separately written graphs, its cost is
O(r³ log r). Repeated names and coincident polynomial values save nothing
needed by this upper bound.

Use dense per-graph vertex identifiers, explicit source/sink references,
vertex/edge counts and finite singleton-label records. By (5) the aggregate
record count is O(r³), so references, labels and lengths take O(log r)
bits per record. Isolated vertices, all constants, zero graphs and all
root-to-abstract-node associations are charged. Gamma-coded nonnegative
integers and fixed finite record tags, as in L031, give total full-bit
length E_ABP=O(r³ log r), including the repeated dictionaries just bounded.
There is no unit-cost allowance for a long identifier.

L031's actual encoding writes n+1 original unit clauses and 12m defining
records, each with nonempty bit encoding. In particular n+m<=T; hence
r<=T+2. Its upper bound on T is not used in this direction. Enumerating
the finite graph and gates, evaluating the sign choice at s_sigma,
expanding exactly the paid formula occurrences, performing the imported
linear-record conversion, repeating dictionaries and renumbering graphs
are deterministic operations on explicitly bounded lists. None enumerates
monomials, assignments, paths or proof ancestry. One implementation stores
the trees with occurrence indices, traverses them with a stack and assigns
consecutive graph identifiers. It uses O(T+r³) record/stack operations and
O(log(T+2))-bit indices. Even replacing indexed accesses by scans of all
stored records and charging quadratic bit operations for each index
calculation gives the conservative time bound

    O((T+r³)² (log(T+2))²) <= K(T+2)^8.

Here r<=T+2 and log²(T+2)=O((T+2)²). The bounded number of graph records,
stack entries and repeated dictionary entries are all already charged.
This deliberately loose fixed polynomial covers parsing, copying and
output writing on a sequential bit machine, without unit-cost arithmetic
on unbounded values. Increasing K also bounds the full output bit length
by the same polynomial.

**Every receiving promise and downstream use.** L031 supplies the valid
width-one original CNF and actual signed-AND ER refutation, with every
original variable occurring in F. L032 supplies the explicit acyclic
abstract DAG, exact signed complements, originals/constants and ordered
AND values r_i=r_a r_b. The separately constructed x-only graphs have
exactly those values. Thus every supplied zero graph satisfies formally

    H_i(x,0)=0,        H_i(x,A)=0=r_i+r_a r_b.

There are no nonextension proof variables absent from F to account for.
The original placeholders are independent, d is the existing bound and
h=1 bounds all zero relation roots. The preceding ledger charges every
part of L037's E_ABP. These verify all its hypotheses. Import its audited
conditional conclusion with N=2+T+S+E_ABP, which is polynomial in T:
the constructed C has both formal IPS identities, O(N⁸ log(N+2)) full
bits, O(N⁸) complete pre-substitution degree and polynomial bit time.
This application does not identify C with L025's prescribed output or
require affine ABPs for L032's optional K/B/D roots. L037 builds its own
alternative corrections from the supplied graphs.

**Continuation test and limitations.** Equations (1)–(5), independent
graph copies and the dictionary ledger meet the required fixed-polynomial
threshold for every graph in the hypotheses, both sigma choices and m=1.
No numerical test is used as the proof. Expansion itself is not needed
for this representation construction beyond the already ensured m>=1.
Accordingly the construction remains available on the unbounded family
where L074's obstruction eventually prevents applying L073; that
obstruction and Attempts 020–021/028 are unchanged. There is no generic
degree-only circuit conversion and no prescribed pair-table conversion.
The original opposing units still have an immediate alternative proof
and constant-size certificate, so this is neither optimal-certificate
hardness nor a resolution of the main gap. The separate critical review below
covers this occurrence/encoding specialization and its receiving interface;
no formally verified implementation is claimed.

**Separate critical audit, 2026-10-17 (step 290).** The preexisting SPECIALIZE
assessment `drafts/literature/2026-10-17-expander-exact-root-affine-abp-audit.md`
covers this REPRODUCTION audit. The target is the complete supplied-data
bound and L037 application, not optional K/B/D outputs or a new conversion
theorem. The full L075 argument, L031's actual definitions and encoding,
L032's exact-root/degree/zero-relation statements and L037's complete
receiving hypotheses were checked. L025's inherited hypotheses introduce
no additional promise omitted from L037's detailed statement. The primary
conversion citation remains Raz–Shpilka, Lemma 2 Step 1, PDF p.5, with the
previously inspected cases and qualifications stated above.

For an independent occurrence check, the q-root sum is

    sum_(i=2)^m (6i−1)=3m²+2m−5.

It is zero when m=1. Adding the m edge roots of size three and the h
root of size 12m−1 gives C_m=3m²+17m−6, including C_1=14.
No q_1 root is charged: R_1 is the existing signed p_1 alias. At sigma=0
exactly the p_i are negative among the eta_k; at sigma=1 exactly q_2,...,q_m,h
are negative. Thus both sign choices add exactly 2m occurrences to C_m.
In either case all U_k are separate trees with positive sizes. The identity

    |A_k|=|A_0|+k+sum_(j=1)^k |U_j|

follows from one new product node at each actual accumulator definition.
Its prefix sums are increasing, giving the stated B_m for every k.
At m=1, write P=x_u x_v and H=(1+P)(1+P). Then |P|=3, |H|=11.
For sigma=0 the anchor size is three, U sizes are (5,11), and accumulator
sizes are (9,21); for sigma=1 they are respectively one, (3,13), and
(5,19). This checks the empty q-range and both signs without replacing
H by 1+P or imposing the contradictory original units.

The exact aggregate representative-tree accounting is

    L=4n+2C_m+8m+2 sum_(k=1)^(2m) |A_k|+2.

Here 8m is the two extra complement occurrences for each of 4m extension
variables, and the last two occurrences are the constants. Substituting
sum_k |A_k|<=2m B_m gives exactly 4n+12m³+90m²+30m−10.
For r=n+m+2>=5 its positive terms are at most
12r³+120r²+4r<=37r³<=128r³. Thus the complete sum of independently
written occurrences, rather than just the largest tree or shared gate
count, satisfies (5). Every signed root and unused root is in this sum.

The imported graph construction's record bound can also be checked per
tree. If a tree has b leaves, u sum nodes and v product nodes, its size is
l=b+u+v. With the stated connector implementation it has 2b+2u<=2l
vertices and at most b+4u+v<=4l edges. Ordered products concatenate
the two disjoint children in the original order, while sum branches stay
disjoint between their fresh endpoints. Distinct terminals are maintained
by all three cases, and deleting a zero-labeled leaf edge changes no
accepting value. These are checks of the cited implementation's receiving
cases, not an invocation of its homogeneous-component/PIT conclusion.
Summing over trees and adding the 4m distinct-terminal zero graphs gives
at most 2L+8m vertices and 4L edges. In particular no zero relation acquires
the constant-one empty path. The constant-one representative does have
the required value, via its single constant-one edge.

There are exactly 2n+12m+2 graph packages. Each full original dictionary
has (n+1)+n+n(n−1)/2 entries, with distinct position identifiers even
when two polynomials coincide. Each entry has a bounded number of symbols
and operations and O(log r) bits, because original indices are at most n
and placeholder positions are O(r²). Repeating the entire dictionary in
every package therefore costs O(r³ log r), independently of whether its
symbols occur on any edge. The graph records contribute the same bound:
their aggregate number is O(r³), and vertex indices, endpoints, counts
and labels each have O(log r) bits. Abstract-node/sign/ordered-operand
associations add O(r log r). This verifies the full E_ABP framing; neither
dictionary sharing nor sharing of graphs across roots is assumed.

The direction of the actual-T comparison is essential. The source
encoding contains n+1 nonempty original unit-clause encodings and 12m
nonempty definition records, including both projection slots of h even
when equal. Consequently n+m<=T directly from the written input. The
upper estimate T=O((n+m)log(n+m+2)) is not inverted. Let
M=T+r³; parsing plus the charged tree/graph/dictionary entries require
O(M) logical record operations with O(log(T+2))-bit indices. Traversal
can write a disjoint child occurrence directly into its destination;
it need not repeatedly copy an already expanded growing prefix.
Formula traversal stacks have at most O(r³) entries and use these same
indices. Replacing each indexed lookup by a scan of O(M) stored records
and each index operation by quadratic bit arithmetic costs at most
O(M² log²(T+2)). This also pays copying and sequential output. Since
r<=T+2, M=O((T+2)³); hence this bound is at most K(T+2)^8 after
enlarging one fixed K. All graph and dictionary entries fit this ledger,
not just arithmetic operations on the formal polynomials.

Finally, L031 gives the required valid width-at-most-three ER input,
width-one F, dense original variables and earlier signed operands.
L032's topological ordering places each complement after its underlying
value and before any AND using it. The S nodes include every proof
value; all nonextension variables already occur in F. Each representative
graph computes the unchanged x-only formal value, so the original and
constant nodes and every exact complement retain their required values.
At each of the 4m AND nodes r_i=r_a r_b formally, which makes its
distinct-terminal zero H satisfy both receiving identities. L032's
d=m²+7m−1>=1 bounds all representative root degrees; h=1 bounds the
zero H roots before substitution. It is legitimate that the unused
original placeholders still occur in the full independent dictionary.
These facts meet every L037 promise with the charged E_ABP. Therefore
N=2+T+S+E_ABP is polynomial in actual T, and L037's audited bit/degree/time
conclusion applies. Its O(N⁸) degree is imported from actual graph size,
not inferred from the optional pair table or from semantic degree alone.

The audit passes the required all-size occurrence, full-bit and receiving
tests with no change to a statement, bound or direct mathematical input.
No finite numerical test is being promoted to an all-size proof, and no
new implementation was verified. This is independent local verification
of a known-machinery specialization, not progress beyond the sources
checked or a newly discovered general theorem. Attempts 020–021/028 and
the immediate alternative certificate remain valid. Arbitrary ER data,
formula-only bounds, W/V/U, every-certificate hardness and unrestricted
SAT transfer remain unresolved. Mathlib coverage remains not checked.

## Mathlib

The full family-specific occurrence/encoding result and the ABP/receiver
specialization are **not checked** in Mathlib; no absence claim follows.
The precise standard input is Raz–Shpilka, Lemma 2 Step 1, PDF p.5, linked
above. L031/L032 fix the already established exact family/data; L037 is
the local conditional receiver. The preexisting SPECIALIZE assessment
authorizes this REPRODUCTION application, not an originality claim or
a new general theorem about ER proofs.

# L071 — Affine-ABP reduced data for treewidth-two extension values

## Hypotheses

Use L025's explicitly encoded width-at-most-three original CNF F and valid signed-AND ER refutation π, with T=2+|F|+|π| in full binary bits. There are n original variables, n≤T. Retain the ordered original clause, Boolean and pair-once commutator axiom list A(x), with independent placeholders t, over the free associative F₂ algebra. Nonextension proof variables absent from F have value zero.

Form the full Boolean value DAG G: one shared vertex per original variable, constants, every extension AND gate with its actual signed operands, and the required NOT vertices for signed values. Include unused extensions and roots. Repeated wires give one adjacency for treewidth, but their operand occurrences remain in the gate description. The treewidth of the underlying undirected graph G is at most two. This is a promise on the full value graph, not just the final output cone, the ER inference graph, or an arithmetic representative graph. Its number of vertices is O(T). The complete source encoding supplies the graph and all root associations; a decomposition need not be supplied.

## Conclusion

There is a deterministic polynomial-bit-time construction of all L037 supplied data. They retain every required abstract value, all original names and axioms, and have S=O(T), x-only affine-ABP representatives r_i, exact original/constant roots, exact signed wrappers 1+r_a, and affine-ABP relations H_i satisfying the formal identities

    H_i(x,0)=0,       H_i(x,A(x))=r_i+r_a r_b

for every extension definition i with signed operands a,b. All representatives are faithful on every original Boolean assignment. Only original Boolean and commutator placeholders occur in H_i. Before axiom substitution their degrees satisfy

    d=max(1,n),       h=max(1,2n−1).

One fixed polynomial in T bounds the aggregate full binary encoding E_ABP, including every separately written representative and H root, all graph labels/references, the full original-axiom dictionary and root associations. More explicitly, the construction obtains one common variable order and complete diagrams of width w≤C(T+2)^c for absolute constants C,c. With B=T+n+2, v=w+2 and

    R=B(n+1)^2 v^3+n^2+1,

the ABP data and auxiliary paired-product graphs have O(R) total graph records and

    E_ABP=O(R(T+log(R+2))+T^3).

Construction time, including compilation, is polynomial in T; the displayed size bound does not claim to bound the compiler's running-time exponent. L037 consequently supplies a polynomial-full-bit original-axiom affine-ABP certificate from this restricted class of supplied ER refutations.

This is a specialization under the prior SPECIALIZE assessment `drafts/literature/2026-10-16-treewidth-two-extension-data.md`. The two interfaces below are local progress beyond the inspected single-output compilation statement, without certified originality. The separate step-274 informal critical audit below found no substantive defect within the stated hypotheses; it changes neither the theorem nor its bounds. No unrestricted ER representation, formula-only certificate bound, ER boundedness, W/V/U, or SAT decision/separation conclusion follows. This is not a main-problem candidate.

## Proof

**Imported inputs and the precise difference.** Use Amarilli–Bourhis–Senellart, *Tractable Lineages on Treelike Instances: Limits and Extensions*, arXiv:1604.02761v1 (10 April 2016), Definition 6.4 and Lemma 6.6, PDF pp.15–16, with Appendix A pp.28–29 ([inspected long version](https://pierre.senellart.com/publications/amarilli2016tractable_long.pdf)): for each fixed circuit treewidth k, a single-output Boolean circuit C has an equivalent OBDD constructible in time O(|C|^c), with c depending only on k. Gates are Boolean AND/OR/NOT with shared input vertices. We use only polynomial, not constant, width. Its proof uses Jha–Suciu, *On the Tractability of Query Compilation and Bounded Treewidth*, ICDT 2012, Corollary 2.14 and section 4 ([author PDF](https://homes.cs.washington.edu/~suciu/file38_paper.pdf), PDF pp.6–7,9), whose decomposition-induced residual bound is polynomial for fixed treewidth.

For completion in a prescribed order use de Colnet–Ordyniak–Szeider, *OBDDs, SDDs, and circuits of bounded width: Completeness matters*, Artificial Intelligence 351 (2026), 104458, Proposition 2, PDF pp.3–4 ([published PDF](https://eprints.whiterose.ac.uk/id/eprint/234745/9/1-s2.0-S0004370225001778-main.pdf)). Completion takes O(n|B|) time and at most n times the old width. No OBDD-to-pathwidth converse is used. These exact inputs and their relevant proof cases were inspected in the prior assessment; they are reused without a new literature search.

For arithmetic graphs use the disjoint serial/parallel composition of Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative Models*, Definition 1/Lemma 2 Step 1, author manuscript pp.4–5 ([PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)). Its role is composition of independently supplied graphs. Neither it nor bounded-treewidth Boolean compilation converts arbitrary arithmetic circuits to ABPs. The new applicability steps here are a single-output selector construction for a common all-root order, and explicit graphs for L026's particular recurrences. L026's formal identities and ordered-multilinear bridge are reused, not reproved as new results.

**A small decomposition can be found directly.** Put m=|V(G)|. If m=0 add an isolated constant vertex, costing O(1). A nonempty graph of treewidth at most two has a vertex of degree at most two: in a width-two tree decomposition remove any leaf bag contained in its neighbor until none remains or there is one bag. In the latter case the graph has at most three vertices. Otherwise a leaf bag has a vertex absent from its neighbor, hence absent from every other bag by connectedness of its occurrence bags. All its neighbors lie in that bag of size at most three.

Eliminate any degree-at-most-two vertex u, adding the edge between its two neighbors if needed. This preserves treewidth at most two. With two neighbors a,b, the resulting simple graph is exactly the minor obtained by contracting ua; with at most one neighbor it is just deletion. Minor monotonicity here has an elementary decomposition proof: for contraction replace u by a in every bag. Bags do not grow, and the occurrence subtrees of u and a join at a bag covering ua, so the bags for a remain connected. Vertex deletion is immediate. Thus scanning for a degree-at-most-two vertex never gets stuck under the promise. At most m eliminations and O(m^3) elementary adjacency work suffice, even with naive arrays.

Reverse the recorded eliminations. Attach the new bag {u}∪N_later(u) to a bag containing N_later(u): for two neighbors their fill edge is present and covered by a current bag; for one neighbor some bag contains it; for no neighbors attach arbitrarily, or start the decomposition. This preserves coverage and connectedness. There are at most m bags, of size at most three. Root this tree and replace any node with many children by a binary tree of copies of its bag. This takes O(m) bags because the sum of original child counts is O(m); original occurrence subtrees stay connected. All subsequent construction is explicit and polynomial in m and the input bits.

**One output that selects every original root.** In the binary decomposition choose, for every original graph vertex u, one bag containing u as its owner. A bag owns at most three vertices. Introduce a fresh independent Boolean selector q_u and the gate h_u=q_u AND u at that owner. Selectors are distinct from originals and from axiom placeholders; they will be removed before the arithmetic construction.

At each bag t, aggregate its at most three owned h_u and at most two child aggregate outputs. If these are a_1,...,a_j with j≤5, create a fresh constant z_(t,0)=0 and fresh binary OR gates z_(t,l)=z_(t,l−1) OR a_l for 1≤l≤j. Let o_t=z_(t,j), including the j=0 case. The root aggregate o_root is the new circuit output. Every original gate is retained and has a path through its own h_u to the output, including unused roots and disconnected components of G. The original graph is acyclic; selectors feed only h, and the aggregate edges run upward through the decomposition. Nothing feeds back into G. Thus the enlarged circuit is an acyclic single-output circuit, of O(m) vertices.

Enlarge each bag by its owned q_u,h_u, its child outputs o_child, and its own constant/OR chain. There are at most

    3 + 2·3 + 2 + (1+5) = 17

vertices per enlarged bag, so the new treewidth is at most 16, independently of m. All original edges are covered by the original bags; each selector/AND and local aggregation edge is covered in its owner's enlarged bag; an edge out of a child output is covered in the parent's bag. Original vertex occurrence subtrees remain connected. Every fresh selector, h gate and nonoutput chain gate occurs in one bag, while each nonroot aggregate output occurs in its own bag and its parent, which are adjacent. This verifies the decomposition, including bags owning no vertex and components with no original edge. There is no vertex identified between distinct fresh aggregate outputs, even when j=0 or j=1.

As a Boolean function the new output is

    g(x,q) = OR_(u in V(G)) (q_u AND f_u(x)),

where f_u is the actual value of u in the retained Boolean DAG. Apply the imported single-output compiler at the fixed width bound 16. It gives one polynomial-size OBDD B_g in one order on the n originals and m selectors. Unused inputs, if omitted from its written order, can be inserted arbitrarily to extend it to a total order. This changes no Boolean function.

For each u, set q_u=1 and every other selector to zero in that same B_g. Bypass each fixed-selector test along its prescribed successor. Acyclicity makes bypassing well defined; no new branching or vertices are required. The resulting diagram computes f_u, and all remaining tests follow the restriction of the same order to original variables. Fill omitted original tests in that induced order using Proposition 2. More directly, every skipped-level edge can be replaced by a chain of redundant tests with identical two successors; there are O(n) new records per old edge, including root/terminal gaps. Thus each complete diagram has polynomial size and width, even when its own cone omits most originals. There are O(T) roots, so their aggregate written size is polynomial in T. In particular one fixed bound w≤C(T+2)^c holds for every completed diagram. The constants absorb the fixed compiler width, completion, and dense-to-original label bookkeeping. No root-specific decomposition order was chosen.

Fresh selectors are now gone. Keep positive extension diagrams, and use L026's terminal complementation for auxiliary signed diagrams, together with its trivial original-variable and constant diagrams. All are complete in that one original-variable order y_1,...,y_n, with width at most v=w+2. Actual signed representatives will be graphs for the exact expression 1+r_a. L026 proves that the auxiliary signed-diagram polynomial is precisely this expression in the free ring. Its diagram promises hold because f_i=f_a AND f_b on every original assignment in G, with repeated/signed operands retained.

**Explicit value and earlier-variable graphs.** Put q=(n+1)v; this q is a numerical size parameter, not a selector. Each individual positive, signed or trivial diagram has O(q) states and edges. For every state u at level j, insert affine edges 1+y_j and y_j to its two successors. Add one fresh final sink ω, a 1-edge from the terminal of value 1 to ω, and no edge from the terminal of value 0 to ω. From any designated state the path-sum is exactly L026's representative recurrence (4). Different terminals or repeated successors retain their multiplicities; parallel edges are allowed. This graph has O(q) records, with no output-path unfolding. Independent copies give every required positive representative; originals and constants can instead use their exact one-edge or zero graphs. An actual signed root uses disjoint sum branches for 1 and the representative being complemented. Only one complement per underlying unsigned value is needed by the signed-literal syntax, so these copies are still O(Bq) in total.

Fix one diagram and an earlier variable y_k. For states u at levels j>k build a K region containing vertices κ_u, together with one disjoint value region of the preceding kind. From κ_u place edges labeled 1+y_j and y_j to κ_(u_0),κ_(u_1), and two edges labeled c(k,j) to the corresponding value-region states u_0,u_1. Here c(k,j) is the pair-once original commutator placeholder for the distinct originals y_k,y_j, independent of their identifier order. K terminal vertices have no outgoing edge to ω. The value region has no edges back to the K region.

This graph is acyclic: levels strictly increase in each region and a path can change region only from K to value. Its path-sum from κ_u obeys exactly L026 (6):

    K_(u,k)=(1+y_j)K_(u_0,k)+y_j K_(u_1,k)
               +c(k,j)(r_(u_0)+r_(u_1)).

K terminals compute zero. Thus it computes the identical formal polynomial of that recurrence, with O(q) records for any chosen root, even if one keeps other unreachable states. No earlier K graph is recursively copied. A fresh entrance with two 1-edges into a copied value region likewise supplies any suffix sum r_(u_0)+r_(u_1) in O(q) records; coincident successors retain two separate edges and cancel correctly over F₂. At terminal suffixes, the K graph is simply zero and all value sums are field constants. These are complete independent graph inputs for the next construction.

**Explicit paired-state W graphs.** Fix one extension's two auxiliary signed operand diagrams U,V. There are at most p=O((n+1)v^2) same-level state pairs. Use a vertex ζ_(u,v) for each pair. At nonterminal level k put affine edges e_0=1+y_k and e_1=y_k to ζ_(u_0,v_0) and ζ_(u_1,v_1). Terminal pair vertices have no outgoing edge. Introduce a fresh final sink Ω. At each nonterminal pair append disjoint serial/parallel blocks for the following three summands, each entered from that pair vertex and exiting only to Ω:

    e_0 K_(u_0,k) (r_(v_0)+r_(v_1)),
    e_1 K_(u_1,k) (r_(v_0)+r_(v_1)),
    b_(y_k) (r_(u_0)+r_(u_1)) (r_(v_0)+r_(v_1)).

The factors are the independently constructed O(q)-record graphs above; e_0,e_1,b_(y_k) are single affine edges. Use a fresh copy for each displayed occurrence and unit connector edges. Internal local blocks are disjoint from all pair vertices, from other blocks, and from Ω. There are constantly many factors per block, so the records used at a pair are O(q). The entire graph has O(pq)=O((n+1)^2 v^3) records.

A path can remain in the pair region only while its level increases. Once it leaves into a local block it can only exit to Ω, never reenter the pair region or another block. Each block is acyclic with a designated sink having no outgoing internal edge. Consequently the whole graph is acyclic, and every accepting path has a unique first exit from the pair region. Finite distributivity, with left-to-right labels unchanged, gives the exact recurrence

    W_(u,v)=(e_0 K_(u_0,k)+e_1 K_(u_1,k))(r_(v_0)+r_(v_1))
              +b_(y_k)(r_(u_0)+r_(u_1))(r_(v_0)+r_(v_1))
              +e_0 W_(u_0,v_0)+e_1 W_(u_1,v_1).

This is L026 (8), including its zero terminal case. The recursive W terms are realized by pair-to-pair edges, not copies of child W graphs. The K-containing terms use only independently built K graphs; K has no W dependency. Therefore there is neither two-sided recursive witness growth nor circuit-valued edge labels. The paired-product recurrence P in L026 (7)–(8) also has an O(p)-record graph: keep the same pair edges and give each terminal pair a unit edge to its fresh sink exactly when the product of its two terminal values is 1. These P graphs are auxiliary and included in the ledger below.

**Formal identities, signs and degrees.** Induction backward in level establishes that the graphs just described compute the identical value, K, P and W polynomials in L026, before any axiom substitution. Hence L026 (5), (9) and the ordered-multilinear output identification apply verbatim. In particular P at the operand roots equals the independently supplied output representative in the free ring, because both are increasing multilinear polynomials in the same order and have equal Boolean evaluations. This is the specific injective subspace from L026, not an inference from Boolean equality for arbitrary noncommutative polynomials. With H_i the W graph at the operand-root pair, the two required H identities follow. No original clause axiom or extension placeholder is used in H.

For exact signed nodes write the actual disjoint graph for 1+r_a. L026 proves equality with the signed auxiliary diagram used in each W construction, so there is no missing sign-translation witness. Original roots stay x_j and constants stay their field values, even if their auxiliary diagram has redundant levels. L026's degree induction gives d=max(1,n) and h=max(1,2n−1) for the identical polynomials; the graph realization does not change either polynomial. One can also check the path degrees: value paths use at most one affine factor per remaining level, K switches once to a value suffix, and a W path leaves after some initial prefix for one local correction of degree at most twice its remaining suffix length minus one. This never exceeds 2n−1 from the full root. Zero terminal graphs introduce no empty accepting path. Repeated operands, equal successors, complementary operands and constants require no alteration of the recurrences.

If n=0, skip Boolean compilation entirely: topologically evaluate every node of G as a field constant, retain exact signed wrappers and set each H_i to the distinct-endpoint zero graph. The scalar relation r_i+r_a r_b is zero. This satisfies the same bounds with d=h=1 and any w≥1. Unused roots are still written. The presence of an original empty clause changes none of these supplied-data constructions or the eventual L037 applicability.

**One aggregate full-bit ledger and downstream use.** The common-order family has O(B) diagrams, O(Bq) records and O(B) required value roots, including original/constants and exact complements. There are at most T extensions. Write each H_i as its own complete graph, with all its pair vertices and independent local blocks. This costs O(T(n+1)^2 v^3) records, and writing each auxiliary P graph adds O(T(n+1)v^2). No sharing between different output files is credited. A fixed diagram/earlier-variable K region can be built in O(q); constructing every such reusable template costs O(Bnq), already below R, while the copies placed inside every H_i have already been charged separately. These templates are temporary, not an uncharged oracle or implicit edge label. The final output consists of the separately rooted r_i and H_i; exporting every internal K state as an additional separate file is not required or claimed by this bound.

All actual abstract nodes and their source associations contribute O(B) more records. The original alphabet and Boolean/commutator positions contribute O(n^2), including unused entries. Thus the aggregate graph-record count is O(R) as stated. Each affine edge has at most two nonzero scalar/symbol terms. Dense graph/state references cost O(log(R+2)) bits; retaining original names or axiom positions and source associations costs at most O(T) per occurrence. The original full ordered axiom list and dictionary cost O(T^3), by L025's receiving convention, and are explicitly retained even though clause placeholders are unused by H. This proves the displayed E_ABP bound; it also covers all input diagrams, terminal labels, common-order names and separate root framing. Arithmetic graph construction is a polynomial number of copies, loops over states/pairs and binary writes. It never enumerates complete diagram paths, extension ancestry paths, truth tables or free words.

Boolean graph construction and decomposition take polynomial bit time; single-output compilation takes a fixed polynomial since width 16 is fixed; all selector restrictions and completions cost a further polynomial. Substituting n≤T and w≤C(T+2)^c into R and E_ABP gives one fixed polynomial in T for the entire supplied collection. Thus S,d,h,E_ABP meet L037's exact receiving hypotheses. Applying its already proved conditional assembly yields the asserted restricted original-axiom affine-ABP certificate. L025 is used for the receiving conventions and axiom accounting, L026 for formal suffix identities, and L037 only after the complete data have been constructed.

Attempts 019–021 do not contradict this conclusion: the unrestricted HWB promise, arbitrary degree-controlled circuits and L025's prescribed two-sided pair table are not the inputs being converted here. No small treewidth is asserted for an arbitrary supplied ER proof, no decomposition claim is made about the compiled arithmetic graphs, and a short restricted certificate is not a deterministic polynomial-time SAT decision procedure. The proof is all-size and informal; no implementation, finite certificate test or separate critical audit was performed in this step.

**Separate critical audit — step 274, 2026-10-17.** This audit uses the
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-17-treewidth-two-data-critical-audit.md`. It checks
the construction against L025, the complete L026 proof and L037's receiving
hypotheses. The preceding statement that no separate audit was performed
describes the original construction step, not this later audit. The
following are all-size proof checks, not finite experimental evidence.

For elimination, the only possible new edge after contracting ua is ab:
u has exactly those two neighbors. Thus the remaining graph is precisely
the filled elimination graph, including when ab was already present.
Replacing u by a in the bags preserves connectedness because their two
occurrence subtrees intersect at an edge-covering bag. In reverse order,
the later-neighbor set is a clique of size at most two, hence lies in one
current bag. Attaching the new bag there preserves each neighbor's
connected occurrence set. Isolated vertices attach without a condition.
Duplicating branching bags uses only linearly many copies and preserves
the same connectedness. This verifies the decomposition algorithm rather
than assuming it is part of the input.

In the selector circuit, assign owners after binarizing the decomposition.
Each bag owns at most its three original vertices. Its added vertices are
at most six selector/AND vertices, two child outputs and six chain vertices.
These, with its original three vertices, account for all 17 positions.
An original vertex u need not be owned by every bag containing it: its
only new outgoing edge uh_u is covered at its single owner, which already
belongs to its connected occurrence subtree. Each fresh aggregate output
occurs only in its bag and the parent bag; even a zero-child/zero-owner
output is a fresh constant, so this occurrence description remains true.
Other fresh vertices occur once. Gate edges, selector edges and child-to-
parent edges therefore all have covered endpoints and connected bags.
Every original gate reaches the new output, but no aggregate or selector
feeds an original gate, so this reachability introduces no directed cycle.

The single compiled order is fixed before any selector is assigned.
Bypassing fixed tests only deletes positions from that order. Assigning
exactly one selector to 1 gives precisely the chosen original vertex's
function, regardless of other gates' values or original unused roots.
Redundant original-variable tests fill every skipped level, including
before the root and after an early terminal. Their equal successors are
retained, so a constant function still has a complete diagram. Completion
costs O(n) records per old edge/root gap; the old outdegree is at most two.
Multiplication by O(T) roots remains polynomial. These checks establish
the simultaneous common-order hypothesis required by L026, rather than
using independent per-root compilation orders.

The value graph has the exact two affine transitions of L026 (4), and
only the terminal labeled 1 has a unit edge to its fresh sink. For K, an
accepting path must switch exactly once from a kappa vertex to a value
vertex on c(k,j); paths ending in a K terminal cannot accept. Splitting
by the first outgoing edge gives precisely (6), including two separately
counted c-edges when successors coincide. For W, an accepting path has a
unique exit from the pair region into one of its three local blocks.
Serial composition in that block gives the displayed ordered factor
product; parallel composition adds the two eK terms. The pair edges give
only the two recursive left multipliers. No local block reaches a pair
vertex or a different block. Consequently its first-edge recurrence is
exactly L026 (8), and terminal pairs compute zero. P uses the same pair
transitions but accepts exactly terminal pairs whose two bits multiply to
1, giving (7) and the P recurrence. This verifies equality of the graph
polynomials before substitution; scalar agreement alone is not used.

The auxiliary signed diagrams complement terminal labels, giving exactly
1+r by L026's induction. The separately written actual signed graphs
compute that same sum. Hence replacing either signed operand in the W
identity is formal substitution of an equal polynomial. The output-root
identification uses only L026's increasing-multilinear injectivity. All
labels remain original x or original Boolean/commutator placeholders;
selectors and extension names are absent from the arithmetic alphabet.
Repeated/equal successors retain their multiplicities, complementary
operands do not require new identities, and disjoint sum endpoints prevent
an unintended empty accepting path. The n=0 branch evaluates scalars and
uses distinct-endpoint zero relations, so it does not require a commutator
for a nonexistent variable or an OBDD with positive depth.

For an independent degree check, a value path over s remaining levels has
degree at most s. A K path takes some affine prefix, one placeholder edge
and the remaining value suffix, with total degree at most s. A W path
first traverses n−s pair levels, then enters a local block of degree at
most 1+2(s−1)=2s−1. Its total is at most n+s−1≤2n−1. Zero-terminal K
branches contribute no paths. Unit connectors add no degree. Thus the
claimed bounds hold even before any cancellation, with n=0 separately
covered by d=h=1. Exact original and signed wrappers satisfy d as well.

Finally let q=(n+1)v and p=O((n+1)v²). One local correction block uses a
constant number of O(q)-record factors, each independently copied; all
copies inside one H cost O(pq). Summing over at most T extensions gives
O(T(n+1)²v³). The other charges are O(Bq) for all signed/base/value roots,
O(Tp) for auxiliary P graphs, O(Bnq) for optional K templates, and
O(B+n²) for associations and alphabet positions. Every one is absorbed
by the stated R. In particular, roots of K used in different H blocks
do not share an uncharged graph, and the absence of per-path unfolding
is a proved property of the directed construction.

The aggregate encoding uses one explicitly written original-axiom
dictionary, referenced by all separately written graphs. This is permitted
by L037's collection-level framing; it is not an implicit external input.
Copied correction blocks contain complete graph records and symbol
references, not copies of the full dictionary. Thus there is one O(T³)
dictionary charge, while every symbol/reference occurrence is included in
O(R(T+log(R+2))). Independent output renumbering, parallel-edge records,
common-order names and source associations have already been counted.
The displayed bound does not promise that redundantly repeating the whole
dictionary in every file is free. This specifies the existing aggregate
encoding convention without changing the bound. Compilation time can have
a larger fixed exponent than this output ledger, as the conclusion states.

All L037 receiving hypotheses are therefore met on the promised class.
The audit finds no substantive defect or needed theorem/bound repair.
It verifies the existing restricted input, without a stronger structural
theorem, certified novelty, implementation, or unrestricted SAT consequence.
Attempts 019–021 still concern different promises or prescribed outputs.

## Mathlib

Full matching theorem, selector construction, free-algebra ABP realization and binary ledger: **not checked**; no absence claim. The exact primary supporting citations are the compilation, completeness and graph-composition results given above. Their hypotheses are applied explicitly, and none is claimed to contain the complete all-root/formal-witness theorem. Classification: POTENTIALLY_NEW under SPECIALIZE, meaning only that the prior comparison did not identify a full matching result; known compilation and graph composition are imported rather than claimed as discoveries.

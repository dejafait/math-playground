# L089 — Single-variable-move OBDD product witnesses

## Hypotheses

Work in the free associative algebra F₂⟨y₁,…,y_q⟩. Supply two explicit
dense deterministic OBDDs D,E over the same listed alphabet, each of
nonterminal width at most three, in orders π,ρ. Each nonterminal state
has one bit-0 and one bit-1 edge to the next level; only level q+1 has
scalar terminals 0 or 1. Repeated successors, redundant tests, unused
states and multiple terminals of either value are allowed and encoded.
Each diagram has a designated first-level root; for q=0 it is a terminal.

Define the exact ordered representatives separately in their own orders
by r_u=(1+z)r_(u,0)+z r_(u,1), with the supplied terminal scalars.
Put f=r_D and g=r_E. Assume fg(a)=0 for every Boolean assignment a.
The orders differ by deleting one named variable and reinserting it
elsewhere, preserving the relative order of every other variable.
Either direction and zero displacement are allowed.

Use exactly L087's original pre-witness M: 2 plus the full binary lengths
of both diagrams, both orders, the original-name dictionary and complete
Boolean/commutator axiom and placeholder dictionaries, including axiom
words and framing. Set B=(y_i²+y_i, y_i y_j+y_j y_i : i<j), in those
fixed positions, with placeholders σ_i,τ_ij. Neither a sought witness
nor its degree contributes to M. Output graphs must be explicit acyclic
affine-F₂ ABPs, with full names/references, not implicit graphs or
circuit-valued edges.

## Conclusion

A deterministic polynomial-bit-time construction on these promised inputs
produces H over the original variables and these placeholders, satisfying
the formal identities

    H(y,0)=0,                 H(y,B(y))=fg.                 (1)

For one absolute K its complete encoding has at most K(M+2)^5 bits.
Its pre-substitution path degree is at most max(1,2q−1). The construction
does not test the Boolean-zero promise. No intermediate-width promise
is supplied: the width bound used below is proved for this construction.

This is an informal restricted specialization. The separate step-347
critical audit below finds no substantive defect, with no certified
originality. It extends the single-move case
beyond L088's logarithmic adjacent-distance restriction. It establishes
neither arbitrary-order W₂, diagram or witness availability for arbitrary
ER data, nor any unrestricted SAT or P-versus-NP conclusion. Attempt 030's
independent availability obstruction is unchanged.

## Proof

**Coverage and precise imports.** The pre-invocation SPECIALIZE assessment
is `drafts/literature/2026-10-19-single-variable-move-obdd-construction.md`;
its completed comparison is in the companion single-variable-move witness
assessment. Randal E. Bryant, *Graph-Based Algorithms for Boolean Function
Manipulation*, IEEE TC 35(8), 677–691 (1986),
[author-restored copy](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
§4.2 pp.10–11/Figure 4 and §4.4 p.15, supplies structural child-pair
sharing and cofactor reference redirection, including the root. Richard
Rudell, *Dynamic Variable Ordering for Ordered Binary Decision Diagrams*,
ICCAD 1993, 42–47,
[primary scan](https://www.larshj.dk/PUMA/references/Dynamic%20variable%20ordering%20for%20ordered%20binary%20decision%20diagrams%20-%20p42-rudell.pdf),
§4.1 p.44, supplies the local four-cofactor swap. His §4.3 p.45 search
cutoff is not an all-position size theorem and is not used as one.

Import the audited exact single-swap correction graph from L088, and
L026 (4)–(12), including its ordered-multilinear injectivity. Import only
L071's post-compilation value/K/W graph realization and its audited
copying interface, not its treewidth-two compilation theorem. These
give formal graphs from already supplied diagrams. The new obligations
here are the bounded state descriptors throughout one move, exact
reception of their merges, the two factor orientations, and the original-M
aggregate ledger. The argument below proves those specializations; it
does not reprove a general OBDD reduction or commutation theorem.

**Exact preprocessing and the choice of direction.** Redirect every
terminal reference to one of two canonical terminal vertices according
to its scalar value. Keep both canonical terminals, even if one is unused.
For q=0 also redirect the designated root. Retain all nonterminal states
and every bit edge individually. Backward induction in the representative
recurrence proves that each original nonterminal/root polynomial is
unchanged: the terminal value and then each of the two ordered summands
are identical. Thus this preprocessing preserves f,g in the free ring,
not merely on Boolean assignments. Its work and original archived input
are charged in M. Each normalized diagram has at most 3q+2 states.

If the orders agree, use the common-order construction below directly.
Otherwise there are lists A,Z,C and a variable x, with Z=(z₁,…,z_d),
d≥1, such that one order is A,x,Z,C and the other is A,Z,x,C. To find
such data, try every named x, compare the two lists with x deleted,
and compare the positions of x. This is polynomial work on the supplied
orders; the hypothesis guarantees a successful choice. Choose the
diagram in which x is earlier and move x right across Z. Consequently
we only need a right-moving construction, even when transforming E to
D's order would have been a left move. Which factor changes will be
handled explicitly below, without interchanging f and g.

**The state invariant for a right move.** Let Q be the chosen normalized
diagram with original order A,x,z₁,…,z_d,C. Let V_t, for 0≤t≤d, be
the set of original Q states at the level immediately following x and
the first t variables of Z. Thus V_t tests z_(t+1) for t<d; V_d is
at the first level of C, or consists of the two canonical terminals
if C is empty. Every V_t has at most three states, except the terminal
case which has two. Write δ_b(v) for the original bit-b successor at
a nonterminal level.

Construct Q_t with order A,z₁,…,z_t,x,z_(t+1),…,z_d,C. Start with Q₀=Q.
Maintain these structural assertions:

- Every state at the current x level has its bit-a edge pointing directly
  to some u_a in the original set V_t. Tag this state by the ordered
  pair (u₀,u₁). At t=0 there are at most three x states, possibly with
  duplicate tags; for t≥1 there is at most one x state for each tag.
- The part strictly after x is the unchanged original suffix beginning
  at V_t, with all its states and transitions. Levels in A are unchanged
  except for reference redirection at their last boundary. Each crossed
  z level has at most nine states. All references still go to the next
  level, and the designated root is explicitly retained or redirected.

The assertions hold at t=0. Suppose t<d. At the x level let u have
tag (u₀,u₁), where u_a is an original z_(t+1) state. Apply L088's raw
dense swap at x,z_(t+1): u now tests z_(t+1), and its bit-b successor
is a fresh x state (u,b) with bit-a successor δ_b(u_a) in V_(t+1).
Delete the old V_t level from this particular reordered diagram, as in
the raw swap. Density ensures that all its incoming edges have just
been replaced. All deeper original suffix levels remain unchanged.

Merge these new x states if and only if they have the identical ordered
pair of successors

    (δ_b(u₀), δ_b(u₁)) ∈ V_(t+1) × V_(t+1).             (2)

Redirect each incoming bit edge separately to the chosen representative
of its class. Keep parallel edges and their labels, including both bit
edges of a parent when their new endpoints coincide. No nonterminal
level is bypassed, even when both children are equal. The newly crossed
z_(t+1) level contains exactly the former x states, hence at most nine
(at most three at the first swap). The merged x level has at most
|V_(t+1)|²≤9 states. This proves the structural assertions for t+1.
All states at unchanged original levels, including unreachable states,
remain included. Only the stated swap deletion and explicit merges are
performed; no hidden reachable-state or semantic minimization bound is used.

**Why the merge is exact in the free ring.** In the raw diagram, two
new x states merged by (2) have literally the same successors p₀,p₁,
in the identical unchanged suffix. Their representatives are both

    (1+x)r_(p₀)+x r_(p₁).                              (3)

Replace each incoming reference by that same polynomial. Induct upward
through every preceding level: each bit-labeled ordered summand is
unchanged, so every preceding state polynomial, and in particular the
root, is unchanged. This also covers shared prefix paths; it never
counts or unfolds them. Two different edges with equal endpoints still
contribute two summands. No equality of Boolean functions is used in this
merge, nor is a variable moved through a prefix or a suffix. The x level
after a right swap is not the root; if x was originally the root, that
same root vertex now tests z₁, and the preceding argument still applies.

The induction proves a uniform intermediate bound. Every Q_t has at
most 9q+2 states. A raw diagram between Q_t and Q_(t+1) has at most
18 states at its new x level, at most nine elsewhere, and two terminals,
so has at most 9q+11 states. In particular all snapshots, raw diagrams,
tag lists and transition lists together have O((q+1)²) records, since
d≤q−1. This bound is independent of d in its exponent. It replaces
L088's loose factor-three iteration, not its exact swap identity.

**Correction reception and telescoping.** Write h_t=r_(Q_t), and let
the raw swapped root be h'_t. L088's audited local graph C_t, constructed
from Q_t before any merge, has O(q+1) records and satisfies

    C_t(y,0)=0,          C_t(y,B)=h_t+h'_t.             (4)

This use of L088 is only its single-swap component, which has no distance
or width restriction. Explicitly, it retains the old prefix, replaces
the swapped block at each boundary u by four τ_(x,z_(t+1)) edges to
the four original grandchildren, and retains their suffix graph.
Repeated grandchildren receive repeated edges. The edge labels come
from the original B dictionary in either original-name orientation.
All accepting paths cross one such edge and never return to the prefix.
L088 proves the exact root identity using these ordered prefix and suffix
regions, with degree at most q−1. We have not replaced this graph by
a quotient of its prefix paths or assumed equality of Boolean functions.

The exact merge argument gives h'_t=h_(t+1). Thus the disjoint parallel
sum J of all C_t has O((q+1)²) records and satisfies

    J(y,0)=0,           J(y,B)=h₀+h_d.                  (5)

The cancellation is additive, with each intermediate root occurring
twice. No previously built witness is substituted into a later one.
Fresh entrances/exits and unit connectors implement the sum with distinct
endpoints. Its degree is at most q−1. For zero displacement take J=0
with distinct endpoints and no path, and leave both diagrams unchanged.

**Common-order reception and both original-factor orientations.** After
the move let the two diagrams, in their original factor positions, have
representatives F,G. They have a common order, one normalized width at
most three and the other width at most nine. Every swap preserves the
Boolean function (the two bit choices reach the same grandchild), and
every merge preserves its formal root. Hence FG vanishes on Boolean
assignments. The synchronous pair representative P from L026 (7)–(8)
is increasing multilinear in this common order and computes that
pointwise product. L026's injectivity on this precise subspace gives
P=0 in the free ring.

The imported L026/L071 graph W therefore has

    W(y,0)=0,           W(y,B)=FG+P=FG.                 (6)

It uses the actual ordered operands F then G; no commutation of whole
operands is performed. If E was moved, then F=f, G=h_d, h₀=g, and take

    H=W+fJ.

Equations (5)–(6) give H(y,B)=fG+f(g+G)=fg. If D was moved, then
F=h_d, G=g, h₀=f, and take instead

    H=W+Jg.

Now H(y,B)=Fg+(f+F)g=fg. Both choices vanish at zero placeholders.
Only one original x-only factor is copied for the serial branch; it
is placed on the indicated side of J. Disjoint internal vertices and
fresh sum/product connectors give exactly these ordered polynomials.
Thus a movement in either direction is covered without a separate
left-moving state invariant or an unproved factor swap.

When q=0 the roots are scalars and the promise says fg=0; output the
distinct-endpoint zero graph. When q=1 or the orders agree, no swap is
needed and (6) alone gives (1). Constant functions, redundant tests and
terminal pairs of either scalar value need no semantic simplification.

**One complete original-input ledger.** The original input/archive and
normalization maps cost O(M) records and bits up to a fixed polynomial;
there are at most M encoded original states and names. All normalized
and raw move snapshots and all independently copied C_t graphs cost
O((q+1)²) records, as proved above. At the common-order stage there are
at most 27 same-level nonterminal pairs per level and four terminal
pairs. Each local W exit has a constant number of independently copied
value/K/suffix-sum factors of O(q+1) records, using precisely L071's
post-compilation construction. Pair transitions move only to later
pairs; an exit block never returns. Consequently the full W graph,
including every independent local block, has O((q+1)²) records.

This count applies in either operand orientation. For example if the
width-nine diagram is first, its K graph has a K region and one value
region, each O(q+1); it is not copied once per path. The auxiliary P
graph has O(q+1) records. Optional K templates for each earlier variable,
all graph endpoints/connectors, the one extra original value factor and
J fit O((q+1)²) records. Retaining the original encoded inputs as well
gives at most C(M+2)² total records, since q≤M. The number of separately
written component copies is bounded by the same allowance. No reuse
across separate output files is credited.

Densely renumber each written graph. Each reference uses O(log(M+2))
bits with an absolute constant, and each affine edge has at most two
terms with bit coefficients. Even spelling each original variable or
placeholder in full costs at most M bits per occurrence. Repeating the
complete original B/name/placeholder dictionary in every component file
costs at most M times the component count, hence O((M+2)³) bits. The
orders, state tags, roots, level indices, scalar labels, parallel edges
and framing have the same bound; binary references add at most
O((M+2)² log(M+2)). Thus the final graph and all charged intermediate
copies fit O((M+2)³) bits under these conventions, and in particular
the deliberately loose absolute bound K(M+2)^5 in the conclusion.
M was fixed before constructing any witness or intermediate diagram.

All operations are finite loops over explicit states, pairs, edges and
dictionary entries. Even naive comparisons to merge identical pairs,
per-graph renumbering and sequential dictionary lookup take a fixed
polynomial in M. No reduction oracle, truth table, semantic-zero tester,
path enumeration, or recursively compounded polynomial exponent is used.

For degrees, every C_t path has at most q−1 affine/placeholder factors,
and the copied original value factor has at most q. The serial branch
has degree at most 2q−1. L071's audited graph realization of W has
pre-substitution path degree at most 2q−1 for q≥1: a path leaves its
pair prefix once for a local correction block with at most twice its
remaining suffix length minus one factors. Unit connectors add no
degree. The q=0 zero output meets the stated max(1,2q−1) convention.

These are all-size informal identities and counts. No executable graph
certificate, finite testing claim or independent critical audit is made.
The result supplies a restricted witness, not the representations for
arbitrary ER inputs or a conclusion about unrestricted SAT.

**Separate critical audit — step 347, 2026-10-19.** Reuse the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-single-variable-move-obdd-audit.md` and its
primary-source comparison. This audit is REPRODUCTION of the existing
argument. Bryant's child-pair sharing and Rudell's four-cofactor swap
are supporting Boolean operations, not external proofs of the following
free-ring reception or quantitative claims. The checked local imports
are precisely L088's audited single-swap graph, L026 (4)–(12) and
injectivity, L071's audited post-compilation value/K/W graphs, and
L087's original B/M convention. No Boolean compiler or treewidth theorem
is being applied to the intermediate diagrams.

First, replacing terminals by their scalar-labeled canonical vertices
preserves each terminal polynomial, then each nonterminal polynomial by
backward induction. Both bit-edge occurrences remain. For q=0 the root
itself is redirected; for q>0 no nonterminal is removed. Arbitrarily many
original duplicate terminals are paid in M before this normalization;
they need not fit the subsequent 3q+2 normalized-state bound. An unused
canonical terminal has no effect on any recurrence.

Deleting the named moved variable from the two orders leaves the same
list. The earlier and later positions therefore give exactly A,x,Z,C
and A,Z,x,C. Choosing whichever original factor has x earlier permits
right swaps throughout. This does not exchange the two factors of fg.
The choice can be found by comparisons of explicit lists; no test of
the represented Boolean functions is involved.

For an independent induction on t, the critical assertion is that the
children of every current x state are in the original set V_t, not in
a previously enlarged reordered level. At t=0 these are its original
successors. At the next raw swap, the child for bit b at the new z level
is an x state whose two children are exactly δ_b(u_0),δ_b(u_1) in the
unchanged original V_(t+1). Thus all raw x states are classified by
ordered pairs from V_(t+1)². Merging only equal pairs establishes the
assertion for t+1; the suffix beyond them remains original. In particular
no recurrence of the form “square the previous width” is needed.

The former x states become the newly crossed z level and have at most
nine states (three at the first swap). Earlier crossed levels keep their
states and can have only their last outgoing references redirected.
The part in A retains its state identities and transitions except the
allowed boundary redirection; no skipped-level edge is introduced.
The removed V_t level has incoming edges only from the old x level,
since the diagrams are dense. This remains true for unused states.
Hence its removal leaves no retained dangling edge or root. If the
swapped x was at the root, its same vertex becomes the new z root.
New x states are below that vertex and are never the designated root.

Equal successor pairs give literally equal ordered expressions (3).
Replacing each incoming reference by that expression preserves each
parent's two summands individually, then all preceding states by
induction. Shared parents and suffixes do not require path enumeration.
When the two parent edges now coincide in endpoint, they still retain
their separate labels and occurrences; neither edge is dropped or
replaced by a single edge. Equal x children also do not license bypassing
the x level. At the final crossing with C empty, V_d has the two
canonical scalar terminals, so the same argument applies. The width
bound actually drops to at most four x states there.

Each normalized snapshot therefore has at most 9q+2 states. The raw
swap has at most twice nine new x states, at most nine states at each
other nonterminal level, and two terminals, giving 9q+11. There are
d≤q−1 swaps, and every nonterminal has two edge records. Ordered-pair
tags have two state references each. Consequently retaining every raw
and merged snapshot, tag and transition list costs O((q+1)²) records.
The number of unused states is included in these estimates.

L088's graph is applied to the pre-merge Q_t. Its four boundary edges
are separately labeled by the one original τ for x,z_(t+1), and point
to the actual four grandchildren. Its boundary suffix after substitution
is (xz_(t+1)+z_(t+1)x) times the sum of their suffixes in that order.
The unchanged prefix propagates this exact difference on the left.
The graph has no boundary edge back into the old second level, and
every accepting path crosses exactly one placeholder edge. It therefore
computes h_t+h'_t after substitution and zero before it. Repeated
grandchildren and the scalar-terminal last swap are included. The merge
just checked gives h'_t=h_(t+1) formally, so disjoint summation yields
(5), with each intermediate h_t occurring twice. It substitutes no
previous correction into a later one.

For W, synchronous same-level pair states use the actual common order.
Their P recurrence selects the same Boolean bit in both diagrams and
produces an increasing multilinear polynomial in that order. The
Boolean-zero promise and the scalar-preserving swaps imply P(a)=0.
Only L026's injective increasing-multilinear subspace is used to conclude
P=0; neither fg nor the differently ordered h_0+h_d is put in that
subspace. L071's graph then implements the exact W recurrence (8) of
L026, with the first operand's K graph followed by the second operand's
suffix sum, and with the Boolean placeholder before both suffix sums.
The recursive pair edges are left multipliers and no local exit block
returns to the pair region. This verifies the needed factor order.

If the second input moves, substitution in W+fJ gives fG+f(g+G)=fg.
If the first moves, substitution in W+Jg gives Fg+(f+F)g=fg.
These cancellations use associativity/distributivity and characteristic
two, without a commutation of f and g. Each serial branch contains J,
which vanishes at zero placeholders, while W vanishes there separately.
Disjoint component interiors, sinks with no internal outgoing edges and
fresh unit connectors implement exactly these sums and ordered products.
For zero displacement J has no path; for q=0 the whole output has no
path and distinct endpoints. For q=1 the common-order construction alone
applies. No unwanted empty accepting path arises in any case.

For an independent copying check, the final widths are at most three
and nine, so there are at most 27 nonterminal pair states per level
and four terminal pairs. At each pair there are constantly many local
factor occurrences. A value or fixed-earlier-variable K graph has at
most two O(q+1)-record regions, independent of its number of paths.
Each occurrence is copied independently, even if two operands or
successors coincide. Thus all local W blocks together have O((q+1)²)
records, as do all snapshots and corrections together. The pair region,
P graph, J connectors and the one copied original value factor fit this
bound. Optional K templates for each of q earlier variables also fit:
one complete O(q+1)-record region per variable per final diagram suffices.
There is no required export of every K root as a separate full file.

Keeping individual corrections and factors as well as their copies in
J, the serial branch and H multiplies these counts only by an absolute
constant; W already pays its independent local copies. Including the
original archive gives O((M+2)²) total records and component occurrences,
using q≤M. Full original name/axiom/placeholder dictionaries cost at most
M bits per component, including unused entries, so repeating all of them
costs O((M+2)³) bits. Full symbol spellings per edge are also at most
M bits; each edge has at most two affine terms. Dense references and
tags cost O(log(M+2)) per occurrence. All remaining order, terminal,
root and framing records fit the same allowance. The resulting
O((M+2)³) estimate implies the stated absolute K(M+2)^5 bound without
including H or its degree in M. Naive state-pair comparisons and
dictionary scans still give polynomial bit time; no precise time
exponent equal to the output exponent is asserted.

Finally, a swap correction path has k−1 prefix factors, one placeholder
and q−k−1 suffix factors, hence degree at most q−1. Adding one original
value factor gives at most 2q−1. For W, suppose a path exits its pair
region with s≥1 remaining levels. It has at most q−s preceding factors.
Its local K exit has degree at most 1+(s−1)+(s−1), and its Boolean exit
has the same bound 2s−1. K terminals have no accepting path. The total
is at most q+s−1≤2q−1. Connectors have degree zero. These are actual
pre-substitution path bounds, not only semantic polynomial degrees.
The q=0 no-path graph satisfies the stated max convention separately.

The audit finds no substantive defect or needed hypothesis, identity,
degree or bound repair. It discharges the existing restricted all-size
audit obligations; it is not a new construction, executable verification
or certification of originality. Arbitrary-order W₂, general ER data
availability and unrestricted SAT remain unresolved. Attempt 030 is
unchanged and concerns independent representation availability.

## Mathlib

Full matching theorem, exact single-move sharing/correction reception and
full binary ledger: **not checked**. Unknown coverage is not evidence
of absence. The primary supporting algorithms are Bryant §4.2/§4.4
and Rudell §4.1 as cited above; the exact formal components are L026,
L071 and audited L088. The assessed Tzameret formula commutation result
does not supply shared-graph size bounds and is not used by unfolding.
Classification: POTENTIALLY_NEW under the saved SPECIALIZE assessment,
meaning only that the inspected comparison did not establish a matching
full result; no originality claim is certified. The separate step-347
audit above is REPRODUCTION of that construction under its own saved
SPECIALIZE assessment; it finds no substantive defect and adds no
Mathlib coverage claim.

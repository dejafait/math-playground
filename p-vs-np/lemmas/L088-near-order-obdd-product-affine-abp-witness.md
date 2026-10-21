# L088 — Polynomial affine-ABP witnesses for nearby-order OBDD products

## Hypotheses

Work over the free associative algebra F₂⟨y₁,…,y_q⟩. Supply two explicit
deterministic dense OBDDs D,E of nonterminal width at most three, on the
same listed alphabet, with orders π,ρ. Every state at level k has two
successors at level k+1; only level q+1 has terminals labeled 0 or 1.
Redundant tests, repeated successors, unreachable states and unreduced
diagrams are allowed and fully encoded. Each diagram has a designated
root at its first level (a scalar terminal when q=0).

Use L026's ordered representatives, separately in the supplied orders:
r_u=(1+z_k)r_(u,0)+z_k r_(u,1), with the stated scalar terminal values.
Let f=r_D and g=r_E. Retain their exact ordered product fg.

Use L087's full pre-witness input length M: 2 plus the binary lengths
of both diagrams, both orders, the complete original-name dictionary,
and the full Boolean/commutator axiom and placeholder dictionaries,
including words and framing. For the listed alphabet the axioms are
b_i=y_i²+y_i and b_ij=y_i y_j+y_j y_i (i<j), with placeholders σ_i,τ_ij.
Call the full substitution tuple B. Neither a witness nor its degree
contributes to M. All output graphs are explicit acyclic affine-F₂ ABPs;
implicit graphs and circuit-valued labels are excluded.

Assume the minimum adjacent-transposition distance d between π and ρ
is at most floor(log₂ M), and fg(a)=0 for every a∈{0,1}^q. Unlike
L087's hardness premise, distance zero is permitted. Intermediate
reordered diagrams need not have width three.

## Conclusion

There is a deterministic polynomial-bit-time construction, on these
promised inputs, of an affine ABP H using only y,σ,τ, with formal identities

    H(y,0)=0,                    H(y,B(y))=fg.

One absolute K bounds its full binary encoding, including the complete
dictionary, by K(M+2)^9. Its pre-substitution path degree is at most
max(1,2q−1). The exponent and K are independent of the input and d.
No semantic-promise tester is needed by the construction.

This is a restricted informal witness theorem. The separate step-342
critical audit below finds no substantive defect in its identities or
fixed bound. It is local progress under SPECIALIZE coverage, without
certified originality. It proves neither L087's arbitrary-order W₂ nor
general ER data availability, an unrestricted SAT consequence, or a
P-versus-NP candidate. Attempt 030's independent availability stop remains.

## Proof

**Sources and the specialization being made.** Reuse the pre-invocation
assessment `drafts/literature/2026-10-18-near-order-obdd-product-witness.md`.
Richard Rudell, *Dynamic Variable Ordering for Ordered Binary Decision
Diagrams*, ICCAD 1993, pp.42–47, §4.1 p.44
([primary scan](https://www.larshj.dk/PUMA/references/Dynamic%20variable%20ordering%20for%20ordered%20binary%20decision%20diagrams%20-%20p42-rudell.pdf)),
supplies the local Boolean cofactor swap. We specialize it to dense,
unreduced diagrams, retaining candidate children rather than relying on
reduction, hash tables, garbage collection or an unread sharp size bound.
The necessary new work is its exact free-ring correction and full-copy
ledger. Boolean preservation alone does not prove the displayed conclusion.

Import L026's ordered suffix identities (4)–(12) and its
increasing-multilinear injectivity. Import only L071's explicit
post-compilation value/K/W graph component and its recorded critical
audit; its treewidth-two Boolean compilation theorem is not invoked.
These components take already supplied common-order diagrams and contain
no treewidth premise. The following use neither reproves their general
identities nor substitutes an external Boolean-equivalence assertion
for a free-ring equality.

**One dense swap and its size.** Consider consecutive levels k,k+1 of
one current diagram, testing distinct variables x then y. For each state
u at level k write v_a for its bit-a successor, and w_ab for the bit-b
successor of v_a. All w_ab lie at level k+2, including the terminal case.
Replace u by a state with the same incoming references, now testing y.
Its bit-b successor is a fresh state (u,b), testing x, whose bit-a
successor is w_ab. Retain all levels above k and below k+1 verbatim.
Delete the old level-k+1 states. Density ensures they have no other
incoming references from retained levels. The root correspondence is
unchanged, including when k=1. Retain two fresh child states for every u
even when they coincide as functions; no reduction is performed.

This is the four-cofactor specialization of Rudell's swap: on bits a,b
the old and new two-level paths both reach w_ab. Therefore it preserves
the Boolean function, for every state above or at the replaced block.
If N is the total number of states, including terminals and unused
states, and A,B₀ are the numbers at levels k,k+1, then exactly

    N_new = N + 2A − B₀ ≤ 3N.                         (1)

All levels remain dense and deterministic. No bound on their individual
widths is inferred beyond their total state count.

**Exact correction of one swap.** Put e_0(t)=1+t and e_1(t)=t.
For each a,b∈{0,1}, expansion in the free ring gives

    e_a(x)e_b(y)+e_b(y)e_a(x)=xy+yx.                 (2)

Indeed write e_a(x)=x+α and e_b(y)=y+β for scalar α,β∈{0,1}.
The xβ, αy and αβ terms occur twice in the sum and cancel in F₂;
the two ordered quadratic terms remain. Thus (2) covers all four
literal choices without imposing Boolean axioms or moving any suffix.

Let r_u,r'_u be the old and new state polynomials and R_ab the unchanged
suffix polynomial at w_ab. Their exact displayed orders give

    r_u  = Σ_(a,b) e_a(x)e_b(y)R_ab,
    r'_u = Σ_(a,b) e_b(y)e_a(x)R_ab,
    r_u+r'_u = (xy+yx) Σ_(a,b) R_ab.                (3)

Repeated grandchildren are counted with multiplicity in these sums.
Let τ_xy be the single pair placeholder indexed by the two original
names in increasing dictionary order. Its axiom is xy+yx in either
orientation over F₂.

Construct an explicit correction graph C as follows. Copy all old states
strictly above k, with their affine transition labels e_a(z). Copy the
level-k states as boundary vertices and retain incoming prefix edges.
From each boundary u add four separately recorded edges labeled τ_xy
to the copied suffix vertices w_ab. Copy all states and affine transitions
at levels k+2 onward. Add a fresh sink, with a unit edge from every
terminal labeled 1 and no edge from terminals labeled 0. The designated
source is the old root, or its boundary copy when k=1. Include no old
outgoing edge at a boundary vertex. This graph has O(N+1) vertices and
edges, even with all unused prefix and suffix states retained.

Every accepting path crosses exactly one boundary edge. It cannot
return to the prefix; all other edges increase the original level.
Hence C is acyclic and C(y,0)=0 path by path. After B substitution,
its suffix at each boundary equals (3). Above the boundary, the old/new
polynomial difference obeys the unchanged linear prefix recurrence
e_0(z)(r_0+r'_0)+e_1(z)(r_1+r'_1). Backward induction on these levels
therefore proves, for the exact old and new roots h,h',

    C(y,B)=h+h'.                                    (4)

This induction also proves that sharing of prefixes and suffixes is
legitimate: their complete paths are never enumerated or independently
copied. Each accepting path has at most k−1 prefix factors, one
placeholder, and q−k−1 suffix factors, so its pre-substitution degree
is at most q−1. A swapped pair requires q≥2. Duplicate edges are kept,
allowing their correct parity cancellation; a zero Boolean function
does not license deleting a formally nonzero graph.

**All swaps with one original-input bound.** Use insertion sorting of
ρ by the positions in π. Each adjacent exchange removes one inversion;
each inversion must be crossed by any adjacent-swap sequence, so this
gives exactly d swaps. The sequence is computed from the two explicit
permutations in polynomial time. Denote the diagrams by E₀=E,…,E_d,
their exact polynomials by g₀=g,…,g_d, and their state counts by N_t.
The final order is π. The swaps preserve scalar evaluations, not exact
root polynomials; (4) supplies the missing formal differences C_t.

Because N₀≤M and d≤floor(log₂ M), (1) implies

    N_t ≤ 3^t N₀,
    3^d ≤ M^(log₂ 3) ≤ M²,
    Σ_(t=0)^d N_t ≤ (3/2)N₀3^d ≤ (3/2)M³.          (5)

These count unused states as well. Each correction graph is independently
copied from E_t and has O(N_t+1) records. Their disjoint parallel sum
J=Σ_(t=0)^(d−1) C_t therefore has O(M³) records, including fresh sum
endpoints, and satisfies formally

    J(y,0)=0,                 J(y,B)=g+g_d.          (6)

Intermediate roots cancel in the sum of (4) in characteristic two.
No previous witness is an input to a later swap, so a polynomial
construction cost is not recursively raised to the number of swaps.
For d=0 take J to be a zero graph with distinct endpoints and no
accepting path. Keeping every intermediate diagram and correction
separately still has the aggregate state bound (5).

**Common-order product and exact recovery of fg.** Now D,E_d have the
same order π, though E_d can have much larger width. Let N_D,N_* be
their state counts, bounded respectively by M and M³. The synchronous
pair representative P of L026 (7)–(8) computes their pointwise product
and belongs to the increasing-multilinear subspace in order π. The
zero-product promise and scalar preservation of swaps give P(a)=0
for every Boolean assignment. L026's injectivity in precisely this
subspace gives P=0 as a free polynomial. No injectivity is applied to
fg or to a sum of representatives in different orders.

L026 (9) and L071's post-compilation graph construction give W with

    W(y,0)=0,                W(y,B)=f g_d + P=f g_d. (7)

For clarity about the changed width bound, there are at most
N_D N_* same-level pairs. Each pair has two recursive affine edges
and three local exit blocks of the forms e_0 K_0(V_0+V_1),
e_1 K_1(V_0+V_1), and σ(U_0+U_1)(V_0+V_1), in these exact orders.
Each value or K factor is an independently copied O(N_D+N_*+1)-record
graph by L071. K has a prefix region and one value region, with no
return, so this count is independent of its path count. There are
constantly many factors per exit block. Pair transitions go only to
later pairs; an exit block cannot return to any pair. Consequently

    records(W) ≤ C(N_D N_*+1)(N_D+N_*+1)=O(M⁷).     (8)

This is the imported exact W polynomial with its graph copies counted,
not an unfolding of W into a formula. Terminal pairs have no accepting
W path, constants are retained in value factors, and repeated successors
retain parallel edges. Terminal value copies can equivalently be merged
by their scalar labels; retaining all of them with the stated sink
edges implements the identical suffix recurrence. L026/L071's degree
bound for W is at most 2q−1 when q≥1.

Take a disjoint value graph for the original D, in its original order,
and concatenate it on the left of J; then take the disjoint sum

    H = W + fJ.                                      (9)

Fresh distinct entrances/exits, unit connectors and disjoint internal
vertices implement these operations with affine labels and no empty
accepting path accidentally added. The factor f is copied once for
this concatenation, not once per path. Equations (6)–(7) give

    H(y,0)=0,
    H(y,B)=f g_d + f(g+g_d)=fg.

Thus the output is the originally prescribed ordered product. The fJ
paths have degree at most q+(q−1)=2q−1 whenever d>0; when d=0 that
branch is zero. If q=0, both roots are scalars and the zero-product
promise says fg=0, so simply output the distinct-endpoint zero graph.
For q=1 there are no swaps and (7) suffices. These cases meet the
max(1,2q−1) convention in the conclusion.

**Full bits, independent copies and construction time.** All counts
above concern fully written graphs, not circuit-valued edge labels.
Since every state has two outgoing transitions or is a terminal, its
number of records is O(N+1). Equations (5) and (8) bound the final graph
and all independent local-block copies by C₁(M+2)^7 records. Optional
temporary value/K templates for all needed earlier-variable choices
cost at most O(q(N_D+N_*+1)); pair tables and all reordered diagrams
also fit this allowance. The complete swap list has O(q²) possible
entries before the promised distance cutoff, with original names from
the supplied dictionaries. No implicit source is used to supply names.

Densely renumber every constructed graph. Every reference then has
O(log(M+2)) bits, with an absolute constant because the record exponent
is fixed. Every edge has at most two affine terms; coefficients are
bits. An original name, axiom-position name or placeholder has at most
M bits, so even spelling original names at every edge gives
O(M+log(M+2)) bits per record. The full original/axiom/placeholder
dictionary already has at most M bits. Repeating it independently in
every local graph file, rather than crediting external sharing, costs
at most M times the number of component copies, itself bounded by the
record allowance. Original and new order lists, roots, level numbers,
terminal data, parallel edges and complete framing are likewise paid.
Thus an O((M+2)^8) full-bit allowance suffices; increasing an absolute
constant gives the deliberately loose K(M+2)^9 bound in the conclusion.
M was fixed before constructing any of these outputs.

All operations are finite loops over explicit states, pairs, copies and
dictionary entries. Sorting, renumbering and even naive sequential
lookup add only fixed polynomial factors to these bounds. This proves
polynomial bit time; it asserts no optimized hash-table runtime. No
truth table, complete path list, semantic zero oracle or extra ER
representation premise is used. The zero-product promise is used only
to conclude P=0, after constructing the exact unconditional correction
identities. The proof is all-size and informal; no implementation or
finite graph certificate is claimed. The separate audit below checks
these all-size obligations.

**Separate critical audit — step 342, 2026-10-19.** This audit uses the
unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-near-order-obdd-witness-audit.md`.
It checks the entire stated theorem, not just finite examples. Rudell's
Boolean operation and the formal-context literature retain the precise
scope stated above; no additional external theorem is imported. In
particular, no unread sharp reordering bound, treewidth premise, Boolean
zero tester or arbitrary-order W₂ is used. The full proofs of the
needed L026 and post-compilation L071 components were checked at their
interfaces, rather than invoking L071's whole theorem.

At a swapped block the old path for bits (a,b) has label
e_a(x)e_b(y), and the new path has label e_b(y)e_a(x); both reach the
same old w_ab. Expanding (x+α)(y+β)+(y+β)(x+α) cancels both scalar
offset cross terms and both constant terms for each of the four choices
of α,β. Thus each summand of the difference is exactly
(xy+yx)R_ab, with the suffix on the right. This requires neither
Booleanity nor commutation with that suffix. Distinct choices reaching
one grandchild still contribute distinct edges; for example two
identical contributions cancel, rather than becoming one contribution.

The correction graph contains no boundary-to-old-child edge. Every
accepting path therefore crosses a single τ edge before entering its
suffix region. Its boundary suffix is τ_xy Σ_(a,b)R_ab; substitution
gives the displayed root difference at that boundary. At each preceding
state the difference of the old and new recurrences equals the sum of
the two unchanged left edge labels times the child differences. This
proves the claimed root identity by induction, including merging prefix
paths. No prefix coefficient is moved through τ or through a suffix.
The construction also gives zero at zero placeholders path by path.
For k=1 the source itself is the boundary; for k=q−1 the w_ab are
scalar terminals and their unit/no-edge exits give exactly those scalars.
Repeated successors, unreachable states and terminals of the same label
do not alter the induction. Density ensures that every incoming edge
to the deleted level came from the replaced level; without density this
deletion argument would be insufficient. Acyclicity and a fresh sink
exclude a spurious accepting empty path in every case.

There are A retained top vertices, 2A fresh second-level vertices and
B₀ removed old second-level vertices, giving exactly N+2A−B₀.
Other levels and all terminals are retained. Each new state still has
two transitions, so counting vertices also controls edge records. The
inversion-sorting sequence has d exchanges of distinct adjacent
variables; its intermediate diagrams remain dense permutations of the
same alphabet. Applying the factor-three estimate successively and
summing the geometric series gives (5), including d=0. Since M is
the original full input length, N₀,N_D,q≤M; the growth estimate never
redefines M using an intermediate diagram or the desired witness.
Independent correction copies and sum connectors cost O(Σ N_t+d)
records. For positive d this is O(M³), and for d=0 the explicitly
chosen zero graph needs only constant many records. Summing (4) cancels
each intermediate g_t exactly twice; no recursive composition of
already constructed witnesses is hidden in this telescope.

For the final common-order step, same-level pairs number at most
N_D N_*. At a fixed pair the earlier variable used by each K block is
fixed. One independently copied K block has a K region and a value
region, each of size O(N_D), not one copy per accepting path or per
possible earlier variable. A suffix-sum factor uses one copied value
region and two entry edges, of size O(N_D) or O(N_*). Thus the constant
number of independently copied factors at each pair costs
O(N_D+N_*+1), as in (8). Pair transitions supply only recursive left
multipliers; no local block returns to a pair. Their first-exit
recurrence is exactly L026 (8), including zero terminal W states.
The auxiliary P graph has the same pair transitions but scalar-product
terminal exits, so it is the increasing-multilinear representative of
the pointwise product. The Boolean-zero promise identifies this P with
zero by L026's injectivity; it does not identify fg or g+g_d with zero
in the free algebra. Equations (6) and (7) then give
W(y,B)+fJ(y,B)=fg_d+fg+fg_d=fg, with f kept on the left throughout.
Fresh sum/product endpoints and disjoint interiors implement that
ordered polynomial, and both summands vanish at zero placeholders.

For an independent path-degree check, a swap path has k−1 prefix
levels, one placeholder and q−k−1 suffix levels, hence degree at most
q−1. An original-f path has degree at most q. In the common-order
graph, a W path with s remaining levels at its first local exit has
q−s preceding affine factors and a local block of degree at most
2s−1. A K path within that block switches once to its value suffix;
terminal K states have no accepting path. Hence the complete W path
has degree at most q+s−1≤2q−1. Unit connectors add no degree. These
are bounds on paths before cancellation, not just on the resulting
polynomial. For q=1 there are no swaps, terminal K terms are zero and
the Boolean exit has degree at most one. For q=0 the promised scalar
product is zero and the distinct-endpoint zero output is valid.

Finally N_D≤M and N_*≤M³ give O(M⁷) records for W. The fJ branch,
all swap diagrams, P pairs, optional earlier-variable templates and
sum/product framing fit that allowance. A complete graph block is
copied a constant number of times per pair, so the number of component
copies is itself O(M⁷). Even writing the full input dictionary anew
for every component costs O(M⁸) bits. Each edge has at most two affine
terms with bit coefficients; dense references need O(log(M+2)) bits
and every original symbol spelling costs at most M bits. Original
orders, terminal data and new root/framing records obey the same
bound. This proves an absolute O((M+2)^8) full-bit bound and therefore
the unchanged K(M+2)^9 conclusion. Loops over explicit records, pair
states and dictionary lookups give a fixed polynomial bit-time bound;
no claim that its exponent equals the output exponent is needed.

The audit finds no substantive defect and changes neither the theorem
nor its mathematical inputs or bounds. It discharges the pending
all-size audit obligations within this restricted scope; it is not a
new witness construction, stronger theorem, implementation or novelty
certification. The arbitrary-order witness bound, general ER data
availability and unrestricted SAT gaps remain unresolved, and Attempt
030's independent availability obstruction remains intact.

## Mathlib

Full matching theorem, exact swap-graph specialization and full-bit
ledger: **not checked**. Unknown coverage is not evidence of absence.
The primary imported local Boolean operation is Rudell §4.1 p.44 as
cited above. The ready assessment also compares Iddo Tzameret,
[*Algebraic Proofs over Noncommutative Formulas*, arXiv:1004.2159v2,
1 August 2010, Definition 3.1 and Lemma 3.4/Claim 3.5, pp.7,9–10](https://arxiv.org/pdf/1004.2159v2):
its formula-context commutation does not itself bound a graph in shared
diagram size and is not invoked by unfolding paths. The exact
common-order identities and affine graph realization are the named
local L026/L071 components. No inspected full-statement match or
novelty certification is asserted. Classification: POTENTIALLY_NEW
under the pre-existing SPECIALIZE assessment, with the known operations
and the new applicability/accounting argument distinguished above.

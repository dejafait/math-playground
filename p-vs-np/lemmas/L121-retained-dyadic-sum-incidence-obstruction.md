# L121 — Retained dyadic sums fail the scalar map and linear graph budget

## Hypotheses

Work over F₂ with finite acyclic occurrence graphs and singleton labels
1 or x. All occurrences are charged, including parallel occurrences.
Use L110 §§4,21's right closure and independent wrapped products:

    K_H=(I+C_H)^(-1), alpha_H=e_s K_H,
    M_H=D_H K_H, beta_H=e_t^T, g(H)=|V(H)|+2|E(H)|.       (1)

An arrow X:U->V must satisfy all three scalar equations

    alpha_U X=alpha_V, M_U X=X M_V, X beta_V=beta_U.       (2)

No elementary reverse companion is imposed. The inverse in (1) is a
finite sum; there is no stored dense-closure oracle.

Let k>=0, N=2^k, and r=N. F_N has vertices f_0,...,f_N and parallel
1/x edges at each layer. G_N is the pure-x path h_0,...,h_N. Keep the
original endpoints A=Prod(F_N,G_N) and B=Prod(G_N,F_N), including their
fresh source/sink, disjoint factors and three constant connectors. Set
S=g(A)+g(B). This is an allowed test family for arbitrary unary G; no
assumption is made about other operands satisfying the desired conclusion.

The **retained dyadic-sum template** replaces the complete placement grid
by the following single explicit operand D_N. Every named changed sum
remains a vertex of the proposed final auxiliary; an arithmetic circuit
used only during construction is outside this restriction.

* Base vertices b_j, 0<=j<N, have parallel 1/x edges b_j->b_(j-1)
  for j>0; b_0 is the operand exit. Put a_(0,j)=b_j.
* For scales u=0,...,k-1, use the PREVIOUS scale's registers. If bit u
  of j is zero, set a_(u+1,j)=a_(u,j), an alias with no new vertex.
  If that bit is one, create v_(u,j) with exactly two constant edges
  to a_(u,j) and a_(u,j-2^u), and set a_(u+1,j)=v_(u,j).
* Add N probe vertices p_j, each with one x edge to a_(k,j).
  The operand source is p_(N-1). There are no other operand edges.

Define Q_N=Prod(F_N,D_N), again with full disjoint copies and the three
constant connectors s->f_0, f_N->p_(N-1), b_0->t. Each two-coordinate
sum is represented by its two edges. Unchanged registers are fully shared.
There is neither a copy per placement nor a free polynomial multiplier.

The trial first matrix X:A->Q_N keeps s,F_N,t, sends

    h_j -> p_(N-j-1)  (0<=j<N),    h_N -> b_0,           (3)

and has no other entries. These are distinct unit rows. No second arrow
is supplied or assumed. The count below also permits any replacement of
Q_N that still represents EACH named base and changed-sum value by one
vertex with that same full raw suffix to its sink. It allows all such
value-preserving vertex identifications, but does not assume they are
scalar simulations. General scalar recoding of the named values is outside
this restricted count.

## Conclusion

The graph Q_N is acyclic and accepts the same polynomial
z^N(1+z)^N as both original endpoints. Each probe has right-closed state
residual z^(j+1). Nevertheless:

1. X satisfies both boundary equations in (2), but for every N>=2 its
   transition equation fails in EXACTLY the N-1 rows h_0,...,h_(N-2).
   In row h_(N-2) the complete unequal vectors are

       (M_A X)_(h_(N-2))=e_(p_0),
       (X M_Q)_(h_(N-2))=e_(v_(0,1))+e_(b_1).          (4)

   For N=1 all three equations hold for this first map only.
2. Q_N contains kN/2 changed sum vertices and has

       S=16N+20,
       |V(Q_N)|=3N+kN/2+3, |E(Q_N)|=5N+kN+1,
       2g(Q_N)=26N+5kN+10.                             (5)

   Even any value-preserving vertex sharing allowed above leaves at least
   N+kN/2 vertices. Thus its twice-counted graph charge is at least
   N(k+2), whose ratio to S is at least (k+2)/36 and is unbounded.
   No universal C can give support plus twice-counted intermediate size
   <=C*S for this retained-register template, whatever the other maps are.

This is a local REPRODUCTION/specialization of finite path semantics,
the already used binomial conversion, and elementary counting. It is new
route evidence here, not a claimed new general circuit or automata theorem.
The count is not a lower bound for arbitrary XOR circuits, scalar-sum
chains, or intermediates that do not retain every named dyadic value.
The wrong map (3) is not evidence that all maps to Q_N fail; its size
already stops the retained template even if another map exists.

The path family stops the template before testing arbitrary G. L120's
valid ordinary projections on both cancellation fixtures remain valid.
No general F_r chain, fourth-comparison receipt, unrestricted proof-system
lower bound or P versus NP resolution is established.

## Proof

### 1. Imported scope and the particular test

Reuse the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-27-batched-incidence-zigzag.md`.
The scalar convention and soundness are imported from Ésik–Maletti,
*Simulation vs. Equivalence*, [2010 author manuscript, Definition 3.1
and soundness, p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ and finite boundary vectors satisfy those hypotheses. The source
supplies neither a sparse matrix here nor this resource bound. No
qualitative simulation, factorization or minimization theorem is reproved.

L110 fixes finite right closure and the complete product recipe. L118
§5's independent suffix polynomials z(1+z)^j and binomial conversion
motivate this choice of candidate, rather than serve as an additional
proof premise. Here the literal graph is checked directly at every scale,
instead of expanding every binomial coefficient into a stored map entry.
The changed intermediate, graph realization, exact failed equation and
retained-node cost require the present calculation; a citation about
qualitative equivalence does not settle them.

L115's single-layer construction, L119's elementary-factor stop and
L120's placement-folding stop are comparisons, not existence premises.
In particular this template uses actual sums and avoids the full placement
grid. It does not require independent output channels or an invertible
change of state basis. No cross-notebook theorem is used.

### 2. Acyclicity and every named polynomial

Order D_N's probes first, then its gates in decreasing scale order, then
b_(N-1),...,b_0. A gate points only to an earlier CREATED gate of smaller
scale or a base vertex; in this topological order its targets are later.
Every base edge also goes forward. Put the product's s,F_N before D_N
and t after it. All three connectors go forward. This proves acyclicity
of the full occurrence graph, including unused probes and gates.

The variable z records the number of x letters, not a second input symbol.
Let H_v(z) denote the FULL raw suffix polynomial from v to the final t,
including leading constants. Let

    R_v(z)=sum_(d>=0) (e_v M_Q^d beta_Q) z^d             (6)

be the right-closed state residual, without a leading K. All sums are
finite. L110's path decomposition gives H_v from e_v K_Q instead of e_v
in (6). These are distinct conventions: a nonfinal vertex with only
constant outgoing edges has M_Q row zero and R_v=0, even if H_v!=0.

The complete base suffixes are H_(b_j)=(1+z)^j. This follows from
H_(b_0)=1, using the connector to t, and the two edges at each preceding
base vertex. We claim, for every scale u=0,...,k and every j<N,

    H_(a_(u,j))=z^l(1+z)^(j-l),  l=j mod 2^u.           (7)

At u=0 this is precisely the base formula. If bit u of j is zero, the
new register is an alias, and j mod 2^(u+1)=j mod 2^u, so (7) persists.
Otherwise write j=H+2^u+l, where 0<=l<2^u and H is divisible by
2^(u+1). The two previous register values, by induction, are

    z^l(1+z)^(H+2^u)  and  z^l(1+z)^H.

The gate's two constant edges sum them. Repeated squaring in F₂[z]
gives (1+z)^(2^u)=1+z^(2^u), so the sum is
z^(l+2^u)(1+z)^H. This is exactly (7) at u+1. This short induction
verifies the particular graph, rather than asserting a new binomial theorem.

At u=k, (7) gives H_(a_(k,j))=z^j. Each probe first takes exactly its
one x edge and then may take any suffix from that register. Since the
probe has no leading constants and is not final,

    H_(p_j)=R_(p_j)=z^(j+1).                            (8)

Thus D_N accepts z^N and Q_N accepts (1+z)^N z^N, as claimed. The
original two products accept the same scalar polynomial by their literal
path recipes. Every gate is constant-only, however, so

    R_(v_(u,j))=0,                                     (9)

not the nonzero polynomial in (7). Omitting this distinction would
incorrectly turn an arithmetic identity into a scalar simulation.

### 3. Complete checking of the trial first arrow

Here are all the original A transition rows; unlisted rows are zero:

    f_i -> sum_(a=i+1)^N f_a + h_0          (0<=i<N),
    h_j -> h_(j+1)                         (0<=j<N-1),
    h_(N-1) -> h_N+t.

Its initial vector is s+sum_(i=0)^N f_i+h_0 and its final vector is t.
These follow by taking constants AFTER each letter, including the terminal
connector h_N->t. There is no constant tail through the nonempty x path.

All Q transition rows are likewise specified by the following display:

    f_i -> sum_(a=i+1)^N f_a + p_(N-1)       (0<=i<N),
    p_j -> e_(a_(k,j)) K_Q                  (0<=j<N),
    b_j -> e_(b_(j-1)) K_Q                  (1<=j<N).

All s,f_N,gate,b_0,t rows are zero. Its initial vector is
s+sum_(i=0)^N f_i+p_(N-1), and its final vector is t. The matrix K_Q
here is the finite closure of the specified graph, not free map data.

Applying (3) to the complete initial vector gives exactly alpha_Q.
Only the source row t maps to a target with final coordinate one, so
X beta_Q=beta_A for every row. The f_i rows agree in the transition
equation by the two displays. The s,f_N,h_N,t rows are zero on both
sides. For h_(N-1), both sides are b_0+t, since a_(k,0)=b_0 and
e_(b_0)K_Q=e_(b_0)+e_t.

For every 0<=j<N-1, the left side of the transition equation is the
unit at p_(N-j-2). The right side is the constant closure starting at
a_(k,N-j-1), supported solely on gates, bases and possibly t. No constant
path from there enters ANY probe. Its p_(N-j-2) coordinate is therefore
zero, while the left side's coordinate is one. These and only these N-1
rows fail. This accounts for every row and both boundaries, including N=1.

For N>=2 specifically, a_(k,1)=v_(0,1), whose two constant children are
b_1 and b_0. The complete constant closures satisfy

    e_(b_0)K_Q=e_(b_0)+e_t,
    e_(b_1)K_Q=e_(b_1)+e_(b_0)+e_t,
    e_(v_(0,1))K_Q=e_(v_(0,1))+e_(b_1).

The two b_0 and two t contributions cancel in the last expression. This
proves the exact unequal vectors (4), independently of any numerical replay.
Their accepted suffixes agree, but their coordinates do not. The missing
second arrow is not used as evidence of failure.

### 4. Retained-size obstruction, even after equal-value sharing

For each of k scales exactly N/2 indices have its bit set, giving kN/2
new gates (zero gates when k=0). Each has two edge occurrences. Thus D_N
has 2N+kN/2 vertices and N+2(N-1)+kN edges. Adding the copied F_N,
fresh boundary vertices and three connectors gives the counts in (5).
Each original endpoint has 2N+4 vertices and 3N+3 edges, so S=16N+20.
No endpoint is replaced by a simplified polynomial in this denominator.

For a changed gate v_(u,j), write l=j mod 2^(u+1), H=j-l. Then
2^u<=l<2^(u+1), and its full suffix, by (7), is z^l(1+z)^H.
This is nonzero, with EXACT orders l at z=0 and H at z=1: the remaining
factor evaluates to one at the corresponding point. These orders recover
j=l+H and u=floor(log2(l)). Hence every changed gate has a different
full suffix from every other changed gate. The N base values are also
pairwise distinct, have order zero at z=0, and are distinct from all gates.

If a replacement must represent each of these named values by one vertex,
distinct values cannot be the suffix of the same vertex. This proves the
lower bound N+kN/2 after ALL permitted value-preserving identifications.
It does not assert that raw suffixes are invariants of arbitrary scalar
row maps, or that these polynomials are linearly independent. In fact
they lie in a polynomial space of dimension N. Replacing many named values
by scalar combinations of fewer vertices drops a template hypothesis.

Every retained intermediate is charged at each of its two incident arrows.
Even ignoring all its edges and all map entries, its charge divided by S
is therefore at least

    2(N+kN/2)/(16N+20) >= (k+2)/36.                     (10)

For any proposed finite C>=0, choose integer k>36C. Then (10) exceeds C.
For the literal Q_N the stronger exact repeated graph count is (5).
Neither larger support nor nonnegative boundary/index/work charges can
repair this necessary size inequality. A different first map, either
orientation of other arrows, and an ordinary projection of a deep
unobservable component do not remove a COMPULSORY named-gate requirement.
Removing that requirement creates a different construction, not a
contradiction to this bound.

For completeness (3) has exactly 2N+4 scalar entries. In an optimistic
two-arrow use of Q_N with the original endpoints, the four graph occurrences
have 10N+kN+14 vertex positions, so even their initial/final vectors require
20N+2kN+28 field positions if stored densely. A topological permutation
uses one index per vertex occurrence; each edge and map entry also needs
its indices, and encoding has additional roots, lengths and framing.
Generating the literal gates and edges requires at least their output
count. These are necessary charges only: no second map, complete wire
bound, checking-work bound or live-memory fit is asserted for a chain
whose first map and graph-size condition have already failed.

### 5. Exact replay and limits

The reproduction command, using a fresh destination to preserve evidence,
is:

```bash
python3 scripts/batched-incidence/check_dyadic_sums.py \
  --output scripts/batched-incidence/output-538-replay
```

The original certificate is
`scripts/batched-incidence/output-538/dyadic-sums.json`. For k=0,...,5
(N=1,2,4,8,16,32), it retains complete original endpoints and Q_N,
all occurrences, closures, transitions, boundaries, raw suffixes,
right-closed residuals, stage registers, gates, the full proposed X and
BOTH sides of every equation. It lists every failed transition coordinate.
The exact computations compare all coefficients and coordinates, not samples.

At N=2 the first arrow fails only in row h_0, at the three coordinates
p_0,v_(0,1),b_1 of (4); both boundary vectors agree. At N=8 it has seven
failed rows and twelve distinct changed gates; S=148 and 2g(Q)=338.
At N=32 the eighty changed gates give S=532 and 2g(Q)=1642. All six
cases have exactly N-1 failed transition rows, and the graph/formula
verification has zero unexpected failures. These finite ratios do not
prove an asymptotic lower bound; (10) supplies that proof.

The complete N=2 graphs/arrow, all N=8 stage/gate values and failed-arrow
coordinates, the N=32 ledger, symbolic thresholds and empty verification
failure list were inspected through selected full JSON pointers. Correct
series and a passing check of expected failures are never labeled an
accepted scalar arrow. The cancellation fixtures were not rerun after
the mandatory path test decisively stopped this template.

## Mathlib

Full matching coverage for this particular retained dyadic-sum graph,
failed scalar map and resource obstruction is **not checked**. No absence
or originality claim is made. The imported scalar convention/soundness is
precisely cited in §1. Finite matrix/acyclic path identities, characteristic-
two repeated squaring and polynomial orders would be supporting ingredients,
not a matching library theorem proving the entire specialized construction.

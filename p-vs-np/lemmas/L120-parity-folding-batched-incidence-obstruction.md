# L120 — Deep projections work, but coordinate folding cannot batch all placements linearly

## Hypotheses

Work over F₂ with finite acyclic occurrence graphs, singleton edge labels
1 or x, arbitrary designated roots, and all parallel occurrences retained.
Use L110 §§4,21's right closure and independent wrapped products:

    K_H=(I+C_H)^(-1), alpha_H=e_s K_H,
    M_H=D_H K_H, beta_H=e_t^T, g(H)=|V(H)|+2|E(H)|.     (1)

The inverse is a finite sum. An ordinary scalar arrow X:U->V satisfies

    alpha_U X=alpha_V, M_U X=X M_V, X beta_V=beta_U.     (2)

No reverse elementary companion is required. F_r, r>=1, has vertices
f_0,...,f_r and parallel 1/x edges at each layer. The original endpoints
are A=Prod(F_r,G), B=Prod(G,F_r), with full disjoint operand copies,
fresh source/sink and three constant connectors. S=g(A)+g(B).

The **tested simultaneous-placement folding template** has this compulsory
stage. Let H_r=A, H_0=B. For 0<i<r let
H_i=Prod(F_i,G,F_(r-i)), with disjoint full factors, fresh s_i,t_i and
four constant connectors. Let U contain one independent copy of each H_i,
identifying only their sinks into a single t. Its entry is H_r's source.
These are complete occurrence lists; no other edges are added. U is
acyclic, by putting the separate nonsink copies in their topological
orders and then t.

The template retains one acyclic singleton intermediate Q that represents
these copies by **coordinate coalescing and deletion**. Precisely, there
is a scalar matrix Z with U rows and Q columns, each row either zero or a
single unit coordinate, satisfying

    M_U Z=Z M_Q, Z beta_Q=beta_U.                      (3)

If Z is used as an accepting arrow, its initial equation in (2) is also
required. The lower bound already follows from the weaker (3). Q may
have additional vertices, arbitrary edges, constants and cancellation.
There is no raw per-label equation, functional-surjectivity condition,
independent output-port contract or bound on the depth of a deleted
component. Any number of partial-function folds/deletions still has a
composite of this form. General scalar row sums are outside this restriction.

U specifies the copied states and incidences exactly. An implementation
may try to generate Q directly; the lower bound is on Q itself and does
not presume that U was first materialized. If U is also retained, its full
size must additionally be charged. Q must occur in the proposed final
chain: a large object used only during construction would not by itself
lower-bound a different final certificate. Other arrows of that chain
are unrestricted; their existence is not assumed.

## Conclusion

1. On both L117's four-vertex cancelling operand and L119's long cancelling
   G_m, the original endpoints have explicit ordinary projection arrows
   A->H<-B, where H is F_r with just a fresh source and sink and two constant
   connectors. Every G coordinate is killed. All three equations hold,
   and support plus twice-counted intermediate size is 12r+20<=2S.
   The long kernel is allowed: no bounded-lag companion is asserted.
2. For G the N-edge pure-x path, every Q satisfying the compulsory stage
   (3) has at least N(r+1)+1 vertices. In particular, at r=N=2^k,

       S=16N+20,
       support + twice-counted intermediate size >=2(N(N+1)+1). (4)

   Thus no universal C gives <=C*S for this folding template. This holds
   even with perfect parity coalescing and deletion of arbitrarily deep
   output-dead components, before charging any construction work.

This stops retaining all placements through partial-function coordinate
folding. It does not stop sparse scalar sums, different auxiliaries that
avoid these simultaneous coordinates, other orientations, or general
scalar chains. The distinguished residuals below are not claimed linearly
independent. This is a REPRODUCTION/specialization of scalar soundness and
elementary polynomial orders, not a new general automata theorem or an
originality claim. No actual fourth-comparison receipt or P versus NP
resolution follows.

## Proof

### 1. Source scope and distinction from earlier failures

Reuse the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-27-batched-incidence-zigzag.md`.
The scalar convention and preservation of series are imported from
Ésik–Maletti, *Simulation vs. Equivalence*,
[2010 author manuscript, Definition 3.1 and soundness, p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ and arbitrary finite boundary vectors meet its hypotheses. Applying
that result to individual state rows requires the transition and final
equations; it does not require the same initial boundary at every row.
No minimization, sparse factorization or qualitative-existence theorem
is reproved. The state computation and resource difference here are the
uncovered quantitative test allowed by the prior assessment.

L110 fixes the right closure and all product connectors. L117 §§3–4 and
L119 §§4–5 supply the complete cancelling endpoint matrices used below.
L115 motivates batching single-layer moves but supplies no such batching.
L112 counts a specified uncompressed cut table; the present bound survives
valid coordinate folds even if Q is generated without that table. L116
requires independent identity-delay output channels; here there is just
one final scalar, and the bound specifically restricts coordinate maps.
L118 fixes a suffix basis and permits arbitrary scalar maps; that is a
different restriction. These three comparisons are not proof premises.

### 2. The cancellation fixtures really admit deep ordinary projections

For either fixture use the common endpoint coordinates s,F_r,G,t from
L117 or L119. Put J_(i,i+1)=1 on F_r, T=J(I+J)^(-1),
h=T e_(f_r)^T, and a=e_p+e_q. In L117 let D have its two nonzero entries
p->u,p->v. In L119 let D be the m-edge p,u_1,...,u_m shift, zero on q.
The complete transition blocks, suppressing only the zero s row/column,
are the already established formulas

    M_A = [ T   h a   h ]       M_B = [ T   0   h ]
          [ 0    D    0 ]             [ 0   D   0 ]
          [ 0    0    0 ],            [ 0   0   0 ].   (5)

Both initial vectors are s+sum_(i=0)^r f_i+p+q+t; both final vectors
are the unit at t. These equalities retain every original occurrence.
In particular the two long exit occurrences in L119 cancel in parity;
in L117 the constant tails after its two x edges cancel. Raw structural
paths are not a justification for deleting states.

Define H literally by vertices s,f_0,...,f_r,t, all 2r F_r occurrences,
and constants s->f_0, f_r->t. Its complete transition has F-to-F block
T, F-to-t column h, and all other rows zero. Its initial vector is
s+sum f_i+t and its final vector is the unit at t.

For each endpoint let P keep s,F_r,t identically and send every G row
to zero. These are the entire maps. Multiplying either matrix in (5)
by P removes its G columns. Every G row also has zero image because
its only transition targets were in G. The remaining rows are exactly
P M_H. The initial vectors project to alpha_H. Only t has a nonzero
final coordinate before and after projection, proving P beta_H=beta_A
or beta_B for every row. Thus both arrows satisfy all three equations.

The killed row space is M-invariant, has zero final functional and may
contain an m-edge nilpotent branch. This validates the intended ordinary
projection without imposing the stopped elementary companion condition.

Here |V(H)|=r+3, |E(H)|=2r+2, g(H)=5r+7, and each P has r+3 entries.
The combined charge is 2(r+3)+2(5r+7)=12r+20. L117 gives S=10r+46;
L119 gives S=10r+6m+34. Both imply the claimed <=2S for r,m>=1.

The four graph occurrences at these two arrows have total vertex count
V_*=4r+20 for L117 and V_*=4r+2m+16 for L119. Dense alpha/beta vectors
cost 2V_* field positions; also retaining raw entry/exit vectors gives
4V_*. A topological permutation uses V_* indices. With
L=ceil(log2(S+2)), each support entry needs at most two L-bit indices
and a field bit; graph edges, roots and framing must also be encoded.
This gives O(S log(S+2)) bits, not a particular wire-byte or live cap.
Computing each column of K_U P by reverse constant-edge propagation,
then applying D_U, and independently each row of P D_H K_H by forward
propagation checks all transition coordinates in O(S²) field operations.
Boundary closure and full comparison scans fit the same bound. Dense
rectangular temporary arrays give an O(S²) field-position storage bound.
No numeric production receipt or total interpreter bound is claimed.

### 3. The complete incidence auxiliary and its explicit copy maps

For every i let J_i map each H_i vertex to its own U coordinate and its
sink to the common t, with no other entries. These are fully specified
unit-row matrices. No edge leaves t; no edge between different copies
exists. Consequently C_(H_i) J_i=J_i C_U and D_(H_i) J_i=J_i D_U,
row by row, including the sink. Finite geometric sums give
K_(H_i) J_i=J_i K_U, and hence

    M_(H_i) J_i=J_i M_U, J_i beta_U=beta_(H_i).         (6)

For i=r the chosen initial source also gives alpha_(H_r) J_r=alpha_U:
A->U is a full accepting arrow. For i!=r the initial equality is NOT
asserted and generally fails. Those J_i are copy incidences used in the
compulsory stage, not additional accepting arrows or a complete chain.
The initial equation must separately hold for every actual chain arrow.

For the path family the exact uncompressed counts are

    |V(U)|=(r+1)(r+N+4)-1,
    |E(U)|=(r+1)(2r+N+4)-2.                           (7)

Indeed endpoints have r+N+4 vertices and 2r+N+3 edges, interior placements
have one extra vertex and connector, and identifying r+1 sinks removes
r vertices and no edges. All occurrences remain separately counted.
These counts are not the final obstruction: the next part bounds Q after
every permitted fold/deletion, even if U is not retained in the chain.

### 4. All distinguished state residuals and the compression obstruction

For a right-closed state v define its finite polynomial

    R_(H,v)(x)=sum_(ell>=0) (e_v M_H^ell beta_H) x^ell. (8)

There is no leading K in (8). It is not the raw constant-closed suffix
polynomial of an arbitrary vertex. From (3), associativity gives
M_U^ell Z=Z M_Q^ell for every ell>=0, and therefore

    R_(U,v)=sum_w Z_(v,w) R_(Q,w).                    (9)

This is the state-row specialization of imported scalar soundness. If
row v of Z is zero its residual must be zero; if it is a unit at w the
two residuals agree. Distinct nonzero residuals therefore cannot be killed
or assigned to the same Q coordinate by this template.

Now take G to have vertices h_0,...,h_N and exactly the x edges
h_j->h_(j+1). For each i=0,...,r and j=0,...,N-1, h_j in H_i has no
outgoing constant edge. Every accepting path from it begins with x,
takes the remaining N-j path edges, the connector to the suffix factor
if present, its r-i parallel 1/x layers and the final connector. Thus,
using right closure with its constants AFTER each letter,

    R_(H_i,h_j)=x^(N-j) (1+x)^(r-i).                  (10)

This also covers i=r (no suffix factor). The omitted h_N has no outgoing
x edge and a different right-closed residual; it is deliberately not
counted. Prefix factors are upstream and cannot affect (10). Equation
(6) gives the identical residual for its copy in U.

Each polynomial (10) is nonzero. Its order of vanishing at x=0 is N-j,
because (1+x)^(r-i) has constant term one. Its order at x=1 is r-i,
because x^(N-j) evaluates to one at x=1. These two orders uniquely
determine (i,j), including exponent zero at x=1. Hence all N(r+1)
polynomials are pairwise distinct. The common final state t has residual
1, distinct from all of them. Applying (9) proves

    |V(Q)|>=N(r+1)+1.                                (11)

This proof permits parity cancellation of all incidences and a kernel of
arbitrary depth. It uses only the explicit restriction that a retained
state maps to a single coordinate. Pairwise distinctness is not linear
independence: all these polynomials have degree at most N+r, in a space
of dimension N+r+1. General scalar sums are an essential open alternative.

Each original endpoint has r+N+4 vertices and 2r+N+3 edges. Thus
S=10r+6N+20. If Q is an intermediate, it is charged at both incident
arrows, so its contribution alone is at least 2(N(r+1)+1). At r=N,
the ratio to S=16N+20 is unbounded. Explicitly 16N+20<=36N for N>=1,
so the ratio is at least (N+1)/18. For any proposed finite C>=0 choose
a power of two N>18C; the required bound fails. Nonnegative support,
boundary, index, graph-encoding and checking-work charges cannot repair
this failed graph-size inequality. No additional arrows are needed to
establish the obstruction, and no failure is inferred from their absence.

### 5. Exact finite replay and limits

`scripts/batched-incidence/check_parity_folding.py` constructs complete
occurrence graphs independently of the displayed block matrices. It
forms finite constant closures, checks every transition and both boundary
equations for all four cancellation arrows, and retains both matrix sides.
At r=6 both cases have charge 92, against 2S=212 for L117 and 260 for
L119 with m=6. The projections discard the long branch in one arrow.

For the mandatory r=N=8 path test it constructs all nine placements and
U, checks all coordinates of (6), and separately records which initial
equation is required. Only i=r is an accepting inclusion. It computes
every state residual through the dimension and checks all 72 selected
polynomials against (10), including their pairwise distinctness and
nonzero values. U has 179 vertices and g=679; S=148; every compressed Q
in the template needs at least 73 vertices. The universal failure follows
from (11), not this single finite ratio or a sample of coefficients.

Full graphs, maps, equation products, all selected polynomial values and
checks are in `scripts/batched-incidence/output-537/parity-folding.json`.
The run reports no verification failures. Reproduce into a fresh directory:

```bash
python3 scripts/batched-incidence/check_parity_folding.py \
  --output scripts/batched-incidence/output-537-replay
```

The stopped template is the retained simultaneous-placement coordinate
fold. No full chain for arbitrary G, nonfunctional compression, universal
C, actual record/event/job binding, general F, mixed letters, later jobs,
Boolean/K/H/nonzero-fJ, full wire/work/live costs, availability, L087 W₂
or unrestricted ER/Frege/SAT conclusion is established. No receiver,
production format, cap or historical recovery route is changed.

## Mathlib

Full matching coverage for this specific incidence-folding obstruction and
the two projections is **not checked**; no absence claim is made. The
imported scalar soundness theorem is cited in §1. Finite matrix powers,
polynomial orders and linear-combination identities are supporting
ingredients, not a matching theorem supplying this resource result.

# L117 — Identity stabilization cannot scalar-shear the unary product pencils

## Hypotheses

Work over F₂. A unary occurrence graph is finite and acyclic, with each
edge occurrence labelled 1 or x. Constants and parallel occurrences are
retained in the graph and summed only when forming parity adjacency.
For H with designated entry s and exit t, use L110 §4's right closure:

    C_H = constant adjacency, D_H = x adjacency,
    W_H = I+C_H, K_H = W_H^(-1),
    alpha_H = e_s K_H, M_H = D_H K_H, beta_H = e_t^T.       (1)

Inverses are finite sums in a topological order. The associated pencil
and raw boundary vectors are

    L_H(z)=W_H+zD_H, eta_H=e_s, theta_H=e_t^T.              (2)

For every integer r>=1, let F_r have vertices f_0,...,f_r and the two
parallel edges f_i->f_(i+1), labelled 1 and x, at every layer. Its roots
are f_0,f_r. Let G have distinct vertices p,u,v,q, roots p,q, and precisely
these five edge occurrences:

    constants: p->q, u->q, v->q;
    x edges:   p->u, p->v.                                (3)

Let A=Prod(F_r,G) and B=Prod(G,F_r) be the original wrapped products
of L110 §21: independent whole operand copies, fresh s,t and three
constant connectors, in the indicated order. No endpoint is trimmed,
substituted, padded in its size denominator, or replaced by its polynomial.
Put g(H)=|V(H)|+2|E(H)|, counting each singleton label entry.

The **tested scalar-shear template** adjoins k>=0 isolated vertices to
each endpoint, with zero raw entry/exit coordinates on them. Thus

    L_H^+ = L_H direct-sum I_k,
    eta_H^+ = (eta_H,0), theta_H^+ = column(theta_H,0).

It seeks invertible scalar matrices P,Q over F₂, independent of z, with

    L_B^+(z) = P L_A^+(z) Q,
    eta_B^+ = eta_A^+ Q,
    theta_B^+ = P theta_A^+.                              (4)

In particular this includes a factor-block permutation followed by
scalar elementary block shears on either side, with identity-pencil
stabilization. Allowing arbitrary scalar invertible P,Q is a relaxation
of sparse boundary-only shears, not an additional restriction imposed
on them. No bound on k, the number of shears or their support is assumed.
Only identity-pencil stabilization is tested; auxiliary graphs with
nonzero letter transitions and singular/rectangular arrows are outside
this template.

## Conclusion

For every r>=1, both original products accept the polynomial (1+x)^r,
all vertices of each operand lie on structural accepting paths, and

    g(A)+g(B)=10r+46.                                    (5)

Nevertheless, in common coordinates for the two endpoints,

    M_A^(r+1)=e_(f_0)^T (e_u+e_v) != 0,
    M_B^(r+1)=0.                                        (6)

In fact their nilpotency indices are r+2 and r+1 respectively. No k,P,Q
can satisfy even the first equation of (4). Thus this stable scalar-shear
realization cannot provide a bridge, irrespective of a proposed support
or graph-size budget. Its transition equation fails before any resource
bound or boundary-vector choice could repair it.

This is a counterexample to one conversion of product-pencil algebra
into scalar simulations. It does not exclude polynomial two-sided
transformations, nontrivial auxiliary graphs, noninvertible scalar
arrows or arbitrary zigzags. It is consistent with L115's five-arrow
single-layer result. It is not a lower bound on all unary certificates,
the fourth comparison, or any unrestricted computational model.

The result is recorded as REPRODUCTION: an explicit application of the
ordinary similarity invariant to this interface, with no originality
claim and no claim of mathematical progress beyond the sources checked.

## Proof

### 1. Imported product presentation and the precise conversion tested

The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-27-boundary-coupled-unary-block-pencil.md`.
For the known rank-one product presentation, import Schrempf,
*Linearizing the Word Problem in (some) Free Fields*,
[arXiv:1701.03378v2, Proposition 1.13, printed pp.4–5](https://arxiv.org/pdf/1701.03378v2).
Its product pencil has diagonal blocks L_F,L_G, upper-right block
−b_F e_G, entry row (e_F,0), and exit column (0,b_G)^T.
Definition 1.11, printed p.4, gives the scalar two-sided transformation
(u,A,v)->(uQ,PAQ,Pv). These are known algebraic inputs, not new results.

The base field may be F₂, the alphabet may be unary, and the pencils here
are full because acyclicity makes them upper unitriangular in a suitable
order. The operand entry is the first coordinate in the displayed
topological orders. No minimality theorem is needed for the product
presentation or for the definition of two-sided change. In characteristic
two the upper-right sign is plus. The original three connectors add
the external source/sink to this same rank-one product construction;
their effects are explicitly retained below, using L110 §§4,21.

The inspected source supplies neither (4) for the exchanged factors nor
a sparse scalar-arrow realization of a polynomial multiplier. The present
test restricts a proposed stable realization to scalar shears and I_k
augmentation, then asks whether it can satisfy the actual endpoint
equations. Its failure does not refute the broader source-level polynomial
mechanism. L112–L116 are scope comparisons, not inputs to this proof.

### 2. Scalar two-sided equivalence forces right-closed similarity

This calculation explains both the intended scalar realization and the
obstruction. Suppose for any two equal-dimensional graphs U,V that

    L_V=P L_U Q

with constant invertible P,Q. Equating the constant and z coefficients
gives W_V=P W_U Q and D_V=P D_U Q. Hence

    K_V=Q^(-1) K_U P^(-1),
    M_V=P D_U Q Q^(-1) K_U P^(-1)
       =P M_U P^(-1).                                   (7)

If the two boundary equations in (4) also hold, X=P^(-1) satisfies
the full scalar simulation contract U->V:

    alpha_U X=eta_U K_U P^(-1)
             =eta_U Q K_V=eta_V K_V=alpha_V,
    M_U X=X M_V,
    X beta_V=P^(-1) P theta_U=beta_U.                     (8)

Thus the proposed scalar strict equivalence really would induce an
invertible arrow after right closure; no raw per-label intertwiner is
assumed. The inverse P^(-1) need not be sparse in general, but that cost
question is not reached in this example.

For k isolated zero-boundary states, W_H^+=W_H direct-sum I_k and
D_H^+=D_H direct-sum 0_k, so M_H^+=M_H direct-sum 0_k. Equation (7)
therefore forces similarity of these stabilized transition matrices.
For each ell>=1 it also forces

    (M_B direct-sum 0_k)^ell
       =P (M_A direct-sum 0_k)^ell P^(-1).                (9)

In particular one side cannot be zero when the other is nonzero. This
uses only associativity and invertibility: the intermediate P^(-1)P
cancel in each power. It applies to every P,Q, so choosing different
sparse shear coefficients or composing more such shears cannot evade it.
For polynomial P(z),Q(z), the coefficient comparison used in (7) does
not apply; no assertion about those transformations follows.

### 3. The operand and both complete closed representations

In the order p,u,v,q, G's matrices satisfy

    C_G=e_p^T e_q+e_u^T e_q+e_v^T e_q,
    D_G=e_p^T(e_u+e_v),
    C_G^2=D_G^2=C_G D_G=D_G C_G=0.                       (10)

The last product is zero because its two p-to-q contributions cancel.
Thus K_G=I+C_G, D_G K_G=D_G, e_p K_G=e_p+e_q, and
D_G K_G e_q^T=0. The three accepting paths have weights 1,x,x, so
the accepting polynomial is 1. All four vertices lie on those structural
paths, and p,q are distinct extremal roots. There are no unreachable
vertices, added dead components or coincident-root exceptions in (3).

On F_r let J have entry 1 at (i,i+1), and zero elsewhere. Then

    K_F=(I+J)^(-1)=I+J+...+J^r,
    T=J K_F=J+J^2+...+J^r,
    h=T e_(f_r)^T.                                     (11)

The entry h_i is 1 for i<r and 0 for i=r. In both products relabel the
independent copies into the common coordinate order s,F_r,p,u,v,q,t.
This coordinate identification is only for displaying matrices; it does
not assert that their occurrence graphs or product order are identical.

The following are **all** nonzero transition rows after right closure:

    A: for 0<=i<r,
         f_i -> sum_(j=i+1)^r f_j + p+q+t;
       p -> u+v.

    B: for 0<=i<r,
         f_i -> sum_(j=i+1)^r f_j + t;
       p -> u+v.                                       (12)

All other rows, including s,f_r,u,v,q,t, vanish. For A, an x edge
out of f_i may be followed by constants through the remaining F states,
then f_r->p, p->q and q->t. These give exactly its displayed row.
The two x edges out of p have constant tails u->q->t and v->q->t;
their q and t contributions cancel, leaving u+v.

For B, each x edge out of f_i has the remaining F constants and
f_r->t as tails, giving its displayed F row. After the x edges out
of p, both constant tails reach q, then f_0 and every later F state,
then t. Every such coordinate occurs twice and cancels; only u+v
remains. Vertices u,v,q have no x edges, so their rows are zero even
though they have outgoing constant edges. This uses right closure,
which places constants after the row's first x, not before it.

The complete initial and final vectors in these same coordinates are

    alpha_A=alpha_B=e_s+sum_(i=0)^r e_(f_i)+e_p+e_q+e_t,
    beta_A=beta_B=e_t^T.                               (13)

In A the leading constant path runs from s through F to p,q,t. In B
it runs from s through p,q and F to t. Neither has a constant path to
u or v. These facts establish (13), including the nonzero empty-word
coefficient. They also account for all three connectors in each graph.
Since G's accepting polynomial is 1, the original products both accept
(1+x)^r, as also follows from the imported product formula.

### 4. The power mismatch for all r, including the complete r=1 case

Ignoring the zero s row/column only for this display, put
a=e_p+e_q and d=e_u+e_v. On the blocks F,G,t, (12) reads

    M_A = [ T   h a   h ]       M_B = [ T   0   h ]
          [ 0   D_G   0 ]             [ 0  D_G  0 ]
          [ 0    0    0 ],            [ 0   0   0 ].     (14)

Here aD_G=d and D_G^2=0. Because K_F commutes with J and has constant
term I, equation (11) gives

    T^r=J^r (I+J)^(-r)=J^r,
    T^(r+1)=0,
    T^(r-1)h=T^r e_(f_r)^T=e_(f_0)^T.                 (15)

For the first identity, every positive-degree term of (I+J)^(-r)
is killed by J^r, since J^(r+1)=0. No binomial-parity assumption is
needed. The last identity also holds for r=1, with T^0=I.

For ell>=2 the F-to-G block of M_A^ell is

    T^(ell-1) h a + T^(ell-2) h a D_G.                 (16)

Indeed, a product contributing to this block enters G once. It either
uses zero or one subsequent D_G factor; every term with two such
factors vanishes. Its F-to-t block is T^(ell-1)h, its F-to-F block
is T^ell, its G-to-G block is D_G^ell, and all other blocks vanish.
For M_B^ell the F-to-G block is zero and the other displayed blocks
have those same formulas. These descriptions cover every matrix entry.

Set ell=r+1. The F-to-t term is T^r h=T^(r+1)e_(f_r)^T=0.
The F-to-F and G-to-G terms vanish because r+1>=2. In (16) only
T^(r-1)h d remains, and (15) identifies it with e_(f_0)^T d.
This proves exactly (6), with two nonzero entries in M_A^(r+1).
Since u and v have zero rows, the next power of M_A is zero.
Also M_B^r has F-to-F block T^r=J^r!=0. The asserted nilpotency
indices follow.

For a fully explicit smallest instance, r=1 gives eight states. The
only nonzero rows are

    M_A: f_0 -> f_1+p+q+t,  p -> u+v;
    M_B: f_0 -> f_1+t,      p -> u+v.

Both initial rows are s+f_0+f_1+p+q+t and both final columns select t.
Multiplication gives just the f_0->u+v row in M_A^2 and no nonzero
row in M_B^2. This is an exact counterexample, not a sampled numerical
test or an inference from a matrix preview. The preceding formulas
prove the stronger statement for every r.

### 5. Failure of the template and the original resource denominator

The nonzero block in (6) survives addition of any zero block. Equation
(9) with ell=r+1 would require an invertible conjugate of that nonzero
matrix to be zero. Multiplication by P^(-1) and P would then make it
zero already, a contradiction. Thus the first equation of (4) fails
for every k and every pair of scalar invertible multipliers. The
boundary equations are not discarded: (8) shows exactly how they
would induce the intended scalar arrow, while (9) is already a
necessary transition obstruction independent of them.

Each original endpoint has r+7 vertices. Its edge list contains 2r
F occurrences, five G occurrences and three constant connectors,
so it has 2r+8 edges and g=5r+23. This proves (5). No size charge
can rescue an impossible equation. In particular identity stabilization,
matrix support, indices, repeated intermediate graphs and checking work
have nonnegative costs and are not claimed to fit any universal C here.
There is no constructed chain whose full ledger remains to be certified.
No finite-job cap, wire format or production receipt is changed.

The decisive feature is an unobservable cancelling branch, not a zero
accepted polynomial: G accepts 1, and every operand vertex lies on a
structural accepting path. Prefixing F extends a nilpotent channel that
is invisible at the final boundary, while suffixing F does not. Scalar
similarity retains that channel. A singular projection or a nontrivial
auxiliary representation could change it; neither is tested or ruled
out by this argument. This observation explains the limitation without
assuming any particular next quotient exists or is sparse.

## Mathlib

Full matching coverage for this endpoint counterexample and stable-shear
restriction is **not checked**. The similarity calculation, nilpotent
matrix powers and finite triangular inverses are elementary supporting
algebra; their availability would not supply a sparse bridge. The product
presentation is imported by the precise citation in §1. No theorem about
arbitrary scalar simulation chains or general complexity is imported or
inferred from this proof.

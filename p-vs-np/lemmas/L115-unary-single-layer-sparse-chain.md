# L115 — A sparse chain moves one 1+x layer past an arbitrary unary DAG

## Hypotheses

Work over F₂. G is a finite explicit acyclic occurrence graph with n>=1
vertices, designated roots p,q, c scalar-one edge occurrences and d x-edge
occurrences. Each label is a singleton. Parallel occurrences, cancellation,
disconnected vertices, arbitrary roots, coincident roots, empty accepting
paths and absence of accepting paths are allowed. No homogeneity, layering,
extremality of roots or restriction on consumed degrees is assumed.

F has two distinct vertices f0,f1 and precisely two parallel edge
occurrences f0->f1, labelled 1 and x. Let A=Prod(F,G), B=Prod(G,F) be
the independent products of L110 §21: fresh source s and sink t, disjoint
complete operand copies and three scalar-one connectors. Keep the original
endpoints, including all their occurrences. As in L110 §4, for each graph H
use its parity adjacency E_(H,0), E_(H,x) and

    K_H=(I+E_(H,0))^(-1), alpha_H=e_s K_H,
    M_H=E_(H,x) K_H,      beta_H=e_t^T.                 (1)

All inverses here are finite geometric sums on acyclic graphs. Set
g(H)=vertices+edges+singleton-label entries, before constant closure, and

    S=g(A)+g(B)=2n+4c+4d+28.                           (2)

An arrow U->V has a scalar matrix X with U rows and V columns, satisfying
alpha_U X=alpha_V, M_U X=X M_V, beta_U=X beta_V. Its support is the number
of nonzero scalar entries, including their separate coordinates; a factored
description does not replace the matrix support.

## Conclusion

There is a directly constructed five-arrow chain

    A -> A0* -> Q* <- R* -> B0* -> B,                   (3)

of right-closed acyclic singleton occurrence graphs. The stars denote the
explicit label substitution in the proof, not an unreceived closure oracle.
Its total scalar-map support is at most 6n+2c+3d+14<=3S. Charging each
intermediate graph separately at both incident arrows gives total size
28n+20c+48d+66<=14S. Support plus this repeated intermediate graph size
is therefore at most **17S**; including the two endpoints gives at most 18S.

This establishes the proposed single-layer primitive for arbitrary G.
It does not establish a uniform linear bound for arbitrary F, nor permit
iteration through arbitrarily many layers without charging every repeated
graph and map. Checking work and index bits are accounted for separately
below; no linear checking-work, fixed wire-byte, live-memory-cap or actual
job reception claim follows. Mixed-letter Dcomm, general availability and
ordinary P versus NP remain unresolved.

The construction is POTENTIALLY_NEW in the limited checkpoint sense: the
prior bounded assessment did not supply this quantitative construction.
There is no claim of certified originality or a new qualitative simulation
theorem. The universal statement below is symbolic; finite replay is only
a check on the formulas and their implementation.

## Proof

### 1. Imported conventions and the missing quantitative specialization

Reuse the pre-invocation EXPLORE assessment
`drafts/literature/2026-10-26-unary-product-sparse-quotient.md`.
The source convention and soundness are Ésik–Maletti, *Simulation vs.
Equivalence*, [2010 author manuscript, Definition 3.1 and soundness,
p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ is an allowed semiring, and its theorem permits arbitrary finite
boundary vectors. We import the fact that these equations preserve series;
we do not reprove qualitative existence or infer a size bound from it.
L110 §4 supplies the finite right-closure semantics, and §21 fixes the
independent product recipe, including arbitrary operand roots.

The inspected minimization/degree-copy results in the assessment do not
give this chain or its scalar-support ledger. The explicit construction
is needed for that uncovered quantitative difference. L112's full-cut,
L113's raw-first and L114's degree-coordinate failures are contrasts, not
mathematical premises of this construction. In particular no separate raw
constant-edge equation is imposed, and no monomial coordinate table or
Cartesian cut table is built.

### 2. Affine letter substitution preserves the same scalar maps

For any one acyclic unary graph with constant/letter adjacency C,D, let
T replace each x occurrence by two parallel occurrences labelled x and 1,
retaining all existing constants. Thus C becomes C+D and D stays D.
The common topological order is still valid, even if parallel occurrences
cancel in parity. Write K=(I+C)^(-1), M=DK, J=(I+M)^(-1). Since M is
strictly upper triangular in that order, J is a finite sum. The identity

    (I+M)(I+C)=I+C+D

gives K_T=KJ, M_T=MJ, alpha_T=alpha J, beta_T=beta.
If M_U X=X M_V, then (I+M_U)X=X(I+M_V), and multiplication by the two
finite inverses gives J_U X=X J_V. Consequently

    alpha_(TU) X=alpha_U J_U X=alpha_U X J_V=alpha_(TV),
    M_(TU) X=M_U J_U X=X M_V J_V=X M_(TV),
    X beta_(TV)=beta_U=beta_(TU).                       (4)

This proves preservation of all three equations with exactly the same X;
it neither reverses an arrow nor asserts a raw intertwiner. It also works
for general fixed boundary vectors, although all graphs used below have
unit source and sink boundaries. The inverse notation is used only in the
proof, not as dense stored map data.

### 3. A five-arrow construction for one x edge

Temporarily let H be any allowed unary operand with n vertices, constant
adjacency C and letter adjacency D. Denote unit row e=e_p and unit column
b=e_q^T, and set

    K=(I+C)^(-1), W=I+C, N=DK, a=eK, z=Kb, gamma=ab.

Let P_x be the two-vertex operand consisting of the single edge f0->f1
labelled x. Write A_x=Prod(P_x,H), B_x=Prod(H,P_x). The same symbols for
operand vertices in different graphs mean independent copies. All edges
listed below are occurrence lists, and every C or D occurrence is copied
separately; these lists are exhaustive.

* A0 has vertices s,a0,H,t. Its edges are s->a0 (1), a0->p (x), all H
  edges and q->t (1).
* B0 has vertices s,H,t. Its edges are s->p (1), all H edges and q->t (x).
* Q has vertices s,U_v,V_v (v in H),t. Its constant edges are s->V_p,
  every U_u->U_v corresponding to a C occurrence, every U_u->V_v
  corresponding to a D occurrence, and U_q->t. Its x edges are precisely
  V_v->U_v, one for every vertex v.
* R has vertices s,U_v,V_v,t. Its constants are s->V_p and two separate
  copies of every C occurrence, within U and within V. Its x edges are
  every V_u->V_v corresponding to a D occurrence, all V_v->U_v, and
  V_q->t.

All four graphs have fresh source s and sink t and their unit boundaries.
For Q and R, put s first, then V_v,U_v in H's topological vertex order,
then t. Every listed edge goes forward. This remains true for nonextremal
p,q, p=q, disconnected states or absent accepting paths. A0 and B0 are
also acyclic by inserting their fresh boundary vertices around H.

For clarity the following display gives the *whole* right-closed
transition matrices: unlisted rows and entries are zero. The symbol a
in a row expression is the row vector eK, not the state a0.

    A_x: row f0 -> f1 + a on H + gamma t;
         rows H -> N on H + N b on t.
         alpha=s+f0, beta=t.

    A0:  row a0 -> a on H + gamma t;
         rows H -> N on H + N b on t.
         alpha=s+a0, beta=t.

    Q:   rows V -> K on U + K D on V + K b on t.
         alpha=s+V_p, beta=t.

    R:   rows V -> K on U + D K on V + b on t.
         alpha=s+a on V, beta=t.

    B0:  rows H -> N on H + b on t.
         alpha=s+a on H, beta=t.

    B_x: rows H -> N on H + N b on f0;
         row f0 -> f1+t.
         alpha=s+a on H+gamma f0, beta=t.                (5)

These formulas follow directly by taking constants *after* each x edge
and taking all constants from s for alpha. For example Q's constant
closure from U is (K,KD,Kb) on U,V,t because V and t have no outgoing
constant edges; R's constant closure stays inside each C copy. In B_x
the constant connector q->f0 is included in every constant tail, whereas
f0->f1 is an x edge and f1->t is constant. This accounts for every
connector. A_x's f1 is retained in (5), even though its transition row
and final coordinate vanish. No full suffix polynomial is substituted for
the right-closed state residual.

The five matrices are specified by all their nonzero row formulas;
unlisted entries are zero and repeated scalar terms add in F₂:

    X1: A_x -> A0
        s->s, f0->a0, f1->0, H_v->H_v, t->t.

    X2: A0 -> Q
        s->s, a0->V_p, H_u->U_u+sum_v D_uv V_v, t->t.

    X3: R -> Q
        s->s, U rows -> W on U, V rows -> W on V, t->t.

    X4: R -> B0
        s->s, U_v->0, V_v->H_v, t->t.

    X5: B0 -> B_x
        s->s, H_u->H_u+b_u f0, t->f1+t.                (6)

No map requires K, a, z, N or any coefficient
table to be materialized. The matrices use only identity entries, root
indicators, D and W=I+C. Acyclicity ensures C has zero diagonal, so the
identity entries in W do not cancel with constant loops.

### 4. Every oriented equation

For X1, projecting away f1 in the first line of (5) gives exactly the
A0 rows; the zero f1 row maps to zero. Initial and final vectors project
to s+a0 and t. Thus all three equations hold.

For X2, the a0 transition row on the left, after applying X2, is
(a,aD,gamma) on U,V,t. On the right it is the V_p row of Q, namely
(eK,eKD,eKb), the same row. Each H row on the left is (N,ND,Nb);
on the right U rows contribute zero and the D combination of V rows
gives (DK,DKD,DKb), again identical. The s,t rows are zero on both
sides. Initial vectors give s+V_p. Only t maps with a nonzero final
coordinate, so the entire final-vector equation also holds.

For X3 the only nonzero transition rows to check are V rows. On the
left M_R X3 has blocks (KW,DKW,b)=(I,D,b). On the right X3 M_Q has
(WK,WKD,WKb)=(I,D,b). The s,U,t rows are zero on both sides. Also
alpha_R X3=s+eKW on V=s+V_p, and the only final coordinate is the
unchanged t. This verifies both boundary equations without treating K
as sparse or swapping the order of D and K.

For X4, projection removes the U block of R and leaves (DK,b) on H,t,
precisely B0's transition rows. Initial vectors give s+a, and t remains
the sole final coordinate; the zero U rows cause no extra equation.

For X5, in each H row the left side M_B0 X5 gives

    N on H, N b on f0, b on f1, b on t.

The right side is the H row of B_x plus b times its f0 row, which is
the same expression. The s row is zero, and the t row maps to f1+t,
both of whose transition rows vanish. The initial vector maps to
s+a on H+ab f0, exactly alpha_Bx. The t row has final value one and
every other source row has final value zero. This checks X5 completely.

This proves A_x->A0->Q<-R->B0->B_x. The proof did not assume existence
of any path, a nonzero series, unique paths, distinct p,q, or homogeneous
vertices. All additions already include parallel cancellation.

### 5. Return to the exact 1+x endpoints

Take H=T(G): its occurrence counts are c_H=c+d and d_H=d, with constant
adjacency C_H=C_G+D_G and letter adjacency D_H=D_G. Build (6) for this
H and apply T once to every graph in that chain. Equation (4) proves
that precisely the same five scalar matrices remain valid.

The first operand T(P_x) is exactly the required two-edge F. In the other
operand T(T(G)), each original x occurrence remains an x occurrence and
has acquired two parallel constant occurrences. They cancel in parity;
original constant occurrences are unchanged. Thus the transformed A_x
and B_x have exactly the same vertex-indexed C,D, initial and final
vectors as the *original* independently built A,B. Their representations
(1) are identical. We therefore use the original A,B in (3), not inflated
endpoints with extra cancelling occurrences. This replacement is justified
by full adjacency equality, not merely equality of the accepted series.

The intermediate graphs A0*,Q*,R*,B0* retain every occurrence produced
by the constructions and by T, even cancelling parallel constants.
Their maps use D_G and W=I+C_G+D_G. In particular this construction
does not change the denominator, silently coalesce endpoint edge records,
or require a common accepting core of the two endpoints.

### 6. Support, repeated graphs, boundaries, indices and work

The support bounds for the five maps in order are

    n+3, n+d+3, 2n+2c+2d+2, n+2, n+4.

These sum to 6n+2c+3d+14. Parallel cancellation can only reduce support;
all graph occurrences are nevertheless charged. The intermediate ledger
after the second substitution is exact, with every edge a singleton:

| Graph | Vertices | Edges (and label entries) | g |
| --- | ---: | ---: | ---: |
| A0* | n+3 | c+3d+4 | n+2c+6d+11 |
| Q* | 2n+2 | c+2d+2n+2 | 6n+2c+4d+6 |
| R* | 2n+2 | 2c+4d+2n+3 | 6n+4c+8d+8 |
| B0* | n+2 | c+3d+3 | n+2c+6d+8 |

Their sum is 14n+10c+24d+33. Each occurs at two arrows, so even charging
two complete copies gives 28n+20c+48d+66. Combining with the support
bound gives 34n+22c+51d+80<=17S by (2). Separately, support<=3S and
repeated graph size<=14S. These inequalities hold for all n>=1,c,d>=0;
acyclicity imposes no extra size hypothesis needed for them.

Counting graph occurrences at every arrow, including endpoints once,
the total vertex count is 14n+26. Dense alpha and beta vectors therefore
have 28n+52 field-bit positions; retaining eta/theta as well doubles
that to 56n+104. This does not assume sparse alpha: constants can make
it dense. A topological permutation for every such graph occurrence has
14n+26 indices. Let L=ceil(log2(2n+4)), an upper bound for every graph's
vertex-index width. Each scalar support entry can be stored with two
L-bit indices and one field bit; edge records likewise need endpoint
indices and label data. These are O(S log(S+2)) bit bounds, not a claim
that the scalar count is a literal byte count or a complete wire format.
Root indices, list lengths, tags and framing must also be encoded.

Graphs and unsummed map entries are generated from individual operand
vertices/edge occurrences; no path, cut or degree enumeration occurs.
Scalar entries with repeated coordinates can be coalesced by parity with
deterministic sorting. This has O(S log(S+2)) comparison work and O(S)
stored records in an ordinary indexed representation. Input validation
also scans every occurrence and checks a topological order. No unchecked
source file or fixed-job binding is thereby received.

The temporary substituted endpoints in §§3–5 serve the algebraic proof;
they are not additional intermediates of (3). The final graphs and maps
can be written directly from G's occurrence lists, using C_H=C_G+D_G
and D_H=D_G. The diagnostic replay below retains extra temporary graphs
to check the substitution explicitly; their storage is not claimed to fit
the 17S chain ledger or any complete wire/live bound.

Here is an explicit, conservative equation-checking procedure. For an
arrow U->V of dimensions u,v, compute K_U X columnwise by reverse
topological constant-edge propagation, then apply E_(U,x). Independently,
for each row of X compute its E_(V,x) action and forward constant closure
as in L110 §4. Compare all uv entries of M_U X and X M_V. Including
initialization/copy/comparison scans this uses at most

    4uv + v*|E(U)| + u*|E(V)|                         (7)

field-position operations for the transition calculation, apart from
loop/index management. Boundary closures and sparse map actions require
additional O(u+v+|E(U)|+|E(V)|+support(X)) field operations. All five
checks together are O(S²), with a straightforward O(S²) field-position
storage bound if rectangular arrays are retained. This is a finite upper
bound, not a claim of linear checking work or a measured live-byte cap.
All equations in §§2–5 were checked symbolically, so (7) is not a proposed
finite experiment substituted for their proof.

### 7. Finite replay and the remaining continuation

The original replay used the script's default `output-529` destination.
To reproduce it, select a fresh output directory (existing evidence is
never overwritten), for example:

```bash
python3 scripts/unary-single-layer/check_chain.py \
  --output scripts/unary-single-layer/output-529-replay
```

The matrix replay constructs full
occurrence graphs/maps, computes finite closures by matrix powers and
checks every coordinate of every equation, including the transformed
endpoint comparison and the graph/support ledger. Its full certificate
and bounded aggregate results are under
`scripts/unary-single-layer/output-529/`. The completed run checks all 593
graphs/root pairs with n<=3, each forward vertex pair carrying at most
one occurrence of each label, plus 24 root choices on three parallel-edge
fixtures: 617 cases and 6,170 arrows across the two phases, with no
equation, endpoint or ledger failure. Every coordinate is compared, not
sampled. The largest observed support/S, repeated-graph/S and combined/S
ratios are respectively about 0.942, 6.618 and 7.324, against the proved
bounds 3,14,17. These observations do not prove the universal statement or
generalize it to other operands F.

The useful local input is the five-arrow primitive with a universal
constant for arbitrary G; the general target still requires arbitrary F.
Successive applications across many layers must count all copies and
intermediate incidences. A bound linear in S for each *individual* move
does not imply one for their composition. A next construction must share
or avoid that repeated cost and verify its own boundary/transition maps.
No raw-first or degree-basis route is reopened, and no stopped receiver
contract, production format or cap has changed.

## Mathlib

Full matching coverage for this particular sparse five-arrow construction
and its occurrence ledger is **not checked**; no absence claim is made.
The imported simulation convention/soundness is cited in §1. The finite
matrix identities, explicit maps, applicability to all stated graph cases
and resource qualifications are proved here. General matrix and nilpotent
geometric-sum algebra would be supporting ingredients, not a matching
library theorem establishing this whole result.

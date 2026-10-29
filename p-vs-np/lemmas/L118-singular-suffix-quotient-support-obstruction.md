# L118 — A singular operand-preserving suffix quotient forces superlinear support

## Hypotheses

Work over F₂. Let G be a finite acyclic occurrence graph with n>=1
vertices, c scalar-one edge occurrences, d x-edge occurrences, and
designated roots p,q. Every label is a singleton. Parallel occurrences,
cancellation, arbitrary or coincident roots, empty accepting paths,
no accepting paths and disconnected vertices are allowed. No unique
consumed degree, layering or root extremality is assumed.

For r>=1, F_r has vertices f_0,...,f_r, roots f_0,f_r, and two parallel
occurrences f_i->f_(i+1), labelled 1 and x, at each layer. Let
A=Prod(F_r,G) and B=Prod(G,F_r) be L110 §21's independent products:
disjoint whole operand copies, fresh source s and sink t, and three
constant connectors in the indicated order. The endpoints and their
occurrence counts are not padded, trimmed or replaced by their series.

For any graph J use L110 §4's right closure, with parity adjacencies C_J,D_J:

    K_J=(I+C_J)^(-1), alpha_J=e_s K_J,
    M_J=D_J K_J,      beta_J=e_t^T.                     (1)

Inverses are finite sums in a topological order. Set g(J)=|V(J)|+2|E(J)|,
counting each singleton-label entry separately, and S=g(A)+g(B).

The specified **suffix quotient Q** has the following complete data:

* vertices s, all vertices of one independent copy of G, d_0,...,d_(r-1),t;
* all original G edge occurrences, unchanged;
* constant edges s->p and q->d_0;
* parallel 1/x edges d_i->d_(i+1) for 0<=i<r-1;
* parallel 1/x edges d_(r-1)->t.

Its roots are s,t. A topological order puts s first, G in its own
topological order, then the delay chain and t. Thus Q is acyclic even
for arbitrary p,q. It keeps operand-state coordinates and only one
boundary-delay chain; no Cartesian cuts, all-state delay copies or
degree-expanded operand are used.

The proposed chain is A->Q<-B, with full scalar matrices X,Y satisfying

    alpha_A X=alpha_Q, M_A X=X M_Q, X beta_Q=beta_A;
    alpha_B Y=alpha_Q, M_B Y=Y M_Q, Y beta_Q=beta_B.       (2)

The matrices have endpoint rows and Q columns. Their support counts
every nonzero scalar entry, including its separate coordinates, rather
than a formula or factorization describing entries. The word quotient
here specifies the common target of (2); no surjectivity, functional-map
or idempotence hypothesis is imposed. No separate raw constant/letter
intertwiner is required.

## Conclusion

For every allowed G,r, explicit rectangular scalar maps (2) exist.
They annihilate the f_r coordinate, and do not require an invertible
similarity. The graphs have

    S=2n+10r+4c+4d+18,
    g(Q)=n+5r+2c+2d+6,    2g(Q)=S-6.                  (3)

Nevertheless, set r=N=2^k for k>=0 and take G to be the N-edge pure-x
path h_0->...->h_N, with its extremal roots. For this allowed family,
**every** X satisfying even the transition and final equations in (2)
has support at least 3^k. Here S=16*2^k+20. Consequently no universal C
can bound support(X)+support(Y)+2g(Q) by C*S for this specified quotient,
even if both constructed maps are replaced by arbitrary scalar maps.

This is a local REPRODUCTION/specialization of scalar simulation and
polynomial-coordinate algebra, not a new qualitative equivalence theorem
or a claim of originality beyond the sources checked. It stops this
operand-preserving suffix quotient. It does not exclude different
coordinates, auxiliary graphs, arrow orientations or longer chains.
It supplies neither an actual fourth-comparison receipt nor a general
certificate lower bound or a resolution of P versus NP.

## Proof

### 1. Imported inputs and the quantitative difference being tested

Reuse the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-26-unary-product-sparse-quotient.md`.
Scalar simulation and its series soundness are imported from Ésik–Maletti,
*Simulation vs. Equivalence*, [2010 author manuscript, Definition 3.1
and soundness, p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ is an allowed semiring and finite arbitrary boundary vectors are
allowed. This qualitative input does not bound scalar support.

L110 §§4,21 fixes closure and the exact wrapped product, including
arbitrary operand roots. L115 §2 proves that replacing every x edge by
parallel 1/x edges preserves the same scalar maps after right closure;
that result is applied, not reproved below. The binary coefficient-count
identity is reused from L114 §4. These inputs leave the full maps to this
specific Q and their necessary support to be checked here. No inspected
source supplies the claimed linear certificate, and no novelty follows
from that absence of coverage. L116's all-state delay and L117's scalar
similarity restrictions are comparisons, not premises of this proof.

### 2. Pure-letter presentation and every closed transition row

Temporarily let P_r be the r-edge pure-x path f_0->...->f_r, and let H
be any allowed unary operand. Write

    K=(I+C_H)^(-1), N=D_H K, a=e_p K,
    b=e_q^T, gamma=ab.                                 (4)

Let A0=Prod(P_r,H), B0=Prod(H,P_r). Let Q0 have the same vertex scheme
as Q, the original H occurrences, constants s->p and q->d_0, and just
one x edge at each of its r delay steps (the last step ends at t).
These occurrence lists are exhaustive. All graphs are acyclic with
fresh s,t, independently of the positions of p,q in H.

The following display gives their entire right-closed matrices; all
unlisted rows and entries are zero. An expression on H denotes all its
coordinates, not an uncharged auxiliary graph.

    A0: alpha=s+f_0; beta=t.
        f_i -> f_(i+1)                         (0<=i<r-1);
        f_(r-1) -> f_r + a on H + gamma t;
        H rows -> N on H + N b on t.

    B0: alpha=s+a on H+gamma f_0; beta=t.
        f_i -> f_(i+1)                         (0<=i<r-1);
        f_(r-1) -> f_r+t;
        H rows -> N on H+N b on f_0.

    Q0: alpha=s+a on H+gamma d_0; beta=t.
        d_i -> d_(i+1)                         (0<=i<r-1);
        d_(r-1) -> t;
        H rows -> N on H+N b on d_0.                   (5)

For example, after an H letter in A0, a constant tail can stay in H or
reach q and then t; these give N and Nb. In B0/Q0 the extra constant
tail instead ends at f_0/d_0. After A0's last delay letter, constants
can visit f_r, H with row a, and t with coefficient gamma. After B0's
last delay letter they can visit f_r and t. No initial leading constant
can pass a pure delay x edge. These facts prove every entry of (5),
including all three original connectors and the empty-word boundaries.
In particular f_r has zero transition row and zero final coordinate.
The formulas do not assume that p,q are distinct, extremal, reachable
or connected by any path.

### 3. Both full rectangular maps and all oriented equations

Define Y0:B0->Q0 by identifying s,H,t, sending f_i to d_i for i<r,
and sending f_r to zero. Define X0:A0->Q0 by the complete row formulas

    s -> s;  t -> t;  f_r -> 0;

    f_i -> a N^i on H
           + sum_(j=0)^i (a N^(i-j)b) d_j      (0<=i<r);

    H rows -> N^r on H
              + sum_(j=0)^(r-1) (N^(r-j)b) d_j.        (6)

All omitted entries are zero. The last line describes all n source rows,
with the displayed column vectors giving the respective d_j columns.
All powers and coefficients are finite scalar computations; they are
not asserted sparse or free. Repeated scalar contributions add in F₂.

For Y0, every H row in (5) projects from (N,Nb f_0) to (N,Nb d_0);
the first r-1 delay rows project to the corresponding delay rows; the
last delay row projects f_r+t to t. The zero s,f_r,t rows have zero
images under the transition on both sides. Initial vectors project to
s+a+gamma d_0, and only t has a nonzero final coordinate. Thus all three
equations for Y0 hold.

For X0, the initial equation is

    (s+f_0) X0=s+a on H+gamma d_0=alpha_Q0.

Only its t row has a t entry, with value 1, which proves the entire
final-vector equation. The s,f_r,t transition equations are zero on
both sides. If 0<=i<r-1, multiplying its f_i image in (6) by M_Q0 gives

    a N^(i+1) on H + (a N^(i+1)b) d_0
      + sum_(j=0)^i (a N^(i-j)b) d_(j+1),

exactly the f_(i+1) image. At the last delay row, its image times M_Q0 is

    a N^r on H
      + sum_(j=0)^(r-1) (a N^(r-j)b) d_j + gamma t.

This equals (f_r+a on H+gamma t)X0, checking that entire row even when
r=1 and the preceding range of delay rows is empty. For all H rows,
the two products are respectively

    M_A0 X0: N^(r+1) on H
              + sum_(j=0)^(r-1) N^(r+1-j)b d_j + Nb t;

    X0 M_Q0: N^(r+1) on H + N^(r+1)b d_0
              + sum_(j=0)^(r-2) N^(r-j)b d_(j+1) + Nb t.

These agree by the indicated index shift, with an empty sum when r=1.
This checks every matrix row and both boundaries; equality of accepted
polynomials was not substituted for any transition equation.

### 4. Return to the original endpoints, including the cancelling fixture

Let T replace each x occurrence by parallel x and 1 occurrences, keeping
existing constants. In §§2–3 take H=T(G), so

    C_H=C_G+D_G, D_H=D_G,
    K=(I+C_G+D_G)^(-1), N=D_G K, a=e_p K.              (7)

Apply T to A0,B0,Q0. L115 §2 shows that the same X0,Y0 still satisfy
all three closed equations. T(P_r)=F_r. In T(H)=T(T(G)), every original
x occurrence has acquired precisely two constant occurrences with the
same endpoints. These cancel in parity, while its x occurrence and
every original constant occurrence remain. Thus T(H) and G have exactly
the same vertex-indexed C,D and the same designated roots.

It follows that T(A0),T(B0) have exactly the closed representations of
the original A,B, and T(Q0) has exactly the closed representation of
the directly specified Q. We therefore take X=X0,Y=Y0 using (7).
No original endpoint record is modified or enlarged. Q is built directly
from its stated occurrence list, rather than from the extra cancelling
constants used only in this proof. Full adjacency equality justifies
the replacement, not merely semantic equality of two series.

In particular these maps pass the L117 cancelling-branch test. Explicitly,
take G with vertices p,u,v,q, constants p->q,u->q,v->q, and x edges
p->u,p->v, rooted at p,q. Put delta=e_u+e_v. Here the parity matrices
have C_G^2=D_G^2=C_G D_G=D_G C_G=0; the last product has two p-to-q
terms and they cancel. Formula (7) consequently gives

    N=D_G, N^2=0, Nb=0, a=e_p+e_q+delta, gamma=1.

The complete X rows on this fixture simplify to

    s->s, t->t, f_r->0, f_0->a+d_0;
    if r=1: H rows -> D_G on H;
    if r>=2: H rows ->0, f_1->delta+d_1,
             f_i->d_i for 2<=i<r.

Y remains the stated projection in every case. This is an explicit
specialization of all equations already checked, not an appeal to
equal output polynomials. In particular X kills the cancelling row
delta, and the construction does not preserve the nilpotency index
that obstructed invertible similarity. No assertion of a full-row-rank
map follows; such a rank condition was never part of (2).

### 5. Forced support for a path operand, for every possible map to Q

Set r=N=2^k and let G be the pure-x path with vertices h_0,...,h_N,
edges h_i->h_(i+1), roots h_0,h_N. This is an allowed operand with
n=N+1,c=0,d=N. The endpoint series is (1+x)^N x^N in both orders.

For any graph J and vertex v define its right-closed residual polynomial

    R_(J,v)(z)=sum_(ell>=0) (e_v M_J^ell beta_J) z^ell. (8)

Nilpotence makes this a finite sum; z marks the degree of the one letter,
not a second input letter. A nonfinal state's residual has zero constant
coefficient and must begin with an x edge. Leading constants are not
included in e_v M_J, so (8) is not an arbitrary full suffix polynomial.

The complete residuals of Q on this family are

    R_(Q,h_i)=z^(N-i)(1+z)^N                  (0<=i<N);
    R_(Q,d_j)=z(1+z)^(N-j-1)                  (0<=j<N);
    R_(Q,t)=1,  R_(Q,s)=R_(Q,h_N)=0.                   (9)

For h_i the path first takes N-i pure letters, then the constant
connector and any choice of the N suffix layers. For d_j it must first
take its letter edge, then can choose either occurrence in each of the
remaining N-j-1 layers. Vertices s,h_N have only outgoing constants,
so their transition rows and residuals are zero. This proves every case
in (9) using the right-closure convention.

In A the complete analogous list is

    R_(A,h_i)=z^(N-i)                         (0<=i<N);
    R_(A,f_i)=z^(N+1)(1+z)^(N-i-1)            (0<=i<N);
    R_(A,t)=1,
    R_(A,s)=R_(A,f_N)=R_(A,h_N)=0.                     (10)

For h_i only the pure-letter suffix and final constant connector remain.
For f_i the first letter is followed by the remaining F layers and all
N letters of G. These account for all cases in (10).

Now let Z be **any** scalar matrix satisfying M_A Z=Z M_Q and
Z beta_Q=beta_A. Iterating the transition equation yields, for each
ell>=0, M_A^ell beta_A=Z M_Q^ell beta_Q. Taking the complete finite
coefficient sums therefore gives, for every source row v,

    R_(A,v)=sum_w Z(v,w) R_(Q,w).                      (11)

The nonzero polynomials in (9) have distinct degrees: respectively
2N,2N-1,...,N+1; N,N-1,...,1; and 0. Each is monic. They are linearly
independent, since the highest-degree nonzero summand in any nonempty
combination cannot cancel. Thus (11) uniquely fixes all coordinates
except the zero-residual columns s,h_N. Those two columns cannot change
or reduce any other required coordinate.

For a row h_i of A put l=N-i, so 1<=l<=N. Its residual z^l has degree
at most N. The unique expression in (9) has zero coefficients on every
Q h_i column, and its delay coefficients are exactly

    z^l = z*((1+z)+1)^(l-1)
        = sum_(j=0)^(l-1) binom(l-1,j) z(1+z)^j.       (12)

These are the separate columns d_(N-1-j); all coefficients are taken
modulo two. Its t coefficient is zero. By the exact binary-support
identity in L114 §4, the number of nonzero coefficients in this row
is 2^popcount(l-1), and their sum for l=1,...,2^k is 3^k. Hence

    support(Z) >= sum_(l=1)^N 2^popcount(l-1) = 3^k.   (13)

This bounds every possible first arrow, without even needing its initial
equation. It is stronger than finding a dense implementation of (6).
Arbitrary entries in unobservable columns, cancellation in generating
formulas and an alternative second map cannot remove these forced entries.
The use of L114 is its existing binary-count identity; the quotient,
operand family, residual basis and required map coordinates here differ
from that lemma's monomial-degree quotient.

### 6. Original denominator, repeated graphs and complete scope of the stop

Each original endpoint has n+r+3 vertices and c+d+2r+3 singleton edge
occurrences. Q has n+r+2 vertices and c+d+2r+2 occurrences. This proves
(3), counting Q once at each of its two incident arrows. Y has exactly
n+r+2 nonzero entries. Formula (6) gives the conservative finite bound

    support(X)<=n^2+2nr+r(r+1)/2+2,

not a uniform linear bound. The matrix powers in that formula must be
computed and their entries charged if this certificate is materialized.

For the family of §5, S=16N+20<=36N and 2g(Q)=16N+14=S-6. By (13),

    support(Z)/S >= (1/36)*(3/2)^k.

For any proposed universal C choose k with (3/2)^k>36C. The first
map alone then exceeds C*S. Nonnegative costs of the other map, the
twice-counted intermediate graph, indices and boundaries cannot repair
this failed threshold. There is no reliance on a finite large example.

For clarity, the other costs are not silently identified with support.
Counting both endpoints once and Q twice gives 4n+4r+10 vertex positions.
Their dense initial/final vectors use 8n+8r+20 field-bit positions, and
their topological permutations need 4n+4r+10 indices. A map entry can
use two ceil(log2(n+r+3))-bit indices and one field bit, before framing;
edge records, roots and tags also need encoding. These charges do not
reduce (13), and no complete byte or live-memory claim is made.

All maps are finite: K and each N action can be computed by topological
edge sweeps, and (6) by successive powers on the n unit rows and a.
This may be dense. L115 §6's column/row sweep checker applies to either
arrow, checking every u-by-v entry with at most
4uv+v|E(U)|+u|E(V)| field-position operations for the transition check,
plus boundary work. Here it gives an O(S^2) check if rectangular arrays
are retained. No linear checking-work or measured storage-cap result is
asserted, and no mathematical script or finite receipt is used in this
symbolic proof.

The graph proposal successfully removes a redundant state and permits
singular maps, including on the cancelling fixture. What fails is its
fixed observable residual basis: on the path family it forces a dense
change of coordinates. This rules out the specified suffix quotient,
not all operand-adapted representations. The construction uses no
all-state delay interface or invertible change, so it is not merely an
instance of L116 or L117. Different intermediate bases and zigzags,
general F, mixed-letter Dcomm, actual input/occurrence reception, full
wire/work/live bounds, general availability and unrestricted complexity
consequences remain unresolved.

## Mathlib

Full matching coverage for this quotient construction and its support
obstruction is **not checked**; no absence claim is made. The external
simulation theorem and its hypotheses are identified in §1. Finite
triangular inverses, polynomial coordinates and binary coefficient counts
are supporting algebra; their availability does not provide a linear
certificate for the original endpoints.

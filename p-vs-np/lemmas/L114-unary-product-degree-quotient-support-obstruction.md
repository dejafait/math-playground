# L114 — A direct degree quotient has superlinear scalar-map support

## Hypotheses

Work over F₂ with the finite singleton-labelled acyclic occurrence graphs
and independent serial-product recipe of L110 §§3–4,21. An edge is labelled
either scalar one or the original unary letter x. Count
g(H)=|V(H)|+|E(H)|+number of singleton-label entries, before constant
closure. The endpoints are fixed; no padding or semantic replacement is
allowed in the denominator S=g(A)+g(B).

For k>=0 set n=2^k. Let F have vertices v_0,...,v_n, designated roots
v_0,v_n, and exactly two separate edge occurrences v_i -> v_(i+1),
one labelled 1 and one labelled x, for every 0<=i<n. Let G have a single
vertex w, no edges, and both designated roots w. Thus G's only accepting
path is its empty path. Let A=Prod(F,G), B=Prod(G,F), each with fresh source
s, fresh sink t, disjoint full operand copies, and three scalar-one
connectors. Vertex names below refer to the separate copies in each graph.

For H=A,B use the right-closed representation

    K_H = sum_(j=0)^(|V(H)|-1) E_(H,0)^j,
    alpha_H = e_s K_H,    M_H = E_(H,x) K_H,    beta_H=e_t^T.

The particular proposal tested here is the common **monomial-degree**
representation Q, built directly, without any Cartesian cut table. Its
vertices are a fresh source a and q_0,...,q_n; its sink is q_0. Its x edges
are q_j -> q_(j-1) for 1<=j<=n. Its only constant edges are a -> q_0
and a -> q_n. The chain sought through this specified Q is

    A -> Q <- B,

with explicit scalar matrices X_H indexed by V(H) times V(Q), satisfying

    alpha_H X_H = alpha_Q,    beta_H = X_H beta_Q,
    M_H X_H = X_H M_Q.                                  (1)

No raw constant-edge intertwiner is required. The support of a matrix
is the number of its nonzero scalar entries, not the length of a program
or a factored expression describing it. Other bases, other intermediates,
reverse arrows and longer zigzags are outside the negative conclusion.

## Conclusion

The three graphs have the same unary series (1+x)^n=1+x^n, and

    S=10n+20,             g(Q)=3n+6.

Both arrows (1) exist. For each H=A,B the minimum possible support of
any matrix satisfying (1) is exactly 3^k+2. Consequently the chain has
minimum total support 2*3^k+4, and

    (2*3^k+4)/(10*2^k+20) -> infinity.

There is no universal C bounding this proposal's support by C*S, even
though its summed intermediate graph size is linear in S. This is an
explicit specialization/calculation for known coefficient coordinates,
recorded as REPRODUCTION; no new general simulation theorem or certified
novelty is claimed. It rejects this degree-coordinate proposal, not the
gate target's existential claim for all possible sparse scalar chains.
It supplies neither a fourth fixed-job receipt nor a P-versus-NP result.

## Proof

### 1. Imported conventions and why the computation is needed

Reuse the prior EXPLORE assessment
`drafts/literature/2026-10-26-unary-product-sparse-quotient.md`.
The oriented scalar equations are Ésik–Maletti, *Simulation vs.
Equivalence*, [2010 author manuscript, Definition 3.1 and soundness,
p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ is an allowed semiring and arbitrary finite boundary vectors are
allowed. Soundness is imported, not reproved; its qualitative existence
results supply no support bound. L110 §4 supplies the finite right-closure
coefficient semantics and §21 the product recipe, including coincident
operand roots. The separate scalar-one intertwining condition rejected
in L113 is not imposed here.

The reviewed degree-copy and minimization statements do not evaluate
explicit scalar-map support for these fixed endpoints. The calculation
below is necessary to test that missing quantitative condition. It is not
a reproof of a matching sparse-quotient theorem, nor an inference of
novelty from the review's failure to find one.

### 2. All graph data and all right-closed state residuals

The three connectors of A are s -> v_0, v_n -> w, w -> t; those of B
are s -> w, w -> v_0, v_n -> t. Each is labelled 1. Together with F's
listed edges these exhaust the graph. The constant subgraph in each
endpoint is one path through all its vertices, so alpha_H has a 1 in
every coordinate, and no edge enters s. Each endpoint has n+4 vertices,
2n+3 edges and 2n+3 label entries. Hence g(H)=5n+10 and S=10n+20.

Every accepting path in F independently chooses 1 or x at each layer,
so its polynomial is (1+x)^n. The other operand and all connectors
contribute scalar one. In characteristic two, repeated squaring of
(1+x)^2=1+x^2 gives (1+x)^(2^k)=1+x^(2^k). This proves the stated
endpoint polynomial without a numerical or sampled identity test.

For each endpoint vertex u define the finite right-closed residual

    h_u(z) = sum_(d>=0) (e_u M_H^d beta_H) z^d.          (2)

Here z is a commuting degree marker for the single original x, not an
additional input letter. Nilpotence makes the sum finite. At vertices
other than t, the d=0 coefficient is zero. If u=v_i, i<n, any positive
length closed walk counted by (2) must begin with the one x edge
v_i -> v_(i+1), because M_H=E_x K_H permits no leading constant segment.
After that first letter it may take any path through the remaining
n-i-1 layers, followed by the unique constant tail to t. Constant-segment
decomposition in L110 §4 counts each such path once, with parity. Thus

    h_(v_i)(z)=z(1+z)^(n-i-1)  (0<=i<n),
    h_t(z)=1,    h_s(z)=h_(v_n)(z)=h_w(z)=0.             (3)

These formulas hold for both orders of the operands: the position of w
changes only the constant tail or the leading segment, and w itself has
no outgoing x edge. In particular a full suffix polynomial starting with
arbitrary constants is NOT substituted for (2).

For Q the closure is I+E_(Q,0), and E_(Q,x)E_(Q,0)=0 since no x edge
ends at a. Therefore

    alpha_Q=e_a+e_(q_0)+e_(q_n),
    beta_Q=e_(q_0)^T,       M_Q=E_(Q,x),
    M_Q^d beta_Q=e_(q_d)^T (0<=d<=n),
    M_Q^d beta_Q=0         (d>n).                       (4)

Its series is exactly 1+z^n. Q has n+2 vertices and n+2 singleton edges,
so g(Q)=3n+6. All statements include k=0, n=1; q_0 and q_n are distinct.

### 3. Explicit maps and verification of every equation

For each H define the complete matrix, with no implicit nonzero entries,
by

    X_H(u,a)=1 if u=s, and 0 otherwise;
    X_H(u,q_j)=[z^j]h_u(z),       0<=j<=n.              (5)

First, X_H beta_Q equals beta_H, since the constant term of (2) is
e_u beta_H for every u. Next the finite residual definition implies

    [z^(j+1)]h_u = sum_v M_H(u,v)[z^j]h_v.

All h_u have degree at most n. For columns q_j with j<n this is exactly
M_H X_H = X_H M_Q, since the right side in column q_j is X_H(u,q_(j+1)).
For q_n both sides vanish by the degree bound. In column a the right
side is zero, and the left side is M_H e_s^T=0: no graph path enters s,
so no E_x K_H entry has column s. This checks the entire transition
matrix, including its zero columns, without requiring raw intertwining.

Finally, alpha_H is the all-ones row. In column a its product with X_H
is 1. In the remaining columns its coefficient polynomial, using (3), is

    sum_u h_u(z) = 1 + z sum_(r=0)^(n-1)(1+z)^r
                 = (1+z)^n = 1+z^n.                  (6)

The middle equality is finite telescoping: multiply the geometric sum
by z=(1+z)+1 and cancel adjacent powers in F₂. Equations (4) and (6)
give alpha_H X_H=alpha_Q in every coordinate. Thus both full arrows
(1) hold; no hypothesis on a common raw accepting core is used.

### 4. Every map to this Q must pay the same degree-coordinate support

Let Y be any matrix satisfying (1) for the same H and Q. Iterating its
transition equation and using its final-vector equation yields

    M_H^d beta_H = Y M_Q^d beta_Q = Y e_(q_d)^T,
                                                        0<=d<=n. (7)

Consequently all n+1 degree columns of Y are forced to be precisely
the columns in (5). Extra entries in column a cannot cancel these
separate coordinates. The initial equation in column a also requires
alpha_H Y(:,a)=1, hence at least one nonzero in that column. Construction
(5) attains exactly one. This proves minimality, not merely that one
chosen matrix happens to be dense.

Write r=sum_j r_j 2^j in binary. The same repeated-squaring identity gives

    (1+z)^r = product_(j:r_j=1) (1+z^(2^j)).

The exponents obtained by choosing subsets of these distinct binary powers
are all different. Thus there is no cancellation and this polynomial has
exactly 2^(sum_j r_j) nonzero coefficients. As r ranges from 0 to 2^k-1,
all k-bit choices occur. Summing their weights gives

    sum_(r=0)^(2^k-1) 2^(sum_j r_j) = product_(j=0)^(k-1)(1+2)=3^k.

By (3), the n nonterminal F rows therefore contribute exactly 3^k
nonzero degree entries. The sink contributes one and all other rows
contribute zero. The source column contributes at least one and (5)
attains it. Every valid Y has support at least 3^k+2, as claimed.

### 5. Ledger, threshold and precise stopping scope

The two arrows have total minimum support 2*3^k+4. For every k>=0,
S=10*2^k+20<=30*2^k, so their support/S ratio is at least
(1/15)(3/2)^k. Given any proposed universal C, choose k with
(3/2)^k>15C. The support bound then fails. This is an exact asymptotic
obstruction, not a large finite example substituted for a proof.

Q is the only intermediate; even charging a separate occurrence at each
arrow gives 2g(Q)=6n+12=(3/5)S. The endpoint denominator remains the two
independent products. Dense initial/final vectors for both endpoints and
two occurrences of Q use 2(2(n+4)+2(n+2))=8n+24 field-bit positions.
A sparse map entry additionally needs its row/column indices; a fixed
width encoding uses ceil(log2(n+4))+ceil(log2(n+2))+1 bits per entry,
before framing, including one field bit. No index charge can reduce the
already superlinear number of entries. No wire-byte claim is made.

The construction never requires a cut/path table. It does require the
explicit coefficient entries in (5), and those are charged. Nor is a
dense K_H free: equations (2)–(7) are mathematical finite-operator
reasoning, not a claim that a numerical matrix has been received. One
possible direct checker computes K_H X_H by reverse-topological constant
edge propagation on the n+2 matrix columns, then applies E_(H,x), and
compares all (n+4)(n+2) transition coordinates per arrow. Its scalar
operation count is O(n^2); even the stated comparison scans
2(n+4)(n+2) coordinates across the two arrows. Boundaries and construction
costs are additional. No linear checking-work or live-memory bound is
asserted, and none is needed to conclude the failed support threshold.

This is an allowed counterfamily to the universal bound for the specified
monomial-degree quotient. It includes mixed path degrees at each layer
and F₂ cancellation in the resulting coefficients, and handles G's
coincident roots exactly. A universal positive construction would still
need arbitrary branching, cancellation, no-path operands, disconnected
vertices and arbitrary roots; their omission from a counterfamily cannot
repair this failed universal proposal. Alternative bases can change
support, so (7) is not a lower bound for arbitrary intermediates or chains.
L112's full-cut and L113's raw-contract obstructions remain separate.
Actual operand binding, mixed-letter Dcomm, full receipt/work/live costs,
general certificate availability and unrestricted complexity remain open.

## Mathlib

Full matching coverage for this specific quotient/support obstruction is
**not checked**; no absence claim is made. The external simulation input
and local finite-closure convention are stated precisely in §1. The
polynomial-support calculation and all specialization hypotheses are
proved above; no uninspected library theorem is an assumed dependency.

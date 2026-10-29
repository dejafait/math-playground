# L116 — Preserving all operand-state delay channels forces product size

## Hypotheses

Work over F₂ with finite acyclic occurrence graphs whose edge labels are
singletons 1 or x. Parallel occurrences and parity cancellation are allowed.
Use L110 §4's right closure and §21's independent wrapped product recipe.
Set g(H)=|V(H)|+2|E(H)|, counting each occurrence and its singleton entry.

For r>=1, F_r has vertices f_0,...,f_r, roots f_0,f_r, and two parallel
occurrences f_i->f_(i+1), labelled 1 and x, at each of its r layers. Let
G have n>=1 vertices, c constant and d letter occurrences, and arbitrary
designated roots. The original endpoints are A=Prod(F_r,G) and
B=Prod(G,F_r), with complete disjoint operand copies, fresh source/sink
and three constant connectors each. Do not pad or replace the endpoints.

The **specified batching proposal** keeps a separate input port v_i and
output port u_i for each of the n operand vertices. It replaces the
separate r-layer channels by a possibly shared acyclic graph D, required
to have the complete port-to-port path-polynomial matrix

    P_D(i,j;x) = delta_(i,j) (1+x)^r.                   (1)

There are 2n distinct ports. Within D, the v_i have no incoming edges and
the u_j have no outgoing edges. All other vertices and edges may be shared
arbitrarily. Constant edges, branching, cancellations and extra disconnected
vertices are permitted; paths with different ports must cancel exactly as
required by (1). The internal graph may depend on the whole operand G.
This is a simultaneous delay preserving every operand-state channel, not
merely the single accepting transfer between G's designated roots.

If D is used in an intermediate graph of a scalar simulation chain, its
distinct vertices remain distinct there. Its ports may be identified with
the host's corresponding operand-state ports. Its stipulated transfer is
computed inside D; exterior paths are not part of (1). Any scheme that uses
exterior feedback/cancellation to change the interface, identifies distinct
ports, or only preserves an accepting scalar is outside this proposal.

All candidate arrows retain the usual three right-closed scalar equations
alpha_U X=alpha_V, M_U X=X M_V, beta_U=X beta_V. No separate raw constant
intertwiner is imposed. The conclusion below holds irrespective of what
arrows are later proposed: the required intermediate already has too many
vertices. No existence of the rest of a chain is assumed or asserted.

## Conclusion

Every graph D satisfying (1) has at least n(r+1) vertices, hence at least
n(r-1) nonport vertices. This lower bound is attained in vertex count by
n disjoint copies of F_r. Sharing states, constants or cancelling paths
cannot lower it while preserving the complete port contract (1).

The fixed original endpoint denominator is

    S=g(A)+g(B)=10r+2n+4c+4d+18.                       (2)

On the allowed family r=n=N and G the n-vertex x path, S=16N+14, whereas
one occurrence of the required intermediate has g>=N(N+1). Its ratio to
S is unbounded. Thus no universal C bounds support plus summed intermediate
graph size by C*S for any chain that includes this specified interface.
Charging the intermediate at both incident arrows only increases the cost.

This rejects the proposed all-operand-state delay-sharing mechanism. It
does not reject arbitrary simultaneous batching, boundary-coupled graphs,
different coordinate systems or unrestricted scalar zigzags. It does not
claim that every way of extending L115 must satisfy (1). Even a complete
linear-size unary chain would leave arbitrary F, mixed-letter Dcomm, actual
reception, total checking costs, general availability and P versus NP open.

The result is a REPRODUCTION: a concrete finite-rank specialization testing
a new interface restriction, not a new general realization lower bound or
a certified novelty claim.

## Proof

### 1. Source scope and the precise failed mechanism

The prior EXPLORE assessment is
`drafts/literature/2026-10-26-unary-product-sparse-quotient.md`. Reuse the
scalar simulation convention and soundness from Ésik–Maletti, *Simulation
vs. Equivalence*, [2010 author manuscript, Definition 3.1 and soundness,
p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ is an allowed semiring. That import gives no linear-size certificate;
the present obstruction does not reprove its qualitative existence theorem.
L110 §4 supplies the finite right-closure coefficient formula for each
designated input/output pair, and §21 supplies the fixed endpoint recipe.

L115 motivates this test through its V_v->U_v operand-state interface.
It does not prove that replacing that interface by an r-layer transfer
gives a valid chain: a naive substitution can change the operand's other
letter weights as well. The present proposal explicitly tests whether
sharing an entire identity-channel delay could meet the size requirement,
even if those other equations were repaired. Its answer is negative without
an unproved assertion that the remaining arrows exist.

L112 counts a specified full cut table; here the interior states may be
shared arbitrarily, so counting a literal table is insufficient. L113's
raw-first condition is not used. L114 bounds support in one monomial basis;
here the bound is on state dimension for every realization of (1), with
no coefficient-coordinate requirement on the arrows. Those results are
comparisons, not mathematical premises of this proof.

The calculation below is just an explicit factorization and the elementary
rank bound for a product of finite matrices (equivalently rank-nullity).
No minimal-realization theorem, sparse-minimization claim or unseen source
is imported. Writing out this special finite matrix is necessary to test
the quantitative condition not settled by the assessed sources.

### 2. All coefficients and a forced full-rank finite matrix

Let m be the number of vertices of D. Write C and E for its parity constant
and x adjacency matrices, and put

    K=(I+C)^(-1), M=E K,
    A_0(i,:)=e_(v_i) K, B_0(:,j)=e_(u_j)^T.           (3)

All inverses are finite sums in a topological order. In particular the
formula is valid with constants and cancellation; no dense K is assumed to
have been supplied or stored. For every integer ell>=0, constant-segment
decomposition, including the leading segment, gives

    A_0 M^ell B_0 = [x^ell] P_D(x) = p_ell I_n,        (4)

where p_ell is the coefficient of x^ell in (1+x)^r. The case ell=0 is
A_0 B_0, not an omitted constant term. We need only ell<=2r. We have
p_r=1 and p_ell=0 for ell>r, irrespective of the lower binomial parities.

Form finite matrices R and O by stacking and concatenating respectively:

    R = [ A_0; A_0 M; ...; A_0 M^r ],
    O = [ B_0, M B_0, ..., M^r B_0 ].                 (5)

They have dimensions n(r+1) by m and m by n(r+1). Their product H has
n-by-n block in block row a and block column b equal to

    H_(a,b) = A_0 M^(a+b) B_0 = p_(a+b) I_n,
                         0<=a,b<=r.                  (6)

Reverse the order of H's block columns, writing the new column index j
for old column r-j. The new (a,j) block is p_(r+a-j) I_n. If a>j it is
zero, and if a=j it is I_n. Thus this is block upper triangular with
identity diagonal, so its rank is exactly n(r+1). Column reversal is a
permutation and leaves rank unchanged. Therefore

    n(r+1) = rank(H) = rank(R O) <= m.                (7)

For completeness, the last inequality uses only that the image of the
map R O lies in the image of R, which has dimension at most the m-dimensional
space on which R acts. It imposes no sparsity, noncancellation, path-length
uniqueness or minimality assumption on D.

There are 2n distinct ports, so (7) also gives m-2n>=n(r-1). Conversely,
take n disjoint copies of the r-layer parallel-1/x path, using their ends
as the ports. The diagonal transfer is (1+x)^r and off-diagonal transfers
are zero. This graph has exactly n(r+1) vertices, 2nr edge occurrences
and g=n(5r+1). Thus the vertex lower bound is sharp for the interface;
it is not an artifact of an excessive explicit construction.

The same finite-rank proof would apply to any monic scalar degree-r
polynomial in place of (1+x)^r. In particular the transfer x^r I_n has
the same dimension bound. This observation is not needed for the endpoint
count or the conclusion.

### 3. Exact original sizes and the universal-threshold failure

Each original product has r+1+n+2=r+n+3 vertices and 2r+c+d+3 edges.
Every edge has one label entry. Therefore

    g(A)=g(B)=5r+n+2c+2d+9,

which proves (2). These counts retain every operand occurrence and all
three connectors, before any constant closure. Neither a substituted
operand nor the proposed delay network enlarges the denominator.

Now let G be the n-vertex path with one x edge at each step, rooted at
its first and last vertices. Then c=0 and d=n-1, including n=1 where the
roots coincide and the path is empty. Every vertex lies on the accepting
structural path, so the counterfamily does not arise by adding unused
operand vertices. Take r=n=N>=1. Substituting into (2) gives

    S=16N+14 <= 30N.

Any intermediate containing the proposed D has at least N(N+1) vertices
by (7). Consequently, even charging it just once and charging zero for
all other graphs and scalar maps, the required ratio is at least

    N(N+1)/(16N+14) >= (N+1)/30 -> infinity.           (8)

Given any proposed universal C, choose an integer N>=1 with N>30C.
Then (8) is greater than C. Alternatively the added nonport states alone
have ratio at least (N-1)/30, which is also unbounded. This proves a
necessary count, rather than only failure of a particular chosen map.

The proof does not assume that a complete chain with this interface exists;
it proves that if one exists its intermediate count already fails the
linear target. All scalar-map orientations and supports are therefore
irrelevant to repairing this specific count. Boundary vectors, graph/map
indices, framing and checking work have nonnegative additional costs and
cannot reduce it. No wire-byte or live-memory lower bound for the actual
fixed job is inferred. Matrices (5) are mathematical witnesses for the
dimension argument, not an uncharged certificate-construction algorithm.

### 4. Scope and verification

The algebraic checks are (4) for every coefficient including zero, the
complete block entry formula (6), its block-column reversal, and the exact
occurrence counts in (2) and (8). These are symbolic proofs for all n,r;
no finite numerical experiment, preview or unreceived script substitutes
for them. No mathematical program was needed for this step.

The counterfamily is sufficient to reject a universal bound for the
specified proposal. An unrestricted positive result must still handle
arbitrary roots, no paths, disconnected states, branching and cancellation;
restricting G to a path here does not assert otherwise. In particular the
forced n independent channels are a hypothesis of this mechanism, not a
consequence of FG=GF. A construction preserving only the final scalar,
allowing interactions with the surrounding operand, can evade this proof's
hypotheses and requires its own equations and full ledger. No such
alternative is established here.

## Mathlib

Full matching coverage for this exact port-interface statement and
occurrence-size specialization is **not checked**. No absence claim is
made. Finite matrix rank bounds, triangular invertibility and nilpotent
closure algebra would be supporting facts; they would not themselves
establish a general sparse simulation chain. The imported simulation
convention and local closure input are given precisely in §1.

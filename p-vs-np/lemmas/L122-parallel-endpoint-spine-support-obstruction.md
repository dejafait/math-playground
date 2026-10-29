# L122 — An endpoint-only parallel/spine lift forces superlinear scalar support

## Hypotheses

Work over F₂ with finite acyclic occurrence graphs, singleton labels 1,x,
and all parallel occurrences charged. Use L110 §§4,21's right closure,
independent products and fresh unit source/sink boundaries:

    K_H=(I+C_H)^(-1), alpha_H=e_s K_H,
    M_H=D_H K_H, beta_H=e_t^T, g(H)=|V(H)|+2|E(H)|.       (1)

The inverse is the finite constant closure. An arrow X:U->V has U rows,
V columns and satisfies

    alpha_U X=alpha_V, M_U X=X M_V, X beta_V=beta_U.       (2)

There is no reverse elementary companion, rank, invertibility, functional
row or preservation-of-operand-coordinate requirement on X. Every nonzero
scalar entry is charged separately, regardless of its formula.

Let k>=0, N=2^k. F_N has f_0,...,f_N with parallel 1/x edges at each
layer. G_N is the N-edge x path h_0,...,h_N. The original endpoints are
A=Prod(F_N,G_N), B=Prod(G_N,F_N), including all three constant product
connectors. Thus S=g(A)+g(B)=16N+20. They are not replaced by smaller
equivalent endpoints.

The particular **parallel endpoint/spine lift Q** is this exhaustive
occurrence graph:

* Keep two independent branches, one with all A occurrences and one with
  all B occurrences, identifying just their fresh s and t. Prefix all
  internal vertices by a_ and b_, respectively. Thus exactly two copies
  each of F_N and G_N are retained.
* Add d_0,...,d_(2N-1), the x edges d_j->d_(j+1) for j<2N-1,
  the x edge d_(2N-1)->t, and constants s->d_0 and d_N->t.
* There are no other vertices, occurrences or cross-branch incidences.
  The designated roots remain s,t.

All maps may use arbitrary scalar sums on both copies and the entire
spine, and may annihilate output-dead states when (2) permits it. The
tested common-target chain is A->Q<-B; the reverse arrow Q->A is also
tested to distinguish a restriction of the graph from an orientation
artifact. This is one allowed path fixture, not an assumption that
arbitrary unary operands are paths.

## Conclusion

Q is acyclic, accepts the same polynomial as A,B, and has

    |V(Q)|=6N+6, |E(Q)|=8N+8, 2g(Q)=44N+44<=3S.         (3)

At N=4 the complete matrices in §3 give valid A->Q, B->Q and Q->A
arrows, with supports 59,50,57. The common-target chain has charge
59+50+220=329 against S=84; this finite ratio is not a universal bound.

For every k and every possible scalar map satisfying (2), however,

    support(A->Q) >= 2(3^k-2^k),
    support(Q->A) >= 3^k.                               (4)

For k>=2 either orientation adjacent to A has support/S at least
(3/2)^k/36, which is unbounded. No universal C can bound support plus
twice-counted intermediate size by C*S for this parallel lift, including
an orientation reversal at A. Arbitrary scalar sums and zero rows do not
remove the forced coordinates.

This is a local REPRODUCTION/specialization of scalar simulation identities
and the binomial-coordinate count already used in L118. It gives new
route evidence about this explicit graph, not a new qualitative automata
theorem, a lower bound for arbitrary scalar chains, or certified originality.
It does not stop cross-coupled intermediates, other representations, or
chains inserting a different graph between A and Q. The path obstruction
already stops the full arbitrary-G proposal; no cancellation-fixture or
general-G extension is claimed. P versus NP and actual Dcomm reception
remain unresolved.

## Proof

### 1. Source scope and why this specialization is required

Reuse the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-27-batched-incidence-zigzag.md`.
The scalar convention is Ésik–Maletti, *Simulation vs. Equivalence*,
[2010 author manuscript, Definition 3.1](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ is an allowed semiring and arbitrary finite boundary vectors are
allowed. Its qualitative simulation soundness is imported, not reproved
or used to claim quantitative existence. L110 supplies closure/path
semantics and the full product recipe. L118 §5, equations (12)–(13),
supplies the binomial support identity

    sum_(j=0)^(2^k-1) |supp((1+z)^j)| = 3^k.            (5)

Those inputs do not analyze Q's retained incoming prefixes or permit
choosing an arrow orientation without counting its entries. The distinct
graph and its exact forced coordinates require the present specialization.
No general factorization, minimization or existence theorem is reproved.

L115's single-layer chain and L119–L121's restricted failures motivate
the test but are not mathematical premises. Q retains neither every
placement nor a register for each partial dyadic conversion, and does
not demand elementary companions. No cross-notebook theorem is used.

### 2. Literal graph, all closed rows and the size ledger

Order s first, then a_F,a_G in their path orders, then b_G,b_F in their
path orders, then d_0,...,d_(2N-1),t. Every listed edge points forward.
This proves acyclicity including both full product branches. Paths cannot
switch branches: only s,t are shared, and t has no outgoing edges.

Write z for the length variable and y=1+z. Each endpoint branch accepts
P=z^N y^N. In characteristic two, repeated squaring gives y^N=1+z^N.
The spine has exactly the two accepting paths of lengths N and 2N.
Thus all three branches accept P=z^N+z^(2N), and their sum is P in F₂.
This verifies only the accepted polynomial, not (2).

For subsequent exact checks the ENTIRE endpoint transitions are as follows;
unlisted rows and entries are zero, and row expressions are F₂ sums:

    A: f_i -> sum_(j=i+1)^N f_j + h_0        (0<=i<N);
       h_j -> h_(j+1)                      (0<=j<N-1);
       h_(N-1) -> h_N+t.
       alpha_A=s+sum_(i=0)^N f_i+h_0, beta_A=t.

    B: f_i -> sum_(j=i+1)^N f_j + t          (0<=i<N);
       h_j -> h_(j+1)                      (0<=j<N-1);
       h_(N-1) -> h_N+sum_(i=0)^N f_i+t.
       alpha_B=s+h_0, beta_B=t.                         (6)

Taking constant tails after each letter gives these formulas, including
the connectors and zero rows s,f_N,h_N,t. In Q, every internal a row
is its A row in (6) with internal names prefixed by a_; every internal
b row is its B row with internal names prefixed by b_. The shared t
retains its name. The remaining nonzero rows are

    d_j -> d_(j+1)                     (j<2N-1, j!=N-1);
    d_(N-1) -> d_N+t;
    d_(2N-1) -> t.

    alpha_Q=s+sum_(i=0)^N a_f_i+a_h_0+b_h_0+d_0,
    beta_Q=t.                                          (7)

The two exceptional spine rows are distinct even when N=1. In particular
the constant exit at d_N contributes after the preceding letter, not
as an extra final value at d_N itself. This is right closure, not a raw
constant/letter intertwiner.

Each endpoint has 2N+4 vertices and 3N+3 occurrences. Q's two internal
branches contribute 4N+4 vertices, s,t contribute two, and the spine
contributes 2N. The branches retain 6N+6 occurrences and the spine adds
2N+2. These counts prove (3), with every singleton label entry charged.
No intermediate register or uncharged polynomial edge is present.

### 3. Complete N=4 matrices and every equation

Here is full finite evidence, including valid maps before the asymptotic
test. A and B use the coordinate order

    s,f0,f1,f2,f3,f4,h0,h1,h2,h3,h4,t.

Q uses

    s,a_f0,a_f1,a_f2,a_f3,a_f4,a_h0,a_h1,a_h2,a_h3,a_h4,
    b_f0,b_f1,b_f2,b_f3,b_f4,b_h0,b_h1,b_h2,b_h3,b_h4,
    d0,d1,d2,d3,d4,d5,d6,d7,t.

The integer in each row below has bit j equal to that column's scalar
entry; bit zero is the first listed coordinate. Thus these lists specify
every entry, not samples, hashes or factored matrices. Using (6)–(7),
the maps X:A->Q, Y:B->Q and Z:Q->A are

    X=[0,536807427,357175300,428613640,285753360,0,
       34633824,67129472,134242560,268452352,0,536904704]

    Y=[0,504368096,335549056,402662144,268452352,0,
       2162815,4325524,8651032,17302032,0,536904704]

    Z=[0,3,4,8,16,0,96,128,256,512,0,
       992,640,768,512,0,127,148,280,528,0,
       127,148,280,528,96,128,256,512,3072].              (8)

Direct F₂ row multiplication gives the following COMPLETE transition
products, with equality on both sides in each display:

    M_A X = X M_Q
      =[0,534644860,177477752,320354416,34633824,0,
        67129472,134242560,268452352,536904704,0,0]

    M_B Y = Y M_Q
      =[0,1006696320,671147264,805357056,536904704,0,
        4325524,8651032,17302032,571538528,0,0]

    M_Q Z = Z M_A
      =[0,124,120,112,96,0,128,256,512,3072,0,
        3968,3328,3584,3072,0,148,280,528,3168,0,
        148,280,528,3168,128,256,512,3072,0].             (9)

The initial rows satisfy

    alpha_A X = alpha_B Y = alpha_Q = 2162815,
    alpha_Q Z = alpha_A = 127.                         (10)

In each of X,Y,Z, only the source's final row has a target t entry,
and it has value one. This proves all three final-vector equations,
including every zero row. Equations (9)–(10) and this final-coordinate
check verify all oriented equations. X,Y have zero s,f4,h4 rows; zero
output states really can be removed. No injectivity was assumed.

The row popcounts in (8) sum to 59,50,57. Together with 2g(Q)=220 and
S=84 these give the finite ledger claimed above. The diagnostic generated
expanded rows by exact operations on the saved graph actions; every
entry is present and charged here. Neither a dense coefficient oracle
nor that generation procedure is posited as a linear-cost primitive.
No universal existence claim is inferred from finite samples.

### 4. Every A->Q map has forced incoming-prefix entries

Let L_(H,v)(z)=sum_(ell>=0)(alpha_H M_H^ell)_v z^ell.
All sums are finite. L110's path semantics identifies this with the
full prefix polynomial from s to v, including constant tails.
The complete A prefix list is

    L_(A,s)=1,
    L_(A,f_i)=y^i                         (0<=i<=N),
    L_(A,h_j)=z^j y^N=z^j+z^(N+j)        (0<=j<=N),
    L_(A,t)=P.                                        (11)

For each 0<=j<N, Q's independent branch and spine have

    L_(Q,b_h_j)=L_(Q,d_j)=z^j.                         (12)

No other branch enters these vertices, so identifying s,t has not
altered (12). This is the specific structural restriction being tested.

For ANY X:A->Q satisfying the initial and transition equations,
alpha_A M_A^ell X=alpha_Q M_Q^ell for every ell, by repeated use of
(2). Consequently each target column w satisfies the finite identity

    L_(Q,w)=sum_v X(v,w)L_(A,v).                        (13)

In (11), the only repeated polynomials are the pairs s,f_0;
f_N,h_0; and h_N,t. After combining these pairs, the polynomials are

    1,y,...,y^N, z+z^(N+1),...,z^N+z^(2N).

They have distinct degrees 0,...,2N and are monic, hence are linearly
independent: the largest degree in any nonempty combination survives.
In particular every coordinate f_i for 1<=i<N has a uniquely forced
coefficient in (13), unaffected by arbitrary choices on duplicated
columns. For w=b_h_j or d_j with j<N, expansion of

    z^j=(y+1)^j=sum_(i=0)^j binom(j,i)y^i

therefore gives

    X(f_i,b_h_j)=X(f_i,d_j)=binom(j,i) in F₂,
            1<=i<N, 0<=j<N.                            (14)

High-degree polynomials cannot cancel to change this conclusion: each
has its own highest degree after the duplicate pairs are combined.
Arbitrary entries in all other Q columns do not occur in the selected
column equation at all. This is why extra scalar coordinates in the
parallel lift cannot reduce these required entries.

Each j row of binomial coefficients has support |supp((1+z)^j)|;
omitting i=0 removes exactly one entry. The two target column sets in
(14) are disjoint. Summing and using the imported identity (5) proves
support(X)>=2(3^k-N). Even the final-vector equation was unnecessary.

### 5. Reversing the arrow does not repair this graph

For a state v set R_(H,v)(z)=sum_(ell>=0)(e_v M_H^ell beta_H)z^ell.
This is the right-closed residual, with NO leading constant closure.
The complete nonzero A residuals, obtained from (6), are

    R_(A,f_i)=z^(N+1)y^(N-i-1)             (0<=i<N),
    R_(A,h_j)=z^(N-j)                      (0<=j<N),
    R_(A,t)=1.                                         (15)

The remaining s,f_N,h_N residuals are zero. The polynomials in (15)
are monic with distinct degrees 0,...,2N, so are independent. Within
Q's b branch,

    R_(Q,b_f_i)=z y^(N-i-1)                (0<=i<N).    (16)

Other branches cannot be entered from these rows. The first step of a
nonfinal residual must use a letter; that accounts for the leading z.

For ANY Z:Q->A satisfying transition and final equations, iteration
gives R_(Q,u)=sum_v Z(u,v)R_(A,v). The degree of (16) is at most N,
so independence in (15) forces all high-degree f columns to zero in
these rows and fixes the low-degree h columns as

    Z(b_f_i,h_(N-1-j))=binom(N-i-1,j) in F₂,
                      0<=i,j<N.                       (17)

Zero residual columns may be assigned arbitrary entries; they cannot
cancel any required entry in (17). Summing its row supports and applying
(5) yields support(Z)>=3^k. The initial equation was not needed.

### 6. Threshold, exact replay and limits

For k>=2, 3^k>=2^(k+1), so both bounds in (4) are at least 3^k.
Since S=16*2^k+20<=36*2^k, support/S>=(3/2)^k/36.
This diverges, already before adding any graph or other-map charge.
The linear graph bound (3), the valid N=4 maps and the correct accepted
polynomial therefore do not establish a universal linear chain.

Reproduce the finite diagnostic from the active notebook:

```bash
python3 scripts/batched-incidence/check_endpoint_spine.py --output scripts/batched-incidence/output-539-replay
```

The default original certificate is
`scripts/batched-incidence/output-539/endpoint-spine.json`.
It saves complete occurrences, topological orders, C,D,K,M, boundary
vectors, prefix/residual coefficient lists, full scalar maps and both
sides of every equation at N=1,2,4,8,16. It checks both constant inverse
identities, every forced coordinate in (14),(17), all finite coefficients
and the exact graph ledger. No verification failure occurred. The entire
N=4 Q data, all three matrices/products and the complete forced incoming
rectangle were inspected, not merely their pass flags. The symbolic
proof in §§4–6, not these finite samples, establishes the unbounded ratio.

The step stops this independent parallel-branch graph before arbitrary-G
or cancellation tests. L120's earlier cancellation projections remain
unchanged. Cross-copy transitions could change (12) and (16); no bound
against such a different lift is claimed. Nor does this result impose
restrictions on all possible accepting scalar chains. General F, mixed
letters, actual record-78/events-2642–2643/job-7 binding, later jobs,
Boolean/K/H/nonzero-fJ, full wire/work/live accounting, certificate
availability, L087 W₂ and unrestricted ER/Frege/SAT remain open.

## Mathlib

Full matching coverage for this occurrence-graph construction and its
support bounds: **not checked**. Finite matrix identities and polynomial
arithmetic are supporting mathematics, not a claimed matching formal
theorem. Unknown coverage is not evidence of absence.

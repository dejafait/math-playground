# L123 — A cross-coupled lift has ordinary kernels but still forces binomial support

## Hypotheses

Work over F₂ with finite acyclic occurrence graphs, singleton labels 1,x,
and every occurrence charged, including parallel cancellations. Use L110
§§4,21's right closure and original independent wrapped products:

    K_J=(I+C_J)^(-1), alpha_J=e_s K_J,
    M_J=D_J K_J, beta_J=e_t^T, g(J)=|V(J)|+2|E(J)|.       (1)

An ordinary scalar arrow X:U->V has U rows, V columns and satisfies

    alpha_U X=alpha_V, M_U X=X M_V, X beta_V=beta_U.       (2)

No companion, injectivity, surjectivity, invertibility or functional-row
condition is imposed on these endpoint maps. All nonzero entries count.

Let k>=0, N=2^k. F_N has vertices f_0,...,f_N and parallel 1/x edges at
each layer; G_N is the pure-x path h_0,...,h_N. Keep the full original
endpoints A=Prod(F_N,G_N), B=Prod(G_N,F_N), including their fresh s,t and
three constant connectors. Their combined size is S=16N+20.

Define the construction-only graph Q0 by two independent full endpoint
branches, sharing just s,t, with internal names a_f_i,a_h_j and b_f_i,b_h_j.
Add d_0,...,d_(2N-1), x edges d_j->d_(j+1) for j<2N-1 and
d_(2N-1)->t, and constants s->d_0 and d_N->t. No other Q0 edges occur.
This is exactly L122's graph. Q0 is a recipe, not an additional graph in
the proposed final chain.

The **two-stage cross-coupled lift Q** retains the same vertices. Define
the scalar matrix H by these entire rows, with all others zero:

    a_f_i -> b_f_i, a_h_i -> b_h_i                  (0<=i<=N);
    b_h_j -> d_j, b_f_j -> d_(N+j)                 (0<=j<N).

Put T=I+H and U=I+H+H². For EACH original Q0 edge occurrence u->v,
labelled l, add to Q every occurrence w->z labelled l with U[w,u]=1
and T[v,z]=1. Retain all multiplicities, even duplicate triples. This
is Q's exhaustive incidence recipe, not a polynomial-labelled edge or
an uncharged dense coordinate oracle. The raw designated roots are s,t.
There are two copies of each operand, one 2N-edge spine and no new states.

Test the common-source chain A<-Q->B, with both maps ordinary scalar
arrows (2). The inverse U is internal to this specified construction;
it is not an asserted invertible map between A and B.

## Conclusion

Q is an acyclic singleton graph with the same accepted polynomial as
A,B, namely z^N(1+z)^N. It has

    |V(Q)|=6N+6, |E(Q)|=24N+11,
    2g(Q)=108N+56<=7S.                                  (3)

At N=4 there are the two explicit valid maps in §3 with supports 42 and
52 and the same 21-dimensional invariant zero-final row kernel. Thus the
common-source charge is 42+52+488=582 against S=84. These maps factor
through a quotient onto their 9-dimensional images; neither is asserted
surjective onto the original 12-state endpoint.

The coupling genuinely changes L122's forced functions. For 0<=j<N,
the b_h_j prefixes become z^(N+j), the d_j prefixes vanish, and the
b_h_j residuals vanish. Nevertheless, for EVERY scalar Q->A map (2),

    support(Q->A) >= 3^k-2^k.                            (4)

For k>=2, support/S >= (3/2)^k/72, an unbounded ratio. Consequently
no universal C bounds the tested chain's support plus twice-counted
intermediate size by C*S. Ordinary invariant-kernel projections and
these actual cross-copy incidences do not repair this particular lift.

This is a local REPRODUCTION/specialization of finite similarity algebra,
scalar simulation equations and the previously established binomial count.
It is new route evidence here, not a claimed new general automata theorem
or a lower bound for arbitrary cross-couplings, other arrow orientations,
or arbitrary scalar chains. The path obstruction stops this template
before cancellation-fixture or general-G extensions. L120's valid fixture
projections remain untouched. No actual fourth-comparison receipt,
unrestricted certificate lower bound or P versus NP resolution follows.

## Proof

### 1. Imported inputs and scope of the specialization

Reuse the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-10-27-batched-incidence-zigzag.md`.
The scalar convention and qualitative soundness are imported from
Ésik–Maletti, *Simulation vs. Equivalence*,
[2010 author manuscript, Definition 3.1 and Theorem 4.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
F₂ is an allowed semiring and finite arbitrary boundaries are allowed.
No source theorem is taken to supply these graphs, maps or support bounds.
L110 supplies exact right-closure and product semantics. L122 §§2,4–5
supplies Q0, the endpoint actions, their independent residual basis and
its §1 equation (5), the already established count

    sum_(d=0)^(2^k-1) |supp((1+z)^d)|=3^k.             (5)

L115, L119–L121 and the prior stopped templates are comparisons, not
mathematical premises. Unlike the independent parallel graph, Q changes
its internal functions through literal cross-copy incidences and permits
singular ordinary endpoint maps. The precise changed residuals and
surviving forced entries require this new local calculation; no qualitative
simulation, factorization or minimization result is reproved. No
cross-notebook input is used.

### 2. Literal graph, acyclicity, boundaries and exact occurrence count

Use the topological order

    s; a_f_0,...,a_f_N; a_h_0,...,a_h_N;
    b_h_0,...,b_h_N; b_f_0,...,b_f_N;
    d_0,...,d_(2N-1); t.                               (6)

Every Q0 edge points forward. In the expanded recipe, U[w,u] can only
replace u by itself or a vertex in an earlier operand block; T[v,z]
can only replace v by itself or a vertex in a later block. No within-block
vertex is changed. Hence every expanded occurrence still points strictly
forward in (6). This checks all edges, including source/sink connectors
and the two finite spine exits; parallel cancellations are irrelevant
to acyclicity.

Every H path has at most two edges, so H³=0. In F₂, TU=UT=I. Parity
adjacencies of the literal occurrence recipe are therefore

    C_Q=U C_0 T, D_Q=U D_0 T, K_Q=U K_0 T,
    M_Q=U M_0 T, alpha_Q=alpha_0 T, beta_Q=U beta_0.     (7)

For the closure equation, I+C_Q=U(I+C_0)T, whose inverse is U K_0 T.
The source row e_s is fixed by U,T, and the final column e_t^T is fixed
by both: H has no row from s and no column at t. Thus (7) uses exactly
the original raw unit boundaries, with beta_Q=beta_0, rather than chosen
new accepting vectors. It follows that alpha_Q M_Q^l beta_Q equals
alpha_0 M_0^l beta_0 for every l>=0. L122's Q0 accepts
z^N(1+z)^N: its two endpoint branches cancel, leaving the spine with
lengths N,2N, and (1+z)^N=1+z^N. These are finite identities.

Here is an exact count of expanded edge occurrences. A column of U has
weight 1 on an a vertex, 2 on a b vertex and 3 on a spine vertex. The
source and sink columns have weight 1. A row of T has weight 2 on every
a vertex and every b_f_j,b_h_j with j<N; all other rows have weight 1.
Each Q0 edge contributes the product of its source column weight and
target row weight. Thus:

| Origin in Q0 | Expanded occurrences |
| --- | ---: |
| a branch F edges | 4N |
| a branch G edges | 2N |
| a branch three connectors | 5 |
| b branch F edges | 8N-4 |
| b branch G edges | 4N-2 |
| b branch three connectors | 8 |
| spine's 2N x edges | 6N |
| spine's two constants | 4 |

The total is 24N+11 for every N>=1. There are still 6N+6 vertices,
proving (3); 108N+56<=7(16N+20). Original diagonal-block occurrences
remain present, and every extra or cancelling occurrence is charged.
Q0,T,U are construction data, not implicit free maps in the final chain.
If retained in a transport or implementation, their extra cost must be
charged too; no wire, work or live-memory cap is claimed here.

### 3. Both complete N=4 maps, equations and projected kernels

Use endpoint coordinate order

    s,f0,f1,f2,f3,f4,h0,h1,h2,h3,h4,t

and Q coordinate order

    s,a_f0,a_f1,a_f2,a_f3,a_f4,a_h0,a_h1,a_h2,a_h3,a_h4,
    b_f0,b_f1,b_f2,b_f3,b_f4,b_h0,b_h1,b_h2,b_h3,b_h4,
    d0,d1,d2,d3,d4,d5,d6,d7,t.                         (8)

These are coordinate orders; (6) is the topological order. A row integer
has bit j equal to its entry in column j of (8), starting at bit zero.
The following lists specify ALL rows of X:Q->A and Y:Q->B:

    X=[0,899,516,520,16,0,96,128,256,512,0,
       896,512,512,0,0,0,0,0,0,0,
       127,148,280,528,96,128,256,512,3072]

    Y=[0,2015,660,792,528,0,1054,20,24,16,0,
       28,16,16,0,0,0,0,0,0,0,
       65,128,256,512,1054,20,24,16,2080].              (9)

Applying the full literal graph's closure gives alpha_Q=63615. Exact
F₂ multiplication produces all transition rows, with equality on both
sides in each display:

    M_Q X=X M_A=
      [0,3964,3192,3184,96,0,128,256,512,3072,0,
       3840,3072,3072,0,0,0,0,0,0,0,
       148,280,528,3168,128,256,512,3072,0]

    M_Q Y=Y M_B=
      [0,4010,3366,3630,1054,0,20,24,16,2080,0,
       2088,2080,2080,0,0,0,0,0,0,0,
       128,256,512,3134,20,24,16,2080,0].              (10)

The initial rows are alpha_Q X=127=alpha_A and
alpha_Q Y=65=alpha_B. In each matrix only the Q row t has a target-t
entry, equal to one, proving X beta_A=Y beta_B=beta_Q on every row.
This verifies all three equations (2), not just accepted polynomials.
The popcounts of (9) total 42 and 52.

Both row kernels are the SAME explicit subspace K, spanned by these
21 vectors in the Q order (8):

    [1,32,1024,2944,4608,8704,16384,32768,65536,
     131072,262144,524288,1048576,2098142,4194964,
     8389400,16777744,33554496,67108992,134217984,268435968]. (11)

Each listed row annihilates both X,Y. Its largest set bit is distinct
from those of all other listed rows, proving independence. Both matrices
have rank at least 9: their rows at d0,...,d7,t are independent, since
their endpoint residual polynomials are
z^4+z^8,z^3+z^7,z²+z^6,z+z^5,z^4,z³,z²,z,1, with distinct largest
degrees. Equation (2) makes those precisely the residuals of the mapped
rows. The 21 independent kernel vectors give rank at most 30-21=9,
so (11) spans the whole kernel of each map. In particular no full-rank
or invertible endpoint map is being silently required.

For u in K, (u M_Q)X=u X M_A=0, and
u beta_Q=u X beta_A=0. Thus K is M_Q-invariant and has zero final
functional. The same argument holds with Y. The complete images of
the 21 basis rows under M_Q and their zero products with both endpoint
maps are saved and checked in the finite certificate. The space is not
merely the span of the displayed zero map rows; its mixed vectors matter.
The quotient by K identifies with each map's image. This is the precise
ordinary invariant-kernel projection being tested, without an elementary
reverse companion or a bounded-depth kernel requirement.

### 4. The coupling changes prefixes and residuals

Let L_J(z)=sum_(l>=0) alpha_J M_J^l z^l be the row of all prefix
polynomials, and R_J(z)=sum_(l>=0) M_J^l beta_J z^l the column of
all right-closed residuals. These are finite. There is no leading K in
a state residual. Equation (7) gives

    L_Q=L_0 T, R_Q=U R_0.                             (12)

Put y=1+z. From L122's independent Q0 branches,
L_(0,a_h_j)=z^j y^N, L_(0,b_h_j)=z^j and L_(0,d_j)=z^j.
For j<N, exactly a_h_j feeds column b_h_j of H and exactly b_h_j feeds
column d_j. Hence

    L_(Q,b_h_j)=z^j y^N+z^j=z^(N+j),
    L_(Q,d_j)=z^j+z^j=0.                              (13)

This explicitly removes L122's unchanged low-prefix condition.

For j<N the old b_h_j and d_j residuals both equal
z^(N-j)+z^(2N-j). The b_h_j row of U is e_(b_h_j)+e_(d_j),
so R_(Q,b_h_j)=0. For 0<=i<N the b_f_i row is
e_(b_f_i)+e_(d_(N+i)), and the old residuals are
z y^(N-i-1) and z^(N-i), respectively. Therefore

    R_(Q,b_f_i)=z y^(N-i-1)+z^(N-i).                  (14)

At i=N-1 it too is zero. For the other rows the highest-degree monomial
has cancelled, but the lower coefficients have not all disappeared.
The spine residual at d_N is z^N, despite its raw constant exit to t:
a nonfinal right-closed residual starts with a letter. This accounts
for the potentially delicate boundary case in (14).

### 5. Every map to A still has the forced remaining coefficients

L122 §5 gives the complete nonzero A residuals

    R_(A,f_i)=z^(N+1)y^(N-i-1)       (0<=i<N),
    R_(A,h_j)=z^(N-j)                (0<=j<N),
    R_(A,t)=1.                                         (15)

The s,f_N,h_N residuals are zero. The polynomials in (15) are monic
with distinct degrees 0,...,2N, and hence independent: the largest
degree in any nonempty combination cannot cancel.

For ANY X satisfying the transition and final equations in (2), iteration
gives M_Q^l beta_Q=X M_A^l beta_A for all l, and hence R_Q=X R_A.
Fix i<N and write d=N-i-1. By (14) the b_f_i residual is
z(y^d+z^d), of degree at most N. Thus (15) uniquely forces zero
coefficients on every high-degree f column and on t, and forces

    X(b_f_i,h_(N-1-j))=binom(d,j)+[j=d] in F₂,
                      0<=j<N.                         (16)

Here binom(d,j)=0 for j>d. The entry at j=d is removed; every other
nonzero binomial coefficient remains. Arbitrary scalar entries in the
three zero-residual columns cannot alter these coefficients. Entries in
other Q rows are absent from this row equation, so neither other rows
nor additional maps reduce the charge.

The b_f_i rows and selected h columns are separate coordinates. Their
total forced support is exactly

    sum_(d=0)^(N-1) (|supp(y^d)|-1)=3^k-N,             (17)

using the imported identity (5). This proves (4) without needing even
the initial equation. For k>=2, N<=3^k/2 and S<=36*2^k, so (4)/S
is at least (3/2)^k/72, which diverges. This proves the restricted stop;
no finite-sample extrapolation is used.

### 6. Reproduction, evidence and limits

Run in a fresh output directory, since the script refuses to overwrite
an existing case certificate:

```bash
python3 scripts/batched-incidence/check_cross_coupled.py --ks 2 0 1 3 4 --output scripts/batched-incidence/output-540-replay
```

The preserved receipts are
`scripts/batched-incidence/output-540/cross-coupled-N{1,2,4,8,16}.json`.
Each contains every graph occurrence and topological order, C,D,K,M,
boundaries, expanded scalar maps, both full transition products, all
kernel basis vectors/images and the entire forced rectangle (16).
The complete N=4 graph, maps/equations, kernels and rectangle were read
with the shared JSON inspector's selected `--full` pointers. The script
reconstructs inputs from incidence lists, not stored status flags.

All equations and symbolic finite formulas pass at those five N. The
respective observed total charges are 188,314,582,1166,2478; S is
36,52,84,148,276 and the forced subrectangle has 0,1,5,19,65 entries.
These are implementation checks of the construction, not a proof of
asymptotic sufficiency or of general map existence for arbitrary operands.
The symbolic bound (17) stops the path template, so cancellation and
general-G extensions are not undertaken. Those inputs remain required
for any future positive arbitrary-G construction.

The proof does not bound all possible mixed-orientation chains. It does
not analyze other couplings, a different residual basis or a new graph
inserted next to A. General F, mixed letters, job-7 and later reception,
Boolean/K/H/nonzero-fJ reception, full wire/work/live costs, availability,
L087 W₂ and unrestricted ER/Frege/SAT remain unresolved. No production
cap, format, receiver or historical accounting route changes.

## Mathlib

Full matching coverage of this explicit occurrence lift, its finite maps
or the support obstruction is **not checked**. No absence claim is made.
The imported weighted-automaton convention is cited precisely in §1;
finite F₂ matrix multiplication, nilpotent inversion and polynomial
coefficient identities are supporting mathematics, not a claimed full
Mathlib theorem or a formal verification of this result.

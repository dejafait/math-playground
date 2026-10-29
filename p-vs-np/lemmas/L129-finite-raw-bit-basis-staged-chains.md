# L129 — Complete N=4,8 raw upper-bit staged scalar chains

## Hypotheses

Work over F₂. Take **only N=4 or N=8**, k=log₂ N, and the original
wrapped L122 endpoints A₀=Prod(F_N,G_N), B₀=Prod(G_N,F_N), with every
original singleton 1/x occurrence and all three constant connectors.
Use the common coordinate order

    s,f0,...,fN,h0,...,hN,t.

The topological orders are s,F,G,t for A and s,G,F,t for B. All coordinates,
including fN, hN and the two roots, remain present at every stage. The
L110 §4 right closure and ordinary scalar-arrow convention are

    K=(I+C)^(-1), alpha=e_s K, M=D K, beta=e_t^T;
    X:U->V means alpha_U X=alpha_V, M_U X=X M_V, X beta_V=beta_U.

Set g(H)=|V(H)|+2|E(H)|, counting both labels if they share endpoints,
and S=g(A₀)+g(B₀)=16N+20. No polynomial-edge shorthand is used.

Define E_u, for u=0,...,k-1, by identity on every coordinate, with the
additional entries

    (E_u)_(f_j,f_(j+2^u))=1  whenever 0<=j<N and bit u of j is zero.

Bit zero is least significant. There is no bit reversal. On each side
independently, define successive raw matrices

    C_(u+1)=E_u^(-1) C_u E_u,
    D_(u+1)=E_u^(-1) D_u E_u.                           (1)

The intermediate graph has exactly one literal constant occurrence at
each nonzero C entry and one literal x occurrence at each nonzero D
entry. This rule applies only to intermediate graphs: it does not
replace the original endpoints or their occurrence records.

## Conclusion

Every graph defined above is acyclic with no incoming s or outgoing t.
For both tested N, the arrows H_u->H_(u+1) with map E_u satisfy **all
three** scalar equations. Both terminal orientations A_k->B_k and
B_k->A_k have solutions to their entire initial/transition/final systems.
The concrete maps below are those selected by ascending-column RREF
with all free variables zero, in the saved source-major coordinate order.

Choose A_k->B_k and traverse the B side backwards. The complete chains

    A₀ -> A₁ -> ... -> A_k -> B_k <- ... <- B₁ <- B₀

have the following exact expanded charges:

| N | S | sum nnz(X) | 2 sum over intermediate positions g(H) | total | S(1+k) |
|---|---|---|---|---|---|
| 4 | 84 | 73 | 528 | 601 | 252 |
| 8 | 148 | 173 | 1968 | 2141 | 592 |

Thus the finite ratios to the proposed scale are 601/252 and 2141/592.
No universal C, asymptotic O(S log N) or O(S) bound, minimum-support
claim, unrestricted chain theorem or complete Dcomm receipt is proved.
The graph term dominates these finite ledgers; its uniform growth and a
uniform central construction remain unresolved. The independent dense
receiver below verifies these finite certificates during the same step;
it is not a later independent conceptual review or a P-versus-NP result.

This is a local REPRODUCTION/specialization: the known binary factors
and ordinary scalar equations are applied to an explicit finite recipe.
The finite construction is new notebook evidence, not a claim of a new
general theorem or certified originality beyond the sources checked.

## Proof

### 1. Imported scope and endpoint binding

Reuse the prior EXPLORE assessment
`drafts/literature/2026-10-29-staged-dyadic-bit-basis-test.md`.
Mereb, *Determinants of matrices related to the Pascal triangle*,
[arXiv:2210.12913v1, §2 Remark 2, p.2](https://arxiv.org/pdf/2210.12913v1),
provides the upper binary tensor factors. Arıkan, *Channel Polarization*,
[arXiv:0807.3917v5, §VII-A–C pp.13–14 and Fig.9 p.15](https://arxiv.org/pdf/0807.3917v5),
provides a bit-stage arithmetic circuit, with different kernel/permutation
conventions; no bit reversal or scalar graph assertion is imported from it.
The scalar convention is Ésik–Maletti, *Simulation vs. Equivalence*,
[arXiv:1004.2426v1, Definition 3.1 p.4](https://arxiv.org/pdf/1004.2426v1).
Finite F₂ sums and arbitrary scalar transfer matrices fit that definition.
L110 §4 supplies finite right closure; L122 §2 specifies all original
endpoint rows and connectors. No unrestricted infinite ε-sum is used.

The sources do not supply these literal stages or their expanded costs.
The following finite specialization is needed to check that arithmetic
factors really realize this graph recipe with accepting boundaries.
L117, L119 and L121, and L126–L128, are scope comparisons, not premises.
In particular no elementary companion or shared original-coordinate
relation space is imposed here, and no arbitrary-operand claim is made.

The producer independently compares every endpoint occurrence and every
closed transition and boundary coordinate with the L122 recipe, using
both existing endpoint constructors. The dense receiver reconstructs
the literal product lists again. All unlisted L122 rows, including the
zero rows at s,fN,hN,t, are included. No parity-compressed graph is
substituted for an endpoint.

### 2. Stage graphs and all scalar equations

Write E=I+J for a stage factor. A nonzero J entry goes from a coordinate
whose selected bit is zero to one whose selected bit is one. No row of J
at a target coordinate is nonzero, so J²=0 and E²=I in F₂. Thus (1)
uses the explicitly computed inverse E itself. In the respective original
topological order, E is upper triangular with unit diagonal. C,D are
strictly upper triangular, hence so are ECE and EDE. This checks
simultaneous acyclicity of the union of the two label sets, not just C.
The original s is first and t last; thus they have no incoming/outgoing
occurrences. Each nonzero entry has precisely its specified literal label.
Applying this argument at every stage proves graph validity for each of
the finitely many stages claimed here. The complete raw rows in §5
also give the exhaustive finite occurrence lists by bit decoding.

Use primes for a candidate next graph. Since I+C'=E(I+C)E, finite
inversion gives K'=EKE. Consequently M'=D'K'=EME. E fixes the raw
source row and raw final column, so

    alpha'=e_s E K E=alpha E,       E beta=beta,
    M E=E M'.                                            (2)

Equations (2) prove all three scalar equations for X=E, with their
orientation fixed as previous->next. They do not merely assert raw
constant/letter intertwining. Every closure used for the finite receipts
is recomputed from the saved occurrences, and also compared with the
full finite power sum I+C+...+C^(|V|-1); both inverse products are checked.

### 3. Complete central maps and equation products

An integer row has bit j equal to its column-j entry in the displayed
coordinate order, with bit zero at s. Thus the following lists specify
all entries, including zero rows. Write X for A_k->B_k and Y for B_k->A_k.

At N=4 the terminal transitions and boundary rows are

    M_A=[0,4,8,16,96,0,128,256,512,3072,0,0], alpha_A=99;
    M_B=[0,4,8,16,2080,0,128,256,512,3106,0,0], alpha_B=65.
    X=[1025,66,132,264,528,1024,2,4,8,16,32,2048];
    Y=[33,96,128,256,512,1024,66,132,264,528,0,2048].

Direct row multiplication gives the complete equal products

    M_A X=X M_B=[0,132,264,528,1026,0,4,8,16,2080,0,0];
    M_B Y=Y M_A=[0,128,256,512,3072,0,132,264,528,3168,0,0];
    alpha_A X=65=alpha_B, alpha_B Y=99=alpha_A.          (3)

At N=8 they are

    M_A=[0,4,8,16,32,64,128,256,1536,0,2048,4096,8192,
         16384,32768,65536,131072,786432,0,0], alpha_A=1539;
    M_B=[0,4,8,16,32,64,128,256,524800,0,2048,4096,8192,
         16384,32768,65536,131072,786946,0,0], alpha_B=1025;
    X=[262145,1026,2052,4104,8208,16416,32832,65664,131328,
       262144,2,4,8,16,32,64,128,256,512,524288];
    Y=[513,1536,2048,4096,8192,16384,32768,65536,131072,
       262144,1026,2052,4104,8208,16416,32832,65664,131328,
       0,524288].

The complete equal products are

    M_A X=X M_B=[0,2052,4104,8208,16416,32832,65664,131328,
                 262146,0,4,8,16,32,64,128,256,524800,0,0];
    M_B Y=Y M_A=[0,2048,4096,8192,16384,32768,65536,131072,
                 786432,0,2052,4104,8208,16416,32832,65664,
                 131328,787968,0,0];
    alpha_A X=1025=alpha_B, alpha_B Y=1539=alpha_A.      (4)

For each of these four maps, the t column has value one exactly in
the t row. Since both beta columns are the t indicator, this proves
both final equations at every coordinate. The row popcounts give
support(X)=support(Y)=17 at N=4 and 29 at N=8. Neither minimization
nor a lower bound on any other solution is inferred.

The full systems have one variable x_(i,j) for every ordered coordinate
pair, all initial equations, all |V|² transition equations and all final
equations. They have 144 variables/168 equations or 400 variables/440
equations respectively. The certificate stores their complete coefficient
and augmented rows, pivot columns, all reversible swaps/XOR operations,
and each reduced row as a combination of original equations. The receiver
reconstructs the entire linear operator by evaluating every coordinate
basis matrix; it replays all operations, checks all provenance rows,
checks reduced pivots and zero nonpivot coefficient rows, and verifies
the zero-free-variable solutions and all their original equations.
Thus consistency is fully received in both orientations, not inferred
from a timeout, partial elimination, sampled rows or solver status flag.

### 4. Expanded ledger, reproduction and limitations

All intermediate graph positions are listed here, without replacing
their sum by a maximum. Each row applies separately on A and B.

| N | stage u+1 | vertices per graph | occurrences per graph | g per graph | nnz(E_u) on each side |
|---|---|---|---|---|---|
| 4 | 1 | 12 | 24 | 60 | 14 |
| 4 | 2 | 12 | 30 | 72 | 14 |
| 8 | 1 | 20 | 48 | 116 | 24 |
| 8 | 2 | 20 | 78 | 176 | 24 |
| 8 | 3 | 20 | 90 | 200 | 24 |

The occurrences are exactly nnz(C)+nnz(D) from §5, with both labels
charged. Every vertex remains, including zero/dead vertices and roots.
At N=4 there are four intermediate graph positions: A1,A2,B2,B1.
The map sum is 4*14+17=73; twice the graph sum is
2*(60+72+72+60)=528. At N=8 the six intermediate positions are
A1,A2,A3,B3,B2,B1. Their charge is 2*(116+176+200+200+176+116)=1968,
and the seven maps cost 6*24+29=173. This proves the stated totals.
Both terminal graphs are counted even if their accepted polynomials
agree. A₀,B₀ are the endpoints in S, not omitted intermediate positions.
Choosing the other received central orientation gives the same totals.

Complete certificates and the dense receipt are in
`scripts/batched-incidence/output-559/staged-bit-basis-certificate.json`
and `scripts/batched-incidence/output-559/staged-bit-basis-receipt.json`.
The certificate stores all vertices, occurrences, closures, inverse
matrices, scalar products and central elimination data. Reproduction:

    python3 scripts/batched-incidence/check_staged_bit_basis.py
    python3 scripts/batched-incidence/receive_staged_bit_basis.py

The producer intentionally requires a fresh output directory. For a replay,
pass `--output scripts/batched-incidence/output-559-replay` to the producer
and `--directory scripts/batched-incidence/output-559-replay` to the receiver,
using a new directory name if that one exists. No existing evidence is
overwritten. The receiver alone can be rerun against the retained certificate.

The successful finite tests retain a candidate staging mechanism for
further investigation. They are not extrapolated to arbitrary k; in
particular no uniform estimate for raw occurrence counts or central
maps has been derived. Larger N, the original linear target, general
operands/mixed letters, actual reception, Boolean/K/H/nonzero-fJ, full
work/wire/live bounds, certificate availability, L087 W₂ and unrestricted
ER/Frege/SAT/P versus NP remain unresolved.

### 5. Exhaustive raw stage rows

The row encoding is as in §3. These C,D lists specify every raw occurrence
and every absent entry at each tested stage. They are the actual expanded
matrices, not tensor-factor storage charged as if it were a graph.

N=4, A1:

    C=[6, 28, 24, 48, 32, 64, 0, 0, 0, 0, 2048, 0]
    D=[0, 28, 24, 48, 32, 0, 128, 256, 512, 1024, 0, 0]

N=4, A2:

    C=[30, 60, 56, 48, 32, 64, 0, 0, 0, 0, 2048, 0]
    D=[0, 60, 56, 48, 32, 0, 128, 256, 512, 1024, 0, 0]

N=4, B1:

    C=[64, 28, 24, 48, 32, 2048, 0, 0, 0, 0, 6, 0]
    D=[0, 28, 24, 48, 32, 0, 128, 256, 512, 1024, 0, 0]

N=4, B2:

    C=[64, 60, 56, 48, 32, 2048, 0, 0, 0, 0, 30, 0]
    D=[0, 60, 56, 48, 32, 0, 128, 256, 512, 1024, 0, 0]

N=8, A1:

    C=[6, 28, 24, 112, 96, 448, 384, 768, 512, 1024, 0, 0, 0, 0, 0, 0, 0, 0, 524288, 0]
    D=[0, 28, 24, 112, 96, 448, 384, 768, 512, 0, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 0, 0]

N=8, A2:

    C=[30, 508, 504, 496, 480, 960, 896, 768, 512, 1024, 0, 0, 0, 0, 0, 0, 0, 0, 524288, 0]
    D=[0, 508, 504, 496, 480, 960, 896, 768, 512, 0, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 0, 0]

N=8, A3:

    C=[510, 1020, 1016, 1008, 992, 960, 896, 768, 512, 1024, 0, 0, 0, 0, 0, 0, 0, 0, 524288, 0]
    D=[0, 1020, 1016, 1008, 992, 960, 896, 768, 512, 0, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 0, 0]

N=8, B1:

    C=[1024, 28, 24, 112, 96, 448, 384, 768, 512, 524288, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0]
    D=[0, 28, 24, 112, 96, 448, 384, 768, 512, 0, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 0, 0]

N=8, B2:

    C=[1024, 508, 504, 496, 480, 960, 896, 768, 512, 524288, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0]
    D=[0, 508, 504, 496, 480, 960, 896, 768, 512, 0, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 0, 0]

N=8, B3:

    C=[1024, 1020, 1016, 1008, 992, 960, 896, 768, 512, 524288, 0, 0, 0, 0, 0, 0, 0, 0, 510, 0]
    D=[0, 1020, 1016, 1008, 992, 960, 896, 768, 512, 0, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 0, 0]


## Mathlib

Full matching Mathlib coverage is not checked. Standard finite-field
matrix multiplication and inversion support the algebraic identities;
no exact theorem name or formal verification of these occurrence graphs,
RREF certificates or ledger is claimed. Unknown coverage is not absence.

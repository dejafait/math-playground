# L112 — Full vertex-cut materialization exceeds the Dcomm linear ledger

## Hypotheses

Work over F₂ with finite explicit acyclic original-only operand graphs F,G,
normalized to singleton edges labelled by scalar one or an original letter.
Keep all edge occurrences after within-label normalization. Use the ordered
path semantics and arbitrary designated roots of L035. Let v_F,m_F,v_G,m_G
be their vertex and edge counts. A normalized zero label supplies no edge.

R_axiom and P are the independent endpoint recipes of L110 §3: R retains
four full operand copies for each **non-literal-empty** central list of
L035 (2), followed by the complete ordered dictionary substitution; P has
separate wrapped products FG and GF, attached to fresh common roots.
In particular an empty selected-pair list leaves exactly two isolated R
roots. Define g(H)=vertices+edges+singleton-label entries before constant
closure, and S_comm=g(R_axiom)+g(P). No endpoint padding is permitted.

The question is uniform over this symbolic recipe family, as in the ready
assessment, not over alterations to the fixed job-7 bytes. Its fixed-job
application still requires source record 78, events 2642–2643 and
output-493 jobs[7] to be independently received as specified in L110.
This proof receives none of those bytes, occurrences or equalities.

The tested representation materializes a cut for **every** marked F-edge
e:u→v and G-vertex a, before identifying or canceling cuts. The explicit
four-copy cut graph T and all proposed arrows are defined below. The
stronger, representation-only obstruction also applies to any intermediate
which retains distinct states indexed by all pairs (e,a). It does not
assume that every possible cancellation certificate uses these states.

## Conclusion

The proposed local cancellation stage has valid scalar simulations

    A = P ⊕ T ⊕ T  --X-->  B = P ⊕ T^0  <--Y--  P,       (1)

where T^0 has T's graph and final vector but zero initial vector. Both raw
and finite right-closed equations hold. These arrows only cancel two
already explicit copies of the cut sum; there is **no** supplied arrow or
chain from R_axiom to A, and (1) is not a Dcomm certificate.

This stage cannot satisfy the requested uniform linear ledger. For every
integer N≥1 the allowed unary operands F_N=x^N and G_N=x^(N+1), represented
by their simple directed paths, give

    S_comm = 12N+38,
    q = |E(F_N)×V(G_N)| = N(N+2),
    n_P = 4N+12,                 g(P)=12N+36,
    n_T = 2+2q(2N+3),            g(T)=2+q(12N+20).

The two matrices in (1) have total support 2n_P+2n_T, and the two
intermediates have summed g equal to 2g(P)+3g(T). Each ratio to S_comm is
unbounded. Even a smaller implementation that keeps only one distinct
state per cut (e,a) has g≥q, whose ratio to S_comm is unbounded.

This rejects materializing all marked-edge/vertex cuts before quotienting,
including on a constant-free operand family with no unused operand states.
It does not reject a quotient constructed without that materialization,
other scalar simulations, the commutator identity, or finite feasibility
for the actual job. No resolution of P versus NP follows.

## Proof

### 1. Imports and the proposed cut graph

The prior EXPLORE assessment is
`drafts/literature/2026-10-26-dcomm-cancellation-cut-construction.md`.
Reuse its completed step-524 comparison and the inspected primary source
[Ésik–Maletti, *Simulation vs. Equivalence*, 2010 author manuscript,
Definition 3.1 and soundness, p.2](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf).
For an A-to-B matrix X the convention is eta_A X=eta_B,
E_(A,b)X=X E_(B,b), theta_A=X theta_B. F₂ satisfies the semiring
hypotheses. We check this particular stage's matrices, rather than reprove
soundness or infer their sparsity from qualitative simulation existence.

The product-commutator algebra is already L035 (2),(4)–(7), with its precise
formula-input comparison to [Li–Tzameret–Wang, arXiv:1412.8746v4,
11 September 2015, Lemma 3.7, p.18](https://arxiv.org/pdf/1412.8746v4).
That theorem is not an arbitrary-ABP scalar support bound. No reproof of
the telescoping identity or the formula theorem is needed here.

In the inner G telescoping, the cut indexed by e:u→v and a∈V(G) has the
ordered polynomial

    C_(e,a) = F[s_F,u] G[s_G,a] h_e G[a,t_G] F[v,t_F],    (2)

where h_e is the singleton label of e. The same expression is the cut
between the incoming and outgoing contributions at a. The proposed
materialization retains every such index, even if a central commutator
list was omitted from R. It is not a complete-path or word-history index.
Using (2) only motivates the candidate stage; it does not provide any
missing scalar intertwiner from R to that stage.

Here is the entire graph T. It has two new distinct common roots. For each
of the q=m_F v_G pairs (e:u→v,a), in edge/vertex order, allocate four
fresh disjoint whole-operand copies with designated roots

    (F,s_F,u), (G,s_G,a), (G,a,t_G), (F,v,t_F).

Retain every internal edge in each copy. Add a scalar-one edge from the
common source to the first entry, from the first exit to the second entry,
from the third exit to the fourth entry, and from the fourth exit to the
common sink. Add one h_e edge from the second exit to the third entry.
There are no other edges. The initial/final vectors of T are the units
at its common source/sink. If q=0, T is the two isolated roots.

This specifies every state, label and incidence of the candidate cut graph.
A topological order follows the copy order inside each branch, with the
common source first and sink last. L035's arbitrary-root composition
argument applies: leaving a designated exit internally cannot return to
its connector in a DAG. Thus T represents the sum of (2), with every
ordered factor and occurrence intact. Its exact preclosure counts are

    n_T = 2+2q(v_F+v_G),
    e_T = q(2(m_F+m_G)+5),
    l_T = e_T,
    g(T) = 2+q(2(v_F+v_G)+4(m_F+m_G)+10).               (3)

The five new edges per cut are four connectors and the central h_e edge.
No cut or copied component is charged only once across different branches.

### 2. All proposed arrows, boundaries and closure

For a graph H write its raw representation as (eta_H,E_(H,b),theta_H),
where b ranges separately over scalar one and every original letter;
parallel occurrences contribute their parity to each adjacency entry.
The direct sums in (1) introduce no new graph vertices or edges. They
use the concatenated boundary vectors. They are general representations,
not assertions that B has a unit initial vector or that its T component
has been deleted. P itself keeps its original roots and graph.

Let n=n_P and t=n_T. In the block orders shown in (1), the entire matrices
are

    X : (n+2t) × (n+t)             Y : n × (n+t)

        [ I_n   0 ]                   [ I_n   0 ].
    X = [  0   I_t ]
        [  0   I_t ]

The first arrow is A→B and the second is P→B; neither is reversed.
For every constant/letter b, put D=E_(P,b), E=E_(T,b). Then

    diag(D,E,E) X = X diag(D,E),
    D Y = Y diag(D,E).

These equalities follow by multiplying the displayed blocks and hold for
every entry, including canceled parallel edges and unused letters. For
the initial vectors,

    (eta_P,eta_T,eta_T) X = (eta_P,0) = eta_B,
    eta_P Y = (eta_P,0) = eta_B.

For the final columns,

    X (theta_P,theta_T)^T = (theta_P,theta_T,theta_T)^T,
    Y (theta_P,theta_T)^T = theta_P.

These are all the raw simulation equations. Cancellation uses 1+1=0 in
F₂, while no cut polynomials or paths are compared or declared identical
without the literal copied-graph correspondence.

Use precisely the right closure in L110 §4:
K_H=I+E_(H,0)+...+E_(H,0)^(n_H-1), alpha_H=eta_H K_H,
M_(H,a)=E_(H,a)K_H, beta_H=theta_H. The rectangular finite-closure
argument checked in L111 §§4,7 applies to any matrix satisfying the raw
equations, not only partial permutations. Hence K_A X=X K_B and
K_P Y=Y K_B; the already checked equations give

    alpha_A X=alpha_B,   M_(A,a)X=X M_(B,a), beta_A=X beta_B,
    alpha_P Y=alpha_B,   M_(P,a)Y=Y M_(B,a), beta_P=Y beta_B.

Thus closure, including the empty word, does not repair the forthcoming
size failure. It leaves the prescribed preclosure graph charges intact.
No dense closure tables are stored or assumed sparse.

### 3. An allowed family with a linear endpoint and too many cuts

Let F_N be the simple path 0→1→...→N and G_N the simple path
0→1→...→N+1, every edge labelled by the same original x. Their designated
roots are the path endpoints. They have no constants, parallel edges,
dead vertices or zero labels, and their polynomials are nonzero. One may
retain the job's six-letter alphabet and full dictionary with five letters
unused. Every edge-pair central list is literally empty by L035 (2), since
there are no distinct original-letter indices. Consequently R_axiom has
two vertices and no edges: g(R_axiom)=2.

These operands are also compatible with L036 (5)'s sum-commutator operand
recipe. Take a normalized suffix graph H with two internally disjoint
x-labelled branches from one vertex to a common terminal, of lengths N
and N+1. The two outgoing edges are distinct occurrences. A separate copy
of H with a fresh selected-edge source, followed by its whole-operand
restriction as in L110 §2, retains exactly the chosen branch with its new
source. These are F_N,G_N. No claim concerns their positions in the fixed
job list or reception of a different source proof. This supplies allowed
parameters for the universal symbolic assertion, without modifying any
fixed endpoint, appending padding, or reconstructing one endpoint from
the other.

For clarity, the fixed P recipe has two fresh roots per serial product,
one full F and G copy, and three product connectors. The outer sum adds
two roots and four connectors, preserving both product graphs in full.
Therefore in general

    n_P = 6+2(v_F+v_G),
    e_P = 2(m_F+m_G)+10,   l_P=e_P,
    g(P) = 26+2(v_F+v_G)+4(m_F+m_G).                     (4)

For this family v_F+v_G=2N+3 and m_F+m_G=2N+1, yielding
n_P=4N+12, e_P=4N+12, g(P)=12N+36 and S_comm=12N+38.
The two product paths have the same ordinary word x^(2N+1), so P is
zero over F₂ but structurally nonempty. No acceptance or zero-test result
is inferred from this fact for the actual job.

There are q=N(N+2) marked-edge/vertex cuts. Every one has its designated
F-prefix, G-prefix, G-suffix and F-suffix paths; its contribution is
x^(2N+1). In particular these cuts are not dummy indices for nonexistent
paths. Substitution in (3) gives exactly the counts in the conclusion.

Already any graph with one distinct state per cut has g≥q. For N≥1,

    q/S_comm ≥ N²/(50N) = N/50.

For each proposed constant C>0 choose an integer N>max(1,50C). Then
q>C*S_comm. Thus no uniform linear bound is possible for that injectively
indexed cut-state family, independently of its transitions or any proposed
endpoint maps. This is a lower bound under an explicit representation
condition, not a lower bound on all graphs computing these polynomials.

### 4. Complete ledger for the tested cancellation stage

There are two arrows. Their supports are n+2t and n, respectively, so
the total is 2n+2t. A and B are both intermediate representations; keeping
the independent endpoint P does not make its two copies in them free.
The summed intermediate size is exactly 2g(P)+3g(T). On the unary family,

    total support = 8N+28+4N(N+2)(2N+3),
    summed intermediate g = 24N+78+3N(N+2)(12N+20).       (5)

Since S_comm≤50N, these two ratios to S_comm are at least
(4/25)N² and (18/25)N². Both exceed every fixed C for large N. This
directly fails both requested thresholds, even before any R-to-A arrows
or outer-F cut stage are supplied. Adding those can only increase the
nonnegative aggregate charges. Reusing, streaming or discarding an
intermediate does not erase its charge in the required summed-g measure.

For completeness, across A,B,P the raw boundary vectors have respectively
6,3,2 nonzero entries, for 11 total. Storing two dense boundary vectors per
representation takes 6(n+t) field bits; this bound also permits closed
initial vectors to become dense. With b=ceil(log₂(3(n+t)+1)), all state
indices and dimensions fit in b bits. Sparse matrix entries and the four
dimensions cost at most (2n+2t)(2b+1)+4b bits, before framing. These
smaller items cannot offset (5). Full original names and dictionary costs
are separate, and are not claimed to fit a numerical wire limit.

The graph-only checks can construct/copy the explicit records, verify the
two block maps and compare every copied occurrence, with no word or path
enumeration. Put U=g(P)+g(T). A conservative bound using sequential scans
for each indexed access is O((U+|alphabet|+1)^3 log(U+|alphabet|+2)) bit
work and O((U+|alphabet|+1)log(U+|alphabet|+2)) retained bits. Raw block
equations imply the closed ones as above, so checking them does not need
all entries of K. These are graph-only upper bounds for this failed-size
proposal, not a total interpreter estimate or a fixed-job execution claim.
No mathematical script or finite experiment is used in this proof.

### 5. Boundary cases and precise stopping scope

The two local arrows work unchanged with constant labels, within-label
zero deletion, parallel edges or repeated words, zero-valued but nonempty
graphs, and disconnected components: they compare exact copies and use
parity only in the displayed scalar equations. Unequal path lengths need
no layering assumption. For coincident/nonextremal operand roots the
four-copy construction uses the arbitrary-root argument in §1; its
connectors remain between disjoint copies. If there are no F edges then
q=0, T is the two-root zero graph and the same matrices apply. Literal-empty
central lists are not used to remove T's cuts: that is the defining
materialization choice which the counterfamily disproves quantitatively.

No endpoint correspondence R_axiom↔A is established. Failure is established
by the exact state/record lower bounds, **not** by missing equations.
Only the two arrows that were actually proposed are claimed and checked.
The semantic telescope cannot supply the missing endpoint maps. A refined
approach must avoid the full cut table before allocation, rather than count
only its final quotient after paying for an already materialized table.
The same warning applies to a representation with fewer copied contexts
but still one separate state per (e,a).

An informative negative result is therefore obtained for this mechanism.
It leaves open cut quotients with noninjective indexing, other sparse
chains, strict input/occurrence reception, full work/live/wire accounting,
later jobs, Boolean/K/H/nonzero-fJ reception, general certificate
availability, L087 W₂ and unrestricted ER/Frege/SAT. Attempts 042–046
retain their separate stop evidence. The proof is neither a failure of
L035 nor an impossibility theorem for the fixed Dcomm equality.

## Mathlib

Full matching coverage of this representation-specific obstruction and
its explicit ledger is **not checked**; absence is not asserted. Standard
scalar simulation soundness and formula telescoping are imported from the
precise primary citations in §1. The stage's block equations and record
counts are the necessary specialization checked here. Finite right closure
uses L110 §4 and L111's rectangular argument, whose inspected primary
inputs include [Mohri, IJFCS 13(1), 2002, Definitions 4–5/Theorem 1,
manuscript pp.4–6 and acyclic case pp.10–11](https://cs.nyu.edu/~mohri/pub/ijfcs.pdf).
The local size obstruction was not supplied by the assessed sources;
POTENTIALLY_NEW does not certify originality. No new soundness or
commutator identity is claimed.

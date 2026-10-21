# L086 — Exponential faithful common-order weighted value size on the used expander family

## Hypotheses

Fix an integer Delta>=3 and a real 0<epsilon<1. Supply a finite simple
graph G on n>=2 vertices, of maximum degree at most Delta, satisfying

    |N_G(U) \ U| >= epsilon |U| for every |U|<=n/2.

Use either of L031's unchanged ER proofs (F_(G,sigma),pi_(G,sigma)),
sigma in {0,1}, with T=2+|F|+|pi|. Its positive extension h has value
f_G, the independent-set indicator, on every original assignment.
The actual derived unit is h for sigma=0 and NOT h for sigma=1.

Supply a graph for this unsigned h in L085's value model, in an
arbitrary permutation y_1,...,y_n of the originals. It has levels
1,...,n+1, an initial vertex at level 1, edges from level i to i+1
labelled a+b y_i over F₂, and scalar F₂ values at level n+1. Its value
is the sum of ordered path products times terminal values. Parallel
edges, zero labels, missing paths, unreachable records and cancellation
are allowed. Fidelity means equality with h on **all** Boolean original
assignments, including those falsifying the contradictory original CNF.
There are no repeated variables, higher-degree transitions, implicit
matrices or circuit-valued labels. Initially take the complete layered
convention; skipped constant levels are addressed below.

Let V and E be the total numbers of supplied vertex and edge records
for this root, and B its complete binary encoding length, including
labels, terminals, order, names and root association. Each explicitly
written edge record occupies at least one bit, so B>=E. We do not need
to infer B>=V if isolated state counts are encoded succinctly. An
aggregate E_val for all L085 roots pays for this root as well.

## Conclusion

Put c=epsilon/(16 Delta(Delta+1)). Every such graph has maximum internal
level size, total vertices and literal bit length satisfying

    max_(2<=i<=n) |level i| >= 2^(c n),
    V >= 2^(c n),   E >= 2^(c n),   B >= 2^(c n).          (1)

Thus along any supplied unbounded family with fixed epsilon and Delta,
no polynomial in L031's actual T bounds these faithful value graphs,
in any order. In particular no polynomial E_val in T supplies L085's
value-graph premise universally for the unchanged proofs. For an
encoding allowing skipped constant levels, the uncompleted graph still
has superpolynomial bit length in T, with the explicit bound below.

This is a REPRODUCTION: import the known weighted roABP lower direction
and L030's graph/rank input, and specialize their model, fidelity and
encoding interface. It is no certified new algebraic lower-bound
mechanism. The separate step-335 critical audit below found no
substantive defect in this specialization; this is informal verification.
No general affine-ABP, alternative-data, alternative-proof,
every-certificate, ER or SAT lower bound is asserted.

## Proof

**Known inputs and why specialization is needed.** The prior SPECIALIZE
assessment is `drafts/literature/2026-10-18-expander-weighted-value-obstruction.md`.
L030, Proof equations (1)--(3), already establishes that for every order
the Boolean truth matrix at k=floor(n/2) has

    rank_F₂ M >= 2^(c n).                                   (2)

We use that rank statement, not its deterministic-diagram conclusion.
Its fully induced matching and disjointness rank proofs and citations
remain in L030; they are not rederived here.

For the weighted upper direction on residual dimension, import Neeraj
Kayal, Vineet Nair and Chandan Saha, *Separation between Read-once
Oblivious Algebraic Branching Programs (ROABPs) and Multilinear Depth
Three Circuits*, author-hosted manuscript dated 22 September 2015,
[Definition 6, Lemma 12 and Appendix B](https://www.csa.iisc.ac.in/~chandan/research/multd3_and_ROABP.pdf),
manuscript pp.7,9,21 (PDF pp.8,10,22). Use only its lower-bound direction:
for a scalar polynomial computed by a width-w roABP, the span of
residual polynomials obtained by assigning a prefix in the program's
own order has dimension at most w. Appendix B's lower-direction proof
uses that very prefix and works over any field, including F₂. It needs
neither deterministic paths nor large-field interpolation. This known
theorem is imported, not reproved.

For an independent precise formulation of the receiving model, see
Forbes, Shpilka, Tzameret and Wigderson, *Proof Complexity Lower Bounds
from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021,
[Lemmas 3.6--3.7 and 3.11, printed pp.19--20](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf).
Its matrix-product/coefficient-dimension facts and evaluation-space
inclusion allow arbitrary fields. The equality in Lemma 3.11 needs a
large enough evaluation set; we do not use that equality, the converse
characterization, or its characteristic-restricted functional bounds.
Neither source states this unchanged ER-root/encoding interface, which
is the reason for the following applicability argument.

**Receive the free-algebra graph as a scalar polynomial.** Apply the
abelianization homomorphism to its polynomial and call the result g in
F₂[y_1,...,y_n]. This does not alter any scalar Boolean evaluation:
the homomorphism and evaluation both respect sums, products and scalars.
In particular all-assignment fidelity gives g(p,z)=f_G(p,z). Although
g is multilinear in this model, we need no inference from Boolean
agreement to formal equality of general polynomials.

For each internal level 2<=i<=n, let H_i be the set of distinct heads
of **all** edge occurrences from level i-1. These include unreachable
heads and heads reached only through zero labels. Every path from the
initial vertex has its level-i vertex in H_i. Omitting coordinates
outside H_i in a normalized matrix product consequently omits no such
path: those coordinates have no incoming edge at all. Keep every
original record paid as input. This structural coordinate selection
requires neither reachability computation nor semantic zero testing.
Write h_i=|H_i| and v_i for the original supplied level size. Then
h_i<=v_i and h_i<=E for every internal i.

Let D_1(y_1) be the 1-by-h_2 row whose coordinate at v sums every edge
label from the initial vertex to v. For 1<i<n, let D_i(y_i) have rows
H_i and columns H_(i+1), its (u,v) entry summing all parallel edge labels
u->v. Finally let D_n(y_n) be the h_n-by-1 column whose u coordinate
sums all last-edge labels u->v multiplied by the supplied scalar value
of v. Each entry is affine in the variable of its own level. Scalar
terminal absorption changes no variable layer and preserves scalar-zero
terminals and cancellations. Missing transitions give zero entries.
The scalar path definition gives exactly

    g=D_1(y_1) ... D_n(y_n).

At n=2 these are just the two boundary matrices, with no intermediate
square factor. No accepting path has been unfolded or deleted; input
edges with a source-free tail cannot occur on one and remain paid in B.
All unreachable coordinates in H_i are retained.

Fidelity implies g(0,...,0)=f_G(0,...,0)=1. Hence an initial to
nonzero-terminal path exists and all H_i are nonempty. Put
w=max_(2<=i<=n) h_i>=1. Zero-pad the internal coordinate spaces to w,
obtaining the usual 1-by-w, w-by-w, w-by-1 matrix product of a width-w
roABP. Padded entries are zero; retained entries have exactly the same
affine labels and order. Affine entries are a special case of the cited
source's univariate entries. In particular

    w <= max_(2<=i<=n) v_i <= V,        w <= E <= B.

This is a polynomial normalization in the actual encoding, even if
isolated vertex counts are written in binary. Put M_0=2+T+B. Then
n,E<=M_0 and w<=E. At most O(n(w+1)^2) entries, each with two field
coefficients and an original name of length at most T, suffice. Together
with framing and the retained input, the normalized representation
has O(M_0^4) bits. Entries are obtained by scanning the edge records,
adding parallel labels and scalar-weighting last transitions; binary
endpoint names have length at most B and comparisons take polynomial
bit time. No dense array indexed by absent vertices is needed. There
is no path enumeration, and the original input cost includes every
unused vertex/edge/terminal record. Thus the matrix normalization is
paid and its width is bounded by the original E, without losing an
exponent to normalization.

**Use the evaluation map in the required direction.** At the actual
half-prefix P={y_1,...,y_k}, Q={y_(k+1),...,y_n}, let

    D=span_F₂ {g(p,Y_Q): p in {0,1}^P}

be a vector space of formal scalar polynomials in the suffix variables.
Define the linear map ev from D to F₂^({0,1}^Q) by evaluating at every
Boolean suffix. The vectors ev(g(p,Y_Q)) are exactly the rows of M,
by all-assignment fidelity. Therefore its image is the row space of M,
and the elementary dimension inequality for a linear image gives

    rank_F₂ M = dim ev(D) <= dim D <= w.                   (3)

The last inequality is the imported Kayal--Nair--Saha lower direction
applied to the normalized width-w program and its own prefix. Their
evaluation span over all field assignments contains precisely the
prefix assignments here because the field is F₂. No evaluation-map
injectivity, residual-count bound, converse, large field, positivity
or determinism is assumed. Equations (2)--(3) give w>=2^(c n), and
V>=w and B>=E>=w give (1). Cancellations and arbitrary terminal scalars
were already included in the polynomial and in the cited theorem.

**Both signs and full proof length.** L031 supplies the positive h=f_G
for each sigma. Its negative derived unit when sigma=1 changes only the
literal used in the proof, not the unsigned extension value that L085
requires. Thus (1) applies separately to either unchanged ER proof.
We do not replace h by 1+f_G or restrict to models of F, which has none.

Receive L031's complete literal encoding bound, not a gate count:

    R_*=22m+n+2,   L=ceil(log₂(R_*+2)),
    T <= 128(R_*+n+3)L =: U_G.                              (4)

Since 2m<=Delta n, U_G=O_Delta(n log(n+2)). For each fixed K>0 and
real a>=0, along an unbounded supplied family with fixed graph
parameters, c>0 is fixed and

    2^(c n)/(T+2)^a >= 2^(c n)/(U_G+2)^a -> infinity.

For example the logarithm of the right side is c n minus
O_(Delta,a)(log(n+2)), which tends to infinity. A concrete sufficient
failure test for a proposed bound B<=K(T+2)^a is

    2^(c n) > K(128(R_*+n+3)L+2)^a.                         (5)

Thus every fixed polynomial is excluded, not merely one chosen
exponent. An aggregate collection for L085 must explicitly contain
this root; hence E_val>=B in the complete-level record convention.
The conclusion is conditional on supplied graphs with the fixed
expansion and degree parameters; no uniform expander finder is claimed.

If an allowed presentation omits constant levels, let B_0 be its full
explicit bit length. Subdivide each recorded edge skipping levels by
a private chain, placing its original affine label at its designated
variable level and labels 1 at the omitted levels. A root prefix or
early scalar terminal is similarly completed with unit chains; retain
all original records and terminal values. The model permits this only
when omitted transitions are constant and the prescribed increasing
order is maintained. At most n unit edges per original edge or explicitly
written root/terminal record suffice; isolated state counts need not
be expanded into new edges. Thus the completed **edge count** is at
most C(n+1)(B_0+1), for an absolute record-convention constant C.
Applying the edge-count lower bound in (1) to the completion gives

    B_0 >= 2^(c n)/(C(n+1)) - 1.                            (6)

Its writing cost, including new identifiers and labels, is polynomial
in T+B_0+2. Equation (6) still exceeds every polynomial in actual T
under (4). No sparse-level convention restores polynomial availability.

**Scope and traps.** This stops universal polynomial availability for
L085's precise common-order read-once faithful value model, without
refuting its conditional construction. The order was arbitrary before
using L030, so the obstruction holds for every order. Unreachable
records, scalar-zero endpoints, zero-labelled edges and cancelling
paths were charged, not removed by semantic tests. All-assignment
fidelity, not the contradictory original clauses, links this graph to
the rank input. There is no lower bound here for repeated-variable or
nonoblivious affine ABPs, sums using different orders, nonfaithful L037
data or alternative certificates. L031's same original opposing units
have an immediate refutation and three-node tree certificate. Hence no
optimal-proof, ER, unrestricted circuit or SAT decision conclusion
follows. No finite script or numerical preview is used as proof.

**Separate critical audit, 2026-10-18 (step 335).** The preexisting
EXPLORE assessment is
`drafts/literature/2026-10-18-expander-weighted-value-critical-audit.md`.
This REPRODUCTION audit uses its inspected primary own-prefix proof,
L030's complete rank proof, L031's complete root/encoding argument and
L085's precise receiving model. The conclusion, exponent, formal
argument and direct mathematical inputs are unchanged. The checks
below verify the specialization rather than reprove the imported
weighted lower direction or graph/disjointness theorem.

Every internal vertex on an initial-to-terminal path is the head of
the preceding recorded edge, hence lies in its H_i. Conversely, the
restricted matrices introduce no transition other than a sum of the
original parallel labels, and every summand of the final column uses
the original terminal scalar. Expanding this finite matrix product
therefore gives the original path polynomial after abelianization.
Parallel-edge summation preserves that polynomial, not a list of
individual path occurrences; original occurrences remain paid in B.
A vertex outside H_i cannot be reached from the designated initial
vertex, even if it has outgoing edges. A vertex in H_i is retained
regardless of reachability, zero labels or cancellation. At n=2 the
one internal space H_2 receives both boundary matrices correctly.
The value 1 at the all-zero assignment rules out an empty internal
space and a graph with no accepting path. It does not authorize
deleting paths merely because their polynomials cancel.

An injection from H_i to incoming edge occurrences is obtained by
choosing one occurrence per distinct head. Thus h_i<=E without any
assumption on a succinct count of isolated vertices. The width after
zero-padding is w=max h_i, so both V>=w and B>=E>=w refer to the
original graph. Its dense normalization is only an applicability
device: the lower bound is not divided by its O(M_0^4) writing cost.
There are at most n(w+1)^2 entries, their two coefficients are bits,
and original names, endpoint descriptions and framing have length
O(M_0). This bounds the written matrices by O(M_0^4); retaining the
input adds B. Lists of recorded heads can be indexed and compared
in polynomial bit time without enumerating a succinct isolated-state
range. All supplied labels, terminals, root/order associations and
unused records are already paid in the original B.

Since 1<=floor(n/2)<=n-1, the chosen cut is an internal one, including
at n=2. Boolean suffix evaluation maps the span of residual polynomials
onto exactly the row space of the Boolean cut matrix, yielding
rank M<=dim D. Neither independence of residual evaluations nor an
inverse evaluation map is presumed. The cited primary lower-direction
proof uses the program's own prefix and bounds dim D by its width over
F₂, including cancellations. L030's fully induced matching restriction
and its GF(2) disjointness theorem apply to this same cut in every
permutation. The arbitrary order is fixed before either theorem is
applied; no common favorable order or existential-cut substitution is
made. These observations verify the whole chain
rank M<=dim D<=w<=E<=B with the stated exponential lower input.

For skipped levels, each original edge receives private intermediate
vertices. An accepting path through its replacement chain has no
choice of exit except the original endpoint; contracting chains
recovers exactly the original accepting path. The sole original
affine label stays at its designated variable position, with scalar
ones elsewhere. Prefix and early-terminal unit chains have the same
property and retain the original scalar terminal value, including
zero. Thus the completion preserves the ordered path polynomial,
not just Boolean evaluations. This uses the stipulated omission of
constant transitions only, never a repeated or out-of-order variable.
At most n additional edges are needed per recorded edge or explicit
root/terminal record. Isolated records do not need accepting chains;
their original records remain paid, and an isolated early scalar
terminal can be placed at the final level, retaining its old level
only as input metadata. No accepting path is affected by that move.
The counts of explicit records requiring chains are bounded by a
constant times B_0+1. Consequently E_complete<=C(n+1)(B_0+1), and
applying the complete-level edge bound gives (6). New identifiers
and variable names have polynomial total writing cost. Crucially,
(6) uses the completed edge count, not an unjustified linear bound
on the completed bit length.

L031's positive h remains f_G for both signed-unit proofs; its domain
is every original assignment. Its encoding counts F, headers, defining
slots, signed pivots and all premise references, giving exactly (4).
The degree-sum bound 2m<=Delta*n supplies its fixed-Delta asymptotics.
For fixed a,K,epsilon,Delta, the logarithm of the ratio of (6)'s
leading term to K(T+2)^a is at least c*n-O(log(n+2)), hence tends to
infinity; subtracting 1 cannot change that conclusion. This also
checks the stronger complete-level comparison (5). The conclusion
remains conditional on an unbounded supplied graph family with fixed
parameters; no graph-selection algorithm or new existence theorem
has been supplied. Aggregating the explicit root into all L085 data
cannot decrease its paid cost.

The audit therefore retains Attempt 030's restricted availability
stop with no weakened threshold or new mathematical dependency.
It finds no obstruction to L085's conditional supplier, general
affine ABPs or alternative data/certificates. It supplies no new
bound beyond the existing specialization, no implementation or
formal proof verification, and no SAT decision/separation result.

## Mathlib

Full matching coverage for this weighted-value/ER specialization and
the cited roABP theorem is **not checked**; unknown coverage is not
absence. The supporting linear-image/rank inequality is ordinary
finite-dimensional linear algebra; no particular Mathlib declaration
has been verified here. The complete graph/rank citations stay in
L030, and the precise weighted primary theorem citations are above.

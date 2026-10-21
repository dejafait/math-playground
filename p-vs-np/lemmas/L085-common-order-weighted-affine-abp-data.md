# L085 — Supplied common-order weighted value graphs give local ABP data

## Hypotheses

Work over the free associative algebra over F₂. Use L037's original
width-at-most-three CNF F, valid fresh acyclic signed-AND ER refutation π,
T=2+|F|+|π|, original-variable convention and complete original axiom list
A. There are n≤T distinct originals, in one supplied order y₁,…,yₙ.
Nonextension proof variables absent from F have value zero.

For every unsigned extension, including unused ones, supply an explicit
x-only layered graph with a designated initial vertex at level 1,
vertices at levels 1,…,n+1, and scalar terminal values in F₂. Each edge
at level k goes to level k+1 and has label a+b yₖ, a,b∈F₂. Its polynomial
is the sum of ordered path products times the terminal scalar. Parallel
edges, zero labels, missing paths and cancellations are allowed. The
graphs are finite and explicitly encoded; implicit matrices or
circuit-valued labels are not admitted. Their polynomials are promised
to compute the respective ER extension values on **every** original
Boolean assignment. Original and constant representatives must be their
exact prescribed polynomials; signed roots must be exactly 1+r.

The common order contains each original once; variables unused by a
graph may have constant-labeled levels. Graphs omitting such levels may
first be completed by constant-1 chains, with the cost charged below.
No repeated-variable or higher-degree transition is admitted. For n=0,
the initial vertex is a scalar terminal. Let E_val include all supplied
graphs, labels, original names, order lists and root associations, and
put Q=2+T+E_val. Fidelity is a promise, not a property the constructor
must decide. No bound on E_val in T is assumed for arbitrary ER proofs.

## Conclusion

There is a deterministic polynomial-bit-time construction of all L037
representatives and local relations, retaining each supplied unsigned
polynomial, exact originals/constants, and exact signed complements.
For every actual AND definition with ordered signed operands a,b it
constructs an explicit acyclic affine ABP Hᵢ satisfying formally

    Hᵢ(x,0)=0,                 Hᵢ(x,A)=rᵢ+rₐr_b.             (1)

Only original Boolean and pair-commutator placeholders occur in Hᵢ.
One can take S=O(T+2), d=max(1,n), h=max(1,2n−1). These degree bounds
hold before axiom substitution; in fact they bound the number of
nonconstant factors along accepting paths of the constructed graphs.
Every accepting H path has exactly one placeholder edge.

The complete aggregate independently written data have E_ABP=O(Q¹⁰)
bits, including repeated full dictionaries and source associations.
For a fixed explicit binary encoding one polynomial KQ²⁴ bounds full
output bits, deterministic bit time and all pre-substitution degrees.
The exponent is deliberately conservative. L037 consequently supplies
an original-axiom affine-ABP certificate polynomial in Q.

This is a restricted supplied-data result. The separate 2026-10-18
critical audit below clarifies the scalar-terminal shortcut and finds
no substantive defect in the identities or bounds. The prior EXPLORE
search established no full theorem match, not
certified novelty. Polynomial common-order value graphs for arbitrary
ER proofs, formula-length-only bounds and unrestricted SAT decision or
separation remain unproved. This is not a P-versus-NP candidate.

## Proof

**Sources and the new obligation.** The unchanged prior assessment is
`drafts/literature/2026-10-18-common-order-weighted-value-data.md`.
Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from
Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021,
Propositions 4.5–4.6, pp.30–32](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf),
give commutative weighted-roABP correction. Their factor moves are not
imported in the free algebra. L026 supplies ordered-multilinear
injectivity, but its two-successor recurrence does not cover these
weighted inputs. L029's fixed atomic lists do not supply a decomposition
of arbitrary weighted graphs. The work below is the weighted ordered
recurrence and its complete independent-copy bound.

Use L035's audited commutator graph on x-only suffix inputs. Its source
comparison imports Li–Tzameret–Wang, [arXiv:1412.8746v4, Lemma 3.7,
p.18](https://arxiv.org/pdf/1412.8746v4), on formula inputs and
Raz–Shpilka, [author-hosted manuscript, Lemma 2 Step 1,
p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
for disjoint graph sums/products. Here the latter operation applies to
explicit affine graphs over F₂ with constant connectors and a fixed
number of factors. Its size is charged per occurrence. No formula
unfolding or reproof of a source theorem is required. L071's
post-compilation graph region is a design comparison only: its whole
treewidth theorem is not invoked without its hypothesis. L036 is not
needed separately, since repeated operands are included below; L037
uses its already audited Booleanity component in the later assembly.

**Representatives and signed auxiliary graphs.** All supplied path
words are increasing multilinear in this one order. Attach a fresh sink
with a scalar edge from each terminal to obtain an ordinary affine ABP.
This preserves the supplied polynomial, including cancellation and
zero/constant cases. Keep that graph for an unsigned representative.
Write originals and constants directly and use a disjoint graph sum
for each exact signed expression 1+r. Keep every root association and
every unused definition.

For the local construction use layered auxiliary graphs for the same
polynomials. An original yⱼ is a chain with label yⱼ at level j and
1 elsewhere; constants have unit chains and the appropriate terminal
scalar. For the complement of a layered graph with n≥1, make a fresh
level-1 root, duplicate the original root's outgoing edges, and add a
separate unit chain from that fresh root to a new terminal of value 1.
All original later vertices/edges are retained. The path sum is exactly
r+1. This adds O(n+outdegree(root)+1) records; it does not complement
the weighted terminal values. For n=0 just complement the scalar.
The same prescription covers signed originals/constants. Thus actual
and auxiliary signed roots agree formally, without a sign witness.

After optional completion of skipped levels, all these graphs together
have at most R≤C Q² vertices, edges and label entries, for an absolute
constant C. Indeed completion costs O(n+1) per supplied edge or root
gap, duplicating all signed graphs costs a constant factor, and all
O(T+2) base/sign chains cost O((T+2)(n+1)). Original names and complete
axiom framing will be charged separately, not counted as unit bits.

**One earlier-variable commutator.** Write f_u for a suffix polynomial
starting at level k+1. Let K(u,k) be the L035 witness for the ordered
pair f_u,yₖ. It satisfies K(0)=0 and

    K(u,k)(A)=f_u yₖ+yₖ f_u.                                (2)

The second operand is a single yₖ edge. L035's marked-edge formula
therefore specializes to a sum, over each suffix edge e at level j>k
with label a_e+b_e yⱼ, of

    (suffix prefix ending at tail(e)) · b_e c(k,j)
                           · (suffix after head(e)).        (3)

Here c(k,j) is the original pair-once placeholder for the two distinct
original names, regardless of their numeric identifier order. Scalar
terminal edges contribute zero. Equation (3) is exactly L035's
four-copy expression with the two scalar subpaths of its one-edge
second operand; it uses no additional commutator theorem. Its original
unpruned graph construction is allowed. There are O(R) marked choices,
each using O(R) graph records, so each complete K copy costs O(R²).
Every accepting path uses one placeholder and at most one original
factor at each other remaining level. If s−1 levels remain in f_u,
its pre-substitution path degree is at most s−1. For a scalar terminal
use the zero K graph with distinct endpoints and no accepting path.
For every other suffix retain the marked-edge construction, even if
its polynomial happens to be constant by cancellation. No semantic
constant test or deletion of cancelling paths is required. Marked
edges with b_e=0 contribute no central placeholder edge, as in L035.

**Weighted paired recurrence.** Fix the auxiliary graphs U,V for the
actual ordered signed operands of one definition. At a same-level
state pair (u,v) at level k≤n, consider every ordered pair of outgoing
edge occurrences e:u→u′ and t:v→v′. Write

    l=a+b yₖ,  m=c+d yₖ,  q=ac+(ad+bc+bd)yₖ,
    f=f_(u′),  g=f_(v′).

All four coefficients are field scalars, not new variables or
placeholders. Define P,W backwards, with terminal values
P_(u,v)=s_u s_v and W_(u,v)=0. At nonterminal pairs put

    P_(u,v)=Σ_(e,t) q P_(u′,v′),
    W_(u,v)=Σ_(e,t) [q W_(u′,v′)
                       +d l K(u′,k) g +bd σₖ f g].         (4)

The Boolean placeholder σₖ substitutes to β=yₖ²+yₖ. All product orders
in (4) are fixed as written. No coefficient or placeholder is moved
past a suffix. Zero coefficients may be omitted or retained on zero
edges, and parallel occurrences remain distinct.

We claim W(0)=0 and W(A)=f_u f_v+P_(u,v). For each edge pair,
literal multiplication of affine labels gives lm=q+bd β. From (2),
f m=m f+d K(u′,k)(A). Therefore

    l f m g=q f g+bd β f g+d l K(u′,k)(A) g.              (5)

This verifies all factor movements: only f across m is corrected,
and β remains before f g. Substitute the child induction
W_(u′,v′)(A)=fg+P_(u′,v′) in (4), use (5), and sum over every
outgoing edge pair. The result is
Σ l f m g+Σ q P_(u′,v′)=f_u f_v+P_(u,v).
The terminal equality holds because its two scalar products cancel.
At zero placeholders every local summand has K or σₖ, and terminal
W is zero, so induction separately gives W(0)=0. This argument keeps
all cancelling path multiplicities and does not assume nonzero values.

P has increasing multilinear words. At Boolean yₖ, q(yₖ)=l(yₖ)m(yₖ),
so backwards induction proves that P evaluates to the pointwise
product of the two suffix functions. In particular at the roots it
agrees with rᵢ by the supplied all-assignment fidelity of the actual
definition. Both P and the **unchanged** unsigned rᵢ are increasing
multilinear in one common order. L026's injectivity on that subspace
therefore gives P=rᵢ formally. Its hypotheses hold even if coefficients
have cancelled; no assertion about arbitrary Boolean-equivalent free
polynomials is used. Taking Hᵢ=W at the operand roots proves (1).

**Acyclic realization without copying recursive W.** Introduce one
vertex for every same-level pair, a fresh output Ω, and edges labeled
q from (u,v) to (u′,v′) for every edge pair in (4). Terminal pair
vertices have no route to Ω. At each edge pair attach two completely
disjoint local serial blocks, for d l K(u′,k)g and bd σₖfg. Each block
is entered from (u,v), exits only to Ω and has independently copied
complete K, f, g factors and unit connectors. Coefficient zero blocks
can simply be omitted. All labels are affine in originals/placeholders;
K is an explicit graph, never an edge label.

Pair edges strictly advance a level. A path leaving the pair region
cannot return, enter another local block, or leave Ω. Each local block
is acyclic by its disjoint forward composition. Consequently the whole
graph is acyclic, and partitioning accepting paths by their first exit
from the pair region proves exactly (4). There is no empty accepting
path and no acceptance through terminal W states. Each accepted path
has one placeholder, supplied either by K or by σₖ. Zero-polynomial
blocks may still have paths that cancel; none are deleted on semantic
grounds. The auxiliary P graph uses the pair edges and terminal scalar
product edges to its own fresh sink, hence is explicit as well.

For s remaining levels, the two local blocks have path degree at most
1+(s−1)+(s−1)=2s−1. A recursive edge has degree at most one.
At s=1 child W is zero; for s≥2 its bound is 1+2(s−1)−1=2s−2.
Thus every accepting W path has degree ≤2s−1. This proves the stated
d,h, including before substitution and without semantic cancellation.
Repeated, equal, complementary or constant operands change no step.
An absent outgoing edge set gives an empty sum and is also covered.
For n=0, fidelity gives the scalar equality for each definition directly;
use zero H graphs and retain the scalar representatives and signs.

**Aggregate full encoding and time.** For each definition, the total
number of same-level state pairs is at most R². The number of ordered
outgoing edge pairs, summed over those states, is at most R²: each
occurrence is a pair of edges in the two operand graphs, filtered by
level. This counts parallel edges rather than Boolean transitions.
Each local K costs O(R²); the other copied factors cost O(R), with
constant extra connectors per block. Hence one whole H has O(R⁴)
records. This is a bound for an actual graph with shared recursive
pair states, not an unfolded recurrence. One P graph costs O(R²).
There are O(T+2) definitions and value/sign outputs. Independent
copies for every H, every local block, all representatives and even
retaining all auxiliary P graphs cost

    O((T+2)(R+1)⁴)=O(Q⁹) records.                         (6)

K instances are constructed from supplied x-only suffixes of at most
R records; no previously built H or product P becomes a K input.
No product-state space propagates between definitions. Entire suffix
copies, unused vertices, scalar terminal edges and graph endpoints
are included in R and (6). Exact signed output sums add only O(R+T)
records. The abstract value DAG has O(T+2) entries in source order,
including all bases, signs and unused definitions; arithmetic vertices
inside graphs are not additional abstract definitions.

Every name in the original source/order has at most Q bits. Dense
vertex and symbol references require O(log(Q+2)) bits since all counts
above are fixed powers of Q. Charging O(Q) bits per record therefore
covers labels, restored names, indices, coefficient bits, endpoints and
length framing conservatively. The original axiom list has O(T²)
constant-width entries and O(T³) bits as in L037's receiving convention.
Write it and the original/placeholder dictionary again with each of
the O(T+2) exported roots; their O(Q⁴) total is below O(Q¹⁰).
Even charging such a full dictionary to each local block gives
O((T+2)R² Q³)=O(Q⁸). Together these prove E_ABP=O(Q¹⁰).

A deterministic constructor scans the source, completes levels,
creates base/sign graphs, loops over definitions, state pairs and
edge pairs, and copies L035's explicit marked-edge blocks with dense
renumbering. Each iteration writes the charged records or performs a
bounded number of comparisons/counter operations on strings of
polynomial length; no path, monomial or assignment enumeration is
used. Even naive sequential dictionary scans, input scans per copy and
quadratic string handling in the O(Q¹⁰)-bit generated material fit
KQ²⁴ bit operations after enlarging a fixed constant K. This one
polynomial also covers output bits and the much smaller degrees.
The constructor does not need to test fidelity or P=rᵢ; these are
proved using the hypothesis. All L037 data promises now hold, so its
conditional assembly applies in a polynomial in Q.

**Limitations and checks.** Attempts 019/020/029 retain their recorded
stops: no small deterministic diagrams, general degree-only circuit
conversion or universal unsimplified structural promise is inferred.
Weighted graph availability remains a separate problem. The exact
order and read-once affine-level assumptions are essential to the
multilinear bridge. The proof includes the four scalar coefficient
choices on each affine edge through identity (5); scalar terminals,
zero paths and cancellation have separate reception arguments above.
This establishes an all-size informal construction; it supplies no
implementation or finite graph verification. The following independent
audit checks signed preparation, the ordered identities and the ledger.

**Separate critical audit, 2026-10-18 (step 331).** This audit uses the
unchanged EXPLORE coverage in
`drafts/literature/2026-10-18-weighted-value-data-critical-audit.md`.
It checks the full L035 marked-edge proof and the precise L026/L037
interfaces, rather than importing the commutative FSTW theorem as a
free-ring identity. It establishes no broader graph-availability claim.

First, the earlier-variable specialization has the correct order.
For each marked suffix edge, L035's four factors are the suffix prefix,
the empty prefix of the single y_k edge, its empty suffix, and the
suffix after the marked edge. The middle commutator label is precisely
b_e c(k,j); constants contribute nothing and j>k excludes a diagonal
pair. Terminal scalar edges are unmarked but remain in the final
suffix factor. For a fixed marked edge, a prefix and suffix cannot
overlap across that edge without a directed cycle. Thus their independent
copies enumerate each marked accepting path exactly once, including
parallel occurrences. Incoming edges at a designated entry and outgoing
edges at its exit add no accepting subpaths: returning to the exit
would create a cycle. This also checks L035's unpruned-copy convention.

The original phrase “a constant suffix has the zero K graph” was
ambiguous for semantic constants. For example, two parallel y_j edges
to a scalar-one terminal have zero suffix polynomial but produce two
cancelling c(k,j) paths in the marked-edge construction. Zero polynomial
does not mean no accepting paths. The specification above now invokes
the path-free shortcut only at scalar terminals; all other suffixes
use the explicit marked-edge graph. This repairs the construction's
description without adding a polynomial identity test, changing any
output identity or increasing the existing worst-case allowance.

For the edge-pair identity, expand without commuting any suffix:
fm=c f+d f y_k and mf=c f+d y_k f, so
fm+mf=d(fy_k+y_kf). Also
lm=ac+(ad+bc)y_k+bd y_k²=q+bd(y_k²+y_k).
Multiplying these equalities on the indicated left/right sides proves
(5) in the free algebra for all sixteen pairs of affine labels.
In (4), after substitution, the summand is
qfg+qP_child+d l K(A)g+bd beta fg, exactly
l f m g+qP_child by (5). Summing over edge occurrences gives the
parent identity by distributivity. This keeps multiplicities until
F₂ addition; it uses neither a bijection of distinct monomials nor
nonzero suffixes. At terminals W=0 and P=s_u s_v, so the two scalar
terms cancel. At zero placeholders every complete accepting path
contains one central placeholder edge; terminal pair states cannot
accept. These arguments independently prove both required identities.

The auxiliary sign graph has exactly two kinds of initial choices:
one duplicated outgoing edge of the old root, or the new unit chain.
Their sums are r and 1. Retained old level-1 vertices cannot be reached
from this new root, and levels prevent returns. Thus the value is
formally 1+r even when r has cancelling paths or no path. For n=0
the scalar complement is exact. Direct original/constant roots and
these signed graphs agree with the written representative outputs,
not merely on Boolean assignments. P and the supplied unsigned root
are both increasing multilinear; the inspected L026 injection therefore
applies after fidelity identifies their Boolean functions. This is the
only Boolean-to-formal step. In particular it is not applied to W,
arbitrary products, or Boolean-equivalent unrestricted free polynomials.

For path degree, a marked K path replaces one of at most s−1 suffix
levels by a placeholder and has at most s−2 other variable-bearing
levels. Hence its bound is s−1, including zero-labelled or cancelling
paths. The two local blocks have bounds 1+(s−1)+(s−1)=2s−1.
An accepting path exits the pair region at one level, enters only one
disjoint local block and then reaches the fresh sink. The recursive
prefix contributes at most one per earlier level, as in the induction
above; it cannot multiply two recursively built W graphs. At s=1
the K block is absent, and the Boolean block has degree at most one.
At n=0 all H graphs have distinct endpoints and no accepting path.
These checks give d=max(1,n), h=max(1,2n−1) with no semantic degree
cancellation assumption. Zero coefficients can be omitted in attaching
blocks; zero-labelled source edges inside retained copies cause no
exception to the upper bounds.

Finally, count records before multiplying by name lengths. Explicit
level completion costs at most O(n+1) records per source edge/root gap;
all base chains cost O(T(n+1)), and signs add a constant factor plus
their unit chains. Thus the aggregate normalized value graphs have
R≤C Q² records including fresh scalar exits. A suffix copy has O(R)
records. The single-variable L035 input yields O(R) marked choices,
each with a fixed number of O(R)-record copies, hence O(R²) for K;
the general two-large-input O(R³) estimate is not needed here.
For each definition, sum the products of outgoing degrees over
same-level state pairs. Each term counts an ordered pair of input edge
occurrences once, so this sum is at most m_U m_V≤R². There are at
most R² pair states. Each of these edge-pair occurrences receives its
own O(R²)-record K block and O(R)-record other factors. No cross-block
sharing is assumed. Thus O(R⁴) per H, and O(T R⁴)=O(Q⁹) for the
complete independent family, cover connectors, unused vertices, all
value/sign outputs and even the unneeded P graphs.

Dense references cost O(log(Q+2)) bits and any restored source name
costs at most Q bits. Charging O(Q) per record gives O(Q¹⁰). The
complete original axiom/dictionary payload is O(T³); O(T) exported
copies cost O(Q⁴), or O(T R²) local-block copies cost O(Q⁸). Internal
graph copies use the enclosing dictionary's dense symbols; if retained
as separate intermediate files, their framing need not be exported.
All final root associations and the O(T) abstract DAG records are
included. A constructor can precompute this dictionary, enumerate the
stated record/edge lists and append records with dense renumbering.
Even whole-output sequential reference scans or quadratic copying on
O(Q¹⁰) written bits cost O(Q²⁰); a further O(Q³) dictionary-scan
allowance per such operation still fits the stated KQ²⁴ bound. Parsing
the input and scalar arithmetic cost less. Neither path enumeration
nor semantic testing is part of this constructor.

Consequently L037 receives exactly its original/constant/sign roots,
ordered AND relations, independent original placeholders, complete
framing, positive d,h and acyclic source associations. Unused definitions
remain included. No new mathematical input or DAG edge is needed.
The audit finds no further defect in this informal conditional argument
after the stated construction clarification. It verifies no implementation
and establishes no novelty, arbitrary ER value-graph availability,
formula-length-only bound or SAT result.

## Mathlib

Matching coverage of this full weighted supplier and its encoding
bound is **not checked**, not asserted absent. L026's injectivity,
L035's audited marked-edge construction and L037's conditional receiver
are the local mathematical inputs. The primary supporting citations
and their narrower scopes are given above. No general weighted-to-
deterministic-diagram conversion or commutative-to-free-ring theorem
is imported.

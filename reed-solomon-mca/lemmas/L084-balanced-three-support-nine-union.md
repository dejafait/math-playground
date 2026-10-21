# L084 — Balanced sixteen-support families contain a nine-vertex triple

## Hypotheses

Let V be a set of sixteen vertices and let E be a family of sixteen
**distinct** four-element subsets of V. Every vertex of V belongs to
exactly four members of E. No field labeling, moment compatibility,
matching-number hypothesis or prescribed triangle is assumed.

## Conclusion

There are three distinct members A,B,C of E such that
\[
 |A\cup B\cup C|\le9.
\]
This is an abstract incidence statement. It neither constructs an MCA
pencil nor excludes sixteen-count equality. In a prospective application,
L010 supplies precisely these incidence hypotheses at equality, but
L010 is not an input to this abstract proof. Completion of the extracted
local configurations and challenge-definition qualifications remain open.

## Proof

We specialize the standard Berge-girth Moore bound, rather than reprove
it. The controlling source is David Ellis and Nathan Linial, *On regular
hypergraphs of high girth*, [arXiv:1302.5090v5](https://arxiv.org/pdf/1302.5090v5),
12 July 2017, Section 1, printed pp. 3–4 (Berge-cycle definition), and
Section 2, Lemma 1, equations (5)–(6), printed pp. 5–6. The published
version is *Electronic Journal of Combinatorics* 21(1) (2014), P1.54,
[DOI 10.37236/3851](https://doi.org/10.37236/3851), Section 2, Lemma 1,
printed p. 4. The versioned arXiv text was the inspected source.

A Berge cycle of length g has distinct edges E_1,...,E_g and distinct
vertices x_1,...,x_g, with x_i in E_i intersect E_{i+1}, cyclically.
Length two is allowed: two edges sharing two vertices give such a cycle.
For an r-uniform d-regular hypergraph on n vertices of finite Berge girth
g, with d>=2 and r,g>=3, the cited bound is
\[
\begin{aligned}
n&\ge 1+d(r-1)\sum_{i=0}^{k-1}((d-1)(r-1))^i
 &&\text{if }g=2k+1,\\
n&\ge r\sum_{i=0}^{k-1}((d-1)(r-1))^i
 &&\text{if }g=2k.
\end{aligned}
\]
We verify its applicability by contradiction. Suppose every three
distinct members of E have union size at least ten.

First, E is linear. Otherwise choose A,B with |A intersect B|>=2
and choose x in their intersection. Four edges contain x, so there
exists C distinct from A and B containing x. Since |A union B|<=6
and C adds at most three vertices,
\[
 |A\cup B\cup C|\le6+3=9,
\]
contrary to the supposition. Thus two-edge Berge cycles are excluded.
This argument also covers intersections of size three; distinctness
excludes equal four-element edges.

Second, there is no Berge cycle of length three. If A,B,C form one,
its three distinct successive intersection vertices each have
multiplicity at least two among the twelve vertex-edge incidences.
For any three edges, their union size is twelve minus the sum over
union vertices of (multiplicity minus one). These three vertices alone
contribute at least three to that sum, so the union size is at most nine.
Any further intersections only decrease it. This again contradicts the
supposition. No assertion that a two-edge cycle by itself is already
three edges is used.

Third, finite girth is available without a connectivity assumption.
Consider any connected component of the incidence graph, whose nodes
are hypergraph vertices and edges and whose adjacency means membership.
Every node has degree four: all four incidences of any node remain in
its component. This finite simple graph contains a cycle. Indeed, in a
longest simple path every neighbor of its last node belongs to the path;
its degree four gives a neighbor other than its predecessor, and the
path segment back to that neighbor closes a simple cycle. An incidence
graph cycle alternates distinct hypergraph vertices and distinct edge
nodes, hence gives a Berge cycle of half its length. Conversely every
Berge cycle gives such an incidence cycle. Therefore this component has
finite Berge girth g. The previous two arguments give g>=4.

The induced hypergraph component is still four-uniform and degree four,
with n'<=16 vertices. Apply the cited lemma to that component with
r=d=4. If g=2k is even, k>=2 and
\[
 n'\ge4\sum_{i=0}^{k-1}9^i\ge4(1+9)=40.
\]
If g=2k+1 is odd, g>=5, k>=2 and
\[
 n'\ge1+12\sum_{i=0}^{k-1}9^i\ge1+12(1+9)=121.
\]
Both contradict n'<=16. Thus the supposition was false, proving the
conclusion. The actual bound required for contradiction is forty,
whereas at most sixteen vertices are available. No enumeration or
asymptotic sparse-hypergraph result is used.

The source supplies the general Moore bound. The argument above is only
its necessary specialization and the nonlinear/short-cycle bridge for
this exact target, classified as REPRODUCTION under the prior SPECIALIZE
assessment. No originality or result beyond the checked sources is claimed.
The previous stopped disjoint-triple, six-edge/eight-vertex and
additional-pair extractions have different conclusions and remain stopped.

### Separate critical audit — 2026-10-14

The separately approved audit found no defect in this scoped theorem.
It used the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-14-balanced-three-support-critical-audit.md`.
This verifies an existing reproduction; it supplies no new count bound
or claim beyond the checked sources.

**Short-cycle bridges.** For a nonlinear pair, simplicity gives distinct
A and B, their union has at most six elements, and degree four at any
shared vertex supplies two other incident edges from which to choose C.
That C is distinct and adds at most three vertices is sufficient; no
assumption on its other intersections is needed. For the triangle case,
the source's three intersection vertices are distinct. Each contributes
at least one to the incidence excess in the displayed union identity.
A triple intersection or additional pair intersections cannot invalidate
this upper bound. Thus the contradiction hypothesis really excludes both
length-two and length-three Berge cycles, without confusing a two-edge
cycle with the three edges requested in the conclusion.

**Components and finite girth.** The incidence graph has two disjoint
types of nodes; a vertex and an edge are different nodes even if their
set-theoretic descriptions happen to coincide. It is a finite simple
bipartite graph. Every incidence neighbor of a node belongs to its
connected component, so all node degrees remain four there. In the
longest-path argument a neighbor other than the predecessor is an earlier
path vertex, and the resulting cycle is simple. Bipartiteness makes its
length even, at least four. Alternation gives distinct edge nodes and
distinct vertex nodes, exactly a Berge cycle; the converse has the same
distinctness. Choosing a shortest such cycle yields a finite integer
girth. No acyclic or isolated component is overlooked. A component's
hyperedges retain all four endpoints and each vertex retains all four
incident edges, so its hypergraph is four-uniform and four-regular with
at most sixteen vertices. Its number of edges need not be sixteen for
the imported lemma to apply.

**External input and specialization.** Rechecked the versioned primary
source above, the cycle definition on printed p. 4 and the entire Lemma 1
statement and short two-case proof on printed pp. 5–6. Its integer,
uniformity, regularity and finite-girth hypotheses match the component;
there is no asymptotic size hypothesis. The source counts a ball centered
at a vertex in the odd case and a neighborhood of an edge in the even
case. The two sums transcribed above match its equations (5) and (6).
Substitution gives branching factor nine. From g>=4, even parity gives
k>=2 and the lower bound 40; odd parity gives g>=5, k>=2 and the lower
bound 121. All omitted summands are nonnegative. Each contradicts the
actual upper bound sixteen. This checks the citation's application,
without reproving the general Moore bound.

**Scope and dependency check.** No RS claim, L010 conclusion, local
classification, field labeling or finite computation is used in this
abstract proof. Accordingly the empty L084 input row in DAG.md is correct.
L010, L032 and L041 remain prospective applications only. The stopped
conclusions in ATTEMPTS/016,017,027 ask for different configurations and
are not reopened. No counterexample or repair arose in this audit.
Moment-compatible completion, the uniform triangle bound and the
challenge qualifications remain unresolved. The canonical audit here
supersedes the overview's pending-audit wording; the overview argument
has not changed.

## Mathlib

Full matching coverage of this extraction or the cited hypergraph
Moore bound: not checked. Supporting incidence-graph/cycle coverage:
not checked. Unknown coverage is not evidence of absence, and the
proof uses the precise external theorem above rather than a library claim.

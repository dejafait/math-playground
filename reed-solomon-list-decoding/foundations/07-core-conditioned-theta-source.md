# Recursive theta: source statements for a core-link model

## Hypotheses

Let J=(V,E) be any finite r-uniform hypergraph, r>=1. Edges are
r-element subsets, with distinct vertices. An independent set contains
no edge. Let IND(J) be the convex hull of independent-set indicators.
For r>=2 and x in V, V_x consists of those y!=x occurring together
with x in an edge; J_x has edges e with e union {x} in E.
All matrices below are real and symmetric; PSD means positive semidefinite.
No regularity or vertex-transitivity assumption is imposed.

## Conclusion

Castro-Silva et al.'s Definition 1.1 defines TH(J)=IND(J) for r=1.
For r>=2 a vector f belongs to TH(J) precisely when a matrix F exists
with diagonal f such that

\[
 R(F)=\begin{pmatrix}1&f^t\\f&F\end{pmatrix}\succeq0,
 \qquad F_x[V_x]\in f(x)\,\mathrm{TH}(J_x)\quad(x\in V).
\]

An empty link imposes no row constraint. The scaled-set condition is
retained when f(x)=0; division by f(x) is not part of the definition.
For r=2 this recovers the graph lift: F(x,y)=0 on every graph edge.
Theorem 2.1 says TH(J) is compact and convex and contains IND(J).
With nonnegative vertex weights w, Corollary 2.3 therefore bounds
alpha(J,w) by max_{f in TH(J)} w^t f. In particular w=1 concerns
ordinary cardinality and needs no edge-induced uniform distribution.

For the same finite hypergraphs, Theorem 2.4 gives the exact supporting
inequality description

\[
 \mathrm{TH}(J)=\{g\in\mathbb R^V_{\ge0}:
 w^tg\le\vartheta(J,w)\text{ for every }w\in\mathbb R^V_{\ge0}\},
 \qquad \vartheta(J,w)=\max_{g\in\mathrm{TH}(J)}w^tg.
\]

It also says TH(J) is of antiblocking type. This applies to the graph
links in L027 without a regularity hypothesis. It supplies an inequality
description, not the values of their weighted theta numbers.

## Proof

Precise citation: Davi Castro-Silva, Fernando Mário de Oliveira Filho,
Lucas Slot and Frank Vallentin,
[A Recursive Theta Body for Hypergraphs](https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf),
Combinatorica 43 (2023), 909–938, DOI 10.1007/s00493-023-00040-9,
final published version: equation (2), printed p. 911; Definition 1.1,
p. 912; Theorem 2.1 and its full proof, pp. 915–916; Corollary 2.3,
p. 917. These passages were inspected, including the independent-indicator
lift, the r=1 base, empty-link convention and closed scaled-link constraints.
These are imported source statements, not a local reproof.
The direct publisher PDF was successfully retrieved again on 2026-10-06
for recovery review of the same cited statements and complete proofs;
no mathematical statement or applicability scope changed.

Theorem 2.4 and its complete proof, printed pp. 917–918, were inspected
on 2026-10-06 for the quantitative-cap review. The proof covers r=1,
uses induction and an indicator Hadamard product to remove negative
weights, then closed convex separation and downward closure. The above
statement is imported by citation, with no local reproof.

Theorem 2.5 and its complete proof, pp. 918–919, give polynomial-time
**weak** optimization for fixed uniformity on the explicitly represented
hypergraph. The proof treats graphs as a separate base; for r>=3 it
uses an interior ball of the unsliced lift and recursive membership
oracles. This is not an exact rational certificate or a practical
algorithm for L027's vertex set of all 7-subsets of 963 points. Adding
pair-zero equations is not covered by that proof's interior-ball
argument. No complexity theorem for the joint affine slice is imported.

Section 4, pp. 924–926, including equation (17), Theorem 4.1 and its
proof, distinguishes TH(J)'s antiblocker from TH of the complementary
hypergraph when r>=3. Theorem 4.1 uses a different body TH-circle; it
does not identify a graph-style complementary-theta dual for L027's
joint lift. Its proof's Appendix A duality input was not independently
audited because no such theorem is applied here. The graph-link
supporting description in Theorem 2.4 is the relevant imported input.

The proposed RS model combines a pair-conflict graph and a labeled
3-uniform hypergraph on the same core-link vertex set. The source does
not assert the joint specialization or its core-incidence transfer:
those differences are now established in L027. It supplies
neither a numeric improvement nor full-SDP feasibility. Symmetry reduction
would require actual automorphisms (Section 5, pp. 926–927); none are
assumed. No spectral proof or weak-optimization complexity theorem is
needed for this input.

## Mathlib

Full matching recursive hypergraph theta theorem: not checked.
Supporting PSD and finite-set counting coverage: not checked.
Unknown coverage is not evidence of absence. The cited source provides
the mathematical input; the unresolved quantitative RS transfer is separate.

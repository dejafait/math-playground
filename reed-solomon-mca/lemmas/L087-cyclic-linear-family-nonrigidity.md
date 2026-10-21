# L087 — A cyclic linear family not isomorphic to L072

## Hypotheses

Let V=Z/16Z and B={0,1,4,6}. Define the block family
F={B+t : t in Z/16Z}. Isomorphism of families means a bijection of
vertices carrying the complete block set of one family onto the other.
The comparison family is exactly the sixteen blocks of L072, namely
four parallel classes of the affine plane on F_4^2: the vertical class
and slopes 0,1,u, where u^2=u+1.

## Conclusion

F consists of sixteen distinct four-element blocks, every vertex has
degree four, and every two distinct blocks intersect in at most one
vertex. Nevertheless F is not isomorphic to L072's family under any
vertex bijection. Thus simple linear degree-four four-uniform families
on sixteen vertices are not unique up to isomorphism.

This is an abstract incidence counterexample to rigidity, not an RS
equality construction or a counterexample to the uniform triangle bound.
No marked-triangle, moment, weight, parameter or rational-chart claim
is included. The global interval 11/q–16/q is unchanged.

## Proof

### Import and applicability

Import the modular-ruler cyclic construction from Marco Buratti and
Douglas R. Stinson, *New Results on Modular Golomb Rulers, Optical
Orthogonal Codes and Related Structures*, arXiv:2007.01908v2,
11 October 2020, Lemma 2.1 (p. 5), Table 1's k=4 rows (p. 6),
and the cyclic configuration correspondence in Theorem 1.6 (p. 2):
[primary manuscript](https://arxiv.org/pdf/2007.01908v2), published
in *Ars Mathematica Contemporanea* 20(1) (2021), 1–27,
[DOI](https://doi.org/10.26493/1855-3974.2374.9ff).
The ordinary four-mark ruler (0,1,4,6) has length L=6; the extension
hypothesis v>=2L+1 holds at v=16. The development formula is also
explicit in Alexander A. Davydov et al., *On constructions and
parameters of symmetric configurations v_k*, arXiv:1203.0709v1,
4 March 2012, Definition 3.3 and equation (3.8), p. 12,
with the circulant characterization in Theorem 1.5(ii), p. 4:
[primary manuscript](https://arxiv.org/pdf/1203.0709v1).
These sources were inspected in the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-linear-sixteen-family-rigidity.md`.
General ruler existence and configuration enumeration are not reproved.
The following small difference checks make the applicability and the
new local comparison explicit.

The six positive differences between marks, in pair order
(1,0),(4,0),(6,0),(4,1),(6,1),(6,4), are
1,4,6,3,5,2. Hence the twelve ordered differences modulo sixteen
are precisely 1,...,6 and 10,...,15, each occurring once.

Every translate has four distinct vertices. If B+t and B+s contain
two distinct common vertices x,y, write x=b+t=b'+s and
y=c+t=c'+s with b,c,b',c' in B. Ordered-difference uniqueness for
x-y=b-c=b'-c' gives b=b' and c=c', whence t=s.
Thus distinct translates meet in at most one vertex and cannot be
equal. There are sixteen distinct blocks. For each vertex x, its
containing translates have exactly the four distinct shifts x-b,
b in B, so its degree is four. This verifies every required incidence
hypothesis without relying on a census or sampled check.

### A complete isomorphism invariant

For any block family define its noncollinearity graph on its vertices:
two distinct vertices are adjacent exactly when no block contains both.
A family isomorphism preserves this predicate in both directions,
so it induces a graph isomorphism and preserves connected components.

In F, vertices x,y occur together in a translate if and only if
x-y is an ordered difference of B. Necessity follows by subtracting
the two translated marks; for sufficiency choose marks b,c with
b-c=x-y and shift t=x-b, giving y=c+t.
Consequently the full noncollinearity graph joins x to x+7,x+8,x+9,
and has no other edges. In particular the difference-7 edges contain
the cycle x_j=7j mod 16, 0<=j<=16. Its first sixteen vertices are
distinct: 7(j-k)=0 mod 16 implies j=k mod 16 since gcd(7,16)=1.
It is a cycle through all vertices, so this graph has one connected
component of size sixteen. The difference-8 edges are also retained;
connectivity is a property of the complete graph, not of a preview.

In L072, every pair of distinct points lies on a unique affine line.
Indeed equal X-coordinates give the vertical line; otherwise the
slope is (Y-Y')/(X-X') and the intercept is determined uniquely.
The five available parallel classes are vertical and slopes
0,1,u,u+1. L072 keeps precisely the first four. Thus a pair occurs
in no retained block if and only if its unique line has slope u+1.
The four lines Y=(u+1)X+e, e in F_4, partition the sixteen points
into four sets of size four. All pairs within any such set are
noncollinear in the retained family; every pair in different sets
has a retained unique line. Therefore the complete noncollinearity
graph is exactly four disjoint copies of K_4, with component sizes
4,4,4,4.

The complete component-size multisets {16} and {4,4,4,4} differ.
No graph isomorphism, and hence no family isomorphism, can exist.
This settles the approved rigidity-or-counterexample target negatively
for rigidity. No full classification is needed.

### Qualifications and verification

The cyclic construction is known mathematics imported above. Its
comparison to the exact L072 family is the local specialization;
POTENTIALLY_NEW records only that the prior assessment did not establish
coverage of this comparison, not originality. L086 motivates the
abstract class but is not a mathematical premise here; L079 excludes
L072 only and is not transferred to this nonisomorphic family.
An auxiliary characteristic-two plane is used only for the comparison.
Neither family is endowed here with actual characteristic-97 moments.

The analytic proof covers every ordered difference, all blocks and
both complete graphs. Supplementary reproduction is
`python3 scripts/triangle-incidence/verify_cyclic_nonrigidity.py`.
Its full certificate is
`scripts/triangle-incidence/cyclic-nonrigidity-certificate.json`,
containing all blocks, degrees, block intersections, pair multiplicities,
graph edges and components for both families. The code builds the
L072 graph from its exact sixteen-block label table, independently of
the missing-slope graph argument. No computational bound is essential
to the proof.

The separate critical audit on 14 October 2026 (step 219) found no
defect in the analytic argument or its stated scope. It checked all
twelve ordered differences, both directions of the pair-containment
equivalence, distinctness and degree of all translates, the spanning
cycle, the omitted parallel class and invariance under arbitrary vertex
bijections. The L072 coordinate table, complete labeled block table and
the verifier's numeric table agree in all sixteen blocks. In numeric
row-major labels, the omitted slope lines are {0,7,9,14}, {1,6,8,15},
{2,5,11,12}, {3,4,10,13}; each contributes its complete K_4.

Independent supplementary replay is
`python3 scripts/triangle-incidence/audit_cyclic_nonrigidity.py`;
its full artifact is
`scripts/triangle-incidence/cyclic-nonrigidity-audit.json`.
It parses both canonical L072 tables, reconstructs lines using arithmetic
in F_2[u]/(u^2+u+1), and compares every field of the original certificate:
all sixteen blocks and degrees, all 120 block intersections and 120
vertex-pair multiplicities per family, every graph edge and every
component. Components are independently computed by transitive closure.
All fourteen audit checks passed and the original certificate's SHA-256
was unchanged by reproduction. The replay shares Python with the
producer; it is supplementary to the complete analytic proof, not a
general classification or an RS-field computation. This audit establishes
no additional theorem and supplies no moments, weights or parameters.

## Mathlib

The full construction and nonisomorphism comparison were not checked
in Mathlib. No Mathlib theorem or library absence is claimed. The primary
citations and complete elementary specialization above supply the input.

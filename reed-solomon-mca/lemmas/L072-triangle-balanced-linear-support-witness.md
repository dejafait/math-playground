# L072 — Balanced linear supports containing the prescribed triangle

## Hypotheses

Let V consist of sixteen distinct abstract labels
\(a,b,c,y_1,y_2,z_1,z_2,w_1,w_2,d_1,\ldots,d_7\).
Prescribe
\[
A_0=\{a,b,y_1,y_2\},\quad A_1=\{a,c,z_1,z_2\},\quad
A_2=\{b,c,w_1,w_2\}.
\]
These are the support names in L057, but no moment, RS-field, weight,
parameter or recovery hypothesis is imposed here.

## Conclusion

There are sixteen distinct four-subsets of V containing these three
sets, with each label in exactly four sets. Any two distinct sets
intersect in at most one label, hence in particular this holds among
the thirteen additional sets. Balance and this prescribed triangle
alone cannot force two additional supports with union of size five
or six. This is an abstract incidence witness, not an equality pencil
or a counterexample to uniform triangle twelve.

## Proof

Import the finite-affine-plane coordinate construction and selection
of parallel classes from Oktay Olmez and Aditya Ramamoorthy,
*Repairable Replication-based Storage Systems Using Resolvable Designs*,
[arXiv:1210.2110v1](https://arxiv.org/pdf/1210.2110v1), 7 October 2012,
Section III, Definition 3 and class-selection paragraph, pp. 3–4;
Section III.A, p. 4, and Lemma 2, p. 5. It supplies the points
\(\mathbb F_t^2\), vertical lines and lines \(Y=mX+e\), with each
parallel class a partition and different-class intersections of size
one. Here t=4 is a prime power and four classes are selected from the
available five. General plane existence is not reproved. The following
coordinate and labeling checks are the required specialization, not
a claim of a new design construction.

Write \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\). The defining
quadratic has no root in \(\mathbb F_2\), so this is a field, with
elements \(0,1,u,u+1\) and \(u^2=u+1\). Label its sixteen points by:

| X \\ Y | 0 | 1 | u | u+1 |
|---|---|---|---|---|
| 0 | a | b | y_1 | y_2 |
| 1 | c | d_1 | d_2 | d_3 |
| u | z_1 | d_4 | d_5 | w_1 |
| u+1 | z_2 | d_6 | w_2 | d_7 |

This is a bijection since every point and label appears once. Choose
the vertical class and the three slope classes m=0,1,u. Their complete
blocks are as follows; row e means the intercept in Y=mX+e.

| Coordinate/intercept | vertical X=e | slope 0 | slope 1 | slope u |
|---|---|---|---|---|
| 0 | {a,b,y_1,y_2} | {a,c,z_1,z_2} | {a,d_1,d_5,d_7} | {a,d_2,w_1,d_6} |
| 1 | {c,d_1,d_2,d_3} | {b,d_1,d_4,d_6} | {b,c,w_1,w_2} | {b,d_3,d_5,z_2} |
| u | {z_1,d_4,d_5,w_1} | {y_1,d_2,d_5,w_2} | {y_1,d_3,z_1,d_6} | {y_1,c,d_4,d_7} |
| u+1 | {z_2,d_6,w_2,d_7} | {y_2,d_3,w_1,d_7} | {y_2,d_2,d_4,z_2} | {y_2,d_1,z_1,w_2} |

The prescribed blocks are X=0, Y=0 and Y=X+1. Their pairwise
intersection points are respectively (0,0)=a, (0,1)=b and (1,0)=c,
which are distinct. The remaining points on those three lines are
exactly the six displayed singleton labels, so their union has nine
labels and no triple intersection.

For completeness, the incidence verification in this specialization
covers every pair of blocks. A vertical line has four points. A
nonvertical line has one point for each of the four X-values. Distinct
vertical lines are disjoint. Two nonvertical lines of the same slope
and different intercepts are disjoint, since subtracting their equations
would equate different intercepts. A vertical and a nonvertical line
meet at exactly the point with their prescribed X-value. Finally, two
lines with different slopes meet at exactly one point: subtracting
their equations gives \((m-m')X=e'-e\), and \(m-m'\ne0\) is
invertible in this field. Thus every pair has intersection at most
one, and no two blocks coincide (coincidence would give intersection
four). There are four blocks in each of four classes, so sixteen
distinct blocks. Each point is in its unique vertical line and in
exactly one line of each chosen slope, with intercept Y-mX. Its degree
is therefore exactly four. Removing the three prescribed blocks
leaves thirteen distinct blocks with the claimed pair bound. For two
of them, union size is 8 minus intersection size, hence seven or eight,
never five or six. This proves the conclusion.

The auxiliary field has characteristic two and is not an embedding
into the characteristic-97 RS field. The bijection may be transferred
to any abstract sixteen-label set, including the set underlying H;
that transfer asserts only incidence and no moment compatibility.
This witness does not supply any nonzero error weights, original
finite parameters, locators or same-support failures. Those independent
conditions remain unresolved.

Supplementary exact reproduction: run
`python3 scripts/triangle-incidence/verify_affine_plane.py`. Its full
certificate at `scripts/triangle-incidence/affine-plane-certificate.json`
contains all sixteen coordinate blocks, the label bijection, sixteen
degrees and all 120 pair intersections, with the thirteen-block
restriction marked. The analytic proof above is independent of this
finite check; no sampled absence or computed general maximum is used.

## Mathlib

Coverage of this complete labeled specialization was not checked.
No Mathlib theorem is used. The cited primary construction, together
with the explicit specialization above, is the mathematical input;
unknown library availability is not an absence claim.

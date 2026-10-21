# Affine-plane rank-two attempt

Approved target: determine whether L072's sixteen-support family admits
an L010 equality pencil for any bijective fixed-H labeling over F_(97^20).
Reuse `drafts/literature/2026-10-12-affine-plane-equality-realization.md`;
no source refresh or sampling campaign. ATTEMPTS/020 and /027 remain
stops on positive-only sampling and balance-only extraction respectively.

Main gap: exclude sixteen actual bad parameters; this family is only
one obstruction, and arbitrary families and challenge qualifications
remain unresolved. Intermediate target: use L073/L074's rank-two-only
kernel to prove uniqueness and prime-field descent of a possible
transversal, then retain every full-weight gate. A unique rational plane
would turn extension-field feasibility into explicit prime-field linear
algebra for each labeling, without claiming a uniform rank computation.

Working argument saved before completion: two independent decomposable
kernel tensors p,q have rank-two sum, so their image planes meet in a
line l and span a three-space T. At most one of four disjoint vertical
blocks contains l. For each other block, the two transversal lines
are distinct and span a two-space inside T. Two such two-spaces must
meet, contradicting the disjoint moment spans. Thus dim K should be at
most one. All equations are over F_97, so a surviving K and its image
plane should descend. These implications still require a complete
proof, including intersection dimensions and coefficient tests.

Continuation/abandonment test: a uniform zero-kernel or zero-coefficient
obstruction excludes the family; a complete full-weight survivor needs
all L010 chart, determinant, locator and same-support checks. A new
necessary restriction is useful only with an explicit closure test.
No genericity, prime-field affine chart or sampled maximum is assumed.

Completed result: [L075](../lemmas/L075-affine-plane-unique-transversal-descent.md)
proves dim K<=1 and descent of the unique surviving plane to F_97.
It also completes the conditional full-weight construction: rank 27
and all 64 coefficients nonzero are necessary and sufficient. Sixteen
distinct rational intersection lines admit a rational finite chart;
the full-error determinant formulas verify D and every locator before
L010 supplies same-support failure and equality over the extension.
This does not assume the original chart is rational. No passing
labeling, uniform coefficient obstruction or rank-28 theorem was found.

The concrete remaining closure test is whether every rank-27 labeling
has a zero coefficient in at least one support intersection. The new
rank bound and descent make this a prime-field test with one candidate
plane per labeling. Its complete quantifier has not been evaluated;
positive-only label samples remain insufficient. L073/L074/L075 await
separate audits. No mathematical script or external source refresh was
needed. This is a partial local advance, not certified originality or
a complete challenge candidate.

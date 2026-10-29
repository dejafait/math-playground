# C155a — Original-pair Segre locus and both quotient ranks

## Hypotheses

Let E be any field extension of F_97. Use L155's original domain:

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

Index the 756 supports I_j union K_j by (I_j,K_j) in
binom(S,2) times binom(J,2), with I outermost and both pairs in
increasing lexicographic order. Fix any original a<b with disjoint
four-element supports. No symmetry quotient or preferred pair is used.
Put W=E^S in increasing coordinate order. For j=a,b use exactly the
original L109/L155 maps, with

\[
 z_j=\min(S\setminus I_j),\qquad
 g_j(X)=\prod_{y\in J\setminus K_j}(X-y),\qquad
 (Q_jw)_x=g_j(z_j)w_x-g_j(x)w_{z_j}
 \quad(x\in(S\setminus I_j)\setminus\{z_j\}).
\]

The target coordinates are in increasing x-order. Let N_j be the
matrix of exterior-square(Q_j) in increasing coordinate-pair bases,
as in L109, and put

\[
 A=V_a=\ker Q_a,\quad B=V_b=\ker Q_b,\qquad
 \mathcal K=\ker\begin{bmatrix}N_a\\N_b\end{bmatrix}
                 \subseteq\bigwedge^2W.
\]

Use L155, including its audited L153 finite input: dim A=dim B=3,
A intersect B=0, and \(\mathcal K=A\wedge B\), where the last expression
is the nine-dimensional **linear span** of mixed wedges. The finite
input's original-domain and verification qualifications are inherited.
No equality-pencil or recovery-gate hypothesis is imposed here.

## Conclusion

For every such original pair and every E/F_97, the map

\[
 \Phi_{a,b}:\mathbb P(A)(E)\times\mathbb P(B)(E)
       \longrightarrow\mathbb P(\mathcal K)(E),\qquad
       ([x],[y])\longmapsto[x\wedge y]                         \tag{1}
\]

is the Segre embedding in the mixed-wedge coordinates. Its image is
exactly the projective nonzero decomposable locus of the common kernel in the
**original** exterior-square(W). Equivalently, after choosing any
bases a_1,a_2,a_3 of A and b_1,b_2,b_3 of B, it has coordinates

\[
 ([s_1:s_2:s_3],[t_1:t_2:t_3])
            \longmapsto[(s_it_j)_{1\le i,j\le3}]
 \quad\text{in the basis }(a_i\wedge b_j)_{i,j}.              \tag{2}
\]

For every point [p] of this locus, let L be its reconstructed
two-dimensional E-subspace of W. Then

\[
 \operatorname{rank}(Q_a|_L)=\operatorname{rank}(Q_b|_L)=1,
 \qquad
 L=(L\cap A)\oplus(L\cap B)\subseteq A\oplus B.              \tag{3}
\]

Both intersections in (3) are one-dimensional. They are the unique
ordered pair of factor lines giving [p] in (1). In particular no
additional decomposable point arises from a plane having a component
outside A direct-sum B in the seven-dimensional W.

These are statements about field-valued points. No equality of
scheme-theoretic intersections, reducedness or descent of a plane from
E to F_97 is asserted. Both selected-row ranks hold before coding
gates; rank tests for other rows and all weight/chart gates remain open.
This is a local partial result; its first separate critical audit below
passes with the inherited finite-input qualifications.

## Proof

### Imported geometry and the local specialization needed

Import the arbitrary-field correspondence between the Segre variety
S_(n,n) and projective lines meeting two fixed disjoint projective
n-spaces from Laura Bader, Antonio Cossidente and Guglielmo Lunardon,
*Generalizing flocks of Q+(3,q)*, Advances in Geometry 1 (2001),
323–331, DOI 10.1515/advg.2001.019,
[section 2, definition and proof of Theorem 1, pp. 324–325](https://www.researchgate.net/publication/249879499_Generalizing_flocks_of_Q_3q).
Section 2 works over an arbitrary field K. Only this correspondence
with n=2 is used, not the theorem's further Veronese/regulus claim or
the later finite-field flock constructions. The two projective planes
here are P(A) and P(B), disjoint by L155, in P(A direct-sum B).
Their vector sum has dimension six, so this is the source's P^5(E).

Import the Segre closed immersion over every base scheme from
[Stacks Project, Lemma 27.13.6, Tag 01WD](https://stacks.math.columbia.edu/tag/01WD),
specialized to Spec(E) and the two projective planes. It supplies the
embedding with product coordinates in (2), without assuming algebraic
closure. Neither source by itself exhausts the decomposable points of
our given exterior subspace in W. The actual-map, ambient-plane and
rank checks below are precisely the remaining local applicability
argument; no general Segre theorem is being reproved.

For exterior bases, induced maps and inclusions of vector subspaces,
use Keith Conrad, [*Exterior Powers*](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated 47-page author PDF inspected 2026-10-25, Theorem 4.2,
pp. 11–12; Theorem 5.1, pp. 15–16; Theorem 5.6 and Corollary 5.9,
p. 18. For vanishing versus independence, plane reconstruction and
its uniqueness, use Theorem 7.1 (with its following all-fields
qualification), Corollary 7.3, Theorem 7.5 and Corollary 7.6,
pp. 23–26. These apply to finite-dimensional vector spaces over E;
the caveat about general module inclusions is irrelevant. Standard
rank-nullity applies to the restricted E-linear quotient maps.
The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-l155-segre-locus-and-projection-ranks-review.md`.
Its inspected source coverage is reused, with no new discovery claim.

### The original coordinates give exactly the Segre map

By L155, any chosen bases of A and B give the nine-vector basis
(a_i wedge b_j) of the common kernel. For nonzero x in A and y in B,
disjointness makes x,y independent, so x wedge y is nonzero. The
linear-span identity in L155 puts it in the common kernel. Multiplying x and
y by nonzero scalars multiplies their wedge by their product, making
(1) well-defined on E-projective points.

Writing x=sum_i s_i a_i and y=sum_j t_j b_j and using bilinearity
gives exactly (2). Thus the imported Segre map, followed by this
linear coordinate identification, is (1). This fixes the factor
order A then B. In the original increasing S-coordinate basis its
coefficient on e_r wedge e_s is x_r*y_s-x_s*y_r for r<s, the same
wedge convention as L109's N_j. The adapted mixed basis is a basis
of the original common kernel, not a replacement of the original
quotient matrices or a transport from another labeled pair.

For this image point set L=span_E(x,y). The actual map Q_a kills x
and does not kill y, since y is nonzero in B and A intersect B=0.
Its restriction therefore has rank one. Q_b kills y and does not
kill x for the same reason, so its restriction also has rank one.
This proves inclusion in the stated decomposable locus and both
ranks for all image points without a coding-pencil assumption.

### Exhaustion in W and exclusion of both rank-zero branches

Conversely, let p=u wedge v be any nonzero decomposable element of
the common kernel with u,v in W. The imported exterior facts imply that
u,v are independent and that [p] determines the plane L=span_E(u,v)
uniquely, independently of this choice of wedge factors. If the locus
is instead described by E-valued Plucker equations, L109's nonzero-pivot
reconstruction produces such u,v in E itself. No field descent is needed.

For each j=a,b, the original matrix identification gives

\[
 0=N_jp=Q_j(u)\wedge Q_j(v).
\]

The vanishing criterion for an elementary wedge says exactly that
these two image vectors are dependent. Thus rank(Q_j restricted to L)
is at most one; its possibilities are zero and one.

Suppose first rank(Q_a restricted to L)=0. Then L lies in A.
But Q_b restricted to A has kernel A intersect B=0, so it is
injective. Its restriction to the two-dimensional L would have rank
two, contradicting N_bp=0. This excludes the first rank-zero branch.
Separately, if rank(Q_b restricted to L)=0, then L lies in B,
and injectivity of Q_a on B forces rank(Q_a restricted to L)=2,
contradicting N_ap=0. Hence both ranks are one. This uses disjointness
from the audited linear bridge, not actual-pencil nonpersistence.

Rank-nullity on L now gives

\[
 \dim(L\cap A)=2-\operatorname{rank}(Q_a|_L)=1,\qquad
 \dim(L\cap B)=2-\operatorname{rank}(Q_b|_L)=1.
\]

These lines have zero intersection because A intersect B=0. Their
direct sum is a two-dimensional subspace of the two-dimensional L,
so it equals L. This proves (3) **in W** and forces every such plane
into A direct-sum B. In particular a plane using the remaining
one-dimensional complement of A direct-sum B cannot be an omitted component:
the actual rank bounds already force it to be spanned by these two
kernel-intersection lines. No generic-position or ambient-dimension
substitution was used.

Choose nonzero x in L intersect A and y in L intersect B. They form
a basis of L, so exterior-square(L) is one-dimensional and its
nonzero elements p and x wedge y are proportional over E. Therefore
\([p]=\Phi_{a,b}([x],[y])\), using the map in (1).
If another ordered pair of factor lines gives [p], its wedge determines
the same L by the imported reconstruction theorem. Its A-line must be
L intersect A and its B-line must be L intersect B, since these
intersections are one-dimensional. This proves exhaustion and
uniqueness, including E-rational factors. The resulting correspondence
is exactly the imported two-disjoint-space correspondence after the
local ambient and quotient checks, now identified with (2).

### Uniformity and limits of the conclusion

The argument fixes an arbitrary original a<b and an arbitrary E/F_97.
All uses of the finite registry and scalar extension are through
L155's audited disjointness and mixed basis. Thus all 79,380 original
pairs are covered with their own actual Q/N maps, without samples,
symmetry reduction, relabeling or any base-field representative of
an extension-field plane. No finite census or mathematical script
is needed for this specialization. It is REPRODUCTION of the inspected
general geometry with the missing original-domain applicability checks,
not mathematical originality or progress beyond the checked sources.

For prospective coding use retain q=97^20, k=8, the pinned
1/4<=delta<5/16 cell, coefficient syndromes in U_S, actual nonzero D
and locators, sixteen original finite events, coding t=0, arbitrary
weights and original chart, and all L056/L069/L040 plus L051/L055
qualifications inherited by the represented class. The theorem only
settles decomposability and the two selected quotient ranks. It does
not force nonzero lambda or any of L109's full-weight inequalities,
make a given direction finite in the original chart, or give rank
one for an additional row. A nonzero linear combination of mixed wedges
whose projective class lies outside the Segre image is not decomposable.

C152a/L086/L152 and L154 are prospective uses, not premises of this
proof. Uniform twelve-row compatibility and a usable many-row solving
bound remain open, as do representation, sharp wider radii and challenge
identification. No numeric extracted pair is identified; L151 label
limits, L104 survivors and ATTEMPTS/041–043,/048–049 are preserved.
The frozen-model interval remains 11/q–16/q. The separate critical audit
below checks this local result; no complete challenge candidate is asserted.

### Separate critical audit — step 489, 2026-10-25

The first separate audit used the unchanged invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-25-c155a-critical-audit-review.md`.
It inspected the complete statement and proof above against L109's
actual covectors, exterior matrix and nonzero-pivot reconstruction,
and L155's audited conclusions and qualifications. The inspected primary
coverage recorded in the step-485 assessment is reused: Bader–Cossidente–
Lunardon section 2, pp. 324–325, Stacks Tag 01WD, and the Conrad results
cited above. No essential theorem case is missing from that coverage.
This audit does not replay L153 or L155, and uses no new mathematical
input beyond the existing L109/L155 dependencies and cited standard tools.

**Actual coordinates and source hypotheses.** The four covectors in
each Q_j are precisely L109's, with z_j the least element of S minus I_j.
Their entries use the original labels embedded in E. In particular
g_j(z_j) is nonzero: its roots belong to J, disjoint from S, and the
field embedding preserves the nonzero differences. For r<s, x<y the
coefficient of e_x wedge e_y in exterior-square(Q_j)(e_r wedge e_s)
is c_{jx,r}c_{jy,s}-c_{jx,s}c_{jy,r}. Commutativity identifies this
with L109 (1), so N_j p=0 is the actual induced-map equation, with
no sign reversal or replacement of a labeled quotient. L155 supplies
the mixed-wedge basis for any bases of A and B. Bilinearity gives
s_i t_j in that basis, while the coefficient in the original W basis
is x_r y_s-x_s y_r. Thus the coordinate identification used for the
imported Segre embedding is an isomorphism onto the stated common
kernel. Its source consists of two disjoint projective planes in
P(A direct-sum B)=P^5(E), exactly the n=2 two-space correspondence.
Stacks supplies the embedding over Spec(E); no scheme-theoretic
intersection claim is inferred from it. Conrad's tools apply to vector
spaces over any field, including E, rather than arbitrary modules.

**Every ambient plane and both zero cases.** Start with any nonzero
decomposable p in the actual common kernel inside exterior-square(W),
without first restricting its plane to A+B. Its independent factors
span a two-dimensional E-plane L. For each selected row N_jp=0 means
that its two image vectors are dependent, hence rank(Q_j|_L)<=1.
If rank(Q_a|_L)=0, then L is contained in A. The kernel of Q_b on
A is A intersect B=0, so its restriction to L is injective and has
rank two, contrary to the b equation. Independently, rank(Q_b|_L)=0
puts L in B, where Q_a is injective, contrary to the a equation.
Both contradictions include the possibility that both ranks were zero.
Neither uses actual-pencil nonpersistence, weights, a finite chart,
generic position, or support disjointness in place of L155's kernel
disjointness. Rank-nullity now gives one-dimensional L intersect A
and L intersect B. They have zero intersection and their dimensions
sum to dim L, proving that they span L. This exhausts W itself;
no plane with a component in its one-dimensional complementary
direction survives the two rank constraints.

**Converse, scalars and uniqueness.** For arbitrary nonzero x in A
and y in B, disjointness implies independence. Their nonzero wedge
is in the common kernel, and the respective images under Q_a and Q_b
span nonzero lines: Q_a y and Q_b x cannot vanish. Thus the converse
has both ranks exactly one and requires no extra gate. Rescaling x,y
by nonzero E-scalars rescales their wedge by the product. Conversely,
for a locus point, generators of L intersect A and L intersect B
form an E-basis of L, so their wedge is a nonzero E-scalar multiple
of p. The exterior-plane uniqueness theorem then forces any second
ordered factor pair to be those same intersection lines. This checks
surjectivity and injectivity on E-points, not merely geometric points.
If the locus is supplied by E-valued Plucker equations, L109's formula
u_x=p_xb/p_ab, v_x=p_ax at a nonzero pivot p_ab reconstructs the wedge
over E: its determinant is
(p_xb p_ay-p_yb p_ax)/p_ab=p_xy by the antisymmetric Plucker relation.
At the pivot coordinates u_a=1, u_b=v_a=0, v_b=p_ab, so independence
is retained. Thus the optional equation-based description does not
silently assume rational descent or algebraic closure.

**Verdict and boundary.** Pass for the complete stated field-valued
locus, both selected ranks and unique ordered factor lines, for every
original pair and every E/F_97, conditional on L155's existing audited
finite input. No repaired assertion, extra hypothesis or DAG edge is
needed. This is REPRODUCTION and a first critical verification of an
existing partial result, not a new theorem beyond the checked sources.
All additional-row ranks, nonzero lambda, full weights, original-chart
conditions, representation and challenge identification remain unresolved.
The audit neither excludes twelve rows nor improves the radius interval.
ATTEMPTS/048–049 still rule out unmotivated repetition of passed inputs.

## Mathlib

Full matching original-pair Segre-locus and quotient-rank result:
**not checked**. Supporting Segre embedding, projective/Plucker
reconstruction, induced exterior maps and rank-nullity coverage:
**not checked anew**. The precise standard sources used above supply
the imported mathematics. Unknown Mathlib availability is not evidence
of absence; the separate informal audit above is not formal
proof-assistant verification.

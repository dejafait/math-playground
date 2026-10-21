# L077 — Affine-plane quadrilateral cross-ratios

## Hypotheses

Let k=F_97, H its order-sixteen multiplicative subgroup, and
F=F_(97^20). Fix any bijection lambda from L072's sixteen abstract
points to H. Use exactly its selected vertical, slope-zero, slope-one
and slope-u blocks. Suppose they are the sixteen full error supports
of an L010 equality pencil. Write t_A for the projective syndrome
direction of the error on block A, in the projective line of its
two-dimensional syndrome plane S. For the equivalent rank-27 case,
use the conditional reduction of L075 and L076, including their
unaudited L073/L074 inputs. No labeling is assumed to satisfy it.

For distinct projective points p_i represented by nonzero two-vectors,
define

    chi(p_1,p_2,p_3,p_4) = [p_1,p_3][p_2,p_4]
                            /([p_1,p_4][p_2,p_3]),

where [p,q]=det(p,q). For scalars z_i, use representatives (1,z_i).
This expression is invariant under rescaling representatives and under
a common invertible change of coordinates.

## Conclusion

Choose one block A_i from each of the four selected parallel classes,
in that order, such that no three of the four blocks are concurrent.
There is exactly one point z_i of A_i belonging to none of the other
three blocks. With x_i=lambda(z_i), every equality realization obeys

    chi(t_A1,t_A2,t_A3,t_A4)
      = (x_3-x_1)(x_4-x_2)/((x_4-x_1)(x_3-x_2)).       (1)

There are exactly 48 such quadrilaterals. An explicit eleven-step
reconstruction below determines all sixteen t_A from

    t_V0, t_V1, t_V2, t_M0D0, t_M1D0.                  (2)

In the rank-27 case these directions lie on the rational plane of
L075. Normalize the first three to infinity, zero and one, respectively.
Only the two remaining seed values alpha,beta are free; they lie in
k minus {0,1} and are distinct. Thus there are 95*94=8930 ordered
seed choices for any fixed labeling. Each choice determines at most
one complete direction tuple, and must still pass pairwise distinctness
and all 48 identities. This count is an exact necessary search reduction,
not an enumerated bound or an assertion that any choice passes.

These identities do not assert moment compatibility, rank 27, full
recovered errors, or sufficiency for realization. No labeling is excluded
here. The family question, global 11/q–16/q interval, uniform triangle
twelve and challenge qualifications remain unresolved. The direct equality-pencil argument passed the separate L079 audit;
the earlier rank/fullness chain and its alternative application remain
unreviewed.

## Proof

### The four-error shortening identity

The four blocks have six distinct pair intersections, since all pairs
are from different classes and there is no triple concurrence. Each
block has three different intersection points and one singleton z_i.
Put U=lambda(A_1 union A_2 union A_3 union A_4); it has size
16-6=10. The four singletons are distinct.

Let e_i be the actual full error on lambda(A_i), and let s_i=sigma(e_i).
L010 gives ker(sigma)=C, where C consists of evaluations of polynomials
of degree less than eight. The s_i are nonzero and lie in
span{sigma(a),sigma(b)}, of dimension at most two. Their projective lines
are distinct: L072 gives intersections of size one between these blocks,
and eight-column independence makes U_A intersect U_B the moment span
of their single common coordinate. A shared syndrome line with full
four-coordinate expansions would contradict that independence.
The same argument, or L076, gives distinct lines for all sixteen blocks.
Consequently any two s_i are independent and span S.

Define E:F^4 -> F^H by E(c)=sum c_i e_i. It is injective: evaluating
at x_i gives c_i e_i(x_i), and e_i(x_i) is nonzero. Let

    R = {c in F^4 : sum c_i s_i=0}.

Then dim R=2 and E(R) is a two-dimensional subspace of the code
supported on U. Put Q(X)=product_(x in H minus U)(X-x), of degree six.
Every codeword supported on U is the evaluation of Q(X)(A+BX): its
degree-less-than-eight polynomial vanishes on the six distinct points
outside U, so is divisible by Q. Conversely each such polynomial gives
a supported codeword. Evaluation is injective by the degree/root bound.
This shortened code has dimension two; thus E(R) equals it exactly.

The coordinates (A,B) therefore identify R with F^2, and evaluation
at each singleton gives

    c_i = d_i(A+B x_i),   d_i=Q(x_i)/e_i(x_i) != 0.      (3)

Hence the four coordinate functionals on R have projective representatives
(1,x_i). Their cross-ratio equals the right side of (1), independently
of the nonzero factors d_i.

To compare this with the s_i, choose coordinates on S taking s_1,s_2
to (1,0),(0,1). Write s_3=(a,b) and s_4=(c,d). Pairwise distinctness
makes a,b,c,d and ad-bc nonzero. In coordinates (r,s) on R, its vectors
are

    (-a r-c s, -b r-d s, r, s).

The four coordinate functionals are (-a,-c),(-b,-d),(1,0),(0,1).
Their cross-ratio is bc/(ad). Direct determinants give the same
cross-ratio bc/(ad) for s_1,s_2,s_3,s_4. Combined with (3), this proves
(1). This computation is the needed four-error specialization; no
general dual-code or interpolation theorem is being asserted or
reproved. The root factorization and moment kernel are the existing
L010 inputs. All weights and original finite parameters may lie in F.

### Complete incidence description

Use auxiliary F_4 coordinates only, with addition denoted + and u^2=u+1.
Write V_i for X=i, M0D_j for Y=j, M1D_k for Y=X+k, and M2D_e for
Y=uX+e. The first three lines are concurrent exactly when k=i+j.
If k differs from i+j, their three pair intersections impose these
three forbidden intercepts for the fourth line:

    e_0=j+ui,   e_1=i+k+ui,   e_2=j+u(j+k).

They are distinct: with delta=i+j+k != 0 their pairwise differences
are delta, u delta and (u+1)delta. All four elements of F_4 sum to
zero, so the unique remaining intercept is

    e=e_0+e_1+e_2=i+(u+1)k+uj.                         (4)

This line avoids each of the three pair intersections. Thus the full
quadrilateral list is exactly the choices i,j,k in F_4 with k!=i+j,
and e given by (4). There are 4*4*3=48; every selection of one line
from each class either belongs to this list or has a concurrent triple.
Each singleton is obtained by deleting the three pair intersections
from its corresponding four-point line. No characteristic-two field
is embedded into the RS field, and no RS labeling symmetry is used.

### Reconstruction and exact gates

In the following table a quadrilateral is always ordered
(vertical, slope 0, slope 1, slope u). Its singleton tuple is in that
same order; it refers to abstract names from L072 before lambda is applied.
Starting with the five directions in (2), each row has exactly one
previously undetermined direction.

| Quadrilateral | Singleton tuple | Recovered direction |
|---|---|---|
| V1, M0D0, M1D0, M2D1 | d_2, z_1, d_7, b | M2D1 |
| V0, M0D0, M1D2, M2D1 | y_2, c, d_6, d_5 | M1D2 |
| V0, M0D3, M1D0, M2D1 | y_1, w_1, d_1, z_2 | M0D3 |
| V0, M0D3, M1D2, M2D0 | b, d_7, z_1, d_2 | M2D0 |
| V2, M0D0, M1D0, M2D2 | w_1, z_2, d_1, y_1 | M2D2 |
| V0, M0D0, M1D3, M2D2 | b, z_1, d_2, d_7 | M1D3 |
| V0, M0D1, M1D0, M2D2 | y_2, d_6, d_5, c | M0D1 |
| V0, M0D1, M1D2, M2D3 | a, d_4, d_3, w_2 | M2D3 |
| V0, M0D0, M1D1, M2D3 | y_1, z_2, w_1, d_1 | M1D1 |
| V0, M0D2, M1D0, M2D3 | b, d_2, d_7, z_1 | M0D2 |
| V3, M0D0, M1D0, M2D3 | d_6, c, d_5, y_2 | V3 |

Every row can be checked directly in L072's displayed block table or
by (4); the recovered blocks and five seeds exhaust all sixteen blocks.
Given three distinct projective points in any three slots of chi,
fixing a cross-ratio different from zero and one uniquely determines
the fourth, distinct from those three. To see this without division
by an affine coordinate, reorder slots so the unknown is last, and
apply the projectivity taking the three known points to infinity, zero
and one. In that coordinate chi(infinity,0,1,z)=z. Permuting slots
only replaces the cross-ratio by the corresponding permuted expression,
which is still the cross-ratio of four distinct singleton labels.
Thus it is defined and differs from zero and one. Recover in homogeneous
coordinates, retaining possible infinity values. If a recovered point
coincides with any other previously known point, reject the seed choice.

L075 descends S and its sixteen intersections to k in the rank-27
case; L076 supplies full coefficients and distinct lines. A rational
projectivity uniquely takes t_V0,t_V1,t_V2 to infinity, zero, one.
The other two seed points are distinct elements of k minus {0,1}.
There are 95 choices for alpha and 94 for beta. The table proves at
most one complete tuple for each ordered choice. All recovered points
remain rational whenever the branch stays distinct, since each step
uses rational homogeneous linear equations. This does not rationalize
an original affine chart or its excluded point.

After reconstruction, test pairwise distinctness and the full set of
48 equations, rather than only these eleven defining equations. In
homogeneous form the equation for the last slot is

    [p_1,p_3][p_2,p_4]-r[p_1,p_4][p_2,p_3]=0,

with r the right side of (1). The first-three distinctness and r not
in {0,1} ensure a unique projective solution. Pairwise distinctness
of the final tuple ensures that cross-multiplication of any remaining
equation introduces no zero-denominator branch. Even a passing tuple
is only necessary: full eight-moment compatibility must still be
checked by the original matrix or an independently proved equivalent
test. No positive-only sampling or sufficiency inference is made.

Supplementary complete incidence verification:
`python3 scripts/triangle-incidence/affine_plane_quadrilaterals.py`.
The certificate `scripts/triangle-incidence/affine-plane-quadrilaterals.json`
records all 256 class selections and all their triple intersections,
the 48 singleton tuples, the formula-set equality and the complete
eleven-step chain. It passes 256/256 coverage, 48/48 quadrilaterals
and 16/16 reconstructed blocks, with no failures. The proof uses the
explicit formula and table above; this script checks their finite
incidence specialization and does not test a single H-labeling or
an RS realization. The cross-ratio proof is algebraic, not numerical.

The concrete closure test is elimination of the two normalized seeds
against all 48 identities, uniformly retaining every H-bijection and
all distinct projective branches. A uniform contradiction would force
rank 28 by L075/L076. A passing labeling would require its complete
original kernel before claiming realization. This is a necessary
restriction toward that test, not a family decision or a complete route
through the independent triangle and challenge-definition gaps.

The separate October 12 L079 audit found no defect in the direct
equality-pencil shortening identity, ordered cross-ratio comparison
and complete incidence/reconstruction tables used here. This scoped
acceptance does not audit the alternative rank-27 descent through
L073–L076. Full replay details are recorded in L079.

## Mathlib

Coverage of this exact family-specific cross-ratio and reconstruction
statement is not checked. No Mathlib theorem is used; unknown coverage
is not evidence of absence. L010 supplies the established moment
kernel and polynomial degree bound; L072 supplies the cited incidence
construction and explicit specialization. L075/L076 are used only for
the rational rank-27 application. The unchanged EXPLORE assessment
did not establish coverage of this uniform specialization, which does
not certify originality.

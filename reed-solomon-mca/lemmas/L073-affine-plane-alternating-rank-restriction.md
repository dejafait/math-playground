# L073 — Rank restrictions on the affine-plane alternating kernel

## Hypotheses

Let F be any extension of F_97 and let H be the order-sixteen subgroup
of F_97^*. Label the sixteen abstract points of L072 by an arbitrary
bijection lambda to H. Use exactly its sixteen blocks: the vertical
class and the classes of slopes 0, 1 and u in its auxiliary F_4 plane.
The auxiliary field is used only for incidence.

Put V=F^8, m_x=(x,x^2,...,x^8)^transpose, and
U_A=span{m_lambda(v): v in A} for each block A. Let

    K = {p in wedge^2 V : (wedge^2 pi_A)(p)=0 for every block A},

where pi_A: V -> V/U_A is the quotient map. This is precisely the
kernel of L026's stacked alternating equations, applied to these
sixteen supports. For p, let p#: V^* -> V be contraction with p, and
write S=im(p#). Rank means dim S, not the rank of the stacked matrix.

## Conclusion

Every nonzero p in K has rank two or four. If its rank is four,
then S contains at least one of the sixteen actual moment columns m_x.
All assertions hold uniformly over the labeling and over F, including
F_(97^20) and the algebraic closure of F_97.

This does not establish K=0 or rank 28 for the stacked matrix. In
particular it does not exclude rank-two tensors, which are exactly
the nonzero decomposable tensors relevant to an independent syndrome
pencil. It neither realizes nor excludes L010 equality for this family.
The new restrictions have not received a separate critical audit.

## Proof

L010 supplies independence of every eight distinct moment columns;
smaller collections are independent by extension to eight. Thus every
U_A has dimension four, and U_A direct-sum U_B=V whenever A and B are
disjoint. L026 supplies a basis of the annihilator of every U_A: the
coefficient rows of X^r product_(x in lambda(A))(X-x), 0<=r<4.
Their six wedges are a basis of the alternating forms on V/U_A.
Consequently their evaluations on p vanish exactly when
(wedge^2 pi_A)(p)=0. This explains the identification with the saved
linear test without a decomposability assumption or any division by
an error weight or pencil parameter.

We first spell out the linear-algebra implication used below, to avoid
assuming that p is nondegenerate on all of V. Alternating elimination
puts a nonzero tensor p in the form

    p = e_1 wedge f_1 + ... + e_r wedge f_r,

where the 2r displayed vectors are independent. Indeed, a nonzero
alternating entry gives an invertible two-by-two block; subtracting
its row/column components splits off that block, and iteration gives
this form, absorbing each nonzero coefficient in one vector. Its
span is S and dim S=2r. On S the tensor is nondegenerate and has an
inverse nondegenerate alternating form omega (either overall sign
convention gives the same orthogonal subspaces).

For any U subset V, set W=S intersect U. The induced map S/W -> V/U
is injective, so zero image of p in wedge^2(V/U) is equivalent to
zero image in wedge^2(S/W). Equivalently the alternating pairing p
vanishes on Ann(W) times Ann(W) in S^*. The isomorphism from S to
S^* given by omega identifies Ann(W) with W^perp. Thus W^perp is
isotropic, and

    W^perp subset (W^perp)^perp = W.

In particular dim W >= r. If dim W=r, then W=W^perp is Lagrangian.
These statements concern each block separately and do not assert that
its original moment columns all lie in S.

### Rank eight is impossible

Here S=V, r=4, so every U_A is Lagrangian. Fix a point v. In L072's
four selected classes, the four blocks through v have three other
points each, all distinct: different lines through v meet only there.
Their twelve moment columns are all omega-orthogonal to m_lambda(v).
Eight of those columns already span V. Nondegeneracy of omega would
then force m_lambda(v)=0, contrary to its first coordinate lambda(v)
being nonzero. This rules out rank eight.

### Rank six is impossible

Here dim S=6 and r=3. Since dim(S intersect U_A)>=3, the image of
every U_A in Q=V/S has dimension at most one. At most six moment
columns lie in S: seven such columns would contradict their linear
independence. At least ten projected columns are therefore nonzero.

The graph on the sixteen abstract points in which distinct points are
adjacent when they share a selected block is complete four-partite.
Its four parts are the lines of the omitted slope-(u+1) parallel class.
To check this directly, two points with different X coordinates have
a unique slope (Y-Y')/(X-X'); points with equal X share their vertical
line. The pair fails to share a selected line exactly when that unique
slope is u+1, equivalently when they lie on the same omitted line.
Each part has size four.

The induced graph on the at least ten nonzero projected columns is
connected: it meets at least two parts, different parts are adjacent,
and two vertices in one part have a common neighbor in another part.
Along an edge both nonzero projections belong to the image of one
U_A, a space of dimension at most one, so they are proportional.
Connectivity makes all nonzero projected columns proportional. But
the moment columns span V, hence their projections span Q, whose
dimension is two. This contradiction rules out rank six.

### A rank-four tensor cannot have all columns outside S

Suppose dim S=4 and no moment column lies in S. Put Q=V/S. For every
block A the intersection S intersect U_A has dimension at least two.
Choose any other block B in its parallel class. The spaces U_A and
U_B are complementary in V; hence their intersections with S are
disjoint, and their dimensions sum to at most four. Each is therefore
exactly two, and together they span S. It follows that their images
in Q are two-dimensional complementary subspaces. Denote these images
by W_A. Thus the four W_A in any one parallel class are pairwise
disjoint except for zero. Every projected moment column is nonzero
under the temporary assumption.

Take the vertical blocks R_0, R_1, R_2, R_3 with X=0,1,u,u+1.
Write Q=A direct-sum B with A=W_R0 and B=W_R1. The space W_R2 is
disjoint from both summands, so it is the graph of an invertible map
T:A -> B. Identify B with A using T; in these coordinates
W_R2={(a,a):a in A}.

For each of the four slope-zero blocks C, its nonzero projected
columns at R_0 and R_1 give vectors (a_C,0) and (0,b_C). They are
independent, and therefore span the two-dimensional W_C. The nonzero
projected column at C intersect R_2 lies on the diagonal. Expressing
that vector in this basis shows that a_C and b_C are proportional;
both coefficients are nonzero, since a nonzero diagonal vector has
both coordinates nonzero. Consequently, for a one-dimensional
subspace l_C of A,

    W_C = l_C direct-sum l_C  subset A direct-sum A.

The four l_C are distinct because distinct C in one parallel class
have W_C intersect W_C'=0.

Now choose any slope-one block D. It too has nonzero projected
columns in its intersections with R_0, R_1 and R_2. The identical
argument gives W_D=l_D direct-sum l_D for some line l_D in A.
Every C intersects D in one point of the affine plane, whose projected
column is nonzero by assumption. Thus W_C intersect W_D is nonzero
for every C. For spaces of the displayed form this requires l_C=l_D:
distinct one-dimensional subspaces of A have zero intersection in
both factors. This contradicts the four distinct l_C. At least one
moment column must therefore lie in S.

Alternating rank is even, nonzero, and at most eight. The three cases
above prove the claimed rank and containment restriction.

Finally, an actual L010 equality pencil would supply
p=sigma(a) wedge sigma(b) in K by L026's necessary equations. Its
syndrome directions cannot be dependent: full four-error syndromes
are nonzero by eight-column independence, whereas two disjoint
vertical supports have moment spans intersecting only in zero.
Thus such a pencil would yield a nonzero rank-two p. The present
restriction leaves that possibility intact. No rational descent of
weights, finite-chart normalization, locator condition, or same-support
failure has been inferred from the common kernel.

## Mathlib

Coverage of this exact family-specific restriction is not checked.
No Mathlib theorem is used, and unknown coverage is not absence.
The moment and exterior constructions are reused from L010 and L026;
L072 supplies the cited affine-plane incidence model. The coordinate
linear-algebra arguments above justify only the new specialization,
not a new general symplectic or affine-plane existence theorem.

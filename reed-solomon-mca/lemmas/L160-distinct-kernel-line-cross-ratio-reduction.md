# L160 — Distinct kernel lines: finite cross-ratios and one possible pencil

## Hypotheses

Let E be the algebraic closure of F_97. Use the original L109 maps on
W=E^S, with

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

For an original label j=(I_j,K_j) in binom(S,2) times binom(J,2), put
T_j=I_j union K_j, g_j(X)=product over y in J minus K_j of (X-y),
z_j=min(S minus I_j), and use the four actual quotient coordinates

    (Q_j w)_x=g_j(z_j)w_x-g_j(x)w_{z_j},
        x in (S minus I_j) minus {z_j}, in increasing order.

Thus V_j=ker Q_j=E^{I_j}+E(g_j(x))_{x in S}, by L109's kernel
identity. All matrices are defined over F_97. Fix four distinct original
labels a,b,c,d, with a<b and c<d in the original lexicographic order.
Assume T_a intersect T_b=T_c intersect T_d=empty and all six support
intersections have size at most one. No permutation quotient is taken.

Write A=V_a, B=V_b, C=V_c, D=V_d. Use C155a for the two designated
disjoint pairs: each space has dimension three and A intersect B=
C intersect D=0. Its audited L155/L153 finite-input qualifications are
inherited. Only these dimension and disjointness conclusions are used;
no exterior-kernel census is repeated. No coding, weight, chart, or
nonzero coefficient on g_j is assumed.

A plane means a two-dimensional E-subspace L with rank(Q_j|_L)=1
for all four selected rows. Its kernel-intersection lines are
ell_j=L intersect V_j. This result concerns exactly the branch in which
all four ell_j are pairwise distinct.

## Conclusion

Define the F_97-linear space and matrix pencil, extended to E, by

    U={(x,y) in A direct-sum B : x+y in C},  k=dim U,
    M(t): U -> E^4,  M(t)(x,y)=Q_d(x+t*y),
    K_t=ker M(t),  t in E minus {0,1}.

Then 2<=k<=3. The planes in the distinct-line branch are in bijection
with the disjoint union of P(K_t)(E) over t in E minus {0,1}, by

    [(x,y)] -> span(x,y).                                  (1)

The parameter t is uniquely determined by the ordered four kernel
lines: their normalized representatives are x,y,x+y,x+t*y.
Zero K_t contributes no point. The following sharper restrictions hold:

1. There are at most three t with K_t nonzero, and the sum of their
   dimensions is at most k<=3.
2. Every nonzero K_t has dimension one or two. At most one has dimension
   two. If all have dimension one, there are at most three planes.
3. If dim K_(t_0)=2, then t_0 belongs to F_97 minus {0,1}. This gives
   one projective-line family of distinct planes, defined over F_97,
   and at most one further plane. A basis of the two-dimensional
   F_97-kernel gives the complete family by (1).

Here a projective-line family means a family parametrized bijectively
by P^1(E), not necessarily a linear line in Plucker coordinates.
Consequently infinitude of this branch is equivalent to a
two-dimensional K_t at one of the 95 base-field parameters t!=0,1.
No such original quadruple/parameter is exhibited here, and absence of
such kernels for all original quadruples is not proved. This is a
partial structural reduction toward the approved finiteness question,
not a solution of it, a coding result, or an explicit counterfamily.
No independent critical audit or mathematical script is claimed.

## Proof

### Standard inputs and the necessary specialization

Use the arbitrary-field finite-dimensional linear algebra recorded in
the invocation-start EXPLORE assessment
`drafts/literature/2026-10-25-four-row-finiteness-review.md`:
A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*,
Gordon and Breach, 1997 paperback, ISBN 90-5699-049-7, Chapter 1
Theorem 3.12, pp. 20–21 and sections 6.2–6.9, pp. 44–46,
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
Only dimensions, kernels, direct sums, and linear-system splittings are
imported. The short eigenspace argument below is given explicitly;
no four-subspace classification, generic enumerative theorem, complex
normal form, or Jordan classification is assumed.

The actual-map specialization is necessary: L157 parametrizes fibers
without bounding their union, L158 treats only three named quadruples,
and L159 treats coincident lines. The present normalization retains all
zero/nonzero g_j coefficients and does not use L159 as a premise.
The source assessment does not supply a matching universal finiteness
theorem. This is REPRODUCTION of elementary linear-algebra mechanisms
with the stated local partial conclusion; no originality is asserted.

### Normalization, bijection, and all exact ranks

Fix a plane in this branch. Choose nonzero generators x_0 of ell_a
and y_0 of ell_b. Because A intersect B=0, these are independent and
span L. A generator of ell_c has form alpha*x_0+beta*y_0 with both
coefficients nonzero: otherwise ell_c equals ell_a or ell_b. Set
x=alpha*x_0 and y=beta*y_0. A generator of ell_d is now gamma*x+
delta*y, again with both coefficients nonzero. Dividing by gamma
makes it x+t*y with t=delta/gamma!=0. Distinctness from ell_c makes
t!=1. Hence (x,y) is a nonzero point of K_t.

The generators of ell_c differ by a common nonzero scalar, so this
construction determines [(x,y)] uniquely. Conversely suppose t!=0,1
and (x,y) is a nonzero vector of K_t. If x=0, then y belongs to C
and t*y belongs to D; since t!=0 and C intersect D=0, y=0, a
contradiction. If y=0, then x belongs to C intersect D, also impossible.
The nonzero x in A and y in B are independent. The vectors x+y in C
and x+t*y in D are nonzero and independent, their change-of-basis
determinant being t-1.

On L=span(x,y), Q_a kills x and does not kill y, since A intersect B=0.
Thus its rank is exactly one; the same reasoning gives rank one for
Q_b. The nonzero independent vectors x+y and x+t*y respectively lie
in C and D. Disjointness C intersect D=0 shows that Q_c kills the
first and not the second, while Q_d kills the second and not the
first. These two ranks are also exactly one. In the basis x,y the
four lines have coordinates [1:0], [0:1], [1:1], [1:t]; t!=0,1
makes all distinct. No weight, generator coefficient or chart gate
was used in these rank exclusions.

Scaling (x,y) by a common nonzero scalar preserves L. If another pair
at any parameter gives the same plane, exact rank one fixes its four
intersection lines. The uniquely normalized ell_c generator then fixes
the pair up to common scalar, and ell_d fixes t. This proves (1),
including injectivity across different parameters and exhaustion.

### At most three parameters, counting kernel dimensions

The sum map sigma:A direct-sum B -> W, (x,y)->x+y, is injective.
Its image A+B has dimension six. Thus sigma identifies U with
C intersect (A+B), and

    2=3+6-7 <= dim(C intersect (A+B))=k <=3.

At t=1 a vector in ker M(1) satisfies x+y in C intersect D=0,
so x=y=0. Hence M(1) is injective. All these data are defined over
F_97. Choose an F_97-linear left inverse R:F_97^4 -> U(F_97) of
M(1) by extending a basis of its image to a basis of F_97^4, and
extend R to E. Write F(x,y)=Q_d x, G(x,y)=Q_d y and T=R G.
Then, as endomorphisms of U,

    R M(t)=R(F+tG)=Id_U+(t-1)T.

For v in K_t with t!=1 this gives

    T v=(1/(1-t))*v.                                       (2)

Distinct parameters give distinct scalars 1/(1-t). Their corresponding
K_t therefore lie in distinct eigenspaces of the same k-dimensional
endomorphism. For completeness, these subspaces have direct sum: in a
finite relation sum_i v_i=0 with T v_i=lambda_i*v_i and distinct
lambda_i, apply product over j!=i of (T-lambda_j*Id). This kills all
terms but (product over j!=i of (lambda_i-lambda_j))*v_i, whose scalar
is nonzero. Hence every v_i=0. Taking bases in each K_t now gives
sum dim K_t<=k for every finite collection. In particular there can
be at most k<=3 nonzero kernels, and the same dimension sum holds for
the full set. No diagonalizability or missing eigenvector assumption
is involved; K_t may be a proper subspace of the eigenspace in (2).

### Excluding a three-dimensional kernel

Suppose some K_t has dimension three. Then k=3 and K_t=U. The maps
(x,y)->x and (x,y)->y are injective on K_t by the zero-component
argument above. Their three-dimensional images are all of A and B.
The maps (x,y)->x+y and (x,y)->x+t*y are likewise injective and have
images all of C and D.

This would force all four spaces to be pairwise disjoint. The designated
pairs already are. For A intersect C, write w=x+y using the surjection
K_t -> C. Membership in A forces y in A intersect B=0, and the
injective y-projection forces (x,y)=0. Thus w=0. For B intersect C
use the x-projection instead. For A intersect D write w=x+t*y;
t!=0 forces y=0, hence w=0. For B intersect D use x=0. This covers
all four cross intersections as well.

But the four I_j have eight coordinate incidences on the seven-element
S, so two of them share some coordinate r. Then e_r is a nonzero
vector in both corresponding V_j by L109's kernel formula. Those
spaces cannot be disjoint. This contradiction excludes dim K_t=3.
It follows that every nonzero kernel has dimension one or two. The
dimension-sum bound permits at most one two-dimensional kernel and,
if one occurs, at most one additional one-dimensional kernel. Via
(1), this proves the claimed finite/projective-line alternatives.

### The only possible infinite family is defined over F_97

Suppose dim K_(t_0)=2. Choose an F_97-basis of U(F_97). In this basis
M(t) is a four-by-k matrix whose entries are linear polynomials in t
with coefficients in F_97. Entrywise 97th powers send M(t_0) to
M(t_0^97); every minor is sent to its 97th power. Nonzero minors stay
nonzero, so the two matrices have the same rank. Thus

    dim K_(t_0^97)=dim K_(t_0)=2.

Also t_0^97!=0,1. Uniqueness of the two-dimensional-kernel parameter
forces t_0^97=t_0. The polynomial X^97-X already has the 97 distinct
elements of F_97 as roots and has degree 97, so it has no other roots
in E. Hence t_0 belongs to F_97 minus {0,1}.

The matrix M(t_0) is now over F_97. Row reduction over that field and
extension of scalars give a two-dimensional F_97-kernel with basis
v_0=(x_0,y_0), v_1=(x_1,y_1), whose E-span is K_(t_0). Its entire
projective-line family is

    L_[r:s]=span(r*x_0+s*x_1, r*y_0+s*y_1),
                 [r:s] in P^1(E).

The already proved bijection gives two-dimensional planes, four exact
ranks one, four distinct intersection lines, and pairwise distinct
planes for every projective parameter. There are no excluded [r:s]:
a nonzero projective combination is nonzero in K_(t_0), and the
zero-component/rank arguments apply to all of them. Since E is an
algebraic closure of a finite field, it is infinite: if it were finite,
product over u in E of (X-u)-1 would be a nonconstant polynomial
without a root in E, contrary to algebraic closedness. Thus this
projective line is infinite. This construction is conditional on a
specified original quadruple actually having the two-dimensional
kernel; none is supplied by this proof.

### What the reduction does not decide

This is more restrictive than an unbounded union of L157 fibers: only
three cross-ratios can occur, and any infinite branch is a single
base-field projective line rather than an extension-only exception.
Nevertheless the actual-map condition dim K_t=2 remains unexcluded
and unrealized. Finite cross-ratios do not imply finitely many planes.
Proving that all 95 potential base-field parameters avoid this rank
defect for every eligible quadruple, or specifying one that has it,
is still required to decide the approved target. No all-label sweep,
finite-field sampling, interpolation assumption, or coding recovery
is substituted for that missing assertion. The coincident branch is
separately treated by L159 and is not used here. Universal twelve-row
exclusion, extraction of a second disjoint pair, all weight/original
chart gates, arbitrary representation and challenge identification
remain independent unresolved steps.

## Mathlib

Full matching original-map cross-ratio reduction and field-of-definition
statement: not checked. Supporting kernel, direct-sum, eigenspace and
finite-field Frobenius results: not checked anew; no exact theorem name
is asserted. Unknown coverage is not absence. This is an informal
partial proof, with no Lean verification or scheme-theoretic claim.

# L161 — Coordinate obstructions to a two-dimensional pencil kernel

## Hypotheses

Use the original L109 maps over E, the algebraic closure of F_97, with

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

An original label j=(I_j,K_j) has two-element I_j subset S and
K_j subset J, support T_j=I_j union K_j, and

    g_j(X)=product over y in J minus K_j of (X-y),
    z_j=min(S minus I_j),
    (Q_j w)_r=g_j(z_j)w_r-g_j(r)w_(z_j),
                      r in (S minus I_j) minus {z_j},
    V_j=ker Q_j=E^{I_j}+E(g_j(r))_(r in S).

Fix four distinct original labels a,b,c,d with a<b and c<d in the
original lexicographic ordering, T_a intersect T_b and T_c intersect
T_d empty, and all six support intersections of size at most one.
Write A=V_a, B=V_b, C=V_c, D=V_d. Use L160's normalization

    U={(x,y) in A direct-sum B : x+y in C},
    K_t={(x,y) in U : x+t*y in D}, t in E minus {0,1}.

Its C155a/L155/L153 disjointness qualifications are inherited. Let m
be the number of S-coordinates belonging to two of the four I_j.
Every coordinate belongs to at most two, because the designated pairs
are disjoint. Thus 1<=m<=4. A plane in the conclusion is an
E-valued two-dimensional subspace L of E^S with all four ranks
rank(Q_j restricted to L)=1. No coding, weight, chart or descent
assumption is imposed.

## Conclusion

If dim_E K_t=2 for any t!=0,1, then m=1. Temporarily name the rows
so that the sole coordinate overlap is I_a intersect I_c. This is a
renaming of the equations only, not a quotient of the original labels.
Then I_b and I_d are disjoint pairs of singly covered coordinates, and
all four distinct monic quadratics

    d_j(X)=product over y in K_j of (X-y)

belong to the two-dimensional polynomial pencil

    span_E{product over r in I_b of (X-r),
           product over r in I_d of (X-r)}.                 (1)

For this fixed S,J there are exactly three possibilities for that
pencil if it contains four distinct J-pair quadratics. They are

    {f in E[X], deg f<=2 : f(0)=h*[X^2]f}, h in {8,12,22}.   (2)

The complete possible J-root pairs in these three pencils are:

| h | J-root pairs |
| --- | --- |
| 8 | {50,70}, {64,85}, {75,79}, {89,96} |
| 12 | {47,89}, {64,79}, {70,75}, {85,96} |
| 22 | {47,50}, {70,89}, {75,96}, {79,85} |

All four pairs in one row of this table must be used, in some order.
The two singleton-coordinate pairs I_b,I_d must be two distinct
members of the following corresponding triple:

    h=8:  {1,8}, {12,33}, {18,22};
    h=12: {1,12}, {18,33}, {22,27};
    h=22: {1,22}, {8,27}, {12,18}.

In particular, when m>=2, or when these necessary m=1 pencil
conditions fail, the entire four-row rank-one locus has at most five
planes: at most two in L159's coincident-line branch and at most
three in L160's distinct-line branch.

These are necessary conditions, not a realization of a two-dimensional
kernel or a proof that the surviving m=1 cases are finite. Universal
four-row finiteness remains undecided. This is a partial local
REPRODUCTION of elementary linear algebra and polynomial evaluation,
with an exact finite structural certificate. L159, L160 and the present
result have no separate critical audit; no complete challenge candidate
or result beyond the inspected general sources is claimed.

## Proof

### Standard inputs and why the local argument is needed

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-10-25-four-row-finiteness-review.md` and its
arbitrary-field linear algebra: A. I. Kostrikin and Yu. I. Manin,
*Linear Algebra and Geometry*, Gordon and Breach, 1997 paperback,
ISBN 90-5699-049-7, Chapter 1 Theorem 3.12, pp. 20–21 and sections
6.2–6.9, pp. 44–46,
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
Only kernels, dimensions, coefficient comparison and linear-system
consistency are imported. The source does not decide these actual-map
pencil defects. L160 leaves precisely the possible dimension-two
kernel; L158's three finite samples and ATTEMPTS/050 do not decide it.
The following specialization is needed to use the coordinate supports
and reciprocal quadratics, rather than to reprove a known general
finiteness theorem. Three-point evaluation on polynomials of degree at
most two is injective: its matrix has rows (1,r,r^2) and determinant
(s-r)(u-r)(u-s) at distinct r,s,u. All differences are nonzero in E.
This explicit observation supplies every polynomial root test below.

### Coefficient coordinates on a putative dimension-two kernel

Put P(X)=product over y in J of (X-y). At every r in S,
P(r) and all d_j(r) are nonzero, and g_j(r)=P(r)/d_j(r).
Apply the invertible diagonal coordinate change w_r -> w_r/P(r).
It preserves dimensions, ranks and all coordinate subspaces. In the
changed coordinates each V_j is

    E^{I_j}+E(1/d_j(r))_(r in S).

In the rest of this proof x,y denote these changed coordinates.
The coefficient of the reciprocal-quadratic vector is unique: its
values are nonzero outside I_j, so it is not in E^{I_j}.
For a vector (x,y) in K_t, denote the four coefficients of
x,y,x+y,x+t*y by alpha,beta,gamma,delta respectively. They are linear
forms on K_t. Outside the corresponding coordinate sets we have

    x_r=alpha/d_a(r),       y_r=beta/d_b(r),
    (x+y)_r=gamma/d_c(r),   (x+t*y)_r=delta/d_d(r).          (3)

All four K_j are distinct: equal K_j would give a support intersection
of size two. Thus the monic d_j are distinct; any two are linearly
independent, since comparison of leading coefficients in a scalar
proportionality would make them equal.

The projection K_t -> E^2, (x,y)->(alpha,beta), is injective. Indeed,
if alpha=beta=0 then x,y are supported in I_a,I_b. There is a
coordinate outside I_a union I_b union I_c (at most six coordinates),
where (3) forces gamma=0. A coordinate outside I_a union I_b union
I_d likewise forces delta=0, including possible cancellation in
x+t*y. If all four coefficients vanish, then at each coordinate at
least two of x_r,y_r,x_r+y_r,x_r+t*y_r vanish: at most two I_j
contain that coordinate. Any two of these four linear forms are
independent because t!=0,1. Hence x_r=y_r=0 everywhere. This proves
injectivity, retaining every vector on which some coefficient is zero.

Suppose henceforth dim K_t=2. Its projection is then an isomorphism,
so alpha,beta vary freely. Every equality of linear forms below is
therefore an identity in two independent variables.

There are 8 coordinate incidences among the I_j. If m coordinates
are covered twice, there are 8-2m covered once and m-1 uncovered,
by counting the seven coordinates. This proves 1<=m<=4.

### Excluding all cases with an uncovered coordinate

First assume m>=2 and choose an uncovered r_0. Put

    A_0=alpha/d_a(r_0), B_0=beta/d_b(r_0),
    e_j(r)=d_j(r_0)/d_j(r).

These are all nonzero evaluation factors, and A_0,B_0 are independent
coordinates. The equations at r_0 give

    gamma/d_c(r_0)=A_0+B_0,
    delta/d_d(r_0)=A_0+t*B_0.                              (4)

At any other uncovered r, compare the coefficients in

    A_0*e_a+B_0*e_b=(A_0+B_0)*e_c,
    A_0*e_a+t*B_0*e_b=(A_0+t*B_0)*e_d.

They imply e_a=e_b=e_c=e_d. At a coordinate covered only by row a,
the identity x+t*y=(x+y)+(t-1)y gives

    (A_0+t*B_0)*e_d=(A_0+B_0)*e_c+(t-1)*B_0*e_b,

so e_b=e_c=e_d. At a coordinate covered only by row b, use

    (A_0+t*B_0)*e_d=t*(A_0+B_0)*e_c+(1-t)*A_0*e_a,

to get e_a=e_c=e_d. For a coordinate covered only by c, use
A_0*e_a+t*B_0*e_b=(A_0+t*B_0)*e_d to obtain e_a=e_b=e_d.
For a coordinate covered only by d, use
A_0*e_a+B_0*e_b=(A_0+B_0)*e_c to obtain e_a=e_b=e_c.
These comparisons use t!=0,1 explicitly and do not divide by A_0
or B_0. Equivalently the normalized polynomials
q_j=d_j/d_j(r_0) have equal values at uncovered r, and the other
three q_j have equal values at a singleton coordinate of row j.

If m=4, there are three uncovered coordinates. All four q_j agree
at these three points, so they are identical polynomials. Monicity
then forces all d_j equal, a contradiction.

If m=3, there are two uncovered coordinates r_0,r_1 and two
singleton coordinates. The span F of the four d_j lies in the
hyperplane

    f(r_1)=h_1*f(r_0),

where h_1 is their common normalized value at r_1. Its dimension
is at most two and at least two, by pairwise independence. Choose
any singleton r. The other three d_j span F, since any two are
independent, and they also obey f(r)=h*f(r_0). These two evaluation
constraints are independent: evaluations at the three distinct
coordinates r_0,r_1,r are independent by the displayed Vandermonde
calculation. Their common kernel in the three-dimensional polynomial
space has dimension one, contradicting dim F=2.

If m=2, there is just r_0 uncovered and four singleton coordinates.
If some row has two singleton coordinates r,s, the other three q_j
agree at r_0,r,s; they are identical, contradicting distinctness.
Otherwise every row has exactly one singleton. Each triple of the
d_j lies in a two-dimensional evaluation hyperplane, using the
singleton of the missing row, and so is linearly dependent. Choose
any two independent d_j. Dependence of each triple containing them
puts both remaining d_j in their span; thus the span F of all four
has dimension two. At each singleton coordinate the other three
span F, so F obeys that coordinate's normalized evaluation constraint.
Two distinct singleton coordinates, together with r_0, give two
independent constraints as above, again forcing dim F<=1. This
excludes m=2 and completes the uncovered-coordinate cases.

### The sole-overlap case forces a common polynomial pencil

Let m=1. Its sole overlap is across the designated pairs. For the
following calculation temporarily name its rows a,c, so that b,d
have two singleton coordinates each. Swapping a,b changes L160's
normalization by (x,y,t)->(y,x,1/t); swapping c,d changes it by
(x,y,t)->(x,t*y,1/t). These invertible transformations preserve
kernel dimension and t!=0,1. They justify this temporary naming
without assuming any symmetry among the original numerical maps.

Write, using the independent alpha,beta,

    gamma=u*alpha+v*beta, delta=w*alpha+z*beta.              (5)

At each of the two singleton coordinates r in I_d, equations (3)
give

    u=d_c(r)/d_a(r), v=d_c(r)/d_b(r).                     (6)

Thus u,v are nonzero, and the three d_a,d_b,d_c have proportional
evaluations on the two points of I_d. They lie in a common
2D evaluation hyperplane. Their span is exactly two-dimensional.

At each of the two singleton coordinates r in I_b, use
x+t*y=t*(x+y)+(1-t)x. Comparing beta and alpha coefficients gives

    z/d_d(r)=t*v/d_c(r),
    w/d_d(r)=t*u/d_c(r)+(1-t)/d_a(r).                     (7)

In particular z!=0. Set h=z/(t*v)!=0. Then on both points of I_b,

    d_d(r)/d_c(r)=h,
    d_c(r)/d_a(r)=(w/h-t*u)/(1-t).

The second displayed constant is nonzero, since its left side is.
Consequently d_a,d_c,d_d have proportional evaluations on I_b,
and span another 2D evaluation hyperplane. The two spans share the
independent d_a,d_c, so they are the same two-dimensional space F.
It follows that all four d_j lie in F, and evaluations restricted to
F are proportional on each of I_b and I_d.

For a pair {r,s}=I_b, choose a nonzero f in F with f(r)=0; the
kernel of this evaluation is nonzero because dim F=2. Proportional
evaluations force f(s)=0. Such a degree-at-most-two nonzero polynomial
is a scalar multiple of (X-r)(X-s), by three-point injectivity or
polynomial division. Thus the monic root polynomial of I_b belongs
to F. The same holds for I_d. They are distinct monic quadratics and
hence independent, giving precisely (1). They have no common root,
since I_b and I_d are disjoint. Therefore F has no common root.
If two distinct d_j in F shared a root, their independence would
make it a root of every f in F, a contradiction. Thus all four K_j
are disjoint as well. The two coordinate pairs determine F over
F_97, so no extension-field pencil is missed by the following check.

### Complete small structural certificate and its limitations

The script `scripts/seven-coordinate/four_row_quadratic_pencils.py`
checks all 105 unordered disjoint S-pair choices: a four-set has
three partitions into two pairs, giving 3*binom(7,4)=105. For a pair
{r,s}, its monic root polynomial has coefficient vector

    p_(r,s)=(r*s, -(r+s), 1) in F_97^3,

in constant/linear/quadratic order. For generators p_A,p_B their
cross product n is nonzero by independence. A J-pair polynomial p_K
belongs to their pencil if and only if n dot p_K=0. All 36 J pairs
are tested for every choice. This is an exact necessary polynomial
pencil test, not an original quadruple census, a fourth sampled
quadruple, or an exterior-rank-only inference.

The full certificate is
`scripts/seven-coordinate/four-row-quadratic-pencils.json`.
Reproduce it from the notebook with

    python3 scripts/seven-coordinate/four_row_quadratic_pencils.py

It records all 105 generator pairs and their normals, all 3780 J-pair
polynomials and determinant residues, complete membership lists,
counts, and failures. Coverage is separately checked by the four-set/
three-partition construction. Membership is independently checked by
writing every monic polynomial in span(p_A,p_B) as
p_A+lambda*(p_B-p_A), solving lambda from a nonzero coefficient of
the difference, and checking every coefficient. All 3780 tests agree;
coverage is 105/105; failures is empty.

The member-count distribution is 70 pencils with zero J members,
22 with one, none with two, four with three, and nine with four.
The required exceptional count is four, and the actual maximum is
four: this exclusion threshold FAILS. The nine surviving choices
group into exactly three distinct pencils, whose normalized normals
are (1,0,89), (1,0,85), (1,0,75). They give (2), since
89=-8, 85=-12, 75=-22 in F_97. Their complete S-pair choices and
J-member lists are the ones stated in the conclusion, and are also
recorded in `surviving_pencil_groups` in the certificate. Those
complete selected values, rather than a bounded preview, were inspected.
The independent full membership checks establish the exhaustive
comparison; a displayed maximum alone would not suffice.

In particular the earlier hoped-for contradiction from two distinct
singleton pairs was invalid: proportional evaluations within each
pair need not be proportional BETWEEN the two pairs. The working
file preserves that rejected inference. The surviving pencils are
concrete evidence against that shortcut, not infinite families.
They still require the remaining singleton/overlap equations and
L160's exact-rank parametrization to decide whether dimension two
actually occurs. No original quadruple is asserted to realize it.

Finally, if these necessary conditions fail then every K_t has
dimension at most one: L160 already excludes dimension three and
bounds the sum of kernel dimensions by three. Its exact bijection
gives at most three planes in the distinct-line branch. L159 gives
at most two in the coincident-line branch. Their union is the whole
rank-one locus, establishing the qualified bound five. This imports
their full stated hypotheses, including L160's inherited disjointness
input, and is not a separate audit of them.

Uniform twelve-row exclusion, extraction of a second disjoint pair,
arbitrary weights and original chart, coding realization over
F_(97^20), representation, challenge equivalence and sharp radius
remain independent unresolved gaps. An E-valued plane need not pass
any coding gate. No improvement to the 11/q–16/q interval is claimed.

## Mathlib

Full matching coordinate-obstruction and finite-pencil classification:
not checked. Supporting linear algebra, polynomial evaluation and
finite-field arithmetic: not checked anew. No exact Mathlib names,
Lean verification or scheme-theoretic assertion is claimed. Unknown
coverage is not evidence of absence.

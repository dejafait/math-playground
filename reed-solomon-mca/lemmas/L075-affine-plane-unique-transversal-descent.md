# L075 — Unique affine-plane transversal and prime-field realization test

## Hypotheses

Let k=F_97, let H be its order-sixteen multiplicative subgroup, and
fix any bijection from the points of L072 to H. Use exactly its sixteen
blocks A. Put V_k=k^8, m_x=(x,x^2,...,x^8)^transpose and
U_A=span_k{m_x:x in A}. Over an extension F of k, extend these spaces
by scalars. Define

    K_F = {p in wedge^2 F^8 : (wedge^2 pi_A)(p)=0 for every A},

where pi_A is the quotient by U_A over F. Equivalently use L026's
96-by-28 matrix M: for each block take the six pairwise wedges of
the four coefficient rows of X^r product_(x in A)(X-x), 0<=r<4,
with coefficients in degrees 0,...,7. All entries of M lie in k.
Use L073 and L074's rank restrictions, which await separate critical
audit. The auxiliary F_4 plane specifies incidence only.

## Conclusion

For every labeling and extension, dim_F K_F<=1. Thus M has rank 27
or 28. If the rank is 27, there is exactly one two-dimensional
subspace S_F meeting every U_A nontrivially. It is the scalar extension
of a plane S_k in k^8, and each S_k intersect U_A is a line.

For each block in the rank-27 case choose any nonzero
t_A in S_k intersect U_A and write its unique expansion

    t_A = sum_(x in A) w_(A,x) m_x,       w_(A,x) in k.          (1)

The following test is exact for this labeled family: it admits an
L010 equality pencil over F_(97^20) if and only if M has rank 27 and
all 64 coefficients in (1) are nonzero. Their zero/nonzero status is
independent of the chosen nonzero t_A. If this test passes, an equality
pencil can already be constructed with input words and sixteen distinct
finite parameters over k; the same pencil remains an equality pencil
over F_(97^20). This is a conditional construction, not an exhibited
passing labeling.

No labeling has been proved to pass or to fail this test here. The
uniform exclusion, actual realization, global fifteen bound and
challenge qualifications remain unresolved. This result and its use of
L073/L074 require a later separate critical audit.

## Proof

### The kernel has dimension at most one

L010 gives independence of any eight distinct moment columns. Each U_A
has dimension four; two disjoint blocks have complementary moment
spans. L026 identifies M's kernel with K_F, including over extensions.
L073 and L074 say every nonzero element of K_F has rank two, hence
is a wedge of two independent vectors.

For a nonzero decomposable p=a wedge b, write S_p=span{a,b}.
The image of p under wedge^2 pi_A vanishes exactly when pi_A(a)
and pi_A(b) are dependent, equivalently S_p intersect U_A is nonzero.
This intersection has dimension exactly one: dimension two would put
S_p inside U_A, whereas a disjoint block B also requires a nonzero
intersection with U_B, contrary to U_A intersect U_B=0.

Suppose p,q are independent elements of K_F. Their planes cannot
coincide, since the exterior square of a plane is one-dimensional.
If the planes had zero intersection, choosing bases a,b and c,d
would express p+q=a wedge b+c wedge d on four independent vectors,
with a nonsingular alternating block on each pair. Its rank would
be four, contradicting L074. Thus their intersection is a line l,
and T=S_p+S_q has dimension three.

The four vertical blocks of L072 have pairwise complementary U_A.
At most one of these spaces contains l. For any other such block A,
the lines S_p intersect U_A and S_q intersect U_A are distinct:
if equal their common line must be l. Their span is therefore a
two-dimensional subspace of T intersect U_A. Choose two vertical
blocks A,B not containing l, which is possible since at least three
do not. The corresponding two-spaces in T intersect nontrivially
by dimension, but are contained in U_A and U_B, whose intersection
is zero. This contradiction proves dim K_F<=1.

### Descent and uniqueness of the plane

Row reduction of M uses only k and gives the same pivots over every
extension. Thus K_F=K_k tensor_k F and rank M is 27 or 28. In the
rank-27 case choose a nonzero p_0 in K_k. Its contraction matrix has
rank two over k by L073/L074. Let S_k be its image; over F the image
is S_k tensor_k F. The preceding argument gives a one-dimensional
intersection with each U_A over k. Solving these rational linear
systems gives t_A and the coefficients in (1) in k.

Any plane meeting every U_A produces a nonzero decomposable element
of K_F by the quotient criterion. That element is a scalar multiple
of p_0 and hence has the same image. This proves uniqueness, including
for planes initially defined over F_(97^20). This assertion descends
the plane, not an already specified affine chart or input words.

### Necessity of the full-coefficient test

An actual L010 equality pencil supplies full errors e_A at its sixteen
distinct finite parameters. Put u=sigma(a), v=sigma(b). These directions
are independent: all error syndromes are nonzero, while two disjoint
vertical supports have moment spans intersecting only in zero, so no
one-dimensional syndrome space can contain both. Hence u wedge v is
a nonzero member of K_F. The rank is 27 and span{u,v}=S_F. Each actual
syndrome is a nonzero scalar multiple of t_A. Independence of the four
columns then makes every coefficient in (1) nonzero, since e_A is full.

### Sufficiency, with all equality gates

Assume rank 27 and all coefficients in (1) nonzero. The sixteen
intersection lines l_A=k t_A are pairwise distinct. Indeed L072 gives
|A intersect B|<=1. Independence of the at most eight columns in
A union B gives

    U_A intersect U_B = span{m_x:x in A intersect B}.

This follows by subtracting the two column expansions: coefficients
outside the intersection must vanish. A common nonzero t_A,t_B line
would consequently be a single moment-column line, or zero if the
blocks are disjoint. Both alternatives contradict full coefficients
on four columns.

The projective line of S_k has 98 points: 97 lines represented in a
fixed basis by (1,t), t in k, and the line represented by (0,1).
Choose a line l_infinity outside the sixteen l_A. Choose a nonzero
k-linear functional h:S_k -> k with kernel l_infinity, a vector u
with h(u)=1, and a nonzero v spanning ker h. For each A the vector

    z_A=t_A/h(t_A)=u+gamma_A v

has gamma_A in k. The gamma_A are distinct, since the l_A are distinct.
Dividing (1) by h(t_A) gives an error e_A supported exactly on A with
sigma(e_A)=z_A. The moment map k^H -> k^8 is onto by L010, so choose
input words a,b over k with sigma(a)=u, sigma(b)=v. This verifies all
eight moments in the original newly chosen finite chart. It does not
normalize a preexisting chart.

For this pencil L010's pointwise full-error formulas give

    D(gamma_A)=det(V_A)^2 product_(x in A)(e_A(x)x) != 0,
    L(gamma_A,X)=D(gamma_A) product_(x in A)(X-x),

where V_A is the four-by-four Vandermonde matrix. In particular D is
a nonzero polynomial. For each x in H choose a block A not containing
x; twelve such blocks exist by L072. The second formula then gives
ell_x(gamma_A)!=0, so every coordinate locator is a nonzero polynomial.
These are exactly L010's nondegeneracy hypotheses, without an assumed
splitting condition.

The kernel identity in L010 makes a+gamma_A b-e_A a codeword.
L010's same-support argument, now applicable because D and all ell_x
are nonzero polynomials, makes gamma_A bad on H minus A. Thus there
are at least sixteen distinct bad parameters. L010 bounds the complete
bad set by sixteen and gives equality, degree-four split locators,
nonzero D at every locator root, and precisely four roots through
each coordinate. Alternatively those four distinct roots exhaust each
nonzero ell_x's degree bound directly, using L072's degree-four balance.
No projected-only recovery or untested lower-weight event is counted.

All coefficients are in k. On extending to F_(97^20), the displayed
sixteen finite events and all nonzero polynomials persist; L010 still
bounds the entire bad set by sixteen. Thus no additional extension
parameters change the equality claim. Conversely the necessity and
descent argument applies to arbitrary extension-field weights and
original finite parameters. This completes the exact conditional test.

The new content is the uniform corank-at-most-one restriction and the
resulting rational full-weight test. L010's moment, determinant and
same-support results and L026's matrix construction are reused, not
reproved. No theorem about a generic labeling is applied to fixed H,
and no finite sampling establishes a uniform conclusion.

## Mathlib

Coverage of this exact family-specific uniqueness and descent statement
is not checked. No Mathlib theorem is used; unknown coverage is not
absence. The ready EXPLORE assessment found no matching theorem, which
does not certify novelty. The matrix and locator inputs are the local
results cited above; the affine-plane specialization and primary design
citation are in L072. No new general design or decoding theorem is
claimed.

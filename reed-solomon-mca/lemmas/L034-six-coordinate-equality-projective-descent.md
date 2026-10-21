# L034 — Union-six equality forces projective descent

## Hypotheses

Use all hypotheses and notation of L033: F=F_(97^20), its prime subfield
F_0=F_97, H of order sixteen in F_0^*, k=8, the pinned radius cell,
nonzero polynomial D and every nonzero coordinate locator. In particular
U=Z_1 disjoint union Z_2 disjoint union Z_3, each Z_i has size two, and
the affine lift is
\[
 f_x(T)=c_x(T-\gamma_i)\quad(x\in Z_i),\qquad c_x\in F^*,
\]
with three distinct finite selected parameters and actual full-weight
four-errors. Write f(T)|_U=u+Tv, J=H minus U, and
ell=P(span_F(u,v)). Its finite chart excludes precisely [v].

Assume additionally N_3=0 and N_ext=13. These are the possible failure
case for L033's twelve-additional-incidence target, since L010 and L033
give N_ext<=13 when N_3=0. Every use of equality below requires this
additional hypothesis.

## Conclusion

Exactly twelve of the additional errors meet U in one coordinate, with
exactly two at each x in U. Exactly one additional error is disjoint
from U. For every pair Z_i={x,y}, the slope ratio c_x/c_y belongs to
F_0^*.

Every one-coordinate-overlap point of ell has a nonzero representative
in F_0^U. Consequently there is a two-dimensional F_0-subspace V_0 of
F_0^U such that span_F(u,v)=span_F(V_0): the projective pencil descends
to F_0. All sixteen witnessed error directions, including the three
selected points and the additional disjoint-support point, are rational
points of this descended line. For each of those directions, choose a
rational lift vector w in F_0^U and extend it by zero outside U. Its
unique weight-four error representative with syndrome sigma(w) then
has all weights in F_0.

This is a necessary condition for thirteen additional incidences, not
a twelve-incidence bound or a refutation. The original affine u,v,
parameters gamma, and excluded point [v] need not be rational. No
affine reparameterization or enumeration bound is asserted. The result
reduces the hypothetical equality case to rational projective geometry,
while retaining the original finite-chart condition.

## Proof

### Equality forces the distribution of overlaps

L033 gives |B|=3+N_ext+N_3=16. L010 therefore supplies sixteen distinct
weight-four errors, with each coordinate appearing in exactly four of
their supports. Each x in U is absent from one selected error and
present in the other two. Thus exactly two additional errors contain x.
Summing over the six coordinates in U gives twelve incidences between
U and the additional errors. By L033 each additional error meets U in
at most one coordinate. Exactly twelve of the thirteen additional
errors therefore have a one-coordinate overlap, two for every x, and
the remaining error is disjoint from U. This counts actual errors and
distinct finite parameters, not indexed projective lines alone.

### Paired slope ratios and rational overlap points

Consider an additional error with support {x} union K, where x is in U
and K is a three-subset of J. At its parameter tau, L033 gives
\[
 f(\tau)|_U=\lambda(g_K(z))_{z\in U}+\mu\delta_x,
 \qquad \lambda,\mu\in F^*,
 \qquad g_K(X)=\prod_{y\in J\setminus K}(X-y).          \tag{1}
\]
All g_K(z) for z in U belong to F_0^*, since all labels are in F_0
and none is a root of g_K.

Fix a pair Z_i={a,b} not containing x. Equation (1) at a and b gives
\[
 \frac{c_a}{c_b}
  =\frac{c_a(\tau-\gamma_i)}{c_b(\tau-\gamma_i)}
  =\frac{g_K(a)}{g_K(b)}\in F_0^*.                    \tag{2}
\]
The canceled factor is nonzero because tau is outside the selected
three parameters. For each i the preceding count supplies an overlap
at a coordinate outside Z_i; applying (2) to that error proves the
rationality of the ratio in every pair. We have not assumed that
lambda, mu, tau, or the individual slopes lie in F_0.

Return to any overlap (1), now write Z_i={x,y}, and put
r=c_x/c_y in F_0^*. Since f_x(T)=r f_y(T) identically, (1) implies
\[
 \lambda g_K(x)+\mu=r\lambda g_K(y),\qquad
 \frac{\mu}{\lambda}=r g_K(y)-g_K(x)\in F_0.          \tag{3}
\]
Its value is nonzero by the actual full-weight condition mu!=0. Hence
\[
 \lambda^{-1}f(\tau)|_U
  =(g_K(z))_{z\in U}
    +(r g_K(y)-g_K(x))\delta_x                       \tag{4}
\]
is a nonzero vector in F_0^U. It is nonzero, for example, at every
coordinate other than x. Thus every overlap point is rational.
This uses the shared-root pair constraints as well as actual full
weights; rational defining lines alone would not suffice.

Choose two of the twelve overlap errors. Their parameters are distinct
by L033's exact accounting, and L033's finite-chart injection says
their projective points are distinct. Take their rational representatives
w_1,w_2 from (4). They are linearly independent over F: dependence would
make their projective points identical. They span the two-dimensional
space span_F(u,v). Their F_0-span V_0 has dimension two and its
F-span is exactly that space. This proves projective descent by explicit
rational vectors, with no assumption about rationality of the chart.

### The other witnessed directions and normalized weights

Each selected point [f(gamma_i)|_U] is the unique zero on ell of a
coordinate x in Z_i. Indeed f_x(T)=c_x(T-gamma_i) has that single finite
zero, and v_x=c_x!=0, so [v] is not another zero. Restricting this
coordinate functional to V_0 gives a nonzero linear functional with
coefficients in F_0. Its one-dimensional kernel over F_0 extends to
the corresponding kernel over F: in a rational basis this is a single
nonzero row of two coefficients. Thus each selected point is rational.

Let K_0 in J be the support of the one disjoint additional error.
L033 puts its point in ell intersect P(W_(K_0)^(0)). Both vector
spaces are defined over F_0; the second is generated by the two rational
vectors (g_(K_0)(z)) and (z g_(K_0)(z)). L033 proves the projective lines
are distinct, so this nonempty intersection has vector dimension one.
It is a rational intersection: express equality of the two rational
bases as a homogeneous linear system over F_0. Gaussian elimination
uses only F_0 coefficients, has the same pivots over F, and gives a
rational basis whose F-span is its entire solution space. The basis
maps to the common vector space, and the map is injective because
each pair of basis columns is independent. A one-dimensional common
space therefore has a nonzero rational representative. This argument
also verifies the required field-extension step rather than assuming it.

Finally choose any of the sixteen rational representatives w just
obtained and let A be the support of its actual weight-four error.
The original lift at that point is a nonzero scalar multiple of w;
scale its error by the inverse scalar. This gives an F-valued error
e supported on A with sigma(e)=sigma(w), all its four weights nonzero.
The first four shifted moments determine those four weights by the
matrix (x^j)_(1<=j<=4,x in A). This is a Vandermonde matrix times a
nonzero diagonal matrix, hence invertible over F_0. Its right side
sigma_j(w) lies in F_0, so its unique solution lies in F_0^A.
It is the already constructed e, so it also satisfies the other four
moments and retains full weight. Uniqueness and same-support badness
for the original finite parameters remain those proved in L010/L033;
no different affine chart or different input pair has been substituted.

The argument establishes an arithmetic restriction on every possible
counterexample to the twelve bound. It does not exclude rational
projective configurations satisfying that restriction. In particular
it does not import L015's five-coordinate enumeration, assert that the
original point [v] descends, or count a point at original infinity as
finite. The global interval remains 11/q–16/q. This proof awaits a
separate critical audit.

The standard coding inputs are already imported and specialized in
L033 (Marquez-Corbella–Pellikaan, section 5, Lemma 5.3 and its following
shortening formula, and Hall, Theorem 5.1.1). No reproof or new use of
their source hypotheses is needed here: the exact L033 overlap formula
and L010 equality criterion are applied with their hypotheses unchanged.
The paired-ratio specialization and its elementary linear algebra are
written out because the reviewed sources do not supply this conditional
descent assertion. Classification is POTENTIALLY_NEW under the saved
EXPLORE assessment, meaning no coverage was established in that bounded
comparison, not a certified originality claim.

## Mathlib

Coverage of the full conditional projective descent statement and its
paired-ratio specialization is **not checked**. Coverage of supporting
finite-field, scalar-extension and Vandermonde results is also not
checked here. No absence or Lean-verification claim is made. The exact
informal field-extension arguments needed are given above; the pinned
ArkLib event is separate from Mathlib and the unread ABF26 definition.

# L019 — Positive-degree vanishing on the cubic correspondence support

## Hypotheses

Let S, F, O, C, nu:W -> C, g_0, g_1, and the tangent spaces be as in
L008, at a very general parameter of the cubic family. In particular
rho(S)=4, the finite singular fibres are irreducible nodal fibres, and
the fibre at infinity is of type III. Write its two reduced components
as E and R=F-E, with E the exceptional component disjoint from O.

Fix any ample line bundle L on S, without replacing it by a power, and
put X=S x S, H=p_1^*L tensor p_2^*L, and
M=g_0^*L tensor g_1^*L. Use additive notation for divisor classes in
intersection calculations. All cohomology is coherent cohomology over C.

## Conclusion

For every integer n>0,

\[
H^1(C,O_C(nH))=0.                                      \tag{1}
\]

More precisely, L-F is nef and big, H^1(W,M^n)=0, and sections of M^n
can prescribe arbitrary values simultaneously at all six preimages of
the three double points of C. The last assertion includes the points
where the two components of a type-III fibre are tangent. No equality
between g_0^*L and g_1^*L is required.

Consequently every admissible smooth complete-intersection union in
L018 with m>n>0 has no embedded first-order lift along a direction in
V_RM outside V_D. This exclusion now holds in every positive containing
degree, not just in a Serre-vanishing range. Equality of its lifting
locus with V_D still requires L018's separate H^1(X,I_C(nH))=0
hypothesis. No existence of admissible sections in every degree is
asserted. The known 21-dimensional cycle span is unchanged, and the
universal rational Hodge conjecture remains unresolved.

## Proof

**A rational divisor basis visible in the equation.** Use the Weierstrass
equation in the [family input](../foundations/05-cubic-rm-family.md).
Set x_0=-c_1/b_1 and choose a square root y_0 of
x_0^3+b_0 x_0+c_0. At very general parameters y_0 is nonzero. The
constant coordinates (x,y)=(x_0,y_0) define a section P. It is disjoint
from O on the finite chart. At infinity use L008's coordinates
X=q^4 x, Y=q^6 y and the blowup of the A_1 point. In its q-chart,
the section has

\[
X/q=x_0q^3,\qquad Y/q=y_0q^5.
\]

The strict transform solves for X/q in terms of (q,Y/q), since its
linear coefficient is b_1 nonzero. The exceptional component is q=0
in this chart, so P meets E transversely at [0:0:1]. This point is
different from the tangency point [1:0:0] of E and R. The zero section
meets R, hence P and O are also disjoint at infinity.

The sections O,P and the component E are smooth rational curves on a
K3, so adjunction gives their square -2. The intersection matrix in the order
(F,O,E,P) is therefore

\[
\begin{pmatrix}
0&1&0&1\\
1&-2&0&0\\
0&0&-2&1\\
1&0&1&-2
\end{pmatrix},\qquad \det=-7.                         \tag{2}
\]

These classes are independent and span NS(S)_Q because rho(S)=4.
Only this rational span is needed. Define

\[
V=P-O-2F+\tfrac12 E.
\]

Then V is orthogonal to F,O,E and V^2=-7/2.

**Enough sections to bound every ample class.** For each integer j,
let Q_j be the section jP for the elliptic-curve group law, with
Q_0=O. A rational section extends across the base by properness.
On the generic elliptic fibre the divisor
Q_j-O-j(P-O) is principal. Its closure on S is thus linearly equivalent
to a vertical divisor. All vertical divisor classes are integral
combinations of F and E: all other fibres are irreducible, and the
remaining component at infinity is F-E. It follows that

\[
Q_j=jP+(1-j)O+a_jF+b_jE
\]

for integers a_j,b_j. A section meets the smooth locus of a fibre,
since its composition with the fibration is the identity. Hence
epsilon_j=Q_j.E is either 0 or 1. Intersecting the displayed expression
with E gives b_j=(j-epsilon_j)/2, so epsilon_j is j modulo 2. Finally
Q_j^2=-2 determines its F coefficient. Rewriting in the orthogonal
coordinates gives

\[
Q_j=O+\frac{7j^2+\epsilon_j}{4}F
       -\frac{\epsilon_j}{2}E+jV.                    \tag{3}
\]

This derivation uses neither a Mordell--Weil generator assertion nor
an integral basis assertion for (2).

Let D=dO+bF+zE+kV be any rational divisor class with d=D.F>0 and
D.E,D.R nonnegative. Then

\[
D.E=-2z,\quad D.R=d+2z,\quad t=-z/d\in[0,1/2].
\]

Choose an integer j nearest k/d, so delta=j-k/d has absolute value
at most 1/2, and put s=D.Q_j. Using (3) and the orthogonality above,

\[
\begin{aligned}
s&=b-2d+\frac{d(7j^2+\epsilon_j)}4
               +z\epsilon_j-\frac72kj,\\
D^2&=2ds+d^2\left(2-\frac72\delta^2-2t^2
                         -\epsilon_j(1/2-2t)\right)\\
   &\ge 2ds+\frac58d^2.                              \tag{4}
\end{aligned}
\]

For epsilon_j=0, the expression in parentheses is at least
2-7/8-1/2=5/8. For epsilon_j=1 it is at least
5/8+2t-2t^2, again at least 5/8. Thus (4) holds for both parities.

Suppose an irreducible curve Gamma has Gamma^2=-2 and Gamma.F>=2.
It is distinct from E, R, and every section Q_j, so its intersections
with them are nonnegative. Applying (4) to Gamma gives a positive
square, a contradiction. Every irreducible (-2)-curve is therefore
either a fibre component or a section: fibre degree zero means vertical,
and fibre degree one makes this smooth rational curve a section.
The only negative vertical components are E and R.

For the fixed ample L, d=L.F>0, its intersections with E and R are
positive, and s=L.Q_j is an integer at least one. Consequently

\[
L^2\ge 2d+\frac58d^2>2d.                              \tag{5}
\]

The class A=L-F has A^2=L^2-2d>0 and A.L=L^2-d>0.
It is nonnegative on every section, because L meets that section in
a positive integer and F meets it once. It is positive on E and R.
For every other irreducible curve Gamma, adjunction gives Gamma^2>=0.
Since Gamma.L>0, Hodge index places Gamma in the closure of the same
positive cone as A; thus A.Gamma>0. This last assertion also follows
directly from the signature (1,rho-1) and the Cauchy--Schwarz inequality
on L's negative-definite orthogonal complement. We have checked
nonnegative intersection with every irreducible curve. Therefore A
is nef; its positive square makes it big. For all n>=1 the class

\[
A_n=nL-F=(L-F)+(n-1)L
\]

is likewise nef and big. In particular no extra positivity hypothesis
on the original L has been imposed.

**The canonical correction on the normalization.** Let T_0 and
T_infinity be the two fibres of W above v=0 and v=infinity, and put
T=T_0+T_infinity. By L008,

\[
T\sim K_W\sim 2F_W=g_0^*F=g_1^*F.
\]

Both g_i are finite flat double covers. The line bundle

\[
B_n=g_0^*A_n\mathbin{\otimes}g_1^*A_n
     =M^n\mathbin{\otimes}O_W(-2K_W)                 \tag{6}
\]

is nef and big. Indeed a finite pullback of a nef class is nef and
has positive square here, and the sum of two such classes remains
nef with positive square. The canonical bundle K_W=2F_W is nef as well.

Import Kawamata--Viehweg vanishing in the smooth projective nef-and-big
form stated in Fujino, *A transcendental approach to Kollar's
injectivity theorem II*, version 1.25 (23 January 2011),
[Corollary 1.7, printed p. 4](https://www.math.kyoto-u.ac.jp/preprint/2011/02fujino.pdf#page=5).
Apply it first to B_n and then to B_n tensor O_W(K_W). The actual
adjoint identities are M^n(-T)=omega_W tensor B_n and
M^n=omega_W tensor (B_n tensor omega_W). They give

\[
H^1(W,M^n(-T))=H^1(W,M^n)=0.                         \tag{7}
\]

The first equality makes H^0(W,M^n) -> H^0(T,M^n|_T) surjective.
This checks the canonical correction twice; ampleness of M alone
would not be a justification for either application.

**Simultaneous values on the two complete fibres.** On either of the
disjoint type-III fibres T_0 and T_infinity, the two components are
copies of E and R. The maps g_0 and g_1 restrict to isomorphisms with
the fibre at infinity on S, preserving its components. This follows
from the unramified base change and L008's order-seven automorphism
on this fibre. Thus M^n has component degrees

\[
2n(L.E)\ge2,\qquad 2n(L.R)\ge2.                     \tag{8}
\]

The three marked points on each fibre are the zero-section point on
R, the tangency point E intersect R, and the other fixed point on E.
The intersection scheme Z=E intersect R has length two, supported
at the tangency, as both components are smooth and have intersection
number two. For a line bundle N on this fibre, the union sequence is

\[
0\longrightarrow N\longrightarrow N|_E\oplus N|_R
\longrightarrow N|_Z\longrightarrow0,              \tag{9}
\]

where the last map is the difference of restrictions with the actual
bundle identifications. This is the standard fibre-product gluing
sequence, cf. [Stacks Lemma 37.67.8, tag 0B7M](https://stacks.math.columbia.edu/tag/0B7M).

Prescribe arbitrary values at all three marked points. Choose any
element of H^0(Z,N|_Z) whose value at the tangency is the prescribed
one. On each component P^1, prescribe this same length-two restriction
and the specified value at its other marked point. These prescriptions
have total length three. For O_(P^1)(e) with e>=2 they can be met,
because H^1(P^1,O(e-3))=0. The resulting two sections glue by (9).
The degree inequalities (8) therefore give surjective evaluation at
the three marked points simultaneously. Applying this independently
on the two disjoint fibres, and using (7), gives surjective evaluation
from H^0(W,M^n) at all six points. The length-two tangency condition
has been retained, not replaced by separate pointwise separation.

**Descent across all three surface double points.** L008's local ring
at each double point has normalization
C[[r_1,r_2]] direct sum C[[s_1,s_2]], with its subring consisting of
pairs having equal constant terms. The normalization quotient is
therefore one copy of C at each of the three points. This local
calculation and the isomorphism elsewhere give

\[
0\longrightarrow O_C\longrightarrow\nu_*O_W
\longrightarrow\bigoplus_{i=1}^3 C_{p_i}
\longrightarrow0.                                  \tag{10}
\]

Tensor by O_C(nH) and use the finite projection formula. The resulting
quotient map on sections is the difference of the two values over
each p_i, with the fibre identifications supplied by O_C(nH). Surjective
evaluation at all six points proves that this difference map is onto,
regardless of those identifications. The long exact sequence of (10)
and H^1(W,M^n)=0 now prove (1). Finite pushforward preserves coherent
cohomology; supporting references are
[Stacks Lemma 30.2.4, tag 089W](https://stacks.math.columbia.edu/tag/089W)
and the projection formula in
[Lemma 20.54.2, tag 01E8](https://stacks.math.columbia.edu/tag/01E8).
No single-pullback description or unproved descent linearization for M
has been used.

**Effect on the attempted construction.** Equation (1) supplies L018's
recovery hypothesis for every n>0. For every admissible smooth B with
the stated m>n, an embedded lift of C union B therefore recovers an
embedded lift of C, which L008 excludes outside V_D. The attainable
ambient directions are contained in the three-dimensional V_D, against
four RM directions required. They equal V_D only under the additional
ideal-cohomology hypothesis retained in L018. This result closes the
remaining positive-degree case of that particular degree ordering.
It neither treats arbitrary added components nor constructs algebraic
cycles on a transverse surface.

The vanishing and gluing frameworks are imported known results. The
all-positive-degree specialization, including (4), was not matched by
the saved literature assessment. It is recorded as potentially beyond
the checked statements, without a claim of originality or a general
Hodge resolution. The proof above is informal. Exact rational checks
of (2), V's orthogonality and square, and (3) for -25<=j<=25 passed;
the generic-fibre argument and the uniform inequality, not this finite
check, prove the assertions for all j and all ample L.

## Mathlib

Coverage of the full statement: **not checked**. No full match,
supporting Mathlib theorem name, or absence is asserted. Fujino
Corollary 1.7 and the named Stacks lemmas are supporting vanishing,
gluing, cohomology and projection-formula inputs; none is claimed to
state (1) for this correspondence. The published family theorem supplies
rho(S)=4. Adjunction, Hodge index, the elliptic generic-fibre group law,
the nef positive-square criterion for bigness on a surface, and the
cohomology of O(e) on P^1 are further named standard inputs. The
specialized lattice inequality, canonical correction and simultaneous
gluing argument are given in full above.

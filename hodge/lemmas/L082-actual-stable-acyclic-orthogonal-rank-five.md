# L082 — Actual stable acyclic orthogonal rank-five fibres from the seed

## Hypotheses

Use L080's marked projective complex K3 surface S and its unchanged
real ample class h, and its actual h-stable spherical rank-two E.
Write eta for the integral point class. Thus c_1(E)=k, k.h=0,
k^2=-14, ch_2(E)=-5 eta, and

\[
J_0=\mathcal O_S\oplus E\oplus E^\vee,\qquad
Q((a,e,\phi),(b,f,\psi))=ab+\phi(f)+\psi(e).
\]

Keep the natural orientation. Use L081's coordinates on
H^1(S,mathfrak m), where mathfrak m=so(J_0,Q), and its compatible
formal deformation with first class

\[
\xi:\quad x=y=u_1=1,\quad v_1=-1/2,\quad u_i=v_i=0\ (i>1).
\tag{1}
\]

L081 proves that this is a formal Maurer--Cartan direction, not just
a solution of a necessary quadratic equation. No image or product
kernel is assumed. Choose a Kahler form omega representing precisely h.

## Conclusion

There is a holomorphic locally free quadratic family on S times a
small complex disc, with central fibre (J_0,Q), fixed orientation and
first Kodaira--Spencer class xi. Every sufficiently small nonzero
fibre J_t is stable as an underlying vector bundle at the exact h,
and has

\[
\operatorname{rank}J_t=5,\quad c_1(J_t)=0\text{ integrally},\quad
c_2(J_t)=10\eta,\quad \det J_t\simeq\mathcal O_S,
\qquad H^i(S,J_t)=0\quad(i=0,1,2).
\tag{2}
\]

Each such fibre and its perfect symmetric form are algebraic.
The family need not be algebraic over the analytic disc. Its formal
completion need not be the particular formal family of L081 beyond
first order.

This gives the individual stable acyclic orthogonal rank-five block
requested in L079's surviving branch. It is a local ADVANCE /
REPRODUCTION of the assessed tools, preserved by the separate critical
audit below.
It does not construct the other image, a common F, its prescribed
mixed character, transport, or additional algebraic Hodge classes.
No spin condition or prescribed w_2 or w_4 is claimed.

## Proof

**Imported results and reason for specialization.** Use Buchdahl--
Schumacher, *Polystable bundles and representations of their
 automorphisms*, Complex Manifolds 9 (2022), 78--113,
[DOI 10.1515/coma-2021-0131](https://d-nb.info/1262812674/34),
Section 2, Lemma 2.5, Proposition 2.6 and (2.4), pp. 83--84;
Theorem 8.1, p. 103, and Theorem 5.4, pp. 93--94 (summarized in
Theorem 3, p. 79). Their analytic vector slice and local stability
criterion apply at a fixed compact Kahler metric to a polystable
bundle. Stability uses the full automorphism group modulo common
scalars (p. 79). These general theorems are imported. Below we check
the quadratic restriction, formal first jet and full-vector orbit,
which those statements do not compute for this seed.

Use Artin, *On the solutions of analytic equations*, Invent. Math.
5 (1968), 277--291,
[Theorem (1.2), p. 277](https://mathweb.ucsd.edu/~toal/artin.pdf):
a formal solution of finitely many convergent equations over C can
be approximated to any finite order by a convergent solution. Use
order two. For the algebraic fibres use Serre, *Geometrie algebrique
et geometrie analytique*, Ann. Inst. Fourier 6 (1956), 1--42,
[Section 12, Theorems 1--3, pp. 19--20](https://www.numdam.org/article/AIF_1956__6__1_0.pdf#page=20).
The actual-fibre cohomology calculation uses only K3 Riemann--Roch,
Serre duality and slope stability, as already used in L080; no
semicontinuity inference from the obstructed central section is needed.

**A compatible metric and the same vector slice.** The
Donaldson--Uhlenbeck--Yau theorem on compact Kahler manifolds gives a
Hermite--Einstein metric on E at omega. Its Einstein constant is zero
because k.h=0. Give E^vee the dual metric and O_S its constant metric.
The direct-sum Chern connection D_0 on J_0 is Hermite--Einstein with
constant zero. Evaluation and multiplication are parallel, so Q and
the chosen orientation are D_0-parallel.

Let T be coefficientwise complex-linear Q-transpose on End(J_0),
not hermitian adjoint. In a unitary frame of E and its dual, Q has
a constant real unitary matrix; hence T is an isometric involution
for the Hilbert--Schmidt metric on endomorphisms. It is parallel.
Consequently T commutes with d=bar-partial_0, its Hilbert adjoint
d*, the Dolbeault Laplacian, harmonic projections H_q and Green
operators. The skew and self-adjoint coefficient spaces are
orthogonal and invariant under all these operators. Skew coefficients
are closed under the graded Lie bracket by L081's calculation.

Work with Sobolev exponent p>4, since dim_C S=2. For a small harmonic
alpha in H^{0,1}(End J_0), the cited slice has

\[
a(\alpha)=\alpha+d^*\beta(\alpha),\qquad
\beta\in(\ker d^*)^\perp\subset A^{0,2}(\operatorname{End}J_0),
\tag{3}
\]

where beta is the unique small analytic solution of

\[
(1-H_2)\{d d^*\beta+
 (\alpha+d^*\beta)\wedge(\alpha+d^*\beta)\}=0.
\tag{4}
\]

Here ker d* on (0,2)-forms equals the harmonic space: there are no
(0,3)-forms on S. Thus (4) is exactly the projection in Proposition
2.6, not a replacement slice. Its linearization in beta is dd*,
invertible on the displayed complement. The estimates and analytic
existence are those of the cited proposition.

If alpha is skew, the entire left side of (4) is skew whenever beta
is skew: the square of a degree-one skew form is one half of its
graded bracket with itself. All the linear operators preserve that
subspace. The same invertible linearization restricts to its skew
part; the analytic implicit-function construction there gives a
solution. Uniqueness in the full vector construction identifies it
with beta(alpha) in (3). Thus a(alpha) is skew, and its curvature is
skew as well. Moreover beta(0)=0 and its linear term is zero.

The actual obstruction is the finite-dimensional holomorphic map

\[
\Psi(\alpha)=H_2(a(\alpha)\wedge a(\alpha)).
\tag{5}
\]

Equation (4) says that the remaining curvature is harmonic; hence
Psi=0 is equivalent to integrability. On skew harmonic inputs it
takes values in H^{0,2}(mathfrak m), of dimension one by L081.
Its domain H^{0,1}(mathfrak m) has dimension twelve. This gives
finite convergent equations for actual form-preserving deformations
inside the *same* vector slice used in the stability theorem. It
makes no assertion that (5) is analytically the quadratic equation
in L081, or that the full vector group preserves the skew subspace.

**The formal curve lies in this slice with the required first jet.**
Represent L081's compatible formal deformation, on the fixed smooth
quadratic bundle, by

\[
\widehat A(t)\in t A^{0,1}(\mathfrak m)[[t]],\qquad
 d\widehat A+\widehat A\wedge\widehat A=0.
\]

Its first cohomology class is xi. Formal smooth quadratic
trivializations and the identity on first cohomology are part of
L081; no convergence of A-hat is assumed.

Place it in d*-gauge using formal orthogonal transformations congruent
to the identity. Explicitly, suppose the coefficients of d*A vanish
below order n, and the order-n coefficient of A is B_n. The function
d*B_n is orthogonal to ker d on degree-zero skew forms. There is a
unique skew phi_n perpendicular to this kernel solving

\[
d^*d\phi_n=d^*B_n.
\tag{6}
\]

The inverse is the degree-zero Green operator on that complement;
it preserves skew coefficients as established above. Gauge by
exp(t^n phi_n). Under the convention g(d+A)g^{-1}, the order-n
coefficient becomes B_n-d phi_n, so (6) kills its d*. Lower
coefficients are unchanged. The successive product is well defined
t-adically, preserves Q and orientation, and yields a formal
integrable A' with d*A'=0. This is an order-by-order argument, not
an analytic gauge-convergence claim. At first order it changes the
representative by an exact term only.

Hodge decomposition coefficientwise gives unique formal alpha-hat
and beta-hat such that

\[
 A'=\widehat\alpha+d^*\widehat\beta,\quad
 \widehat\alpha=H_1 A',\quad
 \widehat\beta\in(\ker d^*)^\perp[[t]].
\tag{7}
\]

The exact component vanishes since d*A'=0. All terms are skew.
Integrability makes beta-hat solve (4). The invertible linearization
in beta makes its formal coefficients unique recursively. They
therefore equal the Taylor substitution beta(alpha-hat) from (3).
In particular

\[
\Psi(\widehat\alpha(t))=0,\qquad
\widehat\alpha(t)=t\xi_{\rm harm}+O(t^2),
\tag{8}
\]

where xi_harm is the harmonic representative of (1). At first order
integrability and d*-gauge say precisely that A'_1 is harmonic.

Choose linear coordinates on the twelve-dimensional skew harmonic
space and on the obstruction space. Apply Artin's theorem to the
convergent equations (5), with independent variable t and formal
solution (8). It gives a convergent alpha(t) satisfying Psi=0 and
alpha(t)=alpha-hat(t) modulo t^2. Shrink the disc so alpha(t) is in
the slice neighborhood. Then a(alpha(t)) is an actual integrable
family of skew Dolbeault operators; the construction of the cited
analytic slice supplies its holomorphic locally free family.
Equivalently its total Dolbeault operator is d+a(alpha(t))+bar-partial_t:
the mixed integrability equation holds because the coefficients are
holomorphic in t. The slice's elliptic regularity supplies the smooth
fibre coefficients. Q stays perfect, symmetric and holomorphic,
and the orientation stays holomorphic because skew endomorphisms
have trace zero. Since beta has no linear term, its first class is
exactly xi. Artin has preserved a jet, not proved convergence of the
original formal series.

**Full underlying-vector orbits, including higher-order terms.**
By L080 the full group is

\[
\Gamma=\operatorname{Aut}(J_0)=\{\operatorname{diag}(a,b,c)\}
 \simeq(\mathbb C^*)^3.
\]

On the quotient by common scalars set r=b/a and s=c/a. With source
and target blocks in the order (O_S,E,E^vee), conjugation has weights

| block | character of Gamma/common scalars |
|---|---|
| Hom(O_S,E) | r |
| Hom(E,O_S) | r^{-1} |
| Hom(O_S,E^vee) | s |
| Hom(E^vee,O_S) | s^{-1} |
| Hom(E^vee,E) | r/s |
| Hom(E,E^vee) | s/r |
| diagonal endomorphisms | 1 |

These are all block characters, with their full cohomology
multiplicities. The block projections commute with D_0 and its Hodge
operators, so they define weight projections on the full harmonic
vector space.

Under the skew inclusion, an E-valued (0,1)-form p has the two
blocks O_S->E, 1->p, and E^vee->O_S, phi->-phi(p).
An E^vee-valued form q has O_S->E^vee, 1->q, and E->O_S,
e->-q(e). These formulas follow directly by imposing
Q(Av,w)+Q(v,Aw)=0. They show that x nonzero gives nonzero harmonic
components of weights r and s^{-1}; y nonzero gives weights s and
r^{-1}. Each of these four cohomology spaces has dimension one by
L080. Choose fixed scalar coordinates on them. Along the actual
alpha(t) all four have nonzero linear coefficients, since x=y=1
in (1). A convergent scalar function with a nonzero linear term
has no zeros on a sufficiently small punctured disc. Thus all four
components are nonzero there, regardless of higher-order corrections
in any other weight space.

For completeness, closedness under the *full* torus is checked
explicitly, rather than inferred from the orthogonal stabilizer.
Fix any harmonic vector z with these four components nonzero, and
write them z_r,z_{r^{-1}},z_s,z_{s^{-1}}. Its orbit projects to

\[
(Rz_r,R^{-1}z_{r^{-1}},Sz_s,S^{-1}z_{s^{-1}}),
\quad (R,S)\in(\mathbb C^*)^2.
\]

This is the closed subvariety of affine four-space defined by the
two equations

\[
Z_r Z_{r^{-1}}=z_r z_{r^{-1}}\ne0,\qquad
Z_s Z_{s^{-1}}=z_s z_{s^{-1}}\ne0.
\tag{9}
\]

It is isomorphic to (C^*)^2, with regular inverse R=Z_r/z_r,
S=Z_s/z_s. Every other coordinate of the orbit is its original
value times a Laurent monomial in R,S (or is constant for weight
zero). Such monomials are regular on (9), since the inverse
coordinates are already regular there. The full orbit is therefore
the graph of a regular map from this closed subvariety into the
remaining affine coordinates. The graph is closed in the full
harmonic vector space. Its stabilizer in the quotient is trivial,
as its nonzero r- and s-coordinates force R=S=1. In Gamma the
stabilizer is exactly the common scalars. This proves affine GIT
stability with the source's scalar convention. It also proves that
additional coordinates cannot destroy the asserted closedness;
no openness of an orthogonal stable locus in the vector locus was
assumed.

Apply this calculation to alpha(t). Shrink the disc once more so
its norm satisfies the uniform neighborhood bounds in Buchdahl--
Schumacher Theorem 8.1 and Theorem 5.4. The seed connection is
Hermite--Einstein at precisely omega, alpha(t) is in the full vector
slice, and Psi(alpha(t))=0. Theorem 8.1 gives polystability of the
actual bundle; Theorem 5.4 upgrades it to stability because the
harmonic parameter is stable modulo common scalars. Equivalently
apply their Theorem 3. Uniformity of the neighborhood matters here:
alpha(t) need not stay on a single ray. No integral polarization,
principal-bundle simplicity, or stability deduced solely from a
first-order direction is substituted for these hypotheses.

**Invariants, actual cohomology, and algebraic fibres.** The family
uses the fixed smooth bundle J_0, so all integral Chern classes
are unchanged. L080 gives ch(J_0)=5-10 eta and trivial determinant;
the preserved orientation trivializes det(J_t) holomorphically.
Thus (2)'s rank and Chern assertions hold, and every J_t has slope
zero. If a nonzero section existed for a nonzero small t, the map
O_S->J_t would be injective as a sheaf because S is integral and
J_t is torsion-free. Its rank-one slope-zero image contradicts
strict stability of the rank-five bundle. Hence H^0(J_t)=0.
The perfect form gives J_t^vee isomorphic to J_t, so Serre duality
and K_S=O_S give H^2(J_t)=0. K3 Riemann--Roch yields

\[
\chi(J_t)=2\operatorname{rank}(J_t)+\int_S\operatorname{ch}_2(J_t)
=10-10=0,
\]

and therefore H^1(J_t)=0. This proves acyclicity on the actual
punctured-disc fibres, not on the unstable central fibre, whose
cohomology remains (1,2,1).

For fixed t, GAGA algebraizes J_t and its analytic dual as coherent
sheaves. Full faithfulness algebraizes evaluation and coevaluation;
their triangle identities persist by faithfulness. Thus the
algebraized sheaf is dualizable, hence finite locally free (locally,
a dual basis supplied by coevaluation proves projectivity). Full
faithfulness also algebraizes Q and the orientation; symmetry,
nondegeneracy and the orientation identities follow by faithfulness,
using the algebraized inverse of Q. Analytic cohomology equals
algebraic cohomology. Every algebraic destabilizing subsheaf would
analytify to one with the same rank, first class and exact-h slope,
so analytic stability implies algebraic h-stability as asserted.
No algebraization of the entire disc is needed.

The construction has reached precisely the individual block in (2).
The compatibility of any two blocks as transforms of one common
rank-two product bundle is an independent, unsolved condition;
existence of this fibre cannot be substituted for it. The original
Hodge target and the earlier stopped necessary-test routes remain
unchanged. The separate critical audit below retains these conclusions
without a stronger existence or transport assertion.

**Separate critical audit (2026-10-10).** The approved audit rechecked
all of this proof and the complete L080/L081 inputs. No substantive
error, new obstruction or stronger conclusion was found. This is an
EXPLORATION / REPRODUCTION audit, not a second existence advance.
The following checks record the load-bearing comparisons explicitly.

For the metric check, in the ordered unitary frame the matrix of Q is
\[
C=\begin{pmatrix}1&0&0\\0&0&I_2\\0&I_2&0\end{pmatrix},
\qquad T(A)=C^{-1}A^{\mathsf t}C.
\]
Thus T is complex-linear, unitary and involutive on coefficient
endomorphisms. Parallelness follows from preservation of Q by D_0;
it is not inferred from holomorphicity alone. Unitarity and dT=Td
imply d*T=Td* by taking Hilbert adjoints. The Green and harmonic
operators therefore preserve both eigenspaces. Although T reverses
coefficient multiplication, for degree-one skew forms A the exterior
sign gives T(A wedge A)=-A wedge A. This is the required nonlinear
invariance; T need not be an algebra automorphism.

The complement in (3) was compared with the actual construction in
Buchdahl--Schumacher Section 2, pp. 83--84, including Proposition
2.6 and (2.4). On this surface d is zero on degree two, so
Delta_2=dd* and ker d*=H^{0,2}. Consequently (4) is precisely its
projected equation, with no extra infinite-dimensional curvature
component. Restricting its invertible linearization to skew forms
and then using uniqueness is legitimate. In Sobolev terms beta lies
in W^{2,p} and a in W^{1,p}, with p>4. More explicitly the equation is
\[
\beta=-G_2(1-H_2)(a\wedge a).
\]
W^{1,p} is an algebra; this identity first improves beta to W^{3,p}
and a to W^{2,p}, and iteration gives smooth fibre coefficients.
The same bounded multiplication and elliptic inverse improve the
Banach-holomorphic dependence on t at each Sobolev order. Thus the
total Dolbeault operator used above defines an actual holomorphic
bundle family, with its fixed smooth form and orientation.

For every formal gauge order, solvability of (6) follows directly
from <d*B_n,z>=<B_n,dz>=0 for each z in ker d. The skew Green inverse
supplies phi_n without a harmonic ambiguity. The correction at
order n is -d phi_n, and all its commutator terms with A begin at
order n+1. Hence the induction preserves all earlier coefficients,
Maurer--Cartan integrability, Q and orientation. Hodge decomposition
then gives (7). At each order the beta coefficient in (4) is fixed
by the same invertible dd*, so formal uniqueness identifies this
series with the analytic slice's Taylor substitution, without an
analytic formality assertion. The saved Artin (1.2)/Rond Theorem 2.1
coverage applies to the twelve finite unknown coordinates and the
finite harmonic equation (5) over C{t}; approximation modulo t^2
retains the first class. It does not assert convergence of the
original formal deformation. The source-access qualifications of
the realization assessment remain unchanged.

The full-vector check retains four distinct one-dimensional block
spaces, even though the skew condition relates their coordinates.
The E and E^vee summands each inject into their two indicated Hom
blocks, and the dual metric makes these maps commute with harmonic
projection. Hence x=y=1 gives four nonzero linear coefficients.
For each sufficiently small t nonzero, (9) describes the projection
of the entire full-vector orbit, not just of an orthogonal orbit.
Its regular inverse determines every remaining Laurent coordinate,
so the graph argument proves closedness in the full affine space.
The r and s characters also kill every quotient stabilizer element;
there is no residual ineffective torus or finite stabilizer to check.

The published Theorem 8.1, p. 103, explicitly bounds the neighborhood
in terms of D_0 alone; the stable continuity argument, pp. 105--106,
retains this direction independence. Its polystability conclusion
therefore applies to the curved analytic arc. Theorem 5.4, p. 93,
requires that conclusion before its stability equivalence can be
used. That order is respected. The common-scalar quotient is the
one specified on p. 79. All these results use the same fixed omega;
no rational replacement of h occurs. These are applications of the
published theorems, not reproofs or newly expanded source coverage.

Finally, a hypothetical actual section gives an injective O_S
subsheaf of equal slope and smaller rank. Even a definition testing
only saturated subsheaves yields the same contradiction, since
saturation cannot decrease degree. Thus stability gives H^0=0;
self-duality gives H^2=0, and chi=0 gives H^1=0. Integral Chern data
are constant on the fixed smooth family. The GAGA argument applies
to each fibre's coherent bundle, its dual and all form/orientation
morphisms; dualizability verifies local freeness and faithfulness
verifies the identities. Neither the central section's first-order
obstruction nor an algebraic disc family is used. The individual
J_5 conclusion survives; the other image, a common F with its full
mixed action, and transport remain unresolved.

## Mathlib

Full matching orthogonal-seed realization, analytic approximation,
fixed-real-metric bundle/GIT comparison and GAGA specialization:
not checked. Supporting Hodge/elliptic and cohomological declarations:
not checked. The cited mathematical theorems, rather than a Mathlib
formalization, supply those inputs. No absence, verified Lean proof,
or mathematical originality is claimed.

# L081 — The actual orthogonal seed has a nontrivial quadratic formal model

## Hypotheses

Use L080's actual projective K3 surface S, real ample class h,
locally free h-stable spherical rank-two E, and quadratic bundle

\[
J_0=\mathcal O_S\oplus E\oplus E^\vee,
\quad Q((a,e,\phi),(b,f,\psi))=ab+\phi(f)+\psi(e).
\]

Thus c_1(E)=k, k.h=0, k^2=-14, ch_2(E)=-5 eta,
H^*(E) and H^*(E^vee) have dimensions (0,1,0), and
Ext^*(E,E) has dimensions (1,0,1). Fix the natural orientation
of J_0 and a nonzero holomorphic two-form sigma on S. Let

\[
\mathfrak m=\mathfrak{so}(J_0,Q),\qquad
M=A^{0,*}(S,\mathfrak m),\quad d=\bar\partial.
\]

We study formal deformations of this actual bundle preserving its
perfect O-valued symmetric form and orientation. No product kernel,
stable deformation, or convergent family is assumed.

## Conclusion

M is formal as a DG Lie algebra. Its cohomology dimensions are

\[
(\dim H^0(M),\dim H^1(M),\dim H^2(M))=(1,12,1).
\]

For symplectically normalized coordinates (x,y,u_1,...,u_5,v_1,...,v_5)
on H^1(M), the quadratic Maurer--Cartan equation is precisely

\[
xy+2\sum_{i=1}^5 u_i v_i=0. \tag{1}
\]

The orientation-preserving central automorphism torus acts with
weights +1,-1,+2,-2 on x,y,u,v respectively. Equation (1) has
points with x and y both nonzero. Any such point is the first class
of a compatible formal form-preserving deformation over C[[t]].
For its first-order truncation, the unique central section of J_0
does not lift.

This proves a useful formal intermediate input for the seed recipe.
It does not prove analytic realization, underlying-vector h-stability,
acyclicity of a realized general fibre, or existence of L079's J_5.
In particular failure to lift the central section over dual numbers
alone is not a claim about cohomology of an actual nearby bundle.

## Proof

**Named inputs and applicability.** Use Bandiera--Manetti--Meazzini,
*Formality conjecture for minimal surfaces of Kodaira dimension 0*,
Compositio Math. 157 (2021), 215--235,
[postprint 1907.10690v2, 2 August 2020](https://arxiv.org/pdf/1907.10690v2),
Theorem 5.1, p. 15, Theorem 2.3, pp. 5--6, and Example 3.2,
p. 6. Theorem 5.1 gives formal derived endomorphisms for a coherent
sheaf with linearly reductive automorphism group on a complex
projective surface with trivial canonical bundle. Theorem 2.3
transfers formality to an injective DG Lie subalgebra which is a
direct summand as a module over that subalgebra. Example 3.2
identifies the degree-one quadratic bracket with the moment map
of the degree-zero symplectic representation. The formal
Maurer--Cartan interpretation and quasi-isomorphism invariance
are recalled in Section 1, p. 2, of the same source.

These general results are imported, not reproved. L080 gives an
actual bundle, Aut(J_0)=(C^*)^3, and the required projective K3
surface. Thus Theorem 5.1 applies without replacing irrational-h
slope polystability by Gieseker polystability at a chosen integral
polarization. We verify the split-module and cyclic hypotheses
and compute their specialization below.

**The split DG Lie subalgebra really preserves the form.** Let T
be coefficientwise Q-adjoint on End(J_0). It is a holomorphic
involution, so commutes with bar-partial. In characteristic zero

\[
\operatorname{End}(J_0)=\mathfrak m\oplus\mathfrak s,
\quad \mathfrak m=\ker(T+1),\quad\mathfrak s=\ker(T-1).
\tag{2}
\]

If a is skew and b is self-adjoint, then
T([a,b])=[a,b]; commutators of two skew coefficients are skew.
For coefficient-valued forms of degrees p,q, the graded bracket
of a alpha and b beta is [a,b] alpha wedge beta, so the same
assertions hold in every degree. Thus M is a DG Lie subalgebra of
L=A^{0,*}(S,End(J_0)), and A^{0,*}(S,mathfrak s) is its DG module
complement. The projection (1-T)/2 commutes with d and the M-action.
L represents RHom(J_0,J_0), since J_0 is locally free, and is
formal by Theorem 5.1. Theorem 2.3 applied to (2) proves formality
of M. A vector-space splitting alone would not suffice; the
commutator calculation verifies precisely the required module splitting.

For clarity, M controls form-preserving deformations: a
bar-partial operator bar-partial+A on the fixed smooth quadratic
bundle preserves Q when A is skew-adjoint, and its integrability
equation is dA+[A,A]/2=0. Changes of a smooth oriented orthogonal
trivialization give the skew degree-zero gauge action. Over an
Artin local base these descriptions lose no quadratic deformation.
Smooth bundle trivializations lift across each nilpotent extension,
because the smooth endomorphism sheaf is fine. A lifted symmetric
form congruent to Q can then be carried to Q: its relative
endomorphism is 1+N with N nilpotent and Q-self-adjoint, and the
finite binomial square root gives the correcting isometry. It can
be chosen congruent to the identity and hence preserves the chosen
orientation. The resulting Dolbeault descriptions glue globally.
This establishes the formal deformation interpretation; it makes
no convergence assertion for a compatible tower of Artin deformations.

**Complete adjoint cohomology and weights.** The form identifies
mathfrak m with wedge^2 J_0. Exterior powers of the displayed direct
sum give an actual holomorphic bundle decomposition

\[
\mathfrak m\simeq
\operatorname{End}(E)\oplus E\oplus E^\vee
\oplus\det(E)\oplus\det(E)^\vee. \tag{3}
\]

The torus b maps the three seed factors by (1,b,b^(-1)). Its
weights on (3) are 0,+1,-1,+2,-2. This is an action on the actual
adjoint bundle, not a choice of extra endomorphisms of E.

Put D=det(E). It is a nontrivial line bundle with c_1=k. Neither
D nor D^vee has a section: an effective nonzero divisor has
positive intersection with the real ample h, whereas +/-k has
degree zero; a nowhere-vanishing section would trivialize the line
bundle, contrary to nonzero first class. Serre duality gives zero
H^2 for both lines. K3 Riemann--Roch gives chi(D)=2+k^2/2=-5,
and similarly for D^vee. Their H^1 dimensions are therefore five.
L080 supplies the complete E,E^vee and End(E) cohomology.
Consequently (3) gives

\[
H^0(M)=\mathbb C a,\quad
H^1(M)=H^1(E)\oplus H^1(E^\vee)\oplus H^1(D)\oplus H^1(D^\vee),
\quad H^2(M)\simeq\mathbb C,
\]

where a=diag(0,id_E,-id_(E^vee)). This proves dimensions (1,12,1),
with no discarded weight-zero H^1 term: that term is zero because
E is spherical.

**Pairing and the single quadratic equation.** On M use the
degree-two cyclic pairing

\[
B(\alpha,\beta)=\int_S\sigma\wedge\operatorname{tr}(\alpha\wedge\beta).
\tag{4}
\]

The trace form on the skew endomorphisms is nondegenerate fibrewise.
For example, after a local orthonormal choice it is the usual
nondegenerate trace form on so(5,C). It identifies mathfrak m with
its dual; Serre duality on the K3 surface therefore makes (4)
nondegenerate on cohomology. The differential and bracket cyclic
identities follow from integration of bar-partial and graded trace
cyclicity. On H^1 it is an alternating form, denoted omega.

The torus preserves (4), so weights whose sum is nonzero pair to
zero. Perfectness now makes H^1(E) and H^1(E^vee) a perfect paired
pair, and likewise H^1(D) and H^1(D^vee). Choose bases e,f and
p_i,q_i with omega(e,f)=1 and omega(p_i,q_j)=delta_ij. All other
pairings follow by antisymmetry or are zero. These normalizations
include the actual trace-form constants; no relative scalar between
the two paired weight spaces is omitted.

Identify H^2(M) with H^0(M)^vee by B. Cyclicity, or Example 3.2,
gives for xi in H^1(M)

\[
B\bigl(a,\tfrac12[\xi,\xi]\bigr)
=\tfrac12\omega([a,\xi],\xi).
\tag{5}
\]

Writing xi=xe+yf+sum_i(u_i p_i+v_i q_i), its a-weights give

\[
\tfrac12\omega([a,\xi],\xi)=xy+2\sum_i u_i v_i.
\]

Since a spans H^0 and its pairing with H^2 is perfect, (5)
vanishes exactly when the entire degree-two obstruction vanishes.
There are no other degree-two components. Formality identifies the
formal Maurer--Cartan deformation functor of M with that of its
cohomology, where d=0 and the equation is [xi,xi]/2=0. This is a
formal statement; no analytic neighborhood is inferred from it.

**A direction and its section test.** Choose

\[
x=y=u_1=1,\quad v_1=-\tfrac12,\quad
u_i=v_i=0\ (i>1). \tag{6}
\]

It satisfies (1) exactly: 1+2(-1/2)=0. The class t xi solves the
cohomological Maurer--Cartan equation over every C[t]/(t^(n+1)).
The formal equivalence transfers it to a compatible formal
deformation of (J_0,Q). The equivalence can be normalized to
induce the identity on cohomology, by precomposing with its induced
graded-Lie cohomology automorphism's inverse. Thus its first class
is the displayed xi, rather than an unspecified transformed class.

Let s_0=(1,0,0) generate H^0(J_0). The first-order obstruction to
lifting s_0 is [A_1(s_0)] in H^1(J_0): expanding a proposed section
s_0+t s_1 in (bar-partial+t A_1)s=0 gives
bar-partial s_1=-A_1(s_0). Under the natural skew identification
of wedge^2 J_0, a wedge s_0 and e sends s_0 to a nonzero scalar
multiple of e, and similarly for E^vee. The two determinant
summands and End(E) annihilate s_0. Hence this cohomological
evaluation map is an isomorphism on each of the E,E^vee H^1
summands, and the section obstruction has nonzero components when
x,y are nonzero. For (6) it cannot vanish. This calculation concerns
the underlying vector bundle and the actual unique central section,
not just the principal automorphism Lie algebra.

**Limits of the conclusion.** The formal equation admits the
discriminating direction (6), so there is no quadratic/formal
obstruction that abandons this seed recipe. Analytic realization
of the compatible formal deformation, or another actual deformation
with the same tangent, remains to be justified separately. Even
realization would require checking cohomology in that actual family
and all underlying-vector slope subsheaves at the exact real h.
A torus stabilizer calculation, simplicity of a principal bundle,
or a first-order section obstruction alone does not prove those
claims. The other L079 image, common kernel and transport remain
independent gaps, as does universal primitive Hodge algebraicity.

## Mathlib

Full matching orthogonal-seed formality, moment-model and K3-bundle
deformation coverage: not checked. The cited mathematical source
provides the supporting general formality/transfer/moment results.
No matching Mathlib declaration, absence claim or formal verification
is asserted. This is a REPRODUCTION specialization of the already
assessed tools, not a claim of mathematical originality.

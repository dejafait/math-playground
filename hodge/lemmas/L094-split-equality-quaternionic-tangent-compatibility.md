# L094 — Compatible quaternionic tangents at the split equality fibre

## Hypotheses

Use L071's marked K3 surface S, exact real Kähler class h and fixed
hyperkähler metric. Let k be its nonzero integral zero-slope class,
with k^2=-14, and L the holomorphic line bundle of class k. Give
E=L direct sum L^{-1} its determinant-one Hermite--Einstein connection
A. Its curvature is ASD for the complex orientation. Write I,J,K for
the metric's ordered hyperkähler structures and omega_R for their
Kähler forms. All coefficient connections and adjoints below use this
fixed metric and the direct-sum Hermitian metric.

The conditional family statement concerns exactly L071's hypothetical
locally free Omega-polystable rank-two F on S_1 x S_2 with integral
c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D, and a parameter y_0 whose
S_1-fibre is E. Both factors have the identical marked metric. L093
places this pair on its equality boundary; it does not assert F exists.

## Conclusion

The determinant-fixed compact stabilizer of A is U(1). Its real ASD
harmonic deformation space V has quaternionic dimension 26. With
respect to I, its complex weight spaces are H^1(L^2) and H^1(L^{-2}),
both of dimension 26, with weights +2 and -2. There is no diagonal
harmonic deformation sector.

The necessary second-order ASD obstruction is

\[
 Q(a)=\Pi_{\operatorname{coker}d_A^+}(a\wedge a)^+,
 \qquad a\in V=\ker d_A^*\cap\ker d_A^+.
\]

It vanishes on an explicit nonzero quaternionic line W in V. This
checks all three real diagonal components and every off-diagonal
component of Q, not only the complex Yoneda equation.

For the actual conditional F, its family derivative at y_0, projected
to V before dividing by the residual stabilizer, is quaternionic and
satisfies Q(df(u))=0 for every real parameter direction u. It need
not be assumed nonzero. The constructed W therefore shows that this
necessary test alone cannot exclude all nonzero quaternionic tangents.
It does not show that the actual derivative equals W, that W integrates,
or that a nonconstant germ or F exists. Zero-derivative germs, higher
orders, the prescribed global mixed action, all-stable equality kernels
and transverse transport remain unresolved.

This is NEGATIVE / REPRODUCTION: a scoped compatibility specialization
of the assessed slice and coefficient tools, with no originality claim.
It stops this bounded exclusion mechanism, not the Hodge conjecture.
The separate critical audit below preserves this conclusion.

## Proof

**Imported scope.** Import Tobias Diez and Gerd Rudolph, *Normal form
of equivariant maps in infinite dimensions*, Ann. Global Anal. Geom.
61 (2022), 159--213, DOI 10.1007/s10455-021-09777-2,
[Theorem 5.8 and Section 5.3, (5.14)--(5.23)](https://link.springer.com/article/10.1007/s10455-021-09777-2#Sec12),
with its slice/tube construction in Theorem 5.3. SU(2) is compact and
semisimple and S is compact, oriented and four-dimensional. Thus an
ASD slice and finite-dimensional equivariant obstruction chart exist
at A, including its reducible stabilizer. Neither genericity of h nor
irreducibility is needed. We do not import a quadratic normal form or
a smooth quotient. The local slice acts on actual connections before
the quotient; we do not lift a map through a quotient homeomorphism.

Import coefficient harmonic quaternionic invariance from Verbitsky,
*Hyperholomorphic bundles*,
[alg-geom/9307008v1, Section 4, Theorem 4.1 and Corollary 4.3, pp. 12--15](https://arxiv.org/pdf/alg-geom/9307008v1#page=12).
The coefficient bundle is End_0(E), with parallel skew-adjoint real
structure; its connection is hyperholomorphic because A is ASD on a
hyperkähler surface. Trace-free and real summands are preserved. This
input concerns coefficients and does not require E simple. It does
not apply the stable coarse-moduli theorems of Sections 6--7 at A.

The analytic fixed-Kähler slice and quadratic moment construction are
also covered by Buchdahl--Schumacher, *Polystable bundles and
representations of their automorphisms*, Complex Manifolds 9 (2022),
78--113, DOI 10.1515/coma-2021-0131,
[Lemma 2.5, Proposition 2.6/(2.4), Corollary 5.3/(5.1)](https://d-nb.info/1262812674/34).
The direct sum E is polystable at the actual real h and its metric
has determinant one. We specialize the necessary quadratic term by
the curvature expansion below: this verifies its three components
without asserting an exact quadratic chart or reproving a slice theorem.

**Stabilizer and the two coefficient spaces.** Every nonzero multiple
of k has degree zero and cannot be an effective divisor, because h is
Kähler. Thus L^{2} and L^{-2} have no section. By Serre duality on S,
they have no degree-two cohomology either. The K3 Riemann--Roch formula
chi(M)=2+c_1(M)^2/2 gives chi(L^{+/-2})=2-28=-26, so

\[
 h^1(L^2)=h^1(L^{-2})=26.                         \tag{1}
\]

Here the named RR and duality inputs have the same scope as L071:
Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication,
[Chapter 1, (2.5)--(2.6) and Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
No rational polarization is used in the endpoint argument.

A parallel off-diagonal endomorphism would be a section of L^{+/-2},
so none exists. Parallel diagonal unitary determinant-one automorphisms
are exactly diag(exp(it),exp(-it)); there is no exchanging component,
as that would give an isomorphism L to L^{-1}. Thus the stabilizer is
U(1), including its ineffective central subgroup {+1,-1}. Write
xi=diag(i,-i) for its parallel infinitesimal generator.

In the I-holomorphic description,
End_0(E)=O diag(1,-1) direct sum L^2 direct sum L^{-2}.
The Kähler harmonic identification sends a real skew-adjoint one-form
a to b=a^{0,1}, with inverse a=b-b^*. Indeed the linearized equations
F^{0,2}=0 and Lambda F=0, together with d_A^*a=0, are exactly
bar-partial_A b=bar-partial_A^* b=0 by the coefficient Kähler identities.
This is a linear identification; no smooth-moduli assertion enters.
Since H^1(O_S)=0, every a in V is entirely off-diagonal. Equation (1)
gives dim_R V=104 and dim_H V=26. Conjugation by the stabilizer has
complex weights +2 on H^1(L^2) and -2 on H^1(L^{-2}).

On real one-forms use R_c a=-a composed with R for R=I,J,K. These
operators are orthogonal, satisfy I_c J_c=K_c and preserve V by the
coefficient harmonic input. They commute with conjugation by the
stabilizer. In particular J_c is anti-complex-linear for I_c and
exchanges the two weight spaces. Below suppress the subscript c.
Let G(a,b)=integral_S -Tr(a wedge *b), a positive real inner product,
and let T a=[xi,a]. Then T commutes with I,J,K and is skew-adjoint.
On the positive weight space T=2I; on the negative space T=-2I.

**The complete necessary quadratic term.** A smooth curve of actual
ASD connections in a Coulomb slice has expansion
A(s)=A+s a+s^2 b/2+O(s^3). The curvature equation gives

\[
 d_A^+a=0,\qquad \tfrac12d_A^+b+(a\wedge a)^+=0.
                                                               \tag{2}
\]

Projecting (2) to the cokernel gives Q(a)=0. Ellipticity supplies the
orthogonal projection and closed range here. This is only a necessary
second-order condition and does not discard higher terms in the chart.

Because a is off-diagonal, a wedge a is diagonal and trace-free. The
connection, d_A^+ and its cokernel projection preserve the orthogonal
diagonal/off-diagonal splitting. Consequently Q has zero component
in both off-diagonal sectors, without any assumption on their cokernel
dimensions. On the diagonal, the coefficient line R xi is parallel
and trivial. An ordinary self-dual two-form in the cokernel of d^+
is coclosed and hence closed, so is harmonic. The K3 self-dual harmonic
space is exactly the three-dimensional span of omega_I,omega_J,omega_K.
Thus the remaining obstruction is completely tested against xi omega_R.

For the complex orientation and omega_R(v,w)=g(Rv,w), the elementary
one-form identity is

\[
 \int_S-\operatorname{Tr}(a\wedge b)\wedge\omega_R=G(Ra,b).
                                                               \tag{3}
\]

It follows, for example, by evaluating in an oriented orthonormal
frame (e,Ie,Je,Ke): omega_I=theta_0 wedge theta_1+theta_2 wedge theta_3
and I theta_0=theta_1; the other two cases follow by the quaternionic
frame permutations. The same identity holds for matrix coefficients
by bilinearity and the trace. Cyclicity and the odd form degrees give
Tr([xi,a] wedge a)=2Tr(xi a wedge a). Since omega_R is self-dual,

\[
 \langle(a\wedge a)^+,\xi\omega_R\rangle_{L^2}
 =\int_S-\operatorname{Tr}(\xi a\wedge a)\wedge\omega_R
 =\tfrac12G(RTa,a)=:\mu_R(a).                         \tag{4}
\]

Normalization of the basis xi omega_R changes the projection
coefficients by a common nonzero factor only. Equations (2)--(4)
show Q(a)=0 if and only if all three mu_R(a) vanish. This explicitly
retains the real moment component as well as the two real components
of the holomorphic obstruction.

**An explicit compatible quaternionic line.** Choose e_1,e_2 Hermitian
orthonormal in the positive complex weight space of dimension 26.
The real quaternionic lines H e_1 and H e_2 are orthogonal: same-weight
Hermitian orthogonality handles e_i,Ie_i, opposite weights are orthogonal
for the unitary circle action, and J preserves the metric. In particular
(e_i,Ie_i,Je_i,Ke_i) is a real orthonormal frame in each line.
Put v=e_1+Je_2. Then

\[
 Tv=2Ie_1-2Ke_2,\quad Iv=Ie_1+Ke_2,\quad
 Jv=Je_1-e_2,\quad Kv=Ke_1-Ie_2.
\]

These formulas give G(Tv,v)=G(Tv,Iv)=G(Tv,Jv)=G(Tv,Kv)=0;
in the I-pairing the two equal norms cancel, and all other terms are
orthogonal. Let W=span_R(v,Iv,Jv,Kv). It is a quaternionic line,
with the displayed four vectors orthogonal of squared norm 2.
For any two real quaternionic linear combinations P,Q of 1,I,J,K,
commutation of T with these operators yields

\[
 G(TPv,Qv)=G(Tv,P^*Qv)=0,
\]

because P^*Q is again a real quaternionic linear combination and
P^*Qv lies in W. Thus T(W) is orthogonal to W. For w in W and
R=I,J,K, formula (4) gives mu_R(w)=-G(Tw,Rw)/2=0. This proves
Q|_W=0 for every vector and hence also for every polarized quadratic
cross term on W. The real-linear map from a quaternionic source line
sending its ordered basis (u,Iu,Ju,Ku) to (v,Iv,Jv,Kv) is injective
and quaternionic. Positive rescaling preserves this compatibility.
No stabilizer quotient or convergent family is constructed by this map.

**Actual-family tangent at the reducible point.** L071 supplies the
conditional F with its compatible hyperholomorphic connection. Its
trivial determinant has flat determinant connection (the HE equation
on the holomorphically trivial determinant has zero curvature), so
we work in SU(2). Over a contractible parameter neighborhood of y_0,
choose a smooth unitary identification of the fibre bundles. Let A_y
be the vertical connection and H_u the horizontal connection coefficient.
The actual mixed curvature satisfies, at y_0,

\[
 r_u(t)=R_F(u,t)=\dot A_u(t)-(d_AH_u)(t).              \tag{5}
\]

Every A_y is ASD, so dot A_u is d_A^+-closed; so is r_u because
F_A^+=0 gives d_A^+d_AH_u=[F_A^+,H_u]=0. Let P_V be orthogonal
projection to V. It annihilates d_AH_u since V lies in ker d_A^*.
Therefore a(u)=P_V r_u is the harmonic class of the actual derivative.
Coulomb slice gauge fixing for this smooth family removes exact terms
using the complement of parallel gauge generators. The slice/tube
input above ensures this before quotienting; a residual U(1) choice
only conjugates the construction. Thus a(u) is also the first derivative
of a slice family and meets (2) for every real parameter curve.

Product hyperholomorphicity uses the same R=I,J,K in both factors:
R_F(Ru,Rt)=R_F(u,t). Substituting -Rt for t gives
r_{Ru}(t)=-r_u(Rt)=R_c r_u(t). The harmonic subspace is R_c-invariant
and R_c is orthogonal, so its orthogonal complement is invariant too.
Consequently P_V commutes with R_c and

\[
 a(Ru)=R_c a(u),\qquad Q(a(u))=0.                    \tag{6}
\]

This is the required actual-family bridge. It uses neither a smooth
coarse quotient nor stable restrictions nor an assumed immersion.
It does not assert that r_u itself is harmonic. A quaternionic map
from the four-real-dimensional parameter tangent is either zero or
injective, but this argument does not decide which occurs. Even if
injectivity were established separately, W shows that equations (6)
have injective solutions. Additional global constraints might reject
those solutions; equations (6) alone do not.

L093's equality conclusion, including acyclic actual images, remains
unchanged. No germ-realization or full mixed-tensor reconstruction is
inferred from this necessary compatibility. The proposed universal
primitive Hodge realization remains entirely unresolved by this test.

**Separate critical audit, 2026-10-12 (step 240).** The stated
compatibility and conditional family bridge survive. This is
EXPLORATION / REPRODUCTION: verification of the existing argument,
with no substantive error, stronger obstruction or existence result.
The approved primary coverage above is reused. In particular the
unitary slice is imported from Diez--Rudolph, not inferred from the
complex gauge slice of Buchdahl--Schumacher.

Here is an explicit check of the real harmonic action in the convention
used in (3)--(6). At a point choose a normal real orthonormal frame
f_0,...,f_3. For an adjoint-valued real one-form a set

\[
 C_0(a)=\sum_i(\nabla_{f_i}a)(f_i),\qquad
 C_R(a)=\sum_i(\nabla_{f_i}a)(R f_i).
\]

These are tensorial contractions, so the choice of normal frame loses
no derivative terms. The quaternionic structures are parallel.
One has d_A^*a=-C_0(a) and
\(\langle d_Aa,\omega_R\rangle=C_R(a)\), with contraction only in
the form indices. The latter identity follows by antisymmetrizing:
\(\frac12\sum_i(d_Aa)(f_i,Rf_i)=C_R(a)\).
The three omega_R span the self-dual forms pointwise. Hence membership
in V is precisely the vanishing of these four contractions. For
S,R in {I,J,K}, with SR=-delta_SR+sum_T epsilon_SRT T,

\[
 C_0(S_c a)=-C_S(a),\qquad
 C_R(S_c a)=\delta_{SR}C_0(a)
                  -\sum_T\epsilon_{SRT}C_T(a).
\]

Thus S_c preserves V. Direct composition gives
I_c J_c a=a composed with JI=-a composed with K=K_c a;
the other quaternionic relations and orthogonality follow likewise.
This verifies the real operator used for harmonic projection, without
depending on an unspecified identification of cohomology actions.

For completeness, the real/Dolbeault bridge uses the skew-adjoint
reality condition, not coefficientwise complex conjugation alone.
Writing a=b-b^* with b=a^{0,1}, d_A^+a=0 gives
bar-partial_A b=0 and Lambda d_Aa=0. The conjugate (2,0) equation
is automatic. The coefficient Kahler identities give
\(\bar\partial_A^*=-i[\Lambda,\partial_A]\) and
\(\partial_A^*=i[\Lambda,\bar\partial_A]\).
If x=bar-partial_A^* b and y=partial_A^* b^*, the two remaining
equations are x-y=0 and i(x+y)=0, hence x=y=0. Conversely a
harmonic b and its adjoint give both equations. This proves both
directions of the real-linear identification. Since I_c acts by i
on (0,1)-forms, its complex structure is exactly the one assigning
the stated weights. J_c anticommutes with I_c and commutes with the
circle, so it exchanges those weights. The parallel diagonal line
has H^1(O_S)=0; the two off-diagonal dimensions are 26, not 13.
The resulting real dimension is 104 and quaternionic dimension 26.

Smooth gauge choice does not require a free gauge action. Work in a
sufficiently high Sobolev completion of the imported unitary slice and
restrict the infinitesimal gauge variable to the L2 orthogonal
complement of ker d_A on zero-forms. For every one-form c,
d_A^*c is perpendicular to ker d_A. The derivative in that variable
of the Coulomb equation d_A^*(g dot A_y-A)=0 is, up to the chosen
gauge sign, d_A^*d_A on that complement. It is invertible there.
The slice's implicit-function construction therefore gives a smooth
local choice g(y), with g(y_0)=1, for this already smooth family of
connections. Elliptic regularity supplies smooth spatial coefficients.
This is the local gauge choice inside the cited tube, not a lift of a
coarse quotient map. Its derivative differs from dot A_u by d_A s_u;
it is Coulomb and d_A^+-closed, so equals P_V dot A_u. The parallel
U(1) has not been removed. A different central stabilizer choice
conjugates the derivative, the quaternionic action and Q together.

The determinant connection is flat: Pic^0(S x S)=0 and integral
c_1(F)=0 trivialize the holomorphic determinant, and its induced HE
connection has zero curvature. Choose unitary determinant-preserving
identifications over the parameter ball. The central HE connection
can be identified with A by uniqueness for the split polystable
bundle, using an isometry of the chosen HE metrics. Formula (5)
then identifies the actual curvature derivative with the slice
derivative after projection. The identity d_A^+d_AH_u=0 uses ASD,
not irreducibility. Orthogonal real harmonic invariance proved above
justifies commuting P_V with R_c in (6). A smooth actual parameter
curve supplies the second derivative in (2), so Q vanishes on each
actual tangent even at this reducible central fibre.

Finally, multiplication of two off-diagonal matrices is diagonal;
cyclic trace and odd one-form degree give Tr(a wedge a)=0. Thus
the quadratic source is in the real diagonal adjoint line. All
operators and orthogonal projections preserve this splitting, so
no off-diagonal obstruction component is missed. In the diagonal
cokernel, d^{+*}phi=0 for a self-dual phi implies d^*phi=0 and
d phi=0. The harmonic self-dual dimension on a K3 is three. In the
ordered frame used in (3), the forms are
omega_I=theta_0 theta_1+theta_2 theta_3,
omega_J=theta_0 theta_2-theta_1 theta_3, and
omega_K=theta_0 theta_3+theta_1 theta_2 (products here are wedges).
These check all three signs in (3). Cyclic trace gives exactly the
factor two in (4). The equal norms in G(Tv,Iv) cancel; the other
three pairings vanish by orthogonality. Since T commutes with every
quaternionic operator and P^*Q is again such an operator, the displayed
T(W)-perpendicular-to-W argument checks every w and every polarized
cross term, not just the four basis vectors. All components of Q|_W
are therefore zero. Neither the residual quotient nor any higher-order
obstruction was calculated. In particular this audit still leaves the
actual derivative possibly zero and proves no integration of W.

## Mathlib

Full matching coverage of this reducible ASD/harmonic-family
specialization: **not checked**. Unknown availability is not absence.
The primary slice, coefficient and RR inputs are cited above; the
explicit representation, curvature expansion and all-component
vanishing are proved here. No numerical certificate or preview is used
as mathematical evidence.

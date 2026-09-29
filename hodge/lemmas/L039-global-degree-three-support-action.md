# L039 — Global degree-three support action for stable sheaf families

## Hypotheses

Let X be a smooth projective complex K3 surface and H an ample
polarization. Let B be a smooth connected projective complex
surface, and write p:B x X -> B and q:B x X -> X.
Let F be a coherent B-flat sheaf whose fibres are H-Gieseker
stable torsion-free sheaves with Mukai vector

\[
v(F_b)=(2,0,-1).
\]

Thus det(F_b)=O_X, c_2(F_b)=3 and chi(F_b)=1. Stability here
means Gieseker stability; slope stability is not assumed.
For the universal-family application, let H be v-generic,
M=M_H(2,0,-1), P an untwisted universal sheaf on M x X, and
F=(f x id_X)^*P for an algebraic morphism f:B -> M.
The prior assessment supplies existence of M and P, not f.

Use Markman's equations (29),(32)--(33): (0,t,0)^vee=(0,-t,0).
Write T(X)=NS(X)_Q^perp for the cup-product transcendental space.
In the intended application B=X=S, T has rank eighteen and
End_Hdg(T)=Q(zeta_7+zeta_7^(-1)). Neither this field hypothesis
nor a dense locus of distinct support points is needed below.

## Conclusion

Every actual fibre hull is trivial:

\[
F_b^{**}\simeq O_X^{\oplus2}.
\tag{1}
\]

There is a rank-two vector bundle V on B and a canonical
evaluation exact sequence

\[
0\longrightarrow F\longrightarrow p^*V
 \longrightarrow Q\longrightarrow0,
\qquad
V=\bigl(\mathcal H^0(Rp_*R\mathcal Hom(F,O_{B\times X}))\bigr)^\vee.
\tag{2}
\]

The sequence commutes with arbitrary base change on B.
Q is B-flat, is supported finitely over B, and has length three
on every fibre. The middle term is a simultaneous hull of F:
its fibre map is the actual double-dual inclusion. On the smooth
product it also identifies F^{**} with p^*V.
No flatness of the structure sheaf of Supp(Q) is asserted.

Let Gamma_Q=[Q]_2 be the dimension-two associated cycle, with
generic-stalk lengths as multiplicities. It is effective and
p_*Gamma_Q=3[B]. Its fibre support cycles define the usual
support morphism Phi_Q:B -> X^{(3)}. In CH^2(B x X)_Q,

\[
\operatorname{ch}_2(F)=p^*\operatorname{ch}_2(V)-[\Gamma_Q],
\qquad
c_2(F)=p^*c_2(V)+[\Gamma_Q].
\tag{3}
\]

Consequently, for every t in H^2(X,Q),

\[
p_*\bigl(q^*t\smile\operatorname{ch}_2(F)\bigr)
 =-p_*\bigl(q^*t\smile[\Gamma_Q]\bigr).
\tag{4}
\]

For the pulled-back universal family this gives

\[
f^*\theta_v(0,t,0)
 =p_*\bigl(q^*t\smile[\Gamma_Q]\bigr).
\tag{5}
\]

All statements include collisions and families entirely outside
the distinct-three-point locus. They give a necessary global
support description and the action of an existing stable map.
They do not assert that an arbitrary degree-three support
morphism has a stable lift, or construct a non-scalar action.

## Proof

**Imported framework and the specialization.**
O'Grady, *Moduli of sheaves and the Chow group of K3 surfaces*,
[arXiv:1205.4119v2, Proposition 4.2 and Remark 4.3,
pp. 11--12](https://arxiv.org/pdf/1205.4119v2#page=11),
supplies the generic three-distinct-point model.
Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
[the online 281-page text, Theorem 8.2.11, Proposition 8.2.13
and Lemma 8.2.14, printed pp. 191--193](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=202),
supplies the slope-moduli and support-cycle framework.
Its graded double dual does not by itself prove (1) or (2).
Import those tools and specialize the actual sheaf, as follows.

**Every stable fibre has the actual trivial hull.**
Temporarily write F for one fibre. A nonzero section O_X -> F
would be injective, since F is torsion-free. The reduced Hilbert
polynomials, normalized by rank, are

\[
p_F(m)=\tfrac12H^2m^2+\tfrac12,\qquad
p_{O_X}(m)=\tfrac12H^2m^2+2.
\]

Stability therefore gives H^0(F)=0. Riemann--Roch and Serre
duality, with K_X=O_X, give

\[
1=\chi(F)=-h^1(F)+h^2(F),\qquad
h^2(F)=\dim\operatorname{Hom}(F,O_X)>0.
\]

Choose a nonzero map F -> O_X. Its image is I_W(-D), for
an effective divisor D and a zero-dimensional subscheme W.
The rank-one kernel K has determinant O_X(D), since det(F)=O_X.
Gieseker stability implies slope semistability, so
mu_H(K)=D.H<=mu_H(F)=0. Ampleness forces D=0.
The kernel is therefore I_Z for a zero-dimensional Z.
Here a rank-one torsion-free sheaf is its determinant tensored
with an ideal, and a line bundle with c_1=0 is trivial on a K3
surface: H^1(O_X)=0 makes the first Chern map injective.
We have the exact sequence

\[
0\longrightarrow I_Z\longrightarrow F
 \longrightarrow I_W\longrightarrow0,
\qquad |Z|+|W|=3.
\tag{6}
\]

The length equation follows by adding Chern characters.
The reduced Hilbert polynomial of I_Z has constant term 2-|Z|.
Its strict inequality with p_F gives 2-|Z|<1/2, hence
|Z|>=2 and |W|<=1. This bound uses stability of the actual F.

Set G=F^{**}. Reflexive sheaves on a smooth surface are locally
free, so G is a rank-two bundle with determinant O_X.
The map F -> O_X extends uniquely to G -> O_X: outside finitely
many points F=G, and Hartogs extension applies to G^vee.
Its image is I_Y, with I_W contained in I_Y. It has no
divisorial factor because the two maps agree in codimension one.
Thus |Y|<=|W|<=1.

The kernel of G -> I_Y is a line bundle. Locally, the ideal I_Y
has depth at least one on a regular surface; the depth lemma
makes this kernel have depth two, and Auslander--Buchsbaum
makes it free. Its determinant is O_X, so

\[
0\longrightarrow O_X\longrightarrow G
 \longrightarrow I_Y\longrightarrow0.
\tag{7}
\]

If |Y|=1, the map H^0(O_X) -> H^0(O_Y) is an isomorphism.
Since H^1(O_X)=0, H^1(I_Y)=0. Serre duality for coherent
sheaves on this smooth surface gives
Ext^1(I_Y,O_X)=H^1(I_Y)^vee=0.
Sequence (7) would split as O_X direct sum I_Y, which is not
locally free at Y. This contradicts the local freeness of G.
Thus Y is empty. Now H^1(O_X)=0 splits (7) as O_X^2.
This proves (1), including every boundary fibre.

Every map F -> O_X similarly extends to G. It follows that
Hom(F,O_X) has dimension two. Combining this with chi(F)=1,
H^0(F)=0 and Serre duality gives

\[
\bigl(\dim\operatorname{Ext}^i(F,O_X)\bigr)_{i=0,1,2}
=(2,1,0),\qquad
(h^0(F),h^1(F),h^2(F))=(0,1,2).
\tag{8}
\]

**Constructing the family hull, rather than assuming it.**
Return to F on B x X. This product is smooth, so F is perfect.
Its derived dual is perfect as well. The product projection p
is flat and proper. Import the perfect-pushforward and arbitrary
base-change theorem
[Stacks, Lemma 36.35.10, Tag 0DJT](https://stacks.math.columbia.edu/tag/0DJT).
It applies to

\[
K=Rp_*R\mathcal Hom(F,O_{B\times X}).
\]

Indeed any perfect complex on this product is B-perfect because
p is flat. Since F is B-flat, its derived restriction to a fibre
is the ordinary F_b. Dualizing a perfect complex commutes with
derived restriction. The derived fibres of K thus have the
Ext dimensions (8).

Here is the needed local-freeness check; constant pointwise
hulls alone would not be enough. Import the local normal form
for a perfect complex
[Stacks, Lemma 15.77.7, Tag 0BCD](https://stacks.math.columbia.edu/tag/0BCD).
Near any closed point of B it represents K by

\[
O_B^{\oplus2}\longrightarrow O_B
\]

in degrees zero and one. At every closed point of that
neighbourhood the kernel on the residue field has dimension two,
by (8). The differential therefore vanishes at all closed points.
B is reduced and of finite type over C, so its matrix is zero.
Hence D=H^0(K) is locally free of rank two, H^1(K) is locally
free of rank one, and their formation commutes with arbitrary
base change. No global splitting of K is needed.

Since the derived sheaf dual has no negative cohomology,
\(D=p_*\mathcal Hom(F,O_{B\times X})\). Adjunction and evaluation
give the canonical map

\[
F\longrightarrow p^*D^\vee=p^*V.
\]

Its fibre is evaluation against all of Hom(F_b,O_X).
Under G_b=O_X^2 this is exactly the inclusion
F_b -> H^0(G_b^vee)^vee tensor O_X=G_b. Thus it is injective
on every fibre, and its fibre cokernel has length three.

For completeness, fibre injectivity gives injectivity on the
product before the short-exact-sequence flatness criterion is
applied. At a closed product point, both source and target are
B-flat. Their associated graded modules for the maximal ideal
of the base are the residue-field fibres tensored with the
graded base ring. The associated graded map is injective in
each degree, because the fibre map is injective. A section
in the kernel therefore belongs to every power of that ideal
times F; Krull intersection in the Noetherian local product
ring makes it zero. Any nonzero coherent kernel would have a
closed support point, so there is no kernel anywhere.

Now import Huybrechts--Lehn,
[Lemma 2.1.4, printed p. 33](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=45):
the fibrewise injections in this exact sequence, with flat
middle term, make Q B-flat. Its support is proper and has finite
fibres over B, hence is finite over B. The sequence remains
exact after arbitrary base change, and the base-changing
relative Hom construction identifies its middle term with the
fibrewise hulls after that base change. This proves (2).

The support of Q has codimension at least two in B x X.
The two sheaves F and p^*V agree off that support. Since the
product is smooth and p^*V is reflexive, taking the double
dual identifies F^{**}=p^*V. The assertion about simultaneous
hulls follows from the constructed sequence, rather than
an inference from constancy of fibre Hilbert polynomials.

**The weighted cycle and action across all strata.**
Import the associated-cycle and leading Chern-character
theorems from Fulton, *Intersection Theory*, second edition
(1998), [Theorem 18.3(3),(5), pp. 353--354, and Example
18.3.11, p. 363](https://djvu.online/file/87GFN2nbfbdF7).
On the smooth fourfold B x X, a sheaf supported in codimension
at least two has ch_0=ch_1=0 and ch_2 equal to its
dimension-two cycle, with generic-stalk lengths.
Applying this to Q and adding Chern characters in (2) gives
the first equation of (3).
Also c_1(F)=p^*c_1(V), so the identity
c_2=c_1^2/2-ch_2 gives its second equation.

The generic fibre of Q has length three, so the weighted
degree of Gamma_Q over B is three, including residue-field
degrees; equivalently p_*Gamma_Q=3[B].
The usual support morphism for a flat length-three sheaf family
is the one in Huybrechts--Lehn, section 8.2, the proof of
Theorem 8.2.11 and Lemma 8.2.14 cited above. Locally trivialize
V to obtain a family in Quot(O_X^2,3) and use its support map
to X^{(3)}. These maps glue because changing the frame does
not change Q or its support cycle. This proves the assertion
about Phi_Q, without imposing a flat Fitting subscheme.

In (3), the term p^*ch_2(V) has no mixed component. For
t in H^2(X,Q), its product with q^*t pushes to zero: a
degree-two class on X cannot be integrated over the surface.
This proves (4) for all t, not just their transcendental parts.

Finally import the Mukai convention from Markman,
*On the monodromy of moduli spaces of sheaves on K3 surfaces*,
[arXiv:math/0305042v3, equations (29),(32)--(33),
pp. 22--23](https://arxiv.org/pdf/math/0305042v3#page=23).
For x=(0,t,0) we have x in v^perp and x^vee=-t.
The degree-two universal pushforward is

\[
-p_*\bigl(q^*t\smile\operatorname{ch}_2(F)\bigr).
\]

The rank term involving t sqrt(td_X)_4 vanishes in H^6(X).
An untwisted universal family has similitude one.
Ordinary and derived pullback of P along f x id agree,
because P is flat over M. Chern characters and integration
along the product projection commute with this pullback.
Equation (4) therefore proves (5).

Tensoring F with p^*L replaces V,Q by V tensor L,Q tensor p^*L.
It preserves their support multiplicities and changes ch_2(F)
only by classes from B, since c_1(F) is already from B.
Thus (4)--(5) retain the usual base-line-bundle ambiguity.
The computation uses the actual quotient and a Chern-character
identity on the product, not a pointwise CH_0 identity or
a determinant identity asserted to control transcendental classes.

This is a reproduction and application of named stability,
duality, flatness, cycle and Mukai tools. The all-fibre hull and
relative evaluation are the identified specialization beyond
the generic presentation, followed by its action calculation.
The saved assessment did not match the full statement to an
inspected theorem; no originality or progress beyond the checked
literature is claimed. On the cubic-RM test a new stable map
still needs a non-scalar support action. No algebraic class or
transverse surface is supplied merely by this reduction.

## Mathlib

Coverage: **not checked** for this full statement or its
stability, hull, relative Hom, finite-support and Mukai inputs.
No matching Mathlib theorem or absence from checked Mathlib
sources is asserted.
The direct O'Grady, Huybrechts--Lehn, Stacks, Fulton and Markman
citations above are supporting results, not matches for the
full all-fibre family/action statement. Riemann--Roch, Serre
duality, Hartogs extension, the depth lemma,
Auslander--Buchsbaum and Krull intersection are the named
standard supporting theorems used in the specialization.

# L090 — Determinant cup-square excludes the prescribed common kernel

## Hypotheses

Assume precisely the conditional data of L079. Thus S is its marked
projective K3 surface, X=S_1 x S_2 uses the identical fixed hyperkähler
metrics, h is the specified real Kähler class, and Omega=p_1^*h+p_2^*h.
Write e_1=eta tensor 1, e_2=1 tensor eta with integral_S eta=1.
The class tau_D is the full integral mixed tensor of that setting,
not just its transcendental projection. Suppose F is locally free
holomorphic of rank two, Omega-slope-polystable, with integral c_1(F)=0
and ch_2(F)=-9e_1-10e_2-tau_D. Its initial higher characters and
K-class are unrestricted. This is the correction pair (-13,-14).

Use L079's actual images G=R^1p_2*F and H=R^1p_1*F, their everywhere
odd concentration and base change, and their determinant/relative-Serre
symmetric forms. In particular their common trivial multiplicity is
t=1 or 2 and the forms restrict perfectly to those trivial parts.
No independently constructed block is identified with either image.

## Conclusion

No F satisfies these hypotheses: both t=1 and t=2 contradict the
rank-two determinant cup-square identity on H^1(X,F). This excludes
the specified common-kernel recipe, including all L079 image branches.
It does not exclude the individual image blocks, topological bundles,
other Chern data or other representatives of a Hodge class. It produces
no algebraic cycle or transverse transport and does not resolve the
Hodge conjecture. This is a NEGATIVE / REPRODUCTION specialization of
the assessed coefficient-cohomology and duality tools, preserved by the
separate critical audit below; no originality claim is made.

## Proof

**One determinant and one global product.** L079 proves det(F)=O_X:
H^1(X,O_X)=0 and the exponential sequence make the integral first
Chern map injective. Fix one holomorphic trivialization and its
alternating perfect wedge A:F tensor F -> O_X. Use this same A
in both relative forms. Set V=H^1(X,F) and define

\[
 B(u,v)=A_*(u\smile v)\in H^2(X,O_X).
\tag{1}
\]

Import the coefficient Dolbeault theorem from Demailly,
*L2 vanishing theorems for positive line bundles and adjunction theory*,
[alg-geom/9410022v3, 28 February 1995, Section 1.A (1.1)--(1.3),
printed pp. 4--5](https://arxiv.org/pdf/alg-geom/9410022v3).
X is a complex manifold and F is holomorphic locally free, so its
smooth (0,*) coefficient resolution is locally exact and acyclic.
The coefficient wedge on that resolution is a morphism of complexes:
bar-partial satisfies its graded Leibniz rule since A is holomorphic.
In degree zero it is A itself. The resolution comparison therefore
computes the derived/coherent cup product, as in
[Stacks 20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3).
Projective GAGA identifies analytic and algebraic coherent cohomology.
These standard comparison theorems are imported, not reproved.

Represent u by a globally bar-partial-closed smooth F-valued (0,1)-form
alpha. In any local holomorphic frame f_1,f_2 with A(f_1,f_2)=1,
write alpha=f_1 a+f_2 b for ordinary smooth (0,1)-forms a,b. Then

\[
 A(\alpha\wedge\alpha)=a\wedge b-b\wedge a=2a\wedge b,
 \qquad (2a\wedge b)\wedge(2a\wedge b)=0.
\tag{2}
\]

The last identity follows by moving the second a past b and using
a wedge a=0. These are scalar forms with commuting complex coefficients.
The determinant-one frames exist locally and the resulting scalar
(0,2)-form is globally defined and closed, so its exterior square
vanishes globally as a form. The scalar Dolbeault product computes
the scalar cohomology product. Consequently

\[
 B(u,u)\smile B(u,u)=0\quad\hbox{in }H^4(X,O_X)
 \quad\hbox{for every }u\in V.
\tag{3}
\]

For distinct inputs the coefficient alternating sign and the degree-one
cohomology sign cancel, making B symmetric. This agrees with
[Stacks 15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN).
Equation (2) does not assert B(u,u)=0, use harmonic multiplication,
or assume F has a flat connection.

**Both actual restriction comparisons.** Choose nonzero
theta_i in H^2(S_i,O_{S_i}), and put x=p_1^*theta_1, y=p_2^*theta_2.
K3 coherent cohomology and the cup-defined Künneth isomorphism give

\[
 H^2(X,O_X)=\mathbb Cx\oplus\mathbb Cy,\qquad
 H^4(X,O_X)=\mathbb C(x\smile y),\qquad
 x^2=y^2=0,\quad x\smile y\ne0.
\tag{4}
\]

Import [Stacks 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN):
the projective factors are quasi-compact and quasi-separated, the
coefficients are O, and Tor-independence holds over the affine field
base C. H^1(S_i,O)=0 removes the cross term in degree two, and the
surface dimension removes H^4(S_i,O). Thus the stated hypotheses
give precisely (4), with even-degree commuting x and y.

Write B(u,u)=a(u)x+b(u)y. L079's single-row Leray sequences give
canonical isomorphisms

\[
 \ell_G:V\simeq H^0(S_2,G),\qquad
 \ell_H:V\simeq H^0(S_1,H).
\tag{5}
\]

Here Leray is [Stacks 20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2).
For z in S_2, evaluation of ell_G(u), followed by the actual
base-change isomorphism G_z=H^1(S_1,F|_{S_1 x {z}}), is restriction
of u. Indeed the Leray edge map is the map from global cohomology
to sections of the sheaf of relative cohomology; evaluation followed
by base change is induced by the same restriction map on a resolution.
Equivalently the counit map defining the edge and base-change maps
gives this composite. The corresponding statement holds for ell_H
on every opposite fibre, using its own actual base-change isomorphism.

Restriction also preserves (1). In the smooth resolution it pulls
back alpha and the coefficient wedge A, so it pulls back their scalar
product. This is the derived composition/base-change compatibility in
[Stacks 20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6) and
[20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99).
These comparisons apply to the locally free coefficient pullback;
the assertion that the coefficient base-change maps are isomorphisms
comes separately from L079. Pullback to S_1 x {z} sends x to theta_1
and y to zero. Hence the determinant cup of the restricted class
is a(u)theta_1. On {w} x S_2 it is b(u)theta_2.

Choose the holomorphic two-forms sigma_i used in L079's relative
canonical trivializations and set

\[
 c_i=\operatorname{Tr}_{S_i}(\theta_i\smile\sigma_i)\ne0.
\tag{6}
\]

Multiplication by the nowhere-zero sigma_i identifies O_{S_i} with
omega_{S_i}; Serre trace is an isomorphism H^2(omega_{S_i}) -> C.
This proves the nonvanishing in (6), without any real positivity or
phase convention. Use the smooth proper relative dimension-two
duality of [Stacks 48.19 (2),(9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT), and the
cup/trace pairing [48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q).
The projections are smooth proper over the Noetherian S_i, and F is
locally free. L079 already applies these inputs to construct the
actual perfect forms Q_G and Q_H with exactly wedge, sigma and trace.
The coefficient analytic realization is also Demailly, cited above,
Section 4.A (4.3)--(4.4'), printed pp. 27--28. Consequently (5) and
the preceding fibre comparisons give

\[
 Q_G(\ell_Gu,\ell_Gu)=c_1a(u),\qquad
 Q_H(\ell_Hu,\ell_Hu)=c_2b(u).
\tag{7}
\]

The left sides are constant scalar sections on their connected
projective bases, so evaluation on any fibre computes these equalities.
Choosing another nonzero normalization of a relative form changes
the corresponding c_i by a nonzero scalar and cannot alter the argument.
No identification between the two image bundles or their bases is
substituted for the two maps from the same V.

**Simultaneous nonvanishing, including t=2.** By L079 each image is
polystable with exactly t trivial lines, all other stable summands
having zero H^0. Thus evaluation identifies its global sections with
the fibre of its trivial isotypic part. That part is orthogonal to
the rest and its restricted symmetric form is perfect. Its matrix
is constant, so it induces a nondegenerate symmetric bilinear form
on the t-dimensional space of global sections. Pulling back by (5)
gives two nondegenerate symmetric forms on the same V, dim V=t.
Their quadratic polynomials q_G and q_H are the left sides of (7).
Each is nonzero: if q vanished identically, polarization
Q(v,w)=(q(v+w)-q(v)-q(w))/2 would make Q zero.

For t=1, choose a coordinate z on V. Nondegeneracy gives
q_G=d_G z^2, q_H=d_H z^2 with both d_i nonzero, so every nonzero
vector has both quadratic values nonzero. For t=2, choose v with
q_G(v) nonzero and w with q_H(w) nonzero. The polynomial
q_G(v+s w) is nonzero because its constant term is q_G(v); the
polynomial q_H(v+s w) is nonzero because its leading coefficient
is q_H(w). Each has at most two roots. Choose s in C outside their
finite union to obtain u=v+s w with both values nonzero. This
argument permits isotropic lines for either complex quadratic form;
no anisotropy or positive definiteness is assumed.

For that u, (6)--(7) give a(u)b(u) nonzero. But (4) gives

\[
 B(u,u)^2=2a(u)b(u)\,x\smile y\ne0,
\tag{8}
\]

contradicting (3). Both branches are excluded. Only L079's actual
trivial-part forms and Leray maps, not a lift of a direct-image
projector, enter this contradiction. No index compatibility or
individual-block existence is promoted to common-kernel existence.

**Separate critical audit, 2026-10-11 (step 222).** The exact exclusion
survives. This audit uses the separately approved coefficient, counit
and trace coverage; it finds no substantive error and asserts no
stronger exclusion. Here are the load-bearing comparisons in detail.

First, integral determinant triviality is essential: the assumed
integral c_1 and H^1(O_X)=0 give one actual holomorphic wedge A. A
change between determinant-one holomorphic frames preserves the scalar
form in (2). The coefficient forms a,b have exterior degree one and
ordinary complex-valued coefficients, so a wedge a and b wedge b
vanish even though their coefficients vary. Consequently the scalar
four-form in (2) is zero before passing to cohomology. Holomorphicity
of A makes the scalar two-form closed. Replacing alpha by a cohomologous
representative does not change its scalar cup class, by the resolution
product comparison already cited. There is no assumption of flatness,
of multiplicative harmonic projection, or of holomorphic global frames.
This verifies (3) for every u, rather than only for classes chosen
fibrewise. The two interchange signs make (1) symmetric, not alternating.

Next fix either projection p:X->B and a closed point j:z->B, with
fibre inclusion i:X_z->X and fibre projection p_z:X_z->z. Put
E=R^1p_*F, so L079 supplies P=Rp_*F canonically identified with E[-1].
This identification is by the single nonzero cohomology sheaf, not by
a choice of splitting of a multirow spectral sequence. Derived
composition, [Stacks 20.13.1, 01EZ](https://stacks.math.columbia.edu/tag/01EZ),
identifies u with a morphism O_B->P[1], hence with a global section
s:O_B->E. Pulling this morphism back to z gives exactly s(z).
There are no extra coefficient Tor terms: E is locally free, F is
locally free, and p is flat. L079's coefficient base-change isomorphism is

\[
 Lj^*P\longrightarrow Rp_{z*}Li^*F
       =R\Gamma(X_z,F|_{X_z}).
\]

By [Stacks 20.28.3, 08HY](https://stacks.math.columbia.edu/tag/08HY),
this map is adjoint to the pullback of the counit Lp^*Rp_*F->F.
The morphism representing u under derived composition is the composite
O_X->Lp^*P[1]->F[1]. Pulling this composite back by i gives the
same counit composite as first pulling s back by j and then using
the displayed base-change map. Thus s(z) maps to i^*u in
H^1(X_z,F|_{X_z}). This proves the two evaluation assertions of (5)
for the actual maps, with p=p_2 and E=G, and with p=p_1 and E=H.
The vector u has not been replaced or independently chosen in either
direction. The cup-base-change compatibility in 20.31.8 then gives
the determinant cup of i^*u as the restriction of B(u,u). Equivalently,
pullback of the same smooth alpha and wedge A gives this equality.

For clarity the trace comparison also uses actual transformations.
For either p, take its relative form sigma and the morphism

\[
 P\mathbin{\otimes}^{\mathbf L}P
 \longrightarrow Rp_*\mathcal O_X
 \xrightarrow{\ \sigma\ } Rp_*\omega_p
 \xrightarrow{\ \operatorname{Tr}_p\ }\mathcal O_B[-2].
\]

The first arrow is cup followed by A. Substituting P=E[-1] and
taking the degree-two component defines exactly L079's Q_E.
The fibre square is cartesian and Tor independent because p is flat;
the closed-point map j itself need not be flat. All schemes are
Noetherian, quasi-compact and quasi-separated; p is proper flat of
finite presentation. Thus [Stacks 48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB)
makes the right-adjoint base-change transformation an isomorphism,
and [48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J)
identifies the pulled-back relative trace with the fibre trace.
The smooth dimension-two dualizing identification is
p^!O_B=omega_p[2], as cited above. Apply these statements in the
bounded coherent/perfect setting here; no unqualified internal-Hom
claim outside D_QCoh is needed from 48.3.6. Pullback of sigma is the
chosen sigma_i on the relevant fibre. Cup and A commute with the
same base change. It follows that

\[
 Q_E(s,s)(z)=\operatorname{Tr}_{X_z}
       \bigl(\sigma_i\, A_*((i^*u)\smile(i^*u))\bigr).
\]

The cup/trace convention here is the definition of Q_E in L079,
so it introduces no further sign choice. Any alternate duality
normalization would only multiply this entire form by a nonzero
constant. On the p_2 fibre, i^*x=theta_1 and i^*y=0; on the p_1
fibre the reverse holds. Multiplication by sigma_i is an isomorphism
O_{S_i}->omega_{S_i}, and Serre duality identifies the trace on
H^2(omega_{S_i}) with the dual of H^0(O_{S_i})=C. Hence both c_i
in (6) are nonzero. Evaluation proves (7); the resulting functions
are constant because the bases are connected and projective. Neither
positivity nor equality of the two trace constants is required.

Finally, write either polystable image as T plus W, where T=O^t
is its full trivial isotypic part. L079's stable-summand argument gives
H^0(W)=H^0(W^vee)=0. Therefore the cross blocks of Q_E between T
and W vanish: they are morphisms O^t->W^vee or W->O^t. Since Q_E
is perfect, its T block is perfect. Evaluation identifies H^0(E)
with T_z, and the matrix of this block is constant. Pullback through
each actual Leray isomorphism therefore gives a nondegenerate
symmetric form on the same V. The nonzero dimension is substantive:
L079 obtains chi(G)=2 and h^0(G)=h^2(G)=t, whence
h^1(G)=2t-2>=0 and t>=1; its retained cases are t=1,2.

In t=1 the nonzero quadratic coefficients are immediate. In t=2
the chosen line v+s w in the proof has a nonzero constant coefficient
for q_G and nonzero quadratic coefficient for q_H. Thus neither
polynomial vanishes identically, even if either form has isotropic
lines or v,w happen to be dependent. Avoiding their finitely many
roots gives the same u with both values nonzero. Scalar Kunneth
identifies x cup y with theta_1 tensor theta_2, a nonzero generator;
its even degrees give the factor 2 in (8), nonzero over C. This
contradicts the already verified identity (3).

All uses of polystability, cohomology concentration and perfect forms
above are supplied by L079 for its exact conditional F. Individual
block constructions, real index lifts and projector lifts are not
premises. The direct local mathematical input remains only L079.
The audit is EXPLORATION / REPRODUCTION: it confirms the recorded
negative specialization without a new mathematical advance, new
correction pair, common-kernel construction or Hodge-class realization.

## Mathlib

Full matching coverage for the coefficient Dolbeault identity, its two
actual relative Serre comparisons, and this common-kernel exclusion
has not been checked. Supporting elementary exterior algebra alone
would not verify those geometric comparisons. Unknown coverage is
not absence; the cited named theorems are imported mathematical inputs.

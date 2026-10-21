# L109 — Equality-family local duality and the two point defects

## Hypotheses

Retain the entire conditional family and corrected conclusions of L108:
on the smooth projective K3 base B, let p:S_1 x B -> B,
V=End_0(F), C=Rp_*V, A_i=R^ip_*V, M=A_1, E=M** and Q=E/M.
Thus F is locally free of rank two, polystable at the fixed real
product polarization, with integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D, retaining the full tensor and common metric.
In particular A_0=0, M is torsion-free, E is locally free of rank
fifty with L108's extended nondegenerate alternating Serre form,
and A_2 and Q have support in the finite, possibly empty split locus Z.
The actual family F and any point of Z are hypothetical. Retain the
chosen fibre K3 form and L108's normalization of the Serre pairing.
No reduced structure or multiplicity is assigned to either defect.

For a closed z in Z set R=O_{B,z}, C_R=C_z, M_z=(A_1)_z,
W_z=(A_2)_z and use E_z and Q_z for the hull and quotient stalks.
In the proof omit the stalk subscripts. For a finite-length R-module T write

\[
 T^\dagger=\operatorname{Ext}^2_R(T,R),\qquad
 \mathbb D K=R\operatorname{Hom}_R(K,R).
\]

This finite-length dual has the same length as T; it is not an
identification with T or with its derived residue-field cohomology.

## Conclusion

The actual cup/trace duality and truncation maps give an exact sequence

\[
 0\longrightarrow M\xrightarrow{b}M^*
 \xrightarrow{\delta}W^\dagger\xrightarrow{\gamma}W
 \xrightarrow{\epsilon}\operatorname{Ext}^1_R(M,R)
 \longrightarrow0.                                             \tag{1}
\]

Here M^*=Hom_R(M,R). Under the restriction isomorphism E^* ~= M^*,
b is the composite of M -> E and L108's extended symplectic
isomorphism E -> E^*. The other maps are specified below by the
actual truncation triangle and its dual; they are not arbitrary maps
between modules of equal length. Consequently (1) induces

\[
 0\longrightarrow Q\longrightarrow W^\dagger
 \xrightarrow{\gamma}W\longrightarrow Q^\dagger
 \longrightarrow0.                                             \tag{2}
\]

In particular, writing q_z=length(Q_z) and w_z=length(W_z),

\[
 q_z\leq w_z,\qquad
 \operatorname{length}(\operatorname{im}\gamma)=w_z-q_z.
                                                               \tag{3}
\]

Summing gives q<=w in L108, but supplies no upper bound for w+q
and no lower bound for c_2(N)/eta=800-w-q. The duality and ordinary
cohomology conditions used here, even together with the split-fibre
derived dimensions (1,52,1), admit the explicit local models below
with q=0 and arbitrarily large w. These models are not realizations
of F or of its actual Kodaira--Spencer derivative.

For Z empty, both defects vanish and the local assertions are vacuous;
globally C=E[-1] and L108's zero-defect value c_2(N)=800 eta remains.
There is no metric-extension, semistability, kernel-existence, cycle
or transport conclusion. The original local ADVANCE / REPRODUCTION
of the assessed framework survives the separate critical audit below.
That audit is EXPLORATION / REPRODUCTION: it finds no substantive error
or stronger conclusion and claims no progress beyond the checked tools
or a resolution of primitive Hodge realization. The duality-only
upper-bound route stops at (2)--(3).

## Proof

**Imported results and applicability.** Reuse the prior SPECIALIZE
assessment `drafts/literature/2026-10-15-equality-local-duality-defect-sequence.md`.
For smooth proper relative dimension two, import
[Stacks Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT):
p^!O_B=omega_{X/B}[2]. The chosen fibre two-form trivializes
omega_{X/B}. The perfect-pairing pushforward and its cup/trace map
are [Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
and the perfect-dual calculation in
[48.12.7, 0E4L](https://stacks.math.columbia.edu/tag/0E4L).
L108 gives perfectness of C and local freeness of V. On V the
matrix-trace form is nondegenerate: End(F)=O id direct sum End_0(F)
is an orthogonal splitting, and tr(id^2)=2 is invertible. Thus these
results apply to this actual coefficient, without local freeness of
the ordinary A_i at z. They give the adjoint isomorphism

\[
       \alpha:C_R[2]\xrightarrow{\sim}\mathbb D C_R.     \tag{4}
\]

It comes from relative cup product and trace, with pairing
C_R tensor^L C_R -> R[-2]. Multiply by the fixed nonzero scalar
used in L108 so its induced degree-one form on the puncture is
exactly L108's omega_E. This is a choice of normalization of (4),
not a numerical-trace compatibility assertion inferred from 0BRT.
We use v -> (u -> omega_E(v,u)) as the flat-map convention.
The positive [2] in (4) is essential.

Import [Stacks Proposition 10.110.1, 00O7](https://stacks.math.columbia.edu/tag/00O7)
for the regular-local resolution bound. The ring R is regular local
of dimension two, and torsion-free M has depth at least one: any
nonzero element of its maximal ideal is a nonzerodivisor on M.
Hence pd_R M<=1. For finite-length T, import
[Lemma 47.16.4, 0A7Q](https://stacks.math.columbia.edu/tag/0A7Q)
and the regular-local formula in
[Lemma 57.11.2, 0G23](https://stacks.math.columbia.edu/tag/0G23):

\[
 \mathbb D T=T^\dagger[-2],\qquad
 \operatorname{Ext}^i_R(T,R)=0\ (i\ne2).                 \tag{5}
\]

Regular local rings are Gorenstein by
[47.21.3, 0AWX](https://stacks.math.columbia.edu/tag/0AWX).
The finite-length scope of
[Matlis duality, 47.7.8, 08Z9](https://stacks.math.columbia.edu/tag/08Z9)
identifies T^dagger with its exact finite-length dual and preserves
length. For noncomplete R this statement is obtained on completion:
T and its finite-length dual already have their natural completed
module structures, Ext commutes with this flat completion for finite
modules, and completion preserves their lengths. No completion of
the geometric family or identification T^dagger=T is made.
These general results are imported, not reproved.

**Truncation and the maps.** Only H^1(C_R)=M and H^2(C_R)=W
are nonzero. Its canonical truncation triangle is

\[
 M[-1]\xrightarrow{i}C_R\xrightarrow{t}W[-2]
          \longrightarrow M.                            \tag{6}
\]

Dualizing (6) and using (5) gives

\[
 W^\dagger[0]\xrightarrow{\mathbb D t}\mathbb D C_R
 \xrightarrow{\mathbb D i}(\mathbb D M)[1]
 \longrightarrow W^\dagger[1].                          \tag{7}
\]

Here H^{-1}((DM)[1])=M^* and
H^0((DM)[1])=Ext^1_R(M,R), with no other cohomology because
pd M<=1. By (4), H^{-1}(DC_R)=M and H^0(DC_R)=W.
The cohomology sequence of (7) is exactly (1). More explicitly,
b is H^{-1}(D i) composed with H^{-1}(alpha), delta is the
connecting map to H^0(W^dagger[0]), gamma is
H^0(alpha^{-1} composed with D t), and epsilon is
H^0(D i composed with alpha). Thus all maps, including gamma,
are attached to the actual C_R and the normalized cup/trace adjoint.

For an independent indexing check, use the contravariant hyper-Ext
sequence in [Stacks Example 21.32.1, 07AA](https://stacks.math.columbia.edu/tag/07AA),
with finite-diagonal convergence as in
[12.25, 012X](https://stacks.math.columbia.edu/tag/012X):

\[
 E_2^{a,b}=Ext^a_R(H^{-b}(C_R),R)
       \ \Longrightarrow\ H^{a+b}(\mathbb D C_R).
\]

The complete list of possibly nonzero entries is M^* at (0,-1),
Ext^1(M,R) at (1,-1), and W^dagger at (2,-2). The only possible
differential is d_2:(0,-1) -> (2,-2); it is delta up to the common
connecting-map sign convention. Hence H^{-1}(DC_R)=ker delta,
and the degree-zero filtration is

\[
 0\longrightarrow\operatorname{coker}\delta
 \longrightarrow H^0(\mathbb D C_R)
 \longrightarrow Ext^1(M,R)\longrightarrow0.
\]

This verifies (1) without assuming degeneration of the spectral
sequence. In particular W^dagger is not simply discarded or
identified with W before its edge map has been constructed.

**Identification with the hull form.** Applying Hom_R(-,R) to
0 -> M -> E -> Q -> 0, with E free over R and (5) for Q, gives

\[
 E^*\xrightarrow{\sim}M^*,\qquad
 Ext^1_R(M,R)\xrightarrow{\sim}Ext^2_R(Q,R)=Q^\dagger.
                                                               \tag{8}
\]

On the punctured Spec R, C_R=M[-1] with M=E, and the map b in
(1) is the degree-one pairing adjoint of actual cup and trace.
By the normalization in (4) it equals omega_E^flat there. Therefore
b and omega_E^flat composed with M -> E agree on the puncture as
maps M -> E^*. They agree over R as well: their difference has
image supported only at the closed point inside the free module
E^*, which has no such nonzero submodule. Equivalently it is already
zero at the generic point and the target is torsion-free.
This checks the actual map, rather than choosing some abstract
self-duality of C_R. Since omega_E^flat is an isomorphism on E,
the cokernel of b is Q, using (8) to identify M^* with E^*.

Now exactness of (1) factors delta through this cokernel as an
injection Q -> W^dagger, and (8) identifies the final cokernel of
gamma with Q^dagger. This proves (2). Both Q and W have finite
length. Exactness and length preservation in (5) give
length(im gamma)=length(W^dagger)-length(Q)=w_z-q_z,
proving (3). The same value follows from W -> Q^dagger.
No equation w_z=q_z or independent isomorphism W^dagger=W follows.

**An explicit limit on the numerical consequence.** This is a
small algebraic specialization testing the information used above,
not a geometric construction or a general reproof of duality.
For each integer n>=1 let R=C[x,y]_(x,y), f=x^n, g=y, and form
the complex K_n in degrees 0,1,2:

\[
 R\xrightarrow{d^0}R^2\xrightarrow{d^1}R,\qquad
 d^0(r)=(-gr,fr),\qquad d^1(a,b)=fa+gb.                  \tag{9}
\]

The composition is zero. The first map is injective. If fa+gb=0,
reduction modulo g shows a=g t, because f is a nonzerodivisor
modulo g; then b=-f t, giving (a,b)=d^0(-t). Consequently H^1(K_n)=0
and H^2(K_n)=R/(x^n,y). The latter has basis
1,x,...,x^{n-1} over C and length exactly n.

On degree zero and degree two use the product pairing, in either
order. On degree one use
omega((a,b),(c,d))=ad-bc. These define a symmetric degree-two
derived pairing K_n tensor K_n -> R[-2]. To check that it is a
chain map, the only nontrivial differential identities are, for
r in degree zero and v in degree one,

\[
 \omega(d^0r,v)+r\,d^1v=0,\qquad
 (d^1v)r-\omega(v,d^0r)=0.
\]

They follow immediately from (9). The endpoint pairings are perfect
and the middle matrix has determinant one, so the adjoint is a
termwise isomorphism K_n[2] ~= D K_n with the usual shift signs.
The skew middle form has precisely the required graded symmetry.

Let P be a free rank-fifty module with its standard nondegenerate
alternating form, and set C_n=K_n direct sum P[-1], with orthogonal
sum pairing. It follows that C_n[2] ~= D C_n,
H^0(C_n)=0, H^1(C_n)=P and H^2(C_n)=R/(x^n,y).
The hull E_n=P has its extended perfect alternating form and
Q_n=0. On the puncture the ideal (x^n,y) is the unit ideal, so K_n
is exact and C_n=P[-1]. At the closed point every matrix in (9)
vanishes modulo the maximal ideal; the complete derived residue-field
cohomology dimensions of C_n are therefore (1,52,1).
In (2) the map gamma is then an isomorphism W_n^dagger -> W_n,
as also follows from this two-generator complete-intersection model.
Thus q_n=0, w_n=n and w_n+q_n is unbounded despite those fixed
derived dimensions. This proves the claimed limit of the sequence's
numerical use.

These models do not retain L095's actual first-order KS constraints,
the global Chern class, the product connection or the full tensor.
For n>1 they specifically allow higher local vanishing order.
They do not prove defects are unbounded for actual F. The earlier
L066 model concerned a different relative Hom problem over a
four-dimensional local base; it is a methodological comparison,
not an input or a duplicate defect computation. The present models
isolate the missing information in this surface sequence only.
An upper bound for actual defects requires additional geometric or
differential control; the duality-only numerical route is parked.
The metric-extension inference in ATTEMPTS/066 remains parked.

**Separate critical audit, 2026-10-16 (step 308).** Use the prior
SPECIALIZE assessment
`drafts/literature/2026-10-16-equality-local-duality-defect-critical-audit.md`.
The following independently checks the maps and complete model evidence;
it finds no substantive error in (1)--(3). Corrected L108, including
its actual normalized form, is retained as an input, not reproved.

The product projection is smooth and proper of relative dimension two
over a Noetherian base. The locally free coefficient V is trace-self-dual:
the scalar summand has trace norm 2, so its orthogonal complement is
nondegenerate. Thus 0BRT and 0G81 apply before any ordinary-image
base change. The chosen fibre two-form and Serre trace give the pairing
of degree two. Its adjoint first has type C -> (DC)[-2]; shifting
gives exactly (4), not C[-2] -> DC. Normalize the adjoint using the
same ordered cup/trace form as L108 (4). This fixes its restriction
to the stable open, including the flat-map convention; no positivity
or metric normalization is inferred from duality.

For the noncomplete stalk R, the finite modules in question have finite
free resolutions of length at most two by 00O7. Tensoring such a
resolution with the flat completion gives a free resolution over the
completion. Termwise finite freeness identifies its Hom complex with
the completed original Hom complex; flatness commutes with taking
cohomology. This verifies the particular Ext-completion passage used
in (5). For a finite-length module, a power of the maximal ideal
annihilates it, and R/m^r equals its completed quotient. The module
and its completion therefore coincide, and completion preserves a
composition series. The regular/Gorenstein finite-length formula
0G23, or 0A7Q with the normalized dualizing complex R[2], places
the only Ext in degree two. Finite-length Matlis duality (08Z9)
is exact, sends the residue field to a module of length one and hence
preserves every finite length. This uses no general Noetherian/Artinian
anti-equivalence over noncomplete R and no identification T=T^dagger.

Torsion-free M has depth at least one, since R is a domain and any
nonzero element of m acts injectively. Thus pd M<=1, including the
free case. In (7) the only nonzero degrees of (DM)[1] are -1 and 0,
whereas W^dagger[0] has only degree 0. The long exact sequence is
therefore

    0 -> H^{-1}(DC) -> M^* -> W^dagger -> H^0(DC)
      -> Ext^1(M,R) -> 0.

Inserting alpha gives precisely the maps in (1). In particular gamma
uses alpha^{-1}, while the maps out of M and W use alpha; these
directions cannot be exchanged merely because some lengths agree.
The independent hyper-Ext check has only (0,-1), (1,-1), (2,-2),
with d_2 of bidegree (2,-1). Its sole possible arrow is therefore
the printed M^* -> W^dagger. The two degree-zero surviving entries
give the filtration in the proof; there is no unlisted incoming
differential or higher transgression.

In the hull sequence, Ext^0(Q,R)=Ext^1(Q,R)=0 and E is free. Its
dual long exact sequence gives both isomorphisms in (8), with no
assumption that M itself is free. Under E^*=M^*, the first map in
(1) and omega_E^flat composed with M -> E agree off the closed
point by the actual cup/trace normalization. Their difference has
zero generic fibre and image in a free R-module, hence is zero.
Its cokernel is identified with Q via omega_E^flat, rather than
by a bare equality of lengths. Factoring delta through that cokernel
and using Ext^1(M,R)=Q^dagger verifies the injection and surjection
in (2). Additivity gives w_z-q_z for the image length on either
side. No splitting, equality q_z=w_z, reduced support or value of
either length is deduced. If Z is empty, W=Q=0 and truncation
globally gives C=E[-1], as asserted.

For the model use the standard exterior Koszul construction in
[Stacks Definitions 15.29.1--2, 0621](https://stacks.math.columbia.edu/tag/0621)
and regular-sequence exactness in
[Lemma 15.31.2, 062D](https://stacks.math.columbia.edu/tag/062D).
Here x^n is a nonzerodivisor in R and y remains a nonzerodivisor
modulo x^n, so this is a regular sequence. The matrix order in (9)
is a basis change of its two-generator Koszul complex. Independently,
the displayed kernel computation is valid because R/(y) is the
domain C[x]_(x). Cancellation of g in R then yields b=-ft.
This checks every cohomology group: H^0=H^1=0 and
H^2=C[x]_(x)/(x^n), with length n, for every n>=1.

Here are explicit signs for the claimed adjoint. Use the cochain
conventions d_{K[2]}=d_K and
d_{DK}^j=(-1)^{j+1}(d_K^{-j-1})^t. Write

\[
 u=\binom{-g}{f},\qquad v=(f\ \ g),\qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Then K[2] has differentials u,v in degrees -2,-1, while DK has
differentials -v^t,u^t. For the convention a -> (b -> omega(a,b)),
the three adjoint component matrices in degrees -2,-1,0 are
respectively 1,J,1: the functional associated with (a,b) has
column (-b,a). Both chain equations hold exactly:

\[
 Ju=\binom{-f}{-g}=-v^t,\qquad u^tJ=(f\ \ g)=v.
\]

All three components are invertible, with det J=1. Thus the
adjoint is a chain isomorphism, not just a dimension comparison.
Endpoint pairing symmetry and middle alternation give the required
graded symmetry. The two chain-map identities printed after (9)
exhaust total degree one; in other total degrees both possible
images in R[-2] are zero. On P[-1], its alternating form gives
the analogous single invertible degree -1 component, with zero
differentials. The orthogonal direct sum therefore retains the
claimed degree-two perfect pairing.

At any nonclosed prime of Spec R, x or y is invertible; the Koszul
complex is exact there. At the closed point all entries of u and v
lie in m, including for n=1, so tensoring this free complex with
k computes its complete derived fibre with zero differentials.
Adding P[-1] gives dimensions exactly (1,2+50,1) in degrees 0,1,2
and zero in every other degree. These agree with the split-fibre
dimensions: trace-free H^0 and H^2 each have dimension one and
chi(V_z)=-50, so H^1 has dimension 52. Nevertheless M_n=P,
E_n=P, Q_n=0 and W_n=R/(x^n,y) has length n. The already checked
sequence now makes its actual gamma an isomorphism; no arbitrary
choice W_n^dagger=W_n is needed. Thus the unbounded numerical
example survives with all its advertised hypotheses.

The audit verifies only this limited countermodel test. It neither
adds the actual KS map to C_n nor verifies a geometric realization,
a global Chern class or a compatible product connection. Those
missing conditions may constrain actual lengths. ATTEMPTS/067's
duality-only stop is consequently retained with precisely that scope;
ATTEMPTS/066's separate metric-extension problem is not addressed.
No new defect bound, kernel, cycle or transport conclusion is obtained.

## Mathlib

Full matching coverage of the actual-family duality/hull sequence
and its defect specialization: **not checked**. No absence is
asserted. The named primary derived-duality, hyper-Ext, regular-local
resolution and finite-length duality results are imported above.
The map comparison and local models are explicit specializations
under the prior assessment, classified as REPRODUCTION.
The separate audit supplies explicit shifted-adjoint matrices and
checks the noncomplete finite-length specialization; it does not
change the mathematical conclusions or the Mathlib coverage status.

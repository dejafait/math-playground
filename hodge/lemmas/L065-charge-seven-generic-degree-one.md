# L065 — Conditional charge-seven image has generic degree one

## Hypotheses

Retain exactly L064's conditional actual rank-two bundle F on B x Y,
with B and Y the identical marked smooth projective complex K3 surface
S, the specified real product polarization, c_1(F)=0 and
ch_2(F)=-6e_1-7e_2+tau_D. Existence of F remains unproved. Use L063's
single integral very ample H and actual algebraic classifying morphism

\[
f:B\longrightarrow M=M_H^s(2,0,-5).
\]

Let Z be its scheme-theoretic image, with closed immersion j:Z -> M
and factor g:B -> Z. L064 supplies that g is finite, surjective and
unramified and that Z is reduced. Use L062's actual ordered family
form beta_F=-2lambda sigma_B, with lambda nonzero, and L064's natural
identification of df with the family Kodaira--Spencer map. No normality
of Z, flatness of g, universal sheaf, global injectivity or embedding
is assumed.

## Conclusion

The generic degree is one:

\[
                         [\mathbf C(B):\mathbf C(Z)]=1.
\]

More precisely, if nu:W -> Z is the normalization, the canonical
factor h:B -> W of g is an isomorphism. Thus g identifies with the
normalization morphism of Z. The original image Z need not be normal,
and no injectivity or closed immersion of g or f is concluded.

This is a conditional REPRODUCTION and specialization of the assessed
normalization, unramified-cover, coarse-moduli-form, trace and
Riemann--Roch theorems. It supplies no F, reconstruction from the
possibly singular original image, inverse transform, transverse
transport, new algebraic Hodge class or universal Hodge resolution.

## Proof

**The actual normalization factor.** The continuous image of the
irreducible B is irreducible. Since g is surjective, Z is irreducible;
L064's reducedness therefore makes Z integral. It is a separated
finite-type complex scheme, being closed in the quasi-projective M.
Its dimension is two, since g is finite and surjective and B is a
surface. Schemes locally of finite type over a field are Nagata
([Stacks Lemma 29.18.2(1), Tag 0359](https://stacks.math.columbia.edu/tag/0359)),
and normalization of a Nagata scheme is finite
([Lemma 29.55.11, Tag 035S](https://stacks.math.columbia.edu/tag/035S)).
Consequently nu:W -> Z is finite and birational, and W is an integral
normal finite-type complex surface.

B is smooth, hence normal, and its unique component dominates Z.
Apply the normalization universal property
([Lemma 29.55.5(4), Tag 035Q](https://stacks.math.columbia.edu/tag/035Q))
to obtain h:B -> W with nu composed with h equal to g. At the generic
point of Z its normalization has the same function field and a single
generic point. Dominance of g therefore makes h dominant as well.
The morphism nu is separated and nu composed with h=g is finite.
The separated-factor criterion
([Lemma 29.45.14, Tag 035D](https://stacks.math.columbia.edu/tag/035D))
implies that h is finite. Its image is closed and contains the generic
point of the integral W, hence is all of W. This checks surjectivity
without assuming that normalization preserves fibres of g.

For B -> W -> Z the transitivity sequence
([Lemma 29.33.9, Tag 01UX](https://stacks.math.columbia.edu/tag/01UX))
ends in

\[
h^*\Omega_{W/Z}\longrightarrow\Omega_{B/Z}
                \longrightarrow\Omega_{B/W}\longrightarrow0.
\]

The middle term vanishes by L064's unramifiedness of g. Hence
Omega_{B/W}=0. Since h is finite, in particular locally of finite
type, the differential criterion
([Tag 02G5](https://stacks.math.columbia.edu/tag/02G5)) makes h
unramified. No flatness of g or regularity of Z was used.

**An étale cover of a smooth proper surface.** A normal scheme is
geometrically unibranch
([Lemma 28.16.2, Tag 0BQ3](https://stacks.math.columbia.edu/tag/0BQ3)).
Apply [Lemma 37.37.2, Tag 0GS9](https://stacks.math.columbia.edu/tag/0GS9)
to h: its target W is integral and geometrically unibranch, its source
B is connected, its source component dominates W, and h is unramified.
The theorem concludes that h is étale. Together with the preceding
paragraph, h is a finite surjective étale map. Let d be its positive
constant degree; W is connected and h is finite locally free.
At the generic point d=[C(B):C(W)]=[C(B):C(Z)].

The map h is faithfully flat and locally finitely presented. Smoothness
of B over C descends through it
([Lemma 35.14.5, Tag 05B5](https://stacks.math.columbia.edu/tag/05B5)),
so W is smooth over C. The structure morphism of B is universally
closed. Universal closedness descends through the surjective h
([Lemma 29.42.9, Tag 03GN](https://stacks.math.columbia.edu/tag/03GN)),
so the separated finite-type W is proper over C. W is also
quasi-projective: Z is closed in the quasi-projective M, nu is finite
and therefore quasi-finite and separated, and the quasi-projective
morphism criteria and composition rule in
[Lemmas 37.49.1--37.49.2, Tag 0B41](https://stacks.math.columbia.edu/tag/0B41)
apply. A proper quasi-projective complex scheme is projective: its
locally closed immersion into projective space is proper and thus a
closed immersion. W is now a smooth projective integral surface; no
such assertion has been made about Z.

**The coarse two-form on W.** Import Huybrechts--Lehn,
*The Geometry of Moduli Spaces of Sheaves*, Aspects of Mathematics
E31 (1997), [Lemmas 10.3.3--10.3.4 and Theorem 10.3.5,
pp. 224--225; Proposition 10.4.1, Corollary 10.4.2 and Theorem
10.4.3, pp. 227--228](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=236).
For a smooth projective surface with trivial canonical bundle, its
stable sheaf moduli space is smooth and carries the coarse Mukai
two-form. Its pullback for an actual flat family is the family
Kodaira--Spencer/Yoneda/trace pairing. The normalization by
quasi-universal similitude makes it independent of the chosen local
family. These general theorems are imported, not reproved. They
apply to the stable numerical-class part M on the K3 Y; a generic
polarization or a global universal sheaf is not required.

Choose the coarse form omega_M using the fixed nonzero sigma_Y.
Its pullback by f is

\[
                              f^*\omega_M=a\,\beta_F,
                     \qquad a\in\mathbf C^* .                 \tag{1}
\]

Indeed at every x, L064 identifies df_x with the actual family's
Kodaira--Spencer map. The cited family formula is its Yoneda product
followed by trace and pairing with sigma_Y, exactly the pairing in
L062 up to the fixed trace normalization and ordered-product sign.
The functional on the one-dimensional H^2(Y,O_Y) is nonzero by
Serre duality. Comparing it with L062's integral convention gives
one nonzero scalar independent of x. Tensoring a local universal
family by a parameter bundle multiplies the pairing by its rank;
the cited similitude normalization cancels that rank. Thus local
choices do not introduce a varying coefficient in (1). No new exact
conversion to a printed Serre-trace convention is asserted.

Define omega_W=(j composed with nu)^*omega_M. This is a global
holomorphic two-form on the smooth W. Functoriality of pullback and
g=nu composed with h give

\[
                   h^*\omega_W=f^*\omega_M
                             =-2a\lambda\sigma_B\ne0.         \tag{2}
\]

In particular omega_W is nonzero. This uses a form pulled back from
M, rather than an assumed descent of a form from B through singular
Z. Pullback of global holomorphic two-forms by the surjective étale h
is injective: at every complex w choose b above it; dh_b is an
isomorphism of tangent spaces, so vanishing of the pullback forces
vanishing at w. Since h^0(B,Omega_B^2)=1, (2) proves

\[
                            h^0(W,K_W)=1.                    \tag{3}
\]

**Coherent Euler characteristic and the degree.** The finite locally
free trace has composite with the unit equal to multiplication by d
([Stacks Section 49.3, Tag 0BVH](https://stacks.math.columbia.edu/tag/0BVH)).
Over C, trace divided by d splits O_W -> h_*O_B. On coherent
cohomology H^1(W,O_W) therefore injects into H^1(W,h_*O_B).
Because h is finite and affine, its higher direct images of O_B
vanish by the affine coherent-cohomology vanishing theorem. The
Leray spectral sequence therefore identifies the latter space with
H^1(B,O_B)=0. Hence q(W)=0.
Properness and integrality over C give h^0(W,O_W)=1; Serre duality
on the smooth projective surface W and (3) give h^2(W,O_W)=1.
It follows that

\[
                           \chi(W,O_W)=1-0+1=2.              \tag{4}
\]

Import the named Hirzebruch--Riemann--Roch theorem, with its smooth
proper structure-morphism formulation in
[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO).
Finite étaleness gives T_B=h^*T_W. HRR and integration under the
degree-d cover give the standard finite-étale Euler identity

\[
\chi(B,O_B)=\int_B\operatorname{td}(T_B)
 =d\int_W\operatorname{td}(T_W)=d\,\chi(W,O_W).             \tag{5}
\]

For an explicit primary use of this identity see Debarre,
*On rationality problems*, 15 April 2024,
[proof of Proposition 2.5(c), p. 6](https://perso.imj-prg.fr/olivier-debarre/wp-content/uploads/sites/34/2024/04/On-rationality-problems.pdf#page=6).
Only this general identity is imported, not that proposition's
rationally connected hypotheses or conclusion. Here both surfaces
are smooth and projective and h has been proved finite étale, so
every hypothesis of the identity has been checked.

The K3 B has chi(B,O_B)=2. Equations (4)--(5) yield 2=2d,
so d=1. A finite étale morphism of degree one is an isomorphism:
its rank-one locally free algebra has unit a basis in every residue
fibre, hence the unit O_W -> h_*O_B is an isomorphism by Nakayama.
This establishes the claimed generic degree and normalization
identification.

The decisive difference from a K3 double cover of an Enriques surface
is (2); an Enriques surface has no nonzero holomorphic two-form
(Huybrechts, *Lectures on K3 surfaces*, author-hosted prepublication
draft, [Section 15.4.3(ii), printed p. 330](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=330)).
A K3 source and unramifiedness alone would not prove d=1. Nor does
d=1 make the possibly singular Z normal: the normalization can
identify distinct points above a singular point. The intermediate
threshold is met, but F existence, reconstruction and transverse
transport remain independent open steps. Earlier stopped index and
lifting mechanisms are not reopened. This conditional result is not
a complete Hodge-conjecture candidate.

**Independent critical audit, 2026-10-07.** The conditional conclusion
survives the approved audit, with no substantive mathematical repair.
For the normalization property, the relevant dominant morphism is
g:B -> Z, with normal integral source and integral finite-type target.
The finite factor h dominates W and is surjective because its image
is closed. Vanishing of Omega_{B/W} follows from Omega_{B/Z}=0;
it requires neither flatness nor normality of Z. In Tag 0GS9 the
connected source is B and the integral geometrically unibranch target
is W. Applying that theorem to g instead would be unjustified.
The resulting finite étale h is the surjective flat locally finitely
presented morphism required in Tag 05B5. For Tag 0B41, Z has an ample
invertible sheaf because it is quasi-projective, so the finite
normalization is covered by 37.49.2(7) and then composition (2).

The constant comparison in (1) can be checked without a metric or a
universal sheaf. On the single fixed vector space H^2(Y,O_Y), put
I(t)=integral_Y sigma_Y wedge t, using Dolbeault representatives,
and let L(t) be the Serre trace of sigma_Y cup t in the cited coarse
form convention. Both are nonzero linear functionals: I is nonzero
on the class of the conjugate of sigma_Y, and L is nonzero by Serre
duality. Thus L=b I for one b in C^*, independent of x. L064 identifies
df_x with the actual kappa_x, so both forms evaluate this same
trace/Yoneda class. L062's prefactor makes a=b(2pi i)^2, up to the
single fixed choice of Yoneda order; its precise value is unnecessary.
Huybrechts--Lehn 10.3.4--10.3.5 cancel the parameter-bundle rank.
The coarse formula on the full Ext^1 tangent is explicitly stated
at the start of Section 10.4, p. 226, before Proposition 10.4.1.
Consequently no parameter-dependent normalization or assumed descent
through singular Z enters (2).

For the Euler step, finite local freeness is established before trace
is used. Its split unit and affine pushforward imply q(W)=0; injective
étale pullback bounds p_g(W) by one and (2) gives the matching lower
bound. Proper integrality and surface Serre duality then give chi=2.
HRR applies to both smooth proper structure morphisms, and the tangent
bundle pullback uses étaleness, not merely unramifiedness. Thus (5)
really yields 2=2d. The rank-one algebra argument identifies B with W
only; it does not remove possible identifications in W -> Z. This
audit confirms the existing specialization of known tools, rather than
establishing a new theorem, repairing an error, or resolving F
existence, reconstruction or transverse transport. Direct mathematical
inputs and all qualifications are unchanged.

## Mathlib

Coverage of the full conditional generic-degree statement, the
coarse sheaf-moduli two-form and their combined specialization:
**not checked**. No matching declaration or absence is asserted.
The proof imports the precise named and cited results above; it is
not a Lean verification or a claim of progress beyond those sources.

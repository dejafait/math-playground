# L120 — Conditional opposite image has normalization B

## Hypotheses

Retain L118's identical marked smooth projective complex K3 surfaces
X=B x Y=S_1 x S_2, common hyperkähler metric g, ordered structures
I,J,K, real ample class h and product polarization Omega. Write
sigma=omega_J+i omega_K and e_1=eta tensor 1, e_2=1 tensor eta.
Retain L071's full integral self-adjoint tensor tau_D, with
D[sigma]=2lambda[sigma] and 1<lambda<5/4.

Suppose F is holomorphic locally free of rank two, Omega-slope-polystable,
with integral c_1(F)=0 and

\[
              \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use L071's actual compatible unitary connection and audited L118's
actual stable classifying morphism

\[
 f=f^-:B\longrightarrow M=M_H^s(2,0,-19),\qquad
                   x\longmapsto[F|_{\{x\}\times Y}].
\]

In particular all its fibres are stable, its natural differential is
the actual family KS class with harmonic representative supplied by
L118, and its normalized metric pullback is 2lambda g. L118 also gives
the actual closed holomorphic two-form

\[
 \gamma^-=p_{1*}\left(
       \frac{\operatorname{Tr}(R\wedge R)}{2(2\pi i)^2}
                              \wedge p_2^*\sigma_Y\right)
                        =-2\lambda\sigma_B.                 \tag{1}
\]

No existence of F, global point separation, original-image normality,
embedding or transverse transport is assumed.

## Conclusion

The morphism f is finite and unramified. Let j:Z -> M be its
scheme-theoretic image; Z is reduced and integral. Its factor
g:B -> Z is finite, surjective and unramified. If nu:W -> Z is the
normalization, the canonical factor a:B -> W is an isomorphism. Thus

\[
                   [\mathbf C(B):\mathbf C(Z)]=1,
\]

and g identifies B with the normalization of its reduced image.

This is a conditional REPRODUCTION/specialization of the assessed
general cover, coarse-form and Euler theorems. The separate critical
audit below preserves it. It establishes no injectivity or closed immersion of
f, normality of Z, existence of F, reconstruction, transport or new
algebraic Hodge class. The universal primitive Hodge gap remains open.

## Proof

**Scope and known inputs.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-17-opposite-image-normalization.md`.
L071 and audited L118 are the direct mathematical inputs. Audited
L119's whole-tangent descent supports the same natural comparison,
but neither its normal character nor a conclusion of L064, L065 or
L099 is needed as a premise. Those earlier maps provide comparison
methods only. Import the following general theorems by citation;
the proof checks their application to this actual opposite family.

**Finiteness and unramifiedness of the actual map.** M is a separated
quasi-projective finite-type complex scheme, being an open-and-closed
numerical-class part of the stable open in the projective Gieseker
moduli scheme used in L118. At each closed complex x in B, the
natural differential df_x is injective by L118: its harmonic real
representative has positive squared norm 2lambda g(u,u) for u nonzero.
The complex differential is the same KS class, with no arbitrary
tangent identification. The two residue fields at x and f(x) are C.
The tangent criterion for an unramified morphism therefore applies
([Stacks Lemma 33.16.8, 0B2G](https://stacks.math.columbia.edu/tag/0B2G)).
Its hypotheses include local finite type, which holds here. The
unramified locus is open
([02G4](https://stacks.math.columbia.edu/tag/02G4)); its closed
complement contains no closed complex point. A nonempty closed subset
of a finite-type C-scheme has a closed point, so the complement is
empty. This treats all scheme points without applying the
equal-residue-field tangent criterion at nonclosed points.

The projective B is proper over C and M is separated over C. Hence
f is proper by the proper-source/separated-target criterion
([Lemma 29.42.7, 01W6](https://stacks.math.columbia.edu/tag/01W6)).
Unramifiedness implies local quasi-finiteness
([02V5](https://stacks.math.columbia.edu/tag/02V5)). Proper and locally
quasi-finite implies finite
([Lemma 37.44.1, 02LS](https://stacks.math.columbia.edu/tag/02LS)).
No properness of the stable ambient open is required.

The kernel of O_M -> f_*O_B defines the scheme-theoretic image
([Section 29.6, 01R5](https://stacks.math.columbia.edu/tag/01R5)).
Its support is f(B), since f is proper. The reduced-source image
criterion ([056B](https://stacks.math.columbia.edu/tag/056B)) makes
Z reduced. Its support is irreducible, since B is irreducible; thus
Z is integral. The factor g:B -> Z is surjective. Since j is
separated and jg=f is finite, g is finite by
[Lemma 29.45.14, 035D](https://stacks.math.columbia.edu/tag/035D).
The differential sequence for B -> Z -> M gives a surjection
Omega_{B/M} -> Omega_{B/Z}. The first is zero. Therefore g is
unramified by the locally-finite-type differential criterion
([01UX](https://stacks.math.columbia.edu/tag/01UX),
[02G5](https://stacks.math.columbia.edu/tag/02G5)). In particular Z
is an integral surface. Reducedness has supplied no normality claim.

**The actual normalization factor is finite etale.** A finite-type
complex scheme is Nagata
([Lemma 29.18.2, 0359](https://stacks.math.columbia.edu/tag/0359)),
and its normalization is finite
([Lemma 29.55.11, 035S](https://stacks.math.columbia.edu/tag/035S)).
Consequently nu:W -> Z is finite birational and W is an integral
normal finite-type complex surface. B is smooth and hence normal,
and its unique component dominates Z. The normalization universal
property ([Lemma 29.55.5(4), 035Q](https://stacks.math.columbia.edu/tag/035Q))
gives the actual factor a:B -> W with nu a=g. Since nu is
birational, dominance of g makes a dominant.

Nu is separated and nu a=g is finite; 035D makes a finite. Its
image is closed and contains the generic point of the integral W,
so it is surjective. In the differential sequence for B -> W -> Z,
Omega_{B/Z}=0 surjects onto Omega_{B/W}. Therefore a is unramified
by 01UX and 02G5. This separately checks its finite-type hypothesis
and does not assume that normalization preserves the fibres of g.

Normal W is geometrically unibranch
([Lemma 28.16.2, 0BQ3](https://stacks.math.columbia.edu/tag/0BQ3)).
Apply [Lemma 37.37.2, 0GS9](https://stacks.math.columbia.edu/tag/0GS9):
the target is integral and geometrically unibranch, B is connected,
its component dominates W, and a is unramified. The conclusion is
that a is etale. Thus a is finite surjective etale, of positive
constant degree d, and

\[
 d=[\mathbf C(B):\mathbf C(W)]=[\mathbf C(B):\mathbf C(Z)].  \tag{2}
\]

The theorem is applied to W, not to possibly nonnormal Z; flatness
is obtained only at this stage. Smoothness of B over C descends
through the faithfully flat locally finitely presented a
([Lemma 35.14.5, 05B5](https://stacks.math.columbia.edu/tag/05B5)).
Universal closedness descends from B -> Spec C through the
surjection a ([Lemma 29.42.9, 03GN](https://stacks.math.columbia.edu/tag/03GN)).
Since W is separated and finite type, it is proper over C. It is
also quasi-projective: Z is closed in quasi-projective M, and a
finite morphism nu is quasi-projective, with the composition rules
in [Lemmas 37.49.1--37.49.2, 0B41](https://stacks.math.columbia.edu/tag/0B41).
Proper quasi-projectivity makes W projective: its locally closed
immersion in projective space is proper, hence a closed immersion.
Thus W is a smooth projective integral surface.

**Nonzero pullback of the actual coarse form.** Import
Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*, E31
(1997), [Lemmas 10.3.3--10.3.4 and Theorem 10.3.5,
pp. 224--225; Section 10.4 and Proposition 10.4.1, Corollary 10.4.2,
Theorem 10.4.3, pp. 226--228](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=236).
These give the coarse Mukai two-form omega_M on the K3 stable
locus and its actual-family KS/Yoneda/trace formula, independent
of a universal family after quasi-universal similitude normalization.
There is no generic-polarization or charge-seven restriction.
Equivalently the actual-family formula is the surface q=0 case of
Kuznetsov--Markushevich, *Symplectic structures on moduli spaces
of sheaves via the Atiyah class*,
[math/0703264v2 (19 October 2007), Theorem 2.2, equations (12)--(14)
and proof, PDF pp. 9--11](https://arxiv.org/pdf/math/0703264v2#page=9).
Use the fixed sigma_Y to choose this form. At every point of f(B),
stability and K_Y=O_Y make trace-free Ext^2 zero, as checked in
L118; the coarse germ there is smooth. We may restrict M to this
smooth open when pulling back its form.

Here is the actual-family comparison, including the curvature order.
For v,w in T_x^{1,0}B let b_v,b_w be the Dolbeault harmonic
representatives of their actual KS classes. L118 identifies them
with the mixed curvature forms R(v,-)^{0,1}, without a factor or
conjugation: the horizontal gauge term is exact before harmonic
projection. In local holomorphic base coordinates the component
of R with one holomorphic base and one antiholomorphic fibre leg
is sum_i dz_i wedge b_i. Moving the fibre leg past the next base
leg in its square shows

\[
 \operatorname{Tr}(R\wedge R)(v,w,-,-)^{0,2}_Y
                      =-2\operatorname{Tr}(b_v\wedge b_w).
\]

Both ordered mixed products are retained. The other terms cannot
contribute: the purely base curvature is of type (1,1), so is zero
on two holomorphic base vectors; also the purely fibre curvature
wedged with sigma_Y has impossible fibre type (3,1). Thus (1)
gives the pointwise identity

\[
 \gamma^-_x(v,w)=-\frac{1}{(2\pi i)^2}
       \int_Y\sigma_Y\wedge\operatorname{Tr}(b_v\wedge b_w).
                                                               \tag{3}
\]

For completeness, both forms use the same fixed trace functional.
On the one-dimensional vector space H^2(Y,O_Y), let
I(t)=integral_Y sigma_Y wedge t and let L(t) be the Serre trace
of sigma_Y cup t in the coarse-form convention. I is nonzero on
the conjugate-sigma class, and L is nonzero by Serre duality. Hence
L=c I for one fixed c in C^*. The coarse family formula evaluates
L on the same class [Tr(b_v wedge b_w)] as (3). Up to a single
fixed Yoneda-order sign, absorbable in c, it follows that

\[
             f^*\omega_M=-c(2\pi i)^2\gamma^-
                         =2c(2\pi i)^2\lambda\sigma_B\ne0.  \tag{4}
\]

This argument needs no asserted numerical Serre-trace normalization.
The functional and the fixed Y are independent of x. Scalar and
base-line changes of local representing families cancel in End;
the cited rank-scaling/similitude formula cancels any parameter-bundle
rank. Thus c is a fixed nonzero scalar, not a parameter-dependent
choice. L118's base-first orientation and full self-adjoint tensor
enter through (1); no signed coefficient from L062 is imported.

Set omega_W=(j nu)^*omega_M on the smooth W. Functoriality gives
a^*omega_W=f^*omega_M, which is nonzero by (4). This pulls back a
form from the stable ambient space; it does not assume descent
of a form from B through singular Z. Since a is surjective etale,
pullback H^0(W,K_W) -> H^0(B,K_B) is injective: its differential
is an isomorphism above every point. The target has dimension one
and omega_W is nonzero, so

\[
                              p_g(W)=1.                    \tag{5}
\]

**Trace, Euler characteristic and degree.** Finite etaleness makes
a finite locally free of rank d. The trace-unit composite on O_W
is multiplication by d
([Stacks Section 49.3, 0BVH](https://stacks.math.columbia.edu/tag/0BVH)).
In characteristic zero, trace divided by d splits O_W -> a_*O_B.
Consequently H^1(W,O_W) injects into H^1(W,a_*O_B). Finite
affine pushforward has no higher coherent direct images, so Leray
identifies the latter with H^1(B,O_B)=0. Hence q(W)=0. Proper
integral W has h^0(O_W)=1, and smooth projective Serre duality
with (5) gives h^2(O_W)=1. Therefore chi(W,O_W)=2.

Import the named Hirzebruch--Riemann--Roch theorem in its smooth
proper structure-morphism form
([Stacks Section 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO)).
Since a is etale, T_B=a^*T_W. Degree-d integration and HRR give

\[
 2=\chi(B,O_B)=\int_B\operatorname{td}(T_B)
        =d\int_W\operatorname{td}(T_W)=2d.                   \tag{6}
\]

This is the standard finite-etale coherent Euler identity; an
inspected primary use is Debarre, *On rationality problems*,
15 April 2024, [proof of Proposition 2.5(c), p. 6](https://perso.imj-prg.fr/olivier-debarre/wp-content/uploads/sites/34/2024/04/On-rationality-problems.pdf#page=6).
Only the identity is used, with smooth proper hypotheses verified
here, not that proposition's rational-connectedness assumptions.

Equation (6) yields d=1, meeting the degree-one threshold. A finite
etale degree-one morphism is an isomorphism: the unit O_W -> a_*O_B
between rank-one locally free modules is an isomorphism in each
residue fibre and hence everywhere. This proves the conclusion.

The nonzero form in (4) is essential; etaleness from a K3 surface
alone allows an Enriques quotient, where p_g=0. Nor does d=1
make the original Z normal or separate its points: only a is an
isomorphism, while nu:W -> Z can still identify distinct points.
No global embedding, F existence or Hodge algebraicity follows.

**Separate critical audit, 2026-10-17 (step 354).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-17-opposite-normalization-critical-audit.md`.
This independent check finds no substantive error, stronger obstruction
or existence conclusion. Its outcome is EXPLORATION / RESEARCH /
REPRODUCTION, with actual task type proof_audit. The direct mathematical
inputs remain L071 and audited L118. L119's character and the degree
verdicts for the other families are not premises.

The audit checks the actual maps in order. The fixed charge 21 excludes
L071's split charges 14r^2, consistently with L118's all-stable placement.
L118's same-extension comparison makes the positive harmonic norm a
statement about the actual coarse differential. Thus the tangent
criterion applies at every closed complex point; the closed complement
of the unramified locus must be empty on the finite-type source. The
proper-source argument uses separatedness of M, not properness of its
stable open. Properness and quasi-finiteness then give finiteness.
On an affine open of M the kernel defining Z has reduced quotient,
since its quotient embeds in the algebra of sections on the reduced
inverse image in B. Irreducibility of the topological image supplies
integrality. Neither fact implies normality.

For the actual factor through normalization, the component of the
normal source B dominates Z, so 035Q(4) applies. Birationality of W -> Z
then gives dominance of a. The separated-factor criterion 035D, whose
proof was reinspected, makes a finite; its closed dominant image is all
of W. The two differential sequences used above have the indicated
surjection direction, so unramifiedness passes to g and then to a.
Normal W is geometrically unibranch, and connected B has a dominating
component. These are all the hypotheses of 0GS9, whose complete proof
was reinspected. In particular no flatness is assumed before that theorem.

The finite surjective etale map is now an fppf cover, as required by
the reinspected smoothness-descent statement 05B5. Universal closedness
descends through this surjection by 03GN. Separatedness and finite type
of W follow from finite W -> Z and the separated finite-type ambient M.
For projectivity, Z is quasi-projective and has an ample line bundle;
finite W -> Z is separated and quasi-finite, so 0B41, Lemma 37.49.2(7),
and composition in (2) give quasi-projectivity over C. The relevant
statements and proof cases were reinspected. Properness then makes a
quasi-projective immersion into projective space closed. This validates
the smooth projective surface scope before Serre duality or HRR is used.

For the form, L118's actual harmonic representative is load-bearing.
Writing v=(u-iIu)/2, its identity R(Iu,bar t)=iR(u,bar t) gives
R(v,bar t)=R(u,bar t); there is no factor two in the natural complex
KS class. The horizontal connection term is exact before harmonic
projection, and the mixed form itself is harmonic. Thus the b_v in
(3) are precisely the representatives used by the coarse family formula.
The primary Theorem 2.2 and complete relevant proof, (12)--(14), of
Kuznetsov--Markushevich at the citation above were reinspected. Here
n=2, q=0 and omega=sigma_Y; the actual flat family may be restricted
to smooth affine opens of B. This specializes their family formula,
without using a fine moduli space or a nonzero-pullback theorem.
The Huybrechts--Lehn similitude/descent coverage is reused.

Independently expand the two mixed factors. If R_m=sum dz_i wedge b_i
in the relevant bidegrees, the dz_i dz_j coefficient of Tr(R_m^2)
is -Tr(b_i wedge b_j)+Tr(b_j wedge b_i)=-2Tr(b_i wedge b_j).
Graded cyclicity of trace supplies the second equality even for
noncommuting matrix coefficients. Division by the Chern--Weil factorial
gives exactly (3). The other curvature components cannot supply its
two holomorphic base and two antiholomorphic fibre legs. Moreover
sigma_Y has degree two, so moving it past a fibre two-form introduces
no further sign. The fixed functionals I and L are both nonzero on the
one-dimensional H^2(Y,O_Y); their ratio is independent of x. Local
isomorphisms of representing families conjugate End-valued classes and
leave their trace products unchanged. Therefore (4) is a fixed nonzero
multiple of the actual gamma^-, with no phase-positivity requirement.

The form omega_W is pulled back along W -> M into the smooth stable
locus; it is not descended from B through singular Z. Etaleness makes
pullback of top forms injective, and (4) supplies a nonzero element in
its domain. Since h^0(B,K_B)=1, this proves p_g(W)=1. The trace splitting
uses finite local freeness of positive constant degree and characteristic
zero; finite affine pushforward identifies H^1(W,a_*O_B) with H^1(B,O_B).
Thus q(W)=0, while proper integrality gives h^0(O_W)=1. Serre duality
and HRR consequently apply with the exact invariants in (5)--(6).
The etale tangent identity and degree-d integration yield d=1. On every
residue fibre a rank-one unital algebra has its unit as a basis; hence
the final unit-map argument really identifies a with an isomorphism.

The degree-one threshold is met under the retained conditional inputs.
The Enriques alternative is eliminated specifically by the actual
nonzero target form, not by the K3 source alone. No part of the audit
proves that nu is injective or that Z is normal. Original-image point
separation, F existence, reconstruction and transverse transport remain
unresolved, as does universal primitive Hodge realization. The index,
automatic metric-extension, compactification and uncontrolled cup stops
are preserved. This is confirmation of a known-tool specialization,
not progress beyond the inspected sources or a new mathematical advance.

## Mathlib

Full matching coverage for this conditional actual-family normalization,
coarse Mukai form and finite-etale Euler specialization is **not checked**.
Unknown availability is not evidence of absence. The proof imports
the precise named classical and scheme-theoretic inputs above; it is
an informal argument, not a Lean verification. The separate critical
audit above preserves the application without an originality claim.

# L151 — The preferred twisted harmonic connection is ASD on the stable open

## Hypotheses

Retain L071's identical marked projective K3 factors S_1 and B=S_2,
their fixed common hyperkähler metric g, ordered structures I,J,K and
Kähler class h. Suppose F is a locally free rank-two bundle on S_1 x B,
slope-polystable at Omega=p_1^*h+p_2^*h, with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use the compatible Hermitian hyperholomorphic connection on F supplied
by L071, with its given metric. Let L on S_1 have class
k=(-4,-2,1,2), k.h=0 and k^2=-14. Fix L094's Hermite--Einstein line
metric h_L and give L^{-1} exactly its dual metric h_L^{-1}. This is
the preferred twisting convention of L150; its central-orthogonality
conclusion is not needed here. Set

\[
 G=F\otimes p_1^*L^{-1},\qquad M=R^1p_{2*}G,\qquad U=B\setminus Z,
\]

where Z is L147's finite, possibly empty, split-parameter set. Give G
the tensor product metric. On M|_U use precisely L148's harmonic L2
metric H, under the natural higher-image/Dolbeault identification and
the fixed fibre metric g. F and a nonempty Z are not asserted to exist.

## Conclusion

The Chern connection of the given Hermitian holomorphic bundle
(M|_U,H) is the natural hyperkähler transform connection. It is a
Hermitian quaternionic instanton and, for the original metric and
complex orientation on U, its curvature satisfies

\[
                         *_g F_{\nabla_H}=-F_{\nabla_H}.       \tag{1}
\]

The positive transform bundle has complex rank 24. The alternating
Dirac index is its negative; that sign does not negate its connection
or metric. No real structure on G or M is required.

This is a conditional REPRODUCTION/specialization of known transform
theorems. The separate critical audit below preserves the conclusion
without a substantive correction or stronger result. It establishes the equation
of the specified connection only on U. It gives no curvature bound at
Z, finite-energy assertion, metric or connection extension, whole-base
IT, polystability of M on B, split-count bound, kernel existence, cycle
or transport. Universal primitive Hodge realization remains unresolved.

## Proof

**Imported preservation and Hermitian comparison.** Reuse the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-stable-open-connection.md`.
Import Bartocci, Bruzzo and Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications 8 (1998),
239–249: [Section 3.1 p. 243, Definition 2 p. 244, Section 3.3
Lemmas 1–2 and Theorem 3 pp. 245–246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
The source X is compact; the hyperkähler target Y is not required to
be compact or complete. For a Hermitian quaternionic-instanton kernel
Q on X x Y and source instanton E satisfying IT, these results transfer
IT to the induced structures and identify the transform naturally as
a holomorphic Hermitian bundle with the index construction. The same
index connection descends and is a quaternionic instanton on Y.

For the projected connection and its metric interpretation, use
Bartocci–Jardim, *Hyperkahler Nahm transforms*,
[arXiv:math/0312045v1, Theorem 2 and its proof p. 4](https://arxiv.org/pdf/math/0312045v1#page=4),
and Bruzzo, Hernandez Ruiperez and Tejero Prieto, *Introduction to
Fourier-Mukai and Nahm transforms with an application to coherent
systems on elliptic curves*, author-hosted `DerCatCohSyst3-v4.pdf`,
[Sections 3.2–3.4, PDF pp. 21–24, Theorems 3.4–3.5 and 3.7](https://mat.usal.es/ruiperez/Site/Papers_files/DerCatCohSyst3-v4.pdf#page=21).
Section 3.2 restricts the fibre L2 product to the Dirac realization;
Section 3.3 treats a general Hermitian holomorphic kernel and identifies
the induced connection as Chern immediately after Theorem 3.4.
Theorem 3.5 identifies its holomorphic higher image. The published
BBHR theorem is the preservation input; the notes clarify the same
metric/connection construction, without a universal-kernel hypothesis.

Do not use the compact-target higher-image statement of Bartocci–Jardim
Theorem-Definition 3 as the localization input. Also do not use the
notes' inconsistent printed IT parity label: the actual even-degree
vanishings and Dirac chiralities below determine the bundle. These
general theorems are imported, not reproved. The remaining argument
checks their applicability to this coefficient and this metric.

**The specified line connection is a source instanton.** The Chern
curvature F_L of h_L is of type (1,1) for I. Its HE contraction is a
constant proportional to k.h, hence zero. Thus F_L is primitive (1,1)
pointwise, rather than merely representing a degree-zero class.
On a Kähler surface with its complex orientation, the self-dual real
two-forms are the Kähler line together with the real (2,0)+(0,2)
plane. On this hyperkähler surface they are spanned by
omega_I, omega_J and omega_K. Consequently F_L is orthogonal to all
three and is ASD, coefficientwise in the unitary line algebra.

Dualizing changes its curvature to -F_L, which is still ASD. For
every induced structure R=aI+bJ+cK, its Kähler form lies in that same
self-dual three-plane. An ASD two-form is primitive (1,1) for R.
Therefore (L^{-1},h_L^{-1},nabla_{L^{-1}}) is a Hermitian quaternionic
instanton on the compact source S_1 with exactly the chosen connection.
This verifies full triple orthogonality, using the HE equation in
addition to k.h=0. No arbitrary twisting-line metric is substituted.

**Restricted kernel and the open target.** Take X=S_1, Y=U,
Q=F|_{S_1 x U}, E=L^{-1}. By L071, Q with its actual metric and
connection is a Hermitian quaternionic instanton for simultaneous
induced structures on the product. Restriction to the open target
preserves this pointwise curvature property. The coefficient E tensor
Q is precisely G|_{S_1 x U}, with precisely its stated metric and
tensor connection: its curvature is

\[
 F_{\nabla_G}=F_{\nabla_F}\otimes 1
                  +1\otimes p_1^*F_{\nabla_{L^{-1}}}.
\]

Both summands have the required invariant type. U inherits the original
hyperkähler metric. Projection S_1 x U -> U is proper: the inverse
image of a compact subset C is the compact product S_1 x C. It is
also a smooth holomorphic product projection, and its algebraic
properness follows by base change from p_2. Target noncompactness
causes no failure of the source-compact preservation setup.

**Actual IT, including rotations.** L147 proves for every b in U

\[
 H^0(S_1,G_b)=H^2(S_1,G_b)=0,\qquad h^1(S_1,G_b)=24.       \tag{2}
\]

In particular it proves these vanishings for the actual twist, by
slope stability of F_b and its degree-zero line twist, dual stability
and K3 Serre duality. Perfect concentration identifies the natural
ordinary bundle M|_U with that degree-one higher image. These are
all even degrees on a complex surface, so they are exactly odd IT
in BBHR Definition 2.

Apply the inspected rotation statement in BBHR Section 3.3/Lemma 1
only after the instanton hypotheses above have been checked. One can
track its chirality in this specialization explicitly. For the fixed
spin structure and metric on S_1, the coupled Dirac operators have,
under the parallel spin/Dolbeault identification for I,

\[
 \ker D_b^+\simeq H^0(S_1,G_b)\oplus H^2(S_1,G_b)=0,
 \qquad \ker D_b^-\simeq H^1(S_1,G_b).                  \tag{3}
\]

Here even Dolbeault degree is positive chirality, and D^- is the
adjoint of D^+. The parallel trivialization of the canonical square
root gives the Hermitian spin/Dolbeault identification used in the
sources. Rotating the induced structure changes that identification,
not the underlying metric spin Dirac operator or coefficient
connection. Hyperholomorphicity makes the rotated Dolbeault operator
integrable, so the same identification applies for each R. The zero
positive kernel therefore means both rotated even cohomology groups
vanish separately, while the negative kernel still has dimension 24.
This is the source's rotation-IT mechanism in this surface case; no
stability assertion in an unchosen algebraic polarization is needed.

Equation (2) holds at every point of U, so the kernels in (3) form a
smooth positive rank-24 bundle V there. Local smooth dependence of
elliptic harmonic projections uses constant kernel dimension on U;
no spectral gap uniform toward Z is asserted. At z in Z, L147 gives
derived dimensions (1,26,1), so no whole-base IT is used. When Z is
empty the same argument simply has U=B. With the stated chirality,
Ind(D^+)=[ker D^+]-[ker D^-]=-[V].

**Identification with the given harmonic Chern connection.** At the
original I, identify V_b with the harmonic G_b-valued (0,1)-forms
using (3). Its metric is the restriction of

\[
             (s,t)_{L^2,b}=\int_{S_1}\langle s,t\rangle_{g,h_G}
                                      \,d\operatorname{vol}_g.
                                                               \tag{4}
\]

The natural cohomology map sends a harmonic form to its Dolbeault
class, and the natural higher-image map then identifies this class
with M_b. These are exactly L148's maps on U, not an arbitrary
holomorphic isomorphism or a choice of abstract rank-24 frame.
L148's harmonic norm is defined by (4), so this identification is a
Hermitian isometry. The usual fixed normalization of the isometric
spin/Dolbeault map may be chosen once on the fixed source; even a
single constant positive normalization would leave the Chern
connection unchanged.

In product notation the transform connection is

\[
             \widehat\nabla_v s=P_b\,\nabla^{\mathcal H}_v s,
                                                               \tag{5}
\]

where P_b is the orthogonal harmonic projection and mathcal H is the
bundle of fibre spinor sections with coefficient G. Its horizontal
connection uses the actual horizontal coefficient connection of F;
the pulled-back source line and the source spin metric are fixed in
the base direction. There is no assumed global flat trivialization of
Q. The fixed product fibre metric has no varying-volume correction.

The natural holomorphic Hermitian comparison in BBHR Lemma 2 and
the Chern identification in the cited notes apply to this very (5).
Thus its (0,1) operator is the natural higher-image holomorphic
structure and its metric is H under the isometry just described.
Equivalently, horizontal (0,1) differentiation of a vertically closed
representative gives that higher-image Dolbeault operator; total
integrability allows it to pass to cohomology, and harmonic projection
selects its representative. Formula (5) is unitary for (4). The unique
connection with these two properties is the Chern connection nabla_H.
This is Chern uniqueness for a specified holomorphic metric, not HE
metric uniqueness on the noncompact target. No scalar self-duality,
real structure on G, or extension of P_b across Z is involved.

**Preservation and the four-dimensional conclusion.** The compact
source, restricted Hermitian instanton kernel, source instanton,
rotation-IT and actual Hermitian identification have now all been
matched. BBHR Theorem 3 makes (V,widehat nabla) a quaternionic
instanton on U. By the preceding identification this is nabla_H.
In real dimension four, a two-form of type (1,1) for every induced
structure has no component along any of omega_I, omega_J, omega_K:
for example (1,1) for I removes the J,K components, and (1,1) for J
removes the I component. This applies coefficientwise to the
curvature. Those three forms span the self-dual part for the original
metric and complex orientation, proving (1).

Only the stable-open equation is obtained. In particular the
curvature criterion of L149 and central cancellation of L150 have
not been applied, and no surface removal or Chern inequality is
invoked. The arbitrary-weight and automatic-extension failures in
ATTEMPTS/063, /066 and /086 remain unchanged.

**Separate critical audit, 2026-10-23 (step 489).** Reuse the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-stable-open-asd-critical-audit.md`
and the completed step-485 primary theorem/proof-case record. The
published BBHR preservation and natural Hermitian comparison, and the
author-note Chern construction at the precise locations cited above,
are imported inputs. This audit checks their application; it does not
reprove the preservation theorem or claim a result beyond those sources.

First retain the actual metric hypotheses. L094 fixes a smooth HE
metric on L, not merely the numerical condition k.h=0. Its Chern
curvature has no (2,0) or (0,2) part, and its contraction with omega_I
vanishes pointwise by the zero HE constant. Thus its self-dual
projection is zero in the complex orientation. Dualization preserves
this assertion. The hyperkähler triple spans the same self-dual
space for every induced structure, so the precise dual connection is
an instanton for all of them. L071 supplies the product-compatible
connection on F. Tensoring these two connections and restricting to
S_1 x U preserves their invariant type; no claim about an arbitrary
weight on L^{-1} is used. U is open in each induced complex structure
and has the restricted smooth metric, whether or not Z is empty.
Compactness of S_1 makes the product projection proper. This matches
BBHR's compact-source setup without silently adding target compactness
or completeness. The compact-target statement of Bartocci–Jardim
Theorem-Definition 3 remains unused for this step.

Second check concentration and chirality on the same coefficient.
L147's stable-open argument applies to G_b itself: tensoring by the
degree-zero line preserves slope stability; a nonzero section would
give a rank-one subsheaf O of the same slope, and dual stability kills
H^2 by K3 Serre duality. Its fibre character is
2-2k-28 eta, so its Euler characteristic is -24 and its sole
cohomology has dimension 24. These vanishings hold at every b in U,
not just generically. The spin structure on a K3 is unique since
H^1(S_1,Z/2)=0. For each induced structure R its canonical square
root has a parallel unit trivialization. The spin/Dolbeault
identification therefore identifies the same coupled spin operator
with sqrt(2)(bar-partial_R+bar-partial_R^*) and preserves chirality:
even degree is positive and odd degree negative in this orientation.
The metric, spin connection and coefficient connection are unchanged
by R. Consequently the zero positive kernel for I remains zero for
each R, and its decomposition into degrees zero and two makes both
rotated groups vanish separately. The negative kernel has rank 24.
Neither a real structure on G nor algebraic stability for a rotated
polarization enters this argument. Local spectral separation follows
from constant kernel dimension and ellipticity on the compact source
near each b in U; it supplies smooth projections only there. At Z
the stated dimensions (1,26,1) explicitly prevent this concentration.
The index -[V] does not replace V by a virtual negative metric bundle.

Third test the natural connection rather than only its isomorphism
class. Fix I and use the isometric spin/Dolbeault map once on the
source, independently of b. Let d_b denote the vertical Dolbeault
operator and let B_{bar v} denote horizontal (0,1) differentiation
using the actual Chern connection of G and the fixed vertical form
bundle. For a product horizontal lift bar v, coefficient integrability
gives

\[
 [B_{\bar v},d_b]=0,\qquad
 B_{\bar v}(d_b u)=d_b(B_{\bar v}u).                    \tag{6}
\]

Here the bracket uses the usual relative-form convention; equivalently
the mixed component of the square of the total Dolbeault differential
is zero. The coefficient of that component is
F_G(bar v,bar w)=0 for every vertical (0,1) vector bar w. Vertical
frame derivatives are absent in the fixed product form bundle.
Thus horizontal differentiation carries closed representatives to
closed representatives and exact representatives to exact ones.
The operator it induces on their cohomology is exactly the
higher-image (0,1) operator, obtained from the relative Dolbeault
resolution of this same holomorphic family. For a smooth harmonic
section s, the natural cohomology map q consequently satisfies

\[
 \bar\partial_M q(s)(\bar v)
       =q(B_{\bar v}s)=q(P_b B_{\bar v}s).              \tag{7}
\]

The second equality is Hodge decomposition of a closed form on the
compact fibre. It does not differentiate a singular projection at Z.
This verifies the natural holomorphic part of the source comparison
in the actual higher image used by L148, with its horizontal kernel
connection retained. In particular it uses no flat trivialization of F.

For real horizontal v, metric compatibility of B_v and the fixed
source volume form give

\[
 v H(s,t)=H(B_vs,t)+H(s,B_vt)
        =H(P_bB_vs,t)+H(s,P_bB_vt).                    \tag{8}
\]

Orthogonality of P_b gives the last equality for harmonic s,t.
There is no varying fibre metric or density term. Under q, H is
exactly L148's harmonic metric because both use the same tensor
metric on G and the same fibre integration. Equations (7) and (8)
show that the projected transform connection is unitary and has
the specified holomorphic (0,1) part. Chern uniqueness, which is
local and requires no compactness or stability of U, identifies it
with the Chern connection of (M|_U,H). A constant normalization of
the spin isometry has no effect on this conclusion. No base-dependent
rescaling or abstract replacement metric has been introduced.

Finally apply the imported preservation theorem to this identified
connection. Its curvature is (1,1) for I,J,K. For each endomorphism
coefficient, the first condition kills the omega_J and omega_K
self-dual components; the second kills the omega_I component.
Thus the entire curvature, including its unitary central part, is
ASD at g. This does not require a symplectic or real reduction of V.
All four applicability bridges survive. No substantive error or
stronger obstruction has been found; the completed audit is
EXPLORATION / REPRODUCTION, not a new mathematical advance.

The direct inputs remain L071, L094, L147 and L148. The use of L148
here is its specified natural harmonic metric, not its singular norm
estimate. L149 and L150's conclusions remain downstream and do not
enter this proof. The audit supplies no curvature estimate at Z,
energy bound, extension on the particular M, positivity, count bound,
F, nonempty Z, cycle or transport. ATTEMPTS/063/066/086 remain valid
stops for their own unsupported inferences. Universal primitive Hodge
realization is unchanged.

## Mathlib

Full Mathlib coverage of the hyperkähler transform theorem, its
natural harmonic Hermitian/Chern identification and this open-target
specialization is **not checked**. No matching theorem or absence
is asserted. The cited primary preservation theorem and inspected
author-note connection construction are imported inputs; the line,
properness, IT, chirality and actual-metric verifications above are
the local specialization. No Lean formalization is claimed.

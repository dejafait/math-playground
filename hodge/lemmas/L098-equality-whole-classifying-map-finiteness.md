# L098 — Conditional equality-family whole classifying map is finite

## Hypotheses

Retain L097's identical marked smooth projective complex K3 surfaces
S_1 and B=S_2, their common hyperkähler metric g and ordered structures
I,J,K, the real class h and Omega=p_1^*h+p_2^*h. Retain the full
integral self-adjoint tensor tau_D, with D[sigma]=2lambda[sigma] and
1<lambda<5/4, and the zero-slope divisor lattice Z k, k^2=-14.
Let L on S_1 have c_1(L)=k.

Suppose F on S_1 x B is locally free of rank two, Omega-slope-polystable,
with integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D. Use the actual
connection and harmonic mixed-curvature derivative of audited L095.
Use audited L096's finite set Z of nonstable closed fibres, possibly
empty, and audited L097's very ample integral H and whole morphism

\[
 f:B\longrightarrow M=M_H^{ss}(2,0,-12).
\]

Thus M is projective over C, f classifies the actual algebraic flat
family, U=B\setminus Z_red=f^{-1}(M^s), and every point of Z maps to
the same closed point m_0=[L\oplus L^{-1}]. The finite reduced closed
subscheme Z_red is only a convenient complement; it is not a claim
about the scheme structure of any jump locus or fibre.

## Conclusion

The whole morphism f is finite. Its scheme-theoretic image W in M
is the reduced induced closed subscheme on f(B). The actual factor
g:B -> W is finite and surjective. On U the map to M^s is unramified.
No unramifiedness at Z, reducedness of f^{-1}(m_0), degree-one,
separation of distinct parameters, normality, flatness or embedding
is asserted.

This is a conditional ADVANCE / REPRODUCTION of the previously
assessed known tools. The separate critical audit below preserves it. The
threshold of whole-map finiteness is met under the retained inputs;
existence of F, integrated compatible germs, global separation,
reconstruction and transverse transport remain unresolved. No new
cycle or universal Hodge resolution is supplied.

## Proof

**Scope and cited tools.** The pre-invocation SPECIALIZE assessment
is drafts/literature/2026-10-12-equality-classifying-map-finiteness.md.
The charge-seven L064 is a methodological comparison only: none of
its family-specific conclusions is an input. The general natural
tangent, GAGA, curvature-representative and scheme theorems below
are imported; only their applicability to this changed family is
proved. Their reproof is unnecessary.

**Natural coarse tangent on the actual stable family.** Import
Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*, Aspects
of Mathematics E31 (1997),
[Theorem 4.5.1 and Corollary 4.5.2, printed p. 101](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113).
At a stable sheaf the completed coarse local ring prorepresents
its deformation functor, and its tangent is naturally Ext^1(E,E).
The theorem's family transformation and etale-slice inverse make
this identification compatible with the classifying differential.
The scalar-automorphism scope is that of
[Lemma 4.3.2 and Corollary 4.3.5, pp. 89--91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=101).
It requires no global universal sheaf. L097's fixed-numerical-class
part is open and closed, so its stable local rings and tangents
are the same as those in the fixed-polynomial stable scheme.

Fix a closed y in U, put E=F_y and m=f(y). For an algebraic tangent
v at y, pull the actual family back to Spec A, A=C[epsilon]/(epsilon^2).
Its identified central fibre is E. Naturality of L097's classifying
transformation sends this pullback to the composite tangent f(v).
As an O_{S_1}-module, its base-flat middle term F_v gives

\[
 0\longrightarrow E\xrightarrow{\epsilon}F_v
                 \longrightarrow E\longrightarrow0.             \tag{1}
\]

Under the natural coarse tangent theorem, df_y(v) is precisely the
Ext^1 class of (1), with both end identifications fixed. This is also
the flat-deformation description in
[Huybrechts--Lehn 2.A.6, p. 50](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=62).

Because E is locally free, Ext^1(E,E)=H^1(S_1,End E). Import exact
analytification and natural coherent-cohomology comparison from
Serre, *Geometrie algebrique et geometrie analytique*, Ann. Inst.
Fourier **6** (1956),
[sections 9, 11--13, Proposition 10 and Theorem 1, pp. 16--22](https://www.numdam.org/article/AIF_1956__6__1_0.pdf#page=19),
and the named Dolbeault theorem for holomorphic vector bundles.
Here S_1 is projective and End E is coherent. Analytification retains
(1), its central identification and local splittings. Their differences
give the same End E-valued Cech cocycle, whose natural Dolbeault image
is the deformation of the actual relative holomorphic structure.
The algebraic tangent of smooth B agrees with its analytic (1,0)
tangent. Thus df_y corresponds to the actual family Kodaira--Spencer
map into H^{0,1}(S_1,End E); this is a comparison of the same extension,
not a choice of tangent-space isomorphism. We use the full Ext^1
tangent, without replacing it by a fixed-determinant tangent functor.

**Match L095's actual real derivative to that class.** Import
Biswas--Schumacher, *Geometry of moduli spaces of Higgs bundles*,
[math/0605589v1 (22 May 2006), Section 3, Lemma 3.3 and equation (12), printed p. 7](https://arxiv.org/pdf/math/0605589v1#page=7).
For a holomorphic family with a smooth Hermitian metric, its mixed
Chern curvature gives the bundle component of the Kodaira--Spencer
representative. Apply this to F over S_1 x U with zero Higgs field
and its actual given Hermitian metric. The bundle component is the
ordinary H^{0,1}(End E) class; the Higgs-variation component is zero.
L095 already supplies harmonicity, so we need neither a new family
metric nor Proposition 3.4 at a split parameter.

For real u in T_yB write r_u(t)=R(u,t). By L095, r_u is skew-adjoint,
ASD-harmonic and Dolbeault-harmonic in its (0,1) part. Also

\[
 r_{Iu}=I_c r_u,\qquad (I_c a)(t)=-a(It),\qquad
 G_y(r_u,r_u)=2lambda g(u,u).                              \tag{2}
\]

Every analytic (1,0) tangent v has the unique expression
v=(u-iIu)/2, with u=v+\bar v real. If \bar t is a fibre (0,1)
vector, I\bar t=-i\bar t, so r_{Iu}(\bar t)=i r_u(\bar t).
Consequently the complexified actual mixed curvature satisfies

\[
 R(v,\bar t)=\tfrac12(r_u(\bar t)-i r_{Iu}(\bar t))
                         =r_u(\bar t).                    \tag{3}
\]

Equations (1)--(3) and the cited representative formula therefore
identify the class of df_y(v) with [r_u^{0,1}] in our curvature
convention. Reversing the common curvature/KS sign convention changes
this by a nonzero overall sign and cannot affect injectivity.

If df_y(v)=0, the harmonic representative r_u^{0,1} is zero by
uniqueness of Dolbeault harmonic representatives on the compact
Kähler fibre. Skew-adjoint reality gives r_u=b-b^*, b=r_u^{0,1},
and hence r_u=0. The positive norm in (2) forces u=0, then v=0.
This proves complex tangent injectivity at every closed point of U.
Only stable sheaves were used in the coarse tangent theorem. The
same raw derivative at a split fibre is not assigned a coarse tangent.

**All scheme points of the stable open.** B and M are finite-type
C-schemes, and f is locally of finite type (on affine charts a
finite generating set over C also generates over the target algebra).
Its restrictions are likewise locally of finite type. At each closed
y in U, both y and f(y) have residue field C. Apply the Stacks Project,
[Lemma 33.16.8, Tag 0B2G](https://stacks.math.columbia.edu/tag/0B2G),
to the tangent injectivity just proved: f|_U is unramified at y.
The unramified locus is open by
[Definition 29.36.1, Tag 02G4](https://stacks.math.columbia.edu/tag/02G4).
If its closed complement in U were nonempty, that finite-type
C-scheme would contain a closed complex point, contrary to the
preceding argument. Thus f|_U is unramified at every scheme point.
By [Lemma 29.36.10, Tag 02V5](https://stacks.math.columbia.edu/tag/02V5),
it is quasi-finite everywhere on U. This uses residue-field equality
only at closed complex points, not at arbitrary generic points.

**The full exceptional fibre.** The point m_0 is outside M^s: its
two nonisomorphic line summands have the equal reduced polynomials
checked in L097. Since U=f^{-1}(M^s), no scheme point of U maps to
m_0. Every point of B outside U lies in the finite closed support
of Z_red. Conversely L097 sends every point of Z to m_0. Therefore

\[
                   f^{-1}(\{m_0\})=Z                     \tag{4}
\]

as sets of all scheme points, not just as a list of complex points.
This is also valid when Z is empty. In particular, no generic point
of a positive-dimensional fibre was omitted. The fibre scheme may
have nilpotents; its full underlying set is nevertheless finite.
Apply [Stacks Lemma 29.21.7, Tag 02NG](https://stacks.math.columbia.edu/tag/02NG)
to the locally finite-type f and (4): f is quasi-finite at every
point over m_0. All points outside U lie over m_0. Together with the
stable-open check, f is locally quasi-finite on the whole B. No
split coarse derivative or unramifiedness at those points is needed.

**Whole-map finiteness.** B is proper over C and M is separated
over C by projectivity. The Stacks Project,
[Lemma 29.42.7, Tag 01W6](https://stacks.math.columbia.edu/tag/01W6),
makes the actual morphism f proper. Apply
[Lemma 37.44.1, Tag 02LS](https://stacks.math.columbia.edu/tag/02LS):
proper and locally quasi-finite implies finite. This is an application
to the whole map, after checking every source scheme point; no
replacement of a full-fibre hypothesis by closed fibres is made.

**The reduced image and its actual factor.** Since f is finite,
the quasi-coherent kernel ideal

\[
                 \mathcal I=\ker(\mathcal O_M\to f_*\mathcal O_B)
\]

defines its scheme-theoretic image W and the factorization
f=j\circ g, with j:W\hookrightarrow M a closed immersion. This is
the quasi-compact kernel-ideal description in the Stacks Project,
[Lemmas 29.6.1 and 29.6.3, Tag 01R5](https://stacks.math.columbia.edu/tag/01R5).
B is reduced; [Lemma 29.6.7, Tag 056B](https://stacks.math.columbia.edu/tag/056B)
therefore identifies W with the reduced induced structure on the
closure of f(B). Properness makes f(B) closed, so this closure is
f(B) itself. The actual factor g exists by the scheme-theoretic
image construction, without assuming image normality.

Since j is separated and j\circ g=f is finite,
[Lemma 29.45.14, Tag 035D](https://stacks.math.columbia.edu/tag/035D)
makes g finite. Its underlying image is all |W|=f(|B|), hence g
is surjective. Finiteness, factorization and surjectivity are thus
separate verified passages. None implies flatness, generic degree
one, identification of the normalization or a closed embedding.

The local intermediate threshold is reached conditionally. No complete
Hodge candidate follows. The independent existence and transport gaps
and all earlier representative/curvature stops remain intact.

**Separate critical audit, 2026-10-13 (step 256).** The pre-invocation
SPECIALIZE scope is
drafts/literature/2026-10-13-equality-whole-map-finiteness-critical-audit.md.
This audit reuses its primary coverage and the forward assessment;
it tests the actual application rather than reproving the general
theorems. Its outcome is EXPLORATION / REPRODUCTION: no substantive
mathematical error or stronger conclusion was found. The conditional
statement above survives, without a new lemma or originality claim.

First check the input scope, including the empty exceptional set.
L097 supplies the actual morphism, projective target and exact
stable-open preimage for the same F, H and metric. L096 supplies a
finite set of closed complex points, not a reduced-fibre theorem.
Although L095 also chooses a split point for its slice conclusion,
its coefficient-Bianchi, quaternionic-Coulomb and raw-pairing proofs
use only the actual product connection and the full prescribed
character. Those arguments run at every y without choosing any
split point. Specifically, the ASD projection of the horizontal
commutator is zero, the identity C_I(I_c r_u)=C_0(r_u) gives Coulomb
gauge, and the holomorphic fibre integral fixes c(y)=2lambda
pointwise on B. The chosen split point is used only to identify the
additional split harmonic representation. Thus the all-fibre
harmonicity and norm imported here do not require Z to be nonempty.

Next check the actual stable deformation. At y in U the fibre is
Gieseker-stable for the chosen H, so the natural family transformation
of Huybrechts--Lehn 4.5.1 applies to its completed coarse local ring.
The numerical-class restriction does not alter this local ring.
Flatness over A identifies epsilon F_v with F_v/epsilon F_v=E;
therefore (1) really has the displayed two identified end terms.
The natural tangent theorem assigns its extension class to df_y(v).
Scalar automorphisms act by conjugation trivially on Ext^1; they do
not introduce an extra tangent quotient or a needed universal bundle.
Exact analytification and the natural cohomology comparison keep
the extension and its end identifications. Local splittings compute
its class on both sides, so the Dolbeault image is the actual KS
class, not an arbitrarily chosen isomorphism of tangent spaces.

For completeness, the real-to-complex passage can be checked before
taking cohomology. The quaternionic formula gives
R(Iu,bar t)=-R(u,I bar t)=iR(u,bar t). Substitution of
v=(u-iIu)/2 therefore gives exactly R(v,bar t)=R(u,bar t).
The mixed-curvature representative theorem applies to this actual
Hermitian holomorphic family; harmonicity is supplied by L095,
not by applying a stable-family theorem at a reducible point.
Writing b=r_u^{0,1}, skew-adjoint reality says that the (1,0) part
is -b^*, where the star includes conjugation of the form leg.
Consequently a zero harmonic Dolbeault class forces b=0 and the
whole real r_u=0. Its positive squared norm is 2lambda g(u,u),
with 2lambda in (2,5/2), so no nonzero u is lost in this comparison.
This checks complex tangent injectivity, including its normalization,
without making any assertion about the split coarse tangent.

For the passage to all points, f and its stable restriction are
locally of finite type, and U is a finite-type C-scheme. A closed
point y in U and its image both have residue field C. These are
exactly the hypotheses needed for 0B2G. The complement of the open
unramified locus is a closed subset of U; if nonempty it has a
closed complex point. Such a point is also closed in B and was
already tested. Thus no nonclosed point can be an overlooked
failure of unramifiedness on U. Tag 02V5 then gives local
quasi-finiteness there.

At the exceptional value the argument uses a stronger input than
merely a list of closed fibres. The equality U=f^{-1}(M^s) is an
equality of open subschemes, and m_0 is strictly semistable.
Therefore every scheme point over m_0 lies in |B| minus |U|=Z.
All points of this complement are closed, all map to m_0, and
there are finitely many. Hence (4) describes the entire underlying
fibre, even if the fibre scheme is nonreduced. If Z is empty the
fibre is empty and this check is vacuous. Tag 02NG applies in either
case. Any other target fibre has all of its preimage in U. These
two checks exhaust every source point before 02LS is invoked.

Finally, properness uses the actual proper source B and separated
target M through 01W6, so proper local quasi-finiteness indeed makes
the whole f finite. The kernel-image construction applies because
f is quasi-compact. Reducedness can also be seen directly in this
application: if a local section a has a power in the kernel, its
pullback has zero power on the reduced open preimage in B, hence
is zero. Thus the kernel ideal is radical, in agreement with 056B.
Properness supplies closedness of f(B); reducedness alone would not.
For the actual factor g through this image, the second morphism j
is a closed immersion and is separated, exactly as required by
035D. Its finite conclusion concerns g with this scheme structure.
Its image contains every point of W because |W|=f(|B|), giving
surjectivity separately. No normality, flatness or degree statement
has entered the proof.

The direct mathematical inputs remain L095, L096 and L097; L064
is only a comparison of methods. No dependency is added or removed.
The audit preserves the finite whole map, finite surjective reduced
image factor and unramified stable restriction, and leaves every
existence, global separation and transport limitation in place.

## Mathlib

Full matching coverage of the natural stable coarse-sheaf tangent
bridge and this combined conditional whole-image finiteness result:
**not checked**. Unknown coverage is not absence. The precise primary
theorems above are the mathematical references. This is a scoped
specialization of known tools, with no originality or beyond-source
claim; the separate critical audit preserves the stated scope.

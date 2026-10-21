# L121 — Conditional opposite coincidences are finite and reduced

## Hypotheses

Retain L118 and L120's conditional setting in full. Thus
X=B x Y=S_1 x S_2 consists of the identical marked smooth projective
complex K3 surfaces, with common hyperkähler metric g, ordered structures
I,J,K, real ample class h and product polarization Omega. Put
e_1=eta tensor 1 and e_2=1 tensor eta, with integral_S eta=1.
The full integral mixed tensor tau_D has self-adjoint cup operator
D, with D[sigma]=2lambda[sigma], sigma=omega_J+i omega_K and
1<lambda<5/4. Suppose F is holomorphic locally free of rank two,
Omega-slope-polystable, with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use L118's actual opposite stable classifying morphism

\[
 f:B\longrightarrow M=M_H^s(2,0,-19),\qquad
 x\longmapsto[F|_{\{x\}\times Y}],
\]

with its natural differential and compatible connection-moduli charts.
In those charts the harmonic hyperkähler metric G is normalized by
f^*G=2lambda g; df commutes with I,J,K, and the parametrized map
is totally geodesic for the original source connection. L120 supplies
f finite and unramified and identifies B with the normalization of its
integral reduced scheme-theoretic image Z. In particular B -> Z is
finite birational. Neither normality of Z nor existence of F is assumed.

## Conclusion

Let R=B x_M B with its actual algebraic fibre-product scheme structure,
and let

\[
                      R_{\rm off}=R\setminus\Delta_B.
\]

Then R_off is a finite reduced C-scheme, possibly empty. At every closed
point (x,y) of R_off, the two real quaternionic tangent lines
df_x(T_xB) and df_y(T_yB), viewed in the same connection-moduli tangent
space, are distinct and have intersection zero. Its local ring is C.
In particular off-diagonal coincidences cannot accumulate at the
diagonal. No bound on their number or emptiness is proved.

This is a conditional local ADVANCE / REPRODUCTION of the assessed
geodesic and scheme tools. It is not a new general theorem claim beyond
the inspected literature. The separate critical audit below preserves it. It
supplies neither F, a globally injective map, normality of Z, an extra
algebraic Hodge class, reconstruction nor transverse transport.

## Proof

**Scope and known inputs.** The pre-invocation assessment is
`drafts/literature/2026-10-17-opposite-coincidence-scheme-finiteness.md`,
whose decision is EXPLORE. The direct mathematical inputs are audited
L118 and audited L120. L071's connection and tensor hypotheses are
retained through those inputs, rather than reapplied here. The earlier
two-branch source comparison did not force equality of tangent lines;
this proof instead excludes equality at a collision and allows distinct
lines. ATTEMPTS/046's isolated Hom-jump alternative is not excluded by
the conclusion, and its stopped Euler method is not repeated.

The needed geodesic uniqueness is the standard named
Picard--Lindelöf uniqueness theorem for the smooth geodesic ODE,
together with the inverse function theorem for exponential charts.
We specialize these local tools below; we do not reprove L118's
hyperkähler embedding theorem or use a global injectivity theorem.
For the scheme passages import
[Stacks, Lemma 29.36.13 (02GE)](https://stacks.math.columbia.edu/tag/02GE),
which characterizes an unramified morphism, locally of finite type,
by its diagonal being an open immersion, and
[Lemma 37.44.1 (02LS)](https://stacks.math.columbia.edu/tag/02LS),
which implies that a proper locally quasi-finite morphism is finite.
Their full statements and proofs were inspected in the saved assessment;
that unchanged coverage is reused. The elementary tangent, Nakayama and
birational-open arguments below are written out to keep track of this
actual scheme and avoid an assumption on the singular image.

**Common charts at a collision.** Let x != y be complex points with
f(x)=f(y)=m. Both fibres are stable by L118. Its same-extension
coarse/connection germ comparison places neighborhoods of x and y in
one smooth connection-moduli neighborhood V of m, of complex dimension
78. The harmonic L2 metric, induced triples and their normalization
are defined on this same V. Indeed an isomorphism of the two stable
fibres identifies their HE connections up to unitary gauge after a
constant rescaling of the fibre metric; scalar ambiguity acts trivially
on End-valued harmonic classes. L118 checks precisely this metric and
triple compatibility on chart overlaps. Thus the two actual natural
derivatives may be compared in T_mV without choosing unrelated metrics.

Let P_x=df_x(T_xB) and P_y=df_y(T_yB), as real subspaces of T_mV.
Injectivity and quaternionic equivariance in L118 make each a real
four-dimensional quaternionic line. If they have a nonzero common
vector a, both contain a,Ia,Ja,Ka. These four vectors are independent:
the quaternionic metric makes them orthogonal of the same nonzero
norm. Hence P_x=P_y. Otherwise their intersection is zero. We must
rule out the equal-line case, rather than assume it is forced.

**Equal tangents would give two copies of an open branch.** Suppose
P_x=P_y=P. Take disjoint small source neighborhoods about x and y.
Give B the metric 2lambda g, whose Levi-Civita connection equals that
of g. The parametrized geodesy identity of L118 says that f sends a
source geodesic to an ambient geodesic with the same affine parameter.
Uniqueness of that ODE, for sufficiently small initial vectors, gives

\[
 f(\exp_x v)=\exp_m(df_xv),\qquad
 f(\exp_y w)=\exp_m(df_yw).                         \tag{1}
\]

All exponential maps here are local; a smooth ambient metric on V
suffices. By the inverse function theorem, shrink the neighborhoods
and choose a small ball W around 0 in P so that both df_x^{-1}W and
df_y^{-1}W lie in the respective exponential domains, with their images
still disjoint. Also require exp_m to be injective on an ambient
neighborhood containing W. Then (1) identifies each of the two open
source neighborhoods

\[
 U_x=\exp_x(df_x^{-1}W),\qquad
 U_y=\exp_y(df_y^{-1}W)
\]

bijectively with the same set exp_m(W). They are open in the real,
equivalently complex analytic, topology of B, since df_x and df_y are
isomorphisms onto P. This is equality of the actual local images; it
does not extend a local source isometry to B.

For clarity, finite birationality provides a nonempty Zariski open
Z^o of Z over which g:B -> Z is an isomorphism. Here is the elementary
application. Choose a nonempty affine Spec A in integral Z. Its inverse
image is Spec A', with A' finite over A and the same fraction field,
by L120. For a finite set of A-module generators of A', choose a common
nonzero denominator s in A in that fraction field. Then A'_s=A_s.
The open Spec A_s is such a Z^o. Its inverse image is a nonempty
Zariski open in irreducible smooth B and meets U_x: a proper algebraic
closed subset of a connected complex manifold cannot contain an
analytic open set, by the holomorphic identity theorem.

Choose b in U_x intersect g^{-1}(Z^o). Equation (1) supplies b' in
the disjoint U_y with f(b')=f(b). Since Z -> M is a closed immersion,
g(b')=g(b) lies in Z^o. This contradicts the isomorphism over Z^o.
Consequently P_x and P_y cannot be equal at any off-diagonal collision.
Their intersection is therefore zero. Generic degree one is used only
in this open-branch contradiction; it is not substituted for separation.

**The actual off-diagonal local ring.** The algebraic morphism f has
the natural differential used above, by L118. The dual-number
description of a fibre product gives, at a closed r=(x,y),

\[
 T_rR=\{(u,v)\in T_xB\oplus T_yB:df_xu=df_yv\}.       \tag{2}
\]

These are complex Zariski tangents. Their underlying real images agree
with the I-invariant subspaces just compared, so their intersection
is zero. Each df is injective. Hence (2) is zero. Passing to the open
R_off does not change this local tangent or local ring.

Write A_r=O_{R_{off},r}, with maximal ideal m_r and residue field C.
It is noetherian because R_off is of finite type over C. The Zariski
tangent is Hom_C(m_r/m_r^2,C), so its vanishing implies
m_r/m_r^2=0. The ideal m_r is a finite A_r-module. Nakayama's lemma
applied to m_r=m_r m_r gives m_r=0. Thus A_r=C, including the entire
local ring, not merely its reduction. In particular there is no hidden
nilpotent structure at an off-diagonal closed point.
Here the precise imported form is
[Stacks, Lemma 10.20.1 (00DV), part (2)](https://stacks.math.columbia.edu/tag/00DV):
the module is the finite ideal m_r and the multiplying ideal is the
maximal ideal of the local ring, hence lies in its Jacobson radical.

**Global finiteness and the diagonal.** Since f is unramified,
02GE makes Delta_B -> R an open immersion. It is also a closed
immersion: f is finite and therefore separated. Thus Delta_B is
both open and closed as a subscheme of R, and R_off is its closed
complement as well as its open complement. The projection R -> B
is finite, being the base change of f. Since B is projective over C,
R is proper over C, and its closed subscheme R_off is proper too.
This rules out an accumulation from R_off to the diagonal already at
the scheme-topological level, and hence also after analytification.

Every closed-point local ring of R_off is C, as proved above. A
finite-type C-scheme with this property is zero-dimensional: if an
irreducible component had positive dimension, choose a closed point
on its nonempty open complement of the other components. Such a
point exists because finite-type C-schemes are Jacobson. The generic
point of that positive-dimensional component would give a strict
specialization chain into the chosen closed point, contradicting its
zero-dimensional local ring. There are finitely many components by
noetherianity; a zero-dimensional finite-type component over C is a
single closed point. Therefore R_off has finitely many points, all
closed, and is locally quasi-finite over C. Properness and 02LS now
make it finite over C.

Its coordinate algebra is a finite-dimensional commutative C-algebra.
If its nilradical were nonzero, that finite module would have a
nonzero localization at some maximal ideal. Each such localization
is one of the local rings A_r=C, which has zero nilradical. Thus the
algebra is reduced. Equivalently it is a finite product of copies of
C, with the empty scheme allowed. This proves the exact finite-and-
reduced threshold, without claiming that this product has zero factors.

The argument uses no completeness of M, global distance preservation,
normality of Z or extension of a local isometry. It does not control
the cardinality, simultaneous collisions of three or more source points,
or emptiness: at any such multiple collision it only makes the finitely
many branch tangent lines pairwise disjoint. F existence, separation,
reconstruction, transverse transport and universal primitive Hodge
realization remain independent unresolved requirements. No script or
numerical evidence is used.

**Separate critical audit, 2026-10-17 (step 358).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-17-opposite-coincidence-critical-audit.md`.
This audit finds no substantive error or stronger conclusion. Its
outcome is EXPLORATION / RESEARCH / REPRODUCTION, with actual task type
proof_audit. It checks the specialization, not the upstream theorems
anew. The mathematical inputs remain audited L118 and audited L120;
no normal character, image normality or compactification is added.

At a common value m both points represent the same stable locally free
bundle on the same marked Y. L118's actual etale-slice family identifies
one coarse neighborhood with one smooth connection neighborhood; by
continuity both source neighborhoods map into it after shrinking.
HE uniqueness identifies the two central connections up to gauge and
constant metric scaling. Conjugation preserves the trace norm, scalar
metric scaling cancels on End, and the fixed fibre triple defines the
same I,J,K on all harmonic representatives. These are precisely L118's
overlap assertions, so the two tangent spaces are being compared in
one actual metric/triple, not in separately chosen isomorphic germs.

An equal tangent line P would give (1) for both parametrized maps:
L118's connection identity implies zero ambient acceleration for every
source geodesic. Local uniqueness applies while the geodesics remain
inside this common chart. The constant scale 2lambda does not change
the source connection. Shrinking the same open ball in P makes both
source exponential images open, disjoint and mapped onto exp_m(W).
No ambient completeness or extension of a local source isometry enters.
The finite birational map in L120 has the asserted isomorphism open:
on an affine integral image chart its finite source algebra embeds in
the common fraction field, so clearing finitely many denominators
indeed gives A'_s=A_s. Its source inverse image meets every nonempty
analytic open in B. Thus a point of U_x in that locus has a second
preimage in U_y, contradicting the isomorphism. This checks the
equal-line contradiction without assuming the image is normal.

For distinct quaternionic lines a nonzero intersection would contain
the four independent vectors a,Ia,Ja,Ka, exhausting both lines; hence
their intersection is zero. The complex differential is the natural
algebraic coarse differential by L118's same-extension comparison.
Its realification is the differential already used in the chart.
The dual-number universal property of the actual fibre product now
gives exactly (2), with zero kernel; no replacement by its reduced set
or by a tangent cone is involved. At every closed complex point the
cotangent space is therefore zero. Finite type makes the local ring
noetherian, so its maximal ideal is a finite module and 00DV applies.
The conclusion A_r=C concerns the entire local ring, including any
putative embedded or infinitesimal structure.

The global step needs both diagonal properties. Unramifiedness gives
openness by 02GE; finite f is separated and gives closedness. Thus the
open complement is also a closed subscheme of R. Base change makes
R -> B finite, and projectivity of B makes R, then R_off, proper over
C. This is a properness argument for the actual complement, despite
the stable ambient moduli space not being proper. It also persists
under analytification, so off-diagonal points cannot approach Delta_B.
The noetherian/Jacobson argument in the proof excludes a positive-
dimensional component using a closed point on that component outside
the others and its strict generic specialization. A zero-dimensional
noetherian scheme has only finitely many points, all closed here.
Consequently the map to Spec C is locally quasi-finite, and 02LS gives
finiteness. Finally the nilradical of its finite algebra vanishes at
every maximal localization; a nonzero finite module cannot do so.
This verifies reducedness globally, including the empty case.

The exact finite-and-reduced threshold survives. This does not control
the number of collisions, exclude a fibre with three or more points,
or determine the singular local ring of Z: the local rings computed
above belong to R_off. In particular pairwise disjoint tangent lines
have not been asserted jointly linearly independent. The stopped Hom
test in ATTEMPTS/046 and the automatic-injectivity, index, scalar-cup
and compactification stops remain. F existence, collision emptiness,
reconstruction and transverse transport are independent unresolved
requirements. This confirmation makes no new mathematical advance
or progress beyond the checked sources and is not a complete candidate.

## Mathlib

Full matching coverage for this conditional geodesic-branch and
off-diagonal algebraic-scheme specialization is **not checked**.
Unknown availability is not evidence of absence. The imported inputs
are the named local ODE and inverse function theorems and the precise
Stacks results above, with L118/L120 providing the actual geometric
hypotheses. This is an informal proof, not a Lean verification, and
the separate critical audit above preserves the exact application.

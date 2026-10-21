# L099 — Conditional equality-family image has generic degree one

## Hypotheses

Retain audited L098's hypothetical locally free rank-two bundle F on
S_1 x B, the identical marked projective complex K3 surfaces, common
hyperkähler metric and ordered structures I,J,K, real product class
Omega, integral c_1(F)=0, Omega-slope-polystability, and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Retain the very general rank-four Picard scope of the marked surface
in foundations/05-cubic-rm-family.md, carried through L025/L044/L071.
In particular rho(B)=4; arbitrary higher-Picard specializations are
not included. Write sigma_1 and sigma_B for the fixed holomorphic
two-forms from the identical metrics. The self-adjoint full tensor
has D[sigma_1]=2lambda[sigma_B], with 1<lambda<5/4.

Use L098's actual finite classifying map and reduced-image factor

\[
 f:B\longrightarrow M=M_H^{ss}(2,0,-12),\qquad
 f=j\circ g,\quad g:B\longrightarrow W,\quad j:W\hookrightarrow M.
\]

Thus g is finite surjective, W is reduced, and U=B minus Z is the
exact preimage of M^s. Here Z denotes the finite reduced exceptional
support, possibly empty; all its points map to
m_0=[L\oplus L^{-1}], and no point of U maps to m_0. The map f|_U
is unramified. Use audited L095's actual curvature/form identities
and L098's natural stable Kodaira--Spencer comparison. No F existence,
image normality, unramifiedness at Z, or extension of a coarse form
across m_0 is assumed.

## Conclusion

The generic degree of g, and hence of f onto its image, is one:

\[
                     [\mathbf C(B):\mathbf C(W)]=1.
\]

If nu:N -> W is the normalization, the actual factor h:B -> N is
an isomorphism. Consequently g is the normalization morphism, under
that identification. This does not prove that W is normal or that
f separates all points or is a closed immersion.

This is a conditional ADVANCE / REPRODUCTION of the pre-assessed
cover, family-form and finite-symplectic-automorphism tools. The
separate critical audit below preserves it. It supplies no bundle, integrated split
germ, inverse construction, transport or additional algebraic Hodge
class. The universal primitive Hodge gap remains unresolved.

## Proof

**Scope and imports.** The pre-invocation SPECIALIZE assessment is
drafts/literature/2026-10-13-equality-normalization-generic-degree.md.
Its primary results are imported below; the work is their application
to this actual family. L065 is a methodological comparison only.
Its global-etale Euler argument does not apply before controlling Z.
The separate compatible quadratic-line stop in ATTEMPTS/061 is unchanged.

**Normalization and the full puncture.** Since B is integral and g
is surjective, the reduced W is integral. It is a finite-type complex
surface: finiteness and dominance preserve dimension. Finite-type
schemes over C are Nagata, and their normalization is finite, by
the Stacks Project, [29.18.2, Tag 0359](https://stacks.math.columbia.edu/tag/0359)
and [29.55.11, Tag 035S](https://stacks.math.columbia.edu/tag/035S).
Thus nu:N -> W is finite birational with N integral and normal.
Normality of B and dominance of g give a unique h:B -> N with
nu h=g, by [29.55.5(4), Tag 035Q](https://stacks.math.columbia.edu/tag/035Q).
It is dominant because nu induces an equality of function fields.
Since nu is separated and nu h is finite,
[29.45.14, Tag 035D](https://stacks.math.columbia.edu/tag/035D)
makes h finite. Its closed image contains the generic point of N,
so h is surjective.

Let T be the reduced support of (j nu)^{-1}(m_0) and put V=N minus T.
The set T is finite because nu is finite and j is a closed immersion.
It is empty if m_0 is not in W. L098's equality for the entire
exceptional fibre gives

\[
                  h^{-1}(T)=Z,\qquad h^{-1}(V)=U.           \tag{1}
\]

These are equalities of supports and complementary open subschemes;
neither exceptional fibre is asserted reduced. Moreover j nu maps
V to M^s. To check this at every scheme point n in V, choose b over
n by surjectivity of h. Equation (1) puts b in U, whose image under
f lies in M^s. Hence (j nu)(n)=f(b) lies there as well.

Consider h_U:U -> V. The relative differential sequence for
U -> V -> M^s, [Stacks 29.33.9, Tag 01UX](https://stacks.math.columbia.edu/tag/01UX),
gives a surjection Omega_{U/M^s} -> Omega_{U/V}. The first sheaf
vanishes by L098, so the second vanishes. Since h_U is finite,
the differential criterion [Tag 02G5](https://stacks.math.columbia.edu/tag/02G5)
makes it unramified. V is integral normal and thus geometrically
unibranch ([28.16.2, Tag 0BQ3](https://stacks.math.columbia.edu/tag/0BQ3)).
U is a nonempty integral open surface and dominates V. Apply
[37.37.2, Tag 0GS9](https://stacks.math.columbia.edu/tag/0GS9),
with this connected dominating unramified source: h_U is etale.
It is therefore a finite surjective etale cover of constant degree
d=[C(B):C(N)]=[C(B):C(W)]. No assertion about etaleness over T
has been used.

**Source-side purity and the Galois refinement.** Every connected
finite-etale cover C_U -> U extends to a finite-etale cover C_B -> B.
Indeed apply [Stacks 58.31.2, Tag 0H2W](https://stacks.math.columbia.edu/tag/0H2W):
B is locally Noetherian and regular, U is dense, and the omitted
points form a finite codimension-two subset. Thus no codimension-one
point is omitted, so the unramified-in-codimension-one requirement
is vacuous. All omitted local rings are regular. This applies also
when Z is empty. This purity application has target B, not N.

The extension C_B is connected. Otherwise each of its nonempty
connected components has open and closed image in the connected B
(the map is finite etale), hence surjects onto B and meets U. This
would disconnect C_U. Import triviality of the algebraic fundamental
group of a complex K3 surface from Huybrechts, *Lectures on K3
surfaces*, 449-page author draft,
[Remark 1.2.3, printed p. 11](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
It makes the connected C_B -> B an isomorphism, so C_U -> U is an
isomorphism. Thus U has no nontrivial connected finite-etale cover.

By [Stacks Section 58.7, Tag 03SF](https://stacks.math.columbia.edu/tag/03SF),
the connected finite-etale cover h_U admits a connected finite-etale
Galois refinement C -> V with a covering morphism C -> U over V.
This latter morphism is finite etale, as a morphism of finite-etale
V-covers. By the preceding paragraph it is an isomorphism. Hence
h_U itself is Galois. Its deck group G=Aut_V(U) has order d,
by the same Galois-cover theorem. We did not assume a general finite
cover of N was Galois.

**Extend that actual deck action.** The finite normal source B is
the normalization of N in C(B). Here is the actual affine check of
the normalization criterion in Stacks 035Q. For an affine open
Spec A in N its preimage is Spec C, where C is a finite A-domain,
integrally closed in C(B), with fraction field C(B). Every element
of C is integral over A. Conversely any element of C(B) integral
over A is integral over C, because the same monic polynomial has
coefficients in C; normality of C puts that element in C. Thus C
is exactly the integral closure of A in C(B).

Each deck automorphism induces an automorphism of C(B) fixing C(N).
It preserves that integral closure for every such A, and so extends
to an automorphism of Spec C over Spec A. The extensions glue:
on overlaps they agree on the dense open U and are morphisms into
the separated B. They extend uniquely, preserve h, and their inverses
extend too. Group identities follow by restriction to dense U, so
G acts faithfully on all B over N. In particular every element has
finite order. This uses the actual finite normal extension, not a
Hartogs assertion for arbitrary maps, smoothness of N, or purity
at its potentially singular points. The affine check is included
to justify this specialization, not as a new cover-extension theorem.

**Compare the actual stable two-form.** Import the coarse Mukai form
and its natural family pairing from Huybrechts--Lehn, *The Geometry
of Moduli Spaces of Sheaves*, E31 (1997),
[10.3.3--10.3.5 and 10.4.1--10.4.3, pp. 224--225 and 227--228](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=235).
The same family formula is covered by Kuznetsov--Markushevich,
[*Symplectic structures on moduli spaces of sheaves via the Atiyah class*,
math/0703264v2, Theorem 2.2 and (13)--(14), pp. 8--10](https://arxiv.org/pdf/math/0703264v2#page=9).
On the stable moduli of sheaves on the fixed K3 S_1, the form is
the Kodaira--Spencer/Yoneda/trace pairing followed by the functional
on H^2(S_1,O) defined by sigma_1. These general results need neither
a primitive Mukai vector, v-generic H, nor a global universal sheaf.
The quasi-universal similitude is cancelled in the coarse form.
They apply to M^s and the actual flat family over U.

Choose the resulting form omega_M on M^s. For y in U and
v,w in T_y^{1,0}B, L098 identifies df_y(v),df_y(w) with the actual
Dolbeault classes represented by

\[
       \alpha_v=R(v,\cdot)^{0,1},\qquad
       \alpha_w=R(w,\cdot)^{0,1}
\]

on S_1. These are the representatives of the same dual-number
extensions as the coarse differential, not chosen abstract tangent
identifications. Their ordered cup product is represented by
alpha_v wedge alpha_w with composition in End(F_y). Define its
unnormalized scalar pairing by

\[
       Q_y(v,w)=\int_{S_1}\operatorname{Tr}
                   (\alpha_v\wedge\alpha_w)\wedge\sigma_1.
\]

The integral defines a nonzero functional on the fixed
one-dimensional H^{0,2}(S_1), by Serre duality (equivalently evaluate
on bar sigma_1). Consequently the cited coarse family formula gives
(f|_U)^*omega_M=b Q for one fixed b in C^*. This coefficient compares
two functionals on that fixed cohomology space, including any ordered
Yoneda convention; it cannot vary with y. Similitude cancellation
removes local-universal-family choices. A simultaneous sign change
in both KS representatives does not affect Q.

Now apply L095 (7)--(9) to this same curvature, extending (7)
complex-bilinearly and combining omega_J+i omega_K=sigma_1.
For v of type (1,0), R(v,t)=0 on fibre (1,0) vectors t because
the Chern curvature is of type (1,1); hence r_v=alpha_v. Those
identities give

\[
 \gamma_R(v,w)=\frac{1}{4\pi^2}Q_y(v,w),\qquad
 \gamma_R=-2\lambda\sigma_B.                               \tag{2}
\]

This retains L095's two ordered mixed products, Chern--Weil
factorial, fibre orientation and removal of the pure-curvature
term. Its second equality is an equality of actual holomorphic
forms on B, not merely of cohomology classes. It uses the full
negative tensor; the charge-seven coefficient is not imported.
Combining the formulas gives, for the fixed nonzero scalar
a=4pi^2 b,

\[
                  (f|_U)^*\omega_M
                   =a\gamma_R|_U=-2a\lambda\sigma_B|_U.     \tag{3}
\]

No exact conversion to the printed Serre-trace normalization or
positive metric scale is needed here.

For s in G, f|_U composed with s equals f|_U, because s is a deck
automorphism over V and f|_U factors through V -> M^s. Pull back
(3) by s. Since a lambda is nonzero, s^*sigma_B=sigma_B on U.
Both are global holomorphic two-forms on B after the extension of s;
their equality on the dense open U implies equality on B. Thus G
is a finite group of symplectic automorphisms of B. We have never
defined a coarse two-form at m_0 or extended one across T in N.

**The rank-four test and degree.** Import Huybrechts, same
449-page draft, [Chapter 15, Section 1.2, Corollaries 1.5 and 1.8
and the following table, printed pp. 309--310](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=310).
A nonidentity finite-order symplectic automorphism of a projective
complex K3 surface forces Picard rank at least nine. The table's
orders 2 through 8 have lower bounds 9,13,15,17,17,19,19. These
are imported constraints, not newly derived lattice bounds.
Here B is precisely the retained very general marked surface with
rho(B)=4. That rank is the source theorem of van Geemen--Schütt,
*On families of K3 surfaces with real multiplication*, Forum Math.
Sigma 13 (2025), e2,
[Theorem 1.2(7), Sections 5.3--5.4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=15),
recorded with its very-general qualification in foundations/05.

If d>1 then |G|=d supplies a nonidentity element, and the imported
bound would require 4>=9. Thus d=1. The finite birational h has
normal target N and is an isomorphism: in the affine integral-closure
description above the function fields now agree, and A is already
integrally closed, so C=A. Therefore B identifies with N and g
with nu. Smoothness of this normalization is a conclusion, never an
input to the cover argument. All exceptional points and any
identifications by nu are retained; no original-image separation
or bound on |Z| follows.

The generic-degree-one threshold is met conditionally using known
tools. Higher-Picard symplectic quotients remain outside this test,
and the old global-etale Euler shortcut was unnecessary. Existence
of F, reconstruction, transverse transport and the universal Hodge
target remain independent unresolved gaps.

**Separate critical audit, 2026-10-13 (step 260).** The pre-invocation
SPECIALIZE scope is
drafts/literature/2026-10-13-equality-normalization-degree-critical-audit.md.
The audit finds no substantive error, repair, stronger exclusion or
existence conclusion. Its outcome is EXPLORATION / REPRODUCTION:
independent verification of the actual applications, not another
mathematical advance or a claim of originality. The full matching
Mathlib coverage remains not checked. Direct inputs remain L095 and
L098; the latter retains L096/L097. The primary form and K3 theorems
are reused with the precise citations above, without reproving them.
The complete statements/proofs of Stacks 0GS9 and 0H2W and the
Galois-cover statement of 03SF were rechecked in this audit.

First, no source or target puncture was lost. The continuous image
of integral B is irreducible, and L098's reduced induced image makes
W integral. Its finite normalization N is integral, and its actual
factor h is finite surjective by the separated-factor theorem.
Since g=nu h, the full set-theoretic inverse image of m_0 agrees
with h^{-1}(T). L098 identifies that entire support with Z, including
all scheme points and allowing nilpotent exceptional fibres. Thus
h^{-1}(V)=U. Surjectivity of h ensures every point of V maps into
M^s; this is not merely a closed-point check. Finiteness preserves
the dimension two of the dominating source, so T and Z have
codimension two when nonempty. Their complements remain nonempty
integral schemes, also when the exceptional sets are empty.

The differential sequence has the required direction: it surjects
from Omega_{U/M^s}=0 onto Omega_{U/V}. The finite h_U is locally
of finite type, so the differential criterion makes it unramified.
Normality gives geometrically unibranch V. The connected integral
source U dominates V, checking every hypothesis of 0GS9; therefore
h_U is finite etale of its function-field degree. This reasoning
does not assert normality of W or unramifiedness at Z.

Next, 0H2W applies to a cover of U with target the smooth B. The
finite complement has no codimension-one generic points, making
its codimension-one ramification condition vacuous, and every
omitted local ring is regular. A finite-etale extension over B
cannot acquire a disjoint nonempty component invisible over U:
each component has nonempty open-and-closed image in connected B,
so surjects onto B and meets U. For connected C_U this proves
connectedness of its extension. The imported K3 algebraic
fundamental-group theorem then makes that extension degree one.
Consequently every connected finite-etale cover of U is trivial.

In the connected Galois refinement C -> V of h_U, the morphism
C -> U is itself finite etale and surjective. Indeed a morphism of
finite-etale V-covers is finite etale; after an etale trivialization
this is a map of finite sets of copies of the base. Its image in
connected U is nonempty and open and closed. Its connected source
therefore triggers precisely the preceding trivial-cover result.
Thus C -> U is an isomorphism, making h_U Galois with |G|=d.
Simple connectedness of U alone is not being used to declare an
arbitrary finite map Galois before checking etaleness and refinement.

For extension of the deck action, a nonempty affine Spec A in N
has actual preimage Spec C in B. Dominance embeds A in C, and
normality and integrality of B make C an integrally closed domain
with fraction field C(B). Finiteness makes C integral over A. An
element of C(B) integral over A satisfies the same monic polynomial
over C, hence belongs to C. This checks the full integral-closure
description used above. A deck field automorphism fixes C(N) and
preserves this algebra. On overlapping preimages the resulting
maps agree on their dense intersection with U and hence agree by
separatedness of B. Their inverses and group identities extend by
the same uniqueness. The resulting global action is faithful and
finite; it neither assumes N regular nor removes ramification over T.

For the form bridge, L098's natural dual-number comparison identifies
the actual stable differential with the class of R(v,.)^{0,1}.
The curvature is of type (1,1) on the product, so for a base (1,0)
vector v its vertical (1,0) component is zero. Thus the complexified
raw r_v is exactly alpha_v, without a projection factor. The same
curvature represents both KS classes in the ordered Yoneda pairing.
Changing its overall KS sign changes both factors together. Any
ordered-pairing sign or Newton normalization is fixed, not dependent
on the parameter.

The trace target H^2(S_1,O) is the same one-dimensional vector space
at every stable parameter. Both the Serre functional used to define
omega_M and integration against the fixed sigma_1 are nonzero on it.
They therefore differ by one fixed b in C^*. Quasi-universal
similitude cancellation makes this a comparison with the global
coarse form, without parameter-dependent choices of a universal
bundle. It follows that the actual pullback is b Q. L095 (7)--(9)
give Q=4pi^2 gamma_R and gamma_R=-2lambda sigma_B. These identities
retain the pure-curvature removal, two ordered mixed products and
first-factor orientation. L098's prior audit also verifies that
these all-fibre identities do not require a split parameter to exist;
the empty-Z case is included. Hence (3) really holds on all U with
a fixed nonzero scalar, without a coarse form at m_0.

Every extended deck transformation preserves f on U, so (3) forces
it to preserve sigma_B there. Equality of global holomorphic forms
then gives preservation on B. Only at this stage is the finite-order
symplectic Picard bound applicable. The retained source is projective
and has rho(B)=4, with the very-general qualification of
foundations/05. A nonidentity element would force rho(B)>=9;
therefore G is trivial and d=1. Finally, the finite birational map
h to normal N is an isomorphism by the checked integral-closure
description. This identifies the normalization, rather than the
possibly nonnormal original image. Higher-Picard specializations,
point separation, F existence and transport remain outside the result.

## Mathlib

Full matching coverage of this conditional degree-one result, its
coarse-family comparison and the finite-symplectic Picard constraint:
**not checked**. Unknown coverage is not absence. The primary results
above are the mathematical references. This is a local reproduction
and specialization, with no claim of originality or advance beyond
the checked sources.

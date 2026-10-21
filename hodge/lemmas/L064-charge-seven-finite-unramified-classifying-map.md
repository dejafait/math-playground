# L064 — Conditional charge-seven classifying map is finite and unramified

## Hypotheses

Retain precisely the conditional actual bundle F of L062 and L063
on B x Y, where B and Y are L044's identical marked smooth
projective complex K3 surface S. Thus F is locally free of rank
two, slope-polystable at the specified real product polarization,
with c_1(F)=0 and ch_2(F)=-6e_1-7e_2+tau_D. Its charge-seven
restrictions E_x to Y are stable. L062 gives injectivity of the
actual family Kodaira--Spencer map at every complex point of B.

Use L063's single very ample integral H and its algebraic flat
family classifying morphism

\[
 f=f_F:B\longrightarrow M=M_H^s(2,0,-5).
\]

M is the stable numerical-class part of the fixed-polynomial
Gieseker moduli scheme for P_H(n)=H^2n^2-3. It is an open
subscheme of a projective complex moduli scheme, with the
numerical-class condition open and closed within the stable
locus. Neither existence of F nor a universal sheaf on M is
asserted. All subsequent conclusions are conditional on this F.

## Conclusion

The algebraic morphism f is finite and unramified. Let

\[
 \mathcal I=\ker(\mathcal O_M\longrightarrow f_*\mathcal O_B),
 \qquad Z=V(\mathcal I)\subset M
\]

be its scheme-theoretic image. The factorization f=j composed
with g, where j:Z -> M is the closed immersion, gives a finite,
surjective and unramified morphism g:B -> Z. The scheme Z is
reduced, but no smoothness or normality of Z is concluded.

This is a conditional application of known deformation and
scheme-morphism theorems, classified as REPRODUCTION. It gives
neither global injectivity nor a closed immersion, flatness,
an inverse, reconstruction, a metric identity, existence of F
or transverse transport. It supplies no new algebraic Hodge
class or solution of the universal primitive Hodge gap.

## Proof

**The actual coarse-moduli differential.** Import Huybrechts and
Lehn, *The Geometry of Moduli Spaces of Sheaves*, Aspects of
Mathematics E31 (1997),
[Theorem 4.5.1 and Corollary 4.5.2, p. 101](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113).
For a stable sheaf the completed local ring of the stable coarse
moduli scheme prorepresents the deformation functor, and its
tangent space is canonically Ext^1 of the sheaf with itself.
The natural transformation in the theorem is the one induced
by classifying flat families. Its etale-slice proof establishes
this compatibility; the general theorem is imported, not
reproved. The scalar-automorphism scope is supplied by
[Lemma 4.3.2 and its following discussion, pp. 89--90, and
Corollary 4.3.5, p. 91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=101),
where the scalar centre is removed in the PGL stable quotient.
No fine moduli assumption is being added.

Fix a closed x in B and put m=f(x). Both are complex rational
points. An algebraic tangent vector v at x is a morphism
Spec(C[epsilon]/(epsilon^2)) -> B with central point x. Pulling
F back along this morphism gives a flat deformation of E_x with
the canonical central-fibre identification. Naturality of L063's
corepresenting transformation says that its classifying morphism
is the composite with f. Thus the canonical tangent
identification sends df_x(v) to this deformation's Ext^1 class.

This is exactly the Kodaira--Spencer class kappa_x(v) of L062,
not an arbitrary isomorphism of vector spaces. Indeed E_x is
locally free, so Ext^1(E_x,E_x)=H^1(Y,End(E_x)). GAGA coherent
cohomology comparison and the Dolbeault theorem identify this
space with the analytic Dolbeault space used in L062. These
natural comparisons send the first-order transition-function
cocycle of the pulled-back bundle to its Dolbeault deformation
class. Algebraization, analytification and base pullback all
retain these same transition functions and the identified central
fibre. The algebraic and analytic tangent spaces of the smooth
complex B agree under the same comparison. Hence L062's
pointwise injectivity applies to this df_x.

More explicitly, write A=C[epsilon]/(epsilon^2) and F_v for that
pullback. Flatness over A identifies multiplication by epsilon
with an exact sequence of O_Y-modules

\[
 0\longrightarrow E_x\xrightarrow{\epsilon}F_v
   \longrightarrow E_x\longrightarrow0.
\]

Here the middle term is viewed on Y by restriction of scalars,
and the central identification fixes both end terms. Its class
is the deformation tangent of
[Huybrechts--Lehn 2.A.6, p. 50](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=62).
Import exact analytification and natural coherent-cohomology
comparison from Serre, *Geometrie algebrique et geometrie
analytique*, Annales de l'Institut Fourier **6** (1956),
[sections 9, 11--13, Proposition 10 and Theorem 1, pp. 16--22](https://www.numdam.org/article/AIF_1956__6__1_0.pdf#page=19).
The required projective scheme is Y and the coherent coefficient
bundle is End(E_x). Local splittings of the displayed sequence
give its End(E_x)-valued Cech cocycle; exact analytification
retains the sequence and these splittings, and the natural
comparison retains their cohomology class. The standard Dolbeault
resolution sends it to the derivative of the relative holomorphic
structure, namely L062's class of partial_v A in its equation
(4a). This is a comparison of the same first-order extension,
not an abstract identification of tangent dimensions. A change
to the opposite KS convention changes both descriptions by an
overall sign and cannot change injectivity. These cited comparisons
are imported; only their application to this extension is needed.

The stable numerical-class part is open and closed in the
stable polynomial space, by L063. Its local rings, completed
local rings and tangent spaces at m therefore agree with those
of that space. We use the full Ext^1 tangent; no fixed-determinant
subfunctor or trace-zero tangent space is substituted. All E_x
are H-Gieseker-stable by L063, so the imported theorem applies.
Consequently df_x:T_xB -> T_mM is injective at every closed x.

**From complex tangent points to the entire morphism.** Both B
and M are finite type over C: B is projective, and M is open in
the Noetherian projective moduli scheme. An open subset of this
Noetherian scheme is quasi-compact. Every morphism between these
finite-type C-schemes is locally of finite type (on affines,
finite C-algebra generators are also generators over the target
algebra). At a closed x and its image m the residue fields are
both C. Apply
[Stacks Project, Tag 0B2G, Lemma 33.16.8](https://stacks.math.columbia.edu/tag/0B2G):
in this equal-residue-field setting injectivity of the relative
tangent map is equivalent to unramifiedness at x.

The unramified locus is open, by
[Tag 02G4, Definition 29.36.1](https://stacks.math.columbia.edu/tag/02G4).
Its complement in B is closed and has no closed points. Any
nonempty closed subset of the finite-type C-scheme B has a
closed point (the weak Nullstellensatz). The complement is
therefore empty. Thus f is unramified at every scheme point;
we did not extend the equal-residue-field hypothesis to nonclosed
points. Equivalently, since f is locally of finite type,
Omega_{B/M}=0 by
[Tag 02G5](https://stacks.math.columbia.edu/tag/02G5).

**Properness and finiteness.** B is proper over C and M is
separated over C, the latter inherited from the projective
ambient moduli scheme and its open subschemes. Apply
[Tag 01W6, Lemma 29.42.7](https://stacks.math.columbia.edu/tag/01W6)
to obtain that f is proper. The theorem uses the closed graph
and the proper-source base change; it does not require M to
be proper or projective. By
[Tag 02V5](https://stacks.math.columbia.edu/tag/02V5),
unramified morphisms are locally quasi-finite. Thus f is proper
and locally quasi-finite, and
[Tag 02LS, Lemma 37.44.1](https://stacks.math.columbia.edu/tag/02LS)
makes f finite. No global injectivity or fibre degree has been
assumed in applying these criteria.

**The actual image scheme and its factor map.** A finite
morphism is quasi-compact. Therefore the kernel ideal I above
is quasi-coherent and defines the scheme-theoretic image through
which f factors, by
[Stacks Project, Section 29.6, Tag 01R5, Lemmas 29.6.1 and
29.6.3](https://stacks.math.columbia.edu/tag/01R5).
Its support is the closure of f(B). Since f is proper its image
is closed; hence this support is exactly f(B), and g:B -> Z
is surjective on underlying spaces. The reducedness assertion
uses the reduced source B and
[Tag 056B](https://stacks.math.columbia.edu/tag/056B),
which identifies the scheme-theoretic image of a quasi-compact
morphism from a reduced scheme with the reduced induced
structure on the closure of its image. Reducedness is not used
to infer any stronger regularity property.

The closed immersion j is separated and j composed with g=f
is finite. Hence g is finite by
[Tag 035D, Lemma 29.45.14](https://stacks.math.columbia.edu/tag/035D).
In particular g is locally of finite type. For B -> Z -> M the
transitivity exact sequence for relative Kahler differentials
from [Stacks Tag 01UX, Lemma 29.33.9](https://stacks.math.columbia.edu/tag/01UX)
has the right-hand part

\[
 g^*\Omega_{Z/M}\longrightarrow\Omega_{B/M}
             \longrightarrow\Omega_{B/Z}\longrightarrow0.
\]

The middle term is zero by the already established
unramifiedness of f. It follows that Omega_{B/Z}=0. The
locally-finite-type differential criterion in Tag 02G5 now
proves that g is unramified. This checks the factor map's
scheme property separately, rather than identifying a set-theoretic
image with its target or assuming unramifiedness descends by
terminology.

The approved threshold is met. The specialization checks above
compose the assessed known theorems with the actual conditional
family; no new general deformation or finiteness theorem is
claimed. ATTEMPTS/041--045 and the parked flat-source blocker
are unchanged. Finite unramifiedness imposes a global constraint
on any prospective F's image but provides neither F nor the
independent inverse/reconstruction and transverse-transport steps.

**Independent critical audit, 2026-10-07.** The conditional statement
survives the approved audit. The extension comparison above checks
the natural algebraic/analytic bridge on the actual family, including
its identified central fibre. The open-and-closed numerical-class
condition leaves the full local deformation tangent unchanged.
The equal-residue-field criterion is applied only at closed complex
points; the empty-complement argument supplies the remaining points.
Properness uses the separated stable target and the proper source,
not properness of that target. Quasi-finiteness, the kernel ideal's
scheme structure and reducedness, and both finiteness and vanishing
of differentials for the factor map each meet their cited hypotheses.
The differential sequence needs no flatness or smoothness of Z.
No substantive error or stronger map property was found. The added
extension detail and precise bridge citations explain the existing
argument; this audit is EXPLORATION and REPRODUCTION, not a new
theorem, a repaired mathematical error or a solution candidate.
The direct mathematical inputs remain L062 and L063.

## Mathlib

The full stable coarse-sheaf-moduli tangent compatibility and
this combined conditional image statement: **not checked**.
No matching declaration or absence is asserted. The proof uses
the precise primary citations above and is not a Lean verification.

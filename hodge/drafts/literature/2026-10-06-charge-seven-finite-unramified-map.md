# Conditional charge-seven map — finite and unramified source coverage

TARGET: Assess whether L062 and L063 force the conditional classifying map to be unramified and finite onto its scheme-theoretic image.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched stable coarse-sheaf-moduli tangent Ext1, injective tangent unramified criteria, proper quasi-finite finiteness and scheme-theoretic image factorization; targeted local searches found no prior combined result, and ATTEMPTS/044--045 stop different mechanisms.
SOURCE_EVIDENCE: Huybrechts--Lehn (1997), 2.A.6, Lemma 4.3.2 and its following scalar discussion, Corollary 4.3.5, Theorem 4.5.1 with full proof and Corollary 4.5.2, pp. 50, 89--91, 101; Stacks Tags 0B2G, 02G4, 02G5, 02V5, 02UR, 01W6, 02LS, 02OG, 01R5, 056B and 035D, statements and relevant proofs inspected.
COMPARISON: Known coarse-moduli deformation compatibility and general scheme-morphism criteria cover the necessary implications; applying them to this actual conditional family and its image remains a separate mathematical step, with no originality claim.
GAP: Check the family differential against the natural deformation identification, extend the closed-point criterion to all points, and check properness, quasi-finiteness and image factorization for L063's actual map; no resulting map property is proved in this literature turn.
REASON: Essential coverage was missing for the stronger target; it is now available without a fine-moduli, v-genericity or projective-stable-open hypothesis.
SCOPE: Exactly L044/L060/L062/L063's conditional charge-seven family on the identical projective K3 factors, with L063's single H and stable numerical-class target; differential, unramifiedness and finiteness onto scheme-theoretic image only.

## Main gap, intermediate threshold and route test

The main gap remains algebraicity of arbitrary primitive rational
Hodge classes; conditional F existence, inverse/reconstruction and
transverse transport are independent gaps. The intermediate threshold
is a fully justified unramified coarse classifying map, finite onto
its scheme-theoretic image. Its plausible downstream use is a global
constraint on the image geometry of a prospective F.

Continue with a cited application if the exact actual-family and
scheme hypotheses below can be checked. Otherwise identify the failed
implication and retain only what is justified. Finite unramified maps
are not automatically globally injective, flat or closed immersions.
No global injectivity or embedding target is approved here.

## Primary deformation statement and scalar scope

Use Huybrechts and Lehn, *The Geometry of Moduli Spaces of Sheaves*,
Aspects of Mathematics E31 (1997 text, 281-page PDF),
[2.A.6, p. 50](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=62),
[Lemma 4.3.2 and scalar discussion, pp. 89--90](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=101),
[Corollary 4.3.5, p. 91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=103),
and [Theorem 4.5.1/Corollary 4.5.2, p. 101](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113).

For a stable sheaf, the completed local ring of the coarse moduli
scheme prorepresents its deformation functor; the Zariski tangent
space is canonically Ext^1. The theorem's proof starts with the natural
family-induced map to moduli and constructs its inverse through an
etale slice and the Quot universal family. This is the compatibility
needed for the classifying differential, rather than an arbitrary
vector-space isomorphism. Section 2.A.6 uses flat deformations with
identified central fibre and describes their Ext^1 tangent classes.

Lemma 4.3.2 identifies Quot stabilizers with sheaf automorphisms. The
following discussion removes the scalar centre by passing to PGL;
Corollary 4.3.5 gives its principal bundle on the stable locus. Thus
the tangent theorem explicitly concerns the coarse stable scheme even
with scalar automorphisms. A global universal sheaf is unnecessary.
The full local proof was read; its general result is imported, not
reproved. Complex characteristic zero and Gieseker stability are the
source scope to retain.

## Primary scheme criteria and essential proof cases

The following are current online Stacks Project statements, accessed
2026-10-06; tags, rather than changing chapter numbering, fix citations.

- [Tag 0B2G, Lemma 33.16.8](https://stacks.math.columbia.edu/tag/0B2G):
  for schemes locally of finite type over S, at x with
  kappa(x)=kappa(f(x)), injectivity of the relative tangent map is
  equivalent to unramifiedness at x. Its proof uses the cotangent
  exact sequence and the vanishing criterion for relative
  differentials. Retain the equal-residue-field hypothesis; the
  closed complex-point test meets this scope.
- [Tag 02G4, Definition 29.36.1](https://stacks.math.columbia.edu/tag/02G4)
  defines the pointwise property using affine neighbourhoods, hence
  the unramified locus is open. [Tag 02G5](https://stacks.math.columbia.edu/tag/02G5)
  characterizes an unramified morphism by local finite type and zero
  relative differentials. These cover the all-points passage and
  the distinction between a tangent calculation and a scheme property.
- [Tag 02V5](https://stacks.math.columbia.edu/tag/02V5) gives local
  quasi-finiteness of an unramified morphism. Its cited algebraic
  case [Tag 02UR](https://stacks.math.columbia.edu/tag/02UR) was also
  read: a finite-type unramified ring map is quasi-finite, using the
  field/residue characterization. No global injectivity enters.
- [Tag 01W6, Lemma 29.42.7](https://stacks.math.columbia.edu/tag/01W6):
  an S-morphism from a proper S-scheme to a separated S-scheme is
  proper. The proof factors through the closed graph followed by
  the base change of the proper source morphism. The target need
  not itself be proper.
- [Tag 02LS, Lemma 37.44.1](https://stacks.math.columbia.edu/tag/02LS):
  proper and locally quasi-finite is equivalent to finite, without
  an additional Noetherian hypothesis. The relevant proof isolates
  the finite fibre in an etale neighbourhood, removes the empty-fibre
  complementary part using closedness, then descends finiteness.
  [Tag 02OG](https://stacks.math.columbia.edu/tag/02OG), also read,
  is a sufficient alternative over a locally Noetherian target:
  proper with finite fibres is finite. Prefer 02LS to avoid an
  unnecessary extra fibre-count argument.
- [Section 29.6, Tag 01R5](https://stacks.math.columbia.edu/tag/01R5),
  Lemmas 29.6.1 and 29.6.3: scheme-theoretic image is the smallest
  closed subscheme through which the morphism factors; for a
  quasi-compact morphism its ideal is the kernel of
  O_M -> f_*O_B, and its support is the closure of the image.
  The proof checks quasi-coherence on finite affine covers.
  [Tag 056B](https://stacks.math.columbia.edu/tag/056B) additionally
  identifies the image of a reduced source with the reduced induced
  structure on that closure. Neither statement gives smoothness
  or normality of the image.
- [Tag 035D, Lemma 29.45.14](https://stacks.math.columbia.edu/tag/035D):
  if g composed with f is finite and g is separated, f is finite.
  Its proof uses the closed graph, finite base change and composition.
  This covers finiteness of a factorization through the closed
  scheme-theoretic image, with its actual scheme structure.

## Application obligations for the next mathematical step

Inputs are L044's projective S, L060's conditional actual F and stable
charge-seven restrictions, L062's audited pointwise Kodaira--Spencer
injectivity, and L063's audited single-H algebraic flat-family map.
No further reading of their unchanged source assessments is required.

The application must identify the pullback of F along a dual-number
point with the deformation in the natural map of Theorem 4.5.1.
It must retain the numerical-class locus as open and closed, so its
local moduli tangent agrees with that of the stable polynomial space.
No separate fixed-determinant tangent space is needed. If one is used,
the trace-zero condition must be explained, rather than silently
substituted for Ext^1.

It must verify finite-type/separated scope, the closed-point residue
fields, and the passage from an open unramified locus containing all
closed points to all of B. For properness it must use projectivity of
B and separatedness inherited from L063's projective ambient moduli
scheme; it must not claim that the stable open is projective. Then
check the scope of 02V5 and 02LS. Treat scheme-theoretic image as a
closed subscheme with its kernel ideal, not just as a set. If also
claiming unramifiedness of the map to that image, justify it separately
using the same tangent criterion or the relative-differential
criterion. These are instructions for the later application, not a
completed derivation in this review.

No reproof of the general deformation, quotient or morphism theorems
is justified. The necessary local specialization is their composition
with the particular conditional family; it adds no theorem beyond
the inspected sources. No essential source is blocked. A direct
shell PDF download failed DNS resolution; the primary PDF passages
were accessible and read through the web tool, so this does not
restrict the ready coverage.

## Searches, overlap and preserved stops

Queries included `Huybrechts Lehn Corollary 4.5.2 tangent stable sheaves
Ext1`, `site.stacks.math.columbia.edu unramified injective tangent closed
points proper quasi finite finite scheme theoretic image`, and finite
morphism factorization through an immersion. Search-result discussion
pages served only as locators; all load-bearing statements above were
read in the book or Stacks Project. Additional unrelated search hits
were not used as evidence.

Targeted searches of local charge-seven assessments, L062/L063 and
histories found no prior combined finite/unramified argument. The
ready family-form and placement assessments cover the antecedents;
their earlier limits remain intact. ATTEMPTS/044--045 explain stopped
index/lifting tests, and ATTEMPTS/041--043 and the parked flat-source
blocker are preserved. This source review supplies neither a new
exclusion nor a Hodge class, and failure to find a combined statement
is not evidence of novelty.

## Mathlib

Combined coarse-sheaf-moduli, tangent-compatibility and conditional
image statement: not checked. No matching declaration or absence is
asserted; Mathlib coverage is not a gate for this cited application.

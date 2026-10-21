# Charge-seven family — off-diagonal relative-Hom test assessed

TARGET: Test whether the relative Hom complex of L065's conditional fibres forces E_x nonisomorphic to E_x' for every pair x != x'.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched relative Ext/diagonal formulas for stable K3 sheaves, derived proper base change, Bondal--Orlov strong simplicity, stable-family relative Hom separation and symplectic immersions; narrowly rechecked L060/L063/L065 hypotheses, history/126--133 and ATTEMPTS/041--045. Primary statements below supply the framework but no matching global separation theorem; failed searches establish no novelty.
SOURCE_EVIDENCE: Read Huybrechts--Lehn (1997), Proposition 1.2.7 and Corollary 1.2.8, pp. 11--12, and Definition/Corollary 6.1.4--6.1.5, p. 142, https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=23 and #page=154; Stacks Lemmas 36.30.4 (0B91), 36.22.5 (08IB), 36.31.1 (0BDI), including relevant proof cases; Bondal--Orlov arXiv:alg-geom/9506012v1, Theorem 1.1, p. 5 and necessity proof, p. 10; Markman arXiv:math/0009109v4, Theorem 1, Remark 3(2), proof through (11) and Lemma 4, pp. 2--6, and Section 3 opening, p. 12; compared arXiv:math/0406016v3, Theorem 8 and its stated scope, pp. 6--8.
COMPARISON: Derived base change and stable-sheaf Hom detection apply to the conditional family but do not force off-diagonal vanishing. Bondal--Orlov assumes stronger orthogonality. Markman's formula uses the full moduli dimension and specified support/codimension/rank conditions rather than proving separation for an arbitrary parameter subfamily. L065 still identifies only the normalization.
GAP: Determine whether the actual relative-Hom differential, beyond its Euler/K-class and generic separation, excludes H^0 of its derived fibre at every off-diagonal pair; no vanishing or diagonal-support assertion is established here.
REASON: Essential source coverage for one bounded test is ready, but the exact global vanishing is not covered by the inspected results; test the actual family without assuming full faithfulness, image normality or a universal moduli sheaf.
LITERATURE_REASON: Essential uncovered target is global fibre separation through relative Hom, beyond the prior generic-degree/local-form assessment; this turn completes that missing coverage.
SCOPE: Only the unchanged conditional F on B x Y, single H and stable moduli map of L060 and L062--L065, carrying L044; assess derived fibres, their jumps and the distinction between differentials and numerical classes. Do not assume embedding, image normality, a universal moduli sheaf, transform equivalence or F existence.

## Target, relevance and exact threshold

The main gap remains universal primitive Hodge algebraicity. This
intermediate target is separation of all distinct complex parameter
points in the conditional charge-seven family. It could remove point
identifications before reconstruction. Even a positive answer leaves
F existence, inverse/reconstruction and transverse transport unresolved.
Generic degree one alone is below the required threshold.

Set T=B x B and p:T x Y -> T. Let F_i be the pullback of the actual
conditional algebraic F using the i-th parameter and Y. The object
proposed for the next mathematical test is

    K = R p_*(F_1^vee tensor F_2).

Neither cohomology concentration nor a diagonal-support formula is an
input. In particular the earlier single-projection IT property is not
an IT assertion for this object.

## Inspected primary inputs and applicability

1. [Stacks, Lemma 36.30.4(1), Tag 0B91](https://stacks.math.columbia.edu/tag/0B91)
   gives perfect derived direct image and arbitrary derived base change
   for a perfect complex under a flat proper morphism of finite
   presentation. The projection p with smooth projective Y has these
   properties, and F_1^vee tensor F_2 is locally free, hence perfect.
   These hypotheses do not require a fine moduli space. The proof
   reduces to 36.30.1 with the structure sheaf as the flat complex.
2. [Stacks, Lemma 36.22.5, Tag 08IB](https://stacks.math.columbia.edu/tag/08IB)
   identifies derived pullback of derived direct image in a
   Tor-independent base-change square for a quasi-compact,
   quasi-separated morphism and quasi-coherent complexes. Flatness
   of p supplies Tor independence for point inclusions. Its proof
   reduces on affine bases to the projection formula and higher-Tor
   vanishing. The fibre test is on the complex computing
   R Hom_Y(E_x,E_x'), not on an ordinary fibre of a cohomology sheaf
   whose base change has not been checked.
3. [Stacks, Lemma 36.31.1, Tag 0BDI](https://stacks.math.columbia.edu/tag/0BDI)
   gives base-change-compatible, upper semicontinuous derived-fibre
   cohomology dimensions for pseudo-coherent complexes. The proof
   uses local finite free representatives and matrix-rank strata.
   It supplies jumping-locus machinery, not diagonal-only jumps.

[Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*, first
edition, Vieweg, 1997, Proposition 1.2.7 and Corollary 1.2.8,
pp. 11--12](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=23)
state that a nonzero map between stable pure sheaves with the same
Hilbert polynomial is an isomorphism, and a stable sheaf over an
algebraically closed field has scalar endomorphisms. The proof compares
the reduced Hilbert polynomial of the image with both sheaves. L063
provides the same H, polynomial and stability for both fibres. Thus the
needed detection is in degree-zero derived-fibre cohomology; stability
itself does not exclude repeated isomorphism classes.
[Definition 6.1.4 and Corollary 6.1.5, p. 142](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=154)
give the Mukai vector and Euler pairing. Their convention writes chi
as the pairing; the commonly used K3 pairing has the opposite sign.
An alternating Euler value must not be interpreted as Hom vanishing.
No pairwise Ext dimensions or global relative character are calculated
in this literature turn. These citations require no reproof.

## Stronger results: why citation alone does not settle the target

[Bondal--Orlov, *Semiorthogonal decomposition for algebraic varieties*,
arXiv:alg-geom/9506012v1, Theorem 1.1, p. 5](https://arxiv.org/pdf/alg-geom/9506012v1#page=5)
uses smooth varieties in characteristic zero and a derived kernel.
Its full-faithfulness criterion requires all-degree orthogonality of
distinct point images, scalar degree-zero self-Hom and self-Ext
vanishing outside degrees zero through the parameter dimension. The
necessity proof uses skyscraper Ext groups (p. 10). Projective B,Y and
locally free F meet the geometric setup; orthogonality is unproved here
and includes the requested vanishing. Do not import full faithfulness
to obtain it.

[Markman, *Generators of the cohomology ring of moduli spaces of sheaves
on symplectic surfaces*, J. reine angew. Math. 544 (2002), 61--82,
arXiv:math/0009109v4, Theorem 1, pp. 2--3](https://arxiv.org/pdf/math/0009109v4#page=2)
gives c_m of minus the relative Ext K-class as the diagonal of the full
smooth stable moduli space of dimension m; completeness is unnecessary.
Its proof (pp. 4--6) has vanishing relative Ext^0 sheaf despite nonzero
Hom at diagonal fibres. Lemma 4 assumes both terminal cokernels are
line bundles supported on a smooth locus of codimension m, and
alternating rank m-2. These are not available assumptions for this
subfamily. The parameter dimension cannot replace the full moduli
dimension. Section 3 opens a semi-universal extension; its full
construction is not imported. The later
[arXiv:math/0406016v3, Theorem 8](https://arxiv.org/pdf/math/0406016v3#page=7)
has explicit v-generic scope, unlike the earlier noncomplete statement.

These are obstructions to unsupported theorem applications, not a
counterexample with the full conditional F data. No inspected theorem
asserts separation from a nonzero pulled-back form and degree-one
normalization alone. The exact L063 vector (2,0,-5) is retained; its
Euler and expected-moduli-dimension substitutions belong to the next
mathematical test, not to a new derivation in this turn.

## Search record, duplicates and source qualifications

Queries included “relative Ext complex stable sheaves K3 surface
 diagonal Markman top Chern class Ext1”, “Stacks project perfect complex
 cohomology base change vector bundle proper pushforward derived base
 change”, “Bondal Orlov full faithfulness criterion Fourier Mukai
 strongly simple sheaves Ext vanishing”, and the narrower phrases
 “K3 symplectic immersion stable sheaves injective”, “stable sheaves
 family relative Hom injectivity K3”, and “K3 unramified moduli sheaves
 normalization”. Exact-title searches located the primary papers above.
The searches found no theorem covering this exact family-separation
statement; no originality follows from that observation.

The local search confirms history/126--133 and L060/L063/L065 exclude
separation from their conclusions. ATTEMPTS/041--045 stop character,
cohomology, parity and lifting tests; none is a duplicate separation
result or a global ban. Their original evidence is preserved.
The supplied REVIEW_REQUIRED assessment was the state at turn start.
The working source record is drafts/2026-10-07-off-diagonal-hom-source-working.md.

PDF screenshots for some primary pages timed out, but the essential
statements and proof cases were accessible as primary PDF text.
This is not a persistent essential source blocker. Search hits on
singular K3 moduli, Ulrich bundles and derived Torelli were not inspected
as theorems for this target; the full semi-universal construction is also
an unread lead. None is imported. Full Mathlib coverage is not checked;
unknown coverage is not evidence of absence.

## Bounded continuation and stopping test

Use L065 with L062, L063 and L064, carrying L060 and L044. Import the
fibre-detection framework, then examine what the actual relative-Hom
complex determines beyond its numerical class. The exact threshold is
H^0 of its derived fibre equal to zero at every distinct pair, not generic
vanishing or all-degree orthogonality. Continue if a justified property
of the actual differential excludes those jumps. Stop this bounded
mechanism if only its Euler/K-class or an equivalent unproved support
condition is available, recording precisely what remains undetermined.
Do not assume full faithfulness, normality or expected codimension to
force an answer. Preserve reasoning that stops short of the threshold.

The same exact target is ready under EXPLORE for one mathematical
attempt. No new lemma, mathematical calculation, proof change or script
was made here. An unlisted target or new mechanism requires a separate
review; merely completing this coverage does not claim separation.

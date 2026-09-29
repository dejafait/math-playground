# Hyperholomorphic cubic RM representatives — literature assessment

TARGET: Assess whether a hyperholomorphic vector bundle on S x S can represent a non-scalar cubic RM action and deform along a direction in V_RM outside V_D, without assuming a Fourier--Mukai equivalence.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched product hyperholomorphic bundles, cubic RM, twistor persistence, nonisometric correspondences and current constructions; the queries, inspected statements and limits are recorded below.
SOURCE_EVIDENCE: Verbitsky, arXiv:alg-geom/9307008v1, Theorem 2.5, https://arxiv.org/pdf/alg-geom/9307008v1#page=9; Schlickewei (2009), Lemma 1.2.1.2 and Proposition 1.2.3.3, https://d-nb.info/1000464202/34#page=30; Markman (2024), Proposition 5.15, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F49D6D83ED3D426A39BA9F4195AB8831/S0010437X24007048a.pdf/rational-hodge-isometries-of-hyper-kahler-varieties-of-dollark3ndollar-type-are-algebraic.pdf#page=23; further versions and locations below.
COMPARISON: Known criteria apply to existing bundles on hyperkahler products without requiring an equivalence, but the inspected existence and propagation results do not supply the specified non-scalar cubic representative or its transverse lift.
GAP: Find a compatible cubic Chern-class candidate, then an actual stable bundle and transport that reaches the missing NS-fixed direction; none is established by this review.
REASON: Import the valid general criteria and isolate the uncomputed cubic compatibility test. The framework is usable, so lack of a ready bundle is not a global stop; neither stability nor class persistence may be assumed from algebraicity on the original family.

## Hypotheses

Retain the very general projective K3 surface S in the
[cubic family input](../../foundations/05-cubic-rm-family.md), its
full RM field E=Q(zeta_7+zeta_7^(-1)), and L006's operator U.
The marked NS-fixed spaces satisfy V_D contained in V_RM, with
dimensions three and four. The desired bundle on X=S x S must
have a degree-four Chern-character action in E outside Q id,
allowing divisor-class and scalar corrections, and must extend
on the same deformation of S in both factors.

The rational Hodge target and its projectivity hypotheses are
unchanged; the adequate [target audit](../../foundations/01-target-and-scope.md)
is reused. Hyperholomorphicity is relative to a chosen hyperkahler
metric. For a bounded initial test, consider the product metric
from the same metric on both factors. This is a selected realization,
not an assertion that it exhausts every possible bundle or metric.

## Conclusion

The source comparison is complete for the saved TARGET. The
conditional deformation framework is known and should be cited.
No inspected theorem constructs the required cubic bundle, and no
nonexistence theorem for all such bundles was found. This bounded
search establishes neither existence nor originality.

The proposed intermediate target is compatibility of a corrected
RM class with a common twistor metric. A positive certificate could
provide Chern-class data for a subsequent bundle construction;
a negative certificate would reject that realization before a
stability search. This is materially different from recovering the
old support from a sheaf lift. It still leaves bundle existence,
stability, all necessary Chern-class conditions, and transport back
to the required NS-fixed RM deformations unresolved.

The actual required threshold remains a lift in V_RM outside V_D,
not merely a twistor deformation or a Hodge class. Prior representatives
reach three directions against four required. The 21-dimensional
span on the original family, the surfaces covered, and the universal
primitive-class gap are unchanged. No candidate proof or new
mathematical result is produced. This completed review is
LITERATURE / NOVELTY_UNCHECKED / EXPLORATION; it uses one exploration
turn after L024, without resetting the count.

## Proof

The evidence consists of primary statements and hypothesis comparisons.
No Chern-class, lattice, or deformation calculation is performed.

### A criterion for an existing bundle, valid on the product

Read Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
[arXiv:alg-geom/9307008v1, 29 July 1993, Definition 1.1 and Proposition 1.2, PDF pp. 2--4; Theorem 2.5, PDF p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9).
For a compact hyperkahler manifold with fixed induced complex
structure and metric, a stable holomorphic bundle with SU(2)-invariant
c_1 and c_2 is hyperholomorphic. Conversely, hyperholomorphic
connections have invariant Chern classes. The definition does not
require irreducibility, so it does not exclude S x S. It presupposes
a bundle and stability; it does not realize prescribed cohomology
classes. Proposition 1.2 identifies invariance with Hodge type for
all induced complex structures, a stronger condition than type
(p,p) on the starting fibre.

Also read [section 11, Proposition 11.1 and Theorem 11.1, PDF p. 40](https://arxiv.org/pdf/alg-geom/9307008v1#page=40).
Projective hyperholomorphicity concerns End(B), with an invariant
discriminant condition for a Yang--Mills bundle. It must not be
silently substituted for hyperholomorphicity of B itself. The
1993 numbering here is intentional; the published theorem was
not separately inspected.

Followed the later sheaf and twistor reference: Verbitsky,
*Hyperholomorphic sheaves and new examples of hyperkahler manifolds*,
[arXiv:alg-geom/9712012v2, 9 December 2012, Theorem 2.27, PDF pp. 23--24; Definition 3.11 and Theorem 3.19, PDF pp. 27 and 31](https://arxiv.org/pdf/alg-geom/9712012v2#page=23).
These restate the bundle criterion and extend it to reflexive
polystable hyperholomorphic sheaves with the specified invariant
Chern classes. [Lemma 7.2 and its following construction, PDF pp. 66--67](https://arxiv.org/pdf/alg-geom/9712012v2#page=66),
give a holomorphic bundle on the twistor space from an existing
invariant-curvature connection. This is actual transport along
that twistor family, without an equivalence-kernel hypothesis;
it does not select the notebook's prescribed ambient direction.
Only these portions are used, not the paper's later moduli or
new-manifold claims.

### The closest RM precedent

Read Ulrich Schlickewei, *Hodge classes on self-products of K3 surfaces*,
Bonn dissertation (2009), [Lemma 1.2.1.2, printed p. 23](https://d-nb.info/1000464202/34#page=25),
and [section 1.2.3, printed pp. 28--30](https://d-nb.info/1000464202/34#page=30),
including Proposition 1.2.3.3 and its proof. For a self-adjoint
endomorphism, the Hodge locus is the period-domain intersection
with its holomorphic-form eigenspace. The twistor comparison asks
that this eigenspace also contain the Kahler class. The existence
proposition treats quadratic RM and Picard rank at least three;
it is not a cubic theorem. The proposed use of a bundle is
conditional. This is a close precedent, not an original route
discovered here. Its unresolved cubic specialization motivates
the bounded test below.

### Propagation without an equivalence still has extra hypotheses

Read Markman, *Rational Hodge isometries of hyper-Kahler varieties
of K3^[n] type are algebraic*, Compositio Mathematica 160 (2024),
[Theorem 5.1 and setup, pp. 1276--1277](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F49D6D83ED3D426A39BA9F4195AB8831/S0010437X24007048a.pdf/rational-hodge-isometries-of-hyper-kahler-varieties-of-dollark3ndollar-type-are-algebraic.pdf#page=17),
and [Proposition 5.15 and proof, pp. 1282--1283](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F49D6D83ED3D426A39BA9F4195AB8831/S0010437X24007048a.pdf/rational-hodge-isometries-of-hyper-kahler-varieties-of-dollark3ndollar-type-are-algebraic.pdf#page=23).
Unlike Theorem 5.1, Proposition 5.15 does not require a Fourier--Mukai
equivalence. It requires a locally free sheaf, stability for an open
cone of paired Kahler classes, and persistence of c_2(End(F)) over
the entire specified moduli component M_psi of rational Hodge
isometries. Its conclusion allows twisted sheaves and transports
the endomorphism algebra. The notebook has not verified those
hypotheses: Hodge persistence only on its RM locus is insufficient
as an applicability check. This refines the earlier
[Theorem 5.1 comparison](2026-09-27-three-rotation-sheaf-extensions.md)
without turning the stronger proposition into an existence theorem.

### Newer constructions and nearby Hodge-theoretic results

Read Maulik--Shen--Yin, *On the Orlov conjecture for hyper-Kahler
varieties via hyperholomorphic bundles*,
[arXiv:2601.20289v1, 28 January 2026, Theorems 0.4, 0.7 and 0.9, pp. 3--5](https://arxiv.org/pdf/2601.20289v1#page=3).
The results give cup-product-preserving homological motive
isomorphisms under derived equivalence, the stated moduli-space
conditions, or a rational Hodge isometry. They do not prescribe
the nonisometric cubic action or supply this bundle.

Read Hartlieb--Shah, *Equivalences via twisted hyperholomorphic
sheaves from transverse Lagrangian fibrations*,
[arXiv:2608.13403v1, 13 August 2026, construction and Theorem 1.3, pp. 2--3](https://arxiv.org/pdf/2608.13403v1#page=2).
The construction starts with transverse Lagrangian fibrations and
uses twisted Poincare equivalences; the resulting bundle is their
composition kernel. It is not existence for arbitrary product
Chern data. No identification of its factors and action with the
required S x S and cubic U is provided here. This preprint is
compared as stated, not independently verified.

Read Huybrechts, *Brilliant families of K3 surfaces: Twistor spaces,
Brauer groups, and Noether--Lefschetz loci* (2023),
[definition and Theorems 0.2--0.4, pp. 397--400](https://numdam.org/item/10.5802/afst.1741.pdf#page=2).
The endomorphism-field theorem assumes CM; the fibre-connection
theorem does not transport the desired bundle. Its integral-class
family setup is not an existence result for the metric proposed
below. These statements give no replacement for the missing
cubic compatibility and bundle hypotheses.

The search also returned Verbitsky's *Projective bundles over
hyperkaehler manifolds and stability of Fourier--Mukai transform*.
The [arXiv:math/0107196v5 withdrawal notice, 17 September 2006](https://arxiv.org/abs/math/0107196v5)
reports errors in Proposition 11.4 and section 12 and restricts
the main assertion. No result is imported from that withdrawn text.

### Search record, redundancy, and source limits

Queries on 2026-09-27 included:

- `Verbitsky hyperholomorphic bundles stable first second Chern class SU(2) invariant theorem product K3`
- `hyperholomorphic vector bundle K3 product real multiplication Hodge correspondence`
- `K3 real multiplication Hodge conjecture hyperholomorphic 2025 2026`
- `Schlickewei "Hodge classes" "hyperholomorphic"`
- `"hyperholomorphic" "real multiplication" Chern`
- `"hyperholomorphic" "cubic" "K3"`
- `"real multiplication" "twistor" cubic`
- `"K3" "Kähler" "eigenvector" "real multiplication"`
- `"self-adjoint" "twistor" "multiplication"`
- `"hyperholomorphic" "real multiplication" bundle existence`
- `"K3" "cubic" "twistor lines"`
- `"real multiplication" "twistor lines" -site:citeseerx.ist.psu.edu -site:researchgate.net`

Title/author follow-ups led to the primary sources above. Search
snippets and third-party summaries are not used as theorem evidence.
The essential criterion, twistor construction, RM comparison and
stronger Markman proposition were read. No essential access gap
remains for this assessment. Uninspected references in these
papers, including a general classification of rational quadratic
forms admitting a prescribed field action, are not counted as
checked results. That arithmetic comparison belongs to the new
target's pending review.

Reused the earlier family and isometry audits. L004 excludes the
span of rational self-isometries, not arbitrary bundles. Reread
L012's hypotheses and conclusion: its actual bundles already have
the desired c_2 action but its construction assumes no stability
and retains the obstruction. A change of terminology cannot
reopen them. L017 and L024 treat specified supported-sheaf motions;
they do not test arbitrary product bundles. L019 already supplies
the rational divisor lattice, so recomputing that lattice is not
part of the proposed work.

### Bounded continuation and stopping test

Let lambda be the real eigenvalue defined by U(sigma)=lambda sigma.
For the selected common-metric realization, ask for a rational
cup-product-self-adjoint A on NS(S)_Q and a Kahler class omega in
NS(S)_R with A(omega)=lambda omega. The full endomorphism to test
is U plus A on T(S) plus NS(S)_Q. This is a problem specification,
not a claimed solution or a new equivalence theorem. It permits
an irrational Kahler class and does not demand a unital E-action
on all of H^2(S,Q).

A useful result would be an explicit certificate using the actual
lattice and Kahler chamber, or a rigorous obstruction for this
test. Positive square alone would not certify membership in that
chamber. Success would justify a separate bundle-existence target;
failure would stop this realization without excluding all bundles.
A twistor line must not be counted as the missing NS-fixed tangent
direction: reaching that locus with a bundle is still required.

The general theorems will be imported. Any future cubic lattice
specialization needs its own source comparison; a
[REVIEW_REQUIRED assessment](2026-09-27-cubic-rm-kahler-eigenvector.md)
records that exact target. No matrix, eigenvector, bundle, lift,
or new lemma was constructed in this turn.

## Mathlib

Coverage: **not checked** for the full bundle target, its cubic
compatibility test, or the supporting hyperholomorphic and twistor
theorems. No absence or matching Mathlib declaration is asserted.
The named results above are supporting mathematical references;
none matches the full saved bundle-and-transverse-lift statement.

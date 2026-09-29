# Extensions between rotation sheaves: literature assessment

TARGET: Determine whether any coherent sheaf extension 0 -> O_(C^(2))^{oplus 2} -> F -> O_C oplus O_(C^(3)) -> 0 has vanishing transverse RM Atiyah obstruction without requiring its filtration to lift.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact K3/RM/rotation-sheaf targets, unfiltered versus filtered deformation theory, semiregularity and stronger Fourier--Mukai lifting results; followed references and checked the Huybrechts--Thomas erratum. Queries, inspected statements, versions and scope limits are recorded below.
SOURCE_EVIDENCE: Huybrechts--Thomas, arXiv:0805.3527v2, Corollary 3.4, p. 14, https://arxiv.org/pdf/0805.3527v2#page=14, and their 2014 erratum, pp. 561--563, https://link.springer.com/content/pdf/10.1007/s00208-013-0999-x.pdf; Stacks Project tags 0CZU, 0CZV and 0BQP, https://stacks.math.columbia.edu/tag/0CZU; Belmans--Lowen--Okawa--Ricolfi, arXiv:2511.10312v1, Corollary B, pp. 3--4, https://arxiv.org/pdf/2511.10312v1#page=3; further comparisons below.
COMPARISON: Known theory supplies the unfiltered middle-sheaf obstruction and a separate obstruction to restoring its filtration. Semiregularity controls only an image, and the inspected stronger lifting theorems have additional hypotheses. No inspected statement determines the mixed Ext groups or transverse obstruction for these rotation extensions; L013 and L016 concern different representatives.
GAP: Determine the global extension classes and the full Atiyah obstruction of their middle sheaves, retaining the intersections, gluing and points at infinity; check the represented correspondence action before claiming relevance to the missing RM direction.
REASON: Import the general criteria and specialize their uncomputed geometric data. The exact existence question remains open in this review; an unfiltered sheaf lift is a materially different test from the stopped embedded union. The calculation is reserved for a separate research turn.

## Hypotheses

Retain the very-general cubic Dickson surface S, X=S x S, the reduced rotation images C, C^(2), C^(3), and their complete structure at infinity. Use the NS-fixed spaces V_D contained in V_RM already recorded in L008: their dimensions are three and four. Both factors deform by the same S_A over A=C[epsilon]/(epsilon^2).

Write K=O_(C^(2))^{oplus 2} and Q=O_C oplus O_(C^(3)). The saved target asks about the middle coherent O_X-module F_e of an extension of Q by K, including the split class. The superscript (2) labels a rotation image; K is two copies of its reduced structure sheaf. It is not an ideal square or the structure sheaf of a length-three thickening. A lift means an A-flat coherent sheaf on X_A with identified central fibre F_e. Its submodule, quotient, support and presentation need not lift. No stability, simplicity or Fourier--Mukai equivalence is assumed.

Reuse the unchanged rational target and its primary-source comparison in the [target audit](../../foundations/01-target-and-scope.md) and the [previous literature assessment](2026-09-27-ramified-three-rotation-lift.md). The universal goal remains rational cycle-class surjectivity for every smooth projective complex variety. This review does not select an integral or nonprojective variant.

## Conclusion

SPECIALIZE. The standard obstruction criterion covers this deformation problem, but its value for the proposed sheaves is not computed by the inspected sources. The exact TARGET is retained for a later research turn. This turn establishes no mixed Ext group, Chern-character action, obstruction kernel or transverse lift.

The intermediate target could help if a middle sheaf represents a non-scalar RM action and lifts in a direction outside V_D. The required first test is an actual global vanishing of its obstruction in such a direction. Earlier representatives permit only three directions against four required for the full RM tangent space. No dimension is established for the new sheaves. In particular, lifting their factors along V_D does not by itself prove that every extension class lifts there; that would require its own compatibility or Ext base-change check.

A successful first-order test would still leave higher orders, algebraization, algebraic representatives on actual transverse surfaces and recovery of the full cubic RM action unresolved. Arbitrary primitive fourfold classes and higher dimensions remain further gaps. The known 21-dimensional span on the Dickson family has not grown.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, using one exploration turn after L016's informative negative result. Supporting results are imported by citation; no result about this target is reproduced or established beyond the checked literature. Failure to find a matching theorem does not certify originality.

## Proof

The evidence is a comparison of source statements and hypotheses, with no new deformation calculation.

### The unfiltered obstruction criterion

Read Huybrechts--Thomas, *Deformation-obstruction theory for complexes via Atiyah and Kodaira--Spencer classes*, [arXiv:0805.3527v2, 15 September 2013, introductory hypotheses, Theorem 3.3 and Corollary 3.4, pp. 2 and 14](https://arxiv.org/pdf/0805.3527v2#page=14). For a perfect complex E on a separated noetherian scheme X and a square-zero thickening X' admitting an embedding in a smooth ambient scheme, the obstruction is

\[
o_E=(\mathrm{id}_E\otimes\kappa(X/X'))\circ\operatorname{At}(E)
\in\operatorname{Ext}^2_X(E,E\otimes I).
\]

It vanishes exactly when a perfect lift exists; lifts, when they exist, form an Ext^1 torsor. Simplicity and a lifted filtration are not hypotheses. Here F_e is perfect on smooth projective X; the NS-fixed ample class supplies projectivity of X_A and a smooth ambient embedding. The classical Atiyah class suffices on the smooth central fibre. The passage between perfect lifts and flat sheaf lifts over these dual numbers was already checked in L013 and is reused. The theorem supplies the criterion, not its value for F_e.

Also read the [2014 erratum, Math. Ann. 358, 561--563](https://link.springer.com/content/pdf/10.1007/s00208-013-0999-x.pdf). The original relative construction omitted flatness assumptions. The corrected sections 2--3 work over a field; the erratum explicitly confirms Corollary 3.4 in that setting and identifies v2 as incorporating the repair. We use the absolute construction over C for X contained in X_A. No flatness of a relative moduli space over an RM parameter space is assumed.

### Restoring the filtration is an additional problem

Read Stacks Project, [Remark 99.7.9, tag 0CZU](https://stacks.math.columbia.edu/tag/0CZU), and [Remark 99.7.10, tag 0CZV](https://stacks.math.columbia.edu/tag/0CZV), as available on 2026-09-27. With a flat lift of the middle sheaf already given, a quotient with kernel K and quotient Q has a separate lifting obstruction in Ext^1(K,Q tensor J), for the square-zero base ideal J. If this obstruction vanishes, quotient lifts form a Hom(K,Q tensor J) torsor. These are the source's named remarks, not assertions of automatic quotient lifting. They justify retaining the saved unfiltered question: existence of a middle-sheaf lift does not include a chosen quotient lift among its data. No vanishing or injectivity relevant to our K and Q is supplied here.

Followed a recent morphism-deformation lead and read Belmans--Lowen--Okawa--Ricolfi, *Deformation theory for a morphism in the derived category with fixed lift of the codomain*, [arXiv:2511.10312v1, 13 November 2025, Example 1.1 and Corollary B, pp. 2--4, Remarks 3.6--3.7, p. 11](https://arxiv.org/pdf/2511.10312v1#page=3). For a flat family of quasicompact semiseparated schemes and an exact triangle F_0 -> G_0 -> H_0, fixing a lift of G leaves an obstruction to lifting the morphism in Ext^1(F_0,b tensor^L H_0). Its vanishing is necessary and sufficient. The stated torsor description additionally assumes the corresponding Ext^(-1) vanishes. The result can compare an object's lift with a lift of additional maps; it does not make that extra obstruction zero. Its semiorthogonal-decomposition application needs vanishing conditions not established for these rotation sheaves. The published IMRN version was located; this comparison uses the identified preprint statement. It supplies no exact mixed Ext computation here.

### Mixed Ext groups and global compatibility

Read Stacks Project, [section 20.43, tag 0BQP](https://stacks.math.columbia.edu/tag/0BQP), as available on 2026-09-27. For bounded coherent complexes the local-to-global spectral sequence has terms H^p(X, sheaf Ext^q(K,L)) and abuts to global Ext^(p+q)(K,L). This is an applicable calculation framework, not a value for any term. In particular, local classes along intersection curves cannot be declared independent global extension parameters before computing the Hom sheaf, the possible differentials and contributions at infinity. L013's reduction to two constant parameters used its own local calculation and vanishing of its Hom sheaf. That reduction has not been checked for this target.

### Semiregularity does not settle the middle-sheaf obstruction

Reread Pridham, *Semiregularity as a consequence of Goodwillie's theorem*, [arXiv:1208.3111v4, 4 November 2024, Corollaries 2.22 and 2.25 and Remark 2.27, pp. 18--20](https://arxiv.org/pdf/1208.3111v4#page=18). For perfect complexes over square-zero extensions, these statements compare the semiregularity image of the obstruction with the Chern-character obstruction. In the smooth proper Artinian setting, that image detects whether the horizontal Chern character remains in the Hodge filtration. The resulting reduced obstruction theory can still have a nonzero kernel. No injectivity for F_e is established. Consequently, neither Chern-character additivity nor Hodge persistence alone answers the saved Ext^2 vanishing question. The comparison concerns all the requisite Chern-character components, rather than silently replacing them by ch_2 alone. These results are supporting inputs, not a theorem lifting every sheaf whose cycle class stays Hodge.

### Stronger geometric lifting theorems and the family source

Read Markman, *Rational Hodge isometries of hyper-Kahler varieties of K3^[n] type are algebraic*, Compositio Mathematica 160 (2024), 1261--1303, [Theorem 1.1 and its hypotheses, pp. 1262--1263, and the setup and Theorem 5.1, pp. 1276--1277](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F49D6D83ED3D426A39BA9F4195AB8831/S0010437X24007048a.pdf/rational-hodge-isometries-of-hyper-kahler-varieties-of-dollark3ndollar-type-are-algebraic.pdf#page=17). The first result realizes rational Hodge isometries by correspondences. The sheaf-deformation theorem starts with a locally free Fourier--Mukai equivalence kernel and a slope-stability condition for an open cone of paired Kahler classes. The proposed F_e is supported on surfaces in X and is not such a locally free kernel. An equivalence and that stability condition are also not hypotheses of the target. Its theorem therefore does not supply the requested deformation. L004's already recorded isometry-span restriction remains relevant to the first result; no obstruction to arbitrary correspondences is inferred.

Followed Markman's reference and read Toda, *Deformations and Fourier-Mukai transforms*, [arXiv:math/0502571v3, 6 April 2007, Theorem 1.1 and preceding setup, pp. 1--2](https://arxiv.org/pdf/math/0502571v3#page=2). An existing derived equivalence extends to the first-order category deformations matched by its induced Hochschild map. These can include twisted and noncommutative directions. The theorem requires an equivalence; it is not a lifting result for an arbitrary correspondence sheaf on the same classical deformation in both factors. No such equivalence or matching condition is available for the specified extensions. This is a scope comparison, not a change to the saved target.

Reuse the [cubic-family audit](../../foundations/05-cubic-rm-family.md) for van Geemen--Schutt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, Theorem 1.2(7) and sections 5.3--5.4. Reread [sections 4.8--4.9, pp. 13--14](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=13): the dihedral graph cycles realize the known RM action, while the remark distinguishes such special representatives from representatives on maximal RM families. These sections do not treat the extension space or an unfiltered sheaf obstruction. The published family construction is an imported input; no new cycle action is computed in this review.

### Redundancy and the precise remaining test

Read the whole overview and DAG before the detailed L013 proof, the latest ramified assessment and [history 019](../../history/019-2026-09-27-ramified-three-rotation-obstruction.md). The earlier second-syzygy result used presentation-map Ext vanishings. The diagonal-extension result used the distinguished identity graph, its two intersection curves and the nodal-fibre argument. Neither establishes the needed vanishings or a distinguished branch for this extension. The latest embedded tests used a structure sheaf and its algebra multiplication, including the ordinary square's generic length three. The present middle object has module data with two copies on the reduced second support. Its deformation is not prescribed to remain a quotient algebra. Applying a previous support-recovery proof would require proving the missing hypotheses for these modules.

The bounded specialization should retain three obligations within the saved target:

1. Determine the global mixed extension space from the full rotation geometry and classify the local middle modules sufficiently to include split and nonsplit cases. Retain the isolated points and all gluing conditions; do not assume cyclicity or that a Fitting support is flat.
2. Check the correspondence action represented by the leading Chern character, using the published rotation construction and known Chern-character additivity. This is a relevance check still to be performed. Then evaluate the full Atiyah--Kodaira--Spencer obstruction of the middle sheaf, allowing its filtration to be forgotten.
3. Compare any achieved kernel with the transverse threshold. Continue on an explicit global extension with a verified transverse vanishing, or a specific surviving cancellation with a bounded unresolved compatibility check. Stop this representative class if every extension retains a nonzero transverse obstruction, or if its action cannot supply the missing non-scalar class. Failure of a chosen split extension or of a filtration-preserving lift alone does not decide the target.

A claim of a full four-dimensional kernel additionally needs lifting in V_D for the same sheaf. No such assertion is imported automatically from the family. Complete the continuation/stop assessment within the shared exploration budget; renaming these extensions would not restart that budget. The initial pending record from step 019 and its proposed unfiltered target are preserved in this completed assessment. Source notes were saved during the review; both follow-up sources identified there have now been read.

### Search and access record

Queries on 2026-09-27 included:

- `"K3" "real multiplication" "sheaf" deformation extension`
- `"K3" "Dickson" "sheaf" extension`
- `"K3" "real multiplication" "sheaves"`
- `"K3" "real multiplication" "Atiyah"`
- `"rotation" "correspondences" "sheaves" "K3"`
- `"three rotation" "K3" sheaf`
- `"cubic" "real multiplication" "Hodge conjecture"`
- `deformation obstruction extension coherent sheaves forget filtration Atiyah Kodaira Spencer`
- `"deformations" "extensions of sheaves" obstruction`
- `"filtered sheaves" "obstruction" deformation filtration`
- `"extensions" "sheaves" "forgetful" "deformation" Ext`
- `site:stacks.math.columbia.edu "quotients" "Ext" "Deformation"`
- `site:stacks.math.columbia.edu "Ext sheaves" "spectral sequence"`
- `"K3" "correspondences" "hyperholomorphic" sheaves`
- `Huybrechts Thomas deformation obstruction theory complexes corrigendum 3.4`
- `"Deformation theory for a morphism in the derived category with fixed lift of the codomain"`

Further author/title searches located the identified theorem texts, Toda's reference and the erratum. Exact-geometry queries produced no inspected match; general queries located the supporting criteria above. This is a bounded search, not an exhaustive novelty claim.

An attempted Huybrechts--Lehn author-hosted PDF was inaccessible; search excerpts about its filtered deformation appendix are not used as theorem evidence. The quotient and morphism comparisons were instead read directly in Stacks and Belmans--Lowen--Okawa--Ricolfi. [Yokogawa's parabolic-Higgs preprint, MPI/93-88](https://archive.mpim-bonn.mpg.de/id/eprint/908/1/preprint_1993_88.pdf), was opened only at its introduction and is not a theorem-level input. The fixed-product sheaf criterion in section 6.2, Theorem 6.6, of [*The Atiyah class on algebraic stacks*](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/atiyah-class-on-algebraic-stacks/92C44757D4DCF43E4B6F368DDC5179EC) was inspected as an adjacent comparison; the moving-ambient criterion selected here is the corrected Huybrechts--Thomas result. The original Illusie, Lowen and Lieblich references were not independently read in this turn. No assertion depends on an unread stronger theorem or an inaccessible source; the essential statements used for the assessment are accessible and identified above.

## Mathlib

Coverage: **not checked** for the full rotation-extension target or its supporting deformation and Ext tools. No matching Mathlib theorem or absence from Mathlib is asserted. The named primary statements and direct links above are mathematical references; their supporting scope is distinguished from a match for the full target.

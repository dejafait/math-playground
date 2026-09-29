# Three rotation supports with a nonuniform thickening: literature assessment

TARGET: Compute the embedded first-order lifting kernel for the nonreduced union defined by I_C intersect I_(C^(2))^2 intersect I_(C^(3)), where C^(3) is the image of (g_0,g_0 sigma^3), and test whether it admits the transverse RM direction.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched K3/RM nonreduced correspondences, Dickson thickenings, deformations of ordinary ideal squares and first infinitesimal neighbourhoods, ropes, and primitive multiple schemes; exact queries, inspected statements and reuse are recorded below.
SOURCE_EVIDENCE: Buchweitz--Flenner (2003), Lemmas 7.6--7.7, Theorem 7.8 and Remark 7.11(1), pp. 190--192, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56; Gallego--Gonzalez--Purnaprajna arXiv:1007.3297v1, Notation 1.1, Definition 1.3, Theorems 1.5 and 2.2, pp. 2--6, https://arxiv.org/pdf/1007.3297v1#page=6; additional primary citations and applicability limits below.
COMPARISON: General relative embedded obstruction theory includes nonreduced closed subspaces; the inspected rope and primitive-multiple-structure results require different support, conormal or ambient hypotheses and do not compute this union's kernel. L014's reduced-support recovery is not a theorem about the specified ordinary-square union.
GAP: Specialize the imported obstruction theory to the exact ideal, first checking its fundamental-cycle relevance, then retaining nilpotent compatibility at all intersections and infinity and testing a direction in V_RM outside V_D.
REASON: The third support changes the critical-pair test loci and the ordinary square changes the deformation problem. These give a distinct bounded test after L014, but neither a Hodge-class argument nor projective-space rope smoothability supplies the desired ambient lift. No target calculation is performed in this literature-only turn.

## Hypotheses

Keep the very-general cubic Dickson family, its finite cover and the same NS-fixed ambient deformation in both factors. Write X=S x S and Y for the central closed subscheme specified globally by the displayed intersection of coherent ideals in O_X. Both factors deform by the same S_A over A=C[epsilon]/(epsilon^2). The square is an ordinary ideal square, not a symbolic square, an unspecified ribbon or a composition of correspondences. Its local structure at infinity is part of the target. An arbitrary flat embedded lift is allowed; preservation of a reduced component or nilpotent filtration is not an additional hypothesis.

The exact universal target is still rational cycle-class surjectivity for every smooth projective complex variety. Reread [Deligne, *The Hodge Conjecture*, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2) on 2026-09-27; its rational formulation agrees with the existing [target audit](../../foundations/01-target-and-scope.md).

## Conclusion

The general deformation framework is covered and should be imported. Its evaluation on this nonreduced union is not supplied by the inspected theorems. SPECIALIZE therefore reserves the exact saved calculation for a later research turn, starting with the cycle-relevance check below. It does not assert that the proposed representative is useful, smoothable, semiregular, or unobstructed.

The local gap is a non-scalar cubic RM representative admitting the missing transverse direction. The potential downstream use is extension beyond the known three-dimensional Dickson family. The required kernel on V_RM has dimension four; the earlier tested representatives attained only three. Neither a larger abstract deformation space nor a smoothing in some projective space meets this threshold. The known 21-dimensional cycle span has not been extended. Higher-order lifting, algebraization, realization of the full RM action, arbitrary fourfolds, and higher dimensions remain unresolved even if the first-order test succeeds.

This review supplies new source comparisons, not a new mathematical result or a reproduction. No fundamental cycle, action of Y, local ideal deformation, or lifting kernel is calculated here. The search did not establish coverage of the full statement; that is not a novelty claim. The completed step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION.

## Proof

The evidence consists of source statements and scope comparisons, with no new informal proof of the saved target.

### General embedded obstruction theory: applicable supporting input

Reread Buchweitz--Flenner, *A Semiregularity Map for Modules and Applications to Deformations*, Compositio Mathematica 137 (2003), 135--210, [Lemmas 7.6--7.7, Theorem 7.8 and Remark 7.11(1), pp. 190--192](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56). For flat closed subspaces in a flat ambient family, the tangent description uses Hom(I_Z,O_Z tensor M), and the relative obstruction lies in T^2_{Z/X}(O_Z tensor M). Reducedness and smoothness of Z are not required. Thus the arbitrary-subspace criterion is available for the specified Y; no new general criterion needs proving. Theorem 7.8 requires injectivity of semiregularity and yields smoothness over a closed subspace of the ambient base. It does not identify that subspace with the desired RM base. Remark 7.11(1) substitutes H^1(N) for T^2 under an lci hypothesis, which has not been established globally for Y. These are supporting theorems, not a kernel computation.

### Ordinary squares, cycles and ropes: what the terminology does cover

Read the current Stacks Project [Lemma 31.22.5, within Tag 0638](https://stacks.math.columbia.edu/tag/0638), together with the regular-to-quasi-regular implication in Lemma 31.22.2. These identify the locally free conormal and symmetric associated graded algebra of a regular immersion. Read [Definition 42.10.2, Tag 02QX](https://stacks.math.columbia.edu/tag/02QX): coefficients of the associated cycle are generic lengths. These are the precise inputs for the preliminary cycle check. An exponent on an ideal cannot be used as a cycle coefficient without that check. Regular-immersion formulas can be applied only on a verified regular locus; they do not describe the full ideal at the isolated singular points.

Read Gallego--Gonzalez--Purnaprajna, *Deformation of finite morphisms and smoothing of ropes*, [arXiv:math/0502467v3 (14 August 2006), Definition 3.1 and Theorem 3.2, pp. 7--8](https://arxiv.org/pdf/math/0502467v3#page=7). A rope of multiplicity m has square-zero ideal locally free of rank m-1 on its reduction; a ribbon has rank one. For smooth support embedded in a smooth ambient variety, Theorem 3.2(2)--(3) describes rope maps by conormal homomorphisms and characterizes embeddings by surjectivity. This describes structures and maps with that support specified, not all deformations of an existing union. Theorem 3.4, p. 8, smooths certain ropes on smooth projective curves under cohomology vanishings and a cover with the required trace-zero module. Its curve hypothesis is not met by our surface union.

For Y, cycle relevance remains an explicit specialization obligation: apply the generic-length rule to the actual ordinary square and combine the resulting cycle with the already normalized rotation actions. The saved observation that all three *reduced* supports have scalar total action is a warning to perform this check, not a calculation for Y. The review identifies adequate standard inputs for it; it does not assert a multiplicity or a non-scalar total action. If that check gives only scalar action, stop before the obstruction calculation. Likewise, a rope description on a smooth open subset would not justify replacing the specified global union by a ribbon or a uniformly thickened smooth support.

### Stronger smoothing results: missing hypotheses and different ambient problem

Read Gallego--Gonzalez--Purnaprajna, *An infinitesimal condition to deform a finite morphism to an embedding*, [arXiv:1007.3297v1 (19 July 2010), Notation 1.1 and Definition 1.3, pp. 2--3; Theorem 1.5, p. 4; Theorem 2.2, p. 6](https://arxiv.org/pdf/1007.3297v1#page=4). The setup is a finite morphism between smooth irreducible projective varieties followed by an embedding into projective space. Theorem 1.5 requires an unobstructed map with an algebraic formally semiuniversal deformation and surjectivity of the associated conormal homomorphism. Theorem 2.2 smooths an embedded rope when its conormal is the cover's trace-zero module and its class lies in the relevant image. No such cover, unobstructed map, or class-lifting statement is supplied for Y. Its reduction is the singular union, not the smooth image required here. Moreover, a projective-space smoothing would not establish containment in the prescribed S_A x_A S_A. Remark 1.10, p. 5, says that the surjectivity condition is not necessary in general, so its failure alone would not stop our target.

Followed the higher-dimensional comparison and read Mukherjee--Raychaudhury, *Smoothing of multiple structures on embedded Enriques manifolds*, [arXiv:2002.05846v3 (12 August 2021), Theorem 4.1(ii), pp. 12--13, and Theorem 4.2(ii), p. 14](https://arxiv.org/pdf/2002.05846v3#page=12). These give embedded smoothings of ropes on smooth Enriques manifolds with the specific conormal supplied by a hyperkahler or Calabi--Yau universal cover. This removes the curve restriction in the earlier examples, but it does not remove the support, conormal, cover or ambient hypotheses. The specified rotation union is not identified with such an Enriques rope, and the conclusions concern projective space rather than the required deforming product. This is a stronger conditional comparison, not a match.

Read Drezet, *Primitive multiple schemes*, [arXiv:2004.04921v3 (28 June 2023), section 1, p. 2](https://arxiv.org/pdf/2004.04921v3#page=2). Its class of objects has smooth connected reduction, a local embedding in one extra dimension, and a line bundle controlling the successive layers. The saved union does not have that smooth reduction; its ordinary square must not be replaced by a primitive multiple structure merely because both are nonreduced. Only the defining scope was inspected for this exclusion. No extension or smoothing theorem later in that paper is counted as read or imported.

### Exact family, earlier failures and reused comparisons

Reread van Geemen--Schutt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, [sections 4.8--4.9, pp. 13--14](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=13). Section 4.8 constructs cycles from powers of the cover automorphism and obtains the RM action. Remark 4.9 distinguishes these special representatives from unknown cycles on maximal RM families. The inspected sections do not supply a thickened-union deformation theorem. The rank, field and moduli dimensions in sections 5.3--5.4 are reused from the [family audit](../../foundations/05-cubic-rm-family.md) and prior assessment, not newly rederived.

The [two-rotation assessment](2026-09-26-current-target.md) is reused for its primary-source comparisons of Tziolas, Felten--Filip--Ruddat and Doi--Yotsutani on reduced normal crossings, and Ran, Nishinou and Pridham on semiregularity. Their exact versions, theorem numbers and direct links remain there. Those normal-crossing formulas cannot be assigned to a nilpotent thickening without checking their hypotheses. Semiregularity controls the image of an obstruction; the previous review did not establish injectivity or recovery of a flat quotient from a perfect-complex lift. These limitations persist. The prior Varesco and Schlickewei comparisons of broader algebraicity results are also reused within their recorded scope.

The earlier [attempt records](../../ATTEMPTS/011-two-rotation-union.md) and L007--L014 were checked for redundancy through the overview, relevant support description, and failure notes. L009's diagonal, L010--L011's fibre additions, and L012--L013's sheaves are different specified representatives. L014 uses reducedness and smooth critical-pair loci to recover a component. Adding the third support and a nilpotent structure changes precisely those hypotheses. This justifies a distinct test, not a presumption that the obstruction disappears. The historical stops remain in place; no stopped representative is reopened.

### Search record and source-access boundary

Queries on 2026-09-27 included:

- `"K3" "real multiplication" "nonreduced" correspondence`
- `"Dickson" "K3" "thickening"`
- `embedded deformations square ideal multiple structures ropes smoothability conormal`
- `"deformations" "square of the ideal" subscheme`
- `site.stacks.math.columbia.edu "quasi-regular" "symmetric" "conormal"`
- `site.stacks.math.columbia.edu "associated cycle" "length"`
- `"On families of K3 surfaces with real multiplication" correspondence maximal`
- `"primitive multiple schemes" deformation "Drezet"`
- `"K3" "real multiplication" "thickening" correspondence deformation`
- `"K3" "real multiplication" "nonreduced" "union"`
- `"nonreduced" "union" "semiregularity"`
- `"primitive multiple schemes" Drezet arxiv`
- `"deformations" "first infinitesimal neighbourhood" "subvariety"`
- `"Hilbert scheme" "powers of ideals" deformation`
- `"nonreduced" "union" "embedded deformations" obstruction`

The exact-geometry searches returned no inspected theorem matching the saved kernel. Broader searches led to the rope and multiple-scheme sources compared above. Results on punctual Hilbert schemes, symmetric ideals and powers of diagonal ideals were leads only; their theorem texts were not inspected or used. The displayed preprint versions are the versions assessed, not an assertion about every subsequent publication. Original references behind the rope classification were not independently checked; the classification statement was read in Theorem 3.2 itself. Friedman's original normal-crossing paper remains unread as recorded in the prior assessment and is not an input here. There is no essential inaccessible source for the selected general obstruction criterion. This was a bounded search and supplies no certification of originality.

### Bounded specialization and stopping test

The single saved kernel test has the following obligations; they are not additional research steps completed in this review:

1. Check the fundamental-cycle multiplicities and non-scalar action using the cited definitions and the existing rotation normalization. Keep the ordinary ideal square at infinity; no symbolic-square substitution is authorized.
2. Describe the actual local deformation modules at the finite intersections and at infinity, including nilpotent directions. Do not require a lift to preserve the original components or filtration. An identity on the reduction, or on reduced graph sheets, needs an additional argument before it becomes an identity on the thickened lift.
3. Evaluate the global embedded obstruction on the same ambient direction in both factors. Any recovery of C or another reduced support must establish its flatness and gluing, including the isolated points. Conversely, the inclusion of the three family directions for this exact scheme also needs a flatness argument.

Continue if the cycle check is useful and an actual transverse lift, or a specific surviving cancellation mechanism with a bounded remaining compatibility check, is obtained. Stop this representative if it has only scalar action or its global obstruction still excludes the transverse RM direction. A kernel of dimension three repeats the earlier achieved threshold; dimension four would address only this first-order intermediate target. Failure of a sufficient rope-smoothing hypothesis is not itself negative evidence about the kernel. The exploration budget is not reset by this source review.

The initial record of 2026-09-26 was REVIEW_REQUIRED: it proposed these supports because the critical pairs used in L014 cease to be smooth single-branch loci, and proposed nonuniformity to seek a non-scalar contribution. It contained no multiplicity, intersection or obstruction calculation. That motivation is preserved; this assessment completes its source screening only. The decision and limitations are recorded in [history 016](../../history/016-2026-09-27-three-rotation-thickening-literature.md).

## Mathlib

Coverage: **not checked** for the full target or the supporting cotangent-cohomology, cycle-multiplicity and multiple-structure tools. No Mathlib theorem match or absence is asserted. The named primary results and direct links above are mathematical references; supporting coverage is distinguished from a match for the full statement.

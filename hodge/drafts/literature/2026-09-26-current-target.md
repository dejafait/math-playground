# Two-rotation union: literature assessment

TARGET: Compute the global double-curve smoothing map for the reduced union C with C^(2), where C^(2) is the image of (g_0,g_0 sigma^2), and test whether it can cancel the transverse RM obstruction.
CHECKED: 2026-09-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact K3/RM/rotation-correspondence smoothing searches and searches for singular embedded deformations, normal-crossing smoothing and semiregularity; queries and inspected primary statements are recorded below.
SOURCE_EVIDENCE: Buchweitz--Flenner (2003), Lemmas 4.13 and 7.6--7.7, Theorem 7.8, Remark 7.11(1), pp. 173 and 190--192, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=57; Tziolas arXiv:1007.3038v1, Theorem 3.5; Felten--Filip--Ruddat (2021), Theorem 1.1; Pridham arXiv:1208.3111v4, Corollaries 2.22 and 2.25, Remark 2.27; the family, scope comparisons and further direct links are detailed below.
COMPARISON: Known results supply the singular embedded obstruction framework and conditional double-crossing tools, but none of the inspected statements computes the global smoothing map or transverse lifting kernel of this two-rotation union.
GAP: Determine the union's actual intersection strata and embedded compatibility maps, including the points over infinity, then decide whether its obstruction vanishes on a direction in V_RM outside V_D.
REASON: Import the general theory and specialize only its uncomputed geometric data; neither abstract smoothability nor persistence of a Hodge class decides this embedded lifting problem. The review is complete, but the calculation is reserved for a separate research turn.

## Hypotheses

Retain the very-general cubic Dickson family, smooth projective S, cover W, maps g_0 and g_0 sigma, and marked NS-fixed spaces V_D contained in V_RM from L006--L009. The saved target defines C^(2) using g_0 sigma^2 and takes the reduced scheme-theoretic union Y=C union C^(2) in X=S x S. Both ambient factors must deform by the same S_A over A=C[epsilon]/(epsilon^2).

C^(2) denotes an image support. It must not be identified without justification with the composition cycle Z^(circ 2) of L006. This assessment does not compute its action, multiplicities, intersection curves or singularities. In particular, ordinary double-crossing hypotheses are conditions to check on the relevant open locus, not assumptions about all of Y.

The universal target remains rational cycle-class surjectivity for every smooth projective complex variety. [Deligne, *The Hodge Conjecture*, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2), was reread and agrees with the existing [target audit](../../foundations/01-target-and-scope.md). No integral or nonprojective variant is substituted.

## Conclusion

The selected general input is the embedded obstruction theory for arbitrary closed subspaces, rather than a smooth-support theorem. Its specialization to this particular Y remains uncomputed. Normal-crossing and semiregularity results below are supporting or conditional results; none is a match for the full saved target.

The reason to continue is concrete: coupling two rotation supports may allow deformations unavailable when the added branch is the forced diagonal. A transverse embedded lift could provide a useful representative of a non-scalar RM class, after checking its correspondence action. The required first-order threshold is a four-dimensional lifting kernel on V_RM; the earlier representatives reached only three. No kernel dimension for Y is established here. Higher-order lifting, algebraization, recovery of the full RM action, and coverage of arbitrary fourfolds and higher dimensions would still need arguments. The known 21-dimensional span has not been extended beyond the previously treated family.

This is a completed literature assessment, not a new mathematical result or reproduction. The general tools are known and should be imported by citation. Coverage of the exact calculation was not established by this bounded search; that is not a claim of originality. The initial review was recorded as LITERATURE / NOVELTY_UNCHECKED / EXPLORATION in [history 013](../../history/013-2026-09-26-two-rotation-literature-review.md). The source-field repair in [history 014](../../history/014-2026-09-26-source-evidence-repair.md) adds no mathematical evidence.

## Proof

The evidence here consists of primary-source statements and comparisons of their hypotheses; no new smoothing calculation is included.

### Selected embedded-deformation input

Read Buchweitz--Flenner, *A Semiregularity Map for Modules and Applications to Deformations*, Compositio Mathematica 137 (2003), 135--210, [Lemma 4.13, p. 173](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=39), and [Lemmas 7.6--7.7, Theorem 7.8 and Remark 7.11(1), pp. 190--192](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56). The previously cited [arXiv version](https://arxiv.org/pdf/math/9912245#page=50) was also checked against the published statements.

For a flat ambient family and a flat closed subspace, Lemmas 4.13 and 7.7 give a lifting obstruction in relative cotangent cohomology T^2_{Z/X}(O_Z tensor M); Lemma 7.6 identifies infinitesimal embedded variations with Hom(I_Z,O_Z tensor M). These statements do not require smooth Z. Thus their scope includes the proposed union in a smooth ambient deformation. Theorem 7.8 adds properness, smoothness of the ambient family and a central fibre bimeromorphic to a Kahler manifold: injectivity of semiregularity gives smoothness over a closed subspace of the base, not automatically the entire base. Remark 7.11(1) identifies T^2 with H^1(N) only in the lci case. Neither injectivity nor that global simplification has been checked for Y.

### Normal-crossing smoothing and its limits

Read Tziolas, *First order deformations of schemes with normal crossing singularities*, [arXiv:1007.3038v1 (18 July 2010), Theorem 1.1(1), p. 2, definitions in section 2, and Theorem 3.5, p. 7](https://arxiv.org/pdf/1007.3038v1#page=7). For a quasi-projective scheme with only ordinary double normal crossings, its singular locus D is smooth and its normalization has an etale double cover D-tilde of D. Theorem 3.5 describes the pullback of the intrinsic T^1 line as O(D-tilde) tensored with its pullback by the sheet-exchanging involution. This retains descent data when branches are not globally labeled. It is a tool for a verified double-crossing locus, not a calculation of this union or its embedding constraints.

Followed the stronger smoothing reference in Doi--Yotsutani and read Felten--Filip--Ruddat, *Smoothing toroidal crossing spaces*, Forum of Mathematics, Pi 9 (2021), e7, [introduction and Theorem 1.1, pp. 1--2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/256301222A979923853B599C43C12EFB/S2050508621000081a.pdf/smoothing_toroidal_crossing_spaces.pdf#page=1). For two smooth components meeting along a smooth divisor D, the introduction identifies intrinsic T^1 with the tensor product of their normal lines. It explains why triviality of this line is tied to a smooth total space, not necessary for every smoothing. Theorem 1.1 gives an abstract smoothing for a proper normal-crossing space with effective anticanonical class, globally generated T^1 and projective singular locus; the anticanonical divisor must satisfy their transverse-strata condition. These hypotheses are not established for Y. Even an abstract smoothing supplied by this theorem would leave lifting the embedding into the prescribed S_A x_A S_A unresolved. Thus failure of d-semistability alone would not be a valid stopping test.

Also read Doi--Yotsutani, *Differential geometric global smoothings of simple normal crossing complex surfaces with trivial canonical bundle*, [arXiv:2203.09304v2 (30 March 2023), Definitions 1.1--1.2, Theorem 1.3 and Remark 1.4, pp. 1--3](https://arxiv.org/pdf/2203.09304v2#page=2). Their theorem assumes SNC local models, d-semistability, anticanonical double divisors and compatible meromorphic volume-form residues. It constructs a differential-geometric smoothing with complex fibres; the total map need not be holomorphic. This is not the required flat embedded deformation in a specified fourfold. Neither this theorem nor the preceding one licenses discarding the points over infinity. No claim that Y meets their hypotheses is made.

### Semiregularity comparisons

Read Ran, *Semiregularity, obstructions and deformations of Hodge classes*, Ann. Scuola Norm. Sup. Pisa (4) 28 (1999), 809--821, [Theorem 0, pp. 809--810](https://www.numdam.org/article/ASNSP_1999_4_28_4_809_0.pdf#page=2). For a connected embedded complex submanifold, obstructions lie in the semiregularity kernel; its relative statement assumes a Kahler ambient space and persistence of the fundamental class's Hodge type. This is not a theorem for an arbitrary singular support, and kernel membership is not vanishing. The older smooth-support failure in L007 remains relevant.

Read Nishinou, *Deformation of pairs and semiregularity*, [arXiv:2009.01651v1 (3 September 2020), introductory hypotheses, Theorems 1--2 and Definition 5, pp. 1--3](https://arxiv.org/pdf/2009.01651v1#page=1). Although section 2 defines semiregularity more generally, the stated relative deformation theorems concern immersed divisor images in Kahler manifolds. Theorem 2 additionally uses surjectivity onto the infinitesimal normal sheaf. Here the proposed image is a surface in a fourfold. Those theorems cannot be imported as a codimension-two lifting result. The published 2024 version's PDF was not readable through the available web interface; only the identified preprint version is assessed.

Read the stronger derived result of Pridham, *Semiregularity as a consequence of Goodwillie's theorem*, [arXiv:1208.3111v4 (4 November 2024), Corollary 2.22, p. 18, Corollary 2.25 and Remark 2.27, pp. 19--20](https://arxiv.org/pdf/1208.3111v4#page=18). For perfect complexes over square-zero extensions, these results identify the semiregularity image of the obstruction with the corresponding Chern-character obstruction. In the smooth proper Artinian setting, the latter measures whether the horizontal Chern character remains in the Hodge filtration. This covers all obstructions, improving the older curvilinear formulation. It still supplies a reduced obstruction space, not automatic vanishing within it. Moreover, deforming a perfect complex is a different claim from deforming the specified quotient support. No injectivity or recovery of that quotient is supplied for Y; persistence of its degree-four cycle class cannot silently replace all the necessary hypotheses.

### Exact family and broader algebraicity checks

Reused the [existing family audit](../../foundations/05-cubic-rm-family.md) and reread van Geemen--Schutt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, [sections 4.8--4.9, pp. 13--14, and sections 5.3--5.4, pp. 14--15](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=13). Section 4.8 treats graphs of all powers of the cover automorphism and the symmetric correspondence realizing RM. Remark 4.9 explicitly distinguishes these special cycles from unknown representatives on maximal RM families. Section 5.4 proves the explicit cubic family's three-dimensional, very-general rank-four/full-field statement; section 5.3 compares it with four RM moduli. These inspected sections do not give a deformation theorem for C union C^(2). The existing construction is covered by citation; the proposed coupled smoothing calculation is not covered there.

Read Varesco, *Hodge similarities, algebraic classes, and Kuga-Satake varieties*, [arXiv:2304.02519v3 (2 November 2023), Theorems 0.1 and 0.3, pp. 2--3](https://arxiv.org/pdf/2304.02519v3#page=2). The first theorem concerns quadratic RM generated by sqrt(p), p=2 or 3, with a Hodge-isometry/symplectic-automorphism hypothesis. The second requires the Kuga--Satake Hodge conjecture for the manifolds involved and concerns Hodge similarities. Neither inspected statement covers arbitrary cubic RM endomorphisms or the saved smoothing map. A four-dimensional quadratic family in that paper is not the missing direction of this cubic family.

Read Schlickewei, *The Hodge conjecture for self-products of certain K3 surfaces*, [arXiv:0907.2503v1 (15 July 2009), Theorems 1--2, p. 2](https://arxiv.org/pdf/0907.2503v1#page=2). Theorem 1 describes a Kuga--Satake isogeny decomposition and endomorphism algebra. Theorem 2 proves algebraicity for self-products of double covers of the plane branched over six lines. It does not compute a union deformation, and no identification of the present cubic family with that geometric hypothesis is supplied. The general Kuga--Satake correspondence cannot be treated as algebraic merely from Theorem 1.

### Search record, reuse and unread leads

Queries used on 2026-09-26 included:

- `"K3" "real multiplication" "smoothing" correspondence`
- `"K3" "rotation" "correspondences" "smoothing"`
- `"Dickson" "correspondence" "deformation" "K3"`
- `"normal crossing" "semiregularity" embedded deformations double curve`
- `Buchweitz Flenner semiregularity map modules applications deformations Theorem 7.8 7.11 pdf`
- `Friedman 1983 global smoothings varieties normal crossings Proposition T1 d semistability pdf`
- `"Deformation of pairs and semiregularity" arxiv`
- `Felten Filip Ruddat smoothing toroidal crossing spaces theorem 1.1`
- `Tziolas smoothings normal crossing schemes T1 normal bundles proposition arxiv`
- `"K3" "real multiplication" "Hodge conjecture" "2026"`
- `"K3" "real multiplication" "Hodge conjecture" correspondence smoothing`

Follow-up searches used the titles and authors of the papers above. The exact-geometry queries did not locate a theorem computing the requested map. Broad results and search snippets were treated as leads; the comparisons above use the identified primary statements. This is a bounded assessment, not an exhaustive novelty search.

The follow-up source-field review on 2026-09-26 reused these comparisons because the target and hypotheses were unchanged. The gate required a URL in the single-line SOURCE_EVIDENCE field; links in the body did not satisfy that check. The focused query `Buchweitz Flenner "A Semiregularity Map" "7.7" "7.8"` located the publisher's PDF. The published statements of Lemma 4.13 (p. 173), Lemmas 7.6--7.7 and Theorem 7.8 (pp. 190--191), and Remark 7.11(1) (p. 192) were reread there. They confirm the existing comparison: the embedded obstruction theory allows singular subspaces, while the relative semiregularity theorem does not guarantee lifting over the whole ambient base. The direct publisher URL is now in SOURCE_EVIDENCE. No additional source gap, theorem for the specific union, or reason to change SPECIALIZE was identified; the other comparisons above are reused from the initial review.

Friedman's *Global smoothings of varieties with normal crossings* (Annals 118 (1983), 75--114) remains an **unread original**: its [publisher record](https://annals.math.princeton.edu/1983/118-1/p06) was accessible, but its theorem text was not inspected. No assertion here relies on that unread theorem. The necessary deformation framework and the compared normal-crossing statements were read directly in Buchweitz--Flenner, Tziolas and Felten--Filip--Ruddat, so there is no essential source-access dependency on Friedman. Uninspected references in these papers are not counted as assessed theorems.

The migration assessment had screened only the family citation and left the smoothing comparison incomplete. Its prior Huybrechts--Thomas reference remains historical support for the sheaf tests; it is not substituted for the selected embedded criterion. The earlier L008--L013 conclusions and their stopped approaches are preserved. In particular, L009 uses a distinguished diagonal and L010--L011 use specific added fibre components; L012--L013 concern specified sheaves. None already computes the new union's coupled map. This review does not reopen those stopped representatives.

### Bounded specialization and stopping test

The next calculation should use the imported criterion, with the following obligations forming one test of the saved target:

1. Determine the actual intersection scheme and its strata, including infinity, before assigning a normal-crossing smoothing line. Verify any normalization and multiplicity identifications needed for this representative.
2. On each locus satisfying the double-crossing hypotheses, identify the local smoothing sheaf with its correct gluing. Compare these intrinsic parameters with embedded ideal deformations; retain every additional local compatibility condition at the excluded points.
3. Evaluate the resulting global embedded obstruction for the same ambient Kodaira--Spencer class in both factors. A nonzero smoothing section alone is insufficient: its compatibility must cancel the obstruction for a class in V_RM outside V_D.

Continue if an actual transverse embedded lift, or a concretely identified nonzero cancellation channel with a remaining bounded check, survives. Stop this representative if the global compatibility conditions force the transverse obstruction to remain nonzero. A three-dimensional kernel merely repeats the achieved threshold; even a four-dimensional first-order kernel would not prove the Hodge conjecture. No explicit map, local-ring computation, kernel claim or new lemma was produced in this literature turn.

## Mathlib

Coverage: **not checked** for the full union statement or its supporting cotangent, normal-crossing and semiregularity tools. No Mathlib theorem name, full match, or absence from checked Mathlib sources is asserted. The named theorems and direct links above are mathematical references; their supporting scope is distinguished from a match for the saved target.

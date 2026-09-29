# Adding an ample complete-intersection surface — literature assessment

TARGET: Test whether adjoining B=H_m intersect H_n to C permits a transverse RM embedded first-order lift, for some m>n>0 with H_m in |mH|, H_n in |I_C(nH)|, and B smooth, where H is a fixed product polarization.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact K3/RM complete-intersection union, ample-curve semiregularity, basic double linkage and fixed-base Bertini statements; read the primary statements and source copies identified below, and reused the sufficient earlier singular-deformation assessment.
SOURCE_EVIDENCE: Buchweitz--Flenner (2003), Lemmas 4.13 and 7.6--7.7, Theorem 7.8 and Remark 7.11(1), pp. 173 and 190--192, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56; Stacks Lemmas 33.47.1 and 33.47.3, https://stacks.math.columbia.edu/tag/0FD5 and https://stacks.math.columbia.edu/tag/0FD6; Diaz--Harbater Theorem 2.1 and discussion preceding Proposition 2.7; liaison and semiregularity theorem numbers, versions, access details and direct links below.
COMPARISON: Known results supply the singular embedded obstruction criterion, Bertini tools and the basic-double-link construction in their stated settings. None of the inspected statements gives a transverse lift of this union in the prescribed K3 product; ample intersection, fixed-ambient liaison and abstract smoothing do not supply that conclusion.
GAP: Verify an admissible smooth B and the actual intersection scheme for m>n, then specialize the singular embedded obstruction and the global compatibility of deformations along the ample curve, retaining C's three non-lci points.
REASON: Import the general tools and investigate only their missing applicability and obstruction calculation for this representative. The source review is complete; no construction, degree bound, smoothing map or new obstruction value is derived in this literature-only turn.

## Hypotheses

Retain C and X=S x S from the very-general cubic Dickson family, and the NS-fixed tangent spaces V_D contained in V_RM from L007--L008. Fix the saved product ample divisor H, whose class stays fixed. Write Y=C union B for the scheme-theoretic union. Both factors of X must deform by the same S_A over A=C[epsilon]/(epsilon^2).

The intended D=C intersect H_m is a smooth ample curve in the smooth locus of C. The construction must arrange that B is smooth and that its intersection with C has the claimed scheme structure and crossing type. These are applicability obligations, not new results of this review. The target requires B smooth; it does not require the containing divisor H_n to be globally smooth. The three singular points of C must remain in the analysis even if B avoids them.

Reuse the unchanged rational target and Deligne citation in the [target audit](../../foundations/01-target-and-scope.md). The saved existential quantifier and m>n>0 are unchanged.

## Conclusion

SPECIALIZE is justified by available general inputs, with a specific missing calculation. No inspected theorem settles whether this Y lifts along any kappa in V_RM outside V_D. The standard construction has a close relative in basic double linkage, so its elementary ideal manipulation should not be presented as new mathematics. Its relative deformation problem still needs to be checked in X=S x S, including the singular support.

The plausible use remains the one registered after L017: an ample intersection curve changes the normal-pole problem responsible for the stopped fibre constructions. B has a divisor-product cycle class, so a successful cycle construction could retain the non-scalar RM contribution after subtracting that known class. This is motivation, not an obstruction-cancellation theorem.

The required test is an embedded lift for at least one admissible pair (m,n) and some kappa outside V_D. Earlier representatives have only three allowed RM tangent dimensions against four required. This review adds no fourth direction, surface, or Hodge class; the known 21-dimensional span remains limited to the treated family. Higher-order lifting, algebraization, extension to actual transverse surfaces, and the universal Hodge conjecture remain unresolved even after a hypothetical positive first-order test.

This completed step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The framework is known and intended for citation. Coverage of the exact specialization was not established by the bounded search; this does not certify originality or supply a mathematical advance. One exploration turn has been used since L017's informative negative result.

## Proof

The evidence consists of inspected theorem statements and comparisons of their hypotheses. No new mathematical proof is attempted here.

### 1. Bertini and the geometry of the added surface

Read Stacks Project [Lemma 33.47.1, tag 0FD5](https://stacks.math.columbia.edu/tag/0FD5) and [Lemma 33.47.3, tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6), online statements checked on 2026-09-27. For a proper scheme, ample line bundle and closed subscheme, sufficiently high powers of sections vanishing on that subscheme generate the line bundle and define an immersion off the subscheme. The proof also records eventual global generation of the twisted ideal. The second lemma gives smooth general sections on a smooth scheme when the sections generate and define an immersion. These supply the standard generation and Bertini inputs; neither asserts smoothness along a singular base scheme.

Read Diaz--Harbater, *Strong Bertini theorems*, Trans. Amer. Math. Soc. 324 (1991), 73--86, Theorem 2.1, pp. 74--75, and the discussion preceding Proposition 2.7, p. 78. The [original journal text was inspected in this reproduced copy](https://www.scribd.com/document/810551917/Diaz-Strong-Bertini); its [publisher PDF](https://www.ams.org/tran/1991-324-01/S0002-9947-1991-0986689-6/S0002-9947-1991-0986689-6.pdf) was inaccessible. In characteristic zero, a general divisor is smooth off the scheme-theoretic base locus and ambient singularities. For a smooth base component, any nonempty general singular locus has codimension in that component equal to its codimension in the ambient variety. The p. 78 discussion explicitly retains this assertion on the smooth part when the base is singular. This is the appropriate source to screen H_n while retaining the exceptional points of C. Its hypotheses require the actual scheme-theoretic base locus; they cannot be replaced by a set-theoretic containment statement. It does not compute a deformation obstruction.

Also read Ghosh--Krishna, *Bertini theorems revisited*, [arXiv:1912.09076v3, section 3.4, Notation 3.7, Lemma 3.8 and Theorem 3.9, p. 9](https://arxiv.org/pdf/1912.09076v3#page=9). Their smoothness statement uses the strict bound max_e(e+dim Z_e)<dim X_reg, where Z_e is the embedding-dimension stratum, together with the stated avoidance conditions. This offers a precise check when a smooth containing hypersurface is sought; it is not permission to ignore the singular base or to impose global smoothness of H_n on the saved target.

The remaining applicability work is concrete: control the base scheme of |I_C(nH)|, arrange the smoothness and intersection conditions on B and D, and check all simultaneous choices with m>n. These sources justify attempting that verification. No effective degree or successful pair is asserted here.

### 2. The standard union construction and liaison's scope

Read Migliore--Nagel, *Applications of Liaison*, [author-hosted version, Theorems 2.7--2.8, pp. 5--6](https://academicweb.nd.edu/~jmiglior/MN14-webpg.pdf#page=5), checked on 2026-09-27. Theorem 2.7 states that for a codimension-two subscheme Z of projective space, F in I_Z, and a regular sequence (F,A), the ideal A I_Z+(F) is saturated. When Z and the complete intersection V(F,A) have no common component, it defines their scheme-theoretic union. This is basic double linkage. Theorem 2.8 has a more general ambient subscheme but assumes it is arithmetically Cohen--Macaulay and generically Gorenstein. These are construction and liaison statements in a fixed ambient space. They do not identify the lifting locus under an assigned ambient deformation.

Followed the general-ambient direction and read Hartshorne, *On Rao's theorems and the Lazarsfeld--Rao property*, Ann. Fac. Sci. Toulouse (6) 12 (2003), 375--393, [Hypotheses 2.1, p. 377, Definition 3.1, p. 381, and Theorem 3.4, p. 382](https://www.numdam.org/item/AFST_2003_6_12_3_375_0.pdf#page=9). The theorem treats codimension-two equidimensional subschemes without embedded components in an integral projective S_3 scheme with very ample O(1) and H^1(O_X(t))=0 for every integer t. It relates biliaison to pseudo-isomorphism classes and supplies descending biliaisons. It does not assert smoothness of the relative Hilbert scheme over deformations of X or equality of ambient lifting kernels.

Thus the saved construction should be compared with these established ideal and divisor operations, with the appropriate sheaf version and hypotheses checked on X. The projective-space or arithmetically Cohen--Macaulay hypotheses are not automatically inherited by choosing a projective embedding. Conversely, the existing singular points alone are not grounds for dismissing all generalized liaison statements. No linkage identification or invariance of the ambient obstruction is proved here.

### 3. The embedded criterion and semiregularity

Reuse the sufficient source reading in the [two-rotation assessment](2026-09-26-current-target.md): Buchweitz--Flenner, *A Semiregularity Map for Modules and Applications to Deformations*, Compositio Math. 137 (2003), 135--210, [Lemma 4.13, p. 173](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=39), and [Lemmas 7.6--7.7, Theorem 7.8, Remark 7.11(1), pp. 190--192](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56). Their relative cotangent-cohomology obstruction and Hom(I_Y,O_Y) tangent description allow singular closed subspaces in a flat ambient family. This is the selected framework for the whole Y. The semiregularity smoothness theorem is conditional and can be over a closed subspace of the ambient base; it supplies no automatic transverse lift. The lci identification with H^1 of the normal sheaf in Remark 7.11(1) must retain its hypothesis. No new source reading was needed for these unchanged general statements.

Read Iacono--Manetti, *Semiregularity and obstructions of complete intersections*, [arXiv:1112.0425v4 (9 November 2012), Set-up, Main Theorem and Corollary, p. 2](https://arxiv.org/pdf/1112.0425v4#page=2). Their setup requires Z to be the zero locus of a section of a rank-p bundle on a neighbourhood in a smooth variety, with codimension p. Their theorem annihilates every embedded obstruction after the indicated semiregularity/truncation map; degeneration of Hodge--de Rham removes the truncation qualification. It gives neither injectivity for Y nor a theorem that adjoining a complete intersection makes a singular cycle semiregular. The union must not be identified with the complete intersection B alone.

Read Dan--Kaur, *Semi-regular varieties and variational Hodge conjecture*, C. R. Math. 354 (2016), 297--300, [Theorem 1.1, Definition 2.2 and Theorem 3.3, p. 298, and Remark 3.5, p. 300](https://www.numdam.org/item/CRMATH_2016__354_3_297_0.pdf#page=2). They make a smooth n-dimensional subvariety of P^(2n+1) semiregular inside a smooth containing hypersurface of sufficiently large degree. This changes the ambient variety. It does not make C union B semiregular in the given fourfold. Their recalled Bertini theorem is not a substitute for checking the base and degree restrictions here.

The stronger perfect-complex comparison of Pridham, [arXiv:1208.3111v4, Corollaries 2.22 and 2.25, Remark 2.27, pp. 18--20](https://arxiv.org/pdf/1208.3111v4#page=18), is reused from the same prior assessment. Persistence of Chern-character Hodge type controls the image of an obstruction; it does not erase its kernel or supply the specified embedded quotient. No positivity argument checked here establishes the needed injectivity.

### 4. Local smoothing versus the prescribed global lift

Reuse Tziolas, *First order deformations of schemes with normal crossing singularities*, [arXiv:1007.3038v1, Theorem 3.5, p. 7](https://arxiv.org/pdf/1007.3038v1#page=7), as assessed earlier. The normal-line formula describes intrinsic T^1 on a verified double-crossing locus, retaining the normalization's descent data. It is a supporting tool for D after the local model is established, not a calculation of the embedded compatibility map or of Y at the isolated points.

Also reuse the earlier comparison with Felten--Filip--Ruddat, *Smoothing toroidal crossing spaces*, [Theorem 1.1, pp. 1--2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/256301222A979923853B599C43C12EFB/S2050508621000081a.pdf/smoothing_toroidal_crossing_spaces.pdf#page=1). Their abstract smoothing theorem has normal-crossing, anticanonical and global-generation hypotheses. No verification for this Y is supplied, and an abstract smoothing would still leave its embedding in the prescribed X_A unresolved. Existence of local smoothing sections is therefore an intermediate datum, not the threshold sought.

### 5. Redundancy, downstream use and the discriminating test

L009--L011 and their recorded failures use the diagonal or particular vertical fibre components; L014--L017 use rotation supports or specified sheaves, including their trace restrictions. None treats an added complete intersection with the proposed ample intersection curve. L007's non-lci warning remains applicable to the existing support. The family construction and the three-versus-four RM dimension comparison are reused from L006--L008 and the previous source assessment; they are not rederived. The preceding sources supply no reason to reopen the stopped representatives.

One bounded specialization of the unchanged target is justified:

1. Verify the actual base scheme, an admissible B and D, and the union's local ideal, preserving m>n and the three old singular points. Import Bertini and compare with basic double linkage instead of reproving those general results.
2. Apply the singular embedded obstruction criterion. Determine which double-curve smoothing or normal-pole data extend globally in the assigned X_A. Keep changes of the containing divisor and possible failure to preserve the components among the allowed deformations.
3. Continue if the calculation gives a flat embedded lift for some kappa in V_RM outside V_D, or a precise nonzero map whose remaining compatibility is a bounded test. Abandon this mechanism if a global obstruction or component-recovery argument excludes that direction throughout the tested range. Count an unresolved calculation as exploration, and finish the continuation or stop decision within the shared three-turn budget.

The quantifier matters: a positive result needs one admissible (m,n). A negative calculation only for sufficiently large degrees, general divisors, or a fixed pair would stop that regime, not disprove the full existential target. The review supplies no bound on the new lifting kernel. Finding B, many local sections, a fixed-ambient deformation, or a vanishing unrelated to the actual obstruction would leave the main transverse gap open.

### 6. Search and access record

Queries on 2026-09-27 included:

- `"semiregularity" "complete intersection" union`
- `"Bloch" "semi-regularity" algebraic cycles complete intersection`
- `deformations union subvariety ample complete intersection semiregular Hodge`
- `"deformations" "adding" "complete intersections" cycles`
- `"basic double link" "deformations" obstruction`
- `"basic double linkage" "Hilbert" smooth`
- `"basic double link" deformations Hilbert scheme Kleppe`
- `"basic double" "obstruction" deformation`
- `"semiregularity" "basic double"`
- `Bertini theorems hypersurface sections containing subscheme Altman Kleiman embedding dimension`
- `"Strong Bertini theorems" Diaz Harbater pdf`
- `"K3" "real multiplication" "complete intersection" correspondence deformation`
- `"K3" "real multiplication" "ample" "deformation" correspondence union`

Title/author follow-ups located the named theorem statements. The exact-geometry searches produced no inspected theorem settling the saved lift. This is a bounded comparison, not an exhaustive novelty claim. Search snippets and broad claimed Hodge resolutions were not used as theorem evidence.

The original Altman--Kleiman 1979 article remains unread: its publisher record was accessible, but the PDF was not. The recalled statement was read in Dan--Kaur and Ghosh--Krishna and is distinguished from reading the original. The selected Bertini inputs were inspected directly in Stacks and in Diaz--Harbater's reproduced journal text, so no essential step is left dependent on access to that original. The Diaz--Harbater theorem comparison uses the article text, not the hosting site's generated title or summary. No account, paid access, or API key was used.

For liaison, the author-hosted Migliore--Nagel theorem statements and Hartshorne's original article were read. The former has no version date on its first page; the URL, theorem numbers, PDF pages and check date identify the copy used. Lazarsfeld--Rao's original construction paper and uninspected references in these papers are not counted as separately read. Migliore's *Experiments in Commutative Algebra and Algebraic Geometry*, pp. 28--31, was an inspected terminology lead; the final comparison uses the more precise statements above. Existing Ran, Nishinou and family-scope comparisons remain available in the earlier assessment and were not mechanically repeated.

## Mathlib

Coverage: **not checked** for the full union-lifting statement, its singular embedded obstruction, Bertini specialization or liaison operations. The named results and direct links above are mathematical sources, not Mathlib matches. No library absence or full formal coverage is claimed.

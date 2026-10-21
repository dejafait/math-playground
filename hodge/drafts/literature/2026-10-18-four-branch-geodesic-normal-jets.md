# Coverage — actual geodesic normal second jets

TARGET: Determine whether L118's common totally geodesic connection forces L126's normal-jet map Nbar to vanish at every four-preimage span-two collision.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Kähler normal holomorphic coordinates/Christoffel vanishing, totally geodesic complex submanifold second jets, and the exact combination totally geodesic/Kähler normal coordinates; compared L118 (3)--(4), L126 (1)--(4) and coordinate invariance with ATTEMPTS/070--072 and the saved opposite-geodesy coverage.
SOURCE_EVIDENCE: Higashijima--Itou--Nitta, hep-th/0203081v3 (17 June 2002), Section 3.1 equations (3.1)--(3.3), (3.7), PDF pp. 7--9, and Appendix A; Jentsch--Weingart, Asian J. Math. 24 (2020), 369--416, Theorem 4.6 proof pp. 389--391, Definition 4.8 and Corollary 4.9 pp. 391--392, inspected at the publisher PDF.
COMPARISON: Primary sources cover holomorphic normal-coordinate tools and even a stronger published submanifold compatibility statement; L126's coordinate invariance is already proved locally. The exact actual-image Nbar specialization is not yet written or proved here.
GAP: Apply the inspected finite-order coordinate tools to the same ambient connection and the four actual branch maps, checking analytic-to-formal jets and the annihilator quotient; do not assume simultaneous linearization as a premise.
REASON: Essential coverage is ready for a separate mathematical specialization; no fresh mathematical result is derived in this literature-only step.
SCOPE: Exactly four preimages with quaternionic tangent span two in L118/L120/L121's opposite stable image, ambient quaternionic dimension 39; retain all F and common-metric hypotheses.
LITERATURE_REASON: The startup gate required review of actual-geodesy specialization, outside the earlier arbitrary-branch jet assessment; the new exact submanifold-coordinate lead warranted primary inspection.

## Main gap and bounded target

Universal primitive rational Hodge realization remains open, already on arbitrary fourfolds. The intermediate target is the exact TARGET above. Resolving the unknown normal-jet rank would make L126's local normalization-defect contribution usable in later global bookkeeping. F existence, collision occurrence, global consequences and transverse transport remain independent unresolved problems.

## Inspected sources and qualifications

[Higashijima--Itou--Nitta, *Normal Coordinates in Kähler Manifolds and the Background Field Method*, v3](https://arxiv.org/pdf/hep-th/0203081): Section 3.1 defines holomorphic Kähler normal coordinates by vanishing holomorphic metric derivatives, equivalently connection derivatives, at the centre. Equations (3.3) and (3.7) give direct and inverse coordinate expansions. The N=2 case supplies the required finite-order tool: vanishing Christoffel symbols at one point in holomorphic coordinates. Appendix A identifies the Kähler connection. Section 2.2 instead exhibits nonholomorphic curvature terms for real exponential coordinates. Only a quadratic coordinate change is needed for the proposed test; no convergence of an infinite expansion is required. These statements apply to smooth Kähler metric germs, without compactness or flatness. They do not state a normalization-length result.

[Jentsch--Weingart, *Riemannian and Kählerian normal coordinates*, Asian J. Math. 24 (2020), 369--416](https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2020/0024/0003/AJM-2020-0024-0003-a001.pdf), Corollary 4.9, pp. 391--392: anchored Kähler normal coordinates restrict to those of any totally geodesic complex submanifold. Its proof is left to the reader; inspected Theorem 4.6's supporting induction, pp. 389--391, including its quadratic base and holomorphic-flow modification. This is a stronger known lead, not a new simultaneous-linearization claim here. Caution: p. 372 asserts real analyticity for every Kähler metric, which is too broad for smooth metrics. Do not use that assertion or infer convergent full coordinates from formal normalization. The independent finite-order tool above suffices for the saved target; no full-order theorem is essential.

No search establishes originality. Search snippets, secondary pages and uninspected references are not imported. The publisher corollary changes the comparison: branch-coordinate compatibility has published precedent, so any successful finite-order application should be REPRODUCTION, not POTENTIALLY_NEW.

## Applicability obligations for the next mathematical step

L118 (3)--(4) provides holomorphic branch maps in one smooth hyperkähler ambient connection germ, with parametrized parallel differential for the original source connection. The local embedded branches, rather than the possibly singular whole image, are the proposed submanifolds. The constant pullback scale 2lambda must remain in the argument; no ambient completeness or global embedding is available or needed for this finite-order test.

L126 defines Q_i as the homogeneous quadratic coefficient, not the Hessian itself. Its coordinate-independence paragraph kills source reparametrizations by U^ann and ambient quadratic changes modulo E_2. The mathematical step must explicitly connect these formal coefficients to holomorphic analytic branch jets; source connection contributions and the factor between Hessian and Q_i must be retained until they are justified away. No computation of Nbar, its rank, or a refined length is made in this assessment.

Keep L120's finite normalization and L121's distinct tangent lines when applying the algebraic length formula. An analytic coordinate jet may be used in the completed complex local ring; a global algebraic coordinate chart is not a supplied premise. No reproof of the general geodesy or normal-coordinate theorem is justified; only the finite-order applicability argument and L126 quotient comparison remain.

## Duplicates, failures and continuation test

The scoped local search found no completed Nbar evaluation. L126's arbitrary complex branch examples omit actual geodesy and do not decide this specialization. ATTEMPTS/070 refutes minimal defect from selected pairwise data; ATTEMPTS/071--072 concern curvature compatibility and its first derivative. Their stop evidence remains intact; none is reopened by changing coordinate tools.

Essential inputs: L118, L120, L121 and audited L126. Retain locally free rank-two Omega-polystable F, integral c_1=0 and ch_2=-14e_1-21e_2-tau_D on identical marked K3 factors, scale 2lambda, exactly four preimages and quaternionic tangent span two. F, the actual jets and collision occurrence remain unproved.

Continue with one finite-order specialization only if the same ambient connection works for every branch. The required test is vanishing of the class defining Nbar, or identification of a precise residual connection term or missing hypothesis. Abandon automatic vanishing if such a term survives; preserve L126 in either case. Full simultaneous holomorphic linearization is unnecessary for this target and must not be assumed. Full matching Mathlib coverage was not checked; unknown coverage is not absence.

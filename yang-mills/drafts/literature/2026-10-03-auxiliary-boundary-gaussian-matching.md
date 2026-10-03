# Auxiliary-field boundary formulation — completed assessment

TARGET: Review whether retaining an independent b field with A_t = c = bar c = b = 0, and no condition on partial_n A_n, yields the tangential Dirichlet/normal Neumann quadratic covariance used in L003 on the cube.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched independent auxiliary-field boundary gauge fixing, relative Hodge quadratic domains on Lipschitz regions, cube BRST conditions and Gaussian Fourier integration; followed Moss–Silva to its auxiliary reduction and inspected Witten, McIntosh–Monniaux, the Cattaneo–Mnev–Reshetikhin boundary-domain appendix and NIST DLMF.
SOURCE_EVIDENCE: Read https://arxiv.org/pdf/gr-qc/9610023v1 sec. II closing paragraph and sec. III (30)–(38), pp. 7–8; https://arxiv.org/pdf/1805.11559v3 secs. 2.2–2.3 (2.18)–(2.27), pp. 8–11; https://arxiv.org/pdf/1608.01797v1 Proposition 2.17, Definition 3.1, Remarks 3.2–3.5 and Theorem 4.3, pp. 6–7, 9–11, 14–15; https://arxiv.org/pdf/1507.01221v2 Appendix A.3.2–A.3.3 (A.9)–(A.11), pp. 65–66; https://dlmf.nist.gov/1.14.E1 and https://dlmf.nist.gov/1.14.T1, Gaussian row. Reuse the prior assessed BRST algebra, without a new cohomology search.
COMPARISON: Known auxiliary reduction and relative Hodge realizations support a regulated Gaussian applicability test, but do not identify the bare boundary traces with a unique cube path-integral prescription. L003 already proves the relative-cochain Hodge covariance and its modes; the missing specialization is the independent auxiliary integration, not another proof of those modes.
GAP: Fix the Euclidean auxiliary contour or Fourier prescription and integration order, specify the scalar and connection spaces, and check the normalized curvature law on the complete cubical complex. Smooth-face equations, off-shell boundary data and the second-order operator domain must remain distinct; no complete continuum auxiliary measure or boundary Ward identity is supplied.
REASON: Complete screening of the unchanged saved target and approve only the finite-mesh auxiliary realization below, using established Gaussian integration and L003. This independently testable specialization avoids assuming a continuum measure replacement or repeating L012's rejected strong-domain test.
SCOPE: Quadratic SU(2) fields about the flat connection in the fixed cube; finite relative cochains, auxiliary-first Gaussian integration and comparison with the already proved L003 law. Nonlinear forest-measure replacement, physical-boundary Ward identities and one-loop subtraction are outside ready coverage.
COVERED_TARGET: At fixed mesh, test a b-first Fourier auxiliary-field realization on L003's relative cochains, with b, c and bar c on interior vertices, for equality of its normalized curvature covariance to L003's Hodge Gaussian.

## Scope and discriminating test

The TARGET is preserved. Its changed hypothesis is the absence of a strong partial_n A_n condition on connection variables before auxiliary integration. Retain the fixed cube, trivial tangential boundary links and flat SU(2) expansion. The literature question is whether an existing prescription, including domains and integration conventions, directly establishes L003's covariance on all faces and intersections.

No inspected full statement meets that test. The source comparisons below identify a bounded specialization with ready coverage, rather than a direct import of the proposed continuum formulation. Equality of that specialization's curvature law has not been calculated in this turn. The literal smooth boundary traces alone are not being accepted as a complete definition of the auxiliary functional integral.

The plausible downstream use is to separate a legitimate Gaussian gauge representation from the failed unrestricted strong domain before formulating boundary Ward identities. It does not supply the desired uniformly O(1) remainder in L011. Even that remainder would leave finite matching and the actual interacting reflected-error threshold <= c_box/2 along a specified coupling trajectory unproved, together with field construction, full limiting reflection positivity, infrared removal and finite positive mass.

The official target is reused from the same-day Clay/Jaffe–Witten check recorded in the [prior assessment](2026-10-03-boundary-brst-counterterms.md); no target or success criterion changes.

## Search and access record

Queries included:

- BRST boundary conditions auxiliary field Maxwell magnetic
- Yang Mills gauge fixing Nakanishi Lautrup boundary Dirichlet b relative boundary conditions quadratic
- Hodge Laplacian cuboid relative boundary conditions sine cosine differential forms Friedrichs
- relative Hodge Laplacian quadratic form Lipschitz boundary
- Witten A Note On Boundary Conditions gauge theory auxiliary
- auxiliary field imaginary boundary Yang-Mills
- cube relative boundary conditions BRST
- Gaussian Fourier transform site:dlmf.nist.gov

No exact cube/auxiliary covariance theorem emerged from the bounded search. This is not an absence or originality claim. Search snippets and secondary pages supplied no premises. Essential comparisons use the inspected primary passages below. The general cohomology and broad boundary-renormalization reviews are reused within their existing scope.

The attempted McIntosh–Monniaux v2 URL did not resolve; the submission history lists only v1, which was inspected. Direct command-line retrieval could not resolve arxiv.org; browser text access supplied the relevant passages. Some PDF screenshot requests timed out and supply no evidence. No essential source is left unread, and no access blocker is being promoted to a mathematical obstruction.

## Inspected statements and their limits

### Auxiliary boundary reduction

I. G. Moss and P. J. Silva, *BRST Invariant Boundary Conditions for Gauge Theories*, [gr-qc/9610023v1](https://arxiv.org/pdf/gr-qc/9610023v1), 14 October 1996, sections II–III, printed pp. 7–8. The end of section II distinguishes retaining and eliminating the auxiliary field. The Maxwell example gives the auxiliary Lagrangian (30), elimination (31), independent-field transformations (33), boundary data (37) and magnetic mixed data (38). The normal Robin condition is presented after elimination, with the stated on-shell nilpotency qualification. This supports the distinction required by L012. It does not specify a convergent Euclidean auxiliary contour or a cube covariance theorem with arbitrary smooth integration variables.

### Euclidean gauge fixing and normal operator data

E. Witten, *A Note On Boundary Conditions In Euclidean Gravity*, [1805.11559v3](https://arxiv.org/pdf/1805.11559v3), 15 July 2023, sections 2.2–2.3, printed pp. 8–11. Equations (2.18)–(2.23) describe the independent multiplet and its elimination. The closing paragraph of section 2.2 discusses retaining the auxiliary field with a different differential-order assignment, but chooses elimination. Equations (2.24)–(2.27) give Dirichlet ghosts and the flat-face normal condition in that reduced formulation. These are smooth-boundary gauge-fixing statements, not an arbitrary off-shell domain-closure theorem or the required finite-cochain matching. Its anti-Hermitian trace convention must not silently determine a real Euclidean auxiliary integration contour.

### Relative Hodge operators on nonsmooth regions

A. McIntosh and S. Monniaux, *Hodge-Dirac, Hodge-Laplacian and Hodge-Stokes operators in L^p spaces on Lipschitz domains*, [1608.01797v1](https://arxiv.org/pdf/1608.01797v1), 5 August 2016. Read the Lipschitz definitions, Proposition 2.17, Definition 3.1, Remarks 3.2–3.5 and Theorem 4.3, printed pp. 4–7, 9–11, 14–15. Minimal/maximal differential domains define the relative realization; its square is the relative Hodge Laplacian. Theorem 4.3 gives the stated Hodge decompositions on very weakly Lipschitz domains in a range containing p = 2. This supplies a framework allowing a cube, rather than a smooth-face restriction. It does not identify an auxiliary Gaussian integral with that realization or provide this notebook's explicit cubical modes. Those remain the local applicability question and the existing L003 result, respectively.

### Boundary trace spaces and eigenfunction spaces differ

A. S. Cattaneo, P. Mnev and N. Reshetikhin, *Perturbative quantum gauge theories on manifolds with boundary*, [1507.01221v2](https://arxiv.org/pdf/1507.01221v2), 30 May 2016, Appendix A.3.2–A.3.3, printed pp. 65–66, (A.9)–(A.11). The appendix distinguishes tangential trace conditions, relative operator conditions and stronger eigenform-compatible conditions; the relative smooth domain need not be preserved by both differential operators. Its boundary components and collar setup are not a theorem for intersecting cube faces. This is supporting domain terminology, not four-dimensional renormalization or auxiliary-measure matching.

### An explicit convergent finite-dimensional integration input

NIST, *Digital Library of Mathematical Functions*, [equation 1.14.1](https://dlmf.nist.gov/1.14.E1) and [Table 1.14.1](https://dlmf.nist.gov/1.14.T1), as read on 2026-10-03. The Gaussian row states the Fourier transform of exp(-alpha t^2), alpha > 0, with the displayed unitary normalization. This is adequate supporting coverage for a real auxiliary Gaussian with an imaginary linear coupling and a specified integration order. No application to cochains, interchange of integrals or covariance identity is performed here. This input cannot construct a positive joint gauge/ghost/auxiliary probability measure or a continuum boundary trace.

## Comparison and continuation decision

| Obligation | What is covered; what remains |
| --- | --- |
| Independent b versus eliminated b | The inspected sources explicitly distinguish them. A pointwise auxiliary equation cannot be treated as an off-shell constraint on every integration variable. |
| Euclidean integration prescription | A Gaussian Fourier identity is available. The exact scalar space, normalization and integration order still need an applicability calculation. |
| Connection boundary space | L003 fixes relative cells and leaves normal links variable. Its Hodge representation is already established, including the whole cubical geometry. |
| Continuum operator and corners | A nonsmooth relative Hodge framework is available. Equality to this auxiliary prescription requires identification; neither a smooth-face example nor ghost equations prove it. |
| Boundary Ward and interaction | No inspected statement replaces L011's forest measure or controls its boundary insertion and remainder. |

**Decision: SPECIALIZE.** Known quadratic reduction, Gaussian integration and Hodge theory cover the mechanism in part. Only the explicit regulator prescription and its comparison with L003 are approved for reproduction. There is no novelty claim and no direct import of the full TARGET. A repeat proof of L003's mode expansion or lower bound would be redundant; the needed difference is the auxiliary prescription and the boundary-data interpretation.

The preapproved test uses L003's finite relative spaces: A on relative links and b, c and bar c on interior vertices, with the same weighted inner products and incidence adjoints. Specify a real Fourier auxiliary integral and perform the b integration first. Alternatively, any use of a joint integral must state a convergent regulator and justify its removal; do not assume unrestricted Fubini or a positive real joint measure. Retain the ghost normalization explicitly, so a determinant or zero mode is not hidden in the comparison. No auxiliary action is evaluated in this assessment.

The sought threshold is exact equality of the normalized curvature covariance at each fixed mesh, with all boundary cells and intersections treated by the same cochain complex. If this is proved, reuse L003's existing sine/cosine and separated reflection results and record only the missing prescription and applicability argument. Continue only to a separately justified Ward formulation. If the proposed realization yields a different quadratic form, extra boundary restriction or undefined normalization, preserve that finding and stop this realization; do not retry the unrestricted strong Neumann domain or infer a boundary divergence. A finite-mesh success alone cannot impose smooth continuum b traces or establish a nonlinear Ward identity.

L003, L012, the whole overview and DAG, the prior two boundary assessments and the recorded failed imports were checked for redundancy. The independent-link, direct positivity, single-factor normalization, compact triplet-only and bulk-only import failures remain preserved. The preceding bulk-locality route remains exhausted at 3 of 3; the informative L012 domain test is retained. This literature turn spends no mathematical exploration turn and resets no external state. Its outcome is EXPLORATION, with new source comparison and one ready bounded specialization, not a mathematical advance.

## Mathlib

Coverage of the full auxiliary-field cube covariance, Gaussian Fourier specialization, BRST-domain statements and relative Hodge results: **not checked**. The precise source identifiers and direct links above distinguish supporting results from a full-statement match. No mathematical result is derived; lemmas, mathematical scripts, PROOF.md and DAG.md remain unchanged. The completed review is LITERATURE / NOVELTY_UNCHECKED; the approved mathematical specialization is REPRODUCTION. STATUS remains IN_PROGRESS with no candidate resolution.

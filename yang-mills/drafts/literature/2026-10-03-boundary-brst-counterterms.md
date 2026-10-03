# Boundary-compatible BRST counterterms — completed assessment

TARGET: Review whether boundary-compatible BRST power counting excludes field-dependent one-loop face and corner counterterms in L011's two-probe response at tau = 1/16.
CHECKED: 2026-10-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched boundary BRST renormalization, relative gauge/ghost domains, composite-insertion counterterms and corners; followed Moss–Silva, Barnich–Brandt–Henneaux and a 2026 Yang–Mills boundary preprint to their primary statements, and compared the positive-flow-time translation insertion.
SOURCE_EVIDENCE: Read https://arxiv.org/pdf/hep-th/0002245v3 secs. 2.2, 2.6, 4.4, 8.6, 11.1, Theorem 11.1 and sec. 12.2; https://arxiv.org/pdf/gr-qc/9610023v1 secs. II–III, (31), (33), (37)–(39); https://arxiv.org/html/2604.05082v1 sec. 2, (2.5)–(2.11), sec. 4, (4.1), sec. 4.3 and sec. 6; https://arxiv.org/pdf/1306.1173v1 secs. 3.2 and 6, (3.12)–(3.13), (6.4), (6.11)–(6.16). Reused the delimited slab and flow statements from 2026-09-27-fixed-box-one-loop-locality.md.
COMPARISON: Bulk cohomology, smooth-face spectral boundary conditions and the flow-boundary translation insertion are supporting results; none supplies the all-stratum, source-extended classification for L011. The eigenfunction/on-shell qualification leaves an explicit off-shell domain check before a BRST exclusion can be invoked.
GAP: Establish the appropriate gauge/ghost domain and source-dependent Ward identity, retain physical surface terms and intersections with flow time zero, and justify any gauge replacement of the forest coefficient. No complete boundary exclusion, surviving counterterm coefficient or O(1) remainder is established.
REASON: Finish the exact saved screening without assuming its desired exclusion. Park the broad counterterm import and preapprove a bounded mathematical compatibility test of the proposed local domain; the original subtraction target and its quantitative gaps remain open.
SCOPE: Supporting citations and the explicit domain test below are covered. No source is a match for the full fixed-box one-loop response, boundary cohomology with corners, or interacting reflected-error estimate.
COVERED_TARGET: Test off-shell BRST closure of A_t = 0, partial_n A_n = 0 and c = bar c = b = 0 on every face of (-4,4)^4 for smooth SU(2) fields, without imposing a ghost equation.

## Exact target, gap and continuation threshold

The TARGET is unchanged. Preserve SU(2), D = (-4,4)^4, a = 8/N with even N, fixed links contained in the geometric boundary, both bare-normalized probes, tau = 1/16 and the exact L010/L011 generator. The object is Gamma_(i,a) in L011 (6), i = 3,6, with action, coordinate Haar density, residual insertion and nonlinear flow retained. The separate Haar divergence is still needed when assembling the full Ward response. Normal links touching the boundary remain variable.

The intermediate question is whether source-compatible boundary power counting and BRST identities actually exclude field-dependent terms on all physical strata. This could identify the subtractions needed for the [saved uniform O(1) remainder](2026-09-27-physical-boundary-remainder.md). The bulk triplet classification in L006 does not answer it. A permitted class would require a matching or decoupling argument; permission alone would not prove a nonzero coefficient.

The source test was an applicable statement with gauge and ghost domains, the actual insertion or its sources, faces and codimension-two, -three and -four intersections, including meetings with flow time zero. Continue to a quantitative subtraction only when these obligations are accounted for. A theorem for an action determinant, a bulk cohomology representative, or the auxiliary flow boundary alone fails this test.

No achieved estimate here improves the actual interacting requirement |Q^(D,matched)_(a,g(a)) - qhat^D_a| <= c_box/2 along a specified coupling trajectory. Even a complete perturbative exclusion would leave finite matching, cutoff-uniform interacting control, field construction, full limiting reflection positivity, infrared removal and finite positive mass unproved.

The [Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) still links the 14-page [Jaffe–Witten statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf). Section 4, printed p. 6, and footnote 2, p. 12, were rechecked on 2026-10-03. The exact target and finite-mass qualification in the [existing audit](../../foundations/01-target-and-scope.md) are retained.

## Search and reading record

Queries included:

- Yang Mills boundary BRST renormalization counterterms relative boundary conditions corners
- BRST invariant boundary conditions Yang Mills ghost Dirichlet Moss Silva
- Yang Mills gradient flow translation Ward identities boundary counterterms local composite insertion
- Barnich Brandt Henneaux local BRST cohomology Yang Mills boundaries total derivatives
- site:arxiv.org "BRST-invariant boundary conditions for gauge theories"
- site:arxiv.org "Worldline Images for Yang-Mills Theory within Boundaries"
- site:arxiv.org "Ward identities" "gradient flow" "translations"
- site:arxiv.org "Yang-Mills" "boundary counterterms" renormalization
- site:arxiv.org "Yang-Mills" "boundary" "BRST" "composite" counterterms
- site:arxiv.org "Yang-Mills" "corners" "counterterms" renormalization
- site:arxiv.org "relative boundary conditions" "off-shell" "BRST"

The last, narrowly conjunctive searches returned no result. This is search evidence, not evidence of nonexistence or originality. Primary full statements, rather than those searches or abstracts, determine the comparisons below.

The requested Del Debbio–Patella–Rago v2 PDF did not resolve; its submission history lists only v1, which was read through the versioned PDF. A repository PDF search lead with an unverified identity did not resolve and supplies no premise. No essential premise of this assessment is left behind either access attempt. Sources already adequately delimited in the prior assessment are reused.

## Inspected primary statements and applicability

### Bulk cohomology and operator mixing

G. Barnich, F. Brandt and M. Henneaux, *Local BRST cohomology in gauge theories*, [hep-th/0002245v3](https://arxiv.org/pdf/hep-th/0002245v3), 13 November 2000. Read the BRST algebra in (2.8)–(2.9), the nonminimal sector (2.47), sections 4.4, 8.6, 11.1, **Theorem 11.1**, printed p. 104, and section 12.2, pp. 117–118.

Under the stated normality, regularity and gauge-group assumptions, the theorem classifies local cocycles modulo BRST variations and spacetime derivatives. Section 12.2 gives the semisimple ghost-number-zero representatives, with the odd-dimensional Chern–Simons qualification. Section 8.6 covers local gauge-invariant operator mixing and BRST-exact partners; its stated decoupling concerns the physical S matrix.

Section 4.4, p. 25, explicitly restricts the identification of local functionals modulo derivatives to contexts in which surface terms can be neglected or are outside consideration. This prevents using the bulk quotient as the requested physical-boundary classification. The result provides no boundary-domain or corner prescription for L011. The standard transformations are supporting input for the covered domain test, not a full theorem match.

### Local boundary data, with the auxiliary-field qualification

I. G. Moss and P. J. Silva, *BRST Invariant Boundary Conditions for Gauge Theories*, [gr-qc/9610023v1](https://arxiv.org/pdf/gr-qc/9610023v1), 14 October 1996; Phys. Rev. D 55 (1997), 1072. Read sections II–III, especially (31), (33), (37)–(39), printed pp. 7–8.

The Maxwell example retains the auxiliary field b before passing to the familiar mixed magnetic boundary conditions: tangential potential and ghosts vanish, with a Robin normal component. Equation (31) eliminates b, and the accompanying discussion states the resulting on-shell nilpotency qualification. This is useful domain information for a smooth face. It does not assert arbitrary off-shell nonlinear SU(2) closure on a cube or classify counterterms for composite sources at intersections.

### A newer Yang–Mills boundary calculation and its spectral scope

S. Christiansen Murguizur, L. Manzo and P. Pisani, *Worldline Images for Yang-Mills Theory within Boundaries*, [2604.05082v1](https://arxiv.org/html/2604.05082v1), 6 April 2026; [43-page PDF](https://arxiv.org/pdf/2604.05082v1). Read section 2, printed pp. 7–10, (2.5)–(2.11); section 4, (4.1); section 4.3, pp. 28–29; and section 6. Its submission history lists v1.

The half-space calculation supplies relative/absolute gauge and ghost operators and a worldline representation. Preservation of the relative normal condition specifically invokes a Laplacian eigenfunction gauge parameter. That restriction must be retained when using its Dirichlet-ghost conclusion.

The computed heat coefficients are a_0, a_1 and a_2 in the convention T^(-D/2) sum_n a_n T^(n/2), rather than a complete four-dimensional logarithmic coefficient. No physical corners, flow insertion or source-extended exclusion for L011 is computed. This inspected preprint is supporting evidence, not an independently reviewed renormalization theorem.

### The actual translation insertion is more specific than action renormalization

L. Del Debbio, A. Patella and A. Rago, *Space-time symmetries and the Yang-Mills gradient flow*, [1306.1173v1](https://arxiv.org/pdf/1306.1173v1), 5 June 2013. Read sections 3.2 and 6, (3.12)–(3.13), (6.4), and (6.11)–(6.16), printed pp. 7–8 and 14–16.

The translation variation of a positive-flow-time probe is represented by an insertion involving the flow multiplier at flow time zero. Their dimension-five mixing discussion permits multiplicative generator matching, while excluding the stated additive bulk mixings; positive flow time avoids the contact terms of unflowed probes. The lattice discussion separately retains translation restoration and residual qualifications.

This concerns the auxiliary flow boundary and the specified translation generator. It neither supplies physical-face/corner domains nor identifies L010's endpoint-averaged generator with that regulator prescription. It cannot set L011's residual to zero or its generator normalization to one in the fixed box.

### Previously inspected action and flow statements

Reuse [the locality assessment](2026-09-27-fixed-box-one-loop-locality.md). Lüscher–Narayanan–Weisz–Wolff, [hep-lat/9207009v1](https://arxiv.org/pdf/hep-lat/9207009v1), sections 3.3–3.5, computes one-loop field-dependent slab action divergences. Section 2.5, printed pp. 10–11, was also inspected here: its boundary polynomial and parity argument concerns the gauge-invariant Schrödinger-functional effective action. It does not classify L011's mixed insertion on all physical strata. In particular, it must not be weakened to mere invariance under boundary-fixed transformations and then treated as the same theorem.

Lüscher–Weisz, [1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7.1–7.4, remains the previously inspected flow-counterterm input. Its locality assumption and BRS identity concern the auxiliary t = 0 boundary following ordinary renormalization. No claim that they eliminate physical-boundary/flow-boundary intersections is imported.

## Comparison obligations and assessment decision

These are source-applicability findings, not newly derived exclusions:

| Required feature | Status after the comparison |
| --- | --- |
| Allowed gauge transformations | L003 fixes transformations at boundary vertices. A local nonlinear gauge/ghost replacement of its exact forest measure has not been established. Its Gaussian Hodge representation is not such a replacement. |
| Smooth-face domains | Known magnetic/relative data are available, with the on-shell or eigenfunction qualifications above. Off-shell compatibility of the proposed cube domain has not been tested. |
| Faces and higher intersections | No inspected classification treats all physical strata with these sources and matching conditions. Smooth half-space results do not supply it. |
| Composite and generator sources | Bulk action power counting does not, by itself, establish the source-dependent classification for the full residual. Both probes and bare coupling factors must be retained. |
| Meetings with flow time zero | Final tau > 0 leaves internal flow times approaching zero. Physical boundary data for the extended gauge/ghost/flow system remain to be justified. |
| Exact and field-independent terms | S-matrix decoupling is not the needed connected Euclidean insertion identity. Total derivatives and purely geometric determinant terms require their own applicability check. |
| Quantitative continuation | No uniform boundary remainder, finite matching coefficient, or reflected-error estimate follows from this review. |

**Decision: EXPLORE.** The bounded search and theorem-level comparison are complete without an adequate full match. The new evidence identifies a precise domain qualification and distinguishes the source-dependent translation insertion from the two prior action/flow arguments. It does not prove that any boundary class survives, has nonzero coefficient, or makes the response divergent. No mathematics beyond the checked sources is established.

The overview, DAG, L003 and L007–L011 definitions, the two preceding source assessments and the recorded failures were checked. The beta = 0 construction, direct positivity import, single-factor normalization, triplet-only displacement and bulk-only locality import remain stopped as recorded. Further bare coefficient expansion or another blanket theorem lookup would not resolve the domain issue.

## Ready bounded compatibility test

The COVERED_TARGET is approved for a mathematical turn. It tests a necessary premise of the proposed BRST mechanism, using the stated smooth flat-face data and standard nonlinear BRST transformations. All fields are smooth up to the closed cube; A_t denotes each tangential component, A_n its normal component, and partial_n the outward normal derivative, separately on every face. c and bar c are ghost and antighost, with arbitrary smooth Grassmann coefficients; b is independent and retained. A flat SU(2) connection and a single-colour ghost profile supported near a face interior are admissible starting tests.

Use sA = D_A c, sc = -[c,c]/2, s bar c = b and sb = 0 in a consistent anti-Hermitian convention, after absorbing the coupling into the connection. These are the cited standard algebra, not a new result. Directly test preservation of every proposed boundary condition without restricting to ghost eigenfunctions or using field equations. No closure calculation or counterexample is supplied in this literature turn.

A smooth failure on one face would stop this particular off-shell domain shortcut, without invalidating L003 or the spectral determinant results. If the test succeeds, source identities and corner compatibility still require justification before any classification or quantitative subtraction. This is a compatibility test, not a new one-loop calculation or a change of the Wilson measure. Its appropriate research classification is REPRODUCTION; no novelty is claimed for this specialization of known domain issues.

The previous bulk-locality route's three-turn exhaustion is preserved. This literature turn spends no mathematical exploration turn and resets no runner counter. The broad boundary-exclusion import is parked in favor of the explicit test, rather than being treated as a theorem ready for application.

## Mathlib

Coverage of the full boundary/insertion classification, the supporting BRST/cohomology and boundary-domain results, and the covered smooth-domain specialization: **not checked**. The precise theorem names and direct primary links above are literature references, not asserted Mathlib matches. No lemma, mathematical script, mathematical assembly or DAG input changes this turn. STEP_CLASSIFICATION is NOVELTY_UNCHECKED; STATUS remains IN_PROGRESS with no candidate solution.

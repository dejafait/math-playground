# Fixed-box one-loop locality — completed source assessment

TARGET: Review whether a one-loop locality theorem covers L011's combined response in L010's all-face fixed box and reduces its logarithmic coefficient to bulk matching.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched one-loop lattice logarithm universality, Yang–Mills physical-boundary renormalization, corner heat coefficients, and finite-volume gradient flow; followed the heat-kernel bibliography to Apps–Dowker and inspected the primary statements below.
SOURCE_EVIDENCE: Read Adams–Lee 0709.0781v3 sec. II and Appendix A theorem (A1); Lüscher et al. hep-lat/9207009v1 secs. 3.3–3.5; Apps–Dowker hep-th/9712019v1 secs. 2–3, 8–9, 12; Fritzsch–Ramos 1301.4388v2 secs. 2.1–2.2; Cattaneo–Mnev–Reshetikhin 1507.01221v2 Remark 1.1 and sec. 1.5; rechecked Lüscher–Weisz 1101.0963v2 secs. 7.1–7.4. Direct links and precise scopes follow.
COMPARISON: The inspected results do not establish the full all-face mixed-response reduction; they cover restricted momentum integrals, a slab effective action, or different corner operators and geometries.
GAP: A cutoff-uniform comparison of the actual combined response with bulk subtractions, including physical faces, their higher intersections, flow times approaching zero, and the actual insertion, remains unproved.
REASON: The bounded review is complete without an adequate theorem match; stop the unsupported bulk-only import at the third exploration turn, preserve the target and partial work, and claim neither a logarithmic coefficient nor a new ultraviolet estimate.

## Exact target, relevance, and threshold

Keep SU(2), D = (-4,4)^4, a = 8/N with even N, all fixed boundary links, bare g, tau = 1/16, L010's endpoint-averaged clover generator, plaquette-triplet/clover-shear insertions, and both centered nonlinear Wilson-flow probes. The coefficient under review is L011's Gamma_(i,a) in Cov(O_i, V_a S_g - J_3 - J_6). Its coordinate Haar-density correction is distinct from the already-separated divergence coefficient of L010.

The intermediate question is whether a named locality theorem accounts for every possibly divergent contribution and controls the remainder sufficiently to reduce this coefficient to bulk matching. This could identify the required normalization of a nonzero observable sector. The eventual interacting reflection comparison still needs error <= c_box/2 along a specified coupling trajectory. A perturbative O(1) remainder or a known logarithm would not meet that threshold. Field construction, full limiting reflection positivity, infrared removal, and finite positive mass remain unresolved.

The official [target audit](../../foundations/01-target-and-scope.md) and the adequate bulk matching portions of the [prior assessment](2026-09-26-current-target.md) are reused. No regulator, observable, coupling convention, or scope of the main goal is changed.

The discriminating test set before the review was: locate an applicable theorem with all insertion and boundary hypotheses, or identify the exact unsupported comparison and decide whether the source shortcut can continue. Failure to find coverage is not proof that the coefficient diverges or that such a theorem cannot exist.

## Search record

Queries on the checked date included:

- Yang Mills one loop renormalization rectangular box corners boundary heat kernel gauge theory locality
- Reisz lattice power counting theorem finite volume boundaries renormalization
- gradient flow Schroedinger functional renormalization boundary counterterms finite volume gauge theory
- McAvity Osborn quantum field theories manifolds boundaries renormalization one loop gauge fields corners
- "one-loop" "lattice" "logarithmically" "Adams" "Lee"
- "heat kernel" "Yang-Mills" "corners"
- "boundary" "corners" "Yang-Mills" "renormalization" -site:qft.org -site:scribd.com
- "all" "Dirichlet" "Yang-Mills" "one-loop" "box" renormalization
- Apps Dowker "C2" "piecewise" heat kernel

D. V. Vassilevich, [hep-th/0306138v3](https://arxiv.org/pdf/hep-th/0306138v3), section 6.4, printed p. 63, and reference [17], served as a discovery guide to the primary corner calculation below. The conclusion does not rely on the survey as a replacement for reading that calculation. Search snippets, secondary sites, and unrelated two-dimensional/topological Yang–Mills results are not imported.

## Inspected primary statements

### One-loop logarithms and quantitative convergence

D. H. Adams and W. Lee, *Structure of logarithmically divergent one-loop lattice Feynman integrals*, [arXiv:0709.0781v3](https://arxiv.org/pdf/0709.0781v3), 5 December 2007, Phys. Rev. D 77, 045010. Read section I, (1)–(4); section II, (7)–(15), printed pp. 5–7; section VI; and the **Appendix A extended power-counting theorem**, (A1), p. 19.

For their Brillouin-zone integrals with smooth scaled numerator/denominator, polynomial continuum limits, denominator positivity/growth, no additional zeros, and infrared convergence, lattice degree zero gives I(p,a) = f(p) log(aM) + g(p) + h(p,M) + o(1), with universal f and h. For negative lattice degree, (A1) bounds the continuum-limit error by c(p) a log(1/a) for fixed p. The constants are momentum dependent.

This is a strong supporting theorem, but does not supply a finite-box kernel comparison. Neither L011's forest-gauge cumulants nor its flow-time integrals have been placed in the required class with uniform control of subsequent external sums. Reproving the covered theorem would be redundant.

### Physical boundary renormalization in a slab

M. Lüscher, R. Narayanan, P. Weisz and U. Wolff, *The Schrödinger functional — a renormalizable probe for non-abelian gauge theories*, [hep-lat/9207009v1](https://arxiv.org/pdf/hep-lat/9207009v1), 9 July 1992. The earlier section 2.5 reading is extended to sections 3.3–3.5, printed pp. 17–22, especially (3.21), (3.25)–(3.28), and (3.35)–(3.37).

For the specified background problem with positive fluctuation operators, the gauge and ghost determinants have a one-loop field-dependent singularity canceled by coupling renormalization. The heat coefficients separate volume and temporal-face contributions; gauge invariance excludes an additional field-dependent boundary contribution at logarithmic order in that calculation.

This is an actual one-loop computation, stronger than citing section 2.5's general discussion alone. Its periodic spatial directions and two physical end faces, and its effective-action observable, leave the all-face box and mixed flowed insertion outside the inspected result. No coefficients are transferred.

### Corner coefficients and their geometric hypotheses

J. S. Apps and J. S. Dowker, *The C2 Heat-Kernel Coefficient in the Presence of Boundary Discontinuities*, [hep-th/9712019v1](https://arxiv.org/pdf/hep-th/9712019v1), submitted 2 December 1997, Class. Quantum Grav. 15 (1998), 1121–1139. Read sections 2–3, pp. 3–5; the right-angle restrictions (43) and result (51) in section 8, pp. 15–16; the smeared result (52), p. 17; and section 12, p. 24. The arXiv version identifier is used rather than the regenerated title-page date.

Their scalar Dirichlet calculation includes codimension-two integrals, with a Robin extension; intersections are assumed closed and smooth. The explicit right-angle formula retains condition (43). General mixed-projector boundary data are not completed.

Thus even this corner result is not the relative gauge/ghost problem on a four-box whose faces have further intersections. It does not show a nonzero boundary term in L011. Pure geometric determinant terms must not be mistaken for a contribution to its connected covariance.

### Flow with physical boundaries

P. Fritzsch and A. Ramos, *The gradient flow coupling in the Schrödinger Functional*, [arXiv:1301.4388v2](https://arxiv.org/pdf/1301.4388v2), 13 September 2013, JHEP 10 (2013) 008. Read sections 2.1–2.2, printed pp. 3–7, (2.5)–(2.9), (2.19)–(2.28).

They impose periodic spatial directions and temporal Dirichlet data and compute the leading finite-volume flowed energy density with the corresponding heat kernels. The displayed infinite-volume one-loop formula (2.3) is distinguished from this finite-volume leading-order computation. Neither is L011's one-loop residual.

M. Lüscher and P. Weisz, [arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), 10 February 2011, sections 7.1–7.4, pp. 20–23, (7.4)–(7.8), was rechecked for the meaning of locality. Its counterterm analysis concerns the extra flow direction and its t = 0 boundary after ordinary renormalization. This remains supporting bulk input; it is not a theorem eliminating physical face/corner terms in the specified box. The prior assessment's bare-normalization and generator qualifications remain in force.

### A general boundary-gauge framework is not the missing renormalization theorem

A. S. Cattaneo, P. Mnev and N. Reshetikhin, *Perturbative quantum gauge theories on manifolds with boundary*, [arXiv:1507.01221v2](https://arxiv.org/html/1507.01221v2), 30 May 2016, Commun. Math. Phys. 357 (2018), 631–730. Read Remark 1.1 and section 1.5, including its displayed theorem.

Remark 1.1 assumes smooth compact oriented manifolds with boundary. Section 1.5 explicitly leaves renormalization issues unresolved for the general framework; the stated theorem concerns the described BF-like configuration-space constructions, including two-dimensional Yang–Mills. This cannot be used as a four-dimensional Wilson-flow locality/renormalization theorem. No master-equation or gluing result is imported into the argument.

## Comparison with the actual response

The following are applicability obligations, not newly derived estimates:

| Required feature | What must still be supplied |
| --- | --- |
| Complete connected coefficient | Account for the action, coordinate density, insertion, and nonlinear-flow terms together; the isolated Haar-divergence bound does not do this. |
| Actual gauge reduction | Justify any replacement of the higher forest-gauge vertices by another gauge's kernels and vertices, including its measure. |
| All physical faces and intersections | Establish a remainder bound for this geometry and these boundary data; a finite slab result cannot simply be assigned to them. |
| Flow times reaching zero | Control the time integrations and internal subgraphs, including those not incident to a final heat factor. |
| Bare-normalized operators | Retain both 1/g^2 factors and the generator/representative matching before drawing conclusions from renormalized finiteness. |
| Continuation toward positivity | Supply finite matching and a nonperturbative error <= c_box/2 later; none of the inspected perturbative statements yields it. |

A position-space bulk subtraction with a uniformly O(1) complete boundary remainder would be a useful sufficient intermediate test, provided its definition and all summations were justified. That proposal is not proved here. Compact support of the displacement alone does not settle it, because the nonlinear flowed probe depends on the initial field throughout the box.

## Unread leads and reuse limits

Caracciolo–Menotti–Pelissetto's 1992 general-discretization matching paper remains an unread lead, as recorded with access attempts in the prior assessment. No use is made of its uninspected formulas. Reisz's original general power-counting papers and McAvity–Osborn's scalar boundary paper were search leads, not newly inspected premises; the stated one-loop comparison uses Adams–Lee's own theorem.

No essential cited premise of this scope assessment is unread. This does not establish an exhaustive absence theorem for the literature. In particular, the remaining analytic comparison cannot be called novel on the strength of these searches. Any proposed use of an unread result must first resolve its statement and hypotheses.

## Completed assessment and stopping decision

The overview, DAG, L008–L011, the previous combined-response assessment, histories 012–013, and all four earlier failed routes were checked. No existing lemma controls the missing remainder. Repeating L010, its free heat-trace argument, a triplet-only projection, or the coefficient expansion would not fill that gap.

The review resolves the pending theorem comparison: **no inspected result licenses the proposed direct bulk-only reduction**. This is a source-scope finding, not a counterexample or a proof of a surviving logarithm. The [stopped import record](../../ATTEMPTS/005-fixed-box-bulk-locality-import.md) preserves that distinction.

Outcome: **EXPLORATION**, the **third of three** turns since L010. Stop this unsupported import and further formal expansion under the exhausted exploration budget. No reset, mathematical advance, or informative divergence result is claimed. The narrower boundary-subtraction target recorded in PROGRESS.md needs a separate assessment; saving it does not authorize an additional exploration turn or alter runner state.

This literature-only turn imports supporting statements by precise citation, reproduces no calculation, and establishes no mathematics beyond the checked sources. STEP_CLASSIFICATION is NOVELTY_UNCHECKED. No lemma, mathematical script, overall mathematical assembly, or dependency is changed. STATUS remains IN_PROGRESS with no complete candidate.

## Mathlib

Coverage of the full fixed-box locality reduction: **not checked**. Coverage of the supporting lattice power-counting, boundary heat-kernel, and flowed renormalization statements: **not checked**. The named source theorem and direct links above are literature references, not Mathlib matches.

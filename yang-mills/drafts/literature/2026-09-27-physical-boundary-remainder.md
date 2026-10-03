# Physical-boundary remainder after bulk subtraction — completed assessment

TARGET: Test whether a position-space bulk subtraction leaves a uniformly O(1) physical-boundary remainder in L011's combined one-loop coefficient for both probes at tau = 1/16.
CHECKED: 2026-10-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched position-space Yang–Mills boundary renormalization, cutoff-uniform half-space remainders, general vector heat-kernel boundary estimates, and physical-boundary gradient flow; followed the scalar surface-counterterm comparison to the 2026 truncation preprint.
SOURCE_EVIDENCE: Read https://arxiv.org/pdf/1604.00784v1 Theorem 1.1, p. 3; https://arxiv.org/pdf/1609.02220v3 secs. 4.6.4–4.8 and Theorem 5.3.1, pp. 46–47; https://arxiv.org/html/2305.18862v1 secs. I, III–IV and VI, Theorem 1, Proposition 4, Corollary 1 and Theorem 2; https://arxiv.org/html/2606.23650v2 secs. I and II.4, Theorems 1–2. Versions and applicability limits follow.
COMPARISON: The inspected statements supply an interior vector-kernel comparison, scalar renormalization with specified boundary counterterms, and localization of already-renormalized scalar correlators; none bounds the complete subtracted L011 coefficient.
GAP: Define the bulk subtraction for every connected subgraph in the actual box and justify the absence or subtraction of physical-boundary terms, gauge/measure equivalence, derivative lattice bounds, and internal flow-time integrals for both probes.
REASON: Complete the saved assessment with direct primary URLs; retain its O(1) estimate as unresolved and investigate boundary-counterterm classification before attempting the entire remainder. Neither source absence nor scalar scope differences prove a Yang–Mills divergence.

## Exact target and relevance

The TARGET is unchanged from the pending assessment. Keep SU(2), D = (-4,4)^4, a = 8/N with even N, fixed links on every physical face, bare g, tau = 1/16, the endpoint-averaged clover generator, and both triplet/shear Wilson-flow probes. The object is Gamma_(i,a) in L011 (6), for i = 3,6, including action, coordinate Haar density, insertion and nonlinear-flow corrections. L010's Ward divergence remains separately accounted for.

The sought intermediate result is a bound on the complete physical-boundary remainder uniform as a tends to zero after a specified bulk subtraction. A source match must give the subtraction, hypotheses and control of all integrations; selected image terms or an external heat trace do not meet that test. Such control could support the bulk matching program. It would still leave bulk coefficient evaluation, finite matching, and the interacting reflected error <= c_box/2 along a specified coupling trajectory unresolved. No achieved estimate here approaches that required threshold.

The [Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) was checked on 2026-10-03: it still links the 14-page [Jaffe–Witten statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), section 4, p. 6, with finite positive mass and footnote 2, p. 12. The [target audit](../../foundations/01-target-and-scope.md) is reused. Field construction, limiting reflection positivity and infrared removal remain necessary.

## Search and reading record

Queries on the checked date included:

- position space renormalization Yang Mills boundary heat kernel bulk subtraction uniform boundary remainder
- "Yang-Mills" "boundary" "renormalization" position space
- "quantum field" "half-space" "renormalization" "flow equations"
- site:arxiv.org "Heat Kernel Renormalization on Manifolds with Boundary"
- site:arxiv.org Borji Kopper "half-space" renormalization
- site:arxiv.org "Yang-Mills" "boundary" "position-space"
- "not feeling the boundary" heat kernel derivatives Dirichlet Neumann lattice uniform estimates
- "Yang-Mills" "boundary" "BRST" "counterterms"
- "Yang-Mills" "physical boundary" "gradient flow" renormalization

The scalar surface paper and the new truncation preprint were read beyond their abstracts. The version identifiers below control; regenerated HTML title-page dates are not substituted for submission/revision dates. A request for a nonexistent Li–Strohmaier v2 failed; the accessible v1 was read. No essential premise remains behind that access attempt.

## Inspected primary statements

### Interior vector heat kernels

L. Li and A. Strohmaier, *Heat Kernel Estimates for General Boundary Problems*, [arXiv:1604.00784v1](https://arxiv.org/pdf/1604.00784v1), 4 April 2016. Read section 1, pp. 1–3, especially **Theorem 1.1**, p. 3.

For any open U in R^d, d >= 2, and a nonnegative self-adjoint extension of the componentwise vector Laplacian, the theorem bounds the difference from the full-space heat kernel by an explicit boundary-distance factor times exp[-(rho(x)+rho(y))^2/(4t)], for 0 < t <= (rho(x)+rho(y))^2/8. Constants do not depend on the chosen extension; the statement does not require a smooth boundary.

This improves the available supporting mechanism: corners and relative vector data are not automatically excluded from an interior kernel estimate. Identification of the relevant continuum operator is still required. The theorem does not state a uniform lattice derivative estimate or control integrated boundary subgraphs in L011.

### Heat-kernel renormalization with a physical boundary

B. I. Albert, *Heat Kernel Renormalization on Manifolds with Boundary*, [arXiv:1609.02220v3](https://arxiv.org/pdf/1609.02220v3), 29 March 2020; [HTML](https://arxiv.org/html/1609.02220v3). Read sections 3.7, 4.1, 4.6.4–4.6.5, 4.8, and Definitions 5.3.1–5.3.2 with **Theorem 5.3.1**, pp. 46–47.

The main theorem constructs scalar effective interactions after counterterms for the stated Dirichlet/Neumann theories, with the specified boundary geometry, including a cylindrical collar. Section 4.6.5 retains boundary-local functionals in the subtraction. Its auxiliary polyhedral Gaussian-integral discussion does not enlarge the main theorem into a lattice gauge theory with corners.

This is a position-space renormalization procedure, not an assertion that bulk subtraction alone suffices. Its gauge, insertion, geometry and regulator differences remain substantial. Reproving its covered scalar result would not resolve them.

### A rigorous bulk/surface split and its boundary prescriptions

M. Borji and C. Kopper, *The Surface Counter-terms of the phi^4_4 Theory on the Half Space*, [arXiv:2305.18862v1](https://arxiv.org/html/2305.18862v1), 30 May 2023; [59-page PDF](https://arxiv.org/pdf/2305.18862v1). Read sections I, III–IV, and VI: **Theorem 1 (Boundedness)**, **Proposition 4**, **Corollary 1**, **Theorem 2 (Convergence)** and their boundary prescriptions.

For massive scalar theory, the surface power counting improves by one power, but Robin/Neumann finiteness uses two surface parameters. The Dirichlet conclusion concerns the stated amputated correlators and Dirichlet heat-kernel tests. Section I excludes a normal-derivative boundary insertion. Its bulk part is a full-space propagator with interaction restricted to the half-space; its counterterms may depend on normal position.

The source therefore does not supply the ordinary translation-invariant bulk subtraction needed here. None of these scalar prescriptions can be assigned to the relative gauge/ghost components or the mixed composite response.

### The stronger, newer truncation statement

M. Borji, *Position-Space Renormalization and Half-Space Truncations in phi^4_4*, [arXiv:2606.23650v2](https://arxiv.org/html/2606.23650v2), 8 August 2026; [86-page PDF](https://arxiv.org/pdf/2606.23650v2). Read section I and section II.4, **Theorem 1 (Besov Regularity)**, **Theorem 2 (Half-space Truncation)** and Corollary 1.

The preprint states cutoff-uniform distributional localization of already-renormalized massive scalar correlators by half-space indicators, with specified regularity loss. Section I explicitly keeps the original action, propagator and renormalization conditions. This removes the possible ambiguity between truncating a bulk correlator and constructing a theory with a physical boundary.

Its statement has been inspected, not independently audited or imported into the Yang–Mills assembly. It does not control L011's boundary-conditioned measure or insertion.

## Comparison obligations and decision

The following are unresolved applicability tests, not derived estimates:

| Requirement of the saved target | What the source comparison leaves open |
| --- | --- |
| Precise bulk subtraction | Specify local subgraph counterterms and how they act with the actual box kernels. Equality with a subtraction of entire full-space amplitudes is not established. |
| All faces and higher intersections | Classify and control possible boundary-supported terms. Interior kernel bounds leave integration points approaching these strata untreated. |
| Relative gauge/ghost data | Justify the operator domains and identities that permit a local gauge description of the exact forest-gauge coefficient. |
| Complete mixed insertion | Retain both channels and every action, coordinate-density, generator and flow correction; action renormalization alone is insufficient. |
| Flow times reaching zero | Bound internal time integrations and differentiated kernels; final positive tau supplies no lower bound on every internal time. |
| Actual reflected observable | Prove finite matching and later error <= c_box/2; an O(1) perturbative coefficient does not imply either. |

The [prior locality assessment](2026-09-27-fixed-box-one-loop-locality.md) remains adequate for its momentum-integral, slab, corner and flow statements. Those results are reused, not re-searched. All five recorded attempts and the overview/DAG were checked. L010's isolated correction and L011's fixed-mesh expansion do not settle this remainder; the earlier beta = 0, positivity-import, single-factor and triplet-only failures remain preserved.

**Decision: EXPLORE**, a completed bounded source assessment with no adequate theorem match, not a novelty claim. The new evidence identifies usable linear-kernel control and the precise counterterm/observable distinctions missing from the proposed shortcut. It neither proves nor disproves the saved estimate. No result is derived, and no lemma, mathematical script, argument assembly or graph input changes.

## Distinct mechanism and continuation test

Three mechanisms were compared: direct import of bulk locality (already stopped), a quantitative position-space subtraction (still lacks a complete boundary prescription), and classification of boundary-local counterterms using boundary-compatible gauge/BRST identities. Select the third for screening. It asks which terms can occur before estimating the full remainder; it does not repeat the stopped theorem lookup or expand additional unevaluated cumulants.

The discriminating test is whether an applicable classification accounts for field-dependent one-loop terms on every physical stratum, including the actual insertion and any intersection with flow time zero. Continue toward quantitative subtraction only if the boundary domain and all potentially relevant terms are accounted for. A permitted term that cannot be shown to decouple requires additional matching, not a claim that its coefficient is nonzero. An unavailable identity or incomplete classification must be recorded as a gap and the test bounded or redirected.

No classification or exclusion is performed this turn. The new target has its own REVIEW_REQUIRED assessment; PROGRESS.md alone records the current Next action. The earlier three-turn exhaustion and stopped import are preserved, and this required recovery does not edit or reset external counters.

## Reuse, unread leads, and Mathlib

Known statements above are supporting citations. No full matching result is imported, no calculation is reproduced, and no mathematics beyond the checked literature is established. STEP_CLASSIFICATION is NOVELTY_UNCHECKED; STATUS stays IN_PROGRESS with no candidate solution.

The older Caracciolo–Menotti–Pelissetto general-discretization paper remains an unread, nonessential lead as recorded previously; it was not retried. The separate restricted-interaction work mentioned by the 2026 preprint was not read and supplies no premise. General boundary-BRST claims need their own source review before use. A failed search is not an absence theorem.

Mathlib coverage of the full remainder, supporting vector heat-kernel estimates, boundary renormalization and BRST classification: **not checked**. The source theorem names and direct URLs above are literature references, not asserted Mathlib matches.

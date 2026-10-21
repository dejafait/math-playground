# Coupled Gaussian first-Laguerre transfer — source assessment

TARGET: Derive the gamma-normalized error in replacing F_ε′²−F_εF_ε″ by the first Laguerre expression of F_0+εG on |ξ|≥40, ε(1+ξ²)≤1, and state the signed margin required for transfer using L366.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Four bounded queries on generalized Laguerre perturbation, Gaussian-regulated zeta error, and stability; inspected the primary Csordas–Vishnyakova statement and relevant proof passages, and reused the scalar response assessments.
SOURCE_EVIDENCE: Csordas and Vishnyakova, Central European Journal of Mathematics 11(9) (2013), 1643–1650, DOI 10.2478/s11533-013-0269-x, Theorem 2.3, Remarks 1.3 and equation (1), pp. 1644–1646, https://d-nb.info/1372516522/34; scalar Paris/DLMF locators retained below; local L357 product-error proof, L358 (3), audited L366 (2).
COMPARISON: The classical criterion requires every generalized Laguerre level at every real point; it supplies neither this regulated perturbation estimate nor an arithmetic sign margin. L357 already proves the generic product-error inequality; L366 now supplies the coupled gamma-scale derivative errors needed to specialize it.
GAP: Obtain the explicit nonlinear error using the actual normalized jets of F_0+εG and the L366 remainder, and distinguish comparison with that first-order transform from comparison with F_0 itself; no favorable margin is known.
REASON: Adequate local derivative estimates and the existing product inequality permit one bounded reproduction/specialization; a fresh contour argument or a real-zero premise is unnecessary. This assessment approves scope, not the proposed bound or sign.
LITERATURE_REASON: The target changed from a linear transform response audit to a nonlinear first-Laguerre comparison on a moving regulator/frequency domain, so the previous scalar assessment did not cover it.
SCOPE: Exactly L357's real family and L358's positive A, |ξ|≥40, 0<ε≤1/(1+ξ²), frequency jets j≤2; error divided by A², retaining the full first-Laguerre expression of F_0+εG, including its quadratic response. No division by F_0, assumed real-rootedness, uniform phase-return onset, higher level, or actual-theta sign theorem.

## Inspected sources and reuse

Queries actually used:

- `generalized Laguerre inequalities perturbation f prime squared f f double prime Csordas Vishnyakova`
- `Gaussian regulated zeta Laguerre inequality perturbation gamma normalized error`
- `"Laguerre inequalities" "perturbation" entire functions`
- `"Laguerre inequalities" "stability" derivatives`

The bounded screen found no full matching coupled-error theorem in the inspected material. This is not evidence of novelty. Orthogonal-polynomial quadrature and differential-equation stability hits address different objects and are not mathematical inputs.

Read the published eight-page Csordas–Vishnyakova primary PDF: the definition and first-level discussion on p. 1644, Remarks 1.3 and equation (1) on pp. 1644–1645, Theorem 2.3 on p. 1645 and the opening proof on p. 1646. For a nonzero real entire function, nonnegativity at all levels and real arguments implies Laguerre–Pólya membership without a prior growth hypothesis. The proof first excludes nonreal zeros via the modulus-square expansion and then uses an analytic logarithm in the upper half-plane. Neither that logarithm nor the all-level premise is available here. The first-level discussion explicitly warns that that level alone is insufficient. This criterion is a contrast, not a new imported sign theorem or a premise for transfer.

Reuse the unchanged scalar-source comparison in drafts/literature/2026-10-04-gaussian-regulator-response.md and its critical-audit assessment. Paris, arXiv:1503.07329v1 (2015-03-25), §2 (2.1)–(2.6), [primary text](https://arxiv.org/html/1503.07329v1), gives inversion/residue tools at fixed real exponent, not growing-complex-exponent uniformity. NIST [DLMF 25.4.1–5](https://dlmf.nist.gov/25.4), [5.11.9–13 and remainder restrictions](https://dlmf.nist.gov/5.11), and [5.15.8–9](https://dlmf.nist.gov/5.15) support completion and gamma estimates. Their version v1.2.8 (2026-09-15) and earlier inspected domains are inherited from those assessments, not independently refreshed. No reproof or extra browsing of these unchanged scalar inputs is needed. L366's completed audit, rather than Paris's theorem, supplies the family-specific uniformity.

The stability-preserver and level-set articles returned by the last queries remain unread leads; none is invoked or needed for the product-error specialization. No essential source blocker remains. Full Mathlib coverage of this nonlinear coupled statement is **not checked**; the scalar support recorded in L357–L366 does not establish it.

## Local duplication, failure and relevance check

Inspected L357's concluding product-error proof, L358's definitions and exact normalization (3), and L366's hypotheses, (1)–(2) and endpoint qualifications. The product subtraction is already established locally, so reproducing it should be explicitly labeled REPRODUCTION rather than a mathematical discovery. The difference needing work is its use with a first-order response and gamma normalization, retaining frequency-dependent jet sizes and uniform remainder constants. The intended derivative jets are F^(j)/A, not derivatives of F/A; if the latter notation is used, all envelope derivatives from L358 (3) must be retained.

The main gap remains global actual-theta mixed positivity. A useful intermediate result would quantify the sufficient signed margin for a coupled comparison without excluding zeros of F_0. This could inform the missing initial logarithmic segment motivated by L320, but neither the remaining low-index signs, heights above forty, endpoint arithmetic margin nor higher-level estimates are supplied by approximation alone.

The recorded stop in ATTEMPTS/2026-10-04-gaussian-common-first-sign-threshold.md remains valid: L365 gives escaping negative regulated signs with ε fixed and an onset that may depend on ε. This forbids reopening a common global sign threshold. It does not forbid this restricted-frequency error estimate. L357's absolute convergence is a duplicate, not an adequate gamma-scale replacement; L366 explicitly gives no vanishing remainder at ε≈ξ^(−2).

## One bounded later test

Keep the exact TARGET. Use L357, L358 and audited L366; L320 supplies only downstream motivation. State a pointwise bound with explicit dependence on all three normalized jets of F_0+εG and L366's three remainder constants. It must hold uniformly on the stated coupled domain, including zeros, retain the quadratic response, and specify which sign transfers in which direction. If further simplification needs an absolute critical-line growth estimate, use the already established L018/L320 coverage and state its hypotheses; do not introduce an uncovered arithmetic lower bound.

Continue only if the resulting error and sufficient signed margin are explicit enough to compare quantitatively in a stated shrinking-regulator regime. A conditional margin is useful and may leave independent gaps open. If this only rewrites the unknown sign without a controlled error, or relies on a favorable margin not proved, record that limitation and stop that proposed signing implementation. Do not claim error vanishes at the upper boundary or that an approximant sign transfers to F_0 without separately controlling the first response. No new bound, lemma or mathematical calculation is derived in this source-only step. The newly completed ready assessment requires the supervisor's separate approval next turn before research invocation.

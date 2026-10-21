# Frequency-coupled regulator response — source assessment

TARGET: Review whether L357's regulator derivative at ε=0 can be expressed through shifted completed-zeta values, with a justified gamma-normalized second-order remainder for F_ε, F_ε′ and F_ε″ on ε(1+ξ²)≤1.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three new queries screened Gaussian-smoothed zeta series with complex exponent, Euler-Jacobi uniform remainders, and functional-equation/gamma remainder tools; read the primary statements below and reused the adequate scalar Poisson and fixed-regulator Mellin assessments.
SOURCE_EVIDENCE: Paris, arXiv:1503.07329v1 (2015-03-25), §§1–2, (1.1), (2.1)–(2.6), and Theorem 1 in §3.2, https://arxiv.org/html/1503.07329v1; NIST DLMF v1.2.8 (2026-09-15), 25.4.1–5, 25.5.13–14, 5.11.9–13, https://dlmf.nist.gov/25.4 and https://dlmf.nist.gov/5.11.
COMPARISON: The sources cover scalar Mellin inversion, finite contour displacement, theta completion, reflection and gamma estimates. They do not cover L357's subtracted/reflected parameter derivative with two frequency derivatives and a remainder uniform for an unbounded complex exponent; importing a fixed-exponent expansion does not establish that conclusion.
GAP: Justify the ε=0 parameter derivative after zero-mode cancellation, identify its completed-zeta shifts, and bound the remainder divided by L358's positive A(ξ) in the coupled range, without dividing by F_0 or assuming nonvanishing.
REASON: The named tools and readable contour argument supply adequate inputs for a bounded specialization attempt; the growing-exponent estimate itself must be proved or rejected, not imported. This review establishes no derivative formula, remainder or actual-theta sign.
LITERATURE_REASON: The saved target changes the regulator/frequency quantifiers and requires a uniform complex-exponent remainder outside the previous assessment's fixed-positive-regulator scope; the runner requires this source-only turn.
SCOPE: L357's exact family, real |ξ|≥40, 0<ε≤1/(1+ξ²), j=0,1,2, A(ξ) from L358; includes kernel-side justification at ε=0 and one finite Mellin contour displacement. No global approximant sign, phase-return rate, division by actual zeta, or higher Laguerre assertion is covered.
COVERED_TARGET: Derive L357's first regulator response at ε=0 through shifted completed-zeta values and test whether the subtracted Mellin contour gives |∂_ξ^j(F_ε−F_0−εG)|/A(ξ)≤C_j ε²(1+|ξ|)^(9/2)log^(j+2)(2+|ξ|) for j=0,1,2 on |ξ|≥40 and ε(1+ξ²)≤1, where G=∂_εF_ε|_(ε=0).
COVERED_TARGET: Critically audit L366's moving-pole cancellation, shifted-completion response and uniform j=0,1,2 remainder on |ξ|≥40, ε(1+ξ²)≤1, checking the negative-line zeta bounds and contour differentiation against L357–L358 and L320.

## Search and source comparison

Read shared GOAL.md/PROMPT.md, local GOAL.md/PROGRESS.md, the whole PROOF.md overview and DAG, and inspected existing changes before selecting work. All existing lemma/script edits were preserved. Local searches of drafts, ATTEMPTS and L357–L365 found the saved scaffold but no prior completed coverage of the coupled response. The scalar Poisson and gamma/beta assessments from 2026-10-03 remain adequate and are reused; their supporting theorems need no reproof.

Queries actually used:

- `Gaussian smoothed zeta Dirichlet series complex exponent uniform Mellin remainder exp n squared`
- `Paris Euler Jacobi series complex w small a uniform remainder`
- `site.dlmf.nist.gov zeta functional equation gamma asymptotic remainder`

The bounded search found no full matching statement in the sources inspected. Unrelated search results supplied no evidence. This is not a novelty claim.

**Closest expansion.** Read R. B. Paris, *The asymptotic expansion of a generalisation of the Euler-Jacobi series*, v1, [§§1–2 and §3.2](https://arxiv.org/html/1503.07329v1), corresponding to printed pp. 1–5 and 8. Equation (1.1) defines the smoothed series. Equations (2.1)–(2.2) give inversion; (2.5)–(2.6) give a finite-residue expansion and integral remainder. The paper assumes real positive w throughout, with fixed parameters as damping tends to zero. Its remainder constant is independent of damping in the stated sector, not asserted uniform in Im w. Theorem 1 requires even positive integer w and p. Thus its theorem cannot be substituted at w=1/2+iξ. The readable argument is a useful template; uniform complex-exponent control remains a separate specialization obligation.

**Completion and reflection.** Read NIST DLMF v1.2.8, [25.4.1–5](https://dlmf.nist.gov/25.4), including the completed xi definition and differentiated reflection identity, and [25.5.13–14](https://dlmf.nist.gov/25.5#E13), the theta integral representation with its rational term. These identify standard possible inputs for shifted completion, but do not justify integrating the separate ε=0 generators or deleting subtraction terms. They assert no sign for the response. The relevant formulas and domains were inspected in HTML; cited books were not read afresh.

**Gamma estimates.** Read [DLMF 5.11.9–13](https://dlmf.nist.gov/5.11#E9), including bounded-real-part uniformity of the vertical-line modulus asymptotic, the explicit sector remainder with its K=1 exception, and fixed-shift ratio conditions. These support tracking gamma decay in a finite contour calculation. A shift with a growing imaginary part is not a fixed-shift application of the ratio formula. Gamma estimates alone do not bound the zeta remainder integral or its frequency derivatives. Existing frequency-derivative tools in the 2026-10-03 spectral assessment remain available.

The primary texts were accessible; no essential access blocker remains for the bounded test. Paris's cited monograph and DLMF's referenced books are supporting unread leads, not invoked sources for a uniform remainder. We do not retry previously failed PDF-image or TeX retrievals.

## Route reassessment and discriminating test

The main gap is global actual-theta mixed positivity, with the low logarithmic and sublogarithmic Laguerre levels not supplied by L296. A frequency-coupled response might quantify an arithmetic approximation at the gamma envelope scale. A later positive arithmetic margin and higher-level estimates would still be needed; neither follows merely from better approximation.

Compare three mechanisms:

1. **Fixed-regulator phase return:** L365 already refutes the common global-first-sign threshold. Repeating its return calculation or auditing it again would not address the limiting actual-theta sign. Keep this mechanism parked, with its obstruction in ATTEMPTS.
2. **Kernel Taylor estimate alone:** L357 provides an absolute O(ε) estimate. A higher absolute Taylor order could justify parameter differentiation, but would not by itself supply a gamma-normalized error at large frequency. Use it only as an interchange check, rather than claim it answers the saved gap.
3. **Finite subtracted Mellin displacement:** select this different mechanism. Retain the moving zeta pole, all subtraction derivatives and the real reflection, and track the complex exponent explicitly. Compare the resulting integral estimate with the proposed polynomial threshold below. It uses actual arithmetic input and does not ask for any phase visit.

The COVERED_TARGET gives the exact single next attempt. Its inequality is a **proposed test**, not a derived result. G is merely notation for the derivative to be justified; no formula is asserted here. The finite contour should retain any second-order residue needed to estimate the first-order remainder. Bound differentiated integrals before using them; track neighborhoods where gamma or zeta arguments change their height scale. An estimate whose constant depends arbitrarily on ξ does not pass.

Continue this mechanism if the formula and uniform threshold are established with controlled constants, recording exactly how much shrinking of ε makes the normalized error useful. If the bounded contour estimate exceeds the proposed threshold, preserve that informative limitation and stop this implementation without concluding that the true remainder violates it. The constraint ε(1+ξ²)≤1 alone is not a promise of a vanishing normalized remainder at its upper boundary. Even a successful estimate would require a separately proved sign margin exceeding the error; zeros of F_0 cannot be bypassed by division.

No mathematical calculation was performed in this literature turn. The completed assessment approves a later specialization of covered tools; it does not certify originality or renew the exhausted global-sign route's budget.

## Mathlib

Full regulator-response and coupled remainder coverage: **not checked**. Previously checked scalar Poisson supporting references in L357 are retained. No full matching theorem or absence from inspected library sources is claimed; optional library lookup is not a continuation gate.

## Same-target audit coverage

The additional covered action is a critical audit of the same response and coupled remainder, with unchanged hypotheses, derivative orders, normalization and source inputs. It reuses the theorem-level comparison above; no new intermediate theorem or source need is introduced. L366 now records the specialization to inspect, rather than being accepted as an imported theorem. This preapproval concerns coverage for a later audit, not validation of its mathematics.

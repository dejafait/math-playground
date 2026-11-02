# Fixed L233 Stein-monotonicity diagnostic

TARGET: Test whether L233's fixed Gaussian-mixture countermodel has a nonincreasing Stein kernel on (0,infinity), retaining its certified negative first Fourier sign.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed monotone-Stein transfer comparison in 2026-10-31-theta-stein-monotonicity-transfer-review.md: exact/stronger Stein/Fourier/Laguerre searches found no matching implication or verified model. L233 was read completely; the target adds only its previously unchecked Stein hypothesis. No novelty is claimed.
SOURCE_EVIDENCE: L233's canonical proof gives the fixed Gaussian mixture, transform and negative first sign; Adrien Saumard, Weighted Poincare inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one, arXiv:1804.03926v3, https://arxiv.org/pdf/1804.03926v3, Section 2 (5)-(6), printed pp. 3-4, supplies the precise Stein ratio, test class and endpoint qualification; these complete passages were directly inspected on 2026-10-31.
COMPARISON: The known model already has strict positivity, evenness, smoothness and faster-than-every-exponential decay of all derivatives. Its negative first Fourier sign alone does not refute a theorem with an additional monotone-Stein premise. Neither L049/L055 nor the inspected probability identities answer that remaining hypothesis.
GAP: Determine global nonincrease of this one ratio or give a rigorous positive derivative somewhere; this is a model diagnostic, not a theta calculation or proof of generic sign transfer.
REASON: A fixed existing countermodel discriminates the proposed criterion without inventing a new kernel or reproducing an already certified Fourier calculation. The separate literature approval on 2026-10-31 repaired the direct-source citation and retained this scope for the next mathematical turn.
SCOPE: Only the fixed mixture below and its Stein monotonicity; no parameter search, changed density, actual-theta derivative, transfer theorem or higher-sign claim.

The essential local input is L233. For the main-gap interpretation only,
L019 identifies actual theta. L055/L603 are comparisons, not premises.
No cross-notebook input is proposed.

Use exactly

\[
g_0(u)=\pi^{-1/2}e^{-u^2},\qquad
k(u)=g_0(u)+\tfrac14[g_0(u-2)+g_0(u+2)],\qquad
\tau(u)=\frac{\int_u^\infty v k(v)\,dv}{k(u)}.
\]

Normalization to mass one does not change this ratio. L233's existing
Fourier conclusion, under `F(x)=integral_R k(u)exp(ixu)du`, is

\[
\left.(F'^2-FF'')\right|_{x=\pi/2}=-\tfrac78 e^{-\pi^2/8}<0.
\]

Import that conclusion; do not recalculate it as a new discovery. The
only proposed calculation is the missing hypothesis: is `tau` globally
nonincreasing for `u>0`? Direct Gaussian integration/differentiation is
justified only to settle this previously unchecked premise; Saumard's
identity need not be reproved. Supply rigorous analytic bounds or a
validated interval certificate for any sign used. Finite numerical samples
do not establish nonincrease. A strict positive derivative at one point,
or a rigorously controlled one-sided expansion implying it, suffices to
discard this fixed model as a counterexample.

If global nonincrease is proved, the already certified Fourier failure
refutes the generic sufficient criterion with every density hypothesis
retained. If monotonicity fails, the criterion remains unresolved and this
model is parked; failure is not an RH result or evidence for generic
sufficiency. If no rigorous decision is reached in one bounded attempt,
save the exact obstruction and reassess rather than silently broadening
the model. Actual-theta applicability, sign transfer and all higher Xi
signs remain unresolved.

This is routine known-model hypothesis analysis, not a creative central-gap
mechanism. Expected research classification REPRODUCTION is a diagnostic
application of a known construction, not a claim that this derivative test
was located in the literature. Mathlib coverage is not checked.

## Separate source approval and direct-URL recovery — 31 October 2026

Read the complete L233 proof and reused the completed transfer assessment
(including its exact/stronger searches and source comparisons). Directly
retrieved [Saumard v3](https://arxiv.org/pdf/1804.03926v3), Section 2,
printed pp. 3-4, equations (5)-(6), including all immediately surrounding
hypotheses. The arXiv version stamp is 23 November 2018; the title page
displays 26 November 2018. No different edition is being imported.

The source assumes a density on the real line with connected support
and a finite absolute first moment; writing its mean as mu, (6) gives
`tau(x)=integral_x^infinity (y-mu)p(y)dy/p(x)` on the support interior.
Its identity (5) applies to differentiable test functions for which both
terms are integrable and the endpoint expression `[tau p phi]_a^b`
vanishes. Existence/uniqueness is up to density-null sets; (6) selects the
pointwise version to be tested. No monotonicity or Fourier-sign theorem
is imported from these equations, and the diagnostic needs no application
of (5) to an unbounded test function.

L233's positive even finite Gaussian mixture has support R and finite
absolute moments. Thus its normalized density satisfies the source
hypotheses, with zero mean by evenness. The common normalization cancels
in (6), giving exactly the already specified ratio for k. This is only
the applicability check, not a derivation of its derivative or sign.
The existing negative Fourier sign is imported from L233 unchanged.
No reproof of the Stein identity, Gaussian transform or variance theorem
is needed. Full-result Mathlib coverage remains not checked.

The earlier citation-only determinant-transfer stop is a different
obstruction: it lacks frequency localization and a signed-remainder
bound. This diagnostic instead tests one additional hypothesis of one
existing countermodel, and repeats neither that failed transfer nor
L603's separate-family sign argument. The reused search does not establish
novelty. No new search was needed for an unchanged exact target.

Approved for the bounded calculation only. A proof of global nonincrease
would refute the proposed generic sufficient criterion; a rigorous strict
positive derivative at any positive point would park this fixed model
only. An inconclusive bounded attempt must preserve its obstruction.
The generic transfer, actual-theta applicability and higher Xi signs
remain unresolved. No mathematical calculation was performed here.
This is a process/citation repair, outcome STALLED, with no claimed
mathematical advance or exploration-budget reset.

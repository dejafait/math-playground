# Gaussian-regulated modular theta approximation — source assessment

TARGET: Test whether subtracting the exact Poisson zero mode from Gaussian-regulated modular theta sums yields even approximants converging to k in L¹(R,(1+u²)du), repairing L235's divergent-mass obstruction.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Eleven target, terminology and stronger-result queries checked regulated theta kernels, zero-mode subtraction, weighted L¹ approximation and differentiated Poisson remainders; the primary statements inspected below give exact scalar and polynomial-weighted transformations, not the proposed weighted whole-line limit.
SOURCE_EVIDENCE: NIST DLMF v1.2.8, 20.2.3, 20.7.32 and 20.13.1–4, https://dlmf.nist.gov/20.7#E32; Sutherland, MIT 18.785 Lecture 17 (4 November 2019), Theorem 17.8 and Lemmas 17.6–17.10, pp. 2–3, https://math.mit.edu/classes/18.785/2019fa/LectureNotes17.pdf; Paris, arXiv:2101.01589v1 (4 January 2021), Theorem 1, (3.10) and Remark 1, pp. 5–6, https://arxiv.org/pdf/2101.01589v1. Statements and the scalar Poisson proof were read; L016's adequate scalar-tail coverage is reused.
COMPARISON: The sources cover the exact Gaussian zero mode and polynomial-weighted dual corrections at each positive theta parameter. They do not supply uniform weighted integrability after the shifted parameter e^(2u)+ε, multiplication by e^(u/2), application of P and reflection. L235's finite averages and L234/L356's reflected boundary blocks use different approximants and do not decide this limit.
GAP: Prove or refute weighted whole-line convergence of the specified even approximants, retaining the actual differential weight and the regulator's escaping tails; spectral positivity of any approximant would remain a separate missing input.
REASON: The changed target now has adequate accessible source coverage for a later mathematical invocation. Import the named scalar and weighted identities; specialize only the uniform whole-line error and regulator-tail estimates missing from their statements. Reproving Poisson summation or inferring spectral positivity from convergence would not address that difference. This review derives no approximation result and makes no originality claim.
SCOPE: Exactly the a_ε, z_ε, h_ε and k_ε defined below, with ε>0 tending to zero, the actual operator P=2D_u²−1/2, even reflection, and convergence in L¹(R,(1+u²)du); includes checking differentiated cancellation and escaping tails, but no spectral-sign or higher-level conclusion.
LITERATURE_REASON: Changed approximation hypothesis: introduce Gaussian index regulation and an explicit Poisson zero-mode subtraction; prior source comparisons did not cover their weighted whole-line convergence.

## Proposed objects and source boundary

For ε>0, u∈R and P=2D_u²−1/2, propose

\[
 a_\varepsilon(u)=e^{u/2}\sum_{n\ge1}
                    e^{-\pi n^2(e^{2u}+\varepsilon)},\qquad
 z_\varepsilon(u)=\tfrac12e^{u/2}(e^{2u}+\varepsilon)^{-1/2},
\]

\[
 h_\varepsilon(u)=P(a_\varepsilon-z_\varepsilon)(u),\qquad
 k_\varepsilon(u)=\tfrac12[h_\varepsilon(u)+h_\varepsilon(-u)].
\]

These definitions specify a future test, not a proved approximation,
sign, cancellation or uniform bound. The intended z_ε is the scalar
Poisson zero-mode term before application of P. The later test must
check its normalization, the constant-term treatment and complete
derivatives of all factors. The identities cited below are covered
inputs; their application does not establish a uniform integrable
envelope in u. In particular, a subtraction at the undifferentiated
level must not be replaced by omission of individual derivative
terms. The proposed objects and exact TARGET are preserved.

## Search and reading record — 2026-10-03

Read the shared instructions, local goal and checkpoint, complete
PROOF.md overview and DAG before the review. Inspected the existing
working-tree changes and preserved the unfinished parity calculation,
source notes and lemma corrections. The relevant local comparison
statements were L016, L019, L233 and L235, the preceding parity
assessment, and the modular-average and complete-parity failed tests.
The local searches found no prior result for these regulated objects.

Queries actually used:

- `theta Gaussian regularization zero mode subtraction weighted L1 convergence Riemann Xi kernel`
- `theta kernel regularized heat parameter Poisson zero mode subtraction logarithmic variable convergence`
- `Jacobi theta Gaussian sum derivatives small parameter asymptotic Poisson summation NIST`
- `"theta" "zero mode" "dominated convergence"`
- `"theta" "Gaussian regularization" subtraction`
- `"theta" "weighted L1" convergence`
- `"theta" "zero mode subtraction"`
- `"Riemann" "theta" "regularized" "approximation" kernel`
- `"theta" "renormalized" "heat trace" "Poisson"`
- `"theta" "derivatives" "exponentially small" "Poisson"`
- `"Riemann xi" "theta" "L1" approximation`

Several literal queries returned unrelated regularization results;
these supplied no evidence. Broader terminology led to the scalar
theta sources and Paris's weighted-Gaussian theorem. No matching
whole-line statement was found in this bounded search. That is a
coverage finding, not evidence of originality or a failed limit.

## Inspected primary statements and applicability

**Scalar Gaussian transformation.** Andrew V. Sutherland,
*The functional equation*, MIT 18.785 Lecture 17, dated 4 November
2019, [pp. 2–3](https://math.mit.edu/classes/18.785/2019fa/LectureNotes17.pdf#page=2).
Read Lemmas 17.6–17.7 (scaling and differentiation), Theorem 17.8
and its periodization proof, Lemma 17.9 (Gaussian Fourier transform),
and Lemma 17.10 with proof. Theorem 17.8 assumes a Schwartz function
and uses exp(−2πixy); Lemma 17.10 gives
Θ(ia)=a^(−1/2)Θ(i/a) for a>0. These fix the scalar zero-mode
normalization. Their summation variable is distinct from the later
logarithmic variable u; the theorem supplies no uniform u-integral
after differentiating the regulated family. L016 already records the
same named theorem and adequate large-parameter derivative tails,
so its proof and estimates should be reused.

**Theta definition, inversion and heat terminology.** Read NIST DLMF
version 1.2.8, released 15 September 2026:
[20.2.3](https://dlmf.nist.gov/20.2#E3), including the constant term
in θ₃; [20.7.32](https://dlmf.nist.gov/20.7#E32), including
τ′=−1/τ and the principal square-root convention; and
[20.13.1–4](https://dlmf.nist.gov/20.13#E1), the heat equation and
periodized Gaussian identity. These are exact parameter identities,
not weighted whole-line convergence theorems. The heat equation
acts in the theta argument z with time related to Im τ. Thus its
usual spatial approximate-identity interpretation is not directly a
theorem about the present u variable and P. The shifted positive
parameter falls within the scalar formulas, but their differentiated
pullback and tail domination remain the specialization to test.

**Polynomial-weighted Gaussian remainder.** R. B. Paris,
*Asymptotics of a Mathieu-Gaussian series*,
[arXiv:2101.01589v1](https://arxiv.org/pdf/2101.01589v1#page=5),
4 January 2021. Read the μ=0 derivation following (3.8), Theorem 1,
(3.10) and Remark 1 on printed pp. 5–6. The theorem treats
S_(μ,γ)(a;λ)=Σ_(n≥1)n^γ exp(−λn²/a²)/(n²+a²)^μ, with
μ≥0, λ>0, γ=2p and p a nonnegative integer, in |arg a|<π/4.
For μ=0, (3.10) gives an exact dual Gaussian sum with finite
polynomial corrections; Remark 1 identifies p=0 with Poisson–Jacobi
and relates the other even weights to parameter differentiation.
This is stronger scalar-weight coverage than an unweighted
asymptotic alone. It does not assert weighted convergence in u or
positivity after P. In particular, small-parameter exponential
remainders must not be integrated over all u without a uniform bound.

**Reading limits.** The MIT PDF and Paris theorem were accessible as
text; a Paris PDF screenshot request failed, but its statement and
μ=0 formulas were readable in the text extraction. No inaccessible
source is essential to this specialization. Search leads on Gaussian
shift approximation, truncated-theta computation and torus heat
traces were not read at theorem level and are not imported. The
books cited by DLMF were not separately inspected. Earlier
polynomial-Gaussian coverage in the parity assessment is reused;
its higher-dimensional theorem does not need another reproof here.

## Difference still requiring a mathematical test

The known scalar identities cover each strictly positive parameter
and the needed even polynomial weights. The remaining claim concerns
the complete differentiated, subtracted family on an unbounded
logarithmic domain. Uniform convergence on fixed compact intervals
and a formal theta transformation would miss the exact obstruction
exhibited in L235. The later test must retain the transition region
e^(2u) comparable to ε and both distant tails, and give either a
uniform weighted domination/tail estimate or an explicit residual
mass obstruction. No bound, limit or sign is computed here.

Only that difference justifies a specialization. A successful result
would be a local application of established theta tools, appropriately
reported as REPRODUCTION, not an asserted mathematical discovery.
Neither source gives the sign of F′²−FF″ for this family; L233's
generic counterexample remains relevant. Further positivity and
higher Laguerre estimates would need their own concrete mechanism.

## Relevance and discriminating test

The unresolved target remains global actual-theta Laguerre positivity.
L356 proves a negative block after complete parity grouping and exact
resummation; it leaves the total spectrum unsigned. L235 supplies a
distinct approximation obstruction: compact convergence alone does
not control the whole-line Fourier integral. A regulator and explicit
subtraction offer a concrete way to test that particular missing
approximation estimate while retaining smooth modular cancellation.

The desired threshold is
∫_R(1+u²)|k_ε(u)−k(u)|du→0 as ε↓0. Its intended downstream use is
control of the Fourier transform and its first two derivatives on the
real axis, the quantities entering L233. Even success would still
require a sign certificate for the approximants with valid passage
to the limit; no positivity transfer, global first sign or higher
Laguerre level is supplied by convergence alone.

Continue only with a proof of that weighted convergence and a
specified tail estimate. An escaping residual mass or a nonvanishing
weighted error would stop this implementation. An identity or compact
convergence without tail control would be inconclusive, rather than
an advance. This target received no calculation in the parity step
or this literature turn. The unchanged TARGET is now ready under
SPECIALIZE; the next ordinary invocation should perform the test
using this assessment. No new mathematical input enters the main
proof or DAG, and established sign and exclusion ranges are unchanged.
The sole current decision and Next action remain in PROGRESS.md.

## Mathlib

Full regulated-approximation statement: **not checked**. No new
library lookup was needed for this source review. L016's saved check
records the supporting scalar theorem
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq)
as present in the documentation it checked; that coverage is reused
without a fresh version check. It is not a match for the weighted
whole-line limit or a Fourier-sign theorem. Other target-specific
Mathlib support is **not checked**, rather than asserted absent.

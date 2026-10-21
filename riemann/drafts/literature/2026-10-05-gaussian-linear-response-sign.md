# Signed linear response — actual-frequency mean test coverage

TARGET: Determine whether L367's signed linear coefficient is negative at arbitrarily large real frequencies.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact/terminology, mixed-zeta-moment and truncated-series searches listed below; narrow local response/transfer assessments and recent histories contain no decision on this coefficient.
SOURCE_EVIDENCE: Arias de Reyna, arXiv:2406.16667v1 (2024-06-24), Theorem 6 and proof, pp. 5–6, supporting Lemmas 2/4/5; Pliego, arXiv:2211.11450v1 (2022-11-21), (1.4)–(1.5), Theorem 1.1 and Theorems 1.2–1.4, pp. 2–4, inspected for mismatch; reuse the saved DLMF scalar and Csordas–Vishnyakova comparisons.
COMPARISON: No inspected theorem decides B's sign. Uniform truncated-zeta coverage includes critical-line complex neighborhoods; right-line series, gamma jets and reflection are already covered. Their specialization to the signed mixed derivative mean remains unproved.
GAP: Compute the normalized dyadic mean of actual B with an error smaller than its leading term, retaining all real-projection and envelope terms; a strictly negative mean would decide recurrent negativity, while the sources alone give no sign.
REASON: Essential scalar coverage is accessible for one bounded mean-value specialization; no ready-made mixed-sign theorem was established, and no novelty is inferred.
LITERATURE_REASON: The target changed from the response-only quadratic margin to a critical-line/right-line coefficient; the previous assessment lacked a uniform critical-line finite-series input for derivatives and averages.
SCOPE: Exactly actual F_0 and G of L366, positive A of L358 and B of L367 (1)–(3), at unbounded real frequencies; test its normalized mean over [H,2H] using fixed-cutoff critical-line approximation, right-line absolute convergence, reflection and gamma derivatives. No arbitrary phase replacement, RH premise or division by F_0 or G.

## Search and inspected evidence

Queries actually submitted included:

- `zeta mixed moment different vertical lines derivatives twisted first moment zeta half it sigma`
- `mixed Laguerre inequality bilinear entire functions Riemann xi derivatives`
- `integral zeta(sigma1+it) zeta(sigma2-it) mean value sigma1 sigma2`
- `"zeta" "Theorem 4.11" "x"` and `"Titchmarsh" "4.11" "sigma"`
- `"zeta" "mixed moment" "different" "lines"` and `"zeta" "sigma_1" "sigma_2" "mean"`
- `"bilinear" "Laguerre" "xi"`, `"polarized Laguerre" inequality`, and `"2f" "Laguerre" "mixed" inequality`
- `"twisted first moment" "zeta" derivatives`, `"zeta" "critical line" "5/2" "moment"`, and `"zeta" "mixed second moment" "sigma"`

Search snippets were discovery aids, not theorem evidence. No full
matching mixed-sign theorem was established in inspected material.
Joint logarithmic-derivative moments, derivative-at-zero moments,
asymptotic derivative-Laguerre, level-set and simultaneous-extreme-value
articles remain unused leads. Titles and abstracts do not approve inputs.

J. Arias de Reyna, *On the approximation of the zeta function by Dirichlet
polynomials*, [arXiv:2406.16667v1, Theorem 6, pp. 5–6](https://arxiv.org/pdf/2406.16667v1#page=5),
states, for fixed real x>0, s=σ+it, σ≥0 and 0<t≤x,

\[
 \left|\zeta(s)-\sum_{n\le x}n^{-s}
                 -\frac{x^{1-s}}{s-1}\right|
       \le\frac{29}{14}x^{-\sigma}.
\]

Read the complete proof and supporting Lemmas 2/4/5, also in the
[primary HTML](https://arxiv.org/html/2406.16667v1). For σ>0 it uses
weighted tail summation with only the zero dual mode and a uniform
t/x≤1 bound; σ=0 follows by continuity. There is no zero hypothesis.
For later use, x=3H fixed over [H,2H] admits small complex disks about
1/2+it. Cauchy's formula on the analytic difference must still provide
the derivative bounds, with pole-correction derivatives retained. The
source states neither a differentiated remainder nor the mixed mean;
its scalar approximation needs no reproof.

J. Pliego, *Twisted mixed moments of the Riemann zeta function*,
[arXiv:2211.11450v1, (1.4)–(1.5), Theorem 1.1, p. 2](https://arxiv.org/pdf/2211.11450v1#page=2),
treats a truncated critical-line factor and two critical-line factors
at integer multiples of height. Theorem 1.1 imposes integer relations,
a truncation range and, in the divisibility case, Conjecture 1.
The unconditional alternatives in Theorems 1.2–1.4, pp. 3–4, still
concern different products. They do not cover B. These statements and
definitions were inspected; their proofs and references are not imported.

Titchmarsh's book was retrieved, but text searches did not isolate 4.11;
it is not independently inspected coverage here. The standalone scalar
theorem removes that source need. The recorded Hardy–Littlewood
approximate functional equation is an alternative, unused in this test.

## Reuse, duplicates and failures

Reuse drafts/literature/2026-10-05-gaussian-response-quadratic-sign.md
for DLMF 25.2.1/11 (Re s>1), 5.11.1–2/9 with sector/remainder
restrictions, and 5.15.8–9 for controlled gamma derivatives. Its checked
version is 1.2.8 (2026-09-15); no refresh is needed. The reflected line
Re s=5/2 is inside absolute convergence; the critical line is outside it.
Completion/reflection coverage in
drafts/literature/2026-10-04-gaussian-regulator-response.md and audited
L366 (1) is reused unchanged.

Reuse drafts/literature/2026-10-05-gaussian-coupled-laguerre-transfer.md
for Csordas–Vishnyakova (2013), Theorem 2.3 and Remarks 1.3,
[pp. 1644–1646](https://d-nb.info/1372516522/34).
The all-level, all-real-point criterion does not sign this polarized
expression. Its essential proof comparison was already inspected.

Inspected L366's response (1), L358 (3), L367 (1)–(15) and L368's
carrier/scalar proof through (7). The recent response/transfer
assessments and 2026-10-05 histories leave B unsigned. The quadratic
margin is already proved and must not be counted again. The failure in
ATTEMPTS/2026-10-04-gaussian-common-first-sign-threshold.md remains
valid: L365's fixed-regulator negatives stop the common global
threshold, but do not decide the derivative at regulator zero.
Arbitrary-phase templates likewise do not decide this coefficient.
This actual-frequency mean test requires no shrinking-window return.

Full matching Mathlib coverage is **not checked**. The named Cauchy
integral formula/derivative estimate, finite exponential integration,
integration by parts and absolute-series operations are standard
supporting tools, not matching sign theorems.

## Relevance and one bounded later test

The downstream use is to decide whether L367's remaining linear term
can be treated as eventually nonnegative in a perturbative comparison.
Negative values at arbitrarily large actual frequencies would stop that
particular sufficient signing step, without signing the total expression.
No applicable eventual-nonnegativity theorem was established. Test
H^(-1)∫_[H,2H] B(t)dt: seek a justified leading term with o(1) error
and a strict negative limit or a fixed negative upper bound. No value
or sign of that proposed leading term is asserted in this review.

The later attempt must retain full real projections and gamma-envelope
derivatives, including both conjugate and sum-phase products until an
exact functional-equation identity or controlled estimate handles them.
Use fixed-cutoff approximation and Cauchy estimates for critical-line
jets through order two, and right-line series with derivative majorants.
Retain all equal-frequency collisions, n=1 terms, off-diagonal
integrals, cutoff tails, pole corrections and moving scalar weights.
An undifferentiated mean cannot simply be differentiated. This mixed
specialization is the difference needing proof; it is not performed here.

Continue if the complete mean has a negative margin dominating every
error. Negativity on unbounded dyadic intervals would give the requested
recurrence by continuity. Abandon this mean certificate if its leading
term is nonnegative or its errors do not separate the sign; that alone
does not settle the original question. Unsigned jet bounds or arbitrary
phase examples do not meet this test.

The essential local context is L366's exact F_0 and reflected G,
L367's coefficient definition and regulator-fixed derivative convention,
and the audited L368 quadratic margin. No division by F_0 or G is
permitted at their zeros. The total actual-theta sign, relative
remainder control, higher levels, endpoint arithmetic margin and heights
above forty remain unresolved. L365's stopped common-global-regulator
certificate remains intact; this changed target does not reopen it.

This newly completed SPECIALIZE assessment requires the supervisor's
separate approval next invocation before research. Its exact TARGET is
preserved. No lemma, mathematical script or sign result was written.

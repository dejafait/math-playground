# Signed-Xi bridge — completed bounded source comparison

TARGET: Assess source coverage for an exact signed representation of D_1(Xi;t) by L548's fixed-data cubic-theta reflection, identifying the required transform or an obstruction before proposing a bridge mechanism.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact cubic-theta/Xi/Laguerre/reflection searches and notebook-local bridge/failure searches found no matching signed identity in the inspected sources. Primary statements, proof cases, queries and local overlap are recorded below; this bounded search establishes neither novelty nor impossibility.
SOURCE_EVIDENCE: OpenAI pinned TeX https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex lines 98–110, 1534–1756 and 2139–2260; Dunn–Radziwill arXiv:2109.07463v3 Section 5.3–5.4, Lemma 5.2, Corollary 5.1, Lemma 5.3 and Proposition 5.1; Csordas arXiv:1309.0055v2 Theorems 4.5–4.6 and Open Problem 4.7, printed pp. 11–12; Sra riem-xi v2 (29 October 2026), introduction and Theorem 1.3, printed pp. 1–3. URLs and reading limits appear below.
COMPARISON: L548 transforms a linear smoothed cubic Gauss-coefficient series T(s,Psi); L233's D_1 identity is the Fourier transform of a quadratic Jacobi-theta associated kernel. The reflection does not identify those objects or supply a nonnegative signed dual expression. The finite-height theorem overlaps L466. No inspected theorem supplies the proposed bridge.
GAP: A specific signed identification, including kernel, normalization, allowed real t, arithmetic choices and justified interchanges, remains missing. Complex phases, absolute-energy estimates and half-plane continuation do not supply it. No impossibility of a different transform or of actual-Xi positivity is proved.
REASON: Complete the essential source comparison before bridge mathematics. Park direct citation of L548 as a D_1 sign certificate; do not authorize an unspecified transform merely because the bounded search found none.
SCOPE: Completed source search only. EXPLORE does not approve a mathematical continuation here: no cubic-to-Jacobi identity, varying-S limit or positivity-preserving operator has been specified. The checkpoint routes to a separate actual-theta source target.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; no prior assessment compared an exact signed actual-Xi transform with the fixed-data cubic reflection.

## Required sign and local overlap

The main gap remains all-degree mixed positivity. This review considered
only D_1(Xi;t)=Xi'(t)^2−Xi(t)Xi''(t)>=0 for every real t, with L018's
actual Xi convention. L233 already proves, for the actual even theta
kernel k with Fourier transform F=2Xi,

\[
 A(v)=\int_{\mathbb R}s^2k(s+v)k(s-v)\,ds,
 \qquad \widehat A(2t)=D_1(\Xi;t).
\]

Its Fourier decomposition has summands F'(t)^2/2 and −(F(t)^2)''/8.
Controlling that signed sum could give the first sign, with higher
signs still unresolved. These are existing identities, not derivations
in this literature turn. L233's comparison kernel is not actual theta.

Read L548's hypotheses/conclusion and the convergence, cusp-derivative,
Mellin and contour-shift proof ranges (440–604, 642–710); L233 in full;
and L466's source/application record. Reused the baseline overlap,
external-input register and finite-factor source assessments. The
[theta failure record](../../ATTEMPTS/2026-09-20-theta-logarithm-relevance-audit.md)
and [associated-kernel assessment](2026-09-27-first-associated-theta-lattice.md)
already distinguish ordinary Gram signs from the required signed signs.
Those stops do not ban a mechanism using additional actual arithmetic.

## Primary comparison and reading limits

**Cubic reflection.** OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, 30 September 2026, commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
Proposition 5.1 (`prop:completed-reflection`), `eq:reflection`,
`eq:reflection-row-phase`, `eq:reflection-direct-mellin`,
`eq:reflection-reflected-mellin`. Read the complete statement and its
analytic proof cases. Fixed S,E,L and finite arithmetic data,
zero-extended characters and rapid two-endpoint decay of every
logarithmic derivative of V are essential. Its Mellin multiplier and
−i/81 phase agree with L548; the dual coefficients remain complex.
Theorem 1.1 explicitly leaves RH open. **Inference:** this reflection
alone is not an imported signed-Xi identity. No gamma-factor or
coefficient-matching no-go theorem is established here.

**Underlying theta transform.** Alexander Dunn and Maksym Radziwill,
*Bias in cubic Gauss sums: Patterson's conjecture*, Annals of Mathematics
200 (2024), 967–1057,
[arXiv:2109.07463v3, 14 May 2024](https://arxiv.org/html/2109.07463v3).
Inspected (5.19)–(5.26), both angular-derivative cases of Corollary 5.1,
(5.43)–(5.48), and Lemma 5.3's negative-index Mellin proof.
The twist is periodic modulo primary r and its finite Fourier
transform must be supported on units. Proposition 5.1 treats completed
cubic-coefficient series: zero angular index has the specified possible
simple pole at 5/6; nonzero indices are entire. Neither case identifies
a quadratic Jacobi-theta kernel. Do not apply that restricted transform
to nonunit frequencies: L548 uses its separate full-frequency
construction. Upstream theta theory and full manuscripts were not
independently audited here.

**Actual-Xi signs.** George Csordas, *Fourier transforms of positive
definite kernels and the Riemann xi-function*,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
Theorems 4.5–4.6 and Open Problem 4.7, printed pp. 11–12.
Read complete statements, the short Theorem 4.5 proof and adjacent
qualifications. Admissibility differs from positive definiteness;
the latter for all associated kernels characterizes real zeros.
The first sign is posed as a problem in that version. Reuse L233's
scaling; the source's frequency normalization differs from L018.
The dated open problem alone does not establish later literature status.

Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
[v2, 29 October 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf),
printed pp. 1–3: inspected the introduction, (1.1), (1.5) and
Theorem 1.3. It assumes RH through T>1/2 and gives all Laguerre signs
on |t|<=T−1/2, including central multiplicities. Its introduction
explicitly leaves the global first sign open. Reuse L466's v1 import
and application audit; no v2 import, strict-sign upgrade or new
manuscript audit is made here.

## Search, decision and different source lead

Web queries, 31 October 2026:

- `"cubic theta" "Laguerre" Xi`
- `"cubic theta" "Riemann Xi" reflection`
- `"Quasi-Riemann" "signed" theta`
- `"Riemann" "Laguerre" "cubic" theta transform`
- `"Xi" "associated kernel" "positive definite" 2026`
- `"Dunn" "Radziwill" "Laguerre"`

Local searches covered family003 Mellin/energy/scalar assessments,
the associated-theta assessment and signed-Xi phrases in ATTEMPTS and
drafts. Absence of `Laguerre` in the primary TeX was a navigation
observation, not a mathematical obstruction. Expositions, snippets,
review sites and adjacent rStation posts were discovery leads only;
no theorem is imported from them. Shell download failed DNS, but
browser access supplied every essential primary passage: not SOURCE_BLOCKED.

Three possibilities were distinguished: directly cite cubic reflection
for D_1 (statement mismatch); repeat the associated-kernel identity
(already L233, no new sign); examine additional actual-theta Fourier
determinant inequalities (a different source lead). Park the first;
the second is duplicate work.

The third lead is Sra, *Sharp order-four sign regularity of a Jacobi
theta kernel*,
[v1, 10 October 2026](https://suvrit.github.io/papers/csordas/csordas-v1.pdf).
Only the introduction, Theorems 1.1–1.4 and the beginning of Assumption
1.5 were inspected for nomination. Theorem 1.4 is a signed integral
constraint on actual Xi under its interval-arithmetic trust model.
The full assumption, essential proof and residual applicability remain
**unreviewed**. No bound or positivity transfer is asserted. Narrow
title/reverse-regularity/quartic-integral searches found no local
assessment or failure; this does not establish novelty.

No specified positive kernel or residual estimate currently justifies
a creative bridge calculation. The separate uncovered assessment names
the next source target and requires an explicit usable inequality and
range, or a precise mismatch. No new lemma, mathematical script,
mathematical obstruction or RH candidate was produced. Full matching
Mathlib coverage was not checked. No cross-notebook input was used.

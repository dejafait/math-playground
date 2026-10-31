# L564 independent audit: source coverage approved

TARGET: Audit L564's complete theta envelope, coefficient normalization, termwise derivatives and all-T cutoff C=16 against its cited inputs.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement searches, stronger-bound comparison and parity/L530/L563 overlap checks in 2026-10-31-hermite-moving-degree-first-sign-review.md and direct-link recovery in 2026-10-31-hermite-effective-tail-specialization.md; inspected L564 to identify its actual source needs. No changed target or new discovery search was needed.
SOURCE_EVIDENCE: Reopened https://arxiv.org/html/1902.06330v3 : (1.1), (1.3), (1.8)–(1.11), Theorem 2.1 (2.1)–(2.3), and proof (2.18)–(2.22) through its final Stirling step; reopened https://dlmf.nist.gov/18.14.E9 and https://dlmf.nist.gov/18.9.E25 and inspected the displayed equations and domains, not only landing pages. Source details and reused comparison below.
COMPARISON: The exact expansion, coefficient integral and real Hermite bound are known inputs. The inspected source statements do not directly supply L564's explicit all-T constants. An independent audit of that quantitative specialization is justified; no reproof of the expansion or new sign mechanism is approved.
GAP: Coverage approval is complete; L564's numerical inequalities, coefficient factors, derivative limits and cutoff remain independently unaudited. Signed discriminant margins remain outside scope.
REASON: This separate literature step clears the new audit target's coverage gate while preserving the completed calculation. It establishes no new mathematical bound and does not certify L564.
LITERATURE_REASON: The startup gate was REVIEW_REQUIRED for the newly nominated independent audit; this separate approval reuses ready discovery and checks its exact source scope, rather than repeating discovery to fill a quota.
SCOPE: Subsequent REPRODUCTION audit of L564 for actual Xi, T>=1, real t in [T,2T], j=0,1,2 and N=ceil(16(T+1)^2), including its complete kernel/coefficient estimates and legitimate derivative limits. No new signed target or complex-argument Hermite estimate is covered.

Inputs for the proposed audit are L018–L020, L564, Romik v3
(1.1), (1.8), (1.11), (2.1)–(2.3), DLMF 18.14.9 and 18.9.25.
The existing source comparison covers their stated normalizations and
real domains. This separate literature turn approves that coverage;
the mathematical audit itself remains the next research step.

The bounded audit test is whether the complete proof establishes,
for every T>=1 and N=ceil(16(T+1)^2), errors at most exp(-2pi T)
for j=0,1,2 throughout [T,2T]. In particular inspect the whole theta
sum, both half-lines, the Gaussian moment factorials, n=0 handling,
summation from N+1 and the uniform derivative-limit justification.
A failed bound must be repaired explicitly or downgraded before use.
Passing would certify an absolute approximation input, not positivity.
No cross-notebook input is proposed. Mathlib coverage remains unknown.

## Separate source-scope approval (2026-10-31)

Romik v3 fixes the same Xi height variable in (1.3), the full theta
kernel in (1.8), evenness in (1.9), and the full-line Fourier convention
in (1.11). Equation (2.1) gives the coefficient integral with the
Gaussian weight exp(-x^2/4) and divisor 2^n n!. Theorem 2.1 uses
physicists' Hermite polynomials, sums even indices with alternating
signs, and gives convergence on complex compact sets. Its constants
depend on the compact set. In the proof, (2.18) controls the first
integration region, (2.19) the remaining region for sufficiently large
indices, and (2.22) retains the full absolute moment tail. The final
Stirling bound has unspecified constants. These passages support the
imported expansion, not L564's numerical all-height estimate.

DLMF 18.14.9 applies to every nonnegative integer degree and every real
argument, with normalized envelope at most one. DLMF 18.9.25 is the
physicists' derivative identity H_n'=2n H_(n-1); the audit must handle
degree zero separately. The neighboring probabilists' identity 18.9.27
is not the input. Section notes attribute these formulas respectively
to Szász (1951) and Szegő (1975), (5.5.10). No source reproof is needed.

The broader saddle/asymptotic comparison and recorded failures are
reused from the two assessments above. In particular the parity and
moment-only preservation failures do not refute an absolute tail
bound; they do prevent treating it as an automatic sign transfer.
No matching explicit constant-16 derivative theorem was identified in
the inspected sources, which is not a novelty assertion.

The audit may use the cited standard expansion and elementary Gaussian
integration, geometric series, uniform convergence and calculus as
written in L564. Its task is to check their application, not to discover
a new lemma. If an essential missing source or changed hypothesis is
found, record that specific gap before dependent work. Passing the
bounded test permits later perturbation estimates for Xi'^2-Xi Xi'';
a signed truncation margin and all higher signs still need independent
work. There is no justified creative central-gap target in this source
approval step: the signed margin is not supplied by these inputs.

This is a process approval with no new mathematical evidence. L564,
its original derivation and all prior route stops are preserved.

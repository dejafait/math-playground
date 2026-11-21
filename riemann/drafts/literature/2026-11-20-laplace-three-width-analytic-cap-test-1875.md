# Analytic three-width cap test — nomination1875

TARGET: Attempt an analytic cap-2 bound for C034j's exact three-width solution using C034b/i's audited quantitative margins, a reparametrized use of de Boor's determinant formula, and C033w's compact Levy excision, without scalar evaluation.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1875 assessed the exact cap question with bounded quantitative interpolation, conditioning, signed-weight/TV and exact-expression searches; reused1838/1745/1797 and compared1789/1747 plus stops1798/1839/1843/1847/1866. Queries and evidence: drafts/literature/2026-11-20-laplace-three-width-variation-source-notes-1875.md; no originality claim.
SOURCE_EVIDENCE: de Boor, Divided Differences, SAT1(2005), pp60-61, Proposition43 and complete proof, Corollary(44), determinant formula(45), https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf ; Rump, Acta Numerica19(2010), internal p53, Theorem10.2/proof(10.8)-(10.9), https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf ; polynomial Lebesgue scope and exact local inputs in source-notes1875.
COMPARISON: Known divided differences supply a possible quantitative determinant tool after changing to the first nonconstant column as coordinate. C034b/i now supplies audited quantitative prefixes unavailable at1797's scalar test, but neither those inputs nor the source give this residual's weights. Rump's conditional solve need not be reproved or numerically reopened.
GAP: Verify the real C^2 reparametrization and node order, bound the actual determinant and relevant cofactors, independently bound the exact compact-excision residual, and test sum_i |a_i|<=2. No inverse norm, small perturbation, weights or cap is supplied; failure need not exclude other supports.
REASON: One bounded analytic application uses later audited margins and unchanged exact laws, avoiding1798's evaluator. This is classical specialization with unpaid family-specific estimates; this new ready nomination needs separate approval next turn before research.
SCOPE: Exactly C034j's width rows(1,3/2,2), columns(1,k(1,sigma),k(2,sigma)), A=M^T, right-hand side(1,m(1),m(2)); C033w's width interval[1,2] and removed Levy interval[1,3/2]; C034b/i signs on[1,2], larger interval for regularity only. No scalar evaluator, altered support/law, global inverse or Xi realization.

Import de Boor's statements, the standard named real inverse function
theorem and Cramer's rule. Check the proposed coordinate x=k(1,sigma),
transformed second derivative and reversed node order before using the
polynomial-column determinant formula. Every denominator and lower bound
must be quantitative. Do not reprove ECT or finite solvability.

C033w/C033m's compact excision is the proposed place to estimate the
residual perturbation relative to width-one observations. No favorable
size is assumed. Memberwise estimates must retain conjugates,
multiplicities and the entire tail. Levy positivity is not spatial
profile positivity. Compare independently justified determinant,
cofactor and residual allowances; do not run stopped scalar sums or
assume an inverse bound.

Success is a justified sum_i |a_i|<=2 for the exact mass/matching solution.
A rigorous >2 rejects only these three widths. If a quantitative input
is unpaid or the allowance loses the threshold, save the precise
comparison and stop. A restated conditional solver with all inputs
assumed is insufficient. No full-observation error, positive minimax
gap, necessary Xi budget or RH conclusion follows even from success.

Inputs: C034j/audit1874, C034b/audit1841, C034i/audit1870, C033w and
C033m's exact excision, inheriting C032m/n, C033l/C032q, C034c/h and
C034d/e/f. Retain labels/conjugates/multiplicities, ordinate0 exclusion,
gamma>14, strict strip/count, displacement zero through100, real zero
in(14,15), reciprocal-square tail, heat positivity, separate fixed-j=0,1
errors, both fixed-v1 sources, zero drift/killing and half-variance.
C034g unused; source-wide/finite-zero validity and matching Mathlib
coverage unverified. No global Sobolev premise or new script is needed.

This could give a feasible finite input to C033w; L030-L032/C032a,
full observations, signed height/cancellation and Xi realization remain
independent. Discovery1796 supplies no bounded independently paid central
interface. This is established-tool development, not creative research.

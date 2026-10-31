# Explicit two-term remainder on the fixed source band

TARGET: Test the uniform bound abs(H_t/B_t-(1+gamma))<=1/100 for 1/25<=t<=11/50, 0<=y<=1 and x>=4*pi*exp(10000), using Polymath v2 Theorem 1.3.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact arXiv/title, real/simple explicit-cutoff and H_t two-term searches plus narrow positive-time/Polymath local searches; inspected results and overlap are recorded in drafts/heat/2026-10-30-explicit-positive-time-tail-source-review.md. No novelty inference from failed searches.
SOURCE_EVIDENCE: D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , (5)–(24), Theorem 1.3, Proposition 6.6(i)–(vi); the explicit input bounds and full notation are transcribed in drafts/heat/2026-10-30-explicit-positive-time-tail-source-review.md. Theorem 1.5(i)–(ii), Proposition 9.1 and Lemma 9.2 with relevant proofs were inspected for downstream scope.
COMPARISON: Theorem 1.3 gives explicit f_t and all approximation errors on 0<t<=1/2, 0<=y<=1, x>=200; Proposition 9.1 gives stronger asymptotic decay but hides numerical constants. The proposed closed-band, prescribed-height 1/100 bound is a quantitative specialization, not a claimed new asymptotic result.
GAP: Bound the two n>=2 sums and e_A+e_B+e_(C,0) uniformly over every x beyond the proposed edge, retaining gamma, kappa, floor N and both time endpoints. Neither the proposed inequality nor a real/simple numerical cutoff has been established.
REASON: A numerical two-term remainder is a concrete input to a later strict contour comparison for a common tail. The source's unspecified phase/count constants prevent direct import of that tail; this bounded calculation can be tested independently of finite collision exclusion.
SCOPE: One analytic calculation using the literal explicit bounds from Theorem 1.3 and Proposition 6.6(ii), elementary series/integral estimates and existing L488 normalization if needed. Do not infer a zero count or use the unquantified |y|<=10 extension, Proposition 9.1 constants, or an unproved t*log(x/(4*pi))/2 lower bound. Source-proof audit, numerical phase estimates and finite collision exclusion are outside this scope.

The fixed height 4*pi*exp(10000) and tolerance 1/100 are proposed test
parameters only. They have not been checked numerically or analytically
in the literature turn that created this assessment. No program is
needed to enumerate N terms: a valid continuation must prove bounds
for all x in the unbounded range. If a mathematical script is useful,
it must retain a full certificate and cannot replace that uniform proof.

All theorem hypotheses and error bounds are available in the cited
source note. No essential source access blocker remains for THIS
residual estimate. Only elementary applicability/majorization is
approved, rather than a reproof of the Riemann–Siegel theorem. The
source's real/simple tail is already known qualitatively in L488.
Even a successful residual calculation would not certify its numerical
cutoff without separate phase control, strict counting and exhaustion.
It cannot exclude finite collisions or control lambda tending to zero.
Full matching Mathlib coverage is unchecked.

Continue if an explicit majorant at most 1/100 is proved throughout
the closed stated range; otherwise preserve the failing bound and
reassess this numerical specialization. No RH-equivalent positivity
or all-real-zero premise is authorized. This new continuation assessment
is subject to the supervisor's separate next-turn approval rule.

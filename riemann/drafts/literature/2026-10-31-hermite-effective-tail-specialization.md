# Effective actual-Xi Hermite tail: proposed specialization

TARGET: Construct an explicit Hermite tail bound for Xi, Xi' and Xi'' on [T,2T] achieving error at most exp(-2pi T) for every T>=1 with N=ceil(C(T+1)^2) and a numerical absolute C, using Romik's coefficient integral and DLMF 18.14.9.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact source comparison in drafts/literature/2026-10-31-hermite-moving-degree-first-sign-review.md: actual Hermite coefficients/remainders, stronger all-real Hermite bounds, derivative identities, local parity and moment-preservation failures were checked there. No exact effective moving-height theorem was found in the inspected sources; no novelty claim.
SOURCE_EVIDENCE: https://arxiv.org/html/1902.06330v3 ; https://dlmf.nist.gov/18.14.E9 ; https://dlmf.nist.gov/18.9.E25 ; Romik arXiv:1902.06330v3 (1.1), (1.3), (1.8), (1.11), (2.1)–(2.3), Lemmas 2.3–2.6 and proof (2.13)–(2.22); Theorem 2.7 and its proof were compared but have unspecified constants/onsets. NIST DLMF 18.14.9 supplies the explicit all-real polynomial envelope, and 18.9.25 the derivative identity. Exact formulas, URLs, scopes and inspected proof cases are retained in the source comparison.
COMPARISON: The expansion and global polynomial bound are known. Only effective numerical coefficient control, derivative domination and summed tail with the specified T/degree/error dependence require work. The target is a conservative specialization of a known approximation mechanism, not a source import or a new signed-positivity claim.
GAP: The exp(-2pi T) threshold and quadratic cutoff with numerical C are unproved. All constants, low indices, theta-sum tails and derivative interchanges must be justified. Truncation discriminant margins and all higher signs remain independent gaps.
REASON: This bounded test removes an actual missing input for a possible first-sign approximation certificate. Reproving Romik's expansion or sharp saddle asymptotics is unnecessary; only new quantitative dependence needed by the test is justified.
SCOPE: Actual Xi in L018–L020; physicists' Hermite polynomials and exact b_(2n) of Romik (2.1); T>=1, real t in [T,2T], derivatives j=0,1,2. No flow, arbitrary moment law, positivity assumption, complex-height global bound or RH-equivalent premise. Direct-source recovery review completed 2026-10-31; this unchanged target is approved for a subsequent calculation turn.

The source review is canonical for the bibliographic detail and source
qualifications. The separate recovery review below approves the unchanged target for the next
mathematical turn; no calculation was performed during either literature turn.

Define P_N as Romik's sum through n=N, degree 2N. The desired claim is
max_(j=0,1,2) sup_(T<=t<=2T) |Xi^(j)(t)-P_N^(j)(t)|
<=exp(-2pi T), with N=ceil(C(T+1)^2) and one explicit absolute C.
The threshold and cutoff are the test, not established estimates.

Essential inputs are L018–L020, Romik's cited exact coefficient integral
and convergent expansion, and the two cited DLMF formulas. L233 and
C233a explain downstream relevance; they are not positivity premises.
No cross-notebook result is used. L530 and L563 remain scope stops,
not inputs to the tail proof. The coefficient-envelope effectivization
may use the actual theta series and elementary inequalities, retaining
all summands. Any changed target needs a new review.

Success means a complete inequality for every T>=1, with numerical
constants, initial orders and legitimate derivative limits. A numerical
sample, an unknown onset or an unspecified multiplicative constant does
not pass. Failure should preserve the obtained envelope and the exact
threshold/budget it misses. This test does not require or certify that
P_N has real zeros or nonnegative D(P_N).

Downstream use is a later comparison of D(P_N) with the full perturbation
error in D(Xi). Its signed margin is unresolved and can vanish at multiple
zeros; all-degree positivity remains open independently. This is routine
quantitative development, classified REPRODUCTION, not creative work.
Mathlib coverage is not checked and is not claimed absent.


## Separate direct-source recovery review (2026-10-31)

LITERATURE_REASON: The supervisor reported that the ready assessment lacked a direct source URL; this bounded source-access/hypothesis check repairs that defect without repeating the discovery search or changing the target.

The primary links are [Romik v3, Chapter 2](https://arxiv.org/html/1902.06330v3#S2),
[DLMF 18.14.9](https://dlmf.nist.gov/18.14.E9), and
[DLMF 18.9.25](https://dlmf.nist.gov/18.9.E25). All three were accessible in
this review. DLMF redirects equation requests to the containing section;
the displayed equation numbers were inspected, not merely the page headers.

Rechecked Romik (2.1) and Theorem 2.1, (2.2)–(2.3): the coefficient is
an integral against the actual even positive Phi, and convergence is on
complex compact sets with constants depending on that compact. Rechecked
(2.22)–(2.23)'s intervening remainder argument through the end of Theorem
2.1: (2.22) retains the whole absolute moment tail; the subsequent use of
Lemma 2.6 and Stirling leaves unspecified constants. The two-region proof
(2.18)–(2.19) was also rechecked: its tail inequalities require sufficiently
large indices. None of these statements supplies the nominated all-T
numerical estimate. Theorem 2.7's asymptotic comparison is reused from the
prior assessment, not newly audited here.

DLMF 18.14.9 states exp(-x^2/2)|H_n(x)|/sqrt(2^n n!) <= 1 for every
real x and nonnegative integer n; its section note cites Szász (1951).
DLMF 18.9.25 states H_n'=2n H_(n-1); use n>=1, with H_0'=0 handled
separately. The section note cites Szegő (1975), (5.5.10). These are
physicists' Hermite polynomials; the adjacent probabilists' formula is
18.9.27 and is not the input. No complex extension of the real bound is
approved. These displayed standard inputs may be cited directly; their
reproof is unnecessary. The actual-Xi normalization and recorded parity,
L530 and L563 scope failures are reused from the source comparison above.

DECISION remains SPECIALIZE. This separate review clears the direct-link
and source-scope gate for the exact TARGET, without establishing its
numerical constants, derivative majorants, theta-series domination or
signed discriminant margin. Mathlib coverage remains not checked.
The unchanged success/abandonment test above controls the next attempt.
This is a process repair with no new mathematical evidence or novelty claim.

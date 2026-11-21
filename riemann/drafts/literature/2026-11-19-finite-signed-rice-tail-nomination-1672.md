# Finite signed Rice tail: source assessment1673

TARGET: Determine whether, for c=-1/4, a_d=2d^(1/3), b_d=d^(2/3)/2, F_d=F_d^I and Q_d=F_d'/F_d, the finite signed Rice tail satisfies integral_[a_d,b_d] F_d(c+it)dt=[F_d(c+it)/(iQ_d(c+it))]_[a_d,b_d]+o(|F_d(c+ia_d)/Q_d(c+ia_d)|) as integer d tends to infinity.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1673 completed bounded nonstationary/complex endpoint discovery and scoped C048/Rice duplicate/failure searches; queries and inspected passages are in 2026-11-19-finite-signed-rice-tail-source-notes-1673.md. Existing derivative-source coverage and stops1657/1665/1667 are reused; no novelty claim.
SOURCE_EVIDENCE: Beck et al., A First Course in Complex Analysis, ed1.6(Aug2025), Thm4.2.5 and Ex4.5.10, pp65,76, https://matthbeck.github.io/papers/complex.pdf ; Temme, arXiv1308.1547v1, Section3.1(3.3)--(3.6), p12, https://ir.cwi.nl/pub/21470/21470B.pdf ; DLMF2.3(i)(2.3.4--6), https://dlmf.nist.gov/2.3#i and2.4(iii)(2.4.10--13), https://dlmf.nist.gov/2.4#iii ; Pemantle--Wilson0903.3585v1 Thm2.3/Cor2.4, p5, https://arxiv.org/pdf/0903.3585 . Exact scopes and reused Nagel/DLMF5.11 coverage are in notes1673.
COMPARISON: Standard complex calculus gives an exact endpoint identity with a remainder; inspected Fourier/Laplace expansions do not automatically give uniform relative error for moving endpoints and degree-dependent data. C048n's pointwise margin and C048l's other-edge bound do not settle the tail. No inspected theorem directly pays the displayed conclusion.
GAP: A later specialization must check the full segment/common onset, actual Q_d' with justified complex neighborhoods, nonzero denominators, lower-endpoint normalization and integrated amplitude control, then prove the exact relative o(1) remainder. None is derived in this literature turn.
REASON: Essential endpoint-source coverage is now sufficient for one bounded REPRODUCTION attempt after separate approval; import known complex integration by parts and reuse derivative tools rather than reprove a theorem. The target is unchanged and the requested asymptotic remains unproved.

LITERATURE_REASON: The target began REVIEW_REQUIRED; assessment1669 explicitly excluded signed integration and no endpoint-remainder theorem had been compared. Inspect that missing scope once, without repeating adequate Cauchy/digamma discovery.
SCOPE: Exact TARGET only with C048a/j/l/m/n functions and branches; finite segment and exact complex integration by parts, including the stated domain, derivative, denominator and relative-error obligations. Excludes infinite opening, contour deformation, sign of the endpoint difference, bounded-core completion and any Xi/height implication. Newly completed review1673 requires separate next-turn source-scope approval.

## Completed comparison1673

[Source notes1673](2026-11-19-finite-signed-rice-tail-source-notes-1673.md)
record precise primary statements, relevant proof cases, source-scope
exclusions and the remaining specialization. No essential source is
blocked. A failed nonessential Drexel fetch is recorded and replaced
by the accessible author-hosted textbook. No Rice estimate or new
lemma was derived; matching Mathlib coverage is unchecked.

## Original nomination1672 (historical rationale)

The text below preserves the original uncovered nomination. Its
source-readiness comments are superseded by review1673 above; its
mathematical target, limitations and stopping test remain unchanged.

## Relevance and bounded test

The main gap is actual-Xi all-degree positivity, L030--L032/C032a,
with C028b's sublinear-height criterion, C028g's limit criterion and
a sufficient signed Mellin bridge unpaid. C048l leaves a finite
vertical integral at c=-1/4. The proposed subsegment would test whether
the audited local phase information can pay an actual signed
contribution, retaining its complex endpoint values. This is a possible
input to later control of that integral, not a sign for the full
integral or a sufficient RH criterion.

Use exactly C048a/j/m/n's functions and branches and C048l's finite
Rice normalization. In particular Q_d is the logarithmic derivative
with respect to s, not with respect to the real parameter t.
The bracket denotes the value at b_d minus the value at a_d.
The proposed formula is a target, not an identity or estimate proved
by this nomination. Verify the entire segment's domain with the shift
p=s+1/2 before using C048n, including all endpoint clearances.
No assertion about the sign or size of a boundary difference is
assumed, and the normalization of the error uses the stated lower
endpoint scale rather than an unproved noncancelling difference.

Continue only if inspected theorems permit a bounded attempt at this
exact relative o(1) endpoint error using the actual I, with uniform
control of every derivative and denominator required. If a matching
known result suffices, import or specialize it. If only an absolute
bound is available or an essential derivative/neighborhood obstruction
persists, record the missing estimate and park this target. A failed
search is neither evidence of novelty nor a reason to declare success.

The finite signed test is distinct from stop1657's fixed-d absolute
infinite opening, stop1665's in-region stationary-point proposal and
stop1667's theta boundary crossing. It asks for none of those stopped
operations. It still leaves the bounded-height part, the remainder
of the vertical segment, total cancellation, other polynomial
arguments and a sufficient Xi/height implication unresolved. An
endpoint expansion alone must not be promoted to a positivity result.

This is a proposed ordinary analytic specialization, not a protected
creative mechanism. No source-covered new mechanism for the bounded
core or the central Xi bridge is currently justified by this audit.
Review signed endpoint tools before planning further mathematical
work; do not repeat the already adequate Cauchy/digamma searches.
No cross-notebook theorem is proposed. Full matching Mathlib coverage
is unchecked. No new mathematics has been derived or approved here.

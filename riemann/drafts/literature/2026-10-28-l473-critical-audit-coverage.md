# L473 application audit: proposed continuation coverage

TARGET: Critically audit L473's paired Hardy-jet specialization and feasible law, including complex-shift errors, coincidence limits, strict covariance positivity and the four tight odd second constraints.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact paired-height comparison in 2026-10-28-two-height-hardy-jet-moment-coverage.md and the invocation-start 2026-10-28-two-height-hardy-jet-feasibility-test.md; this is an audit of the completed specialization, with no new discovery search or enlarged target.
SOURCE_EVIDENCE: Bettin arXiv:1111.0925v1 Theorem 1 p. 2 https://arxiv.org/pdf/1111.0925v1#page=2; Bui--Hall arXiv:2304.05178v1 Introduction (1), (6)--(7), Proposition 3 and Sections 5/7 https://arxiv.org/html/2304.05178v1; the primary statements/conversion passages were checked during L473's application; L472 Sections 4 and 7 supply the audited first-jet bulk.
COMPARISON: The cited arithmetic theorems cover the fixed complex shifts and orders; L472 covers only the first-jet bulk. The new paired specialization and matrix correction in L473 require an independent application audit, not reproof of the moment theorems or a new feasibility problem.
GAP: Check every analytic uniformity and finite-law step in L473, especially the weighted Bettin primitive at coincident shifts, the all-entry fourth Cauchy passage and exact correction of tight odd seconds. The current construction has not received that separate audit.
REASON: Separate literature approval completed on 2026-10-28: the saved scope covers the exact pending application audit. Its subtle complex-shift and small-eigenvalue arguments warrant conceptual audit next turn; no mathematics is approved for this literature-only invocation.
LITERATURE_REASON: The supervisor requires separate approval of this newly written audit assessment; recheck the essential primary shift hypotheses and conversion passages without enlarging the already assessed target.
SCOPE: Exactly L473 under its fixed ell=log H, separation 1/ell, orders 0--2 and stated errors; no shrinking separation, extra moments, effective onset, actual-law identification or stronger theorem.

Read the full canonical L473 and the input portions of L472, using the
completed source comparison for hypotheses and qualifications. The actual
proofs of Bettin's theorem and Bui--Hall Proposition 3 are not audited by
the application; the latter source omits its proof. No new external input
or Mathlib matching theorem is asserted. Recheck primary passages only
where needed to resolve a precise applicability issue.

The decisive tests are: the complete Bettin bracket remains holomorphic
at c=0 after weighting; normalized Cauchy derivatives retain O(1) and
O(ell^3) uniformly; all 21/126 entries are represented with the correct
phase signs; strict Gram positivity is proved analytically; the Schur
extension preserves L472's clipped marginal; the rare/bulk covariance
identity is exact, all masses are nonnegative, and one common onset gives
the coefficient 1/288 while preserving every tight odd error. Repair any
failure in the canonical proof and record its scope. A numerical preview
or the documentation checker cannot certify these mathematical claims.

The new obstruction is an abstract-law result, not a complete RH candidate.
Audit success without a repair is verification, not another mathematical
advance. A materially changed claim or new essential source scope requires
its own assessment. No broader positive-sign mechanism is preapproved.

## Separate source-scope approval, 28 October 2026

Reused both completed paired-height assessments, read canonical L473 in
full and L472 Sections 4/7, and checked the exact discriminator's failure
record. No duplicate audit was found in those relevant records. The
one-height obstruction and ordinary-moment/frozen-jet failures retain
their narrower scope; they do not discharge this application audit.

Reopened [Bettin v1 Theorem 1, p. 2](https://arxiv.org/pdf/1111.0925v1#page=2)
and its small-shift completion, pp. 9--10. The complex-shift hypothesis,
primitive error and complete-bracket coincidence prescription match the
saved source scope. Weighting that primitive and controlling coincidence
after the Hardy conversion remain application checks, not newly imported
conclusions. No arithmetic proof is independently certified here.

Reopened [Bui--Hall v1](https://arxiv.org/html/2304.05178v1), Introduction
(1) and preceding odd bound, (6)--(7), Proposition 3, Section 5's Cauchy
paragraph and Section 7's reflection conversion. Proposition 3 states
uniformity for four independent complex shifts of size O(1/log T), with
error O(T(log T)^3); its proof is explicitly omitted. These are the needed
source hypotheses, rather than a restriction to two squared values.
The extension to the specified paired centers and preservation of all
errors still require the independent audit. The sharper complex phase
estimate in L473 is an application argument to scrutinize, not a verbatim
claim of (6).

Decision: retain SPECIALIZE and approve exactly the unchanged TARGET for
the next research turn. No essential source blocker or changed assumption
was identified. This approval repeats the source decision and establishes
no new mathematical input: outcome STALLED, classification
NOVELTY_UNCHECKED. Full matching Mathlib coverage remains unchecked.
An essential hypothesis outside this scope requires renewed review;
failure of a covered application step should instead be repaired or
reported in that audit. No lemma, script, dependency or proof overview is
changed by this source review.

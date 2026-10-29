# L467 critical audit — approved source scope

TARGET: Critically audit L467's A=18 half-open and closed unit-shell bounds against Bellotti–Wong v2 Theorem 1.1, checking endpoint conventions, multiplicities, compact heights and exact all-height inequalities.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the scoped known-result, duplicate and failure comparison in drafts/literature/2026-10-25-explicit-unit-shell-count-coverage.md and the ready specialization assessment; reopened the versioned primary theorem and located its argument-principle passage; no new mechanism search was needed.
SOURCE_EVIDENCE: Bellotti–Wong arXiv:2412.15470v2 (7 July 2025), https://arxiv.org/pdf/2412.15470v2, definition and Theorem 1.1, printed p. 1, Section 3 opening argument-principle passage, p. 9, and Section 5, pp. 23–24; Section 5 coverage is reused from the count assessment and its two height cases were reconfirmed.
COMPARISON: The cited unconditional global count covers the analytic input; L467 supplies elementary specialization rather than a new count theorem. The source scope supports checking the specialization, but does not itself certify its inequalities or endpoint limits.
GAP: No essential source passage is missing for this bounded audit; independent verification of L467 remains pending. Full source-computation and manuscript audits, numerical tail onset and initial signs remain outside scope.
REASON: Complete the separate source gate for the newly written specialization and return to a mathematical audit using existing coverage.
SCOPE: Exact TARGET only, using L018, L464 Section 3 equation (6), L467 and the versioned theorem; no RH, simplicity or fixed-half-plane premise.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED requires separate approval of the new audit scope; reuse ready assessments and inspect only the endpoint/multiplicity-relevant primary passages.

## Source scope established

The definition on printed p. 1 uses positive ordinates through T inclusive,
and Theorem 1.1 states its first bound for every real T>=e, with constants
0.10076, 0.24460 and 8.08344. Section 3, printed p. 9, relates N to
the symmetric rectangle count via the argument principle. Thus the count
is multiplicity-counted; the displayed set notation is not a simplicity
assumption. The word “multiplicity” was not found in the searchable PDF;
the argument-principle passage supplies the relevant source evidence.

Section 5's large-height Table 2 case and compact-height Platt/gamma
case are covered by the prior assessment. Their split and final all-height
claim were reconfirmed. The source's computations remain cited inputs,
not independently rerun or audited. No new theorem or bound is derived
in this literature turn. Exact primary hypotheses, rather than the
abstract or a search snippet, support the approval.

## Audit obligations and relevance

The saved original target was to assess source coverage for this critical
audit. That comparison is complete; the TARGET above is the now-approved
mathematical continuation. SPECIALIZE permits a REPRODUCTION audit of
the elementary difference, not a reproof of the source analytic theorem.

Read L467's whole proof and test its source subtraction, derivative
comparison, exact decimal arithmetic, left-limit argument, compact N(4)
comparison, and multiplicity-preserving Xi interpretation. In particular,
the closed lower endpoint must retain all its zeros. If any off-ordinate
formula is used, its one-sided limit must be justified rather than
assuming the formula at a jump. These are next-turn proof obligations,
not conclusions of this source review. No specific defect is asserted.

Continue only if the audit verifies both shell conventions for every
stated height with one fixed constant. Repair a local proof defect if
possible; otherwise narrow or suspend that claim and record the exact
failed inequality or hypothesis. Do not silently use a first-zero table,
simplicity, an optimized increment theorem, or a generic-height exception.

The downstream use is a reliable explicit count constant in L464's
near-factor and far-shell estimates. The earlier duplicate search found
qualitative or assumed local counts, not this numerical certificate;
reuse that comparison without claiming novelty. The full effective-onset
route stays parked: saddle/amplitude constants, common onset, unbounded
initial signs and global mixed positivity remain independent gaps.
Mathlib coverage is unchecked. No cross-notebook input is used.

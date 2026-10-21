# Proposed independent marked octic support audit

TARGET: Critically audit L114's exact discriminant support and both infinity-point evaluations against Bruin–Stoll's hypotheses.
CHECKED: 2026-10-21
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Existing support assessment covers the construction target; no separate audit comparison has been performed.
SOURCE_EVIDENCE: Reuse drafts/literature/2026-10-21-marked-octic-two-cover-support.md and its inspected primary Bruin–Stoll Section 2, Lemma 4.3 and Section 6; audit-specific source comparison remains to be approved.
COMPARISON: L114 specializes known support containment, with exact polynomial arithmetic; the next target is an independent correctness audit, not a new descent execution.
GAP: Approve audit scope before independently replaying the full determinant/factor certificate and checking both smooth infinity rows and scalar-quotient containment.
REASON: Newly proposed continuation requires a separate approval turn; this proposal does not itself approve or perform the audit.

Essential inputs are L114, audited L113, the full
scripts/pair-genus-two/marked-octic-support-certificate.json and its
producer, and the unchanged support source assessment. The independent
audit should check signs, nonmonic leading coefficient, all prime factors,
the entire etale algebra and supported representatives, denominators,
the real-place qualification and the two distinct infinity points.
Its pass test is exact agreement on disc(G)=2^72*3^27*5^8*11^21,
sufficient support {2,3,5,11}, and two identity infinity images under
the cited convention; record any correction canonically. No assumption
of irreducibility, polynomial-order maximality, S-unit exhaustion,
complete local testing or rational-point completeness is permitted.
Unit/class data, surviving covers, degree-nine root recovery, remaining
factors, both L095 systems and minus-eleven stay unresolved.

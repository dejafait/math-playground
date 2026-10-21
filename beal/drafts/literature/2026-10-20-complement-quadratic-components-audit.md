# Quadratic direct-component classification — audit coverage

TARGET: Critically audit L104's exhaustive quadratic direct-component list, including discriminant support, splitting at two and whole-factor matching.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact quadratic-classification/splitting and Putz searches in 2026-10-20-complement-quadratic-components.md; scoped local checks found L104's construction and pending audit, with no completed independent L104 audit.
SOURCE_EVIDENCE: Reused inspected Shotton Proposition 5.14/Theorem 5.17, Oh Example 1.28 pp.19–20/Theorem 4.11 pp.78–79/Exercise 2.1 solution p.222, and Putz Proposition 5.26 pp.171–172; compared their recorded hypotheses with L104 and the canonical L093/L103 audited applications; no fresh external inspection claimed.
COMPARISON: The same negative squarefree quadratic fields and odd-discriminant two-adic splitting cases are covered; L103's audited idempotent argument covers whole-factor matching. Independent exhaustion and application verification remain a finite specialization, not a theorem import or stronger classification.
GAP: Perform the separate mathematical audit of every displayed support candidate, completion and whole-factor assignment; coverage approval alone verifies neither L104's arithmetic nor realization of a complementary algebra.
REASON: The prior source assessment has unchanged hypotheses and adequate essential coverage for this audit; approve its reuse without repeating browsing or doing the audit in a literature-only turn.
SCOPE: Exactly TARGET under L104's hypotheses and necessary-test interpretation, using L093 and audited L103; no L094 refinement, larger-field classification, compatible-product construction or fiber realization.
LITERATURE_REASON: The supervisor required separate approval of this newly proposed audit target; this turn compares its scope with ready coverage rather than adding literature to the already ready construction target.

## Gap, use and continuation test

The main gap in this branch remains elimination of both L095 simultaneous
integer power systems. Independent Beal signatures also remain unresolved.
The intermediate target is independent verification of L104's necessary
quadratic direct-component list. A verified list could constrain the
(8,2) and (4,4,2) branches before later field or fiber comparisons; it
would not settle the degree-ten or (6,4) branches.

Continue with the audit if the same hypotheses cover every case. Check
all eight negative squarefree support candidates, all four claimed
unramified-at-two completions, and each entire local-factor assignment.
Correct a missing field or overstated compatibility before accepting the
application. Abandon any shortcut that treats a subfield of U4 or U10 as
a direct factor, imports special-coefficient eliminations, or identifies
passing necessary tests with realization. No such finite check is
performed or approved as a result in this literature turn.

## Reusable primary inputs and scope comparison

The prior ready assessment is
`drafts/literature/2026-10-20-complement-quadratic-components.md`.
It records actual primary inspection and queries; those searches and
source versions are reused, with no novelty inference from search failure.

[Shotton, Number Theory III](https://www.maths.dur.ac.uk/users/jack.g.shotton/Teaching/number-theory/notes.html),
Michaelmas 2026, Proposition 5.14 classifies quadratic fields by a unique
squarefree integer different from 0 and 1; Theorem 5.17 supplies both
integral-basis cases. The negative squarefree parameters in L104 lie
within those hypotheses. No class-number or solution-coefficient
restriction is introduced by these results.

[Oh, An Invitation to Modern Algebraic Number Theory](https://www.math.columbia.edu/~gyujinoh/ANT_revised.pdf),
author-hosted revised PDF, accessed in the prior assessment on 2026-10-20
(no dated revision identifier established), Example 1.28 pp.19–20 gives
the maximal discriminant in both basis cases. Theorem 4.11 pp.78–79
equates its prime divisors with ramification. The complete Exercise 2.1
solution p.222 gives splitting/inertia at two for squarefree d congruent
to 1 modulo 4, distinguishing residues 1 and 5 modulo 8. These are
exactly the input types L104 invokes. Theorem 2.9's different congruence
case is not a substitute for that exercise solution. The audit must
check the arithmetic application; no reproof of the named inputs is needed.

L093's canonical audited application of
[Putz's thesis](https://doi.org/10.5463/thesis.832), version of record
(2024), Propositions 5.18–5.20 pp.168–169, fixes the coefficient-one
entire etale algebra, real signature, support and full two-adic products.
Its computational two-adic theorem is imported without replay. The
reviewed hypotheses include nonzero primitive coordinates and odd
coefficient product; they do not require every coordinate to be odd.
The rational direct factor remains a separate global hypothesis.

L103's independent audit, particularly its cancellation and idempotent
argument, already covers the passage from a global direct component to
a product of whole local fields, retaining repeated factor positions.
Thus the proposed L104 audit introduces no new base-change principle.
Its direct mathematical inputs remain L093 and L103; L095 is branch
context, not an additional solution or realization premise.

Putz Proposition 5.26 pp.171–172 was read in full in the reused assessment.
Its stronger quadratic eliminations use restricted coefficients and
stronger local data, so no terminal exclusion transfers here. There is
no essential unread theorem for this bounded audit. A citation alone
does not check L104's finite enumeration and application, which is why
SPECIALIZE rather than IMPORT is appropriate. Future audit classification
should be REPRODUCTION. Mathlib coverage remains not checked.

## Duplicate/failure check and decision

Scoped local checks covered L104, its construction draft, histories
353–354, the prior exact-target assessment, and audited L093/L103.
No completed independent L104 audit was located. ATTEMPTS/045's class-group
execution park and the complete high-degree classification park remain
unchanged; this finite audit requires neither backend nor database.
The existing standalone local-solvability results are not reopened.

This is coverage approval only. No new lemma, mathematical script,
arithmetic exhaustion, independent audit verdict or stronger result was
produced. PROOF.md and DAG.md remain unchanged. The exact TARGET is now
ready for a separate research invocation; stronger continuations require
their own coverage review.

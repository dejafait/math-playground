# All-order effective smoothing — conceptual audit coverage approved

TARGET: Critically audit L771's all-order integer threshold M(r), signed base lower bound and complete-theta relative error for every r>=2, m>=M(r) and u>=0, including parity, full-series differentiation, coalescing nodes and low-coordinate localization.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step404 reused the completed step402 exact-target search and step392 primary proof-case comparison; inspected L771 scope and all five proof sections for source dependencies, plus L019. No new external search or mathematical audit was performed.
SOURCE_EVIDENCE: Direct primary URLs https://publish.uwo.ca/~jnuttall/basicRH.pdf and https://publish.uwo.ca/~jnuttall/cumanal_a.pdf reopened 2026-11-04; Theorem3.1 and Theorem5.6 statements rechecked. Reused Nuttall basicRH.pdf (October2012), Theorem3.1/(3.1)–(3.12), pp.5–6; cumanal_a.pdf (20-page author copy, internal date unknown), Sections4–5, Lemmas4.1–4.3/5.1–5.5, Theorem5.6/(5.59)–(5.73), pp.8–19; exact inspected source cases and qualifications in step402/392 assessments. L019 and L771 were read locally for applicability scope.
COMPARISON: Existing coverage includes the same arbitrary-r/full-B/complete-K/all-height target. Neither the unsmoothed polynomial formula nor the different-Theta1 existential theorem imports L771. Its finite determinant, reciprocal derivative and conditional probability arguments are written directly and require conceptual audit, not a new source specialization.
GAP: L771 remains unaudited: its signed normalization, universal derivative majorant, conditional localization and integer onset require checking jointly for every r>=2,m>=M(r),u>=0. Exceptional coefficient transfer remains independent and outside scope.
REASON: Approve the exact saved audit target using unchanged adequate literature coverage; no essential unread external theorem is a premise of L771. EXPLORE authorizes scrutiny of the local proof and possible explicit repair within the same claim, not mathematical acceptance or a novelty assertion.
SCOPE: L771 as written, r>=2 integer, m>=M(r) integer, u>=0, original C_m factorials, full B and complete K; no smaller-onset, unsmoothed, exceptional-index or RH conclusion.

This nomination is not a literature assessment completed during the
research step. The previous EXPLORE assessment authorized the proof
attempt, not same-turn critical acceptance. No new theorem search is
needed merely because a separate audit is nominated; first reuse the
unchanged source comparison and inspect the exact new proof scope.
Any genuinely missing essential source case must be named before
additional literature. No numerical source table is an input.

Essential input: L019's kernel identity. L771 proves its determinant
integration, reciprocal transformation, coefficient/derivative costs
and low-region estimate directly. L769/L770 are methodological
precedent rather than mathematical premises of L771. The audit must
test this claimed dependency scope as well as the inequalities.

Check both (-1)^(r(r-1)/2) signs in the integral and reciprocal
change, the original factorials and origin boundaries, the confluent
coefficient determinant one, uniform C^(r-1) extension of the complete
theta remainder at y=0, and absolute rather than favorable signed
error control. Inspect the full infinite-series majorants, not only
the finite algebra certificate. Check the free-interval construction
against arbitrary unbounded conditioning coordinates and the all-m
integer cutoff, including x0>=A and u=0. Confirm that the positive
reference measure has finite nonzero mass and that no negative base
region is dropped. The exact finite r=2,...,7 checks are consistency
evidence only; they do not establish the universal statement.

The acceptance discriminator is the complete inequality
S(B)>=11/16 S(F0)>0 and |S(K)-S(B)|<S(F0)/8, uniformly on the
stated domain, with every constant computable from r by integer
arithmetic. If a defect appears, identify the precise estimate and
repair it within justified scope or qualify the result. A failure of
this particular bound would not refute eventual smoothing in general.
No new mechanism, transfer theorem or complete RH candidate is
nominated here. Full Mathlib coverage remains unchecked.

## Completed source-scope approval — step404

The prior nomination above is retained as the audit checklist. Its
statement that no assessment was completed refers to step403. This
separate literature-only step completes the readiness decision; it
neither repeats the proof attempt nor accepts its inequalities.

Reused [step402](2026-11-04-all-order-full-base-localization-review.md)
for the arbitrary-order polynomial, full-base low-height warning and
all-height comparison, and [step392](2026-11-04-nuttall-cumulant-induction-transfer-review.md)
for the essential different-kernel determinant and saddle cases.
These recorded primary reads already cover the unchanged source
question. No new browsing was necessary. Numerical beta-root tables,
unsmoothed formulae, Theta1 signs, and source display discrepancies
remain scope comparisons, not load-bearing theorem imports. No
source formula is specialized or reproved in this turn.

Read L771's hypotheses, conclusion, Sections1–5 and qualification
sections, and L019's kernel identity. This was a dependency/scope
inspection, not an independent verification of any estimate. L771
states its determinant integration and Newton/Rolle argument in
place, and gives its own full-series majorants and conditional bound.
Its only direct notebook premise remains L019. No all-order use of
L769/L770 or uninspected paper theorem is declared as a premise.
The audit must verify that assertion, including analytic domination;
its truth is not established by this readiness decision.

The distinct source obstructions remain relevant: positivity of each
kernel summand alone does not sign a derivative determinant, and the
source's pure-base comparison cannot simply transfer to full B.
L771 explicitly proposes to pay the low-coordinate signed region
under a positive reference measure. Whether that payment is correct
is precisely the next test, not a reason to ban this target based
on an older different-kernel stop. The coefficient range
k>=r-1+ceil(m/2) and exceptional-index gap remain unchanged.

The exact TARGET is now covered for one conceptual audit. Accept only
a complete check of the stated 11/16 and 1/8 bounds, including the
all-m integer cutoff and all-u conditional estimate. Record and
repair any defect explicitly or qualify the claim; a finite grid,
normalization certificate or fixed-u limit cannot pass this test.
No new lemma, script, DAG edge or PROOF change was made. Full Mathlib
coverage remains unchecked. Outcome EXPLORATION records a completed
source-scope decision, with no mathematical advance or newly proved
obstruction. Essential audit takes priority over discovery; there
is no independently supported new exceptional-index mechanism ready
for creative routing. Once approved, default to the mathematical
audit rather than another unchanged literature review.


## Direct-source recovery — step405

The ready assessment omitted direct URLs although its reused assessments
contained them. This is a citation-metadata repair, not a new mathematical
assessment or acceptance of L771. Both primary author-hosted PDFs were
successfully reopened on 2026-11-04:

- John Nuttall, [*Basic Wronskians in the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/basicRH.pdf), October 2012, seven pages, Theorem 3.1, printed p.5, (3.1)–(3.3). Rechecked the arbitrary-r polynomial statement against the saved step402 comparison. It concerns the unsmoothed beta base; no effective cumulant threshold is imported.
- John Nuttall, [*Cumulants, the Riemann Hypothesis, and Similar Problems*](https://publish.uwo.ca/~jnuttall/cumanal_a.pdf), 20-page author copy, internal version date still unestablished, Theorem 5.6, printed p.17, (5.59)–(5.60), and determinant expansion (5.61)–(5.65), p.18. Rechecked that its existential onset and all-u signs concern Theta1. This does not establish the full-B/complete-K quantitative comparison under audit.

The unchanged essential proof-case reads remain recorded in step392 and
step402; they were not repeated or newly certified. Existing display,
uniformity and coefficient-transfer qualifications remain in force.
No source is imported as a theorem for L771 and no specialization or
reproof is performed. Mathlib coverage remains unchecked. DECISION:
EXPLORE continues to authorize the exact conceptual audit, with no
essential source blocker identified. LITERATURE_REASON: supervisor-required
repair of missing direct primary-source URLs in this ready assessment;
this does not justify a further unchanged literature turn. The completed
step is STALLED mathematically: access and citation metadata were repaired,
but no new mathematical evidence or route-changing source overlap arose.

# Step196 nomination preserved before step197 source review

Historical snapshot only; the current assessment is
`drafts/literature/2026-11-10-fixed-eta-second-difference-review-196.md`.
The text below was the supplied, unapproved nomination.

# Fixed-parameter second difference — unapproved continuation

TARGET: Test whether Q_{eta_n}(n+1)-2Q_{eta_n}(n)+Q_{eta_n}(n-1)>=0 for every n>=2, with eta_n=1/(64*9^n), the same eta_n in all three terms, and the actual Xi paired nodes with all multiplicities.
CHECKED: 2026-11-10
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Nomination only; reused the inspected step192 recurrence comparison and L967/L971 stop records to distinguish the target. No discovery search for this exact fixed-parameter second-difference inequality has been completed.
SOURCE_EVIDENCE: Reusable background is Xiao arXiv:2006.13103v1 Theorem3.2/(3.10) p4 and Corollary3.3/proof with Conjecture3.4 pp4-5, as inspected in step192; L964, L966, L968 and audited L972 were read in step196. No primary theorem for this regularized inequality has been inspected.
COMPARISON: Xiao gives an ordinary-Li signed recurrence and an RH-conditional bound, not an unconditional convexity theorem or this three-index regularized comparison. L972 pays only denominator movement at one polynomial index; it supplies no answer to the nominated inequality.
GAP: Complete source and duplicate coverage for the exact all-n sign test, including known obstructions to convexity, before any new recurrence derivation or mathematical test. No sign or formula for the proposed second difference is asserted.
REASON: This is an independently testable component of the unpaid signed-index problem after completing the parameter-movement audit. Changed polynomial indices and a proposed signed convexity threshold lie outside the prior SPECIALIZE scope; the next invocation must be literature-only.
LITERATURE_REASON: The target now changes polynomial indices at fixed eta_n, whereas the ready assessment covered only an audit of moving eta at fixed index; essential exact-target comparison and possible convexity obstructions remain unread.
SCOPE: Nomination only, not research approval. Actual Xi nodes, algebraic squares, all multiplicities and complete denominators; n>=2 ensures every polynomial index is positive. No ordinate replacement, RH premise, assumed positive Stieltjes law, new finite-Q certificate or cross-notebook input.

## Definitions and reason to test

Use L972(1)'s already justified Q_u(k) for any positive real u and
integer k>=1, with a_k as in L964(5). In all three terms of TARGET
the parameter is eta_n, including the terms indexed n+1 and n-1.
This is not the second difference of the diagonal sequence with
three different eta values. No identity for this quantity is derived
in this nomination.

Main gap: L030-L032/C032a mixed positivity, equivalently the still
unpaid sufficient all-n sign condition in L966/L968. The proposed
intermediate target tests whether a nonnegative fixed-parameter
second difference is a viable signed-forcing component of a later
recurrence. Such a component could help control growth after initial
data, but does not by itself pay the parameter movement, initialize
that recurrence or close a cumulative margin. Those obligations
remain open even if the inequality succeeds.

Continuation test: a source comparison must identify the strongest
known conclusion and its exact assumptions, then select a bounded
proof or obstruction test for the complete displayed sign. A known
obstruction can retire the proposed convexity mechanism. Otherwise
only separately ready coverage may authorize a mathematical attempt.
A finite nonnegative prefix, a sign-free recurrence or omission of
any distant resolvent term cannot establish the all-n inequality.
A model obstruction must be distinguished from an actual-Xi failure.

## Coverage to reuse and coverage still missing

Reuse `2026-11-10-prescribed-q-index-recurrence-review-191.md`
for the exact ordinary-Li recurrence, source normalization, Xiao's
RH-conditional corollary, conjectural convexity, and the Maslanka
computational comparison. Do not rederive any published recurrence
or infer this regularized sign from the RH-conditional corollary.
Check exact convexity terminology, stronger results and negative
results before selecting new algebra. Discrete almost-periodic
sign-change results are a possible source lead, not an inspected
input or an asserted obstruction. No fresh retrieval has been made
for that lead or the new inequality.

The prior Cauchy/Taylor coverage and L972's off-diagonal definition
can be reused for their unchanged scopes; neither approves a new
signed index estimate. If a theta partial-fraction representation
is used outside L966's diagonal family, justify it and retain every
charge. No such extension is performed here.

The two retired alternatives are the L967 pointwise actual-profile
allocation and the L971 fixed reflected-prefix allocation; their
canonical failure records were read in step196. This new test asks
for the sign of a complete scalar index difference, not another
allocation of either failed kernel. It is selected as a different
independently testable target, without asserting it is viable.

No mathematical exploration or new lemma was undertaken on this
target. Mathlib coverage for a full matching theorem is unknown;
no Mathlib result is imported. This REVIEW_REQUIRED file does not
approve its own uncovered mathematics. Separate literature review
must precede any calculation or proof attempt.

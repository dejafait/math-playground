# Dyadic cubic infinite tail — second-ray nomination

TARGET: Test whether F(z)=product_(j>=0)P(2^(-j)z), P(w)=1+2w+2w^2+w^3, has det([z^(2+j-i)]F)_(0<=i,j<r)>=0 for every integer r>=1, with negative-index coefficients zero.
CHECKED: 2026-11-06
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Nomination only. Reused the first-ray source comparison, L840 finite-class stop and all-fixed-shifts source blocker as contrasts; a complete exact-family and stronger-result comparison for shift two has not been performed. No second-ray calculation or novelty claim accompanies this nomination.
SOURCE_EVIDENCE: Existing inspected sources are Macdonald (1995), I.2 (2.4)–(2.6)/(2.9), pp.20–23, I.3 (3.4)/(3.5)/(3.9), pp.41–42, and McMullen (2025-12-02), compact-product criterion/Theorem3.1 p.80, Cauchy coefficient formula/bound pp.12–13. L840 is the audited finite input; new L841 proves the infinite first ray and compact coefficient passage but is not independently audited. No inspected second-ray sign theorem is asserted.
COMPARISON: The scalar reciprocal-coefficient argument in L841 covers shift one only. L840's finite palindromic shift-two equality and nonnegative finite factors do not supply the missing infinite second-ray sign argument. Rectangular Schur identities and coefficient log-concavity are relevant source-search directions, not imported sign conclusions.
GAP: Compare the exact shift-two question with known rectangular Schur, reciprocal-coefficient and q-product results; inspect the hypotheses and any zero/equality cases needed for a complete sign test. No all-rank second-ray certificate, negative minor or asymptotic has been derived.
REASON: Shift two is explicitly outside the unchanged ready first-ray assessment. A separate literature-only turn must approve this exact target or identify a matching result before dependent mathematical work.
LITERATURE_REASON: The essential sign target changes from a scalar reciprocal coefficient to a higher solid shift; the saved first-ray coverage expressly excludes k>=2. Reuse its analytic and universal-identity evidence while assessing only the missing second-ray scope.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. This intermediate target tests whether the successful
infinite first-ray model also survives its next necessary shift.
Its plausible use is to discriminate a possible infinite-tail weak-ray
obstruction. It establishes no actual-Xi signs or realization, even
if the complete second ray is nonnegative.

The prior first-ray assessment is
`drafts/literature/2026-11-06-dyadic-cubic-infinite-tail-first-ray.md`.
Reuse its inspected Macdonald and compact-product sources; do not
repeat that search or broaden to general infinite determinant
asymptotics merely because Bultheel was previously blocked.
The all-fixed-shifts assessment and finite-class ATTEMPTS stop retain
their original evidence. Full support, inherited PF order, strict
signs, every k>=3, useful Xi growth and realization remain outside
this target. No cross-notebook input is proposed.

Essential local inputs are L840 at m=1 and L841, with the latter's
independent-audit status explicit. Reuse L841's ordinary coefficients,
F(0)=1, compact convergence and zero-free reciprocal disk only within
their proved scope. Check the exact shift/rank convention of any
rectangular identity before later use. Do not divide by zero minors,
assume strict positivity from weak signs, or infer closure of solid
rays under multiplication of their generating functions.

Continuation/abandonment test for a later approved attempt: one
rigorously negative determinant rejects this family's all-shift
weak-sign ansatz; a positive answer requires every integer r>=1
with exact zero cases and any analytic limit justified. A finite
sample is insufficient. If the bounded proposed method leaves an
uncontrolled sign or remainder, retain that specific obstruction
and stop it rather than switch to an unassessed pole mechanism.

No justified creative central-Xi target has emerged: an independently
signed Xi input is still missing. This nomination remains a model
specialization, not a relabeled creative attempt. Full matching
Mathlib coverage is unchecked. The current file nominates work only;
it neither approves its own new scope nor rejects the completed L841
specialization.

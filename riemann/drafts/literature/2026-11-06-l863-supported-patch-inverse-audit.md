# Supported phase-patch inverse: proposed audit

TARGET: Audit L863's matrix lower bound, complete adjoint compatibility and supported Holder estimate without assuming global or divisor-uniform control.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the off-divisor-linear-patch-inverse-test and collar-preserving-linear-phase assessments; targeted L863/L850 and patch-history comparison confirms unchanged scope. Primary Teixeira theorem and proof reopened for the required direct-URL recovery; no novelty search or mathematical audit performed.
SOURCE_EVIDENCE: Reinspected https://arxiv.org/pdf/1608.06213v7#page=8 Section4 Theorem3/Remark3 and full proof pp8-10, plus Section2.2 pp6-7 and Definition2 p7; reuse https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449 Section13.13 (13.7)-(13.9), pp449-452, previously inspected in the collar assessment.
COMPARISON: The divergence solver is known. L863 adds a conditional local coefficient lifting, an adjoint-kernel identification and a displayed Holder estimate, all within the prior patch-test scope. Reused source coverage suffices for a bounded audit of that specialization; replay the exact collar/regularity conventions and local checks, without a new mechanism or nonlinear theorem.
GAP: Source-scope approval is complete; independent checking of the specialization remains pending; no global seed, transition inverse, divisor-uniform estimate, nonlinear correction or Xi sign is established.
REASON: Approve the saved bounded audit after direct-primary-source traceability repair and scope comparison. L863 coefficient lifting still needs verification; reprove no general divergence theorem. This is process recovery, not mathematical progress.

The eventual audit inputs are L847, L850's general identities (not its
exterior numerical certificate), L863, and the already inspected Teixeira
linear theorem. Check its prescribed collar and Holder operator estimate,
the original-coordinate sign, distributional adjoint kernel, product-norm
and inverse-matrix estimates, and the strict e<delta^2 threshold.
The proof does not invoke Delay's API/KRC theorem. Do not require or infer
global ellipticity, a background graph seed, symmetry-preserving assembly,
or extension through F=0. The separate source-scope approval is now complete; execute the saved
bounded audit next, using this assessment unchanged. Full matching Mathlib coverage remains
unchecked. No cross-notebook input is proposed.


## Recovery source check and applicability

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in
this audit assessment; reopen only the essential theorem and reuse other coverage.

Pedro Teixeira, *Dacorogna-Moser theorem on the Jacobian determinant equation
with control of support*, DCDS 37 (2017), 4071-4089,
[DOI 10.3934/dcds.2017173](https://doi.org/10.3934/dcds.2017173),
[arXiv v7, 5 August 2018](https://arxiv.org/pdf/1608.06213v7#page=8).
Theorem3 allows integer r>=0, 0<alpha<1, n>=2, a bounded connected smooth
domain, signed C^(r,alpha) data with zero integral and zero on the fixed
collar. It gives a linear C^(r+1,alpha) solution zero on that same collar,
with norm constant depending on r,alpha,U,Omega. Remark3 makes the operator
independent of regularity indices, including smooth preservation. Definition2
uses a compact embedded collar of the whole boundary. The proof subtracts
a divergence-free extension from the boundary-zero initial solution;
Theorem2 supplies that extension via forms. These passages were reinspected,
including the proof's universality footnote. No positivity of linear data or
smallness condition from the nonlinear theorem is needed.

L863 uses n=2 and r=0 on its stated smooth coordinate domain; its collar
is explicitly of this kind. Retain closure regularity and the full prescribed
collar, rather than only zero boundary values. The coefficient lifting,
orientation, complete adjoint kernel and explicit bound are application
obligations for the next audit, not conclusions of this source review.
The Guillemin-Sternberg pullback citation above is reused, not newly inspected.
Delay's theorem and its API/KRC hypotheses are unnecessary for this audit.

The named parent assessments and history/2026-11-06-off-divisor-supported-patch-inverse-01.md
record the relevant overlap and transition limitations. No new source match
supersedes those stops. Retain L847, L850 general identities and L863 as
essential local inputs; do not use L850's exterior numerical certificate.
Continue if the audit validates the conditional matrix threshold, full
compatibility and Holder estimate, or identifies a repairable defect. Abandon
any inference of global or divisor-uniform correction absent new input.
This approves coverage only; full matching Mathlib coverage remains unchecked.

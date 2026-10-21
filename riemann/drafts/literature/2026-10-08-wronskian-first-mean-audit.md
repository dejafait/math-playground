# Proposed critical audit of the actual Wronskian first mean

TARGET: Critically audit L380's zero-safe Wronskian identity, moving-weight bounds and first-mean error comparison.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact/stronger-result searches recorded in 2026-10-08-actual-wronskian-noncommon-zeros.md and the unchanged first-mean assessment; scoped searches of the calculation draft and first-mean history identify L380 as completed calculation with audit pending, not a duplicate completed audit.
SOURCE_EVIDENCE: Reused Arias de Reyna arXiv:2406.16667v1 Theorem 6 and full proof pp. 5–6 https://arxiv.org/pdf/2406.16667v1#page=5; DLMF 25.2.1 https://dlmf.nist.gov/25.2#E1, 5.11(ii) https://dlmf.nist.gov/5.11#ii and 5.15.8 https://dlmf.nist.gov/5.15#E8; read full L380 and complete L369 (12)–(18), alongside L366 (1), L368 (3)/(5)–(7) and L369 carrier/reflection passages.
COMPARISON: L369 (16) covers complex C1 bounded-variation weights and total jet order at most two; L380 uses first jets only and the same positive-height fixed pair. The scalar sources do not state its Wronskian identity or mean: these and the actual weight hypotheses remain objects of critical audit, not imports.
GAP: Separate critical review of the completed first-mean specialization remains pending; no noncommon-zero implication or higher moment is covered by this proposed audit.
REASON: Separate source-scope comparison now approves the unchanged critical audit using ready literature coverage; no additional source theorem or reproof is required, and the completed calculation is neither rejected nor validated here.
LITERATURE_REASON: The newly written audit was REVIEW_REQUIRED; this separate turn checks its exact first-jet and moving-weight scope against ready coverage before any mathematical audit.
SCOPE: Critical audit only of unchanged L380 for the actual L366 pair, ordinary real derivatives, positive heights, dyadic normalization A²T²L and the stated first-mean error; no higher moment or zero-localization extension.

## Exact scope proposed for the next approval

Essential inputs are L366 (1), L368 (3), L369 (4)–(6)/(9)/(15)–(18),
and the whole new L380 proof. The prior assessment retains the primary
scalar theorem and proof cases, gamma-sector qualifications and direct
URLs. Reuse that adequate source review; this proposal supplies no new
literature evidence and does not request a repeated broad search.

The separate approval should determine whether that source coverage
licenses a critical audit of the unchanged ordinary-real-derivative pair
at positive heights, with normalization A²T²L. Review all four exact
mixed terms, b and b', variation of T,L, and the complete diagonal
including the n=1 collision. The audit must compare the bound
H^(-1/2)(log H)^2 with the diagonal H^(-1), without treating a large
upper error envelope as a lower bound on the actual error. No source
currently read supplies a noncommon-witness theorem.

Do not assume RH, simplicity, independence, eventual disjointness,
D≤0 or a common-zero count bound. Higher moments, response-phase
windows, noncommon localization, global actual-theta positivity, the
total L367 margin, low indices, heights above forty and endpoint margin
remain outside this audit. A successful audit would validate the
vanishing mean and this certificate's limitation, not infer an RH
consequence. Full matching Mathlib coverage remains not checked.

## Separate coverage approval, 2026-10-08

This review changes the audit decision from REVIEW_REQUIRED to SPECIALIZE.
It reuses the primary-source assessment rather than reopening an unchanged
search. The source statements and full essential proof cases were inspected
in that assessment; they were not downloaded again in this turn. Read here
were the complete L380 and L369 (12)–(18), plus the exact pair, reflected
carrier and carrier derivative passages named above. No correctness verdict
on L380 is issued in this literature-only turn.

Arias de Reyna v1 Theorem 6 assumes fixed x>0, sigma>=0 and
0<Im s<=x and retains the pole correction x^(1-s)/(s-1).
Its previously inspected proof treats sigma>0 and the sigma=0 continuity
case. L369 uses fixed x=3H and disks of radius min(1/4,1/log x)
inside that domain, deriving analytic jets by Cauchy estimates. The
right-line jets use local uniform absolute convergence at Re s=5/2>1.
DLMF version 1.2.8 coverage recorded in the reused assessment supplies
separate digamma/polygamma remainder estimates in sectors away from the
negative real axis; 1/4+it/2 stays in such a sector. Neither an Euler
series on the critical line nor differentiation of a real O term is
licensed. No new source version or changed hypothesis requires refresh.

The audit may cite L369 (16) if it verifies each actual complex weight
against (15): sup|w|+integral|w'| bounded independently of H.
The imported local proof includes the analytic truncation remainder,
pole correction, n=m=1 and every other diagonal, omitted diagonal tail,
and the far-below, far-above and near-diagonal off-frequency ranges.
All three derivative pairs used by L380 lie within its total-order-two
scope. This establishes coverage to attempt the audit; it does not certify
L380's bounds or their applicability without the later mathematical check.
No reproof of the scalar or weighted-mean input is needed.

The exact audit must check the opposite convention relative to L370,
the common-envelope cancellation and reflection term without dividing by
zeros, all four mixed terms, the full complex b,b', and variation of T,L.
It must then check the complete diagonal and the H^(-1) versus
H^(-1/2)(log H)^2 comparison. A larger upper error envelope is not
an actual-error lower bound. Retain L373's common-only-reset obstruction
as context, never as a premise of the mean or an actual-family conclusion.

Continue if each claimed identity and bound is justified by these inputs;
repair or qualify a failed claim during the later audit and preserve its
evidence. Even a successful audit only validates a vanishing mean and
this certificate's lack of a proved sign margin. Higher moments,
common-free localization and the main RH gaps remain uncovered. Full
matching Mathlib coverage remains not checked. This is source-scope
EXPLORATION, not a new mathematical result or completed proof audit.

# Nilpotent full-cost floor: audit coverage approved1952

TARGET: Review source coverage for an independent audit of C029c's phase conversion, all-channel norm comparison, and full trace-norm lower bound at T_d=d^2.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1952 reused the exact-statement searches and duplicate/failure comparison in assessments1947/1949 and source-notes1947/1950; read C029c, the needed finite-realification proof in C029b, stop1951 and Watrous coverage1523. Targeted primary-source opens resolve the standard-input scope, with no new broad discovery search or novelty inference; details are in drafts/literature/2026-11-20-nilpotent-floor-audit-source-notes-1952.md.
SOURCE_EVIDENCE: Reinspected Stillfjord-Tronarp2310.13462v2 Section1 (1b)-(2) p1 https://arxiv.org/pdf/2310.13462v2 ; Shadrin-Nikolov-Aleksov1510.03265v1 Theorem1.1 p2 and both proof cases p7 https://arxiv.org/pdf/1510.03265v1 ; Watrous2018 Section1.1 (1.175),(1.181) printed pp33-34 https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf ; NIST DLMF Tables18.3.1/18.5.1 and (18.5.5),(18.5.7) https://dlmf.nist.gov/18.3 https://dlmf.nist.gov/18.5 . Reuse source-notes1947/1950/1523 for earlier scope and proof-case evidence.
COMPARISON: The sources cover finite Gramian positivity, a degree-at-most-n scalar Markov bound for both parities, the rectangular Schatten ideal inequality, and standard Legendre data. They do not establish C029c's phase-conjugated all-derivative isometry, norm comparison, endpoint witness pairing or full-cost floor. Those existing local specializations, rather than new estimates, are the exact audit difference.
GAP: A later independent conceptual audit must verify C029c's phase direction, square-root covariance, every observation channel, degree/rescaling and constant cases, finite endpoint identities and compression-to-full-norm implication. This source review verifies coverage only; C029c's claimed finite floor and liminf>=7/16 remain unaudited, and actual-Xi transfer is outside scope.
REASON: This separate literature-only turn completes the pending approval of the audit proposed in1951. Standard inputs are sufficiently covered; no essential source blocker remains. Approve one conceptual audit of the existing proof, without deriving a new floor, repeating the diagnostic or reopening the parked actual-family attempts.
SCOPE: Exactly C029c's d>=3 unit subdiagonal shift, identity observation on all 2d real coordinates, specified normalized principal block, T_d=d^2 and full Schatten trace norm. Only audit and necessary correction of the existing specialization are covered; new horizons, metrics, witnesses or actual-family estimates require their own assessment.
COVERED_TARGET: Independently audit C029c's phase conversion, all-channel polynomial norm comparison, and full trace-norm floor at T_d=d^2, repairing or retracting any failed claim.
LITERATURE_REASON: C029c's newly written proof and proposed audit had only REVIEW_REQUIRED coverage at turn start; the required separate approval includes standard Legendre normalization references not explicitly scoped by the earlier diagnostic assessment.

## Exact continuation and available evidence

The canonical proof is
[C029c](../../lemmas/C029c-nilpotent-full-gramian-positive-floor.md).
Its hypothesis is exactly the unit subdiagonal shift, d>=3, the full
identity-observation realification, upper-left normalized block, and
T_d=d^2. The claimed finite bound is
(1-(d+1)^2/(8d^2))*sqrt(1-d^(-2))/2, with liminf at least 7/16.
These are claims to be audited, not independently verified here.

Reuse assessment1949 and source-notes1950, plus assessment1947 and
source-notes1947/1523 for finite Gramian and Schatten input scope. C029b is
the direct local input for the finite realification convention and
formula. C028b supplies main-gap relevance only, not a premise of the
nilpotent estimate. The exact finite Rodrigues calculations are written
out in C029c to fix normalization and endpoint signs. Review1952
located precise standard-reference coverage in DLMF; this licenses
checking that finite normalization calculation as reproduction, without
assuming a new asymptotic theorem. The notes distinguish source formulas
from the local all-channel witness argument, which still needs audit.

The subsequent conceptual audit should test the direction of phase
conjugation and square-root covariance; the bijection to every
derivative order; repeated use of the degree-n Markov constant on
lower-degree polynomials; even/odd orthogonality in the full norm;
endpoint signs and factors 2,T; and the use of a two-dimensional
compression as a lower bound on the full Schatten norm. The general
matrix input is precisely Watrous (1.175), with compatible rectangular
maps and p=1, not a dimension-normalized trace convention. This review
has approved coverage and has not executed that mathematical audit.

No unresolved spectral or conditioning premise is claimed for the
model proof. Correctness of its new specializations remains to be
independently checked. The actual-Xi coefficient structure, signed
energy estimates, full k_d=o(1), H_d=o(d), and model-to-actual comparison
remain unresolved and outside this continuation. The model's spectrum
is real but defective; a uniform diagonalizability assumption has not
been tested. Full Mathlib coverage is unchecked. No RH candidate exists.

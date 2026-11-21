# Actual Mellin factor: one fixed necessary-condition test

TARGET: Determine the sign of E'(0)^2-E(0)E''(0) for C828a's actual gamma-normalized Mellin factor, with certified endpoint, theta-series, quadrature and infinite-tail errors, and stop this fixed diagnostic after a pass or an inconclusive result.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step647's exact direct-factor interpolation and Laguerre-inequality comparison in 2026-11-05-direct-mellin-laguerre-interpolation-scope.md. This is its single s=0 diagnostic, not a point/order sweep or a changed class.
SOURCE_EVIDENCE: Patrick Pacific J.Math.44(1973),675–682, (1.1), Theorem1/(2.3)/(2.15) pp675–679; Runckel Trans.AMS143(1969),343–362, type(A) p356/Theorem4 p357/proof pp359–360; DLMF5.4.13/5.5.5; Johansson arXiv:1802.07942v1 Sections2/2.1 pp2–3. Primary links, full hypotheses and inspected proof cases are in step647's assessment.
COMPARISON: The inequality and sufficient interpolation theorem are known. Only actual logarithmic Mellin data and rigorous error bounds require specialization; neither q membership nor Xi zeros may be assumed. A negative value excludes the sufficient class, while a pass proves only one necessary condition.
GAP: The scalar's sign and its complete error certificate are not yet known. Global actual-E class membership, all-point inequalities, a sufficient actual sign mechanism and RH remain unresolved regardless of a pass.
REASON: A finite actual-data diagnostic can independently reject a now precisely specified sufficient premise. Prepare one bounded calculation, classified REPRODUCTION, after separate approval; no new preservation theorem or general quadrature reproof is needed.
SCOPE: Newly written ready continuation from literature step647, subject to separate supervisor approval. Exactly s=0, derivative orders zero through two, at most two declared precision/subdivision stages, with no automatic enlargement of the mathematical target.

Use exactly L828 (6), with C828a's p and M(0)=1/2:

    E(s)=sqrt(pi)4^(-s)M(s)/(M(0)Gamma(s+1/2)).

E is already real entire and E(0)=1. These construction facts do not
identify E with a distinguished reciprocal Bernstein-gamma solution.
Read L828 Section2 and C828a Section1 for the actual integral and
domination; L019 supplies the explicit theta kernel. L016/L018 fix
conventions. The complete-Bernstein exclusion and q-index stop are
scope contrasts, not mathematical premises for a derivative sign.

The future calculation must derive the differentiated-Mellin reduction
with absolute logarithmic domination, retain the factor 2 in x^(2s),
and propagate errors through the reciprocal gamma normalization.
Do not differentiate a truncated numerical table. The cited constants
can be imported from [DLMF5.4.13](https://dlmf.nist.gov/5.4.E13).
The completed assessment checks the factorial interface and downstream
meaning; global membership is not an input to evaluating the scalar.

Use [Patrick's necessary inequality](https://msp.org/pjm/1973/44-2/pjm-v44-n2-p26-s.pdf)
by citation, not a fresh proof. A canonical result file, if written in
research, must state exact density/normalization, evaluation hypotheses,
complete errors and the restricted conclusion. Mathlib matching coverage
is not checked; availability is not inferred from library homepages.

On the positive half-line split off the logarithmic endpoint, a finite
middle interval and the infinite tail. Make constants in the existing
kernel envelope effective, and certify the theta-series remainder uniformly
where integration uses it. A rigorous real-box sum is permissible.
If using [Johansson's analytic integration contract](https://arxiv.org/pdf/1802.07942),
reject complex boxes crossing the logarithm cut or leaving the theta
strip; certify both holomorphy and the full-box series remainder.
No singular endpoint or infinite interval is paid by the finite integrator.
All software/version/provenance assumptions must be stated in the result.

Declare a finite two-stage effort cap before numerical work. Save the
full certificate under scripts/<topic>/ with code, exact parameters,
all errors, complete load-bearing intervals and failure conditions.
Print the final interval, required threshold zero, pass/fail/inconclusive
status and artifact paths. Inspect complete selected values using the
local JSON inspector; previews do not verify bounds.

A certified upper endpoint below zero rejects the nominated Runckel
class (and LP membership). A certified lower endpoint at least zero
passes only this necessary condition. Overlap with zero without certified
nonnegativity is inconclusive; equality must not be excluded. Passing
or uncertainty ends the test, with no new orders or real points. If
certification fails, preserve partial reasoning and the exact missing
bound or backend, without a sign. Any subsequent mechanism needs an
independently new input and separate assessment.

This is routine known specialization, suitable for calculation/standard/high.
It is not a creative proof attempt or a possible complete solution.
No cross-notebook input, paper23 supplement or scheduler edit is needed.

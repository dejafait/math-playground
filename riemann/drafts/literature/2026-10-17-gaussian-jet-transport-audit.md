# Source-scope assessment for the finite-interval transport audit

TARGET: Critically audit L424's finite-interval transport identity and complete L423-law reduction, including all endpoint, scaling and component errors.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed step-174 primary-source and terminology search; inspected L424 in full, the scoped step-175 failure/history, L405 jet definitions, L421 component definitions/bounds, L423 correction and its step-172 audit, and L419 Borel branch cases. No new external search or novelty claim.
SOURCE_EVIDENCE: Reused Lasserre--Henrion--Prieur--Trelat (2008), author manuscript dated 2008-01-30, Sections 2.1--2.3, (2.7),(2.10)--(2.12), pp. 3--5; Henrion--Korda--Kruzik--Rios-Zertuche (2023-03-04), Definitions 2.4/2.7, (6)--(8), pp. 3--4, and Lemma B.1 with proof, pp. 17--18; exact citations and scope below.
COMPARISON: The sources cover the necessary C^1 finite-interval identity and finite-moment integrability; the remaining audit checks local normalization, explicit constants and complete component bounds, without weak limits or realization. The existing local inputs supply the stated component scope, but L424's calculations still require an independent mathematical audit.
GAP: Audit both endpoints, moving L correction, global psi/chi/Q estimates, high and intermediate contributions and symmetric translated bulk error at the exact finite-H Borel basis. Signing B_H, basis replacement and actual-height phase averaging remain outside this approval.
REASON: The proposed audit stays within the already inspected necessary identity and documented local construction; no essential source is missing. Approve one REPRODUCTION proof_audit next turn, without performing it in this literature-only step.
LITERATURE_REASON: The newly proposed critical audit required its separate scope approval; this turn compares it with reusable primary coverage and the exact local inputs, without repeating browsing.
SCOPE: Only the exact saved TARGET and L424's existing finite-interval reduction; no new separator, limiting distribution, nonlinear test family or trajectory realization.

## Reused primary coverage and applicability

The completed assessment
`drafts/literature/2026-10-17-jet-trajectory-compatibility.md` records the
queries, inspected primary statements and essential proof cases. Reuse
is appropriate because neither the test nor its finite-interval scope
has changed. This is a separate approval of the audit proposed after
step 175, not retroactive approval of new mathematics.

J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat,
*Nonlinear optimal control via occupation measures and LMI-relaxations*,
SIAM J. Control Optim. 47 (2008), 1643--1666,
[DOI 10.1137/070685051](https://doi.org/10.1137/070685051),
[author manuscript](https://homepages.laas.fr/henrion/Papers/ocp.pdf),
equation (2.12), supplies the integrated time/state derivative with both
terminal values for C^1 tests. Its setup uses smooth dynamics, bounded
measurable controls and compact state/control sets. In the proposed
specialization, C^2 f makes the two-coordinate trajectory C^1 and its
third jet continuous; each fixed H admits a finite compact box. The
Gaussian test restricted to that box is C^1. A uniform box as H grows is
not required for this identity. The audit must check the exact
nonautonomous substitution and bounds, rather than reprove the theorem.
Theorem 2.3(iii)'s convex velocity/reduced-cost no-gap conclusion is not
an input and supplies no realization of L423.

D. Henrion, M. Korda, M. Kruzik and R. Rios-Zertuche,
*Occupation measure relaxations in variational problems: the role of
convexity*, [2023-03-04 manuscript](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
Definitions 2.4/2.7 and Lemma B.1, distinguish nonlinear test integrability
from affine constraints: their finite-p test class has p-growth in the
test/time derivative and (p-1)-growth in its state derivative, with
interior and boundary p-moments. The inspected proof uses Holder (finite
p) or compact support (p=infinity). This supplies no H-uniform
integrability or weak-limit theorem. L424 proposes no such passage.

## Local comparison, duplicates and failure boundary

Essential local inputs are L405's ordinary jets, L419's actual Borel
six-state construction, L421's full high/intermediate definitions and
bounds, and L423's complete corrected law. L424 is the object of review.
Keep fixed response derivatives, curvature, covariance correction,
translation, every original moment tolerance and the uniform height
marginal. No RH, conditional independence, critical-function realization,
uniform integrability, or asymptotic distribution is an input.

For component scope, L421 (3)--(6) includes both high-radius branches and
the zero convention, the unnormalized high second-moment bound, and the
intermediate probability and direction. L423 (9)--(11), together with
its step-172 audit, retains the full O(sqrt(ell)) covariance correction,
bounded translation, exact mixed weight, uniform spectral bounds and
height marginal. L419's explicit strict/equality branch cases supply
Borel vectors, not continuity of the selected basis. These are existing
inputs for the later audit, not results newly certified here. In
particular, the older L419 rare-component bounds must not replace
L421's different high/intermediate construction.

The reused duplicate comparison finds that the undamped quadratic test
is already represented by the preserved second moments. No claim of
novelty is made for Gaussian damping or occupation identities. The
relevant failure record is
`ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`.
The numerical script is ancillary, not a theorem dependency. A successful
audit would validate a reusable necessary-test reduction, not provide its
missing bulk estimate or reopen the stopped numerical signing shortcut.
Any proposed new defect estimate needs its own concrete threshold and
source-scope decision. Continue the audit if all existing estimates can
be checked with these exact inputs; record a precise failed claim if
one cannot. Completion validates only a necessary-test reduction. It
does not reopen numerical signing: that requires a rigorous exact-bulk
estimate exceeding the complete error. No proof or mathematical script
was changed in this source review. Full matching Mathlib coverage remains
unchecked; generic calculus support is not a matching formalization.

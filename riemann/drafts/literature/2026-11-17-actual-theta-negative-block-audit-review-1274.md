# Actual-theta negative aligned blocks — audit scope1274

TARGET: Audit Planat202608.1692v1 Theorem6 for the actual theta kernel Phi=K/4, checking the origin-curvature sign, retained transverse endpoints and compact-uniform remainder needed for C_m^tot<=-pi*delta/(4*x^2) at fixed y>0 and Q_y'>=delta>0.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1274 reused the complete31Oct nonlocal-paired-tail source assessment and September27 parity comparison; exact paper/title/block searches in local assessments, failures and canonical results found source comparisons, L559's endpoint audit and C233a's small-y transfer, not an independent audit of this total-block claim. No novelty inference.
SOURCE_EVIDENCE: Planat, Preprints.org202608.1692v1,25August2026, DOI10.20944/preprints202608.1692.v1, Lemma2/(8)-(11), Section5 Lemmas4-5/Proposition4/Theorem4/(38)-(49), Lemma6/(51)-(52) and Theorem6/(60), with proof coverage reused from31Oct and selected relevant cases inspected in1274; published communication Symmetry18(2026)1283 Theorem7 reports the same claim.
COMPARISON: The exact negative-block result is already a source theorem. The task audits its applicability and proof, particularly the moving transverse endpoint and uniformity over blocks; it does not seek a new theorem, infer the total-integral sign or reopen independent-sector positivity.
GAP: The source's decimal curvature bounds, analytic remainders and local specialization have not been independently verified here. Even a successful audit only excludes universal phase-aligned block positivity in this representation; Schur positivity and correlated/global signing remain open.
REASON: A concrete known sign claim is independently testable after no central positive-sign candidate survived discovery. Reproof is limited to auditing this source claim, justified by L559's failure of an earlier endpoint deletion and the need to distinguish compact-uniform estimates from pointwise ones; no certificate campaign or general theta reproof is requested.
SCOPE: Fixed arbitrary y>0; the exact full Phi, M, A, Q_y, epsilon_x and J_m defined in L559 and the cited source; compact intervals K0 strictly inside K1 strictly inside (0,infinity), inf_K0 Q_y'>=delta>0; eventual x with J_m contained in K1. Check local existence of such an increasing interval using Phi''(0)<0. No y-to-zero uniformity, global sector asymptotics, total-growth sign or all-degree extension.

## Source claim and exact test

Use L019's K and the matching Phi=K/4 normalization recorded in
C233a. The interval K0 in this assessment is not the theta density K.
The source defines alpha_m=m*pi/x and J_m=[alpha_m,alpha_m+pi/x].
Use the complete C_m^tot=C_m^(Q)+C_m^(epsilon) of L559; neither
transverse endpoint may be deleted.

[Planat202608.1692v1](https://www.preprints.org/manuscript/202608.1692),
Theorem6, asserts the TARGET threshold for every block with alpha_m
in K0, beyond x1(y,K0). Its proof invokes the compact-uniform
hierarchy of Theorem4 and the increasing-origin interval of Lemma6.
The complete proofs were already inspected in
`2026-10-31-nonlocal-paired-tail-remainder-comparison.md`; reuse that
coverage. Section2 Lemma2 treats the negative n=1 curvature summand
and a positive infinite tail. Section5 retains four integrations by
parts, full-period Taylor moments and a bounded integral remainder.
These are source claims for audit, not mathematical deductions made
in this literature turn. The unrefereed version's abstract prefactor
differs from its master identity; use the body and C233a's normalization.
The published communication is [Symmetry18(2026),1283](https://doi.org/10.3390/sym18081283),
Theorem7; its short proof explanation defers to the companion.

The bounded audit must check the actual theta curvature sign with
rigorous inequalities, retain b=0 and b=a contributions, and justify
each needed uniform bound on the compact triangle 0<=b<=a, a in K1.
Do not infer an integrated remainder order by integrating an inadequately
controlled pointwise asymptotic. If a printed constant-dependence list
omits a necessary derivative, state the correction and prove its finiteness
for the actual kernel before using it. No effective x1 is required by
the stated claim; any claimed explicit threshold would require additional
coverage. The grid conclusion must retain the block-containment and
interval-length conditions. No assertion is made about fixed m near
the origin as x tends to infinity.

Continue if these checks rigorously establish the quoted eventual
negative bound with all hypotheses. A wrong endpoint, failed curvature
certificate or unrepairable uniformity assertion stops this import;
save the exact defect. A correction sufficient only for a weaker
threshold must be labeled accordingly. Numerical block samples do
not settle the assertion. Do not conclude that the global integral is
negative, that a Schur form is negative, or that RH is false.

## Relevance, inputs and routing

The main gap is L030-L032/C032a's all-degree actual-Xi mixed sign.
Plausible downstream use is to prevent this particular positive-envelope
IBP decomposition from being used as a termwise sign certificate.
This is an obstruction audit, not a new central positive mechanism.
The negative-block conclusion is source-known and supplies no progress
beyond the inspected literature. No lemma should be added just to
record another copy of its statement; retain any full audit in the
appropriate existing canonical proof or a justified separate result.

Essential inputs are L016/L019 for the actual theta series, modular
evenness and derivative domination, L559 for the precise residual and
retained endpoints, and C233a for coordinate/normalization comparison.
L030/L032/C032a explain relevance only, not sign premises. Before
mathematics read the needed full canonical proof ranges; this nomination
does not independently audit their existing arguments. Initialization,
singular Schur blocks, all degrees, graph realization and global signs
remain unpaid. No cross-notebook input. Mathlib full matching coverage
and supporting uniform-IBP coverage are unchecked; no absence claim.

This newly written ready assessment awaits separate next-turn approval.
After approval the mathematical work is REPRODUCTION and
proof_audit/conceptual_audit, deep_research/xhigh: moving boundaries,
oscillatory cancellations and uniformity are the critical checks.
No creative routing is justified without an independent central signed
identity; this audit must not be labeled creative or candidate review.

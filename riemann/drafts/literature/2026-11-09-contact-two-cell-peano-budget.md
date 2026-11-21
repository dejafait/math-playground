# Fixed two-cell contact Peano budget — source-approved test

TARGET: Test whether the fixed two-cell endpoint-corrected Peano budget at x=1/4 and x=1 is nonnegative at every genuine d=2 actual-theta contact for 0<lambda<1/20, retaining all three null rows and the full exterior penalty.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step191's completed contact-specific source comparison, exact/stronger Peano and theta-contact searches, and its scoped duplicate/failure check. No matching actual-contact budget theorem was inspected. The precise pilot below is a proposed bound, not an assertion of originality or feasibility.
SOURCE_EVIDENCE: Direct primary PDFs inspected 2026-11-09: Diethelm(1997), Theorem1.1 p727, https://ems.press/content/serial-article-files/34945?nt=1 ; Karlin–Novikoff(1963), Section1 identity(A), pp1252–1253, https://msp.org/pjm/1963/13-4/pjm-v13-n4-p18-s.pdf ; Bozek–Solak–Szydelko(2008), Section2.1 pp112–115, sign split p114 preceding(9), https://journals.bg.agh.edu.pl/OPUSCULA/28-2/28-2-01.pdf . Compact hypotheses and both kernel-sign cases checked; no infinite-interval or theta-sign result imported.
COMPARISON: Compact signed-measure remainder representation and sign splitting are known; only their endpoint-corrected application needs reproduction. The new proposed estimate bounds curvature on two fixed cells and charges an absolute exterior error. It asks the complete contact system for additional quantitative information, permits L916's negative curvature and imposes neither a global comparison order nor a crossing count.
GAP: Verify the proposed interface including endpoint regularity and orientation, then establish or obstruct the actual fixed budget under H2>=0 and all H2c=0 rows. No budget sign, contact, flux sign or all-degree statement is established. An interface identity alone does not meet this target.
REASON: This is one independently testable localization mechanism beyond the stopped global-convex application. Its separate positive/negative kernel masses, curvature bounds and exterior cost can be bounded without assuming the flux. Stop at an unpaid decisive estimate rather than moving cuts, enlarging a multiplier class or reverting to one crossing.
SCOPE: Exactly the definitions and two cells below, actual full theta law, 0<lambda<1/20 and all nonzero real contact vectors normalized by c0^2+c1^2+c2^2=1; every support pattern and all three null rows are retained. Optional L914 arithmetic is unnecessary. Source approval completed in step192 after the step191 nomination; the exact target is ready for a subsequent research invocation, with all mathematical checks below still unpaid.

## Purpose and inputs

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is a sufficient conditional d=2 boundary-flux
test, potentially useful for decreasing-parameter continuation. Essential
local inputs are L019/L058/L874/L915/L916 and the named Csordas input
as qualified there. L916 is a shape obstruction to retain, not a
contact premise. No cross-notebook result is used. Contact existence,
initialization, tangency, lambda=0 and higher degrees remain open.

Use L915's Q(x)=R(sqrt(x)), nu_lambda and h=-sigma_lambda.
Let mu denote the signed pushforward of -Q dnu_lambda by h, with
H=h^(-1). Mu is not an alternative positive probability law. Retain
H2>=0 and all three equations H2c=0. The proposed normalization of c
is to remove the homogeneous scale, not to discard a support pattern.

## Proposed fixed certificate, not a derived result

The following specifies the mathematical test; none of the claimed
interface properties or inequalities is proved in this literature turn.
First check every normalization and orientation from the canonical
lemmas and the primary compact theorem. No script has been run.

Take a=-1 (the proposed lower image endpoint), b=h(1), d=h(1/4).
Check the extension H(a)=0 and H in C^2[a,b], including its right
derivatives at a. No lower-endpoint assertion is imported from L916's
interior inverse theorem. Put

    M0 = integral_[a,b] dmu,       M1 = integral_[a,b] y dmu,
    wa = (b*M0-M1)/(b-a),         wb = (M1-a*M0)/(b-a),
    J(f) = integral_[a,b] f(y) dmu(y)-wa*f(a)-wb*f(b),
    Kc(t) = J((y-t)_+),           a<=t<=b.

The endpoint terms are signed and may have either sign. Check that
this finite signed functional has the required affine cancellations;
do not claim that restricting mu preserves its original cancellations.
Do not confuse this Kc with the theta kernel K(u).

For the fixed cells I1=[a,d], I2=[d,b], propose the quantities

    Pj = integral_Ij max(Kc(t),0) dt,
    Nj = integral_Ij max(-Kc(t),0) dt,
    kj_minus = inf_Ij H''(t),     kj_plus = sup_Ij H''(t),
    ell(y) = H(a)+(H(b)-H(a))*(y-a)/(b-a),
    D = integral_(b,infinity) |H(y)-ell(y)| d|mu|(y),
    Budget = sum_(j=1)^2 (kj_minus*Pj-kj_plus*Nj)-D.

The exact infima/suprema may be replaced only by certified outward
bounds, with the corresponding orientation checked. They depend on
lambda and the fixed cells, not on a desired contact flux. The total
variation in D retains the complete exterior; in square coordinates
the proposed expression is

    D = integral_(1,infinity) |x-ell(h(x))| |Q(x)| dnu_lambda(x).

Check that the inverse is defined on the whole proposed exterior and
that D is finite. The integrability estimates for xQ and hQ in L915
are available inputs; any further endpoint or limit claim must be paid
explicitly. No finite cutoff or head-only theta approximation is allowed.

The proposed application would need to verify the orientation

    -Phi = integral H dmu  >= Budget,

before seeking Budget>=0 at every stipulated contact. This line is
the interface to test, not a proved lemma here. Cite the known compact
Peano representation rather than reprove its general theorem. Any
local derivation is justified only to check endpoint correction, tails
and signs; an interface-only lemma does not close the nominated gap.

## Discriminating test and stop conditions

The essential new test is Budget>=0 for the actual contact-conditioned
data with exactly these cells and full D. Unlike a flux rewrite, this
candidate uses separate extremal curvature bounds and an absolute
exterior penalty; it may fail even when the desired flux sign holds.
No sign of Kc, global convexity or concavity of H, reversed convex order,
exact crossing count or all-degree positivity may be assumed.

Use the finite null equations to seek independent control of Pj, Nj
and D. Do not replace that task by direct evaluation of Phi, or by
repeating the already known two cancellations. A successful certificate
must display actual versus required bounds and every boundary term.
Failure on arbitrary moments or noncontact c rejects only that
relaxation, not the actual-contact statement. A genuine-contact negative
needs a rigorous actual-law contact certificate; none is presently
asserted. A conditional obstruction must retain that qualification.

If the first bounded attempt supplies only the representation or
leaves its decisive budget sign unpaid, preserve that reasoning and
stop this pilot without adjusting the cuts or launching a sweep. If
the contact domain is shown empty, record that as an emptiness result,
not evidence that this comparison mechanism signs an existing boundary.
Do not add a lemma merely to record a standard identity. Any substantive
proved input belongs later in a canonical lemma with Hypotheses,
Conclusion, Proof and Mathlib; no lemma is created in this nomination.

The stopped global-convex, automatic-variation, one-crossing and
degree-nine density-dual scopes remain intact. This is a proposed
conditional sufficient bound, not a candidate RH solution. Full and
supporting Mathlib coverage for this specific application are unchecked,
not asserted absent. Classification of future work: REPRODUCTION for
the compact interface alone; POTENTIALLY_NEW only for a genuine new
actual-contact estimate or obstruction within the assessed scope.


## Separate source approval — step192, 2026-11-09

LITERATURE_REASON: Supervisor recovery identified missing direct URLs in
this ready assessment. Reuse step191 discovery and duplicate/failure
comparison; retrieve only its load-bearing primary statements and cases.
No fresh broad search or mathematical specialization was undertaken.

Diethelm Theorem1.1, p727, requires a continuous linear functional on
C[a,b], annihilation of polynomials of degree at most s-1, and an
absolutely continuous derivative of order s-1 for the test function.
Its kernel is the functional on the truncated power divided by (s-1)!.
Only s=2 is proposed here. PDF text was inspected; the page-image request
returned a placeholder and is not claimed as visual verification.
Sard Chapter1 Theorem43 remains an unread proof reference; the named
Peano–Sard theorem is imported by Diethelm's precise statement.

Karlin–Novikoff Section1, pp1252–1253, identity(A), treats signed measures
on a finite interval with zero mass and first moment. These cancel the
boundary terms in the two integrations by parts. The subsequent convex
cone conclusion additionally needs a nonnegative second primitive.
Neither that sign nor an infinite-interval extension is imported here.

Bozek–Solak–Szydelko Section2.1, pp112–115, treats its specific affine-exact
quadrature and C^2 tests. The constant-sign case uses one derivative
value; the sign-changing case on p114 separates two values. Its K-minus
is min(K,0), whereas this pilot's N is a nonnegative negative-part mass.
This is a source-notation distinction to check in the future application,
not a derived budget inequality. No quadrature constants transfer.

Decision: retain EXPLORE for the exact actual-contact budget; source
coverage is adequate for one bounded attempt. This repairs traceability
and separately approves the nomination; it establishes no new estimate
and does not improve on step191's mathematical evidence. Do not extend
coverage to other cuts, contact bands or multiplier classes. Endpoint
regularity, affine correction, full-tail orientation/integrability and
budget nonnegativity remain research obligations. Full and supporting
Mathlib coverage for this application remain unchecked. No lemmas,
mathematical scripts, DAG edges or proof overview were changed.

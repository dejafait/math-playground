# Fixed-minus-three marked curve: quotient attempt

2026-10-20. Approved target: Test whether L109's fixed-minus-three
marked curve has an explicit genus-one quotient over Q.
Prior SPECIALIZE assessment:
`literature/2026-10-20-marked-pair-genus-one-quotient.md`.

Main gap: residual primitive integer exclusion, here the rational-factor
branch of ordered (3,5,11). The intermediate target is an actual proper
genus-one image of the marked pair curve D, with the exact minus-three
twist. Its plausible use is a smaller necessary rational-point image.
Continue only after exact square-class, inverse-field, degree and proper
extension checks succeed; otherwise park this factor-cover implementation.
Point completeness, degree-nine root recovery, remaining factors, both
L095 power systems and minus-eleven remain independent gaps.

Inputs read: audited L109 and L110, including L110's completed critical
audit and normalized charts. Compared the existing source assessment,
history/383–384 and ATTEMPTS/050. No existing quotient was found in those
records; the exhausted bounded Jacobian detector is preserved.

Initial work in progress, saved before arithmetic verification: write
Q4=7+52T−6T²−64T³−25T⁴, a=−3(T²−4),
rho=M L/[30(T+2)K], with L110's F,K,L,M,u,W.
The proposed identity is z=a*rho². Proposed split coordinates are
h=v/rho and R=3W/h, giving h²=a and R²=−33Q4.
These formulas and their inverses have not yet been certified here.
The candidate quotient is the smooth quartic R²=−33Q4; rational origins
must be tested exactly, including T=±2 and infinity. No rational-point
classification or integer exclusion is claimed.

## Completed bounded attempt

The proposed twist and maps pass. Canonical full proof and precise
source specializations are in
[L111](../lemmas/L111-marked-pair-genus-one-quotient.md).
The smooth proper quotient is
R²=825T⁴+2112T³+198T²−1716T−231, of genus one with origin (2,165).
Its degree-two map is the fixed field of h -> −h, R -> R;
the deck involution over B instead changes both signs. The maps
preserve L110's original s and exact marked constant. A finite
quotient point lifts precisely when 3(4−T²) is a rational square,
with the ramified T=2 fibers and infinity treated in smooth charts.

`scripts/pair-genus-two/marked_quotient.py` writes the complete
`scripts/pair-genus-two/marked-quotient-certificate.json`.
All 28 checks pass, with twelve full field-identity residuals zero.
Actual/required degree is 2/2; actual/required quotient genus is 1/1.
The proof supplies the geometric degree, proper extension and genus
arguments; printed thresholds alone do not verify them. Complete
residuals, gcds, rho and check values were inspected using the shared
JSON inspector. No integer-origin scan was needed after the exact
boundary origin succeeded. Initial Python lower/upper-field coercion
failed before output; fixing operator delegation repaired the script,
with no mathematical change or earlier failed certificate to discard.

Outcome: RESEARCH / ADVANCE / REPRODUCTION; actual type proof_attempt.
This is useful local specialization of inspected known methods, not
progress beyond them or a Beal exclusion. Continue to a separate
critical audit, preceded by approval of that new target's source scope.
All independent gaps and parked mechanisms listed above remain open;
L108 and all preexisting work are preserved.

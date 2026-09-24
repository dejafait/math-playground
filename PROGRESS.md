# Current notebook state

STATUS: IN_PROGRESS

STEP_ID: 2026-09-24-endpoint-first-order-subtraction-01
STEP_OUTCOME: NEGATIVE
STEP_EVIDENCE: L348 derives the exact correction and improves its remainder's long-height mean square to O(r^(-4)), but leaves nonconstant mass at least 3r/4−O(1), or 3r/16−O(1) for every scalar multiple. The weighted certificate still diverges. See lemmas/L348-endpoint-first-order-subtraction-obstruction.md.

Main bottleneck: global mixed reciprocal-zero positivity remains unproved. L320 needs a logarithmic initial segment of Laguerre signs, but L296's bands strictly above coefficient 1/4 leave low logarithmic and sublogarithmic indices open. Heights above forty and the endpoint arithmetic margin remain unresolved.

Route decision: stop first-order subtraction at σ=1+1/r as a repair for absolute sampling norms. Test changing the denominator to the Mellin width σ=1+1/sqrt(r); uniform grouped coefficient mass and control at a_n are unproved. All established sign/exclusion ranges are unchanged.

Exploration turns used: 0 of 3 consecutive unresolved exploration turns; the pole and Liouville tests give a new obstruction, including optimal scalar damping. No RH candidate.

Next action: Prove or refute an O(1) bound on the sum of absolute grouped coefficients of S_r(a)/|ζ(1+1/sqrt(r)+ia)|²−1, using normalized Euler-factor ratios on the Mellin contour.

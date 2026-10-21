# Approved actual Wronskian second-moment attempt

Working target: the exact TARGET in the prior SPECIALIZE assessment
`drafts/literature/2026-10-08-wronskian-second-moment-calculation.md`.
This draft saves unfinished reasoning; no conclusion is established yet.

Main gap: global actual-theta positivity and total L367 margin.
Intermediate target: H^{-1} integral_[H,2H] Wcal^2 = c log H + o(log H), c>0.
Downstream use: quantitative nondegeneracy for a separately covered localization test;
common-zero resets and the global positivity gaps remain independent.
Continue only with a positive explicit coefficient and all projection/tail errors below
log H. Stop this implementation if either retained component stays uncontrolled at that scale.

Inputs read: L366 (1), L368 (3),(5), L380 (3)-(8), complete L320 strip proof,
and the omitted primary comparison/duplicate/failure evidence. Young's direct primary
PDF was retrieved for Lemmas 4-5 and (3.4), without a new literature assessment.

Proposed calculation, still to justify: use C from L380 (5), so Wcal^2=(|C|^2+Re C^2)/2.
Critical-line reflection gives |C|^2=|b/(T^2 L)|^2 |U' Z-U Z'-(b'/b)UZ|^2.
For C^2 extend bar U as zeta(1/2-i tau) and omega by the paired digamma
formula, then shift tau upward by i. L320 with R=1 and logarithmic-radius
Cauchy disks appears sufficient to bound vertical edges by O(H), and the
new horizontal edge has both zeta lines at 3/2. This needs a full proof.

For the modulus term, fixed Euler heads give rational twists. Evaluate both
Young diagonals together on unequal-radius alpha,beta contours, where alpha+beta
is bounded away from zero. The candidate leading mixed derivative is
(gcd(h,k)/sqrt(hk)) (log t)^3/3; no coefficient is adopted without this check.
Use h=k=1 jet moments to control every right-line tail before removing the head.
Smooth nonnegative moment comparisons must bracket the sharp dyadic interval.

Unresolved at this checkpoint: diagonal error uniformity and shift degeneracy,
endpoint jet bounds, smooth bracketing, full tail transfer and explicit coefficient.

## Completed attempt

The full argument, hypotheses, exact coefficient and retained error estimates are
canonical in `lemmas/L381-actual-wronskian-dyadic-second-moment.md`.
The working proposals above are preserved as the initial checkpoint, not current
unresolved mathematical claims: the coefficient, projection, tail and endpoint
arguments are now supplied there, subject to a separate critical audit.

Outcome: ADVANCE / RESEARCH / REPRODUCTION. The coefficient is
ζ(5)ζ(3)^2/(96π^2 ζ(6))>0, from the full gcd collision sum. Both functional-equation
diagonals precede unequal-radius Cauchy differentiation; the same-height projection
average is O(1); fixed-head height and smoothing limits precede infinite-head removal.
No mathematical script or numerical certificate is used.

This is local specialization progress, not a claim of an original moment theorem
or progress on the missing global positivity itself. The next target is a separate
critical audit, with coverage recorded as REVIEW_REQUIRED. Essential inputs are
L381, L380, L368, L366, L320 and Young Lemmas 4-5/(3.4). No additional zero
assumption is introduced. Common-free localization and all main positivity/count
gaps remain unresolved.

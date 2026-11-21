# Fourth-order complete-theta comparison — step400

Approved target: Test the r=4 full-B cumulant comparison uniformly for all integers m>=M4 and u>=0, seeking explicit M4>=7, a positive signed base and relative complete-theta error below 1/2.

Use the unchanged pre-invocation EXPLORE assessment
`drafts/literature/2026-11-04-fourth-order-large-smoothing-comparison-review.md`.
Main gap remains actual-Xi all-degree positivity. This fixed-order
comparison could give uniform smoothing control, but general order,
exceptional coefficient transfer and Xi signs remain independent gaps.
Continue on an explicit all-m, all-u bound below 1/2; unpaid regimes
require refined input, and an isolated onset failure does not refute
eventual comparison. No new source approval or cross-notebook input.

Coverage and prior failures: reuse step398's full-B source comparison,
L769's exact signed representation and 19/72 lower factor, and L019's
kernel. L767/L768 are only fixed-pair precedent and are not inputs to
the new estimate. The direct Conrey–Ghosh transfer stop remains in
force. Existing files and unfinished work are preserved.

Unfinished reasoning saved before lengthy estimates: put y=1/x and
h_j(y)=y^4 q_j(1/y). The normalized alternant is det[h_j(y_l)]/Delta(y),
and its base is P(x)/prod(x)>19/72. The theta perturbations are smooth
and flat at y=0. Newton divided differences should bound the complete
alternant error by C^3 norms, retaining cancellation at coincident
points and permitting a very small bound when every x_l>=A.

For the remaining mixed regime, change the positive reference integral
to unordered x variables. Its density is proportional to
prod_j(log(x_j/x0)^(m-4) x_j^(5/4) exp(-x_j)) times
prod_(i<j)((log x_j-log x_i)(x_j-x_i)), where x0=pi exp(2u).
For x0<=A, condition on three coordinates. Among the four intervals
[2A,3A], [4A,5A], [6A,7A], [8A,9A], at least one stays distance A/4
from all three coordinates (expand each interval by A/4 first).
Comparison to that interval should suppress the conditional mass
x<=A by rho^(m-4), rho=log(A/pi)/log(2A/pi)<1, with explicit finite
cost independent of the conditioned coordinates and u. Union over
four points. All constants, complete theta sums, divided-difference
bounds and integral transformations still need checking; no theorem
or onset is asserted in this saved plan.

Completed outcome: the saved plan closes the stated quantitative
comparison, subject to independent review. The full proof is canonical
in `lemmas/L770-fourth-order-uniform-complete-theta-comparison.md`.
It gives M4=16000 and relative error<2^-117<1/2 uniformly over
every larger integer m and every u>=0. The small-height event has
reference-measure probability<2^-318; the complete normalized
alternant error is globally<2^160 and <2^-120 when all x_l>=128.
The proof includes the full infinite theta sum and arbitrarily close
nodes. These are proved analytic bounds, not sampled evidence.

`scripts/cumulant-comparison/uniform-fourth-order-constants-400.json`
records 112 passing exact finite recurrence/constant checks and no
failures. Its final bound and failure list were inspected in full.
The mathematical proof, not a preview or numerical certificate, supplies
the infinite quantifiers. The prior noncertified diagnostic is unused.

Outcome ADVANCE / RESEARCH / POTENTIALLY_NEW means a local quantitative
input not matched by the recorded source review; it certifies no
originality beyond those sources. This remains development of the known
cumulant program. No fixed-order smoothing conclusion resolves the
general-order cost or exceptional coefficient interface. L769 and L770
are unaudited, and no RH candidate is claimed.

Continuation: critically test the same approved target by auditing L769
and L770, especially the exact signed formula, reciprocal alternant,
complete C^3 tail estimate and conditional localization. The prior
assessment and its exact COVERED_TARGET remain unchanged and adequate;
no additional source review is nominated. The new explicit bound needs
an essential conceptual audit before further route expansion. No
justified creative central-gap target is manufactured from this
fixed-order result. Its general-order extension is not preapproved.

# Negative discriminant measure — step 41 working checkpoint

Approved target: the unchanged quantitative negative-set action in
`drafts/literature/2026-10-10-negative-discriminant-set-measure.md`
(prior SPECIALIZE). This is a RESEARCH / REPRODUCTION proof attempt.

Main gap: global actual-theta mixed positivity. Intermediate test:
establish the complete normalized discriminant second moment
H^(-1) integral |Delta|^2 = O((log H)^4), then obtain negative physical
set measure at least c H/(log H)^2 from audited L388. The downstream
use is to constrain concentration of the negative mean; eventual sign,
pencil margin and common-zero counts remain separate open problems.

Read audited L370 and L388 in full, and relevant exact definitions and
ordinary-jet bounds in L366/L367/L368/L380. Narrow local searches found
only the existing measure proposal; prior grid and sharp-source failures
remain parked and do not concern this continuous-height moment.

Planned application, not yet a completed proof: f=F_0/A is a constant
sign times Hardy Z. The physical P_j retain A'/A and A''/A. Known
fixed-order Hardy fourth moments should give integral |P_j|^4 bounded
by C H log^4 H for j=0,1,2. Complete V_j are uniformly bounded by
L366 (2). L370 (3), with no divided-function differentiation, should
then bound |Delta|^2 by a fixed multiple of sum |P_j|^4. Apply
Cauchy–Schwarz only on the measurable negative set, using L388's full
all-H negative mean. Stop this certificate if any retained term exceeds
that budget; certificate failure would not disprove the measure target.

Unresolved work: write and check the Hardy phase identification, all
ordinary product derivatives, pointwise polynomial bound and measure
argument. Essential inputs: L366, L370, L388, Bui–Hall Theorem 3.
No RH, simplicity, noncoincidence, independent phases, eventual D sign
or common-zero bound is assumed. No complete RH candidate is proposed.

## Completed application

The working plan is now completed in canonical L389. The constant
Hardy branch sign, both ordinary envelope derivatives and every order-two
response jet are retained. The exact polynomial gives
|Delta|^2<=300 K^4 sum_(j=0)^2 |P_j|^4, with fixed K. Known Hardy
fourth moments give the required O(H log^4 H) bound. L388's mean and
Cauchy–Schwarz on the negative set give c H/log^2 H for all sufficiently
large real H. The threshold test succeeds; constants are existential.
No source theorem is reproved. Separate critical review is pending,
with its new assessment recorded as REVIEW_REQUIRED.

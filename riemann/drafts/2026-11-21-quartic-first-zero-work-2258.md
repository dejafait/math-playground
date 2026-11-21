# Fixed quartic test2258: saved setup

Approved target: assessment2256, exactly K(u)=exp(-u^4-u^2), first
positive cosine-transform zero in(0,8), curvature only at u=1.
The main gap is actual-Xi all-degree mixed positivity. The possible
use is testing a generic shape invariant for repeated real-zero
removal; actual-K hypotheses, iteration and the all-degree interface
remain independent gaps. A positive curvature lower bound refutes
the invariant; a nonpositive upper bound settles only this fixed point.
No parameter, point or search-cap changes after the result.

Fixed numerical setup before evaluation: composite Simpson on[0,4]
with2048 panels; the shifted integral uses the same mesh on[1,4].
Frequency census mesh1/32 up to8, then at most10 bisections of the
first sign-change cell. Whole-interval derivative bounds, complete
tails and rational trigonometric Taylor errors will be recorded in
the certificate, using70-digit outward Decimal intervals. Backend
contracts are correct CPython integers/Fraction, libmpdec directed
basic operations, correctly rounded HALF_EVEN exp and neighbor steps;
they are explicit assumptions, not independently verified software.
No sample or diagnostic is a proof of the first-zero condition.

Analytic obligations: every K derivative is a polynomial times K;
strict logarithmic curvature includes0. Apply Tuck's strict decreasing
sine-amplitude theorem to K(u+t), pay all derivative tails, use the
root for G'(0)=0, and the ODE for all odd origin derivatives and the
entire quotient identity. C919m is a template/contrast, not an input.
All unfinished prior work is preserved; no cross-notebook theorem.

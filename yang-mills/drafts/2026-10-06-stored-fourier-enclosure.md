# Stored Fourier arithmetic enclosure — bounded working note

STEP_ID: YM-20261006-052-stored-fourier-enclosure

The approved combined-response target is unchanged. Its bounded intermediate
test is to discharge L035's Fourier-input hypothesis using L036's exact
quadrature bound plus stored-minus-exact-rule errors below 5.93e-12 and
8.79e-12. Inputs: L008, L034–L036 and the degree-144 Integrals implementation.
The full response, other pairing classes, nonlinear jets, L019 compensation,
tensor sensitivity and weight/arithmetic enclosures remain unresolved.

Use the existing outward integer arithmetic at scale 10^180. Enclose all roots
of P_144 by rational sign brackets, verify disjointness and total degree,
and enclose weights by 2/((1-z^2) P'_144(z)^2). Certify pi with Machin's
formula and alternating arctangent sums. Evaluate rho and trigonometric
phases with outward Taylor bounds and exact doubling identities. Compare
every stored complex transform to the enclosed exact four-panel rule;
reflection/conjugation reduces exact-rule evaluation only, while both signs
of every stored frequency are checked. Store complete root, weight and
transform evidence. A failed enclosure is evidence against this precision
or method, not a sign or a response result. Passing supplies only the actual
coefficient input, not the downstream sensitivity contraction or response.

Existing L034 scalar propagation fails at binary64-scale assumed errors
(ATTEMPTS/016). L035 supplies the sharper conditional modewise propagation;
L036 certifies the exact quadrature alone. No duplicate stored-transform
enclosure was found in those canonical results or histories 049–051.

Continue if both actual margins pass for every h and |n|<=224. Otherwise
record the failing frequency and bound, then select a concrete arithmetic
repair or abandon this comparison. Reuse the unchanged SPECIALIZE source
assessment; this reproduces standard quadrature/interval techniques for
the exact local representatives, not general flow renormalization.

The first execution failed to resolve a bisection sign at scale 10^80.
Increasing the scale alone exposed wrapping in polynomial evaluation on
width-1e-40 root intervals: the resulting derivative denominator included
zero. The repaired implementation uses scale 10^180 and root intervals of
width at most 1e-90. Both failures are arithmetic enclosure failures; neither
is mathematical evidence that the requested coefficient budget is false.
This reasoning was checkpointed before completion; the completed outcome
is recorded below and in the canonical result.

## Arithmetic proof obligations for the running comparison

For integer endpoints scaled by S, addition/negation are exact;
multiplication uses the extrema of all four endpoint products with
floor/ceiling division by S. Division uses the extrema of all four
rational endpoint quotients and is permitted only when zero is excluded
from the denominator. Thus interval induction encloses each expression.

P_144 is evaluated from P_0=1, P_1=z and
j P_j=(2j-1)z P_(j-1)-(j-1)P_(j-2). Every saved rational root bracket
has opposite endpoint signs, so contains a root by continuity. Disjointness
of 144 brackets and degree 144 prove that these are all roots and each is
simple, without trusting the NumPy proposals. Standard Legendre identities
give P'_144=144(P_143-zP_144)/(1-z^2), and the standard Gauss–Legendre
weight formula gives w=2/((1-z^2)(P'_144)^2). Evaluating these on the whole
bracket encloses the actual root weight; a denominator including zero fails.

Machin's identity pi=16 arctan(1/5)-4 arctan(1/239) uses the principal
real arctangent. Each arctangent is between its alternating partial sum
through j=79 and that sum plus term j=80. Exact rational evaluation and
outward rounding give the pi interval. The identity follows from the
tangent addition formula and 4 arctan(1/5)-arctan(1/239) in (0,pi/2).

For positive-panel nodes, rho=1 on (0,5/2). On (5/2,3), both u=9-x^2
and v=x^2-25/4 are positive and the exact ratio is evaluated with
outward exp(-1/u), exp(-1/v). exp(-t) is range-reduced to t/2^k<=1/8,
bounded between alternating Taylor sums of degrees 61 and 60, then
enclosed through k squarings. All endpoints and denominators are checked;
fixed-scale underflow is bounded outward, not deleted by a machine cutoff.

Likewise reduce a nonnegative phase to theta/2^k<=1/8. The cosine sum
through power 60 and sine sum through power 61 end in positive terms;
subtracting the next term gives lower bounds. All term magnitudes decrease.
Propagate these intervals by cos(2t)=cos(t)^2-sin(t)^2 and
sin(2t)=2sin(t)cos(t), always using old values on both right sides.

The exact four-panel rule is reflection symmetric: Legendre parity and
the weight formula map every root and weight to its negative partner.
Consequently F_0^Q(n)=2 sum_(positive panels) w rho(x) cos(omega n x),
F_1^Q(n)=2i sum_(positive panels) w x rho(x) sin(omega n x). Negative
frequencies are their conjugates. This symmetry is used for the exact
rule only. Every stored transform at both signs is separately compared
as an exact dyadic complex number. If its real/imaginary differences
have interval absolute bounds d_r,d_i, then complex error<=d_r+d_i.
The certificate records all 898 comparisons. L036 supplies the separately
established integral-minus-exact-rule bounds for the final triangle inequality.

The saved audit recomputes all root signs, all weights and all positive-panel
nodes/cutoffs, checks weight positivity and that sum w encloses 2, verifies
the complete frequency set and exact table hex values, and recomputes every
saved comparison and margin. It does not independently reevaluate the
trigonometric transform sums; those rely on the generating interval induction.

## Completed outcome

[L037](../lemmas/L037-stored-fourier-transform-enclosure.md) is the canonical
statement and proof. The generator and all-record audit pass, with no
failed comparisons. Stored-minus-exact-rule errors are below 8.643e-14
and 1.233e-13, versus 5.93e-12 and 8.79e-12. Including L036 gives
errors below 1.565e-13 and 3.333e-13, versus 6e-12 and 9e-12.
This discharges only L035's coefficient hypothesis for the saved hexadecimal
table; exact sensitivity and the remaining tensor evaluator stay open.
The local advance reproduces standard interval methods and certifies
neither a sign nor the combined Ward coefficient. Continue with an
enclosure of L035's exact full-time sensitivity, using the certified table
and keeping all modes, components and exact parity exclusions.

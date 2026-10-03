# Persistent-root puncturing calculation

Date: 2026-10-03. One mathematical attempt on the exact target approved in
the SPECIALIZE assessment `drafts/literature/2026-10-03-persistent-root-puncturing.md`.

## Gap, proposed use, and test

The four-omission cell for the pinned RS[F_(97^20),H,8] model permits
fifteen bad parameters. L010 excludes persistent coordinate locators;
the aim is to cover that excluded class when D is a nonzero polynomial.
A bound at most fifteen would resolve this class, leaving the
nondegenerate sixteen-count case, identically singular pencils and July
ABF26 correspondence unresolved. The actual global bounds are still
10/q and 69/q. The failed full-orbit and blocked four-block routes are
preserved and are not used here.

Continue if all original bad parameters, including singular ones, can
be controlled after puncturing with a combined count at most fifteen.
An auxiliary closeness bound or a transfer that discards input failure
does not suffice. A counterexample to that transfer, or a combined
estimate above fifteen, would reject that version of the mechanism.
The existing fixed-four-support pencil, with q close parameters and
only four bad ones, is a required check.

## Reasoning saved before checks

Fix a persistent root x. The weight-four locator identity in L010's
proof uses no nonvanishing assumption on the coordinate locators.
It implies x belongs to every weight-four error support. At a
singular decodable parameter the error has weight at most three.
Thus deleting x always leaves at most three errors for the punctured
length-15, dimension-8 code, including every singular bad parameter.

The covered finite bound for that auxiliary code specializes to twelve:
n'=15, R'=7, r'=3, and 15*(8-3)/(3*(8-6))=25/2.
Alternatively, the covered BCHKS Theorem 1.3 applies to thirteen close
parameters at radius 3/15: its threshold is 25/2, and joint distance
is at most (13/12)*(3/15). Integrality would then put both punctured
residual inputs on at most three common coordinates.

The unresolved transfer issue has a possible dichotomy. If a decoded
original support loses input failure after deleting x, interpolation
would put both original residual inputs on a fixed set of at most four
coordinates. Every original bad parameter on such a family must cancel
an active affine coordinate, suggesting a bound of four. Otherwise all
original bad parameters should transfer to the punctured support event,
where the covered bound is twelve. The support sizes, uniqueness, and
the fixed-family count still need to be written out and checked; these
are working statements, not a completed proof.

All sources are reused from the ready assessment. The auxiliary MCA
bound is known mathematics; only the persistent-root transfer and
combined original-support count are the proposed specialization. Mathlib
coverage is not checked. No challenge-level candidate is claimed.

## Completed result and decision

The full proof is saved in
[L011](../lemmas/L011-persistent-root-puncturing-bound.md). It gives
at most twelve original bad parameters, below the required fifteen,
for every pair in the approved persistent-root class over F_(97^20).
The transfer dichotomy is the decisive step: loss of failure even once
puts the entire original pair in a fixed four-coordinate residual
family and bounds its whole bad set by four. Otherwise every original
bad parameter transfers to the length-15 support event, whose known
bound specializes to twelve. There is no separate singular-parameter
allowance to add to either count.

The imported input is BCHKS Theorem 1.3 and its joint-proximity
interpretation. Its hypotheses specialize to degree seven, length
fifteen, Delta=8/15 and radius 1/5. Thirteen close parameters exceed
the threshold 25/2 and force residual inputs on at most three common
coordinates by integrality. Counting affine coordinate cancellations
then contradicts thirteen bad parameters. This reproduces the auxiliary
twelve bound also covered by the assessed LC1–LC2 statement; it does
not reprove a general proximity theorem or construct a new decoder.

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/persistent-root/check.py`
passes independent interpolation checks on every original support of
size at least twelve and every punctured support of size at least twelve.
The fixed-support regression has original bad set {24,32,48,96},
punctured bad set {24,32,48}, and all 97 parameters decodable in
both codes. Thus automatic bad-set inclusion is actually false:
parameter 96 loses failure at the removed coordinate, and is covered
by the fixed-family branch. The confluent-moment test has three
persistent roots and one singular bad parameter, zero, whose weight-one
error omits the chosen persistent coordinate. Its failure survives
puncturing. A codeword translation gives the same event and checks
that the proof is about residuals rather than literal sparse inputs.
These finite examples do not establish an extension-field maximum.

Outcome: ADVANCE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION:
POTENTIALLY_NEW. The known auxiliary bound is imported/applied; the
full persistent-root transfer/count is not matched by the checked
source statements, and originality is not certified. This closes one
excluded class in the main model gap. Nonpersistent equality, D
identically zero, the overall sharp radius and July ABF26 correspondence
remain open. Global bounds stay 10/q and 69/q, and STATUS stays
IN_PROGRESS. The next direction is the identically singular class;
its different hypotheses require a new assessment before calculations.

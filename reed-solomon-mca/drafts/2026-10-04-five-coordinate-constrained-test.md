# Five-coordinate actual-pencil test

Date: 2026-10-04. One mathematical attempt on the unchanged actual-pencil
COVERED_TARGET in the saved
[SPECIALIZE assessment](literature/2026-10-03-nonpersistent-resultant-equality.md).
The adequate source coverage is reused without browsing.

## Gap, intermediate target and stopping test

The pinned four-omission cell has global bounds 10/q and 16/q, while its
budget allows fifteen. The intermediate test restricts actual moment
pencils to the span of five coordinate columns. This includes every
pencil through two four-error representatives whose supports intersect
in three coordinates, and allows arbitrary extension-field weights.
Excluding sixteen in this class would restrict the support geometry of
any remaining equality witness; finding sixteen would decide unsafety
for the pinned model. Other classes and the July correspondence remain
open. L013 treats prescribed weights on a five-set, whereas this test
allows every line in its error space. The stopped full orbit and the
parked four-block/July target are not being retried.

For a five-set A and its eleven-point complement J, a nondegenerate
pencil in its error space has a unique representative z(T) supported
on A, with five affine coordinate weights. At most five finite
parameters can cancel a weight. At all remaining parameters a
four-error representative must be disjoint from A: otherwise the
difference from z(T) would be a codeword of weight at most eight,
contradicting minimum weight nine. Its support C is a four-subset of J.
The corresponding codeword is a scalar multiple of
Q_(J minus C)(X)=product_(y in J minus C)(X-y), of degree seven.
Thus its five values on A specify a projective point
p_C=[Q_(J minus C)(x)]_(x in A) in P^4(F_97).

There are 330 such points. Eleven would have to lie on one projective
line to permit sixteen total parameters. A line through two distinct
points is defined over F_97 even when the original inputs range over
F_(97^20). This permits an exact finite configuration test of the
five-set class, rather than a sample of its weights. Multiplication by
H identifies five-sets in free orbits of size sixteen, leaving 273
representatives. The point reduction and field passage require proof;
computation alone will not be presented as a general count theorem.

The planned bounded calculation enumerates all point pairs for those
273 representatives and groups their normalized Plucker coordinates.
A line with m distinct points contributes exactly binom(m,2) pairs.
The test stops after this finite configuration is enumerated. Any
selected actual pencil must additionally pass L010's determinant,
same-support, resultant and exact F_(97^20) checks. If no useful
restriction or witness emerges, record EXPLORATION and reassess the
mechanism; do not infer a global fifteen bound from a sample.

## Saved unfinished reasoning

The needed distinctness follows from minimum weight nine: if p_C and
p_D were proportional, their codewords agree on A after rescaling;
their difference would be supported on C union D, of size at most
eight, so would vanish. Their seven-element zero sets would then
coincide, forcing C=D. All five point coordinates are nonzero.
Projective lines can therefore be grouped without repeated points.
A dimension-one syndrome pencil needs separate treatment. Equality
has no lower-weight point and sixteen distinct supports by L010.

No enumeration, actual-pencil conclusion or improved count was asserted
in this initial checkpoint. The completed test follows.

## Completed reduction and finite test

[L015](../lemmas/L015-five-coordinate-projective-reduction.md) proves the
five-set reduction, distinctness of the 330 rational points, and field
passage for arbitrary extension-field weights. Its unconditional bound
is |B(a,b)|<=5+M(A). A sixteen-count pencil with two supports intersecting
in three coordinates would therefore require eleven collinear points in
the configuration of their union. A rank-one pencil has at most one bad
parameter under the nonpersistent hypotheses. The argument does not
assume a numerical value of M(A).

The command `python3 scripts/coefficient-feasibility/five_coordinate.py`
enumerates 14819805 point pairs across all 273 free multiplicative orbits,
covering every one of the 4368 five-sets. The
[orbit records](../scripts/coefficient-feasibility/five-coordinate-orbits.jsonl)
retain each representative, line-size histogram and a maximal line's
Plucker coordinates and supports. The
[summary and actual-pencil certificates](../scripts/coefficient-feasibility/five-coordinate-result.json)
report 265 representatives with maximum five external points and eight
with maximum six. No configuration has the eleven needed for sixteen.

Pairs are grouped by their normalized ten two-by-two minors. These
determine the two-dimensional row space: normalize the first nonzero
minor and recover its row-reduced basis, so equal keys describe the same
projective line. Distinctness ensures a line of m points contributes
exactly binom(m,2) pairs. Every pair total is 54285 and every stored
maximum is independently checked by point membership. A separate Python
pair enumerator reproduces the entire mask-539 configuration:

| Points on line | Number of lines |
| --- | ---: |
| 2 | 49318 |
| 3 | 114 |
| 5 | 461 |
| 6 | 1 |

The orbit reduction is proved in L015, and the script independently
checks the disjoint union of those orbits against all five-subsets.
This is an exact finite configuration test after a proved field
reduction. Its class exclusion has explicit computational dependence;
the handwritten theorem gives the reduction and threshold, not an
analytic proof of the enumerated maximum. It does not exclude general
pencils whose syndromes require more than five coordinates.

## Eleven-parameter witness and redundancy check

The maximal line for A={1,8,22,27,89} yields an actual prime-field pencil
with eleven bad parameters. Its input weights (a_x,b_x) on sorted A are
(1,96), (67,3), (9,46), (47,66), (55,39); both words vanish elsewhere.
The five cancellations are {1,10,16,23,86}, and its six additional bad
parameters are {0,7,11,49,57,87}. Its exact minors satisfy the inverse
recurrence audit with rank fifteen, and all coordinate locators are
nonzero and squarefree. Its product has degree 64 and fails all 48
remaining fourth-power residuals. The residual after removing the
eleven known fourfold roots has an eight-degree simple factor and a
four-degree factor of multiplicity three; it was not squarefree as an
initial auxiliary assertion expected. Those extra locator incidences
are retained and have multiplicity below four. The corrected factor
audit and exact root checks exclude them from the bad set.

An independent original-event check examines all 2517 qualifying
supports, and modular Frobenius/GCD checks determine the bad root
polynomial in F_(97^20). It has degree eleven and already splits over
F_97. Manufactured quartics were not used as candidate moments.

The selected line is covered by the existing local L013. For
B={18,33,50,85,96} and J={12,47,64,70,75,79}, its words are
a=85*a_0+46*b_0 and b=27*a_0+66*b_0, where a_0,b_0 are L013's
prescribed inputs. The change-of-input determinant is 3!=0. Thus the
new point generator found a partition and a different affine chart
of the known two-block family, rather than an independent sixteen-count
mechanism. Its exact count should use L013 by specialization.

[C013a](../lemmas/C013a-eleven-challenge-partition-specialization.md)
checks the partition's ratios {54,55,55,55,55,11}. The size-four fiber
at ratio 55 has roots {47,64,70,75}, and its monic degree-five polynomial
has residual factor X+20. L013 gives exactly A union B union {77} for
its original chart, over the full target field. This supplies the
unconditional local lower bound eleven independently of the finite
point enumeration. The script separately audits that chart's actual
locator, power residuals, exact-field roots and original support event.

## Outcome and continuation decision

Outcome: ADVANCE for the explicit, proved improvement of the achieved
lower count from ten to eleven. STEP_KIND: RESEARCH;
STEP_CLASSIFICATION: REPRODUCTION. Standard power/resultant tools are
imported, the point reduction specializes existing MDS/moment geometry,
and the witness is an application of the established local L013. No
claim of progress beyond the checked literature or certified originality
is made. The finite search helped locate the explicit application.

The global interval is now 11/q–16/q, still straddling the allowable
fifteen. The finite configuration result stops this five-coordinate
generator as a sixteen-count search. The next independent constrained
candidate test should use two four-error representatives whose union
has at least six coordinates, solve one further support constraint,
then apply the unchanged actual-pencil equality and field gates. It is
within the existing ready COVERED_TARGET; no new source need arose.
No such next calculation is performed here.

Consecutive uninformative mathematical turns used: zero after this
local advance; resultant-target mathematical attempts: three; this
five-set test: one. The stopped orbit/two-block generators and parked
four-block/July source failures remain preserved. No complete resolution
candidate appeared; STATUS stays IN_PROGRESS. L015 and C013a record
Mathlib coverage and its qualifications; no library lookup was needed.

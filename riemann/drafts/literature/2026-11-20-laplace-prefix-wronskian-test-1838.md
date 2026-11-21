# Actual Laplace prefix test — nomination1838

TARGET: Attempt one analytic all-prefix Wronskian test for (1,k(1,sigma),k(2,sigma)) on [1,2] using C032n's normalized heat evolution, retaining the full divisor; stop if the derivative signs cannot be separated rigorously.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1838 completed1837's exact-kernel discovery and duplicate/failure comparison; queries, inspected local ranges and primary proof cases are recorded in drafts/literature/2026-11-20-laplace-interpolation-source-notes-1838.md. No matching actual-kernel prefix-sign theorem was located; no originality claim.
SOURCE_EVIDENCE: Novaes--Torregrosa, UAB July2015, printed p2 all-prefix ECT criterion and Section2 pp5-6 (5)-(9)/nonvanishing division-derivation proof, https://mat.uab.cat/dpt/Publ/prep/p13_15.pdf ; C032n imports the normalized Gaussian heat identity from Nolen Section2.3 (3.17), pp14-17, https://math.stanford.edu/~ryzhik/STANFORD/STANF227-10/notes227-09.pdf ; reuse1745/C032m/n's Haslinger Theorem2.39 pp67-68 https://www.mat.univie.ac.at/~has/scriptneu.pdf with its actual majorant hypotheses. Source-notes1838 records the reused TP and numerical comparisons.
COMPARISON: The classical ECT theorem covers the conditional implication after C^2 width regularity and every prefix nonvanishing hypothesis are proved. C032n supplies normalized b evolution and first width regularity; C033g/k's odd-kernel signs supply neither of the new nonconstant prefix tests. No automatic Laplace/exp/heat TP transfer is available from the inspected sources.
GAP: Justify the required width-regularity specialization and test W(1,k(1,.)) and W(1,k(1,.),k(2,.)) over the full closed interval, retaining complex paired zeros, full R integral and normalization. Neither sign nor nonvanishing is assumed. Actual det M and quantitative inverse/weights/TV remain unknown.
REASON: Essential framework coverage is ready for one bounded analytic attempt at an independent interpolation gap. This is a new continuation requiring separate approval next turn; it does not authorize a mathematical application within review1838.
SCOPE: Exactly C033w/l's actual qualified probability transform k(s,sigma)=exp(-b_sigma(sqrt(s))) at s=1,2 and widths [1,2], with C032m/n and the C032q identification retained. No odd-kernel substitution, new zero list, changed evaluator or unassessed external theorem.

## Classical input and kernel-specific obligations

Use the cited closed-interval C^r, r>=n ECT theorem with n=2 and
the ordered functions u0=1, u1=k(1,.), u2=k(2,.). Test all three
prefixes, retaining endpoints. No reproof of that classical theorem
or the Gaussian heat identity is needed. Do not use the source's
isolated final-Wronskian sentence to omit lower prefixes. Source
Section2's denominators require nonvanishing throughout the interval.

C032m gives joint continuity and complex-argument holomorphy, not by
itself second width regularity. C032n supplies its exact normalized
heat evolution, first width derivatives and fixed complex derivatives
on a neighborhood containing [1,2]. C033k's Gaussian/p/R/E regularity
argument through (5) is supporting reasoning only; its analytic proof
is unaudited and its odd-kernel relative bounds cannot be substituted.
Explicitly justify whatever additional width derivatives, noncompact
spatial majorants, removable values and primitive exchanges are used.
Do not differentiate a bound as though it were an identity.

Try the actual positive-real lift at arguments1 and sqrt(2) through
the normalized b evolution before taking absolute remainder bounds.
Retain its normalization term, full spatial integral and every divisor
member. Derive and record any needed kernel-specific Wronskian formulas
only in the approved research attempt. No cancellation identity,
monotonicity, orientation or scale is asserted by this assessment.
Using the existing normalized evolution is the proposed change of
interface; do not replay1746's independent ratio-jet boxes or refine
its cover. No large scalar evaluation or mathematical script is needed
for the nominated analytic attempt.

## Bounded test, use and stop rule

One coherent analytic attempt. Seek a rigorous proof that both
nonconstant prefix Wronskians are nowhere zero on [1,2], with the
required C^2 width regularity. If obtained, explicitly justify the
classical implication for the fixed mass-and-two-observation matrix
at widths1,3/2,2 and track its column order. No quantitative margin
or confluent determinant estimate is required for this target.
A proof of only one prefix can be retained as a useful intermediate
input while the other remains open; it is not matrix nonsingularity.

A rigorously established zero or opposite signs of one prefix refutes
this sufficient criterion only. It does not prove the fixed distinct-site
matrix singular. An enclosure containing zero is inconclusive: record
the attained estimate, required strict threshold and lost correlation,
then park this attempt. Repetition requires a materially new input or
signed identity, not a finer grid or a renamed criterion. If an essential
unassessed external input becomes necessary, save the reasoning and
return to REVIEW_REQUIRED before using it.

The plausible use is removing one qualitative solvability gap for
C033w's mass-one/two-observation interpolation. Inverse norm, accurate
entries and m, exact weights, TV<=2 and full observations stay unpaid.
L030-L032/C032a actual-Xi positivity, signed height, cancellation and
realization remain independent. Rump1797 and1798/1837 stops persist;
C034a is arithmetic support only, not a sign premise.

Retain all actual divisor/conjugation/multiplicity, ordinate0 exclusion,
strict-strip/gamma>14, counting/through100/retained-real-zero,
reciprocal-square-tail, heat-positivity/separate-fixed-j-error,
both fixed-v1, zero-drift/killing and Gaussian-half-variance qualifications.
No full source-wide or finite-zero verification is claimed. Matching
Mathlib coverage remains unchecked/unknown. This is established-framework
development, not a justified creative mechanism at the main RH gap.

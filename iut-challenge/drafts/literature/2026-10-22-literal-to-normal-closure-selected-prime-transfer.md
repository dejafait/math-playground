# Literal-to-normal-closure selected-prime transfer — source scope approved

TARGET: Test whether every prime ell>=7 satisfying (P2) over G_o also avoids all rational pole orders and satisfies all-place q-order coprimality over C_o, without assuming j-integrality at ell.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step399 reused step398's exact P2/P3 comparison and step394's general local sources; read L090/L092 hypotheses and degree statement, L098 reduction proof through full-torsion semistability, L099 imported statements and height/ramification proof, the step390 reduction assessment and ATTEMPTS/035. No new discovery search or matching transfer theorem is claimed.
SOURCE_EVIDENCE: Reused inspected IV April 2020 Proposition 1.8(v) statement p.19/proof p.20 and Corollary 2.2(ii) proof pp.44-46, especially P2 p.45; GenEll Definition 3.3/Remark 3.3.1 p.17; Silverman AEC second edition VII.5.5 pp.197-199, residue-two proof A.1.3/A.1.4(b) pp.412-413 and C.14.1(b,d) p.445; Kedlaya equation (3) p.2 and Theorems 1-2/relevant proof pp.3-4; Milne ANT v3.08 Theorem 3.34/full Galois proof pp.59-60, Corollary 7.42/Remark 7.43 p.124 and Exercise 4-2/solution pp.83,155. Direct links and applicability limits below.
COMPARISON: The inspected semistability theorem requires complete prime-to-residue torsion, not normality of the base number field; the general height and valuation theorems allow every finite Q_p-extension, including p=ell. Galois efg is available for C_o/Q, not asserted for G_o/Q. L099's extra integrality premise prevents importing its conclusion unchanged; its cited methods cover the new conditional specialization.
GAP: A later research turn must apply these sources at every actual G_o-place, derive rational pole-order avoidance from the explicit P2 premise, and transfer coprimality to every actual C_o-place, including a possible ell-pole. This review proves none of those conclusions; no essential source coverage is missing for that attempt.
REASON: Separate approval of the changed conditional target is complete. Reuse the ready general sources for one RESEARCH / REPRODUCTION attempt; no general reproof or further discovery is justified unless an actual applicability gap appears.
SCOPE: Same arbitrary L089 survivor, all six full-coordinate L090 models in the fixed closure, C_o=G_o^nor over Q, S={p:v_p(j(E))<0}, and ell>=7 prime satisfying IV P2 at every finite G_o-place. No assertion of ell-integrality or full initial theta-data; no changed fields or ell-division-field heights.

## Proposed later mathematical test

Original finite B>=A is the main gap. The intermediate target would
decide whether normal closure preserves the source's height-avoidance
clause even when ell is not known to be outside S. Its downstream
use is a partial prerequisite for a possible repair; it cannot remove
the independent integrality/support issue or L092's relative excess.

Essential local inputs are L089, L090, L092, L098 and L099. The latter
two are method and hypothesis comparisons, not unconditional premises
after their ell-integrality assumption is removed. Use their inspected
general reduction and height sources to check the actual new scope.
The review should determine whether full rational 15-torsion permits
the same semistability argument over G_o, whether the general Tate
height formula covers every actual G_o-place and extending C_o-place,
and whether the actual extension/ramification degrees permit the
required prime-to-ell transfer. Preserve nonsplit reduction and integer
downstairs normalization; a rational invariant alone does not justify
silently transporting a height without that check.

Continue to a later RESEARCH / REPRODUCTION attempt only after this
scope approval. That attempt must establish both rational pole-order
avoidance and all-place coprimality, including a possible p=ell case,
from the explicit P2 hypothesis. A missing source hypothesis or an
actual counterexample stops the claimed implication. No construction
of an actual selected prime or finite-exception avoidance is part of
this conditional target; those remain separate applications.

Use the complete [step398 comparison](2026-10-22-height-selected-prime-avoidance-comparison.md)
for exact primary links, quantifiers, duplicates and failed retrieval
limits. Reuse that adequate evidence rather than repeating discovery
or ATTEMPTS/035 authentication. Source-version/def= qualifications,
actual height selection, ell-integrality, selected/theta data, exact
generation/repairs, native input/action/factorization/pilot transport
and essentiality remain unresolved. Mathlib coverage is unchecked.
No new lemma or mathematical script has been written in this step.

## Step399 — separate applicability review

LITERATURE_REASON: The gate requires a separate comparison for the changed
scope: literal G_o heights and possible residue characteristic p=ell,
without L098-L099's ell-integrality assumption. Existing theorem readings
are adequate; this is not renewed discovery or authentication.

The following primary statements are reused at their inspected versions:

- [IV April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 1.8(v), p.19 and full proof p.20: full rational prime-level
  torsion of level at least three invertible in a complete DVR gives
  semistability. Corollary 2.2(ii), proof pp.44-46, supplies the exact
  conditional P2 input: ell divides no nonzero local curve height at
  any finite place of F, here the literal G_o. P3 does not supply
  ell-integrality. Current author/journal authentication remains unresolved.
- [Silverman, AEC, second edition (2009)](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves),
  VII.5.5 pp.197-199 and A.1.3/A.1.4(b) pp.412-413: perfect-residue-field
  potential-good/integral-j criterion, including residue two. Use this
  only after semistability; arbitrary potentially good twists need not
  have good reduction. [C.14.1(b,d), p.445](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf)
  supplies the Tate comparison and the unramified quadratic splitting
  extension in the nonsplit multiplicative case.
- [Mochizuki, Arithmetic Elliptic Curves in General Position, journal
  52 (2010)](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf),
  local setup pp.16-17, Definition 3.3 and complete Remark 3.3.1 p.17:
  the curve height uses the surjective integer valuation downstairs;
  over a split extension its Tate order is divided by the extension's
  ramification index. The convention is extension-independent.
- [Kedlaya, Introduction: the Tate curve, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
  equation (3) p.2, Theorems 1-2 and relevant proof pp.3-4: the complete
  convergent integral j-series and geometric parameter comparison over
  finite Q_p-extensions. These statements impose no inequality between
  p and an independently chosen test prime ell. A split isomorphism
  requires split multiplicative reduction; do not omit the nonsplit case.
- [Milne, Algebraic Number Theory v3.08 (19 July 2020)](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Theorem 3.34 and complete Galois proof pp.59-60, Corollary 7.42 and
  Remark 7.43 p.124, Exercise 4-2/solution pp.83,155: prime decomposition,
  Galois efg, local degree ef, restriction of integer valuations and
  multiplicativity of ramification. None requires tame absolute bases
  or p different from ell.

### Applicability obligations for the approved attempt

L090 defines G_o with both coordinates of every geometric 15-torsion
point. This is the required input for testing complete rational level
five torsion away from p=5 and level three at p=5 over every actual
G_o-completion. The semistability source does not require G_o/Q to be
Galois. The later proof must explicitly check that completion retains
the full geometric torsion sets, rather than citing L098's conclusion
outside its hypotheses. L098's method is a duplicate reduction method,
not an unconditional theorem input after deleting ell-integrality.

For heights, both G_o and C_o completions are finite Q_p-extensions
with finite perfect residue field. The inspected Tate/GenEll statements
therefore cover their local curve heights, including nonsplit reduction.
At a rational j-pole the later proof must supply the whole-series
valuation comparison, the split-extension normalization and positivity
of the actual downstairs height before invoking P2. No point height,
selected singleton, or later ell-division-field order is substituted.

For ramification, L092 records the same C_o as a finite normal closure
and its exact degree 1105920=2^13*3^3*5. The Galois hypothesis needed
for Milne's efg statement is thus supplied for C_o/Q. The later proof
must apply it at each actual C_o-place and compare its prime factors
with ell>=7. It must not use degree divisibility for nonnormal G_o.
This scope comparison licenses the use of that theorem; no all-place
coprimality or rational-avoidance conclusion is proved in this review.

In particular p=ell is inside the general sources' scope. The proposed
argument uses level-five torsion there, rather than ell-torsion; the
Tate series and ramification theorems have no prime-to-p hypothesis
on the independent integer being tested for divisibility. A possible
ell-pole must remain in S for the later proof. Neither the premise
P2 nor this source coverage asserts that no such pole exists.

### Decision, duplicates and stopping test

SPECIALIZE approves exactly TARGET for a later RESEARCH / REPRODUCTION
attempt. The sources cover the general ingredients, not this completed
field-specific transfer. Reproof of their general statements is
unnecessary; only their explicit specialization and elementary
implications are justified. L099's ell-integrality premise is retained
in its canonical file and its conclusion is not imported unconditionally.
L061/L084 use different fields and remain method comparisons only.
ATTEMPTS/035's authentication failure remains parked. No fresh source
retrieval was attempted; previous optional retrieval failures do not
create a new essential coverage blocker. Mathlib coverage remains
unchecked, with no absence claim.

Continue if the later proof checks full torsion, actual downstairs
heights, rational pole orders and prime-to-ell ramification at every
required place, including p=ell. Abandon the implication if a required
source hypothesis or normalization fails; save the precise failed case.
The main gap remains original finite B>=A. A successful transfer would
clear only a height-avoidance prerequisite for a possible normal-closure
repair. Actual prime selection, ell-integrality and native selected
support, L092's factor-four relative excess, exact generation/full
initial data, marked input/action/factorization/pilot and essentiality
remain unresolved. No lemma, mathematical script or new mathematical
result was produced in this source review.

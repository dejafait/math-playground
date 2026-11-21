# Full signed support source comparison1760

19 November 2026. Literature-only completion of review1759's exact
target. Main gap: L030-L032/C032a actual-Xi all-degree positivity.
Intermediate target: the support value over all real signed Borel eta
on W=[1,2], eta(W)=1, |eta|(W)<=2, for a given continuous real finite
Laplace payoff. Its use would be to specify the continuum extrema
needed by C033l/n's separator interface. No support identity, new lemma,
numerical margin or RH result is proved in this turn.

## Primary statements and relevant proof cases

Richard F. Bass, *Signed measures*, Chapter12, version 4 November2011,
[author-origin university extract](https://webspace.science.uu.nl/~kraai101/SignedMEasures),
Theorem12.8, complete proof and (12.1), printed p97: Jordan decomposition
on an arbitrary measurable space gives unique mutually singular positive
parts; total variation is their sum. The proof constructs them by Hahn
restriction and proves uniqueness using null symmetric differences.
This includes arbitrary finite signed Borel measures, without a density
or finite-support premise. Exercise12.2, p98, defines signed integration
and asks for its domination inequality; it is not a supplied proof.
Use C032q's existing bounded signed-integration result for that interface.
The PDF text extraction loses minus signs; do not import its damaged
literal displays. A p98 screenshot timed out; the complete extracted
exercise was available, and no essential theorem is source-blocked.

Theo Buhler and Dietmar A. Salamon, *Functional Analysis*, 11 May2016,
[Example1.3.7, printed p28](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf#page=36):
read the complete example. For second-countable compact Hausdorff M,
the real dual of C(M) is isometrically all finite signed Borel measures
with variation norm. Its discussion explicitly uses Borel regularity
and Hahn decomposition. Its underlying Riesz proof is cited, not given
there; reuse source-notes1748/1542 rather than claim a fresh proof audit.
W satisfies these hypotheses. This checks the existing full-class
interpretation; dual representation is not needed to redo Jordan
optimization. The standard named extreme value theorem applies to
continuous real functions on the nonempty compact W; no effective
extremum-computation theorem is asserted or needed for that existence.

Lenaic Chizat, *Sparse optimization on measures with over-parameterized
gradient descent*, Mathematical Programming194 (2022),487-532,
published online17 March2021,
[Appendix A, Proposition A.1 and complete proof](https://doi.org/10.1007/s10107-021-01636-z):
read the signed lifting in (17), both directions of the proposition,
and the proof's variation comparison for arbitrary positive-pair
representations, with equality for Jordan parts. This is useful
confirmation that arbitrary signed measures can be handled by positive
parts. Its optimization is TV-penalized; it does not state our joint
mass-one, hard-cap support identity. No convergence algorithm,
complexity bound or constrained equivalence is imported from it.

The probability-distance mismatch in notes1752 is reused: Charalambous
et al.(2014), Problem2.1 and Theorem4.1, optimize probabilities within
distance of a fixed probability. That is not this signed norm cap.
Their proof was not read anew and their formula is not imported.

## Exact applicability difference, reserved for research

Decision: SPECIALIZE. The essential general measure-theory coverage is
available; no inspected theorem states the exact requested support
value. This is a routine application of known tools, not a novelty
claim. A separate mathematical turn must impose mass and variation on
the Jordan masses simultaneously, bound the linear payoff over the
whole signed class, and prove equality by an admissible measure.
It must handle zero negative mass and constant payoffs separately where
necessary: coincident extremizers do not give two mutually singular
nonzero Jordan parts. Do not replace TV<=2 by TV=2 without justification.
These are proof obligations, not established reductions or formulas.

For the finite Laplace payoff, C033l gives continuity on the entire
closed W and reality of each positive-argument coordinate. Coefficients
can have either sign. Keep C032q's signed integration and C033n's
rational stability; neither supplies the missing exact support value.
The desired discriminator is an upper bound valid for every Borel eta,
matched by a feasible attaining measure, including constant payoffs.
Failure of either direction or a need for an extra constraint stops
the specialization at that exact missing premise. No grid computation,
analytic derivative estimate, general computable maximum or new source
theorem is required by this bounded target.

## Search scope, duplicates and preserved stops

Queries actually issued: `"signed measures" "total variation" "mass"
"support function"`; `"signed measure" "supremum" "oscillation" norm
mass`; `"signed measures" "Jordan decomposition" optimization total
variation constraint`; `"signed measure" "mass one" "total variation"
maximum minimum`; `"signed measures" "mass constraint" "linear"
variation`; `"signed measure" "3/2" "1/2" "maximum"`. These searches
did not locate an inspected exact hard-cap/mass-one formula. No
originality follows. Chizat was followed to its primary appendix;
other optimization/moment/transport hits and computable-Jordan material
were leads only and are not essential sources. The parked general
computable-maximum source was not retried.

Narrow local checks: C033l full proof and relevant scope; C032q's
source and bounded-integration interfaces; C033m/n's support exclusions;
source-notes1542/1748/1752/1756; the two stop records1571/1576. No exact
support evaluation occurs in these paths. Stop1571 concerns coarse
independent boxes for another dictionary; stop1576 concerns literal
evaluator cost. Neither is refuted or reopened by this source review.

Unresolved: actual separator data, certified continuum extrema,
coefficient-amplified error below a witnessed gap, useful runtime,
uncapped variation, cancellation, moments and actual-Xi realization.
All divisor/conjugation/multiplicity, excluded ordinate zero,
strip/counting/first-zero/through100/retained-real-zero, heat, fixed-v1,
half-variance and C033i/j/C032s residual/error qualifications remain.
No external preprint or zero-data audit was performed. Full matching
Mathlib coverage is unchecked/unknown; no absence claim is made.

This review changes the missing-source decision to a bounded ready
specialization, with its new continuation in assessment1760 requiring
separate supervisor approval. Mathematical exploration usage is zero.
No justified new central creative mechanism arose within this narrow
scope; the independent signed-height/theta input remains missing, and
discovery1747's parked batch is not repeated or relabeled creative.

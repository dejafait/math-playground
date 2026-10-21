# Ready continuation: actual Wronskian second moment

TARGET: Compute the dyadic second moment of L380's normalized actual Wronskian, testing c log H+o(log H) with an explicit c>0 and retaining the complete projection and infinite tails.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed primary comparison and scoped duplicate/failure checks in 2026-10-08-wronskian-second-moment.md; the target and hypotheses are unchanged apart from proceeding from comparison to its proposed specialization.
SOURCE_EVIDENCE: https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf (Young, DOI 10.1007/s00013-010-0199-9); Young, Arch. Math. 95 (2010), 539–548, Lemmas 4–5 and complete Lemma 5 proof pp. 542–543, (3.4) Cauchy differentiation p. 541; complete L320 (4)–(5) strip proof; L368 (5) absolute right-line jets; reused DLMF 25.2.1 and sector-qualified gamma inputs through the canonical local results.
COMPARISON: Known finite rational-twist shifted moments cover one part; the actual projection, coefficient, uniform tail passage and same-height contour estimate are the identified family-specific difference and require a proof.
GAP: No value or positivity of c, complete o(log H) error, mean-square tail transfer or dyadic unsmoothing is established.
REASON: One bounded specialization can test nondegeneracy after the stopped first-mean signing certificate; reproduce the standard moment inputs by citation and derive only their applicability and the residual family-specific estimates.
SCOPE: Fixed actual F_0,G,A and Wcal of L380, positive real t, ordinary real derivatives, H tending to infinity; no RH, simplicity, noncoincidence, independence, discriminant sign or common-zero count bound.

The direct-source recovery review on 2026-10-08 retains SPECIALIZE
coverage for this unchanged target. No mathematics is derived in this review. The full
hypotheses, precise citations, inspected proof cases and comparison
limitations are in the preceding source assessment, which must be
reused without a broad literature refresh.

Essential inputs: L366 (1), L368 (3),(5), L380 (3)–(8), and L320
(4)–(5) with its strip proof. L369 (16) is only a scope contrast.
Use the exact complex expression in L380 (5) and every term of its
real-projection square. Preserve both functional-equation diagonals
and every reduced-ratio collision. Do not replace that square by half
a modulus square without estimating the other term.

The proposed single attempt uses a fixed finite Euler head, small
complex shifts and Cauchy differentiation of the uniform moment,
a separate analytic contour test for the same-height component, and
unweighted jet moments for uniform tail control. All these
specializations, including derivative normalization and weight
variation, need proof. In particular, a fast gamma carrier is not an
admissible Young weight. Check the α+β degeneracy and exact analytic
representations before applying Cauchy's theorem. Justify the height,
head-removal and smoothing limits in their stated order.

Continue if the full coefficient is explicit and positive and every
retained error is o(log H); a rigorously useful weaker nondegeneracy
estimate may instead be recorded with its actual scale. Stop this
implementation if an uncontrolled projection contribution or tail
remains at the proposed main scale. Do not treat a positive diagonal
as a signed total or repeat the first-mean certificate. No coefficient
is guessed in this assessment.

Downstream use: quantitative nondegeneracy for a later sign-set or
localization test. Common-zero resets remain possible; a second
moment alone gives no common-free zero. Global positivity, total L367
margin, low indices, heights above forty and endpoint margin remain
unresolved. Full matching Mathlib coverage is not checked. The later
calculation is intended as REPRODUCTION, with no originality claim.

## Direct-source recovery review

On 2026-10-08 the direct PDF above was opened successfully. Checked
the weight conditions (2.1)–(2.3), the Cauchy argument after (3.4),
Lemma 4 and all of Lemma 5's proof (pp. 541–543). Both off-diagonal
orderings are treated by symmetry and integration by parts; both
functional-equation diagonals are retained. The apparent singularity
in the auxiliary G at α+β=0 is still an applicability obligation,
not permission to differentiate separate singular expressions.

The existing primary comparison and duplicate/failure checks are reused;
no changed hypothesis calls for another search. The direct URL repairs
the reported process defect only. The finite-head specialization remains
a test, and neither its cross-term estimate nor infinite-tail transfer
is asserted proved. No lemma, script, DAG edge or argument was changed.
The completed recovery is LITERATURE / NOVELTY_UNCHECKED / STALLED;
the next mathematical attempt is intended as REPRODUCTION.

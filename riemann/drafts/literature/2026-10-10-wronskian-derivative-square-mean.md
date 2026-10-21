# Derivative-square mean coverage review

TARGET: Compute the dyadic mean of L370's derivative-square term w'(t)^2/(T^4L^4), testing its log H leading coefficient with complete projection, tails and sharp endpoints.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-statistic/Wronskian and derivative twisted-moment searches found no inspected matching theorem; targeted local searches found only this proposed statistic and the preserved recovery decision, not a completed duplicate. Reused stronger-result comparisons in the L381 assessment; queries and unread leads below. No novelty inference from search failure.
SOURCE_EVIDENCE: Young, A short proof of Levinson's theorem, Arch. Math. 95 (2010), 539–548, DOI 10.1007/s00013-010-0199-9, https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf, published ten-page copy, (2.1)–(2.3), Cauchy paragraph after (3.4), Lemmas 4–5, (4.1)–(4.5) and complete Lemma 5 proof, printed pp. 540–543, directly retrieved this turn; reused audited L381 sections 2–4 and Separate critical audit, audited L386 sections 1–4 and Separate critical audit, and their cited DLMF 25.2.1 and 5.15.1, 5.15.8–9 (version 1.2.8) inputs.
COMPARISON: Young covers the needed small-complex-shift finite-twist input; audited L386 already supplies ordinary order-two moments, signed unsmoothing, full derivative tails and order-two height-rectangle bounds. None evaluates this derivative-square statistic: exact carrier algebra, both real-projection contributions, moving normalization and coefficient remain family-specific proof obligations.
GAP: Essential source coverage is ready for one logarithmic-scale attempt, not a proved reduction or asymptotic. The complete derivative-square projection, leading coefficient and o(log H) error ledger remain unproved; no total discriminant mean or lower-order expansion is approved.
REASON: The changed square statistic lies within the already audited order-two toolkit and can be tested independently of the parked sharp-Hardy source and grid-count imports. Cite Young and derive only the precise application in a later research turn.
LITERATURE_REASON: The statistic changed from wk to w' squared; this separate review checks its required jet, projection, tail and endpoint scope against reusable Young/L381/L386 coverage.
SCOPE: Fixed actual L366 pair, f=F_0/A, g=G/A, w=fg'-f'g, ordinary real derivatives, T=1+t and L=log(2+t), sharp [H,2H] average, logarithmic leading scale only; no RH, simplicity, noncoincidence, physical D<=0, common-zero upper bound or phase independence.

## Main gap, target and use

Global actual-theta mixed positivity remains the main gap. This target is
one missing term in L370's exact discriminant decomposition, independently
of the audited L386 residual. Its plausible downstream use is a later
comparison with that residual and L370's bounded envelope curvature.
That assembly is outside this approval. Even a total mean would not
supply a pointwise sign, total L367 margin or RH resolution.

Essential input IDs: L370, L366, L368, L380, L320, audited L381 and
L386. Use their fixed actual functions and ordinary derivatives.
L386's negative residual mean is a prospective comparison input,
not a value of this square mean. No cross-notebook input is used.

## Primary theorem and source comparison

[Young's published paper](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
printed pp. 540–543, was retrieved at the hypotheses and relevant proof
cases before further source comparison. Lemma 5 requires positive integer
twists h,k, hk<=T_Y^(2 theta), theta<1/2, small complex shifts of size
O(1/log T_Y), and smooth weights between zero and one, supported in
[T_Y/4,2T_Y] with derivatives bounded at scale T_Y/log T_Y. Setting
T_Y=2H fits fixed relative endpoint transitions and every fixed Euler
head eventually. This does not permit a growing head.

Both functional-equation diagonals and both off-diagonal orderings in
the complete Lemma 5 proof were read. The Cauchy paragraph after (3.4)
requires holomorphic uniform errors. The auxiliary singularity at the
shift sum zero must be removed before differentiation. The apparent
reversed ratio in extracted (4.4) is not used: retain (4.1), the large-mn
decay in the proof and L381's audited integration-length qualification.
Import this theorem; a reproof would add no required input.

The stronger-source comparisons are reused from
`drafts/literature/2026-10-08-wronskian-second-moment.md`, the inspected
Bettin–Chandee–Radziwill Theorem 1 and Section 3.1 and Bui–Hall
Proposition 1 comparisons. Longer unshifted polynomial coverage supplies
no holomorphic derivative error; the particular mollifier result does
not authorize the present right-line factor or real projection. Their
hypothesis differences remain unchanged. The parked Das–Pujahari source
was not requested again; its missing proof cases are retained in
`ATTEMPTS/2026-10-10-parked-sharp-hardy-source-and-recovery.md`.

## Finite covered reduction and application obligations

L370 explicitly identifies w'=fg''-f''g; its statistic uses only ordinary
jets through order two. L386 (9) supplies the exact complex Wronskian
expression, and its carrier/reflection inputs are fixed. A later attempt
must write the complete derivative expression from those fixed inputs,
including the carrier and polynomial derivatives. No expression for it
is derived in this literature turn. Differentiating an averaged
w-square asymptotic is not a permitted reduction.

For the opposite-height contribution, audited L386 (2)–(8) already
covers all ordinary jet pairs j,k<=2, including complex cross moments,
both diagonals, all gcd collisions and the removable shift singularity.
The required matrix of moments is finite. Ordinary derivative phases
must be retained, as must powers of the slowly varying carrier.
L386's moving-divisor comparisons are available tools, not an evaluated
coefficient for this target. The calculation must justify every
replacement with the exact T^4 L^4 denominator.

For the same-height contribution, L386 (15)–(18) and its audit supply
holomorphic reflected critical jets through order two, full right-line
jets through order two, the carrier and its first derivative, pole
exclusions, and estimates on both full vertical edges and the entire
top edge. These are the required derivative orders for L370's w'.
The later attempt must construct its own complete holomorphic numerator
from these jets and check its normalized edge bounds. The available
comparison is the order-two strip/Cauchy envelope and absolutely
convergent top edge of L386; there is no essential new source case.
This identifies a testable projection mechanism, not a proof of its
bound. Never insert a fast gamma phase into Young's weight or discard
the same-height contribution of a real square.

For tails and sharp endpoints, audited L386 (4), (6)–(7) supplies positive
critical-jet norm bounds, nonnegative endpoint majorants and complete
right-line tails rho_0,rho_1,rho_2. The square attempt must transfer the
norm of the full derivative expression and its difference from a fixed
head using these bounds and Schwarz. It must also control endpoint
cross moments through the positive majorants, rather than order a
complex integrand. Let H grow at fixed smoothing width and head, then
remove smoothing, then the head; any other order needs its own proof.
No shrinking-width or head-uniform source theorem is presumed.

Thus every required derivative order and projection/endpoint tool has
inspected coverage. Exact algebra, degree counts, normalized bounds and
coefficient summation remain research work; approval is for one attempt,
not a claim that those obligations have been met.

## Search, duplicates and recorded failures

Queries submitted this turn: `zeta Wronskian derivative squared mean
critical line shifted zeta second moment`; `"A short proof of Levinson"
Young complex shifts Lemma 5`; `"zeta" "Wronskian" "mean square"
derivative`; `"twisted second moment" "derivatives" zeta Young`.
The direct Young paper was inspected. Search leads on fractional joint
moments, logarithmic-derivative moments, shifted Fourier kernels, local
extrema and Dedekind-zeta moments were not read as primary theorem inputs
and are not coverage or evidence of an exact match. Secondary snippets
are discovery only. No novelty or theorem absence is inferred.

Targeted searches of local literature, ATTEMPTS and history for the
square-statistic terminology found this proposal and its recovery
selection, no completed evaluation. Read L370's definition, the relevant
L381 and L386 moment/projection proofs and audits, and the named parked
route. L381's w-square and L386's wk results are distinct statistics;
L380's stopped first-mean signing and the stopped direct grid imports
do not evaluate this term. Their evidence is preserved. Continuous
height averaging does not repair a discrete common-zero bound.

## Decision and continuation test

SPECIALIZE approves the unchanged TARGET for one later bounded
REPRODUCTION attempt. Continue if its logarithmic coefficient is
explicit with a full o(log H) error, or record a precise informative
certificate failure. A projection, tail or endpoint error surviving at
log H scale stops this implementation. Cancellation in a later total
comparison does not authorize a lower-order target without new review.
No coefficient is predicted or calculated here.

Global mixed positivity, total L367 margin, physical D<=0, actual
common-zero upper count, low indices, heights above forty and endpoint
arithmetic margin remain unresolved. Full matching Mathlib coverage is
not checked. This source review changes readiness only; no lemma,
mathematical script, DAG edge or PROOF.md argument is changed.

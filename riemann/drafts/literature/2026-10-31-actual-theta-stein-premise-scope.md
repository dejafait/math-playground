# Independent actual-theta Stein premise: completed source comparison

TARGET: Assess whether Csordas's theta shape theorem and Bagnoli--Bergstrom's hazard theorem cover nonincrease of the Stein kernel for the normalized full L019 theta density, checking coordinates, support, and tail hypotheses.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the discovery queries and comparison in 2026-10-31-theta-stein-monotonicity-transfer-review.md. Rechecked L019/L233, C233b and the L604 statement and their two named stops. New narrow query: Csordas Varga "Moment inequalities and the Riemann hypothesis" pdf Theorem 2.1; found the author-hosted original, but its scanned theorem was not readable through the text interface.
SOURCE_EVIDENCE: Directly read Csordas arXiv:1309.0055v2 (21 February 2014), https://arxiv.org/pdf/1309.0055v2, equation (4.2), Theorem 4.1(i)-(v), p. 10, Theorem 4.2(a)-(b) and Remark 4.3(a), p. 11; Bagnoli--Bergstrom, 4 March 2004, https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf, Theorem 3/Corollary 2 and proof, p. 4, Appendix 8.2 Remark 4 and the complete log-concave case of Lemma 4, p. 25. The original 1988 source and access limitation are recorded below.
COMPARISON: The exact kernel definitions match by K(u)=4 Phi(u/2) for u>=0. Csordas supplies log-concavity of Phi(sqrt(s)); Bagnoli--Bergstrom supplies nondecreasing hazard for a normalized positive C1 log-concave density on (0,infinity). These cover the source inputs for a reciprocal-hazard specialization, not a stated full-theta Stein theorem or a Fourier-sign transfer.
GAP: A later mathematical step must write and verify the change of variables from the centered full-line Stein numerator to the square-root-coordinate survival integral, retaining all factors, and justify normalization, finite tails, positivity, smooth extension and the endpoint u=0. No such specialization or monotonicity proof is derived in this literature turn.
REASON: Exact source comparison resolves the essential coverage gap: the needed shape theorem is in the squared coordinate, rather than ordinary log-concavity of the original full-line density. A later specialization is justified without repeating the stopped two-point sign argument.
SCOPE: Only source coverage of Stein nonincrease on the positive half-line for normalized full L019 theta. The unchanged first-sign transfer, integrated L604 remainder, higher signs and RH are outside this assessment.
LITERATURE_REASON: Actual-theta applicability was explicitly left outside the ready generic two-point scope; its exact coordinate, support and endpoint mapping is essential unread application evidence, not a reason to repeat the completed generic search.

## Completed comparison, 31 October 2026

The main gap is actual-Xi all-degree positivity at unbounded heights.
This review addresses only an independent theta premise. A later valid
premise plus a separate sign-transfer theorem could address L233's first
Xi sign; higher signs remain open. C233b excludes only its fixed mixture,
and L604 excludes pointwise positivity of its particular remainder.
Neither result blocks this independent applicability check.

### Exact coordinate and hypothesis comparison

Term-by-term comparison of the displayed definitions in L019 and
Csordas (4.2) identifies K(u)=4 Phi(u/2), u>=0. This is the
source-coordinate identification, not a Stein monotonicity proof.
The proposed auxiliary density is proportional to Phi(sqrt(s)) on
(0,infinity). It is **not** the distribution of U squared: the latter
would introduce a Jacobian factor. Applying the hazard theorem directly
to the original full-line density would concern an unweighted tail and
would leave the weighted Stein numerator unmatched.

For the auxiliary density, the required checklist is positive finite
normalizing integral, C1 regularity on its open support, and log-concavity.
The cited shape and decay statements cover those hypotheses in scope;
L019 also records integrable superexponential tails in the local
coordinate. The positive half-line is connected and its right endpoint
is infinite. The later proof must explicitly carry the tail substitution,
normalization cancellation and endpoint limits. No finite-endpoint
extension of the hazard theorem is assumed. The centered full-line
Stein ratio is the one already cited in C233b/L604 from Saumard v3,
Section 2 (6); evenness, finite first moment and positive full-line
support must be checked in the application. Nonincrease means on
u>0, with continuous extension at zero; an even nonconstant ratio is
not asserted to be nonincreasing on the whole real line.

### Precise inspected sources and qualifications

[Csordas v2](https://arxiv.org/pdf/1309.0055v2), pp. 10-11,
(4.2), Theorem 4.1 and Theorem 4.2, gives the matching kernel,
positivity, even analyticity, derivative decay and strict concavity
of log Phi(sqrt(s)) for s>0. Part 4.2(a) concerns the logarithm
of its integrated tail; it alone is not a claim about the ratio of
that tail to its density. Part (b) is the relevant density premise.
These are named theorems imported as stated, without reproof.

[Bagnoli--Bergstrom manuscript](https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf),
p. 4, Theorem 3 and Corollary 2, requires a C1 log-concave probability
density on an interval and gives log-concave survival and nondecreasing
hazard. Read the corollary proof and p. 25's complete concave Lemma 4
case: its positive C1 function has right integral and endpoint limit.
The displayed inequality before the final conclusion gives
f' times survival + f squared >=0. The next printed line reverses
that sign and refers to F/Remark 3; those are apparent typographical
errors, inconsistent with the preceding inequality and Remark 4.
The theorem and corollary agree with the preceding correct argument.
Only this concave case is needed; no convex-case import is made.

Followed Csordas reference [21]: Csordas--Varga, *Moment inequalities
and the Riemann hypothesis*, Constructive Approximation 4 (1988),
175-198, Theorem 2.1, [author PDF](https://www.math.kent.edu/~varga/pub/paper_161.pdf).
The PDF opened as 24 scanned pages with no readable text. Screenshot
requests provided no inspectable image in this interface; direct shell
retrieval failed DNS. Its theorem/proof is therefore an **unread original
lead**, not independently audited evidence. This does not block importing
the explicitly stated Csordas v2 Theorem 4.2(b); no original-proof audit
is claimed. Its abstract/search preview was used only to locate it.

### Decision and next-step boundary

SPECIALIZE approves the source scope, not a newly derived result. The
remaining work is a routine mathematical application, not a new central
mechanism: establish the exact reciprocal-hazard identity including
coordinate constants, then invoke the hazard theorem and handle zero.
If the proposed identity or a necessary endpoint hypothesis fails,
record the discrepancy and stop this specialization. A verified premise
would not sign L604's remainder or establish any Xi sign. Full-result
Mathlib coverage remains not checked.

The separately saved specialization assessment receives a distinct
approval turn before mathematical invocation. This review derives no
new lemma and changes neither the DAG nor PROOF assembly.

## Superseded nomination (preserved)

## Relevance and bounded review

The main gap remains actual-Xi all-degree positivity at unbounded
heights. An independently verified theta premise would settle one
separate applicability question for a future generic transfer theorem;
it would not bypass the still-missing transfer. L604's pointwise stop
and C233b's fixed-model stop remain evidence, not premises of this
application. No cross-notebook input is proposed.

Read L019 only as needed for the exact kernel, coordinates, positivity
and decay, and use L233 for the stated connection to the first Xi
sign. Retrieve the named primary theorem hypotheses and relevant proof
case before any larger passages. Reuse the existing discovery queries
unless the actual hypothesis comparison reveals a specific missing
lead. Check whether citations suffice or identify precisely the
specialization still required; do not treat spatial shape as a Fourier
positivity theorem.

The continuation test is whether these named sources provide a valid,
fully specified route to this one premise. If so, prepare the exact
specialization for a later approved mathematical turn. If a necessary
hypothesis fails or no implication is supplied, record that exact gap
and park the source-only application. Do not infer a theorem from the
source titles or silently assume the desired Fourier sign.

This original nomination did not derive new mathematics and was not approval.
Full-result Mathlib coverage remains not checked. The appropriate next
work is literature comparison; a future covered specialization would
be reproduction or a known import according to what the sources state.

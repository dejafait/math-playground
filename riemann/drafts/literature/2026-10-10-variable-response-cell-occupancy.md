# Variable response-cell occupancy — proposed specialization coverage

TARGET: Test whether Trudgian's counting argument proves at least c T log T complete actual response cells (g_j,g_(j+1)] contain no full-strip zeta-zero ordinate, retaining the unresolved left endpoints.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The adjacent-response-grid review located the published empty-Gram-interval proof; scoped response/count assessments and L379/L383 failure records contain no matching variable-grid occupancy application.
SOURCE_EVIDENCE: Trudgian, Acta Arith. 148(3) (2011), 225–256, DOI 10.4064/aa148-3-2, Theorem 5.1 and complete Theorems 5.2–5.3 proofs pp. 242–244, with (35), Theorem 4.1 and (36) pp. 237–238; Korolev arXiv:1106.0516v2 Theorem 4/full proof pp. 17–18 independently confirms ordinary-grid occupancy and one-sided endpoint scope.
COMPARISON: Known results prove positive-proportion empty ordinary Gram intervals; only the bounded variable response phase, complete-cell endpoints and associated count balance need specialization, rather than a new shifted-S moment theorem.
GAP: No actual-grid occupancy theorem is proved yet; a successful half-open count would still leave its left endpoints, strict adjacent products and common-free Wronskian use unresolved.
REASON: Prepare a bounded specialization of an inspected proof mechanism after direct pair-sign import fails its applicability check; new ready coverage requires separate supervisor approval next turn.
LITERATURE_REASON: The changed conclusion is half-open all-strip occupancy on the exact variable grid, with endpoint nonvanishing deliberately left as a separate gap; the original pair-sign assessment did not cover this application.
SCOPE: Actual eventual consecutive G zeros from L366/L368/L372; all-strip zeros counted with full multiplicity, complete cells contained in [T,2T], T sufficiently large, existential fixed c>0; no RH, F_0 simplicity, noncoincidence or discriminant assumption.

This is source coverage for a proposed attempt, not a lemma or a theorem
application completed during this literature-only turn.

## Sources and import boundary

Use [Trudgian's published version](https://www.impan.pl/shop/publication/transaction/download/product/82370).
Theorem 5.1 reproduces Tsang's shifted-S moment theorem for fixed
a>1/2, T^a<H<=T, 0<h<1 and positive integer m. With
ell=log(2+h log T), it states

\[
\int_T^{T+H}(S(t+h)-S(t))^{2m}\,dt
=\frac{(2m)!}{(2\pi^2)^m m!}H\ell^m
+O\bigl(H(Am)^m\{m^m+\ell^{m-1/2}\}\bigr).
\]

Only m=1,2 and H=T are proposed for import. Retain the complete
displayed error and choose h=C/log T with a fixed sufficiently large
C; do not call the fixed-C expression an asymptotic with vanishing
relative error. The named source is K.-M. Tsang, *Some Omega-theorems
for the Riemann zeta-function*, Acta Arith. 46(4) (1986), 369–395,
Theorem 4, DOI 10.4064/aa-46-4-369-395. Its original PDF endpoints
returned 403; its proof is unread. The fully stated known input in
Trudgian Theorem 5.1 is the proposed citation basis, not a claim that
Tsang's proof was checked. No reproof of that theorem is proposed.
This coverage relies on the reproduced theorem, not on resolving those
access failures. If a later attempt needs stronger uniformity, that
changed input requires review.

Read the whole published 5.2–5.3 argument, including runs, their
exceptional neighborhoods, the fourth moment and the zero-count balance.
Its ordinary-grid conclusion is not imported as an actual-grid theorem.
The zero-count input is Backlund's formula, Trudgian Theorem 4.1 and
Titchmarsh (1986), pp. 212–213; retain S=O(log T), (36), sourced there
to Titchmarsh Theorem 9.4. Trudgian uses the right-hand S limit at a
zero but writes a strict inequality in his N definition; a specialization
must define its own consistent one-sided count and retain endpoint
multiplicities. Korolev's proof is a comparison, not a second essential
moment input. Neither cited paper covers the actual grid directly.

## Bounded specialization to test after approval

Main gap: global actual-theta mixed positivity and the total L367 margin.
Intermediate target: the exact occupancy statement in TARGET. Its
plausible use is to isolate many response cells with no interior F_0
zeros, before independently addressing left-endpoint common zeros and
strict signs. Neither that last step nor the Wronskian implication is
being derived or assumed here. Even success would not settle RH.

Essential canonical inputs are L366's fixed pair, L368's carrier and
right-line bounds, and L372's strictly increasing full phase, simple
crossings and bounded phase error. L379 fixes the existing Hardy
normalization; L380 is needed only for a later Wronskian application.
Preserve the exact beta(t)+eta(t); do not freeze it or transport
ordinary Gram-point signs. The proposed proof obligations are:

- Control S differences within a run of response cells each containing
  one full-strip zero, using the bounded phase correction itself.
- Bound the neighborhoods of the remaining cells using actual response
  spacing, and apply the two cited continuous moments with full errors.
- Compare full-multiplicity strip counts with complete response-cell
  counts, including incomplete boundary cells and one-sided endpoints.

These are obligations, not established estimates. Continue only if they
give a fixed positive c uniformly for all sufficiently large T. Abandon
this specialization if the variable correction or boundary budget cannot
be controlled at that scale. Keep a successful half-open theorem separate
from strict endpoint products; no o(1) common-zero count is assumed.
Do not change the test to another L383 shift or repeat L379's absolute
triangle bound. The earlier stops concern different certificates.

No matching full Mathlib theorem was checked. General measure/counting
or continuity infrastructure would be supporting coverage only, not this
zeta theorem. No novelty follows from the search. Classification for a
later successful specialization is REPRODUCTION, unless a genuinely
different uncovered mechanism changes the assessment.

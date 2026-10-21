# L096 critical application audit — coverage approved

TARGET: Independently audit L096's two primitive eleven-adic lifts and its reconstruction of both L095 systems.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the bounded exact-system searches in 2026-10-18-rational-factor-eleven-adic-solvability.md and the L095 audit assessment; read L096, the relevant L095 statement and identity, ATTEMPTS/043 and histories 319–321. No intervening independent L096 audit or additional theorem input was identified in these records.
SOURCE_EVIDENCE: Reused inspected Zábrádi, Notes for the course p-adic methods in arithmetic, 29 June 2022, Lemma 2.3 and Theorem 2.4, printed p.4, with their proof as recorded in foundations/17-local-power-hensel-inputs.md and the prior assessment; L095 supplies identity (4) and both exact systems. No fresh external retrieval or arithmetic replay was performed.
COMPARISON: The cited theorem supplies exact lifting under an error/derivative inequality, not the numerical hypotheses or reconstruction of these two points; independent checking of that specialization is justified. No new lifting method or integer existence claim is proposed.
GAP: Independently verify both exact polynomials, error and derivative valuations, uniqueness in the specified disks, common tuple reconstruction, nonzero unit coordinates and the local-only conclusion; coverage approval does not establish these facts.
REASON: All essential methods for this narrowly scoped audit are covered by the prior inspected sources. EXPLORE permits checking the explicit specialization without certifying its correctness or originality.
LITERATURE_REASON: The target changed from constructing local witnesses to independently auditing the newly written L096; this separate approval compares its actual inputs with the ready lifting and L095 coverage, without repeating discovery.
SCOPE: Exactly TARGET over Z_11, using L095, L096, foundations/17-local-power-hensel-inputs.md and the full eleven-lifts certificate; elementary exact arithmetic, polynomial identities, valuation tests and Hensel lifting only. No new global exclusion, classification of all local valuations or local-to-global implication.

## Reused theorem and its limits

Gergely Zábrádi, *Notes for the course p-adic methods in arithmetic*,
ELTE summer school, 29 June 2022,
[author PDF](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
Theorem 2.4, printed p.4 (PDF index 3), assumes f in
Z_p[x_1,...,x_m], an integral approximate root alpha modulo p^n,
and one partial derivative of valuation k with 0 <= 2k < n.
It gives an exact integral root congruent to alpha modulo p^(n-k).
The prior assessment inspected the theorem and its proof, which
iterates Lemma 2.3 in one variable while fixing the others. That
coverage is reused; no primary page was reopened this turn.

L096 claims the case p=11, n=1, k=0 with only a changing.
Its claimed uniqueness is an elementary difference-of-cubes argument,
separate from the quoted existence conclusion, and must be checked.
The audit must verify the actual integral polynomials and strict
valuation inequality rather than infer existence from residue samples.
No general cube-surjectivity assertion is needed. Clark's more general
Newton theorem and the unit decomposition are available background,
not additional essential inputs for this audit. No reproof of Hensel
is justified or proposed.

L095's audited identity (4), with its displayed Q,H, is the exact
reconstruction input. A polynomial identity over Z can be evaluated
over Z_11; the audit must check both substitutions and the cancellation
in system II using the same lifted a. Its global positivity and
coprimality requirements at other primes are not part of L096's local
claim. In particular C=6 is not an integer witness for L095's global
conditions. The local interpretation is explicit and does not assert
that every local point arises from a global rational direct factor.

## Duplicates, failures and downstream use

Histories 319–321 distinguish the completed L095 audit, the local-method
review and L096's construction. The construction's sixteen passing
checks are reported evidence awaiting independent audit, not a new
verification made here. The prior solvability assessment records the
bounded queries and relevant primary-source comparisons. Its Putz and
Pacetti–Villagra Torcomian limitations remain unchanged; neither source
supplies a coefficient-one global exclusion that supersedes this test.
No fresh novelty search is needed for an unchanged known lifting method.
Full matching Mathlib coverage remains not checked, not asserted absent.

The main gap is global integer elimination in the rational-factor branch
of ordered (3,5,11), with other algebra factors and residual signatures
also unresolved. The intermediate target is reliability of L096's two
local witnesses. A passing audit would validate retirement of standalone
eleven-adic nonexistence, preserving ATTEMPTS/043; it would supply no
integer solution or global compatibility. Historical local stops concern
specific mechanisms and do not ban combined global work.

## One approved audit, still unperformed

Read both complete records in
scripts/rational-factor/eleven-lifts-certificate.json and independently
check their load-bearing arithmetic against L095 and L096. Check all
coordinates, the exact complementary identities, error and derivative
valuations against the strict required inequality, the same tuple
throughout reconstruction, and uniqueness as claimed. Finite precision
alone is insufficient: the cited theorem must apply to the exact
polynomial. Existing scripts may be replayed in the research turn;
none was run or modified in this literature-only review.

Continue by certifying only exact primitive local existence if every
check passes. If a check fails, record the precise defect and its effect
on the local-solvability conclusion before deciding whether repair is
possible. Do not escalate precision to reopen standalone exclusion after
a valid exact lift. No lemma, mathematical script, DAG or argument was
changed, and no mathematical audit verdict was reached in this review.

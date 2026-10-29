# Quartic class-generator critical audit: source coverage ready

TARGET: Critically audit L135's Minkowski-bound class-group generator certificate, including exceptional-prime completeness and generation from bounded ideal representatives.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-instance generator assessment; compared L135 with L133/L134 statements, history/480–481 and ATTEMPTS/019,045,058; located and read Stevenhagen Section 12's explicit Minkowski factor-base generation statement.
SOURCE_EVIDENCE: Milne ANT v3.08 (2020-07-19), Theorem 4.3 p.70 and final proof p.81, Proposition 4.2 pp.69–70, Theorem 3.7 p.49, Theorem 3.41/Remark 3.43 pp.62–63 including proof, ideal correspondence pp.14–15; Stevenhagen (2008), Theorem 8.2/proof pp.229–230, Example 8.3 pp.230–231, Theorem 8.4/proof p.232, and Section 12 pp.244–245 opening factor-base statement.
COMPARISON: The ordinary-class generation implication is explicitly known, including unconditional use of the Minkowski cutoff; the audit must certify the exact L135 instance and exhaustive ideal lists, not discover or reprove general ideal theory.
GAP: No essential theorem coverage remains missing for the proposed audit; correctness of L135's arithmetic, completeness arguments, source-code implementation and binding to its final list remains unreviewed.
REASON: The new audit scope now has precise source coverage, including an explicit source for prime-ideal class generation; approval of scope is not acceptance of L135.
SCOPE: Exactly TARGET, with L133's fixed quartic field, audited L134's maximal order and L135's existing full certificate, replay, source programs and ledger. No relations, units, class number, descent, ranks or points.
LITERATURE_REASON: The supplied audit assessment was REVIEW_REQUIRED; this turn resolves its separate source-applicability gate using prior coverage and the newly inspected explicit generation passage.

## Relevance, reuse and prior failures

The main Beal gap is still exclusion of all residual primitive signatures.
On this route class relations, units, quotient ranks and point control are
unresolved. The intermediate target is critical validation of L135's finite
class-generator input, potentially useful for subsequent class relations
and supported descent. No complete route from this input to Beal is known.

The prior assessment `2026-10-25-pair-quartic-class-generators.md` remains
adequate for its unchanged field and hypotheses. No duplicate calculation
is requested. L135 claims the exact 32 ideals but expressly lacks a separate
critical proof audit; L134's audit concerns the integer ring, not that list.
ATTEMPTS/019 concerns an enormous degree-36 cutoff; ATTEMPTS/045 concerns
an unavailable full-class backend; ATTEMPTS/058 excludes a quadratic tower.
This audit neither repeats those tests nor relies on their failed mechanisms.
No cross-notebook input is used; unfinished L108 and all prior stops remain.

## Primary statements and applicable cases

[J. S. Milne, Algebraic Number Theory, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
Theorem 4.3 concerns integral representatives of ordinary ideal classes;
its final proof p.81 explicitly handles arbitrary fractional classes by
inverse-class cancellation. Proposition 4.2 gives multiplicative numerical
norms; Theorem 3.7 supplies unique ideal factorization in a Dedekind domain.
Theorem 3.41 assumes a power basis; Remark 3.43 relaxes that hypothesis
prime by prime using the discriminant ratio. Its proof includes repeated
factors and identifies residue degrees. Pages 14–15 give ideal correspondence
and the maximal-ideal/field-quotient criterion. Apply these to the integer
ring certified in L134, retaining the ordinary/narrow distinction.

[Peter Stevenhagen, The arithmetic of number rings, MSRI Publications 44
(2008)](https://library.slmath.org/books/Book44/files/08psh.pdf):
Theorem 8.2 and proof distinguish singular power-order primes; Example 8.3
shows splitting upon normalization. Theorem 8.4 requires regularity above p.
Section 12, opening pp.244–245, explicitly permits the Minkowski bound as a
prime-ideal class generating cutoff, and distinguishes the GRH-dependent
Bach bound. This directly covers the general generation claim; no GRH
input is needed here. It does not certify this quartic's evaluated list.

These passages were actually reopened, rather than inferred from search
snippets. Source versions agree with the prior assessment. The Section 12
passage supplies a direct citation previously absent from the assessment;
no broader reading of its class/unit algorithm or unread references is
needed for this audit. No new theorem search or novelty assertion follows.

## Exact audit contract for a later research turn

The following are review obligations, not conclusions verified this turn.

1. Bind L135's field, basis, multiplication table, discriminant and index
   to L133 and the accepted L134 data. Check the certificate and replay
   input hashes against actual files. A success flag is insufficient.
2. Review the sign-interval argument and rational bound comparison in
   L135; check signature, constants, integer endpoint and the complete
   rational-prime domain through the saved conservative cutoff 159.
3. At primes outside the power-order index, check every modular factor,
   multiplicity, irreducibility domain and omitted norm. Review the exact
   applicability of Remark 3.43, including the ramified repeated-factor
   case at 11. Review the containment-plus-dimension argument identifying
   each saved reduction with its claimed ideal.
4. At 2,3,5 review enumeration of every subspace of the full maximal-order
   algebra, duplicate freedom, invariance tests, all nonideal witnesses
   and every maximality/containment comparison. Do not substitute factors
   of the power-order polynomial or a sum(e*f) check for this exhaustion.
5. Review preimage lattices, pO containment, multiplication closure,
   determinants, norms, primality and exact identification with the 32
   ideals printed in L135. Completeness must cover excluded ideals too.
6. Critically assess the existing bounded-representative-to-generator
   argument using the cited sources, including the unit-ideal case.
   Generators alone give neither a presentation nor a class number.
7. Inspect producer and independent replay implementations and complete
   relevant certificate evidence, rather than treating check counts or
   previews as proof. Reuse prior arithmetic replay where adequate;
   document any selective additional check and its actual scope. Preserve
   cumulative accounting; any new mathematical implementation must be
   bounded under the existing calculation ceilings or separately reviewed.

Only the audit, not a new class-relation search, is approved as SPECIALIZE
for a REPRODUCTION research turn. General source theorems are imported;
instance verification is necessary because sources do not evaluate L135.
The test is whether all generation hypotheses, completeness claims and
final-list identifications survive critical review. On a failed claim,
preserve evidence and isolate the repair; do not use the generators as an
audited input. If an essential new theorem is needed, stop dependent work
for its own coverage gate. Acceptance authenticates only this partial input.

Mathlib coverage remains not checked, as stated in L135; no formal
verification or absence claim is made. No lemma, mathematical script or
certificate was created or modified, and no L135 correctness verdict was
issued. PROOF.md and DAG.md are unchanged because the argument has not changed.

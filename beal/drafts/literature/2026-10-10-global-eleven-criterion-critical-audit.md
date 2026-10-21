# Global eleven projection criterion — completed audit coverage

TARGET: Critically audit L045's global eleven-adic projection criterion and both-or-neither intersection dichotomy.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the documented exact-field, K(S,p), valuation/class-group and S-unit searches in drafts/literature/2026-10-10-global-eleven-valuation-image.md; compared L045 hypotheses and its ideal-criterion/dichotomy proof scope with that assessment, L033, L041, L044, ATTEMPTS/013 and history/113. No fresh external search or novelty inference is claimed.
SOURCE_EVIDENCE: Reused inspected Sharifi Iwasawa Theory Chapter 1, Notation 1.1.1, Remark 1.1.2, Definition 1.3.19, Proposition 1.4.5 and proof; Schaefer–Stoll June 13, 2001 manuscript Section 5 pp.8–9 and Theorem 8.1 proof pp.20–21. Exact locators, versions and qualifications are recorded below and in the reusable assessment.
COMPARISON: General principal-ideal and S-class structure covers the unchanged number-field hypotheses; the proper-subset valuation projection and ordered-prime dichotomy are the local specialization to audit, not a source theorem computing these classes. No additional source theorem or certified arithmetic is essential to this logical audit.
GAP: L045's field-specific equivalence and dichotomy still require independent mathematical audit; u and v remain unevaluated, and no global image, branch emptiness or simultaneous point lifting is established by this review.
REASON: Approve the exact saved audit target using adequate existing coverage; checking the specialization is distinct from repeating or extending the exhausted witness search.
SCOPE: Exactly TARGET, including L045's conditional cardinality statement, with L033's exact field and K(S,5), L041's ordered maximal-order valuations and L044's audited two-vector set; no class computation or new witness search.
LITERATURE_REASON: Separate approval was required for the newly selected critical-audit target; its source comparison can reuse the unchanged global-valuation assessment without further browsing.

## Source scope and comparison

Romyar Sharifi, [*Iwasawa Theory*, Chapter 1](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html), live author HTML inspected on 2026-10-10 in the reusable assessment, with no identified revision date: Notation 1.1.1 and Remark 1.1.2 supply the principal fractional ideal/class sequence and number-field scope; Definition 1.3.19 supplies the S-class quotient. These are the essential imported structures for an ideal-factorization audit. Proposition 1.4.5 and its proof give the S-unit/Kummer/S-class n-torsion sequence when S includes the infinite places and all places over n. For n=5, including infinite places is compatible with the finite valuation definition in L033; no odd-power sign restriction is imposed. The proposition does not require mu_5 in K. The following Lemma 1.4.6's extra root-of-unity hypothesis is not an input. This sequence explains the torsion-lift coverage to retain; it does not evaluate our projection.

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS **356** (2004), 1209–1231, [DOI](https://doi.org/10.1090/S0002-9947-03-03366-X). Locators refer specifically to the [June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf): Section 5, printed pp.8–9, supplies K(S,p) and the unit/class construction; the ideal-map calculation in the proof of Theorem 8.1, pp.20–21, is a methodological comparison. Its CM and split-prime hypotheses are unavailable for K, so its dimension theorem is excluded. L033's existing descent interface remains an input; no general isogeny-descent reproof is needed.

The reusable assessment also inspected PARI's bnfinit, bnfcertify, bnfisprincipal and bnfsunit documentation. Those guarantees concern a future certified arithmetic computation, not this audit. No arithmetic implementation or availability check is needed now. Previously unread exact-field computational leads remain unread; they are not essential to testing the ideal argument.

## What the next mathematical audit must check

The source comparison leaves these proof obligations for the separate research turn:

- Check both directions of L045's membership equivalence for arbitrary integer lifts of the three valuation residues, allowing arbitrary exponents at every prime above five and fifth-multiple exponents at every other prime. Test whether the fractional-ideal principalization argument retains S-class five-torsion lifts and ideals containing primes of S.
- Check that L041's full local decomposition supplies precisely the ordered global primes and normalized ramification indices used in the principal ideal of eleven. Do not substitute factorization in Z[k] for the maximal integer ring, or require an unnecessary five-adic prime identification.
- Check the passage to the class quotient, rank/cardinality alternatives and intersection with L044's two vectors. Keep the inherited affine norm plane separate from the unrestricted global subgroup, and distinguish valuation attainability from descent-point or integer attainability.

These are audit obligations, not independently verified conclusions in this literature turn. The known general structures should be cited; only the field-specific specialization needs checking. No reproof of Kummer theory or a source theorem is justified.

## Relevance, duplicates and decision test

The main gap is unconditional global emptiness of the five surviving twists for ordered (3,4,11), together with infinitely many other signatures. The intermediate target is a verified logical interface for the eleven-adic projection in the 54a1 branch. Its plausible downstream use is to specify which certified ideal-class relation could exclude that branch or leave both local vectors available; it need not solve independent gaps.

L045 already contains the proposed criterion, so no duplicate lemma is wanted. L033 gives class containment, L041 gives ordered places and L044 gives the local filter; none evaluates the global quotient classes. ATTEMPTS/013 and history/113 record the failed 103,532-element search and its precise limitation. Neither enlarging those boxes nor repeating the two-adic filter is part of this target. Preserve ATTEMPTS/008–014 and unfinished arithmetic. A logical audit is independently testable without unavailable certified class data and does not reopen the stopped arithmetic route.

Continue if the independent audit validates the full equivalence and dichotomy, or identifies a concrete repairable defect. If a genuinely essential source hypothesis is missing, return to source review; if the criterion fails, preserve the defect and choose a corrected or different separately assessed target. Successful validation still leaves u, v, global intersections, all twist emptiness claims and infinitely many signatures unresolved.

Essential continuation inputs: L033, L041, L044 and L045. L038 is needed only if identifying primes above five becomes necessary; this audit's formulation retains all of them abstractly. No cross-notebook theorem is used. No GRH, class-table correctness, rank, Sha vanishing or Selmer/point equality is assumed. Mathlib matching coverage is not checked; unknown is not absence.

This completes source approval only. No mathematical audit, lemma/script modification or argument/DAG change was performed.

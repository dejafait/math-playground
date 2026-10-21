# Canonical quotient consequence — audit coverage ready

TARGET: Critically audit L063's quotient-vanishing application and its exact projection alternatives.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready consequence assessment and its exact K(S,p), class-group and localization searches; compared canonical L045/L063, L062 hypotheses and completed audit, histories 188–189 and ATTEMPTS/013,027,028. L063 is the new review object; no prior completed L063 audit was found in these records. No fresh external search or novelty inference is claimed.
SOURCE_EVIDENCE: Reused inspected Sharifi Chapter 1 Notation 1.1.1, Remark 1.1.2, Definition 1.3.19 and Proposition 1.4.5 with proof, and Schaefer–Stoll June 13, 2001 manuscript Proposition 4.6 p.7 and Section 5 pp.8–9; read saved theorem hypotheses/proof-case notes in the global-eleven-valuation-image and canonical-global-five-eleven-class assessments and the ready consequence assessment. FNS Section 7.2/Table 5 and Stacks tag 01JQ coverage remain audited inputs through L062; no fresh primary retrieval is claimed.
COMPARISON: The unchanged ideal/class and support/localization coverage suffices for an independent audit of L063's combination of L045 and audited L062. The general sources do not state this field-specific consequence; the review must check the local application, not reprove general theory or compute a class group.
GAP: Coverage for this precise audit is now approved; its mathematical correctness review remains to be performed separately. The value of v, full eleven-adic units, all-place restricted intersection and rational/integer lifting remain outside scope.
REASON: The new L063 review object required separate audit-scope approval; essential source coverage is unchanged and reusable, so the next turn should perform the mathematical audit.
SCOPE: Exactly TARGET, with L063 as review object and L045/L062 as direct mathematical inputs; retain their same K, every prime in S, L041 ordered maximal places and normalized orders. Reuse already audited dependencies; do not extend the target to unit classes or integer emptiness.
LITERATURE_REASON: Separate approval of the newly written L063 audit continuation, using existing ready source coverage rather than repeating browsing.

## Gap, intermediate target and decision test

The main gap is positive primitive integer emptiness for the residual
signatures, including the 54a1 branch of ordered (3,4,11). The intermediate
target is a critical audit of the recorded quotient consequence, not a
new witness or exclusion. Its downstream use is to make retirement of
that valuation-class obstruction reliable before choosing another global
restriction. Independent unit and lifting gaps need not be resolved by it.

Continue with the audit if the established source hypotheses cover the
same-global-class support, exact maximal-order quotient and normalized
place interface. That coverage comparison passes. In the next research
turn, approve the application only after checking every interface and the
full projection alternatives; otherwise identify the first failed premise
or inference and preserve the incomplete review. No finite search restart
is part of this test.

## Precise reused sources and hypotheses

Romyar Sharifi, [*Iwasawa Theory*, Chapter 1](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html),
live author HTML inspected 2026-10-10, no revision date identified:
Notation 1.1.1 and Remark 1.1.2 give fractional ideals, the ordinary
principal-ideal/class sequence and class-group finiteness for number
fields; Definition 1.3.19 defines the S-class quotient. Proposition
1.4.5 and its inspected proof give the S-unit/Kummer/S-class n-torsion
sequence when S contains infinite places and all places above n.
Take n=5; infinite places impose no odd-power sign restriction. The
following Lemma 1.4.6's roots-of-unity hypothesis is not part of this
input. L045's exact projection is a specialization of ideal theory,
not an import of a field-specific class value. Its audited sufficiency
retains arbitrary fractional ideal factors and every prime above five.

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf):
Proposition 4.6, printed p.7, includes every prime above the isogeny
prime and places where either Tamagawa number is divisible by it.
The inspected Lemmas 4.3–4.5 cover the unramified-image cases; Section 5,
pp.8–9, supplies the global/local restriction diagram and K(S,p)
construction with the cohomological identification. L062's completed
audit verifies these hypotheses for all global point classes, through
L033's normalized dual-isogeny map. It does not use an integer-solution
premise, Selmer/point equality or Sha vanishing. Theorem 8.1's CM and
split-prime dimension statement is not an input.

FNS, *The generalized Fermat equation with exponents 2, 3, n*,
Compositio Math. **156** (2020), 77–113,
[June 10, 2019 manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2 opening and Table 5, identifies the entire 54a1 fiber before
the GRH-dependent Selmer computation. [Stacks Lemma 26.17.2/tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ)
supplies its affine tensor-product base change. Their statement and
proof-case coverage is already recorded and applied in audited L062;
this review needs no new algebra identification or GRH-dependent result.

## Scope comparison and future audit checklist

The ready assessment
`drafts/literature/2026-10-13-canonical-witness-ideal-class-consequence.md`
already covers the combination of L045 and L062. The additional work
here is approving critical review of the completed application L063.
Read L045's canonical proof and existing audit, L063 in full, and L062's
hypotheses/conclusion and completed audit. The K and S declarations,
ordinary exponent-five quotient, ordered places (residues 8,2,10) and
normalized maximal-DVR convention match in these texts. L062 supplies
membership for one fixed global class, independent of a computed sigma.
This is a hypothesis/scope comparison, not the critical audit itself.

The research audit should check both permitted witness vectors in the
identical criterion, the invertibility used in the consequence, and
necessity AND sufficiency before asserting both-vector attainment.
Check the 25/125 alternatives without assuming a value of v. Distinguish
subgroup membership in the quotient from ordinary principality or
membership in 5 Cl(K) alone. Distinguish valuation attainment from full
local-unit compatibility; in particular, no conclusion that both vectors
share the witness's five-adic class is justified by the projection alone.
No reproof of the imported general theorems or new scripts is needed.

## Duplicates, failures and limits

History 188 approves the earlier consequence attempt; history 189 records
its completion and explicitly leaves L063's critical audit pending. L045
and L062 have their own completed audits, which should be reused rather
than duplicated. ATTEMPTS/013,027,028 contain incomplete polynomial and
principal/mixed-ideal lists. Their negative searches omit the full ideal
freedom in L045 and are not mathematical inputs to L063's application.
Those lists remain parked; this review does not reopen them.

Essential inputs are L045 and audited L062, with L063 the review object;
L033/L041/L044 enter through those existing interfaces. No cross-notebook
input, complete class group, unit basis or original integer solution is
assumed. Full Mathlib matching coverage remains not checked; unknown is
not absent. This turn changes source coverage only, writes no lemma or
mathematical script and does not certify L063's correctness. The exact
saved target is ready for one separate mathematical audit.

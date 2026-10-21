# Canonical witness and quotient ideal-class obstruction — coverage ready

TARGET: Determine whether L062's global witness resolves L045's quotient ideal-class obstruction without a class-group computation.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-field, K(S,p), valuation/class-group and localization searches in the 2026-10-10 global-eleven-valuation-image and 2026-10-12 canonical-global-five-eleven-class assessments; searched the canonical witness assessments and histories 184–187 for an already recorded quotient consequence, and compared L045, L062 and ATTEMPTS/013,027,028. No completed quotient application was located in those relevant records; no novelty inference or fresh external search is claimed.
SOURCE_EVIDENCE: Reused inspected Sharifi Chapter 1 Notation 1.1.1, Remark 1.1.2, Definition 1.3.19 and Proposition 1.4.5 with proof; Schaefer–Stoll June 13, 2001 manuscript Proposition 4.6 p.7 and Section 5 pp.8–9; FNS June 10, 2019 Section 7.2 and Table 5; Stacks Lemma 26.17.2/tag 01JQ. Read their saved hypothesis/proof-case assessments and L045/L062's canonical application and audit passages; no fresh primary retrieval is claimed.
COMPARISON: The covered principal-ideal/S-class theory and audited local statements permit a bounded application of L045 to L062's one global class. The source methods cover this specialization, but neither primary source supplies its field-specific quotient value; no reproof or full class-group computation is needed for the proposed logical application.
GAP: The next research turn must apply L045's exact criterion to L062's normalized vector and state precisely which quotient obstruction is decided; no quotient value or projected intersection is established in this literature turn. The remaining class v, full projected group, eleven-adic unit image, all-place restricted intersection and integer lift are outside scope.
REASON: Approve the saved target with unchanged essential coverage after comparing the previously separate global-witness and maximal-order quotient interfaces; preserve all finite-search stops and leave the mathematical consequence to a separate turn.
SCOPE: Exactly TARGET with L033, L041, L044, L045 and audited L062; retain every prime above five, both possible ordered vectors and the exact quotient. No ordinary principality, complete class group, full local unit image or integer lifting.
LITERATURE_REASON: Changed interface from simultaneous local membership to L045's maximal-order quotient criterion required separate approval; adequate prior source coverage is reused without repeating browsing.

## Relevance and decision test

The main gap is positive primitive integer emptiness for the residual
Beal signatures, including the 54a1 branch of ordered (3,4,11).
The intermediate target is deciding the previously unevaluated quotient
obstruction using the audited intrinsic witness. Its downstream use is
to retire or redirect the class-vanishing certificate route, without
claiming that the remaining independent gaps have been closed.

Continue with one logical specialization if the global class belongs to
the same K(S,5) and its localization uses precisely L045's normalized
ordered maximal places. Test either allowed vector, without selecting
one by an uncomputed field identification. If an essential interface
fails, record the first failure and park the inference. Do not enlarge
finite lists or use their failure to infer nonvanishing.

## Reused primary coverage

Romyar Sharifi, [*Iwasawa Theory*, Chapter 1](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html),
live author HTML inspected 2026-10-10, no identified revision date:
Notation 1.1.1 and Remark 1.1.2 supply fractional ideals and the ordinary
principal-ideal/class sequence for number fields; Definition 1.3.19
supplies the S-class quotient. Proposition 1.4.5 and its proof supply
the S-unit/Kummer/S-class n-torsion sequence when S includes infinite
places and every place above n. For n=5, infinite places add no sign
restriction. No containment of mu_5 in K is required; the following
Lemma 1.4.6's extra root-of-unity hypothesis is not imported. The
criterion must retain torsion lifts and arbitrary fifth-power fractional
ideal factors, rather than restrict the class to an S-unit.

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf):
Proposition 4.6, printed p.7, requires all primes above the isogeny
prime and places where either Tamagawa number is divisible by that
prime. The inspected unramified-image proof cases in Lemmas 4.3–4.5
and Section 5's global/local restriction and K(S,p) construction,
pp.8–9, cover arbitrary global point classes. L033's general support
passage and L062's completed audit check this application independently
of an integer solution. The CM/split-prime dimension theorem in
Theorem 8.1 is not applicable and is not imported. A point/Selmer
identification and Sha vanishing are not required.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. **156** (2020), 77–113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[June 10, 2019 author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2 opening and Table 5 (PDF indices 24 and 26; prior records
use printed pp.25–27), identify the entire twelve-subgroup canonical
field for 54a1 before the separate GRH-dependent Selmer computation.
[Stacks Lemma 26.17.2/tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ),
statement and full tensor-product proof inspected 2026-10-12, covers
base change of that entire affine fiber. These unchanged results are
already applied and audited in L062; no new field identification or
base-change theorem is needed here. Underlying unread references and
unrelated exact-field computational leads remain unread and are not
inputs to this consequence.

## Hypothesis comparison and approved difference

L045 and L062 both refer to L033's degree-twelve K and S consisting
of all finite primes above five and eleven, with outside-S valuations
zero modulo five. L062's general support conclusion is explicit; its
original-solution clause is not needed. L045 uses the maximal integer
ring and all prime-five classes, without requiring their enumeration.
The quotient is exactly

    V = Cl(K)/(5 Cl(K) + <[Q] : Q lies above five>).

It is neither the ordinary class group nor a quotient by one selected
prime above five. L045's map rho uses maximal DVR orders. L041 orders
the eleven places by generator residues 8,2,10, with ramification
indices 1,1,10. L062 explicitly uses that same order and normalized
uniformizer order at the third place. Its conclusion retains both
vectors of L044, irrespective of the chosen fixed rational field
identification; no local permutation has to be resolved in advance.

Thus no essential source gap was found at these interfaces. The
separate research task is to use the established membership and exact
criterion, not to repeat the ideal-theory proof or the witness audit.
Write its full bounded application in a canonical lemma with hypotheses,
qualifications and Mathlib status, and update the narrative only when
that argument has actually been made. Whether the remaining quotient
class v vanishes and which rank alternative holds are separate questions.
Do not infer ordinary principality, a power-order lattice identity or a
complete global restricted image from the quotient conclusion.

## Duplicates, failures and continuation

L045 already proves the criterion and both-or-neither dichotomy, while
L062 proves same-global-class membership. The inspected assessments and
histories 185 and 187 stop before their quotient consequence, so the
next application is not another witness construction or duplicate audit.
ATTEMPTS/013's 103,532 elements and ATTEMPTS/027–028's prescribed
principal/mixed lists are incomplete searches. Their failures omit the
arbitrary prime-five freedom and fifth-power ideal factors allowed by
L045 and do not obstruct this different intrinsic-witness mechanism.
All recorded stop evidence remains intact.

Essential continuation inputs: L033, L041, L044, L045 and L062. Reuse
L062's audited dependencies rather than rederive them. No cross-notebook
input, GRH, computed class table, unit basis, rank, Sha vanishing or
integer-solution hypothesis is authorized. Full eleven-adic units,
all-place restricted compatibility and rational/integer lifting remain
unresolved. Mathlib full matching coverage is not checked, not absent.

This completes coverage comparison only. No mathematical consequence
was derived, no lemma or mathematical script was changed, and no
mathematical certificate was run.

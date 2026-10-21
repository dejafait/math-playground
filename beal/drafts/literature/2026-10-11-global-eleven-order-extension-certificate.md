# Power-order certificate interface — source coverage

TARGET: Assess whether an exact identity alpha*R=(11,k-8)*R*A^5*(5*R)^e in R=Z[k] suffices to certify u=0 in L045 without computing the maximal order.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched ideal extension/product identities, fractional ideal factorization and exact integer-lattice HNF; inspected Ben Lynn's authored extension notes, Milne ANT v3.08 and PARI's official mathnf entry; compared L033, L041, audited L045 and ATTEMPTS/013,025.
SOURCE_EVIDENCE: Lynn, Extension and Contraction, product identity item 3; Milne ANT v3.08 (2020), Corollary 3.13 p.51, fractional ideal definitions and Example 3.19/Theorem 3.20 pp.52–53, Theorem 3.29 p.57; PARI linear-algebra manual, mathnf flags 0,1 and column-module specification.
COMPARISON: General extension and exact lattice interfaces are covered; the field-specific identification of the extended J=(11,k-8)R and the sufficient implication remain a separate specialization. Rational five factors are principal, hence cannot model arbitrary five-prime class freedom in L045.
GAP: Prove the local identification of JO_K, extend the fractional identity by denominator clearing, and give an exact rank/stability/product/equality verifier specification; no witness or class value has been obtained.
REASON: These inspected sources support a bounded mathematical interface proof using existing complete local data, without a computed maximal basis or certified enumeration; general sources alone do not perform the field-specific application.
LITERATURE_REASON: The changed power-order hypotheses and exact verification interface were outside the prior maximal-order assessment.
SCOPE: Only sufficient verification of a supplied identity in the degree-twelve 54a1 field; alpha in K*, A a full-rank fractional R-ideal and e an integer. No witness search, class completeness, equivalence or absence inference.
COVERED_TARGET: Prove the sufficient power-order certificate interface for L045, including the exact extension of (11,k-8)R and a rational-lattice verification specification.

## Source review and precise coverage

The original proposed assessment remains the TARGET. This literature-only
turn supplies coverage for the separately listed mathematical continuation;
it does not prove that continuation or write a lemma or mathematical script.

Queries included `extension ideals ring homomorphism product ideals`,
`algebraic number theory Dedekind criterion index prime factorization ideals`,
and the official PARI linear-algebra manual's `mathnf` entry. Dedekind's
index-dependent polynomial factorization shortcut is unnecessary for the
proposed follow-up: L041 already gives all completed fields and the
integral generator residues. A failed search is not evidence of novelty.

Ben Lynn, [Extension and Contraction](https://crypto.stanford.edu/pbc/notes/commalg/extcon.html),
authored Stanford commutative-algebra notes, live version inspected
2026-10-11 with no revision date identified, defines extension for an
arbitrary ring homomorphism and states product preservation in item 3
of the operations list. It explicitly warns that extension need not
preserve primality. This covers integral ideal products without flatness,
maximality or invertibility; the fractional application must be justified
by clearing denominators. The source does not identify our extended J.

J.S. Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
v3.08, July 19, 2020: Theorem 3.29, p.57, applies to the integral closure
of a Dedekind domain in a finite separable extension. Here the base is Z
and the extension is the characteristic-zero field of L033. Corollary
3.13, p.51, detects ideal equality in localizations. The definitions on
pp.52–53 cover fractional ideals and their products; Example 3.19 gives
the DVR description, and Theorem 3.20 gives unique prime factorization
for fractional ideals in a Dedekind domain. These statements and the
localization/factorization proof cases were inspected. They apply to
O_K, not automatically to R. The planned proof must use the complete
L041 places to determine J's local exponents, and must handle negative
e and fractional A by common denominators. Nothing here licenses
invertibility of arbitrary R-ideals or a computed class group.

[PARI official linear-algebra manual](https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#mathnf),
live HTML accessed 2026-10-11, no release number identified, entry
`mathnf`: for integer matrices its output columns span exactly the
input column module; full output flag 1 supplies a unimodular
transformation with M U=[0|H]. The full hypothesis and flag description
were read. This covers exact integer-lattice arithmetic rather than
floating short-vector enumeration. A future verifier may clear rational
denominators and use this interface, or explicit integral coordinate
certificates for both inclusions. No implementation availability or
runtime bound has been established.

## Specialization still required

The next proof must identify J O_K using all three eleven places,
including the degree-ten place, and all places away from eleven.
Checking only the root at residue 8 would leave an essential gap.
It must extend the entire proposed identity, rather than contract a
maximal-order identity and assume extension/contraction are inverse.
No global equality R=O_K or polynomial-index calculation is requested.

The exact-verification specification must retain the power basis from
L033, twelve-dimensional rational coordinates, nonzero alpha, rank
twelve for A, a common denominator, and closure under multiplication
by k. It must explain product generation by all generator products
reduced modulo L033's monic polynomial, principal multiplication and
literal lattice equality. Rank alone is not ideal stability; equal
determinants or field norms alone are not equality of lattices.
Negative e denotes rational scaling by 5^e, not an assumed inverse of
an arbitrary noninvertible R-ideal. No numerical computation is approved
by this source review beyond that future specification.

The rational five factor is principal in the inspected fractional-ideal
terminology. Therefore the continuation must explicitly compare its
restricted sufficient certificate with L045's freedom at every prime
above five; it must not claim equivalence or lose that freedom in the
original criterion. No decomposition at five is needed merely to state
this restricted interface. Whether any such restricted witness exists
is unresolved, and this may be a substantially stronger demand than
L045's class condition.

## Relevance, duplicates and decision test

The main gap remains unconditional positive primitive integer emptiness
for surviving ordered (3,4,11) branches and all other residual Beal
signatures. The intermediate target is a sufficient certificate interface.
Its plausible downstream use is exact verification of a future u=0
witness, retiring the eleven projection as an exclusion mechanism while
leaving unit classes, other-place compatibility, global modular points
and integer-power lifting independent.

Essential inputs are L033's field and power basis, L041's complete local
factors and ordered primes, and audited L045's quotient criterion. L044
provides the downstream two-vector filter and L032 the branch scope.
There is no cross-notebook input. L045 does not already prove the R
interface. ATTEMPTS/013's bounded norm failure and ATTEMPTS/025's
maximal-order/enumeration blocker remain preserved; neither proves
class nonvanishing. This source review does not reopen their searches.
The target statement audit in foundations/01-target-and-scope.md already
records the primary formulation checked today and is reused.

Continue with the separate interface proof only if complete local
identification and exact finite-lattice verification can be justified
from these inputs. Park the interface if either needs unavailable
maximal-order data, unsupported inverse arithmetic, or a completeness
claim for restricted witnesses. No witness construction is yet approved.
Mathlib coverage of the full specialized interface is not checked;
no absence assertion is made. Outcome EXPLORATION records new source
coverage, not a proved certificate, computed u or new mathematical result.

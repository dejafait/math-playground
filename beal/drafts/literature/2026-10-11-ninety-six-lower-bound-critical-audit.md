# Degree-36 lower-bound critical audit — approved source coverage

TARGET: Critically audit L052's complete local factorization, maximal-discriminant tower bound and strict Minkowski threshold comparison.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior lower-bound assessment's exact field/coefficient and standard-theorem searches; inspected L051,L052, ATTEMPTS/018-019 and histories 137-140; reopened only primary theorem passages needed for the audit, with no new broad search or novelty claim.
SOURCE_EVIDENCE: Milne ANT v3.08 Theorem 7.38, Corollary 7.42, Remark 7.43 and Proposition 7.44 pp.123-126, Theorem 4.3 p.70; Sutherland Fall 2021 Lecture 11 Theorem 11.23 pp.8-9 and Lecture 12 Proposition 12.28 p.10; Conrad The Different Ideal Theorem 4.13 pp.12-14; retained prior coverage of completion/different norms and FNS field models/degrees.
COMPARISON: These standard results cover every theorem interface in the saved audit target; the additional inspected valuation-normalization passage makes the slope-denominator premise explicit. Their coverage does not independently certify L052's coefficients, local conclusions or threshold arithmetic.
GAP: Independent verification of the entire local factors, maximal-ring specialization and exact squared inequalities remains; no global class/unit/Selmer completeness or branch emptiness is established.
REASON: Separate approval of the unchanged critical-audit target is complete; reuse known methods for one mathematical audit, without reproof or further literature scheduling.
SCOPE: Exactly the saved L052 audit, using L051 and the complete certificate /local and /cutoff fields; corrections to that argument are covered, but different fields or new ramification mechanisms require review.
LITERATURE_REASON: The supervisor required a separate audit-coverage gate; the essential valuation-normalization and conjugate-slope proof cases were inspected explicitly, while the remaining ready lower-bound literature was reused.

## Reused sources and exact theorem comparison

The prior [lower-bound assessment](2026-10-10-ninety-six-field-discriminant-lower-bound.md)
is adequate for the unchanged fields and mechanism. Its search queries,
FNS final June 10, 2019 manuscript pp.4,27, primary section7.magma
coordinate transport, and completion/different norm statements are
reused rather than rediscovered. The source's degree 36 and K96 degree
12 remain cited premises, without importing its conditional Selmer work.

Milne, [ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
July 19, 2020, Theorem 7.38 assumes a complete discretely valued field
and a finite separable extension; the valuation extends uniquely.
Corollary 7.42 gives degree ef, and Remark 7.43 gives the extended
normalized value group (1/e)Z. These statements and their local
normalization argument were read. Proposition 7.44 assumes
characteristic zero and supplies slope blocks over the base field;
its conjugate-valuation/factor-descent proof was read. Its descending
coefficient convention must be reversed for L052's arrays. Theorem
4.3 p.70 supplies the ideal-class Minkowski expression for a number
field, with s counting nonreal embedding pairs. Its statement was read;
no fresh proof of the general Minkowski theorem is needed.

Sutherland, [Lecture 11](https://math.mit.edu/classes/18.785/2021fa/LectureNotes11.pdf),
October 18, 2021, Theorem 11.23 assumes a Dedekind base, finite
separable fraction-field extension and integral closure. Parts (3)-(5)
preserve e,f, identify local degree ef and give the entire completion
product. Their proof, including the dimension and approximation step,
was read; no Galois assumption is needed for these parts.
[Lecture 12](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf),
October 20, Proposition 12.28 p.10 applies to a further finite separable
extension and its integral closure, giving the discriminant tower formula.
Its statement was read; its reference to Serre, Local Fields,
Proposition III.8 was not newly opened. Retain prior inspected
Proposition 12.4 and Theorem 12.17 for completion and different norms.
An arbitrary polynomial order cannot substitute for these closures.

Conrad, [The Different Ideal](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf),
undated author PDF retrieved October 11, 2026, Theorem 4.13 pp.12-14
applies to every number field and prime above p. It gives exponent
e-1 if p does not divide e and at least e otherwise. The nilpotent-trace
and residue-filtration cases were read in full through equation (4.9)
and the nonzero finite-field trace argument. Corollary 4.16 p.14 was
also inspected. Wild equality is not asserted; no polynomial-index
or Galois premise is needed. These cited theorems suffice; a reproof
would not resolve the remaining field-specific audit.

L052 is the existing field-specific result, so this target is an audit
of a recorded specialization, not a duplicate new lemma or a novelty
search. ATTEMPTS/018 concerns an order upper cutoff; ATTEMPTS/019
records the subsequent true-cutoff stop. Neither blocks checking the
new certificate. No source inspected changes those mathematical
decisions, and this coverage approval is honestly STALLED rather than
a new advance or informative negative. Mathlib coverage remains not
checked; unknown coverage is not evidence of absence.

## Approved audit and continuation test

Essential mathematical input is L051, including the source's absolute
degree 36 and K96 degree 12. Inspect L052 and the entire certificate
fields `/local` and `/cutoff` during the next mathematical audit. No L033/L045,
cross-notebook result, class backend or GRH-dependent computation is
required. Unresolved assumptions remain the independent correctness
of the new specialization, all class/unit/Selmer completeness and
global branch emptiness. Actual signature and exact field discriminant
are not needed for this one-sided threshold conclusion.

Pass test: every prime completion is accounted for, each local bound
is in the maximal ring, the degree-three tower cannot subtract exponents,
and the exact lower comparison is strictly above 10^6. Repair a concrete
error if found; if the bound fails, withdraw only the new threshold stop
and retain ATTEMPTS/018. This audit decides certificate reliability,
not Beal or necessary class-group complexity.

The main gap remains unconditional global emptiness of L032's surviving
branches, alongside independent residual signatures. This intermediate
audit can secure or correct the enumeration routing evidence. No
certificate computation or mathematical audit was performed in this
literature turn; canonical proofs and scripts remain untouched.

# Normal closure — remaining-prime ramification application scope

TARGET: Test whether, for every L089 survivor, all six orderings and actual w|v|p with p not in {2,3,5}, (C_o)_w/T_v is tame and is unramified when v_p(j(E))>=0.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step382's all-place comparison identified this missing assertion; reuse step364's repair searches and step368's reduction coverage, with fresh remaining-prime/tame-compositum queries recorded in 2026-10-20-normal-closure-all-place-different-assembly.md. L090's conjugate setting and L092-L095's scopes contain no completed remaining-prime application.
SOURCE_EVIDENCE: IV April 2020 reproduction Proposition 1.8(vi),(vii), statements p.19 and proof cases pp.20-21, freshly read; Conrad Math 248A Tame ramification and composite fields, Theorem 2.1 p.2 and proof reduction/Lemma 3.1 pp.2-3, freshly read; Milne ANT v3.08 7.50-7.52 pp.127-129 freshly read, 8.10/8.13 pp.139/141 reused; Silverman AEC second edition VII.5.5 pp.197-199 reused from step368. Links and scope below.
COMPARISON: Known odd-residue Legendre reduction, prime-to-residue torsion and tame/unramified compositum theorems cover the methods needed; the difference is their application to every actual conjugate/completion of L090's C_o, not a new general ramification theorem.
GAP: No such all-survivor/order/place application has been proved here. It would still not identify native selected conductor support, prove the weighted estimate or repair exact generation and independent initial data.
REASON: This bounded same-field test isolates the remaining-prime obligation without repeating authentication or assuming an initial-data construction.
SCOPE: Only exact TARGET with L090's actual conjugates, all extending places and unchanged L089 survivors; no conductor/support or repair verdict.

## Ready coverage for a later application

Written during step382's literature-only review; no application proof
is supplied. Newly written ready continuations receive separate
supervisor approval on the following turn.

The main gap is original finite B>=A. This intermediate target could
supply a remaining-place input to the printed pre-ell estimate.
Continue only if actual conjugates and their completion compositum
are identified and both reduction cases justified. A failed hypothesis
stops this application; native support and weighted assembly remain
independent obligations, not automatic consequences of a positive test.

Essential input is audited L090 with inherited L089 survivor E/Q,
c,h,d_*,e_*, both fixed domains and closure: T=Q(E[2])=Q(t_o), every
literal E_o, G_o=T(iota,E_o[15]), C_o=G_o^nor subset M=Q(E[60]),
and all occurring Q-conjugates. Keep every actual w|v|p with compatible
completion embeddings and v_p(p)=1. L092-L095 motivate this target
but their estimates need not be premises. Initial theta-data are not
assumed. No height-selected-prime substitution is involved.

Import without general reproof:

- Mochizuki, [*IUT IV*, April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 1.8(vi),(vii), pp.19-21: over an odd-residue complete
  DVR fraction field, a Legendre model becomes semistable over an
  extension of degree at most two; the potentially-good case is good
  over the original field. For level invertible in the DVR, good
  reduction gives unramified full torsion and multiplicative reduction
  gives a tame torsion field with ramification index dividing the level.
  Split multiplicative reduction is not required by the statement.
- Silverman, [*AEC*, second edition (2009)](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves),
  VII.5.5 pp.197-199: potential good reduction is equivalent to
  integral j for complete discrete valuation fields with perfect
  residue field. Reuse the inspected general theorem/proof record in
  `2026-10-20-normal-closure-local-two-degree-scope.md`, rather than
  only its prior dyadic application.
- Conrad, [*Math 248A. Tame ramification and composite fields*](https://math.stanford.edu/~conrad/154Page/handouts/tamecomp.pdf),
  Theorem 2.1 p.2: tameness persists under finite base change and
  finite composita of tame extensions are tame, with embeddings into
  one common field fixed. The proof reduction and Lemma 3.1 pp.2-3
  were read. No date/version appears in the four-page PDF. No exact
  ramification-index formula for our fields is imported.
- Milne, [*ANT* v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  7.50-7.52 pp.127-129: unramified extensions and their composita
  inside a common algebraic extension of a complete field with perfect
  residue field; 7.51 also covers prime-to-p roots of unity. Reuse
  8.10/8.13 pp.139/141 for actual completion/tower identifications.

The later proof must check that 2 and 15 are units, apply reduction
to the actual literal equations and their actual conjugates, retain
the common geometric j, handle the quadratic semistable extension,
full-coordinate torsion and iota, and identify the finite completed
compositum. A potentially-good Legendre model is distinguished from
an arbitrary potentially-good quadratic twist. Do not interchange
completion and normal closure by fiat or reprove general theorems.

Mathlib full/supporting coverage is unchecked. April-reproduction
authentication/current-version and def= qualifications remain;
ATTEMPTS/035 stays parked. Even a positive result leaves native
selected support, the normalized sum, exact generation/repairs,
height-selected prime, independent initial data, native input/action/
factorization/pilot and essentiality unresolved. STATUS remains
IN_PROGRESS; no complete-solution candidate is proposed.

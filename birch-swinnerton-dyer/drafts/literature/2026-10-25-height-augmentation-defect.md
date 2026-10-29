# Height pairing and augmentation defect — duplicate established criterion

TARGET: Assess whether nondegeneracy of the cyclotomic p-adic height on E(Q) tensor Q_p removes L002's augmentation defect under finite Sha[p-infinity] and good ordinary reduction.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Targeted local height/augmentation searches found the exact result in L003 and foundations/04; checked ATTEMPTS/002 and ATTEMPTS/031, then reused their source comparisons and checked the published statements below.
SOURCE_EVIDENCE: Ray (2023), Theorem 3.4 and Section 3.2, p.445; Stein--Wuthrich (2013), Section 3 opening p.1761 and Theorem 6.1 p.1776; Schneider publisher record confirms the original remains subscription-only; precise attribution is through Ray.
COMPARISON: L003(2) already answers the exact target under odd good ordinary p, classical cyclotomic control/cotorsion, finite p-primary Sha and nonzero ordinary cyclotomic regulator; no new proof or lemma is warranted.
GAP: No local gap remains for this conditional implication; uniform Sha finiteness, height nondegeneracy and comparison with complex analytic order remain unproved.
REASON: The exact duplicate changes routing: reuse L003 and abandon its proposed rederivation; separately approve only the quantitative full-Selmer filtration specialization described in the continuation assessment.
SCOPE: Import the existing sufficient criterion only, including CM curves; retain non-CM for the converse from the checked Stein--Wuthrich source. No unconditional height, Sha or complex-order conclusion is covered.
LITERATURE_REASON: The startup assessment was REVIEW_REQUIRED and the required duplicate/hypothesis comparison had not been performed for this invocation; ready older height coverage was reused immediately when found.

## Target, test and duplicate evidence

The main gap is rational rank versus complex analytic order at arbitrary
order at least two. The intermediate target was removal of L002's delta
under finite Sha and nondegenerate rational cyclotomic height. Its plausible
use is one algebraic input to a later order comparison, with those hypotheses
still independent. The test was an applicable characteristic-order theorem,
with abandonment of any duplicate or circular proposal.

Read L001 and L002 in full, then the relevant L003 proof and
[existing height source audit](../../foundations/04-cyclotomic-height-criterion.md).
L003(2) already states precisely the requested implication, including
TM=0 and augmentation semisimplicity. Its proof retains finite generation
and torsion of the classical Selmer dual and the canonical ordinary height.
Its conventions include the empty regulator determinant in rank zero.
The [original decision](../../history/003-2026-09-25-cyclotomic-height-criterion.md)
already records its successful conditional scope. This is new evidence of
duplication for the proposed continuation, not a new mathematical discovery.

## Sources actually inspected and applicability

Anwesh Ray, *Remarks on Hilbert's tenth problem and the Iwasawa theory of
elliptic curves*, Bull. Aust. Math. Soc. 107 (2023), 440--450,
[Theorem 3.4, p.445](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/32000D6BB2B3EC97CAD0B6F932B84935/S000497272200082Xa.pdf/remarks-on-hilberts-tenth-problem-and-the-iwasawa-theory-of-elliptic-curves.pdf#page=6):
read the full statement, its citation proof and preceding definitions.
It requires odd ordinary p, finite p-primary Sha, nonzero regulator and
finitely generated torsion Selmer dual. It gives characteristic order equal
to rank. Set K=Q; its regulator normalization differs by a nonzero scalar,
so nonvanishing is unchanged. Section 4's non-CM condition is later.
Its leading-term assertion is not used. Ray attributes this to Schneider,
*p-adic height pairings. II*, Invent. Math. 79 (1985), 329--374,
Theorem 2', p.342. The [publisher record](https://doi.org/10.1007/BF01388978)
was inspected, but the original theorem/proof remains unread; subscription
access was not pursued. The published restatement is sufficient here.

William Stein and Christian Wuthrich, *Algorithms for the arithmetic of
elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), 1757--1792,
[Theorem 6.1, p.1776](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=20):
read its full ordinary-case statement and surrounding attribution, Selmer
definition on p.1775, and the standing non-CM condition on p.1761.
Its equality criterion retains both finite Sha and nondegenerate height;
its converse is imported only with that standing restriction. Good ordinary
reduction, rather than the multiplicative extension, is used. The theorem
is about the algebraic characteristic series, not an analytic p-adic BSD
conjecture. No original theorem proof is claimed to have been replayed.

Reused foundations/03 for Mazur control and Kato--Rohrlich cotorsion;
no stronger control claim or residual irreducibility hypothesis is added.
The [current Clay page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
and [Wiles statement, p.2](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=2)
were checked: the rank assertion and separate leading-coefficient refinement
have the recorded scope. The notebook's argument and target did not change.

Bounded external queries were `Schneider "p-adic height pairings. II"
"Theorem" 342 pdf` and `"elliptic" "augmentation" "derived heights"
Howard`. Search snippets and an unreviewed claimed BSD proof were not
accepted as evidence. No novelty inference follows from these searches.

## Failures and distinct continuation

ATTEMPTS/002 forbids characteristic-ideal/control-only rank inference;
ATTEMPTS/031 preserves the unresolved ordinary-to-strict localization
branch. Neither contradicts L003's additional arithmetic hypotheses.
The prior full-Selmer review
[dated 2026-10-04](2026-10-04-cyclotomic-selmer-height-radical.md) and
L019 retain the obstruction to promoting height structure to rational
Kummer membership, even with compatible divisible Sha towers.

For a genuinely different bounded use of the same height machinery,
Howard's full-Selmer filtration can potentially quantify delta when the
first height is degenerate. Reused that review and inspected Howard's
Section 4 setup, Lemma 4.1, Theorem 4.2 with its proof, and Corollary 4.3
with its complete proof, printed pp.15--17. This is a known theorem lead,
not a new derivation. The exact later specialization is recorded in
[its separate assessment](2026-10-25-derived-height-defect-accounting.md)
for next-turn approval. No lemma or mathematical script was written.

## Mathlib

Full arithmetic height criterion and derived-height formalism: not checked.
Supporting DVR and finite-generation coverage: not checked. The existing
canonical proof and precise published citations suffice for this review;
unknown Mathlib coverage is not an absence claim.

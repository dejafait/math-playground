# Actual rank-two Kato exterior certificate: completed source comparison

TARGET: Assess whether an actual rank-two derived Beilinson--Kato class supplies a nonzero rational exterior-square certificate under L018's hypotheses without finite Sha, distinguishing point-valued formulas from full-Selmer determinant formulas.
CHECKED: 2026-10-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for actual derived Beilinson--Kato rational formulas, rank-two p-converses and balanced diagonal point formulas; reused the earlier BKS/Sano assessment and read additional primary BCGS and BSV statements. Queries and versions are recorded below.
SOURCE_EVIDENCE: BKS arXiv:1910.07404v2 Hypothesis 2.2, Section 4.2 and Theorem 6.2; Sano arXiv:2308.08875v1 Section 5.2/Theorem 5.9; BCGS author text dated 2026-01-02 Theorem C/Corollary C, p. 4; BSV author volume final article Section 1, Assumption 1.1/Theorem A/Corollary B/Remark E, article pp. 2--7. Direct links and read limits appear below.
COMPARISON: The point-valued BKS formula retains finite Sha and positive rational rank; Sano's domain remains cohomological with the dual H^2 factor and a conjectural analytic identification. BCGS supplies Kato-family nonvanishing and a fine-Selmer index, while BSV's multiplicative-prime formula concerns a local logarithm in an Artin-twisted representation. Neither new statement supplies the retained rational exterior-square certificate.
GAP: No inspected theorem supplies a nonzero element in wedge^2(E(Q) tensor Q_p) under L018 alone. Actual derivative nonvanishing, rational determinant membership and production of the two-prime premise from analytic order two remain unproved.
REASON: Do not import an unconditional rational certificate from these sources. Park this direct import and preapprove the independently testable finite-extension/global-Kummer transfer criterion in the companion assessment; its geometric realization is an explicit later gap.
SCOPE: Retain L018's non-CM ordinary non-anomalous, residual, local, Manin/Tamagawa, minimal two-prime and central-vanishing hypotheses. Do not infer complex order two, finite Sha, positive rational rank, equality of Kim's integral and mod-p indices, or a rational exterior-square domain from a Selmer determinant theorem.
LITERATURE_REASON: The saved arithmetic target was REVIEW_REQUIRED; the specific source need was an actual point-valued comparison without finite Sha, including the scope of newer nonvanishing and balanced-diagonal theorems.

## Gap and threshold

The main unresolved assertion is rank E(Q) = m(E) for m(E) >= 2.
The achieved bound on L018's conditional branch is r <= 2; the needed
threshold is r >= 2. A nonzero rational exterior square would supply
that lower bound. A formula that already assumes a rational basis or
finite p-primary Sha cannot produce it here. The fixed two-prime
premise, its production from m(E) = 2, analytic comparison and higher
ranks remain separate unresolved steps.

Reuse the earlier [cyclotomic derivative assessment](2026-10-03-cyclotomic-kato-derivative.md)
for its unchanged general determinant construction, and the
[all-depth assessment](2026-10-04-central-vanishing-all-depth-classical-lifting.md)
for Kim and the Kummer quotient. L013 already tests formal determinant
sufficiency; L019 already tests the ordinary height radical. Repeating
either model would not test the actual arithmetic class. The rank-one
correction failures and parked Eisenstein/Nekovar/Jones blockers remain
preserved. The new sources below do not overcome them.

## Primary statements compared

**Burns--Kurihara--Sano**, *On derivatives of Kato's Euler system for
elliptic curves*: reused the previously read published statement record;
reopened [arXiv:1910.07404v2, Hypothesis 2.2 and Remark 2.3](https://arxiv.org/html/1910.07404v2#S2.SS2),
Section 4.2 (Proposition 4.5, Definition 4.6), and
[Theorem 6.2](https://arxiv.org/html/1910.07404v2#S6.SS2).
The v2 submission is dated 2020-04-17; it is not silently identified with the
2024 journal version. Hypothesis 2.2 adds positive rational rank and
finite p-primary Sha. The resulting point/cohomology identification
is therefore unavailable under L018. The derivative index in Section
4.2 uses a = max(0,r_alg-1), not analytic order or Selmer dimension.
Theorem 6.2's generalized Rubin formula retains Hypothesis 2.2.
Augmentation divisibility gives neither the requested rational domain
nor its nonzero exterior square. This scope is already covered; no
reproof or further retrieval of the earlier failed journal URL is needed.

**Takamichi Sano**, *Derived Bockstein regulators and anticyclotomic
p-adic Birch and Swinnerton-Dyer conjectures*,
[arXiv:2308.08875v1, Section 5.2](https://arxiv.org/html/2308.08875v1#S5.SS2),
2023-08-17: reused Section 2 coverage and re-read Example 5.2(ii),
Hypothesis 5.3/Remark 5.4, the regulator domain in Section 5.2,
Conjecture 5.5 and Theorem 5.9 (PDF pp. 34--37).
The Kato example has basic rank one, distinct from rational rank.
The regulator retains wedge^(r+e) H^1 and wedge^e (H^2)^*, with
cohomological e and Bockstein-determined order. It is not a map
defined on wedge^2 E(Q) without further identification. Theorem 5.9
assumes both a main conjecture and Conjecture 5.5. Even a determinant
lift of the actual Kato element would not supply the omitted point
identification. This is the same covered limitation as L013, not new
negative evidence by itself.

**Burungale--Castella--Grossi--Skinner**, *Non-vanishing of Kolyvagin
systems and Iwasawa theory*,
[author PDF dated 2026-01-02, Theorem C/Corollary C, printed p. 4](https://web.math.ucsb.edu/~castella/Kolyvagin.pdf#page=4):
read the introductory statement and Kato-family definitions there.
The [arXiv locator is 2312.09301](https://arxiv.org/abs/2312.09301);
no identity of all versions or audit of the proof is claimed.
Theorem C assumes non-CM, good ordinary p, E(Q_p)[p] = 0 and the
rational cyclotomic main conjecture; its stated irreducible p > 3
case gives family nonvanishing. Corollary C measures the first
nonzero Kato-system index by the **fine Selmer corank**. These are
actual arithmetic classes, but neither statement gives a prescribed
two-prime index or a rational-point exterior square. Family
nonvanishing is not nonvanishing of the desired rational determinant.

**Bertolini--Seveso--Venerucci**, *Balanced diagonal classes and
rational points on elliptic curves*: read Section 1 of the
[author-hosted volume, final article pp. 2--7, PDF pp. 182--187](https://web.mat.upc.edu/victor.rotger/docs/Volume-BSV-DR.pdf#page=182),
including Assumption 1.1, representation factorization (4),
Theorem A, Corollary B and Remark E. This is the accessible author
volume; published pagination/normalizations were not compared.
Theorem A relates a **local** Bloch--Kato logarithm to the product of
Heegner/Stark--Heegner logarithms. Its prime is multiplicative and
inert in the auxiliary quadratic field, unlike L018's retained good
ordinary prime. Its representation factors into two induced-character
summands, so order two for the triple-product L-function is not the
assertion m(E) = 2. Imaginary-quadratic points in the formula live in
ring class fields; Remark E in the real case states a Selmer-localization
conclusion. A product of logarithms is not a global exterior-square
identification. Changing the prime and auxiliary representation would
require new hypotheses, not a direct import into L018.

The earlier Castella--Hsieh Theorem A and Section 5.7 coverage is
adequate and reused from [the foundation](../../foundations/07-castella-hsieh-nonvanishing.md).
Reopening its finite-Sha point formula would duplicate that audit.
Castella--Sano Proposition 2.3.1 was rechecked only for source scope:
its nonzero character-specialized Kato class is an additional premise;
the preceding derivative assessment already records the limitation.
No broader theorem is imported from that paper.

## Bounded continuation decision

The new BCGS and BSV comparisons rule out two apparent shortcuts from
actual classes or point logarithms to the missing certificate **in the
retained setting**. They do not disprove an arithmetic rationality
theorem, BSD, or these constructions. No exact matching theorem was
found in this bounded search; no originality inference follows.

Three mechanisms were compared: the covered cohomological determinant
descent (insufficient by L013), the new balanced-diagonal local point
formula (different hypotheses/domain), and global Kummer realization
after restriction to a finite number field. Choose the third for a
bounded transfer test. It adds a genuinely global-point condition absent
from the formal height/tower model; local Kummer membership in a Selmer
group does not satisfy it.

The [ready companion assessment](2026-10-04-finite-extension-kummer-transfer.md)
imports the standard transfer identity and finite Kummer sequence and
approves one conditional calculation. It asks whether an L018 basis
at a coefficient depth exceeding the p-valuation of an extension degree
can certify r = 2 if both restricted classes are globally Kummer there.
That threshold is a proposed test, not a result proved in this turn.
Production of such point realizations from an actual Kato/cycle family
is explicitly unproved. The downstream use would be a concrete
finite-field arithmetic witness for the missing lower bound, rather
than an assumption of finite Sha.

Continue this mechanism only if the cited transfer and exact sequence
give the stated conditional implication with a precise degree loss.
Abandon or weaken it if an unretained torsion/local/compatibility premise
is required. A success would justify seeking a point-valued realization
in one field; it would not establish that realization. Fields with
unbounded p-part of their degrees must not be silently treated as a
fixed-degree witness. No calculation is performed here.

## Search and access record

Queries actually issued on 2026-10-04 included:

- `"derived Beilinson" "rank" "two" rational points finite`
- `"Kato" "exterior" "rank two" Sha`
- `"rank two" "p-converse" elliptic curves`
- `"derivatives of Kato" "finite" Shafarevich`
- `"On derivatives of Kato" Burns Kurihara Sano`
- `"rank two" "rational points" "Kato" theorem finiteness`
- `"derived Kato" "rational" conjecture`
- `"Balanced diagonal classes" "rational points" rank`
- `site.jmilne.org "restriction" "corestriction" "multiplication" Galois`
- `"Tate-Shafarevich" "restriction" "corestriction" "degree"`
- `"On derivatives of Kato" 90699069 pdf`
- `"Non-vanishing of Kolyvagin systems and Iwasawa theory" Burungale Castella Grossi Skinner arxiv`
- `"Kummer" "corestriction" "norm" elliptic curves global points restriction`
- `"Selmer" "fixed extension" "Kummer" "degree"`

Essential primary texts for the source comparison and transfer subtarget
were accessible. The full newer proofs and their cited inputs were not
audited; they are not needed for the limited scope exclusions. Optional
2026 inert-prime diagonal-cycle and derived Beilinson--Flach search
leads were not read at theorem level and are not supporting evidence.
An incorrect provisional arXiv locator returned an unrelated paper;
it is excluded entirely. Search snippets, secondary summaries and
claimed complete BSD proofs were not accepted as theorem evidence.
The current Clay page was opened; its official target is unchanged,
so the existing Wiles statement/scope coverage is reused.

The completed step is a literature NEGATIVE: new theorem-domain
comparisons change the continuation to a finite-extension geometric
witness test. It reproduces known source distinctions, claims no
mathematical rank improvement or progress beyond the checked literature,
and spends no mathematical exploration turn. No lemma, script, graph
input or complete candidate is added.

## Mathlib

Full Mathlib coverage of the rational exterior-square certificate,
supporting derived-class formulas and transfer specialization:
**not checked**. The named primary results above support this domain
comparison; none is a full TARGET match or a Mathlib declaration.
Absence from Mathlib and mathematical originality are not inferred.

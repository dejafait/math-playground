# First Kato-system index and rationalized localization — limited specialization

TARGET: Specialize Kim's first-index theorem and ordinary/strict exact sequence to L026 to characterize nonzero rationalized p-localization, retaining both source branches and finite localization images.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The saved semisimplicity/localization review searched exact ordinary/strict and first-index terminology and checked L014/L021 and recorded determinant/height failures; its query and duplicate record is reused unchanged.
SOURCE_EVIDENCE: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf (2025-05-12, printed pp. 10--11, 14--15, 20, 26--28: Sections 2.1/2.5, Definition 2.12, Theorem 2.13(5), Proposition 3.13, (5.1), Sections 5.3.2--5.3.4); https://www.maths.nottingham.ac.uk/plp/pmzcw/download/fine.selmer.pdf (25-page author version, printed pp. 5--8: Section 2.1, Lemma 3.1, Proposition 4.1). Direct URLs and essential statements were rechecked for source-URL recovery on 2026-10-14; broader coverage is reused from the parent assessment.
COMPARISON: The cited source identifies strict corank with the first nonzero Kato-system index and explicitly keeps two classical/strict-corank branches. The local task is only the compact/discrete and localization specialization to L026/L005, not a reproof of the source theorem or production of a first-index witness.
GAP: The source formula must be matched rigorously to L005's compact rationalized localization, distinguishing a finite discrete image from positive image corank; L026 alone has not selected a successful index.
REASON: The exact arithmetic criterion could make the remaining localization prerequisite independently testable without auxiliary-field choices or rational-point assumptions. Only this specialization is covered; no new semisimplicity-to-localization claim is approved.
SCOPE: Retain all L026 hypotheses and its corank-two conclusion, and all source classical/strict/relaxed conditions; allow no zero-finite-quotient, finite-Sha, positive-rational-rank or Kummer-membership assumption.

The separate literature approval and direct-source-URL recovery were
completed on 2026-10-14. DECISION remains SPECIALIZE for the unchanged
target and hypotheses. No mathematical result is derived here.

Use [the complete comparison](2026-10-14-cyclotomic-semisimplicity-localization.md)
for queries, primary statements, essential proof cases and duplicate checks.
That assessment supplies theorem-level coverage; sources need not be
browsed again for unchanged hypotheses. Import the results by those exact
citations, writing only the compact/discrete applicability argument. A
reproof of the general Kolyvagin structure theorem is unnecessary.

Essential local inputs are L002, L005 and L026; L014/L021 and L013/L019
are contrasts/failure checks, not additional arithmetic premises. No
cross-notebook input is proposed. Retain non-CM E/Q, good ordinary p>=5,
surjective residual representation, p coprime to #E(F_p), the Manin constant
and all Tamagawa numbers, E(Q_p)[p]=0, the compatibly normalized nonzero
residual Kurihara collection, L(E,1)=0, sign +1 and the independently
certified primitive a_2. L026 gives classical corank two and TM=0; it
does not supply L018's prescribed basis or eliminate the finite quotient.

Let D=Sel(Q,E[p^infinity]), D_0 its p-strict subgroup, and S the compact
rationalized space of L005. Let k be Definition 2.12's first nonzero index
of the nontrivial **whole** Kato Kolyvagin system. It is not the first index
of its singular localization, the first residual Kurihara index, the
cyclotomic order of its initial Iwasawa class, or ord_T L_p. The target is
an exact criterion involving k for loc_p:S -> V_loc to be nonzero, with
both source branches explicit. Establish nontriviality from the retained
collection premise using Proposition 3.13, and justify all Tate-module
identifications before using coranks. Preserve the finite-image branch;
do not infer compact nonvanishing from an isolated mod-p localization.

The downstream use is an independent threshold for the localization
prerequisite of the separately assessed generalized Kato theorem.
Producing that threshold, actual auxiliary data, rational membership of
its strict class, and arbitrary complex-order comparison remain open.

Continuation test: continue only if the specialization gives the exact
criterion without losing finite errors or importing a point basis. Stop
if it needs finite Sha, already nonzero localization or the rejected
height-radical surjection. No formal countermodel, new arithmetic source
production or assertion that TM=0 selects a branch is in scope.

Mathlib coverage of the full specialization and source theorems is not
checked. Supporting module facts must be justified in the applicability
proof; unknown library coverage is not evidence of absence.

## Direct primary-source recovery and approval

The main gap is arbitrary higher-order complex/rational rank equality.
This assessment approves only the first-index localization criterion
stated in TARGET; it cannot select the successful branch.

[Kim's primary text](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=15)
is dated May 12, 2025. The recheck covered the classical and dual canonical
local conditions (printed pp. 10--11), Definition 2.12 (p. 14),
Theorem 2.13(5) (p. 15), Proposition 3.13 (p. 20), and the exact sequence
(5.1) and complete positive-corank cases (pp. 26--28). The first index
refers to the whole system. Collection nonvanishing is not componentwise
equivalence. The proof treats equal classical/strict coranks and a
difference of one separately, using large coefficient depth, bounded
finite parts and useful-prime selection. Both are retained as source
inputs; none is chosen from L026's semisimplicity.

[Wuthrich's primary text](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/fine.selmer.pdf#page=6)
is the same 25-page author version recorded in the parent review. Section
3's diagram and Lemma 3.1 (printed p. 6) give finite-index compact/fine
comparisons with the discrete fine group's Tate module, rather than an
integral equality. Proposition 4.1 (pp. 7--8; its complete proof coverage
is reused from the parent) retains finite restriction errors. These
results support the proposed matching, but do not themselves identify
L005's classical space or select a localization branch.

The duplicate/failure comparison in the parent assessment and
ATTEMPTS/031 was checked again. L014/L021's residual-system obstructions
and L013/L019's determinant/height tests are contrasts, not premises.
No new search for unchanged coverage, reproof of the cited structure
theorem, lemma write or mathematical script is warranted. The forthcoming
applicability proof must justify classical compact/discrete coefficient
matching and local Tate-module maps, retaining finite images. Continue
only if this gives the exact index criterion without a point basis; stop
if finite Sha, nonzero localization or height-radical surjectivity is
assumed. Source approval adds no mathematical evidence toward BSD.

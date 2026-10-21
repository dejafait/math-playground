# Cyclotomic semisimplicity and localization — source comparison

TARGET: Assess whether L026's cyclotomic augmentation semisimplicity forces nonzero p-localization of the classical rationalized Selmer group, without assuming positive rational rank or finite p-primary Sha.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for cyclotomic semisimplicity, nonzero Selmer localization and fine/strict control; newly read Kim's two positive-corank proof branches and Wuthrich's general fine-Selmer control/height statements. Queries and read ranges are recorded below; no novelty claim follows from search failure.
SOURCE_EVIDENCE: Kim, publisher-hosted author text used in L026, Sections 2.1/2.5, Definition 2.12, Theorem 2.13(5), Proposition 3.13, equation (5.1), Sections 5.3.2--5.3.4 and Section 6's two residual cases; Wuthrich, author fine.selmer.pdf, Sections 2.1/3/4, Proposition 5.3 and Theorem 6.1. Reused the existing full-Selmer height and auxiliary-field assessments.
COMPARISON: Kim explicitly retains both equal strict/classical corank and a one-corank difference; Wuthrich's control preserves fine corank but does not select a branch. His general Theorem 6.1 uses a separate fine-height hypothesis without finite Sha, whereas its rational-point corollaries add finiteness. None of these statements supplies the saved ordinary-semisimplicity implication.
GAP: Nonzero localization under L026 remains unproved; the ready limited specialization is an exact first-Kato-index localization criterion, not production of the required index or a claim that semisimplicity excludes the equality branch.
REASON: Stop direct import from control or height formulas; retain the arithmetic branch distinction as an independently testable threshold. A compact/discrete specialization is needed to apply the inspected first-index theorem to L005's actual localization map; no reproof of Kim or Wuthrich is justified.
SCOPE: This assessment covers the saved source comparison and only the bounded first-index specialization named below; it approves no new formal countermodel, arithmetic realization or semisimplicity-to-localization theorem.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; essential ordinary/strict exact-sequence and fine-control statements had not been inspected. Existing height coverage was reused, not counted as a fresh discovery.
COVERED_TARGET: Specialize Kim's first-index theorem and ordinary/strict exact sequence to L026 to characterize nonzero rationalized p-localization, retaining both source branches and finite localization images.

Retain every L026 hypothesis: non-CM E/Q, good ordinary p >= 5,
residual surjectivity, non-anomalous and Manin/Tamagawa coprimality,
E(Q_p)[p]=0, residual Kurihara nonvanishing with the fixed normalization,
central vanishing, sign +1 and the certified primitive quadratic
coefficient. Put S=Sel(Q,V_p E) as in L005, and retain L026's TM=0 and
two-dimensional specialization. Do not assume L018's prescribed basis
or zero finite quotient. No auxiliary-field hypotheses are part of this
proposed implication.

Essential local inputs for the review: L002, L005, L013, L019 and L026;
foundations/03--04; the existing height-radical assessment; and the
completed auxiliary-field assessment. No cross-notebook input is proposed.
The primary comparison below distinguishes theorems about the full Selmer
group from rational-point corollaries. No new mathematical result is
derived or inserted into lemmas during this literature-only step.

The desired threshold is loc_p|S nonzero. If obtained, it would settle
one prerequisite for Castella's nonzero strict Selmer construction on
curves satisfying its separate auxiliary conditions. It would not imply
q(kappa)=0 or positive rational rank, and therefore would not close BSD.
Continue only with an inspected arithmetic map/criterion testing the
zero-localization branch. Kim supplies such a criterion through the strict
corank and the first nonzero Kato-system index. It does not supply that
index from augmentation semisimplicity. Park direct control/height import;
do not replace Selmer by points or repeat L019's radical-surjection test.

## Primary statements and essential cases inspected

Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture
for elliptic curves*, [publisher-hosted author PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf),
the same 2025-05-12 version identified in L026 (40 PDF pages, printed
pagination begins at 0). Read Sections 2.1/2.5, printed pp. 10--15;
Proposition 3.13, p. 20; equation (5.1), p. 26; Sections 5.3.2--5.3.4,
pp. 27--28; Section 6's residual alternatives, pp. 32--33; and Proposition
7.1 (p. 33)/Conjecture 1.14/Theorem 1.15 (p. 8). Section 2 assumes p>=5
and residual surjectivity; the Kato/Kurihara comparison retains the
prime-to-p Manin constant. His p-strict condition is zero at p and
classical elsewhere. Compact and discrete groups use coefficient inverse
and direct limits respectively. These are not rational-point groups.

Definition 2.12 measures ord(kappa) by the minimum number of primes of a
nonzero component in the entire nontrivial system. Theorem 2.13(5) equates
it with strict corank. Proposition 3.13 compares nontrivial collections,
explicitly not componentwise nonvanishing. Equation (5.1) identifies the
classical/strict quotient with the dual cokernel of relaxed singular
localization. Sections 5.3.3--5.3.4 retain respectively equal coranks and
a difference of one. They examine a first nonzero Kato component and its
singular localization, using bounded finite strict groups and useful-prime
selection. Section 6 again keeps both residual branches: a mod-p
calculation alone does not select the rational branch. No such branch
selection is asserted here. Kim's fine-module semisimplicity Theorem 1.15
assumes Conjecture 1.14; it is not L026's ordinary-module conclusion.

Christian Wuthrich, *Iwasawa theory of the fine Selmer group*, J. Algebraic
Geom. 16 (2007), 83--109; [author text](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/fine.selmer.pdf),
25 pages, received 2005-11-08, with placeholder publication header.
New reads: Section 2.1 and Lemma 3.1, author pp. 5--6; Proposition 4.1
and its complete local/global error argument, pp. 7--8; Proposition 5.3,
p. 11; Theorem 6.1, pp. 12--13, and the proof's opening map comparison,
p. 15. His compact all-place and p-only fine groups differ by finite
index. Proposition 4.1 has finite restriction errors without finite Sha.
Theorem 6.1 uses nondegeneracy of the fine height, also without finite Sha,
and relates fine characteristic order to fine corank. The proof uses that
height assumption in its map comparison. Theorem 1.1 and the rational
formulas add finiteness. Ordinary semisimplicity is not substituted for
the fine-height premise. The earlier assessment had read the introduction;
the general theorem is newly inspected, not a correction of that limited
earlier citation.

## Applicability, duplicates and continuation

L026's retained residual/period premises permit the collection comparison
already justified there. Its dimension-two conclusion concerns L005's
compact rationalized Selmer space. The next specialization must justify
passing between that space, the discrete strict group and local Tate
modules; it must not presume inverse-limit surjectivity or treat finite
localization images as rationally nonzero. Wuthrich's compact/fine
finite-index statements provide supporting coverage for this matching.
No finite quotient F, Sha contribution or coefficient premise is removed.

Reuse [the height assessment](2026-10-04-cyclotomic-selmer-height-radical.md)
for Howard's ordinary first-height/augmentation criterion. It does not
identify a rational Kummer subspace or an ordinary-to-fine height
comparison. L013's localization is already nonzero; L019 tests a different
marked-Sha surjection. Neither is a counterexample to the saved implication.
Targeted checks of L014/L021, ATTEMPTS/014--015 and the existing derivative
and exterior assessments found no completed compact first-index
localization criterion under L026. L014's classical-system vanishing and
L021's residual finite-pair defect remain relevant restrictions, not bans
on this arithmetic criterion. The auxiliary-field comparison is reused
only for downstream relevance and its extra hypotheses.

The next target is the exact COVERED_TARGET above, with its standalone
[assessment](2026-10-14-first-kato-index-localization-criterion.md).
This is a known-source specialization requiring separate supervisor
approval next turn. Its sought result characterizes the localization
threshold by the first Kato-system index, with the finite-image case
explicit; it does not establish the successful index. Continue if the
compact/discrete matching is rigorous and leaves an independently
testable index condition. Abandon this reduction as a production route
if it silently assumes nonzero localization, finite Sha or Kummer
membership. A criterion alone cannot resolve BSD.

## Search and remaining qualifications

Queries on 2026-10-14:

- `cyclotomic Selmer semisimple localization fine Selmer p-adic height Wuthrich`
- `Selmer group localization nonzero semisimplicity cyclotomic augmentation elliptic curves`
- `Wuthrich Iwasawa theory fine Selmer group height semisimple pdf`
- `"Selmer" "localization" "semisimplicity" cyclotomic`
- `"strict" "Selmer" "semisimple"`
- `"Selmer" "localization" "nonzero" "cyclotomic" rank two`
- `"Kim" "Selmer" "strict" "corank" localization`
- `"localization" "Selmer" "semisimple" elliptic`

Search results on signed/nonordinary or CM towers, adjoint representations,
and unrelated new claimed converses were not used as theorem evidence.
No larger new source is essential to the bounded criterion specialization.
No original proof of Mazur--Rubin Theorem 5.2.12 or Kato Lemma 18.7 is
claimed: Kim imports them by precise reference; this step inspected his
statements and essential classical-comparison cases, not those originals.
Mathlib coverage of the full source statements and the proposed compact
specialization is not checked; no absence claim is made.

The current [Clay/Wiles statement](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf#page=2)
was checked at printed p. 2: the rank assertion and separate refinement
retain foundations/01's scope. Neither is advanced by this source review.

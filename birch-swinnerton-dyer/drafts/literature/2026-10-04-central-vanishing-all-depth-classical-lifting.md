# Pending assessment of all-depth classical lifting after central vanishing

TARGET: Test whether Kim's Selmer structure theorem and Cassels pairing upgrade C016a's p^2 lifting to compatible classical Selmer lifting at every coefficient depth, without assuming finite p-primary Sha.
CHECKED: 2026-10-04
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: No new search or theorem comparison for this stronger all-depth target is performed in the completed research step; reuse the existing Kim, Sakamoto and Kummer assessments when screening it.
SOURCE_EVIDENCE: Previously inspected inputs are Kim, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf, author text dated 2025-05-12, Theorem 1.8 and Corollaries 1.11/1.12; Sakamoto 2022, https://ems.press/content/serial-article-files/29299?nt=1, Theorem 2.20(2) and Proposition 3.19; Milne, https://www.jmilne.org/math/Books/EC2.pdf, Theorem IV.5.4 and the printed p. 129 Kummer diagram. Their full all-depth implication has not been assessed here.
COMPARISON: C016a establishes only the first coefficient surjection and infinitude of p-primary Selmer. Compare the proposed compatible lifting with the stronger known Selmer structure and pairing consequences before deriving anything; no novelty or full-statement coverage is claimed.
GAP: Determine whether both prescribed depth-two basis classes admit compatible classical lifts at all larger depths under C016a's hypotheses. Any successful lifting still leaves their rational Kummer membership and r >= 2 unresolved.
REASON: This target changes the conclusion from a single p^2 obstruction to all coefficient depths and is not an exact preapproved target in the saved assessment. Its separate source comparison is required; the completed step does not attempt it.
SCOPE: Retain C016a's non-CM ordinary non-anomalous hypotheses, surjective E[p], local-torsion/Manin/Tamagawa conditions, fixed P_(2,0) primes, minimal nonzero mod-p two-prime Kurihara premise and L(E,1)=0. Assume neither finite p-primary Sha nor positive rational rank; require no higher eligibility for the old primes.

## Proposed intermediate target and discriminating test

For S_m = Sel(Q,E[p^m]), the requested lifts would be classes x_i^(m)
for every m >= 2 with x_i^(2) = c_i, and with each coefficient map
[p]: S_(m+1) -> S_m sending x_i^(m+1) to x_i^(m), for i = 1,2.
This is classical coefficient lifting; it does not request new
prime-deletion system components at an index outside P_(m,0).

The first error is settled in C016a by the already assessed converse.
Repeating that converse or recomputing tau via an initial Fitting ideal
would be redundant. The remaining test should compare the known
structure theorem, the divisible part of p-primary Sha and its finite
paired quotient with the coefficient maps. Read any missing exact
statement needed for that comparison before calculating.

Continue this lifting route if the retained inputs force the indicated
compatible lifts. Stop the all-depth implication if an allowed finite
Sha contribution obstructs a later coefficient map. In either case,
distinguish compatible Selmer classes from rational points: the latter
must supply two rational directions to meet the required r >= 2 bound.
The main target remains r(E) = m(E) for arbitrary m(E) >= 2.

No all-depth result, countermodel, lemma or mathematical program for
this pending target is constructed here. The next source comparison
should reuse adequate prior coverage and approve a concrete mathematical
application if possible; no repeated browsing quota is intended.

## Mathlib

Full coverage of the proposed all-depth compatible lifting implication:
**not checked**. Supporting Selmer structure, divisible Sha, Cassels
pairing and coefficient Kummer maps: **not checked**. The named primary
sources are previously inspected supporting leads, not a claimed match
for this full target or Mathlib theorem names. No absence inference is made.

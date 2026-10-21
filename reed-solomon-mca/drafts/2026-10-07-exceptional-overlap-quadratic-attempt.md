# Exceptional overlap: comparison of two union-six lifts

Date: 2026-10-07. STEP_ID: 2026-10-07-mca-076-exceptional-quadratic.

Approved target: Prove or refute that every L033 union-six pencil over F_(97^20) with no weight-three parameter has at most twelve valid additional finite incidences.

Reuse the unchanged EXPLORE assessment in
[the twelve-incidence review](literature/2026-10-07-six-coordinate-twelve-incidence-bound.md).
Main gap: arbitrary-family sixteen-count equality. Intermediate test:
compare the two union-six lifts forced by L035's exceptional intersecting
tag pair. Their difference is a codeword supported on eleven labels;
shortening leaves a quadratic polynomial pencil. Seek a necessary,
nontrivial condition on the four paired label sets. This could exclude
labelings in the exceptional completion branch; the all-disjoint branch,
universal extraction and global fifteen remain independent gaps.
Continue if it supplies a checkable restriction beyond packing; abandon
this mechanism if it merely restates the shortened moment equations.
Only thirteen actual valid incidences meeting all L010 gates would
refute the approved bound.

Before extended reasoning, checked L035's complete packing proof and
L034's distribution argument against L010, L032 and L033. No defect was
found at the uses needed here; neither lemma receives separate audit
status in this research turn. Read the needed moment-kernel, affine-lift,
shortening and full-weight cases in those inputs. Targeted searches in
L031–L035 and the six-coordinate drafts found no two-lift quadratic
constraint. Reuse the saved source comparison and ATTEMPTS/017, /019,
/020; no stopped sampling or universal small-union route is reopened.

Unfinished reasoning saved before completion: write the exceptional
supports as {x,p,a,b}, {x,p,c,d}, and K_0={a,b,c,d}. They give the
alternate cluster U'={x,p,a,b,c,d}, whose overlap with the original U
is {x}. The common-tag pair has root at K_0's parameter in the new
affine lift. The difference of the original and new lifts vanishes
off U union U', so its polynomial is h(X)(q_0(X)+T q_1(X)), where
h has the five excluded labels as roots and deg q_i<=2. The two
original pairs not containing x and the two pairs {a,b}, {c,d}
each have equal coefficient directions in this quadratic pencil.
Must check pencil rank, possible common factors and the resulting
bilinear equation before recording a lemma. No bound is claimed.

Completed: [L036](../lemmas/L036-exceptional-overlap-quadratic-involution.md)
establishes the two-lift quadratic representation, independence of its
coefficient polynomials, and a rank-two test on four disjoint paired
label sets. The test forces a single nonidentity fractional linear
involution over F_97 to exchange all four pairs. Rank-three labelings
are excluded uniformly over the full F. An exact displayed minor is
84 modulo 97 for one H-labeling, demonstrating a failed label test;
this is not a complete support-family enumeration. No coprimality claim
is needed: independence and the equal-value cross product suffice for
the bilinear equation. Nondegeneracy of the involution follows from the
disjoint pairs, with its finite denominators checked separately.

This passes the intermediate test by adding a necessary label restriction
absent from L035's packing conditions. Outcome: ADVANCE / RESEARCH /
POTENTIALLY_NEW; local progress, not certified novelty beyond the inspected
sources. The canonical proof gives precise shortening citation and
applicability for five deletions and marks Mathlib coverage not checked.
No mathematical script, external browsing or finite sample was used.
The source assessment remains unchanged; its approved target explicitly
permits a rigorous intermediate obstruction to equality.

The twelve bound is neither proved nor refuted. All-disjoint tag pairs
and exceptional labelings passing the rank test remain; even a passing
labeling needs all weights, moments, locators and original finite-chart
conditions. Preserve those cases and continue the same approved target.
L034–L036 await separate critical audits; the needed dependency inspection
and the algebra check in this attempt do not confer that status. Global
fifteen, universal extraction and challenge identification remain open.

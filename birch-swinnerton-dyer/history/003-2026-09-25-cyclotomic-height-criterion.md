# 2026-09-25 — Cyclotomic height criterion

Preserved the existing edits and inactive attempts. The Clay source was
rechecked with unchanged scope. The
[saved selection](../drafts/2026-09-25-cyclotomic-height-criterion.md)
records the gap, intermediate target, downstream use, and test before the
source audit was completed.

The [source audit](../foundations/04-cyclotomic-height-criterion.md) found
the required sufficient theorem for all E/Q at an odd good-ordinary prime,
with finite p-primary Sha and nonzero canonical cyclotomic regulator
explicit. It also caught the standing non-CM hypothesis in the source
used for the converse. Access to Schneider's original full text failed;
the theorem number and general sufficient statement are checked through
the cited published restatement, with that limitation recorded.

[L003](../lemmas/L003-cyclotomic-height-semisimplicity.md) connects the
theorem to the invariant-to-coinvariant map. The exact algebraic threshold
is reached conditionally; the unrestricted result remains rank <=
characteristic order. The new input neither proves finite Sha or height
nondegeneracy for arbitrary curves nor compares characteristic order with
complex analytic order. There is no candidate proof or disproof of BSD.

Decision: retain the successful conditional height criterion. Merely
restating it cannot remove its two arithmetic hypotheses. The reason for
the next direction is to test whether independent points and an analytic
p-adic coefficient can give matching rank bounds and thus certify the
defects' vanishing. Producing such certificates at n = m(E) for arbitrary
curves would remain a separate unresolved task. The old finite-descent
and characteristic-ideal-only failures remain applicable to their data.

Mathematical review checked the classical Selmer conventions, p > 2 and
ordinary reduction, the four hypotheses of the sufficient theorem,
nonzero regulator normalization, and the converse's non-CM restriction.
The corank-zero argument uses finite generation of the Sha dual and
Pontryagin duality. L002 is the sole earlier mathematical lemma used;
the old abstract countermodels are motivation, not proof inputs. No
numerical computation was needed for this citation-and-deduction step.

The required command
`python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
passed with three nodes, one genuine direct mathematical edge, valid
links, and compact overviews. `git diff --check -- .` also passed.
Structural validation is not a verification of the arithmetic theorem.

Completed step BSD-2026-09-25-003-cyclotomic-height-criterion is ADVANCE:
a conditional standard arithmetic input has been established in the
notebook. This does not claim new general mathematics or an unconditional
advance to rank equality for arbitrary curves. Exploration turns without
an advance or informative negative result remain 0 of 3.

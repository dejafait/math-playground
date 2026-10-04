# 2026-10-04 — Fixed lower-Chern Bogomolov test

STEP_ID: 2026-10-04-hodge-086-fixed-lower-chern-bogomolov-test.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Reused the prior SPECIALIZE
[assessment](../drafts/literature/2026-10-04-fixed-lower-chern-stability-test.md)
and imported Perego's Corollary 6.42 without another source review.
[L046](../lemmas/L046-fixed-lower-chern-bogomolov-exclusion.md)
contracts the full fixed second character at the actual product
Kahler class and obtains (8+4lambda)q(omega_c,omega_c)>0.
The known necessary inequality has the opposite sign for c_1=0.

This excludes all positive-rank polystable locally free bundles
with these exact lower data, independently of higher characters
or K-class. It broadens the preceding fixed-class failure but
neither excludes arbitrary representatives of the cubic action
nor produces a new cycle. The result is a numerical reproduction
of known tools, not a claim beyond the checked literature.
The span remains 21, and attained RM directions three against four
required; the universal rational Hodge gap stays unresolved.

Preserved the existing changes, lower-degree survivor, fixed V'
failure and older route stops. Added the full proof, a calculation
checkpoint and the scoped failure record; updated the overview,
compact checkpoint and ID-only DAG for the genuine L044 input.
Consecutive mathematical exploration usage remains zero after
this informative negative result. No complete Hodge candidate arose.

The reason for the next direction is that this contradiction fixes
both pure point coefficients as well as the mixed action. The
already preapproved pure point correction test measures exactly
the numerical change needed before any existence work is useful;
it does not reopen the excluded data or assume stability.

Exact arithmetic in the cubic quotient field checked the final
tensor directly, including its 4 id divisor contribution, and
confirmed the positive polynomial contraction. The shared checker
`python3 ../scripts/docs/check_structure.py --problem hodge` passed:
47 nodes, 105 unique edges, acyclic graph, full file coverage and
valid local links. The only new mathematical edge is L046's use
of L044's fixed chamber and full lower character; L045 is a scope
comparison rather than an input. Structure checks do not prove the
inequality's applicability or the Hodge conjecture.

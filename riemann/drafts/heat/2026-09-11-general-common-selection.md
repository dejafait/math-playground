# General common selection — 2026-09-11

Checkpoint: inspected existing changes and completed Lemma 105; preserved all work.
Current step: extend the fixed-subset equivalence in Lemma 104.

Draft claim (unproved at this checkpoint): for arbitrary strictly increasing
positive x_n with summable reciprocal squares, common vanishing on an
infinite A is equivalent to bounded K_n=sum_{j>n}(x_j-x_n)^(-2) on A.
Summability implies x_n tends to infinity, hence each fixed K_n is finite
by x_j-x_n >= x_j/2 eventually. Lemma 74 supplies the product and
V_n <= 2H sum_{j>n}x_j^(-2) -> 0. The sufficiency estimate is unchanged.
For necessity, the continuity, threshold and marked-jump argument of
Lemma 104 only require individual K_n finite and unboundedness on A.

Resume: audit that argument under the general hypotheses, especially all
infinite sums and strict heights; store the canonical proof, graph,
history and final progress, then run structure and whitespace checks.

Completed: audited and stored as Lemma 106. The draft claim above is
now proved there; the resume note is historical. PROGRESS.md holds the
current next action.

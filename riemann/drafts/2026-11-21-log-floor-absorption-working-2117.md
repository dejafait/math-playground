# Logarithmic-floor absorption working note2117

Approved target: assessment `literature/2026-11-21-local-count-absorption-review-2115.md`, SPECIALIZE at invocation start. One mathematical specialization; no new source search.

Put s=sqrt(x^2+R^2), L=log(2+s), eta=1/(1000L), p=w eta.
Candidate proof: |w'|<=w/R, |L'|<=1/R, L>5, hence
|p'|<=(6/5)w/(1000RL). For |x|>=2R, C488c gives nearby
count <=100RL, paying at most (3/25)w/|y|. For |x|<2R,
C488a(4) gives count <=(3R+20)log(12R+40)<= (31/5)RL,
paying at most (93/12500)w/|y|. Check the logarithm comparison
by (R+2)^2>12R+40 for R>=200. The scalar kernel estimate is
2|d||y|<=d^2+y^2. No lower ordinate or separation is used.

Completed in canonical C488d with hypotheses, exact closed cutoffs and multiplicities.
This pays only the nearby real-partner p' cost; no derivative of a
multiple-zero branch, total differential inequality, all-height reality,
overlap, or mixed positivity is asserted. Review must separately check
these calculations and their count domains. Main gap remains L030-L032/C032a.

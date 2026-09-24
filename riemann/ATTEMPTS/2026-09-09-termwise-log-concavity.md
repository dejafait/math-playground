# Attempt: sum the individual theta log-concavity statements

Date: 2026-09-09

Outcome: failed general inference; the actual theta sum still admits a quantitative approach.

The mathematical counterexample or obstruction is proved in [Lemma 46](../lemmas/L046-the-variance-obstruction-in-a-sum-of-log-concave-terms.md).

**WHY IT FAILS.** The variance of the logarithmic slopes is nonnegative and can outweigh the negative individual curvatures. For the explicit pair e^{-(u-2)²}, e^{-(u+2)²}, each log curvature is -2 but the sum's log curvature at zero is 14. Thus summing individual log-concavity inequalities is invalid. For the theta kernel a separate domination estimate might control the variance, because higher n terms are exponentially small; that estimate, not the generic preservation claim, must carry the argument.

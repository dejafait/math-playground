# Attempt: sum the individual theta log-concavity statements

Date: 2026-09-09

Outcome: failed general inference; the actual theta sum still admits a quantitative approach.

Each K_n is strictly log-concave by Lemma 45. The tempting conclusion was that K=ΣK_n must therefore be log-concave. The differentiated sum actually gives (log K)''=Σw_n(log K_n)''+Var_w((log K_n)').

**WHY IT FAILS.** The variance of the logarithmic slopes is nonnegative and can outweigh the negative individual curvatures. For the explicit pair e^{-(u-2)²}, e^{-(u+2)²}, each log curvature is -2 but the sum's log curvature at zero is 14. Thus summing individual log-concavity inequalities is invalid. For the theta kernel a separate domination estimate might control the variance, because higher n terms are exponentially small; that estimate, not the generic preservation claim, must carry the argument.

Next lemma: bound the actual theta variance using K_n/K_1≤2n⁴e^{-(n²-1)v}, v=πe^{2u}, and compare it with the negative mean curvature.

# Attempt: transfer ordinary moment Gram positivity through the logarithm

Date: 2026-09-09

Outcome: failed preservation principle; actual ordinary Gram positivity remains proved.

The positive theta kernel gives G_d=(M_{2m+2n})>0 for every d. The desired matrices H_d use the coefficients of log Ξ instead. The attempted step was to transfer positivity from all G_d to these logarithmic-coefficient matrices automatically.

For g(u)=exp(-cosh(2u)), use the positive even mixture h(u)=(9/10)g(u)+(g(u-8)+g(u+8))/20. Its ordinary Gram matrices are all positive definite. Its normalized fourth cumulant is κ_4=ν_4-3ν_2²+(7/100)8⁴, where ν are g's normalized moments. The Gaussian comparison in Lemma 44 proves ν_2<3/2, hence κ_4>27997/100. Therefore its corresponding logarithmic quantity T_2=-κ_4/12 is negative.

**WHY IT FAILS.** The passage from moments to coefficients of the logarithm introduces subtractions, not an operation preserving positive Gram matrices. The explicit positive smooth even superexponential mixture already produces a negative scalar T_2 despite positivity of every ordinary moment Gram matrix. Thus the correct integral representation for G_d cannot simply be reused for H_d. The specific theta kernel might possess additional structure, but that extra structure would need a separately proved inequality; positivity and moment existence alone do not supply it.

Next lemma: seek a concrete stronger property of the actual theta kernel rather than relabeling ordinary moment positivity. A candidate is a direct analytic inequality for logarithmic derivatives or a controlled test of kernel log-concavity; neither is currently established as sufficient for RH.

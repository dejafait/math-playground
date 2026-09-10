# Lemma 45: strict log-concavity of each theta-kernel summand

**Hypotheses.** n≥1, u≥0, v_n=πn²e^{2u}, and K_n is as in Lemma 35. Put ℓ_n(u)=log K_n(u), which is defined since K_n>0.

**Conclusion.**

ℓ_n'(u)=9/2-2v_n+6/(2v_n-3),

ℓ_n''(u)=-4v_n-24v_n/(2v_n-3)²<0.

Thus every individual K_n is strictly log-concave on [0,∞).

**Proof.** Factor K_n=4v_n(2v_n-3)e^{u/2}e^{-v_n}, with v_n≥π>3 and v_n'=2v_n. Its logarithm is log 4+log v_n+log(2v_n-3)+u/2-v_n. Differentiation gives 5/2+4v_n/(2v_n-3)-2v_n=9/2-2v_n+6/(2v_n-3). Differentiating once more gives the displayed negative expression. Every denominator is strictly positive on the stated domain, so both differentiations are valid. ∎

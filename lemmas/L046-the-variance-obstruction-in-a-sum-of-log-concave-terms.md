# Lemma 46: the variance obstruction in a sum of log-concave terms

**Hypotheses.** Positive C² functions f_n on a real interval have locally uniformly convergent sums of f_n, f_n', f_n'', and f_n'^2/f_n. Set f=Σ_n f_n>0, w_n=f_n/f, and ℓ_n=log f_n.

**Conclusion.**

(log f)''=Σ_nw_nℓ_n''+Σ_nw_n(ℓ_n'-Σ_jw_jℓ_j')².

These hypotheses hold for f_n=K_n on u≥0. Even if every ℓ_n'' is negative, (log f)'' need not be negative.

**Proof.** The convergence hypotheses justify f'=Σf_n' and f''=Σf_n''. Since f_n''=f_n(ℓ_n''+(ℓ_n')²), substitution into (log f)''=f''/f-(f'/f)² gives the mean-curvature plus variance identity. The squared sum is well-defined by the assumed convergence and Cauchy–Schwarz for the nonnegative weights. For K_n, Lemma 45 and the explicit K_n formula bound every relevant summand, on each compact u-interval, by a fixed polynomial in n times e^{-πn²}; the rational denominators are bounded away from zero. These bounds give all required local uniform convergence, including termwise derivatives.

For the failure example, f_1(u)=e^{-(u-2)²} and f_2(u)=e^{-(u+2)²} each have log second derivative -2. Their sum is 2e^{-u²-4}cosh(4u), whose log second derivative at u=0 is -2+16=14>0. Thus termwise log-concavity alone cannot remove the variance term. ∎

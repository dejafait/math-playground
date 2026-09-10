# Lemma 50: a small superexponential mixture remains strictly log-concave

**Hypotheses.** a=1/100, g(u)=exp(-cosh(2u)), and h_a(u)=(9/10)g(u)+(g(u-a)+g(u+a))/20 on R.

**Conclusion.** h_a is strictly log-concave on all R; more quantitatively,

(log h_a(u))''<-(1/4)cosh(2u).

Its entire Fourier transform still has nonreal zeros from its factor (9+cos(az))/10.

**Proof.** Regard the three terms as p_i exp(-V_i(u)), with shifts t_i∈{-a,0,a}, weights p_i∈{1/20,9/10,1/20}, and V_i(u)=cosh(2(u+t_i)). Write C=cosh(2u)≥1 and B=sinh(2a). The elementary exponential-series bound e^x≤1/(1-x) for 0<x<1 gives e^{2a}<2 and B<1/49<1/40. For every shift, V_i≥e^{-2a}C>C/2, so the mean logarithmic curvature is Σw_i(-4V_i)<-2C.

The three logarithmic slopes are -2sinh(2(u+t_i)). Their range is exactly 4CB. For any real variable in an interval of length L, its variance is ≤L²/4: expand the nonnegative product (X-min)(max-X), then bound (mean-min)(max-mean) by L²/4. Thus the slope variance is ≤4C²B²<C²/400. If C≤128, this is at most (8/25)C, giving total curvature <-(42/25)C.

For the remaining region use the identity Var_w(ℓ_i')=Σ_{i<j}w_iw_j(ℓ_i'-ℓ_j')². Put Δ=V_i-V_j. The ratio of any two weights p_i,p_j is at most 18, and the denominator of w_iw_j is at least either unnormalized term squared; hence w_iw_j≤18e^{-|Δ|}. The hyperbolic addition identities give

(V_i'-V_j')²=4Δ²+16sinh²(t_i-t_j)≤4Δ²+16B².

For x≥0, x²e^{-x}≤4/e²<1. Each pair therefore contributes <72+288/1600=3609/50 to the variance, so all three contribute <10827/50. If C≥128, combining this with mean curvature <-2C gives

(log h_a)''<[-2+10827/6400]C=-(1973/6400)C<-C/4.

This and the first region prove the uniform conclusion. Smoothness, evenness, positivity, and superexponential decay follow from the explicit positive shifts, as in Lemma 22. Real substitution in the entire Fourier integral gives F_a(z)=[9+cos(az)]G(z)/10; taking z=(π+i log(9+√80))/a makes the prefactor zero. This supplies a global small-shift proof rather than assuming log-concavity is stable under shifts. ∎

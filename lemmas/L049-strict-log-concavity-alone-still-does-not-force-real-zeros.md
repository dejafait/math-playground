# Lemma 49: strict log-concavity alone still does not force real zeros

**Hypotheses.** g(u)=e^{-u²}, h(u)=(9/10)g(u)+(g(u-1/2)+g(u+1/2))/20, and F(z)=∫_R h(u)e^{izu}du.

**Conclusion.** h is smooth, strictly positive, even, and strictly log-concave, with (log h)''≤-1. Nevertheless F has nonreal zeros and its local logarithmic quantity T_2, defined as in Lemma 44, is -7/19200<0. This example has Gaussian decay, not the theta kernel's superexponential decay scale.

**Proof.** Factor h(u)=e^{-u²}L(u), where L(u)=9/10+(e^{-1/4}/20)(e^u+e^{-u}). The three positive exponential terms in L have constant logarithmic slopes 0,1,-1 and zero logarithmic curvature. The finite version of Lemma 46 therefore gives (log L)'' equal to their weighted slope variance, at most their weighted second moment, which is ≤1. Thus (log h)''=-2+(log L)''≤-1. Positivity, evenness, and smoothness are immediate.

The Gaussian Fourier transform and real shifts give

F(z)=√πe^{-z²/4}[9+cos(z/2)]/10.

For b=log(9+√80)>0, cosh b=9, so z=2π+2ib is a nonreal zero. All transforms and their derivatives are entire by Gaussian exponential-moment domination on compact z-sets. Finally the normalized Gaussian has second moment 1/2 and fourth moment 3/4, so its fourth cumulant is zero. The shift calculation in Lemma 44, now with shift 1/2 and total shifted weight 1/10, gives fourth cumulant (7/100)(1/2)^4=7/1600. Hence T_2=-(7/1600)/12=-7/19200. This demonstrates that strict log-concavity is insufficient on its own; the example does not refute a theorem using the additional theta-scale decay or other specific theta identities. ∎

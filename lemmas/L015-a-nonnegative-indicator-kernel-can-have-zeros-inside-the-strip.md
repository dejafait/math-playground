# Lemma 15: a nonnegative indicator kernel can have zeros inside the strip

**Hypotheses.** v(u) is the indicator of [0,1]∪[2,4], and H(s)=∫_0^∞v(u)e^{-su}du.

**Conclusion.** H is entire, is positive for every real s, and has a nonreal zero s with 0<Re(s)<(log 2)/2<1.

**Proof.** The compact support makes the integral entire (differentiate under the integral, bounded on every compact set), and its integrand is positive for real s on a set of positive measure. For s≠0, direct integration gives

H(s)=(1-e^{-s})(1+e^{-2s}+e^{-3s})/s.

Consider Q(z)=1+z²+z³. Its derivative is z(2+3z). Q(-2)=-3 and Q(-1)=1. Its stationary values are Q(-2/3)=31/27 and Q(0)=1. The derivative signs show that Q has exactly one real root r, lying in (-2,-1). By the fundamental theorem of algebra and real coefficients, the remaining roots z and conj(z) are nonreal. Vieta's formula gives r|z|²=-1, so 1/2<|z|²<1. Choose any complex logarithm of this individual nonzero number z and set s=-Log z. Then e^{-s}=z and

0<Re(s)=-log|z|=(log(-r))/2<(log 2)/2<1.

This s is nonreal and nonzero because z is nonreal. The displayed factorization gives H(s)=0. The elementary bound log 2<1 follows from ∫_1^2 dx/x<1. No numerical root estimates are used. ∎

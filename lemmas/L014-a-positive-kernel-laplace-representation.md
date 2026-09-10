# Lemma 14: a positive-kernel Laplace representation

**Hypotheses.** Re(s)=σ>0. Let w(x) be 1 on the union of [2n-1,2n), n≥1, and 0 elsewhere on [1,∞).

**Conclusion.**

η(s)/s=∫_1^∞ w(x)x^{-s-1}dx=∫_0^∞w(e^u)e^{-su}du.

Both integrals converge absolutely and locally uniformly on Re(s)>0.

**Proof.** On each interval [2n-1,2n], integrating the derivative of x^{-s} gives

(2n-1)^{-s}-(2n)^{-s}=s∫_{2n-1}^{2n}x^{-s-1}dx.

Summing through n=N gives η_{2N}(s) on the left. On the right, absolute integrability follows from 0≤w≤1 and ∫_1^∞x^{-σ-1}dx=1/σ; the omitted integral is bounded by (2N+1)^{-σ}/σ. Pass to the limit using Lemma 12 and divide by s≠0. The substitution x=e^u proves the second identity. For Re(s)≥δ>0 the absolute tails are bounded by the corresponding tails of x^{-δ-1} or e^{-δu}; these bounds also give local uniform convergence. ∎

# Lemma 16: theta transformation and exponential tails

**Hypotheses.** x>0 is real. Define θ(x)=Σ_{n∈Z}e^{-πn²x} and ψ(x)=Σ_{n≥1}e^{-πn²x}, so θ=1+2ψ.

**Conclusion.** θ(x)=x^{-1/2}θ(1/x). For x≥1 and each integer j≥0 there is a finite constant C_j such that |ψ^{(j)}(x)|≤C_j e^{-πx}.

**Proof.** Use the standard named Poisson summation theorem for Schwartz functions with Fourier transform f̂(y)=∫_R f(u)e^{-2πiuy}du. The Gaussian f_x(u)=e^{-πxu²} is Schwartz. Its Fourier transform is x^{-1/2}e^{-πy²/x}: the Gaussian integral gives f̂_x(0)=x^{-1/2}, while differentiation under the integral and integration by parts give f̂_x'(y)=-(2πy/x)f̂_x(y), which determines the transform. Both operations are justified by Gaussian integrability of polynomials times f_x. Poisson summation Σ_n f_x(n)=Σ_n f̂_x(n) proves the transformation; both sums converge absolutely.

For the tail estimate, termwise j-fold differentiation gives ψ^{(j)}(x)=Σ_{n≥1}(-πn²)^j e^{-πn²x}. On x≥1 its absolute sum is at most

e^{-πx} Σ_{n≥1}(πn²)^j e^{-π(n²-1)} = C_j e^{-πx}.

The constant is finite since exponential decay dominates every fixed polynomial. These bounds and the Weierstrass uniform convergence test also justify each termwise derivative (or apply the same bounds successively on compact x-intervals in (0,∞)). ∎

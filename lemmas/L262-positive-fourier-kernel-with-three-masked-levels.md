# Lemma 262: a positive Fourier kernel retains three masked Laguerre levels

**Hypotheses.** Set b=1/4, ε=1/40, P(z)=z(z²−ε²)(z²−4ε²)(z²+b²), E(z)=P(z−10)P(z+10), and F(z)=−exp(−z²)E(z). Define D_n as the coefficient of y^(2n) in F(x+iy)F(x−iy).

**Conclusion.** There is a strictly positive even Schwartz function K on the real line such that F(z)=∫_ℝ K(t)exp(izt)dt for every complex z. Every zero of F is simple, including ±10±i/4, and every zero obeys |Re z|>4 and |Im z|<1/2. For every real x, D_n(F;x)>0 for n=1,2,3. F has order two, not theta's order one. These combined properties therefore do not suffice generically for real zeros.

**Proof.** Put Q=−E and define c_0,…,c_7 by

Σ_(k=0)^7 c_k v^k = ∏_(r∈{10−2ε,10−ε,10,10+ε,10+2ε})(v+r²) · [v²+(200−2b²)v+(100+b²)²].

Pairing the real roots and multiplying the four nonreal-root factors gives Q(z)=Σ_k (−1)^k c_k z^(2k). All c_k are strictly positive. Let g(t)=exp(−t²/4)/(2√π), whose Fourier transform with the stated convention is exp(−z²), and set K=Σ_k c_k g^(2k). Integration by parts gives the transform of g^(2k) as (−1)^k z^(2k)exp(−z²). Boundary terms vanish even for complex z, since each derivative is a polynomial times a Gaussian. This proves the transform identity, with absolute convergence everywhere.

It remains to prove positivity, not just the transform identity. Put u=t/2. Differentiating the Gaussian gives

g^(2k)(t)/g(t)=Σ_(l=0)^k (−1)^(k−l)(2k)! u^(2l)/[(k−l)!(2l)!4^(k−l)].

For example this follows by extracting the coefficient of h^(2k) in g(t+h)/g(t)=exp(−uh−h²/4). Thus K(t)/g(t)=Σ_(l=0)^7 h_l u^(2l), where

h_l=Σ_(k=l)^7 c_k (−1)^(k−l)(2k)!/[(k−l)!(2l)!4^(k−l)].

Here is a finite rational arithmetic certificate of all eight signs. The entries m_l in order l=0,…,7 are

966, 915, 883, 869, 872, 893, 934, 1000.

Substitution in the displayed product and sum gives m_l c_l ≤ 1000h_l < (m_l+1)c_l for every l. These are exact rational inequalities, not rounded floating-point estimates; a full reproduction using only integer and rational operations is `python3 scripts/laguerre/gaussian_masking_check.py`. Since c_l>0 and m_l>0, every h_l>0. In particular the constant is positive, so K(t)>0 everywhere. Its evenness and Schwartz decay follow from the polynomial-times-Gaussian formula.

L261 applies because ε/b=1/10≤1/√20, giving the simple zero assertions and the three strict signs for E. The multiplier has no zeros, and

F(x+iy)F(x−iy)=exp(−2x²)exp(2y²) E(x+iy)E(x−iy).

Consequently D_n(F;x)=exp(−2x²)Σ_(j=0)^n 2^j D_(n−j)(E;x)/j!. For n≤3 all summands are nonnegative and the j=0 term is strictly positive. Finally polynomial growth times exp(−z²) gives order at most two, and growth along z=ir gives log|F(ir)|=r²+14 log r+O(1), proving order exactly two. ∎

The attained threshold is positive Fourier-kernel compatibility with three strict levels, simplicity, and coarse localization. The required threshold is still actual-theta all-degree positivity or another sufficient theta-specific assertion. This is neither an arbitrary-finite-level theorem nor a counterexample to RH; no theta modular identity or complete-monotonicity assertion is supplied.

**Mathlib.** Not checked for the full statement or supporting Gaussian Fourier and polynomial identities. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/

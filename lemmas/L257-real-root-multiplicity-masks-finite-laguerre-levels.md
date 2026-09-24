# Lemma 257: real-root multiplicity masks any finite set of Laguerre levels

**Hypotheses.** Fix an integer K≥1, b>0, and m=2K−1. Put J(z)=z^m(z²+b²). For a real polynomial F let D_n(F;x) be the coefficient of y^(2n) in F(x+iy)F(x−iy), including D_0(F;x)=F(x)².

**Conclusion.** For every real x and 1≤n≤K, D_n(J;x)≥0, although J has nonreal zeros ±ib. For K=2 one has explicitly

D_1(J;x)=x⁴(5x⁴+4b²x²+3b⁴),
D_2(J;x)=x²(10x⁴+3b⁴).

Nevertheless D_(m+1)(J;0)=−2b²<0. The even polynomial E(z)=J(z−10)J(z+10), with b=1/4, also satisfies D_n(E;x)≥0 for every real x and 1≤n≤K. All its zeros obey |Re z|>4 and |Im z|<1/2, and it retains nonreal zeros. These examples depend on K; no one example is asserted to pass all levels.

**Proof.** Write s=x² and t=y². Direct multiplication gives

J(x+iy)J(x−iy)=(s+t)^m[(s+b²)²+2(s−b²)t+t²].

For 1≤n≤K one has n≤m. Set A=binom(m,n), B=binom(m,n−1), C=binom(m,n−2), taking the last binomial to be zero when n=1. Extracting the coefficient of t^n yields

D_n(J;x)=s^(m−n)[(A+2B+C)s²+2b²(A−B)s+A b⁴].

For n=1 the term involving C is absent; the displayed formula still holds, including s=0, as a polynomial identity. The ratio A/B=(m−n+1)/n≥1 because m=2K−1≥2n−1. Thus every coefficient in the bracket is nonnegative, with positive constant term, proving the asserted signs on s≥0 without dividing by J(x). Substitution of m=3 gives the two explicit formulas. At x=0 the generating polynomial is t^m(b²−t)², whose coefficient of t^(m+1) is −2b². This also exhibits a higher-level detection rather than inferring it from a real-zero criterion.

For any two real polynomials U,V, multiplication of the finite generating polynomials gives

D_n(UV;x)=Σ_(j=0)^n D_j(U;x)D_(n−j)(V;x).

Translation gives D_j(J(z−c);x)=D_j(J;x−c). Hence all terms in this convolution are nonnegative for n≤K for the two translated factors defining E. Since m is odd, J is odd, so E(−z)=E(z). Its complete list of zeros is ±10, each of multiplicity m, together with 10±ib and −10±ib. With b=1/4 these obey the stated strict localization and include nonreal zeros. ∎

The exact achieved threshold is nonnegativity of every level up to any prescribed finite K on the entire real axis. The main required mixed positivity and the all-level global Laguerre condition are stronger. The construction uses repeated real roots (for K≥2); it proves neither strict positivity at those roots nor a counterexample under a simple-zero hypothesis. No positive Fourier-kernel representation, theta identity, or RH counterexample is asserted. It differs from finite Hankel tests at one expansion center: the inequalities here hold at all real centers.

**Mathlib.** Not checked for the full statement or supporting binomial and coefficient-convolution identities. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/

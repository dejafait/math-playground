# Lemma 265: nonreal deflation retains the witness normalization gap

**Hypotheses.** Let F be a nonzero entire function real on the real axis, with a zero rho=a+ib of exact multiplicity k≥1, where a is real and b>0. Put

F(z)=((z-a)²+b²)^k G(z),
A=|F^(k)(rho)/k!|,
T=|G(a)/G(rho)|.

The quotient is understood by removable continuation. For the theta specialization take F=Ξ as in L259, assume Ξ(a)≠0, choose R>b, and write U(R)=Ξ(iR), q=b²/R².

**Conclusion.** The function G is entire and real on the real axis, G(rho)≠0, and

|F(a)|=(b/2)^k A T.

Consequently L259's sufficient witness cutoff is exactly

N_R=ceil(log(4^k U(R)²/[b^(2k) A² T²(1−q)])/log(1/q)).

For an integer J≥1, the condition N_R≤J is equivalent to the lower-bound requirement

A T ≥ (2/b)^k U(R) q^(J/2)/sqrt(1−q).

Derivative normalization does not algebraically eliminate T. Even among real entire polynomials with simple zeros, fixed b, and bounded circle growth after derivative normalization, T can tend to zero while A stays bounded away from zero. Removing the nonreal pair can also leave a quotient with all nonnegative Laguerre coefficients, so a negative witness for the quotient cannot be inferred from the removed zero. These are limitations of the proposed normalization argument, not claims about actual zeros of Ξ.

**Proof.** Reality gives a zero of multiplicity k at the distinct point conjugate(rho). Division by the two factors therefore has removable singularities and gives an entire real G. Exact multiplicity implies G(rho)≠0. Near rho,

F(z)=(z-rho)^k(z-conjugate(rho))^k G(z),
F^(k)(rho)/k!=(2ib)^k G(rho).

At a, F(a)=b^(2k)G(a). Taking absolute values proves the identity. In the theta case F(a)≠0 makes T positive, and substituting its squared identity in L259 gives the asserted cutoff. For integral J, ceil(x)≤J if and only if x≤J. Exponentiating with log(1/q)>0 and rearranging gives precisely the displayed lower bound. Thus even a lower estimate for A alone would not be the required estimate.

One can bound the deflated function from above on |z-a|=R: both distances |z-rho| and |z-conjugate(rho)| are at least R−b, so L259's theta majorant gives

|G(z)|≤U(R)/(R−b)^(2k).

This is an upper bound only; it gives no positive lower estimate for T. Dividing G by G(rho) leaves the upper bound with a derivative denominator and leaves its central value equal in modulus to T.

For an exact diagnostic fix b>0 and 0<epsilon<b, set w=z-a, and take

F_epsilon(z)=(w²+b²)(w²−epsilon²), G_epsilon(z)=w²−epsilon².

All four zeros are simple. At rho=a+ib,

A_epsilon=2b(b²+epsilon²),
T_epsilon=epsilon²/(b²+epsilon²),
|F_epsilon(a)|=b² epsilon².

Hence A_epsilon≥2b³ but T_epsilon tends to zero. Fix R>b. On |z-a|=R,

|F_epsilon(z)|≤(R²+b²)(R²+epsilon²).

The real normalization F_epsilon/A_epsilon therefore has uniformly bounded circle maximum as epsilon tends to zero and derivative modulus one at rho. Nevertheless, for H_epsilon(y)=F_epsilon(a+iy)F_epsilon(a−iy), its actual maximum M_epsilon on |y|=R satisfies

M_epsilon/|F_epsilon(a)|²
 ≥ (R²−b²)²(R²+epsilon²)²/(b^4 epsilon^4) → infinity.

Indeed evaluating at the real point y=R gives that numerator exactly. Scaling F by any nonzero real constant leaves this ratio unchanged. Thus the Cauchy cutoff based on even the exact circle maximum diverges at fixed b,R despite this derivative normalization.

Deflating the pair removes the premise H(b)=0 used in L258. Here the quotient has, at any real center x with v=x-a,

G_epsilon(x+iy)G_epsilon(x−iy)
 =(v²−epsilon²)²+2(v²+epsilon²)y²+y^4,

whose coefficients are all nonnegative. For contrast the original function at a has

H_epsilon(y)=(b²−y²)²(y²+epsilon²)²,

and its y^6 coefficient is 2(epsilon²−b²)<0. Thus the example does not show that the true first witness index diverges: a witness occurs by index three. It shows precisely that the proposed Cauchy bound remains ill-conditioned and that one cannot transfer the negative-witness premise to the deflated quotient. ∎

If Ξ(a)=0, T=0 and this cutoff is inapplicable; L258's separate real-center deflation must still be used. Nothing here supplies a lower bound for its first nonzero central derivative either. The required actual-theta product lower bound above and exterior signs through the resulting cutoff are both unresolved. No height-only bound, nonreal theta zero, or impossibility of a different witness estimate is asserted.

**Mathlib.** Not checked for the full statement or supporting removable division, multiplicity/derivative identity, and polynomial coefficient calculations. No matching theorem or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/

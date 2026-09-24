# Lemma 254: second-spectrum theta index pairing obstruction

**Hypotheses.** For n≥1 and u≥0 set

q_n(u)=(8π²n⁴e^(9u/2)−12πn²e^(5u/2))exp(−πn²e^(2u)),
k_n(u)=q_n(|u|), F_n(x)=∫_R k_n(u)e^(ixu)du, d_n=q_n′(0).

Let k=Σ_n k_n be the actual even theta kernel, F=Σ_n F_n, and A₂(t)=∫_R s⁴k(s+t)k(s−t)ds. Define the symmetric bilinear expression

B_nm(x)=[F_n F_m⁗+F_m F_n⁗−4(F_n′F_m‴+F_m′F_n‴)+6F_n″F_m″]/32.

**Conclusion.** For every real x the absolutely convergent double series satisfies

Â₂(2x)=Σ_{n,m≥1} B_nm(x).

For each fixed pair n,m, as x→+∞,

B_nm(x)=9d_n d_m x^(−8)+O_nm(x^(−10)).

Here d_1>0 and d_m<0 for m≥2. Thus every unordered block B_1m+B_m1 with m≥2 is eventually strictly negative. Pairing only the two index orders cannot give nonnegative summands. This does not rule out larger, frequency-dependent groupings or prove that the total spectrum is negative.

**Proof.** L019 gives q_n>0 and every absolute moment of k finite. Tonelli therefore gives, for each integer 0≤j≤4,

Σ_n ∫_R |u|^j k_n(u)du=∫_R |u|^j k(u)du<∞.

Differentiation under each integral is valid, and the derivative series Σ_n F_n^(j)(x) converges absolutely and uniformly for real x by this same bound. Consequently all products in B_nm have absolutely convergent double sums. Summing them gives [FF⁗−4F′F‴+3F″²]/16, which equals Â₂(2x) by L253. Equivalently this is the symmetrized double theta-series Fourier integral; its absolute convergence follows from ∫∫(|u|+|v|)^4k(u)k(v)du dv<∞. No positivity of its oscillatory integrand is asserted.

For fixed n every derivative of q_n, with any polynomial weight in u, is integrable and vanishes at infinity. Repeated half-line integration by parts, applied separately to u^j q_n for 0≤j≤4 in the cosine or sine integral for F_n^(j), gives

F_n^(j)(x)=−2d_n(−1)^j(j+1)!x^(−2−j)+O_n,j(x^(−4−j)).

Here no derivative of a big-O remainder is taken. To check the boundary order, the first derivative of the appropriate parity of u^j q_n that contributes is of order j+1 and equals (j+1)!d_n; the order j term has the wrong parity. The next possible contributing order is j+3. Integrating further bounds the remainder by a fixed boundary derivative and the L¹ norm of a higher derivative. This is the same half-line argument as in L234, now through j=4.

The leading coefficients for j=0,1,2,3,4 are respectively −2d_n, 4d_n, −12d_n, 48d_n, −240d_n. Substitution into B_nm gives

[960−1536+864]d_n d_m/32=9d_n d_m.

Each remaining product is O_nm(x^(−10)). L234 proves the exact modular cancellation Σ_n d_n=0, absolute convergence of this sum, and

d_n=−2πn²(2πn²−1)(4πn²−15)e^(−πn²).

It also proves d_1>0 and d_m<0 for m≥2. Thus the leading coefficient of 2B_1m is strictly negative, proving the assertion for each fixed m.

The modular cancellation makes the formal sum of the leading coefficients 9(Σ_n d_n)²=0. This algebraic sum is legitimate because Σ|d_n|<∞, but it is not a uniform Fourier asymptotic: the fixed-pair remainders have not been bounded uniformly in the indices. In particular it gives neither a sign nor a nonzero lower bound for the full spectrum. ∎

The required threshold remains Σ_nm B_nm(x)≥0 for every real x. Negative unordered blocks refute only the proposed termwise proof. Modular reflection is already used to represent k by its positive half-line terms and to cancel the total boundary derivative; it does not make these individual blocks nonnegative. Higher associated levels and all-degree mixed positivity remain unresolved.

**Mathlib.** Not checked for the full statement or supporting series, Fourier differentiation, and integration-by-parts results. No matching theorem is claimed. Reference portal: https://leanprover-community.github.io/mathlib4_docs/

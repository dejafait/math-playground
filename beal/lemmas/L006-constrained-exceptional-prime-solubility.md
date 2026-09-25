# L006 — The constrained cube branch lifts at 2 and 3

## Hypotheses

Fix an odd integer p >= 5 and positive integers u,v with u odd and v congruent to 1 modulo 12. In particular, the conclusion applies at the active residual primes p >= 19 congruent to 1 modulo 3. Set

\[
K=3^{2p-3},\qquad s=3^{p-1}u^p,\qquad
\Delta=4v^p-Ku^{2p},\qquad c=3uv.
\]

These are the parameters of L003's system II. The restrictions from L005 motivate the hypotheses; its theorem about integer solutions is not applied to local points. Local primitivity means that every pair of coordinates contains a unit at the specified prime. Valuations are those of nonzero elements of the relevant local field.

## Conclusion

For each ell in {2,3}, there is a nonzero d_ell in Z_ell with

\[
d_\ell^2+Ku^{2p}=4v^p.
\]

The roots have compatible reductions at every power of ell. The coordinates

\[
a_\ell=(s+d_\ell)/2,\qquad
b_\ell=(s-d_\ell)/2,\qquad c=3uv
\]

are nonzero elements of Z_ell and solve a_ell^3+b_ell^3=c^p. They are pairwise locally coprime and have the exact required valuations:

\[
\begin{array}{c|c}
\ell=2&v_2(a_2b_2)=1,\quad v_2(c)=0,\quad v_2(s^2-d_2^2)=3,\\
\ell=3&v_3(a_3)=v_3(b_3)=v_3(d_3)=0,\quad v_3(c)=1+v_3(u).
\end{array}
\]

At 3, the quadratic factor has valuation one and v_3(s)=p-1+p v_3(u), so positive 3-adic valuations of u remain allowed. At 2, exactly one of a_2,b_2 has valuation one and the other is a unit; the two may be interchanged.

For every such p, infinitely many positive integer pairs (u,v) also satisfy gcd(u,v)=1, the condition that every prime divisor of v is 1 modulo 3, and

\[
0<\Delta<s^2.
\]

Thus the same auxiliary pair can have the required local points at 2 and 3 and a real root d_infinity=sqrt(Delta) satisfying the strict positivity bound |d_infinity|<s. The roots at the three places are not asserted to be one ordinary integer.

Consequently the restrictions in question do not yield an obstruction at 2 or 3, even at unbounded prime-power precision or when their finite congruences are combined. This does not test other primes, produce an integer square Delta, or exclude a sieve with further global information.

## Proof

**The two residue conditions.** Since p is odd, the exponent 2p-3 is odd. For odd u,v,

\[
Ku^{2p}\equiv3\pmod8,\qquad 4v^p\equiv4\pmod8,
\]

so Delta is 1 modulo 8. Also v is 1 modulo 3 and 3 divides K, so Delta is 1 modulo 3. These statements hold even when 3 divides u.

**Compatible binary lifts without a simple-root assumption.** Start with r_2=1. Inductively, for k >= 2, require r_k odd and

\[
r_k^2\equiv\Delta\pmod {2^{k+1}}.
\]

The starting condition follows from Delta congruent to 1 modulo 8. Write E_k=(r_k^2-Delta)/2^(k+1), an integer. For epsilon in {0,1},

\[
(r_k+\epsilon2^k)^2-\Delta
\equiv 2^{k+1}(E_k+\epsilon r_k)\pmod {2^{k+2}}.
\]

The omitted term is divisible by 2^(2k), and 2k >= k+2. Since r_k is odd, exactly one epsilon makes E_k+epsilon r_k even. Choose it and set r_(k+1)=r_k+epsilon 2^k. This preserves r_(k+1) congruent to r_k modulo 2^k and improves the square congruence by one power of 2. The compatible sequence therefore defines d_2 in Z_2. For any fixed precision the square congruence holds eventually, so d_2^2=Delta. It is odd and hence nonzero. The derivative 2r_k was never assumed to be a unit.

**Compatible ternary lifts.** Start with t_1=1. Suppose t_k^2 is Delta modulo 3^k. For eta in {0,1,2}, expansion gives

\[
(t_k+\eta3^k)^2-\Delta
\equiv3^k\left((t_k^2-\Delta)/3^k+2t_k\eta\right)
\pmod {3^{k+1}}.
\]

Here 2k >= k+1, and 2t_k is a unit modulo 3 because t_k remains 1 modulo 3. There is a unique correcting eta. Defining t_(k+1)=t_k+eta 3^k produces compatible residues and hence a root d_3 in Z_3 with d_3 congruent to 1 modulo 3. This root is nonzero.

**Reconstruction and exact valuations.** At 2, s and d_2 are odd, so (s+d_2)/2 and (s-d_2)/2 belong to Z_2. At 3, division by 2 preserves integrality. Apply the polynomial reconstruction identities from L003, which hold over these fields by the same expansions as over the integers:

\[
a_\ell b_\ell=(s^2-d_\ell^2)/4=Ku^{2p}-v^p,
\qquad
a_\ell^2-a_\ell b_\ell+b_\ell^2
=(s^2+3d_\ell^2)/4=3v^p.
\]

For the last equality use s^2=3Ku^(2p) and d_ell^2=4v^p-Ku^(2p). Multiplying the quadratic factor by s gives

\[
a_\ell^3+b_\ell^3=s\cdot3v^p=(3uv)^p=c^p.
\]

Modulo 4, K is 3, u^(2p) is 1, and v^p is 1. Thus the ordinary integer Ku^(2p)-v^p is 2 modulo 4. The displayed product has valuation exactly one at 2, so both coordinates are nonzero, one has valuation one, and the other valuation zero. Since c is odd, each pair contains a unit. Multiplication by 4 gives v_2(s^2-d_2^2)=3.

At 3, s is divisible by 3 and d_3 is a unit. Therefore a_3 and b_3 reduce to opposite nonzero residues and are units. As 3 does not divide v, c has valuation 1+v_3(u); the triple is again pairwise locally coprime. The formulas for s and the quadratic factor give their asserted valuations. None of these calculations requires 3 not dividing u.

**Simultaneous finite congruences.** Fix nonnegative integers r,t. Choose integer representatives of d_2 modulo 2^(r+2) and d_3 modulo 3^t. The Chinese remainder theorem supplies an integer d with both residues, and hence

\[
d^2\equiv\Delta\pmod {2^{r+2}3^t}.
\]

This representative is odd. For a=(s+d)/2, b=(s-d)/2, which are integers, the same identities give

\[
a^3+b^3-c^p=3s(d^2-\Delta)/4\equiv0\pmod {2^r3^t}.
\]

Taking the auxiliary precisions at least 4 at 2 and at least 1 at 3 also preserves the exact local valuation and primitivity conditions above. A fixed d meeting the equation at every precision is not obtained by this finite Chinese remainder argument.

**Compatibility with the real interval and prime support.** For k >= 1 put v=13^(2k). This has only the prime factor 13, is 1 modulo 12, and is prime to 3. Let lambda=K^(-1/(2p))>0. Choose u in the open interval

\[
\lambda13^k<u<2^{1/p}\lambda13^k
\]

with u congruent to 1 modulo 26. The interval length is (2^(1/p)-1)lambda 13^k, which tends to infinity for fixed p. Once it exceeds 26, it contains such an integer u: take the first integer in that residue class strictly above the left endpoint, whose distance from that endpoint is at most 26. This u is odd and prime to 13, so gcd(u,v)=1.

Raising the strict interval inequalities to the positive power 2p gives

\[
v^p<Ku^{2p}<4v^p.
\]

The right inequality gives Delta>0. The left gives Delta=4v^p-Ku^(2p)<3Ku^(2p)=s^2. This constructs infinitely many pairs because the values of v are distinct. The real root yields positive real a_infinity,b_infinity by the strict bound on d_infinity. It does not imply integer a,b.

As a concrete exact control at p=19, take u=5 and v=181. The number 181 is prime, is 1 modulo 12, and is coprime to 5. Here

\[
s=7389459400177001953125,\qquad
\Delta=13272700465307974015006493558304900267225409.
\]

The inequalities 0<Delta<s^2 hold, but with R=3643171758963331393128 one has R^2<Delta<(R+1)^2. This pair meets the auxiliary restrictions and the real interval and has both local roots, while its discriminant is not an integer square. It is not a Beal solution.

**Required threshold and scope.** An exclusion using just the tested local conditions needs zero surviving compatible primitive classes at at least one tested prime, or incompatible combined finite congruences. The constructions instead provide local roots for every pair in the stated congruence class, compatible finite combinations, and infinitely many auxiliary pairs respecting coprimality, prime support, and real feasibility. The actual integer system still needs one integer d whose square is exactly Delta. There is no height bound or global descent in this result, and the other Beal signatures are untouched.

The exact-arithmetic checks in scripts/constrained-local-lifts/check_lifts.py exercise both digit inductions, reconstruction, combined finite congruences, and the displayed nonsquare control. These bounded checks supplement the general proof and do not replace it.

## Mathlib

Coverage of the full statement: **not checked**. Supporting declarations for p-adic completeness, square roots of units, the Chinese remainder theorem, and valuations: **not checked**. No full matching theorem, supporting declaration name, or library absence is asserted. The two lifting arguments are proved explicitly; a simple-root Hensel theorem would support the ternary step only, not the binary step as written.

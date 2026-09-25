# L001 — Primitive local solutions for every Beal signature

## Hypotheses

Fix integers x,y,z >= 3. Congruences below refer to the equation A^x + B^y = C^z. Local primitivity has the meaning fixed in foundations/01-target-and-scope.md: every pair of p-adic coordinates contains a unit.

## Conclusion

1. For every positive integer modulus M and every integer H >= 1, there are pairwise coprime positive integers A,B,C, each greater than H, such that A^x + B^y is congruent to C^z modulo M.
2. For every prime p there are A_p,B_p,C_p in Z_p, all nonzero and different from one, with A_p^x + B_p^y = C_p^z and with every pair locally coprime.

Consequently, no finite collection of congruences for the unrestricted equation can exclude a whole signature by leaving no primitive admissible residue triple. Even solving the equation at every prime separately, allowing all powers of that prime, does not supply a local obstruction. These conclusions do not assert an ordinary integer solution or exclude congruence arguments with additional global restrictions.

## Proof

**Finite moduli with genuinely coprime integer representatives.** Put t = M(H+1) and set

\[
A=t,\qquad B=t+1,\qquad C=t(t+1)+1.
\]

All three integers exceed H. Consecutive integers A,B are coprime. Since C = AB+1, it is congruent to one modulo each of A and B, proving gcd(A,C) = gcd(B,C) = 1. Modulo M the triple is (0,1,1), so A^x+B^y is congruent to 0+1 = 1 = C^z. This proves the first claim. Any finite list of moduli is covered by their least common multiple; no integer equality is inferred from the congruence.

**Compatible lifts at a fixed prime.** Fix p, put s = v_p(z) and K = 2s+1, and choose the ordinary integers

\[
A_p=p^K,\qquad B_p=1+p^K,\qquad U=A_p^x+B_p^y.
\]

We also regard these integers as elements of Z_p. Then U is congruent to one modulo p^K. We construct integers c_k for k >= s+1 satisfying

\[
c_k\equiv1\pmod {p^{s+1}},\qquad
c_k^z\equiv U\pmod {p^{k+s}},\qquad
c_{k+1}\equiv c_k\pmod {p^k}.
\]

For k = s+1 take c_k = 1; the required exponent k+s is exactly K. Suppose c_k has been constructed. For a digit d in {0,...,p-1}, the binomial theorem gives

\[
(c_k+d p^k)^z\equiv c_k^z+z c_k^{z-1}d p^k
\pmod {p^{k+s+1}}.
\]

Indeed, every term of degree j >= 2 in d p^k is divisible by p^(2k), and 2k >= k+s+1 since k >= s+1. This estimate uses only the integrality of the binomial coefficients and remains valid for p = 2 and for p dividing z.

Let e_k = (c_k^z-U)/p^(k+s), an integer by induction, and a_k = (z/p^s)c_k^(z-1). Both z/p^s and c_k are units modulo p, so a_k is invertible modulo p. Choose the unique digit d with e_k+a_k d congruent to zero modulo p, and set c_(k+1) = c_k+d p^k. The displayed expansion proves the equation to the next precision. The correction preserves c_(k+1) congruent to one modulo p^(s+1) and supplies the required compatibility.

The successive corrections are divisible by p^k, so the sequence converges to some C_p in Z_p with C_p congruent to one modulo p^(s+1). At every fixed precision p^N, all sufficiently late c_k equal C_p modulo p^N and have c_k^z congruent to U modulo p^N. Hence C_p^z = U in Z_p. This is the defining completeness of compatible residues, not a limit in the ordinary absolute value.

The coordinates B_p and C_p are units, while A_p is nonzero with valuation K. Each pair therefore contains a unit. The ordinary integers A_p,B_p exceed one and are not equal to one in Z_p. The unit C_p is nonzero; if C_p = 1, then the nonzero ordinary integer U-1 would be zero in Z_p, impossible since an integer divisible by every p^N is zero. Thus the second claim also avoids a coordinate that is exactly zero or one.

The constructions for different primes need not be the same ordinary integers. Nor are the representatives for different moduli bounded or fixed. There is no passage here from local solvability to a positive integer solution. In particular, the same constructions work for x=y=z=3, where Fermat's Last Theorem rules out any positive integer solution. This named theorem is a control comparison, not an input to either construction.

The zero-survivor threshold sought by an unrestricted congruence sieve is therefore unattainable: at least one admissible class remains for every modulus. A descent, a height bound, or another global restriction could change the admissible set and is not tested by this statement.

The exact-arithmetic check in scripts/local-solubility/check_lifts.py exercises the finite representatives and the lifting induction, including ramified exponents. It is a bounded implementation check; the general proof is the argument above.

## Mathlib

Coverage of the full statement: **not checked**. Supporting results about binomial expansion, coprimality, and the completeness of Z_p were not looked up. No matching theorem name or library absence is asserted. The digit-lifting proof is given explicitly, so no unverified invocation of a Hensel theorem is required.

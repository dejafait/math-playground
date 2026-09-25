# L002 — Reduction to odd-prime and fourth-power exponents

## Hypotheses

Let A,B,C,x,y,z be positive integers with x,y,z > 2 and A^x + B^y = C^z. Set

\[
S=\{4\}\cup\{p:p\text{ is an odd prime}\}.
\]

Primitivity means gcd(A,B,C) = 1. No base is assumed greater than one.

## Conclusion

Each of x,y,z has a divisor in S. For **any** choice r,s,t in S with r dividing x, s dividing y, and t dividing z, the positive integers

\[
a=A^{x/r},\qquad b=B^{y/s},\qquad c=C^{z/t}
\]

satisfy a^r+b^s=c^t. The primes dividing each new base are exactly those dividing its original base. Thus primitivity, and also pairwise coprimality, are preserved in both directions by these power substitutions.

Consequently, Beal's conjecture is equivalent to the nonexistence of positive primitive solutions whose ordered exponent triples lie in S^3. This is an exact reduction of the signature space, not a proof of nonexistence on that space.

## Proof

For any integer n > 2, an odd prime divisor, if present, is an allowed divisor in S. Otherwise the fundamental theorem of arithmetic gives n = 2^k for an integer k >= 2; hence 4 divides n. This proves existence separately for x,y,z. It does not require a divisor common to all three exponents.

For an allowed choice r,s,t, all three quotients x/r,y/s,z/t are positive integers, so the displayed new bases are positive integers and

\[
a^r=A^{(x/r)r}=A^x,\quad
b^s=B^{(y/s)s}=B^y,\quad
c^t=C^{(z/t)t}=C^z.
\]

Substitution gives the claimed equation. For every prime ell and every positive integer k, ell divides A^k if and only if ell divides A. The reverse implication is immediate; the forward implication follows by repeated application of Euclid's lemma to the product of k copies of A. This also holds for A = 1, since neither side has any prime divisor. Apply the same argument to B and C. There is therefore a prime common to all three new bases exactly when there is a prime common to all three old bases. As an integer greater than one has a prime divisor, the two gcds equal one simultaneously. Applying the same reasoning to each pair proves the assertion about pairwise coprimality. The numerical gcds need not be equal when they exceed one.

If Beal fails at an arbitrary signature, the construction gives a positive primitive solution at a signature in S^3. Conversely, every positive primitive solution at a signature in S^3 already satisfies all the hypotheses for a counterexample to Beal. These implications prove the equivalence.

The equivalence concerns existence somewhere in the two signature collections. A solution at a reduced signature need not lift to a prescribed original signature: the new bases might lack the additional perfect-power properties required by that lift. No such reverse lift is used.

## Mathlib

Coverage of the full statement: **not checked**. Supporting results about prime divisors, powers, and coprimality were not looked up. No matching theorem name or absence claim is asserted. The elementary reduction and both directions of the existence equivalence are proved above.

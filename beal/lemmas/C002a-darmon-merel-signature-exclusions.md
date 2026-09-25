# C002a — Qualified global exclusions after exponent reduction

## Hypotheses

Let S = {4} union {odd primes}. A solution at an ordered signature (r,s,t) means positive integers a,b,c with a^r+b^s=c^t and gcd(a,b,c) = 1. The right-hand position remains distinguished.

The named inputs are Fermat's Last Theorem and Darmon–Merel's Main Theorem, parts 2 and 3, with part 3 made unconditional by Breuil–Conrad–Diamond–Taylor, Theorem A. Precise statements, source locations, and direct links are recorded in [standard inputs](../foundations/02-standard-results.md). These are cited theorems, not consequences of the Beal target.

## Conclusion

There is no positive primitive solution at any of the following signatures in S^3:

| Signature | Range and permitted placements |
| --- | --- |
| (n,n,n) | Every n in S. |
| (p,p,3) | Every odd prime p >= 5; all three placements of the singleton exponent. |
| (p,p,4) | Every odd prime p >= 5; all three placements of the singleton exponent. |
| (4,4,3) | Exactly the displayed placement of the cube. |

Let R be S^3 with these signatures deleted. Every positive primitive Beal solution would yield a solution at a signature in R, for every allowed divisor choice in L002. Therefore Beal is equivalent to the nonexistence of positive primitive solutions at all signatures in R.

R is the residual set for these exclusions, not a classification of signatures open in the literature. In particular (3,3,4), (4,3,4), (5,5,7), and (3,4,5) belong to R; no assertion of existence or of literature-wide unknown status is made for them.

## Proof

**Nontriviality and primitivity of the auxiliary equations.** Positive a,b,c satisfying a^r+b^s=c^t cannot all equal one, since that would give 2 = 1. Thus abc > 1. Each substitution below only permutes coordinates, changes a sign, or squares one coordinate. Such operations preserve the prime divisors of the corresponding coordinates, so gcd one is preserved. All coordinates remain nonzero and the absolute value of their product remains greater than one. They therefore meet Darmon–Merel's definition of a nontrivial primitive integer solution, even when one original base equals one.

**Equal exponents.** If r=s=t=n > 2, Fermat's Last Theorem excludes the equation, without even needing primitivity.

**Repeated odd prime and a cube.** Suppose p >= 5 is prime. When the cube is on the right, a^p+b^p=c^3 directly contradicts Darmon–Merel, Main Theorem part 3. If instead a^p+b^3=c^p, rearrange to

\[
c^p+(-a)^p=b^3.
\]

This identity is valid because p is odd, and gives the same contradiction for the signed primitive triple (c,-a,b). The third placement follows by interchanging the original summands, an operation that preserves the equation. The full-modularity theorem verifies the historical hypothesis of part 3 in all these applications. The case p = 3 would just repeat the already excluded equal-exponent signature.

**Repeated odd prime and a fourth power.** If a^p+b^p=c^4, rewrite the right side as (c^2)^2. Because p >= 5 is in the permitted range n >= 4, this contradicts Darmon–Merel, Main Theorem part 2. For a^p+b^4=c^p, use

\[
c^p+(-a)^p=(b^2)^2.
\]

Again p is odd, and the theorem applies to (c,-a,b^2). Interchanging the original summands supplies the third placement.

**Two fourth powers summing to a cube.** The equation a^4+b^4=c^3 is exactly the case n = 4 of Darmon–Merel, Main Theorem part 3. This argument proves only the displayed placement. In a^4+b^3=c^4, the attempted replacement c^4+(-a)^4=b^3 would be false: (-a)^4=a^4. No sign-based use of that theorem is asserted for this other ordering.

These arguments prove all exclusions in the table. Now apply L002 to any purported Beal counterexample. Every allowed divisor choice yields a positive primitive solution in S^3 and hence cannot yield one of the excluded signatures; it must lie in R. Conversely, a positive primitive solution at a signature in R is already a Beal counterexample because R is a subset of S^3. This proves the final equivalence without claiming that R contains no solutions.

**Boundary and threshold checks.** The restriction p >= 5 in the fourth-power argument cannot be dropped just by invoking the square clause. At n = 3 that clause's conclusion is false: 1^3+2^3=3^2 is a nontrivial primitive solution. Its square base 3 is not itself a square, so it gives neither a solution nor an exclusion at (3,3,4). Separately, (4,3,4) fails the sign conversion above. A pair of repeated exponents with a third odd prime >= 5 has neither a square nor a cube supplied by its signature, while a triple of distinct reduced exponents need not have any repeated exponent. Additional perfect-power information about particular bases could create further reductions, but none is assumed here.

Infinitely many signatures remain, for example (3,5,q) for primes q >= 7. The required endpoint is zero positive primitive integer solutions for every member of R. These exclusions provide no such uniform result and no effective height bound. Fixed-signature finiteness does not fill this gap.

## Mathlib

Coverage of the full corollary: **not checked**. Coverage of Fermat's Last Theorem, the Darmon–Merel clauses, full modularity, and supporting power/coprimality lemmas was not checked. The named theorems and direct primary-source links are preserved in the cited foundations file; they are mathematical inputs, not claims of matching Mathlib declarations or formal verification.

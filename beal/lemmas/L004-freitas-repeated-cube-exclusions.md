# L004 — Qualified repeated-cube exclusions from Freitas's theorem

## Hypotheses

Put

\[
T=\{p:p\text{ is prime},\ p\ge17,\ p\equiv2\pmod3\}.
\]

A solution at an ordered signature (r,s,t) means positive integers a,b,c satisfying a^r+b^s=c^t and gcd(a,b,c)=1. Bases equal to one are permitted. The cited global input is Freitas, *On the Fermat-type equation x^3+y^3=z^p*, Theorem 3; its exact version and direct sources are in [the foundation](../foundations/03-freitas-repeated-cube-theorem.md).

## Conclusion

For every p in T, there is no positive primitive solution at any of the ordered signatures

\[
(3,3,p),\qquad (p,3,3),\qquad (3,p,3).
\]

Consequently, a primitive Beal solution at exponents (x,y,z) is impossible whenever there is a permutation (r,s,t) of (3,3,p), for some p in T, such that r divides x, s divides y, and t divides z.

Neither of the complete systems I and II in L003 has a solution when n belongs to T. This last assertion includes every coprimality, prime-divisibility, and positivity condition in those systems; it is not an exclusion of either quadratic factor in isolation.

## Proof

**The exponent condition.** For any prime p>3, -3 is a square in the field F_p if and only if p is congruent to 1 modulo 3. Indeed, if w^2=-3, then t=(w-1)/2 satisfies t^2+t+1=0, since 4(t^2+t+1)=(2t+1)^2+3. Such t is nonzero and differs from 1: substituting 0 gives 1, and substituting 1 gives 3, both nonzero in this field. Therefore t has multiplicative order exactly three. Lagrange's theorem gives 3 dividing p-1. Conversely, if 3 divides p-1, Cauchy's theorem applied to the group F_p^* gives an element t of order three. Factoring t^3-1 and using t different from 1 yields t^2+t+1=0, so (2t+1)^2=-3. As p>3, the two possible nonzero residues of p modulo 3 are 1 and 2. Thus every p in T has (-3/p)=-1, with the minus sign essential.

**Application at each placement.** Freitas's Theorem 3 now applies at this p. For any proposed positive primitive solution, the following signed integer triples (X,Y,Z) would solve X^3+Y^3=Z^p:

| Original equation | Triple (X,Y,Z) |
| --- | --- |
| a^3+b^3=c^p | (a,b,c) |
| a^p+b^3=c^3 | (c,-b,a) |
| a^3+b^p=c^3 | (c,-a,b) |

For example, the second row follows from c^3-b^3=a^p and (-b)^3=-b^3. The third row has the same justification with a in place of b. Each transformation only permutes the original bases and changes at most one sign, so its coordinates are nonzero and their gcd, defined using absolute values, is one. All three triples meet the cited theorem's hypotheses and are impossible. A base equal to one causes no exception because nontriviality here means XYZ nonzero.

**Transfer to unreduced exponents.** Suppose the divisibility conditions in the conclusion hold for a putative primitive solution A^x+B^y=C^z. By L002, the positive bases a=A^(x/r), b=B^(y/s), c=C^(z/t) give a primitive solution at (r,s,t). The preceding exclusion contradicts this. Only the forward power substitution is used; no solution at a reduced signature is presumed to lift to prescribed original exponents.

**The two factor systems.** If system I or II of L003 were solvable at n=p in T, its proved converse would reconstruct positive coprime integers a,b and a positive integer c with a^3+b^3=c^p. In particular gcd(a,b,c)=1, contradicting the first placement above. The converse includes parity and strict positivity, so no zero or fractional coordinate is introduced. This use of L003 does not reverse the implication from a lone factor-power condition to a cube solution.

**Scope and threshold.** The first eligible exponent is 17. Although 5 and 11 satisfy the nonsquare condition, they fail the theorem's lower bound and are not covered by this citation. At the complementary prime 19, for example, 4^2 is congruent to -3 modulo 19, so the nonsquare hypothesis fails. No assertion of existence follows from any failed hypothesis.

The achieved threshold is zero primitive solutions at each of the three placements for every p in T, and hence zero solutions of both complete factor systems there. This is stronger than fixed-signature finiteness, but still falls short of zero solutions for all residual Beal signatures. After this application, the repeated-cube primes not covered by these assembled exclusions are 5, 11, and primes congruent to 1 modulo 3. Other mixed families, including (3,5,q) for primes q>=7, also remain outside this conclusion. The earlier local-solubility and single-factor obstructions remain valid limitations on their respective methods; they are not premises in this global application. No new literature result, height bound, or complete candidate for Beal is claimed.

## Mathlib

Coverage of the full statement: **not checked**. Supporting finite-group results used above are the standard named Cauchy and Lagrange theorems; their Mathlib declarations and the power-substitution/coprimality declarations were not checked. Freitas's Theorem 3 and its direct links are retained in the cited foundation as the matching external mathematical input for the signed repeated-cube exclusion. They are not a Mathlib match. The placement, divisibility, and factor-system consequences are proved here.

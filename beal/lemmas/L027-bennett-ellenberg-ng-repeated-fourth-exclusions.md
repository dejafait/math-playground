# L027 — Repeated fourth powers with an odd-prime right side

## Hypotheses

Let a,b,c be positive integers with gcd(a,b,c)=1, and let p>=5 be an odd prime. Bases equal to one are permitted. The signature (4,4,p) is ordered: the pth power is on the right.

The external input is Michael A. Bennett, Jordan S. Ellenberg and Nathan C. Ng, *The Diophantine equation A^4+2^delta B^2=C^n*, **International Journal of Number Theory 6 (2010), 1–27, Theorem 1**. Its coefficient-one clause excludes A^4+B^2=C^n for positive coprime integers A,B,C and integers n>=4. See [Bennett's author manuscript, p. 1](https://personal.math.ubc.ca/~bennett/BeElNgdraftFINAL.pdf#page=1), [publication DOI](https://doi.org/10.1142/S1793042110002971), and [canonical source scope](../foundations/14-bennett-ellenberg-ng-fourth-square-theorem.md). The foundation records the inspected essential proof cases and author-copy wording/access qualifications; no conjectural hypothesis is used for this clause.

For the divisor consequence, let A,B,C,x,y,z be positive integers with x,y,z>2, gcd(A,B,C)=1 and A^x+B^y=C^z.

## Conclusion

There is no positive primitive solution of a^4+b^4=c^p for any odd prime p>=5. Consequently, no original primitive Beal solution has 4|x, 4|y and p|z for such a prime. This includes positive base-one cases and swapping the two fourth-power summands. No other placement of p is asserted here.

## Proof

Suppose a^4+b^4=c^p. A prime dividing any two of a,b,c divides two terms of this equation and hence the third power, so divides the third base. Primitivity therefore implies pairwise coprimality. This implication uses the equation and is not an assertion about arbitrary triples of gcd one.

Set (U,V,W)=(a,b^2,c). These are positive integers and satisfy

\[
U^4+V^2=a^4+(b^2)^2=a^4+b^4=c^p=W^p.
\]

For every prime ell, ell divides b^2 if and only if ell divides b, by Euclid's lemma. Thus the auxiliary bases have exactly the original prime supports and remain pairwise coprime; in particular gcd(U,V,W)=1. The exponent n=p is an integer at least five, hence satisfies n>=4. These are precisely the positive coprime hypotheses of the coefficient-one clause of Theorem 1, which gives a contradiction. No coefficient-two clause is used.

If any original base is one, its auxiliary base is still one, positive and nonzero with empty prime support. The cited positive scope imposes no lower bound greater than one on any base. If a source nontriviality convention is expressed by the product being greater than one, the equation also ensures it: all three bases cannot be one because 1+1 is not 1, and their product is positive. Hence no base-one case is lost. Swapping a and b gives the same argument for the identical ordered signature.

Now suppose 4|x, 4|y and p|z for such a prime p. The selected exponents (4,4,p) belong to L002's set S. Apply L002 with these divisors, setting

\[
a=A^{x/4},\qquad b=B^{y/4},\qquad c=C^{z/p}.
\]

All quotients are positive integers. L002 gives a^4+b^4=c^p and preserves each base's prime support, so gcd(a,b,c)=1, including when an original base equals one. The exclusion just proved contradicts this reduced solution. Only the forward divisor substitution is used; a reduced solution is not asserted to lift to any prescribed original exponents.

The achieved threshold is zero positive primitive solutions for every displayed prime and ordered divisor family, with unrestricted bases. The global nonexistence theorem and its modular/analytic computations are imported by citation, not independently reproduced. The elementary substitution is the local assembly. A negative sign cannot be absorbed into a fourth power to obtain (4,p,4) or (p,4,4); neither those placements nor a composite-singleton theorem application is claimed here. Infinitely many residual signatures and the independent mixed-seventh global-algebra and packet-exhaustion gaps remain unresolved.

### Critical application audit — 2026-10-06, step 058

The coefficient-one statement in foundation 14, with its recorded positive coprime convention, is the external premise. Its essential prime cases are already inspected there; this audit does not reverify the source's computations. The older p>=211 theorem is not substituted for Theorem 1, and p=5 remains covered by the stronger cited theorem.

The pairwise check covers all three pairs: a prime dividing a,b must divide c by the equation; one dividing a,c must divide b; one dividing b,c must divide a. Each contradicts gcd(a,b,c)=1. For (U,V,W)=(a,b^2,c), common primes of U,V, of U,W, and of V,W would therefore be common primes of a,b, of a,c, and of b,c respectively. None exists. This verifies even a pairwise interpretation of the source's coprimality hypothesis.

Base one is checked at each position. If a=1, U=1; if b=1, V=1. The other coordinates remain positive and the prime-support proof still applies. If c=1, the equation is impossible because a^4+b^4>=2 while c^p=1. If a=b=1, then c^p=2: c=1 gives 1 and c>=2 gives c^p>=32, so this too is impossible. No source convention excluding the all-one triple loses a possible solution, and no restriction a,b>1 is imposed.

For the divisor consequence, 4 and p belong to S, and the selected divisibility hypotheses give positive integer quotients x/4, y/4, z/p. The identities (A^(x/4))^4=A^x, (B^(y/4))^4=B^y and (C^(z/p))^p=C^z verify the ordered equation. By L002, a prime divides each new base exactly when it divides its original base, so a common prime of the new triple contradicts the original gcd-one hypothesis. Thus every source hypothesis passes. The sole direct local lemma input remains L002; foundation 01 supplies the primitivity convention and foundation 14 the source theorem. No additional lemma input or cycle is needed.

No mathematical error or new exclusion was found. The zero-solution threshold was already supplied by the known application above. Other placements, composite-singleton applications, mixed-seventh global algebra applicability and packet exhaustion remain outside this verified claim.

## Mathlib

Coverage of the full source theorem and this application: **not checked**. Supporting prime-support, power and coprimality declarations were not checked. The precise citation supplies the nonexistence input; the elementary applicability and L002 transfer are proved above. No formal verification, absence claim, or independent rerun of the cited computations is asserted.

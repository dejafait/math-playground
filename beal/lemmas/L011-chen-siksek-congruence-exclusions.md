# L011 — Congruence exclusions and the remaining repeated-cube prime classes

## Hypotheses

Let p >= 5 be prime. A primitive positive solution at signature (r,s,t) means positive integers a,b,c with a^r+b^s=c^t and gcd(a,b,c)=1, including bases equal to one.

The external input is Chen–Siksek, *Perfect powers expressible as sums of two cubes*, **Theorem 1**. The [foundation](../foundations/08-chen-siksek-congruence-families.md) records its exact signed scope, positive-divisor condition, and computational qualifications; its [statement is on manuscript p. 2](https://samirsiksek.github.io/siksek.github.io/papers/qr8.pdf#page=2).

## Conclusion

If p satisfies any one of

\[
\begin{split}
&p\equiv2,3\pmod5;\qquad p\equiv17,61\pmod{78};\\
&p\equiv51,103,105\pmod{106};\qquad
p\equiv43,49,61,79,97\pmod{108},
\end{split}\tag{E}
\]

there is no primitive positive solution at any placement (3,3,p), (p,3,3), or (3,p,3). This also excludes an original Beal signature whenever the entries of one such placement divide its corresponding exponents, and makes both complete L003 factor systems empty at n=p.

Combining these exclusions with L004 and L010, a primitive positive solution at any placement of (3,3,p) requires p > 10^9 and all four conditions

\[
\begin{array}{ll}
p\bmod108\in R,&R=\{1,7,13,19,25,31,37,55,67,73,85,91,103\},\\
p\bmod5\in\{1,4\},&p\bmod13\in\{1,2,3,4,5,6,7,8,10,11,12\},\\
p\bmod53\in\{1,2,\ldots,49\}.&
\end{array}\tag{R}
\]

For primes above 10^9, (R) is exactly the complement of these three exponent tests: Theorem 1, L004, and L010. It does not assert that any surviving signature has a solution. There are exactly 14,014 residue classes satisfying (R) modulo M=372,060; the new theorem removes 30,914 of the 44,928 reduced classes previously allowed by p congruent to 1 modulo 3.

## Proof

**Normalization of the cited theorem.** Set B={43,49,61,79,97}. The source's sixty residues in clause IV are exactly

\[
\bigcup_{j=0}^{11}(B+108j)
\]

within [0,1296). Each is the unique lift of its member of B with the indicated quotient on division by 108. Since 1296=12 times 108, the printed clause is equivalent to membership in B modulo 108. The literal source list and the expanded set are independently compared in the stored arithmetic check.

For n=p, the only positive divisors are 1 and p. The divisor 1 meets none of the four source clauses, while p meets a clause exactly when (E) holds. Thus the prime specialization loses no possible divisor. Applying the cited theorem with n=d=p excludes every signed nonzero primitive solution of X^3+Y^3=Z^p for (E). The theorem itself allows composite divisors for composite exponents; no prime-only reinterpretation of its general statement is made.

**Placements, divisor extensions, and complete systems.** For the three proposed positive equations, the signed triples in the source's equation are respectively

\[
\begin{array}{c|c}
a^3+b^3=c^p&(X,Y,Z)=(a,b,c)\\
a^p+b^3=c^3&(X,Y,Z)=(c,-b,a)\\
a^3+b^p=c^3&(X,Y,Z)=(c,-a,b).
\end{array}
\]

In the second row, c^3+(-b)^3=a^p; the third follows in the same way by moving the other cube. The maps only permute absolute values, so every coordinate stays nonzero and the gcd stays one. In an actual coefficient-one solution, a prime dividing two bases divides the third, so the coordinates also meet a pairwise-coprime convention. No base-one exception occurs. The source theorem contradicts each row.

For an original signature divisible entrywise by an excluded placement, all entries of the placement belong to S={4} union {odd primes}. L002's positive power substitution preserves primitivity and produces a solution at that placement, a contradiction. A solution of either complete L003 system reconstructs a positive primitive cube solution by its exact converse and is equally impossible. Integrality, coprimality, and strict positivity are part of that converse; an isolated factor condition does not suffice.

**Exact complement of the exponent tests.** L010 excludes every prime p <= 10^9 in the present domain. Any remaining prime exceeds 2,3,5,13,53. L004 then excludes p congruent to 2 modulo 3, leaving p congruent to 1 modulo 3. Such a prime is congruent to 1 modulo 6.

Clause I of (E), together with 5 not dividing p, leaves precisely p modulo 5 in {1,4}. For clause II, the residue 17 modulo 78 is already impossible under p congruent to 1 modulo 3. Among numbers congruent to 1 modulo 6, the Chinese remainder theorem makes p congruent to 61 modulo 78 equivalent to p congruent to 9 modulo 13: 61 is 1 modulo 6 and 9 modulo 13. Avoiding this clause leaves the eleven nonzero residues modulo 13 other than 9.

For odd p, the three residues 51,103,105 modulo 106 correspond exactly to residues 51,50,52 modulo 53. Each nonzero class modulo 53 has a unique odd lift modulo 106. Avoiding clause III, together with 53 not dividing p, therefore leaves residues 1 through 49 modulo 53.

There are eighteen residues congruent to 1 modulo 6 in [0,108):

\[
1,7,13,19,25,31,37,43,49,55,61,67,73,79,85,91,97,103.
\]

Removing B leaves exactly R. This proves necessity of (R). Conversely, each prime p > 10^9 satisfying (R) is 1 modulo 3, fails every clause of (E), and is outside L010's interval. The divisor 1 still fails the source clauses, so none of the three specified exponent tests applies. This proves exactness of the complement of the tests, without reversing a nonexistence implication into an existence assertion.

**Counting and threshold.** The moduli 108,5,13,53 are pairwise coprime, and their product is M=372,060. The Chinese remainder theorem identifies the classes satisfying (R) bijectively with choices from sets of sizes 13,2,11,49. Their count is consequently

\[
13\cdot2\cdot11\cdot49=14,014.
\]

All these choices are units at their respective moduli. There are 36 times 4 times 12 times 52 = 89,856 reduced classes modulo M. Of these, 18 times 4 times 12 times 52 = 44,928 are 1 modulo 3. Thus exactly 44,928-14,014=30,914 of the previously allowed classes are newly excluded. The compatible choice of residue 1 at each modulus demonstrates that the complement is nonempty. These are finite class counts; no assertion that a density implies emptiness is used.

The reproducible check

```text
python3 scripts/chen-siksek-congruences/check_residues.py
```

compares the literal clauses and (R) for every class modulo M, checks the sixty-residue normalization, and stores [results](../scripts/chen-siksek-congruences/results.json). It also checks two prime controls above the old endpoint by exact trial division through their integer square roots: 1,000,000,009 has residues (37,4,8,37) modulo (108,5,13,53) and survives; 1,000,000,021 has residues (49,1,7,49) and is newly excluded by clause IV alone. The controls concern exponent tests, not integer solutions of the Diophantine equation. The source's modular and number-field calculations are not rerun.

The achieved result is zero primitive positive solutions with unrestricted bases on the additional stated exponent families. The remaining target requires zero solutions for every surviving signature, including all repeated-cube primes in (R) and unrelated mixed signatures. The finite arithmetic audit supplies neither an upper height bound nor an exclusion of those residual equations. No complete Beal candidate follows.

## Mathlib

Coverage of the full lemma: **not checked**. Supporting Chinese remainder, congruence, gcd, and power declarations: **not checked**. Chen–Siksek's numbered theorem and direct source above match the external signed nonexistence input. The Chinese remainder theorem is a standard supporting result for the exact finite classification; it is not a match for Diophantine nonexistence. The placement and residue arguments are proved here, with the arithmetic check as corroboration.

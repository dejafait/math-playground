# L010 — Repeated-cube exclusions through exponent one billion

## Hypotheses

Let n be an integer with 3 <= n <= 10^9. A primitive positive solution at signature (r,s,t) consists of positive integers a,b,c satisfying a^r+b^s=c^t and gcd(a,b,c)=1. Bases equal to one are included.

The external input is Chen–Siksek, *Perfect powers expressible as sums of two cubes*, **Theorem 2**, with the nontrivial primitive scope specified by section 12 of its proof. The [foundation](../foundations/07-chen-siksek-exponent-range.md) identifies the publication, the [author's manuscript statement on p. 3](https://samirsiksek.github.io/siksek.github.io/papers/qr8.pdf#page=3), the [proof on p. 18](https://samirsiksek.github.io/siksek.github.io/papers/qr8.pdf#page=18), and the computational and source-version qualifications.

## Conclusion

There is no primitive positive solution at any of

\[
(3,3,n),\qquad(n,3,3),\qquad(3,n,3),\qquad 3\le n\le10^9.
\]

In particular this excludes n=7,11,13. An original Beal signature (x,y,z) is excluded whenever an ordered placement (r,s,t) of (3,3,n), for an n in this range, satisfies r dividing x, s dividing y, and t dividing z.

Both complete square-discriminant systems I and II of L003 are empty for every n in this range. Their coprimality, divisibility, and strict positivity conditions remain part of this assertion.

## Proof

**Precise cited input.** The external theorem excludes nonzero primitive integer triples (X,Y,Z) satisfying X^3+Y^3=Z^n in the stated range. It places no bound on the bases. Its short statement's reference to solutions is read with the source's definitions and the explicit nontrivial primitive claim in section 12. It cannot mean that all integer triples are excluded: for example, (1,-1,0) remains a solution. No exclusion of zero-coordinate or nonprimitive triples is needed here.

In an actual coefficient-one solution, any prime dividing two coordinates divides the remaining coordinate by the equation. Thus gcd(a,b,c)=1 implies pairwise coprimality. The proposed triples meet either convention for the source's coprime coordinates; this implication would not hold for arbitrary triples without the equation.

**Placements and signs.** For a proposed positive solution, use the following signed coordinates:

| Original equation | (X,Y,Z) in X^3+Y^3=Z^n |
| --- | --- |
| a^3+b^3=c^n | (a,b,c) |
| a^n+b^3=c^3 | (c,-b,a) |
| a^3+b^n=c^3 | (c,-a,b) |

For the second row, c^3+(-b)^3=c^3-b^3=a^n; the third follows by swapping the summands in the original equation. Each map only permutes the bases and changes a sign, so their absolute-value gcd remains one and every coordinate remains nonzero. A base equal to one therefore causes no exception. Only a cube absorbs a minus sign; the argument is valid for both odd and even n. The cited theorem contradicts every row.

**Exponent-divisor consequence.** Suppose a putative original solution has the divisors in the conclusion. L002 shows that n has a divisor d in S={4} union {odd primes}. Since 3 <= d <= n <= 10^9, the first part of this proof applies to d. Replace the singleton n in (r,s,t) by d to obtain a placement of (3,3,d) whose entries belong to S and divide (x,y,z). L002 now gives a positive primitive solution at that reduced signature, which was just excluded. This argument uses L002 only within its stated domain; it does not assume that a composite n belongs to S or that a reduced solution lifts to a prescribed original signature.

**Complete factor systems.** L003 holds for all integers n>=2. A solution of either of its complete systems at one of the exponents here reconstructs positive coprime a,b and positive c with a^3+b^3=c^n. Its converse proves integrality, positivity, and coprimality, including at even n. This contradicts the first placement above. Satisfying an isolated factor-power condition does not suffice for this implication.

**Threshold and scope.** This achieves zero solutions, with no height restriction, for the stated exponent range and its divisor extensions. It is stronger than finding no examples with bounded bases and stronger than fixed-signature finiteness. The upper endpoint 10^9 is an exponent bound, not a height bound. The result alone leaves every prime n>10^9 untreated, as well as unrelated mixed signatures. It is an application of a cited theorem, not a proof of the full Beal conjecture. The theorem's computational proof is not independently reproduced here.

## Mathlib

Coverage of the full lemma: **not checked**. Supporting declarations for signs, gcds, and powers were not checked. The named theorem and direct sources above match the external nonexistence input; they are not claimed as Mathlib declarations. The placement and divisor arguments and the application of L003 are proved here.

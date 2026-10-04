# L014 — Fifth-power/nineteenth-power signature exclusions

## Hypotheses

A solution at an ordered signature (r,s,t) means positive integers a,b,c with a^r+b^s=c^t and gcd(a,b,c)=1. Bases equal to one are included, and the right-hand position is distinguished.

The external input is Dahmen–Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100, Theorem 1, p. 67**, restricted to ell=19. It classifies coprime signed integer solutions of X^5+Y^5=Z^19, all of which have a zero coordinate. The exact clause and its qualifications are in [the foundation](../foundations/11-dahmen-siksek-fifth-nineteenth-theorem.md); [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/83637), [numbered theorem statement](https://arxiv.org/html/1309.4030v2#Thmtheorem1).

## Conclusion

There is no positive primitive solution at any of the three ordered signatures

\[
(5,5,19),\qquad(5,19,5),\qquad(19,5,5).
\]

Consequently, an original Beal signature (x,y,z), with x,y,z>2, is excluded whenever at least one of the following conditions holds:

\[
\begin{aligned}
&5\mid x,\quad 5\mid y,\quad 19\mid z;\\
&5\mid x,\quad 19\mid y,\quad 5\mid z;\\
&19\mid x,\quad 5\mid y,\quad 5\mid z.
\end{aligned}
\]

These are zero-solution conclusions with unrestricted positive bases.

## Proof

**Coprimality and nonzero scope.** In an actual solution a^r+b^s=c^t, a prime dividing any two bases divides their two corresponding powers. The equation then makes it divide the third power, and hence its base. Thus a prime shared by a pair would divide all three bases, contradicting gcd(a,b,c)=1. The bases are therefore pairwise coprime. A permutation or sign change preserves the prime divisors and gcds of their absolute values. All bases are positive, so every transformed coordinate is nonzero, including when its absolute value is one.

**All three placements.** Each putative solution gives a signed triple for the source equation:

| Original equation | (X,Y,Z) | Identity X^5+Y^5=Z^19 |
| --- | --- | --- |
| a^5+b^5=c^19 | (a,b,c) | a^5+b^5=c^19 |
| a^5+b^19=c^5 | (c,-a,b) | c^5-a^5=b^19 |
| a^19+b^5=c^5 | (c,-b,a) | c^5-b^5=a^19 |

The last two rows use the oddness of the fifth power: (-a)^5=-a^5 and (-b)^5=-b^5. The identities are exact rearrangements of the original equations. Each row is a nonzero pairwise coprime signed integer triple by the preceding paragraph. The ell=19 clause of Dahmen–Siksek's Theorem 1 permits only the six zero-coordinate triples recorded in the foundation, so every row contradicts the classification. The theorem covers both 5 dividing Z and 5 not dividing Z and imposes no exclusion of coordinates of absolute value one. Thus the argument covers both branches at 5 and every positive base-one case.

**Exponent-divisor extensions.** Suppose A^x+B^y=C^z is a positive primitive solution satisfying one of the displayed divisibility conditions. Choose (r,s,t), respectively, as (5,5,19), (5,19,5), or (19,5,5). Since 5 and 19 are odd primes, these exponents belong to the set permitted in L002. Their divisibilities give positive integer quotients and hence, by L002, positive integers

\[
a=A^{x/r},\qquad b=B^{y/s},\qquad c=C^{z/t}
\]

with a^r+b^s=c^t and gcd(a,b,c)=1. This contradicts the corresponding placement already excluded. L002 preserves each base's prime support, also for a base equal to one. Only the forward substitution from an original solution is used; no reverse lift to a prescribed original signature is required.

**Threshold and remaining gap.** The result reaches zero positive primitive solutions for these three placements and their stated divisor extensions. It adds a signature family not excluded by the notebook's previously assembled inputs, including L013's separate ell=7 clause. The zero-solution classification is known and imported by precise citation; the proof above supplies its applicability. No independent genus-nine calculation, modular computation, or fifth-cyclotomic descent is claimed. Uniform emptiness of the other residual signatures and the constrained repeated-cube complement remains unproved. The conditional D_19 alternative is not used, and no other clause of the paper is imported here.

## Mathlib

Coverage of the full lemma: **not checked**. Supporting sign, power, and coprimality declarations were not checked. Dahmen–Siksek's Theorem 1 at ell=19 matches the external signed classification; the placement and divisor arguments are proved above. The direct primary-source links identify mathematical sources, not matching Mathlib declarations or formal verification.

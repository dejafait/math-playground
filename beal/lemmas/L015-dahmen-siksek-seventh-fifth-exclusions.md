# L015 — Seventh-power/fifth-power signature exclusions

## Hypotheses

A solution at an ordered signature (r,s,t) means positive integers a,b,c with a^r+b^s=c^t and gcd(a,b,c)=1. Bases equal to one are included, and the right-hand position is distinguished.

The external input is Dahmen–Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100, Theorem 2, p. 67**. It classifies coprime signed integer solutions of X^7+Y^7=Z^5, all of which have a zero coordinate. The exact statement and source qualifications are in [the foundation](../foundations/12-dahmen-siksek-seventh-fifth-theorem.md); [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/83637), [numbered theorem statement](https://arxiv.org/html/1309.4030v2#Thmtheorem2).

## Conclusion

There is no positive primitive solution at any of the three ordered signatures

\[
(7,7,5),\qquad(7,5,7),\qquad(5,7,7).
\]

Consequently, an original Beal signature (x,y,z), with x,y,z>2, is excluded whenever at least one of the following conditions holds:

\[
\begin{aligned}
&7\mid x,\quad 7\mid y,\quad 5\mid z;\\
&7\mid x,\quad 5\mid y,\quad 7\mid z;\\
&5\mid x,\quad 7\mid y,\quad 7\mid z.
\end{aligned}
\]

These are zero-solution conclusions with unrestricted positive bases.

## Proof

**Coprimality and nonzero scope.** For an actual solution a^r+b^s=c^t, a prime dividing any two bases divides their corresponding powers. The equation then makes it divide the third power, hence its base. A prime shared by a pair would therefore divide all three bases, contradicting gcd(a,b,c)=1. Thus a,b,c are pairwise coprime. A sign change or permutation preserves the prime divisors and pairwise gcds of their absolute values. Positivity makes every transformed coordinate nonzero, also when its absolute value is one.

**All three placements.** A putative solution gives a signed triple for the source equation as follows:

| Original equation | (X,Y,Z) | Identity X^7+Y^7=Z^5 |
| --- | --- | --- |
| a^7+b^7=c^5 | (a,b,c) | a^7+b^7=c^5 |
| a^7+b^5=c^7 | (c,-a,b) | c^7-a^7=b^5 |
| a^5+b^7=c^7 | (c,-b,a) | c^7-b^7=a^5 |

The second and third rows use (-a)^7=-a^7 and (-b)^7=-b^7, respectively, so their identities follow by exact rearrangement. Every row gives a nonzero pairwise coprime signed integer triple. Theorem 2 permits only the six zero-coordinate triples recorded in the foundation, contradicting each row. The theorem covers both branches at 7 and has no exception for coordinates of absolute value one. All positive base-one cases are therefore included.

**Exponent-divisor extensions.** Suppose A^x+B^y=C^z is a positive primitive solution satisfying one of the displayed divisibility conditions. Choose (r,s,t), respectively, as (7,7,5), (7,5,7), or (5,7,7). Since 5 and 7 are odd primes, they belong to L002's permitted exponent set. The corresponding divisibilities give positive integer quotients. L002 then supplies positive integers

\[
a=A^{x/r},\qquad b=B^{y/s},\qquad c=C^{z/t}
\]

with a^r+b^s=c^t and gcd(a,b,c)=1, contradicting the corresponding placement already excluded. L002 preserves each base's prime support, including a base equal to one. Only the forward power substitution is used; a reduced solution is not asserted to lift to a prescribed original signature.

**Threshold and remaining gap.** This reaches zero positive primitive solutions for all three placements and their stated divisor extensions. The repeated exponent is seven, so these placements are distinct from the earlier repeated-fifth-power exclusions. The global classification is known and imported by precise citation; the proof above supplies its applicability. No independent modular, rank, or rational-point computation is claimed. The restricted auxiliary set C_{5,3}(K)' is not replaced by a purported classification of the full curve, and no GRH assumption is used. Uniform emptiness for the other residual signatures and the constrained repeated-cube complement remains unproved.

## Mathlib

Coverage of the full lemma: **not checked**. Supporting sign, power, and coprimality declarations were not checked. Dahmen–Siksek's Theorem 2 matches the external signed classification; the placement and divisor arguments are proved above. The direct source links identify mathematical sources, not matching Mathlib declarations or formal verification.

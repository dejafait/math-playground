# L013 — Fifth-power/seventh-power signature exclusions

## Hypotheses

A solution at an ordered signature (r,s,t) means positive integers a,b,c with a^r+b^s=c^t and gcd(a,b,c)=1. Bases equal to one are included, and the right-hand position is distinguished.

The external input is Dahmen–Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100, Theorem 1, p. 67**, restricted to ell=7. It classifies coprime signed integer solutions of X^5+Y^5=Z^7, all of which have a zero coordinate. The exact clause and source qualifications are in [the foundation](../foundations/10-dahmen-siksek-fifth-seventh-theorem.md); [published paper](https://www.impan.pl/shop/publication/transaction/download/product/83637), [numbered theorem statement](https://arxiv.org/html/1309.4030v2#Thmtheorem1).

## Conclusion

There is no positive primitive solution at any of the three ordered signatures

\[
(5,5,7),\qquad(5,7,5),\qquad(7,5,5).
\]

Consequently, an original Beal signature (x,y,z), with x,y,z>2, is excluded whenever at least one of the following conditions holds:

\[
\begin{aligned}
&5\mid x,\quad 5\mid y,\quad 7\mid z;\\
&5\mid x,\quad 7\mid y,\quad 5\mid z;\\
&7\mid x,\quad 5\mid y,\quad 5\mid z.
\end{aligned}
\]

These are zero-solution conclusions with unrestricted positive bases.

## Proof

**Coprimality and nonzero scope.** For an actual solution a^r+b^s=c^t, a prime dividing any two bases also divides the third: it divides two terms of the equation and hence the remaining positive integer power, so it divides that power's base. Therefore gcd(a,b,c)=1 implies pairwise coprimality. A sign change or coordinate permutation preserves all prime divisors and the gcds of absolute values. Positivity makes every coordinate nonzero, including a coordinate equal to one. The equation also prevents all three original bases from being one, since 1+1 is not 1.

**All three placements.** Each putative solution supplies a triple for the external equation as follows:

| Original equation | (X,Y,Z) | Identity X^5+Y^5=Z^7 |
| --- | --- | --- |
| a^5+b^5=c^7 | (a,b,c) | a^5+b^5=c^7 |
| a^5+b^7=c^5 | (c,-a,b) | c^5-a^5=b^7 |
| a^7+b^5=c^5 | (c,-b,a) | c^5-b^5=a^7 |

The second and third rows use (-a)^5=-a^5 and (-b)^5=-b^5, respectively. Thus their identities are exact rearrangements. By the preceding paragraph every row gives a nonzero pairwise coprime signed integer triple. The ell=7 clause of Dahmen–Siksek's Theorem 1 lists only triples with a zero coordinate, contradicting each row. Neither a base-one case nor either divisibility case at 5 is omitted.

**Exponent-divisor extensions.** Suppose A^x+B^y=C^z is a positive primitive solution satisfying one of the displayed divisibility conditions. Choose (r,s,t), respectively, as (5,5,7), (5,7,5), or (7,5,5). Each entry is an odd prime, so it belongs to L002's permitted exponent set, and r divides x, s divides y, and t divides z. L002 gives positive integers

\[
a=A^{x/r},\qquad b=B^{y/s},\qquad c=C^{z/t}
\]

with a^r+b^s=c^t and gcd(a,b,c)=1. This contradicts the corresponding placement just excluded. The preservation of prime support in L002 includes bases equal to one. Only the forward substitution is used; no reduced solution is asserted to lift to a prescribed original signature.

**Threshold and remaining gap.** This reaches zero positive primitive integer solutions for precisely these three placements and their displayed divisor extensions. It closes the (5,5,7) gap in the notebook's assembled exclusions. The input is known and imported by citation; no independent fifth-cyclotomic descent or computational reproduction is claimed. Uniform emptiness for all other residual signatures, including unrelated mixed signatures and the remaining repeated-cube complement, is still unproved. The ell=19 clause and other theorems in the same paper are not used in this lemma.

## Mathlib

Coverage of the full lemma: **not checked**. Supporting power, sign, and coprimality declarations were not checked. Dahmen–Siksek's Theorem 1 at ell=7 matches the external signed classification; the placement and divisor arguments are proved above. The named paper and direct links are mathematical sources, not matching Mathlib declarations or claims of formal verification.

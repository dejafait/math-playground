# L009 — Small repeated-cube exclusions from Bruin's theorems

## Hypotheses

Let n belong to {4,5}. A solution at an ordered signature (r,s,t) means positive integers a,b,c with a^r+b^s=c^t and gcd(a,b,c)=1. Bases equal to one are included.

The external inputs are Nils Bruin, *On Powers as Sums of Two Cubes*, **Theorem 1** for n=4 and **Theorem 2** for n=5, printed p. 170. The exact signed statements and source-access qualifications are in [the foundation](../foundations/06-bruin-small-exponent-theorems.md), with the [publisher's statements](https://page-one.springer.com/pdf/preview/10.1007/10722028_9#page=2) and [publication record](https://doi.org/10.1007/10722028_9).

## Conclusion

There is no positive primitive solution at any of

\[
(3,3,n),\qquad(n,3,3),\qquad(3,n,3),\qquad n\in\{4,5\}.
\]

In particular, an original Beal signature (x,y,z) is excluded whenever some ordered placement (r,s,t) of (3,3,4) or (3,3,5) satisfies r dividing x, s dividing y, and t dividing z.

Both complete square-discriminant systems I and II of L003 are empty at n=4 and n=5, including all their coprimality, divisibility, and strict positivity conditions. This does not exclude an isolated factor-power condition.

## Proof

**The cited zero-solution result.** Bruin's Theorems 1 and 2 give gcd(X,Y,Z)>1 whenever X^3+Y^3=Z^n, XYZ is nonzero, and n=4 or 5 respectively. The coordinates are integers, with no positivity or absolute-value lower bound beyond nonzero. Thus gcd(X,Y,Z)=1 is impossible under these hypotheses. This is the precise cited global input; no finite search or per-signature finiteness theorem is substituted for it.

For clarity, the primitive solutions left by that theorem all have a zero coordinate. Their complete lists follow elementarily:

\[
\begin{array}{c|l}
n& (X,Y,Z)\\ \hline
4&(1,-1,0),\ (-1,1,0),\ (0,1,\pm1),\ (1,0,\pm1)\\
5&(1,-1,0),\ (-1,1,0),\ (0,1,1),\ (0,-1,-1),\ (1,0,1),\ (-1,0,-1).
\end{array}
\]

Indeed, if Z=0, then X=-Y and primitivity forces |X|=|Y|=1. If X=0 and Y,Z are nonzero, every prime factor of either Y or Z divides the other by Y^3=Z^n. Primitivity therefore forces |Y|=|Z|=1; for n=4 the sign of Y must be positive, and for n=5 it must agree with that of Z. The case Y=0 is obtained by interchanging X and Y. If two coordinates vanish, all three do and the gcd is not one. This proves the lists, whose entries directly satisfy the equations. In particular the source's word 'trivial' does not conceal any nonzero base-one exception.

**All three placements.** A proposed positive solution gives a signed solution to the cited equation by the following substitutions:

| Original equation | (X,Y,Z) in X^3+Y^3=Z^n |
| --- | --- |
| a^3+b^3=c^n | (a,b,c) |
| a^n+b^3=c^3 | (c,-b,a) |
| a^3+b^n=c^3 | (c,-a,b) |

For example, the second identity is c^3+(-b)^3=c^3-b^3=a^n. Each substitution only permutes coordinates and changes the sign of a cube base. Thus the coordinates remain nonzero and the gcd, defined on absolute values, remains one. Bruin's appropriate theorem rules out each triple. This works at n=4 because the moved term is a cube; no minus sign is absorbed into a fourth power. Positivity of the original bases, including a possible base one, ensures nonzero coordinates in every row.

**Transfer through exponent divisors.** For an original putative primitive solution A^x+B^y=C^z and a divisor choice (r,s,t) as in the conclusion, L002 supplies the positive primitive solution with bases A^(x/r), B^(y/s), C^(z/t). The resulting signature is one of the six just excluded, giving a contradiction. This is a forward power substitution, not an assertion that every reduced solution lifts to a prescribed original signature.

**The complete factor systems.** The hypotheses of L003 allow every integer n>=2, so include both exponents here. Its converse turns a solution of either full system at n=4 or 5 into positive coprime integers a,b and a positive integer c with a^3+b^3=c^n. That contradicts the first row above. L003 proves the needed parity, coprimality, and strict positivity in that converse. Its isolated quadratic-factor witnesses at n=5 fail the remaining sum-power condition and hence are consistent with this exclusion.

**Achieved threshold and remaining scope.** The result is zero positive primitive solutions at six ordered reduced signatures and at all original signatures admitting the stated divisor choices. In particular it supplies the missing zero-solution threshold for (3,3,5) and for the adjacent (3,3,4) boundary. It gives neither an upper height bound nor an exclusion at repeated-cube prime 7,11,13 or at the remaining complementary primes through this citation. The signature (4,3,4) has two fourth powers and only one cube, so is not a placement of (3,3,4). Other residual mixed families remain. This is a consequence of published theorems, not a new resolution of Beal.

## Mathlib

Coverage of the full lemma: **not checked**. Supporting sign, gcd, and exponent-divisor declarations were not checked. Bruin's Theorems 1 and 2, with their names and direct links above, match the signed nonexistence inputs but are not asserted to be Mathlib declarations. The classification of zero-coordinate cases, placement arguments, and consequences are proved here; the global exclusion is imported by precise citation.

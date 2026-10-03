# L012 — Boundary signature exclusions from Cohen's proposition

## Hypotheses

A solution at an ordered signature (r,s,t) means positive integers a,b,c with a^r+b^s=c^t and gcd(a,b,c)=1. Bases equal to one are included, and the right-hand position is distinguished.

The external input is Henri Cohen, *Number Theory, Volume II: Analytic and Modern Tools*, first edition, GTM **240**, Springer, 2007, Section 14.6.3, **Proposition 14.6.6, pp. 484–485**. Its minus clause excludes X^4-Y^4=Z^3 in nonzero coprime integers. The precise source scope and access qualifications are in [the foundation](../foundations/09-cohen-boundary-theorem.md); [inspected theorem text](https://dokumen.pub/number-theory-volume-2-analytic-and-modern-tools-2-0387498931-9780387498935.html), [publisher chapter record](https://link.springer.com/chapter/10.1007/978-0-387-49894-2_6).

## Conclusion

There is no positive primitive solution at either ordered signature

\[
(4,3,4),\qquad (3,4,4).
\]

Consequently, an original Beal signature (x,y,z), with x,y,z>2, is excluded whenever

\[
(4\mid x,\ 3\mid y,\ 4\mid z)
\quad\text{or}\quad
(3\mid x,\ 4\mid y,\ 4\mid z).
\]

These are exclusions with unrestricted positive bases, not bounds on a finite search.

## Proof

**Source coprimality hypotheses.** For a positive solution a^r+b^s=c^t, any prime dividing two bases also divides the third. For example, a prime dividing a and b divides c^t and therefore c. A prime dividing a and c divides b^s and therefore b, and the remaining pair is identical. Thus gcd(a,b,c)=1 implies pairwise coprimality for an actual solution. This argument does not assert that gcd one implies pairwise coprimality for arbitrary triples.

**The two boundary placements.** A proposed primitive positive solution produces the following triple for Cohen's minus clause:

| Original equation | (X,Y,Z) in X^4-Y^4=Z^3 |
| --- | --- |
| a^4+b^3=c^4 | (c,a,b) |
| a^3+b^4=c^4 | (c,b,a) |

In the first row, c^4-a^4=b^3; in the second, c^4-b^4=a^3. These are direct rearrangements, with no negative sign absorbed into a fourth power. Each triple permutes the original coordinates, so every coordinate is nonzero and the pairwise coprimality just proved is preserved. Cohen's proposition contradicts each row. A coordinate equal to one remains nonzero and is permitted by the source. Also the original equation cannot have all three bases equal to one, since 1+1 is not 1; there is no hidden exceptional primitive solution at that boundary. No parity case is discarded.

**Exponent-divisor extensions.** Suppose A^x+B^y=C^z is a positive primitive solution at an original signature satisfying the first divisibility condition. Apply L002 with (r,s,t)=(4,3,4). It gives positive bases

\[
a=A^{x/4},\qquad b=B^{y/3},\qquad c=C^{z/4}
\]

with a^4+b^3=c^4 and gcd(a,b,c)=1. This contradicts the first row. Under the second condition, use (r,s,t)=(3,4,4) and bases A^{x/3}, B^{y/4}, C^{z/4}, contradicting the second row. L002 proves that these substitutions preserve prime support and primitivity, including bases equal to one. Only this forward substitution is used; no reduced solution is asserted to lift to a prescribed original signature.

**Threshold and remaining scope.** The achieved threshold is zero positive primitive integer solutions at both boundary placements and every original signature admitting the displayed exponent divisors. This closes the boundary gap in the assembled exclusions. It does not exclude unrelated mixed signatures or the repeated-cube primes left by L011, supply an upper height bound, or give a complete Beal argument. The zero-solution input is known and imported by precise citation; the proof above supplies its local applicability and the existing substitution consequence.

## Mathlib

Coverage of the full lemma: **not checked**. Supporting power, sign, and coprimality declarations were not checked. Cohen's Proposition 14.6.6 matches the external nonexistence input, while the placement and divisor arguments are given above. The source citation is not a claim of a matching Mathlib theorem or formal verification.

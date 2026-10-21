# L026 — Siksek–Stoll exclusions for the (3,4,5) placements

## Hypotheses

Let a,b,c be positive integers with gcd(a,b,c)=1. Bases equal to one are allowed.

The external input is S. Siksek and M. Stoll, *Partial descent on hyperelliptic curves and the generalized Fermat equation x^3+y^4+z^5=0*, **Bull. London Math. Soc. 44 (2012), 151–166, Theorem 1.1**. It classifies all signed integer triples (X,Y,Z) with gcd(X,Y,Z)=1 and X^3+Y^4+Z^5=0. The precise statement, manuscript version, essential proof cases and computational qualifications are recorded in [the foundation](../foundations/13-siksek-stoll-three-four-five-theorem.md); [author manuscript, July 4, 2011, p. 2](https://www.mathe2.uni-bayreuth.de/stoll/papers/345-revised.pdf#page=2), [publication](https://doi.org/10.1112/blms/bdr086).

For the exponent-divisor conclusion, let A,B,C,x,y,z be positive integers with x,y,z>2, gcd(A,B,C)=1 and A^x+B^y=C^z, as in L002.

## Conclusion

None of the following equations can hold:

\[
a^3+b^4=c^5,\qquad a^3+b^5=c^4,\qquad a^4+b^5=c^3.
\]

Interchanging the two summands also gives no positive primitive solutions. Consequently, an original primitive Beal solution cannot have a permutation (r,s,t) of (3,4,5) with r dividing x, s dividing y and t dividing z. This excludes all six ordered divisor patterns and includes every base-one case.

This is a fixed-signature import and its divisor consequence, not a resolution for arbitrary mixed exponents.

## Proof

Theorem 1.1 lists exactly

\[
(0,\pm1,-1),\quad(-1,0,1),\quad(1,0,-1),\quad(-1,\pm1,0)
\]

as the primitive signed integer solutions of X^3+Y^4+Z^5=0. Every listed triple has a zero coordinate. The source imposes no exclusion of coordinates of absolute value one and states the classification unconditionally.

For each possible positive equation use the following substitution:

| Positive equation | (X,Y,Z) | X^3+Y^4+Z^5 |
| --- | --- | --- |
| a^3+b^4=c^5 | (a,b,-c) | a^3+b^4-c^5=0 |
| a^3+b^5=c^4 | (-a,c,-b) | -a^3+c^4-b^5=0 |
| a^4+b^3=c^5 | (b,a,-c) | b^3+a^4-c^5=0 |
| a^4+b^5=c^3 | (-c,a,b) | -c^3+a^4+b^5=0 |
| a^5+b^3=c^4 | (-b,c,-a) | -b^3+c^4-a^5=0 |
| a^5+b^4=c^3 | (-c,b,a) | -c^3+b^4+a^5=0 |

The identities use (-u)^3=-u^3 and (-u)^5=-u^5. In the second row the fourth-power term stays positive: no invalid sign change of an even power is used. Each substitution only permutes the bases and changes signs, so gcd(X,Y,Z)=gcd(a,b,c)=1, where the gcd of signed integers is that of their absolute values. Positivity implies XYZ is nonzero. Thus each row contradicts the complete theorem list. This argument remains valid when any base equals one.

Pairwise coprimality, if required by a source convention, also follows here: a prime dividing any two bases divides two terms in the original equation and hence the third power, so divides the third base, contradicting gcd(a,b,c)=1. Sign changes and permutations preserve this property. No pairwise hypothesis on arbitrary triples is assumed.

The displayed signatures are exactly (3,4,5), (3,5,4), (4,3,5), (4,5,3), (5,3,4), and (5,4,3), exhausting the six permutations. Rows three, five and six explicitly include the summand swaps of rows one, two and four, respectively.

Finally suppose there is a permutation (r,s,t) with r|x, s|y and t|z. L002 supplies positive integer bases

\[
a=A^{x/r},\qquad b=B^{y/s},\qquad c=C^{z/t}
\]

with a^r+b^s=c^t and gcd(a,b,c)=1. The quotients are positive integers; by L002 each base has exactly the prime support of its original base, including empty prime support for a base equal to one. The reduced signature is one of the six excluded permutations. This contradiction proves the divisor consequence without asserting a reverse lift to any prescribed original signature.

The theorem's descent, Edwards parametrization, MAGMA Selmer calculations and Mordell–Weil computations are imported by the precise citation, not independently reproduced. The foundation retains the unprinted individual computational outputs and original-Edwards-access limitation. No exceptional-algebra hypothesis or modular-packet claim from the mixed-seventh work is used.

### Critical application audit — 2026-10-06, step 054

Checked all six displayed identities separately against the source equation and complete solution list. Each row uses every base once, with only signs and permutations; consequently all retain gcd one and nonzero coordinates. Every source triple has a zero coordinate, so none can equal a transformed triple, even if one or more bases is one. For each ordered divisor pattern, 3,4,5 belong to L002's set S and its three divisibility hypotheses make x/r, y/s, z/t positive integers. The power identities and prime-support argument in L002 therefore apply independently in every row; no common exponent divisor or reverse lift is needed. The required threshold is zero positive primitive solutions in each of these six divisor families, and the cited classification supplies exactly that threshold. No failing placement or correction to the argument was found. This audits the local applicability only; the published classification and its computations remain cited inputs, and no additional signature is excluded.

## Mathlib

Coverage of the full classification and this placement/divisor lemma: **not checked**. Supporting sign, power and coprimality declarations were not checked. The named theorem matches the external signed classification; the local substitutions and L002 application are proved above. The source links are mathematical references, not claims of matching formal declarations or independent computational certification.

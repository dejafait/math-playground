# L005 — Kraus's restriction selects the ramified cube branch

## Hypotheses

Let p >= 17 be prime. A cube solution means positive integers a,b,c with

\[
a^3+b^3=c^p,\qquad \gcd(a,b,c)=1.
\]

Bases equal to one are permitted. Set s=a+b, q=a^2-ab+b^2, and d=a-b. The notation v_ell denotes the prime valuation of a nonzero integer, using its absolute value. The external input is Kraus's divisibility restriction in the precise published restatements recorded in [the foundation](../foundations/04-kraus-divisibility-restriction.md).

## Conclusion

Every cube solution satisfies

\[
c\equiv3\pmod6,\qquad v_2(ab)=1.
\]

Consequently only branch II of L003 can occur. Its unique positive coprime parameters obey

\[
s=3^{p-1}u^p,\qquad q=3v^p,\qquad c=3uv,
\]

with u odd, v congruent to 1 modulo 12, and 3 not dividing v. The integer d is odd, 3 does not divide d, and

\[
d^2+3^{2p-3}u^{2p}=4v^p,\qquad |d|<3^{p-1}u^p,
\qquad v_2(s^2-d^2)=3.
\]

The parameter u may still be divisible by 3. After interchanging a,b if necessary, v_2(a)=1 and b is odd.

For every prime p >= 17, the complete system I of L003 has no solution. Every solution of its system II must satisfy the additional restrictions above, and retains L003's exact converse. No condition on p modulo 3 is imposed for these statements. Emptiness of the remaining system is not asserted.

## Proof

**The cited global input and its normalization.** A prime dividing any two of a,b,c divides the third by the equation, so these positive primitive solutions are pairwise coprime. Thus they meet the nonzero-coprime hypotheses of Bennett–Chen–Dahmen–Yazdani, *Generalized Fermat equations: A miscellany*, Proposition 7, printed p. 6, restricted to prime p >= 17. That source explicitly attributes this prime range to Kraus. It gives c congruent to 3 modulo 6 and v_2(ab)=1. These are the external mathematical input, not conclusions of an elementary congruence argument. The foundation records the source-access and historical-modularity qualifications.

Since v_2(a)+v_2(b)=1 and both valuations are nonnegative integers, one coordinate has valuation one and the other valuation zero. Interchanging the summands preserves the equation and primitivity, and permits the stated labeling. No conclusion is obtained by applying an asymmetric wording twice to the two labelings.

**Selection of the branch.** We have 3 dividing c. Reduction modulo 3, using t^3 congruent to t, gives 3 dividing a+b. L003 therefore gives its second factor split, with positive coprime u,v and 3 not dividing v. Its square identity and positivity give the displayed equation and strict inequality. Since c=3uv is odd, both u and v are odd. The odd and even parities of a,b give d odd.

Neither a nor b can be divisible by 3: if, for example, 3 divided a, the equation and 3 dividing c would force 3 dividing b, contrary to primitivity. Since b is congruent to -a modulo 3, d is congruent to 2a modulo 3 and is nonzero there. The identity s^2-d^2=4ab then gives v_2(s^2-d^2)=2+v_2(ab)=3. This valuation is well-defined since ab>0.

**Restriction on v.** Because s is odd and ab is congruent to 2 modulo 4,

\[
q=s^2-3ab\equiv1-3\cdot2\equiv3\pmod4.
\]

On the other hand q=3v^p. Since p and v are odd, v^p is congruent to v modulo 4; multiplying by the inverse of 3 modulo 4 gives v congruent to 1 modulo 4. L003 proves that every prime divisor of v is congruent to 1 modulo 3, so v is congruent to 1 modulo 3, including v=1. Combining these two congruences yields v congruent to 1 modulo 12. Nothing in this argument changes the allowed 3-adic valuation of u.

**The complete systems.** Suppose system I of L003 had data at n=p. Its converse produces a positive primitive cube solution with c=uv and 3 not dividing uv. This contradicts the cited conclusion 3 dividing c. Thus I is empty throughout the stated prime range, including p congruent to 1 modulo 3.

Similarly, any data in II produce a positive primitive cube solution by L003. Applying what was just proved forces all the additional restrictions. Conversely, data satisfying II together with those restrictions still reconstruct a cube solution by the same converse. The restrictions are necessary filters on II, not a replacement of its equation by isolated congruences.

**Scope and threshold.** The intermediate target was emptiness of branch I for every prime p >= 17; this is achieved by the cited global input. The full family requires emptiness of both branches. At complementary primes p congruent to 1 modulo 3, the assembled argument still leaves the constrained system II. Its interval for v from L003 has width proportional to u^2 for fixed p. Restricting u to odd numbers and v to a class modulo 12 supplies no upper height bound and does not establish emptiness. No conclusion at p=5,7,11,13 is added by this application. Other residual signatures are outside its scope.

The stopped unrestricted-congruence and single-factor shortcuts are not premises here. In particular a global modular restriction on integer solutions is compatible with the existence of unrestricted solutions over each local field.

## Mathlib

Coverage of the full statement: **not checked**. Supporting valuation, parity, and congruence declarations: **not checked**. The precise external match for the global restriction is Proposition 7 on the prime range specified in the foundation, corroborated by Freitas's Theorem 1; full modularity is a supporting result. The branch elimination and auxiliary congruences are proved above. No absence claim or formal-verification claim is made.

# L003 — Exact factor conditions for a primitive sum of two cubes

## Hypotheses

Let n >= 2 be an integer. A solution means positive integers a,b,c with

\[
a^3+b^3=c^n,\qquad \gcd(a,b,c)=1.
\]

The active Beal subfamily has n=p >= 5 prime. Primality is not needed for this reduction; the n=2 instances below are controls outside Beal's exponent range. No base-one case is discarded. For a solution set s=a+b, q=a^2-ab+b^2, and d=a-b. The valuation v_3 is the exponent of 3 in a positive integer.

## Conclusion

Exactly one of the following two branches holds, with uniquely determined positive coprime integers u,v:

| Branch | Exact factor conditions | Additional restriction |
| --- | --- | --- |
| 3 does not divide s | s=u^n, q=v^n, c=uv | 3 does not divide uv |
| 3 divides s | s=3^(n-1)u^n, q=3v^n, c=3uv | 3 does not divide v; 3 may divide u |

In the second branch,

\[
v_3(q)=1,\qquad v_3(s)=n\,v_3(c)-1=n-1+n\,v_3(u).
\]

There is an exact converse expressed by either of these two systems, where u,v are positive integers and d is an integer:

\[
\begin{aligned}
\text{I:}\quad &\gcd(u,v)=1,\quad 3\nmid uv,\\
&u^{2n}+3d^2=4v^n,\qquad |d|<u^n;\\[3pt]
\text{II:}\quad &\gcd(u,v)=1,\quad 3\nmid v,\\
&d^2+3^{2n-3}u^{2n}=4v^n,\qquad |d|<3^{n-1}u^n.
\end{aligned}
\]

For I set s=u^n, c=uv; for II set s=3^(n-1)u^n, c=3uv. In either case

\[
a=(s+d)/2,\qquad b=(s-d)/2
\]

are automatically positive coprime integers and solve a^3+b^3=c^n. The displayed systems thus lose neither parity nor primitivity conditions. Changing d to -d interchanges the summands.

In either branch, every prime divisor ell of v satisfies ell congruent to 1 modulo 3. Positivity also forces the bounds

\[
\begin{array}{ll}
\text{I:}&4^{-1/n}u^2\le v<u^2,\\
\text{II:}&4^{-1/n}3^{2-3/n}u^2\le v<3^{2-3/n}u^2.
\end{array}
\]

These are simultaneous power-and-square conditions, not an exclusion of either branch. The interval widths grow proportionally to u^2 for each fixed n; they give no uniform upper bound on u. The ramified branch gives the lower bound s >= 3^(n-1), not an upper bound on a solution's height.

## Proof

**Primitivity and the gcd of the factors.** In an actual solution, a prime dividing any two of a,b,c divides the third by the equation. Hence gcd(a,b,c)=1 implies that a,b,c are pairwise coprime. In particular gcd(a,b)=1. The identities

\[
a^3+b^3=(a+b)(a^2-ab+b^2)=sq,\qquad q=s^2-3ab
\]

hold over the integers. A common divisor of s and either a or b would divide both a and b, so gcd(s,ab)=1. Therefore

\[
\gcd(s,q)=\gcd(s,3ab)=\gcd(s,3).
\]

If 3 does not divide s, the factors are coprime. If 3 divides s, write s=3k. Neither a nor b is then divisible by 3, since otherwise both would be. Consequently

\[
q=3(3k^2-ab),\qquad 3\nmid(3k^2-ab),
\]

which proves v_3(q)=1 exactly, not merely 3 dividing q.

**Allocation of prime powers.** When 3 does not divide s, the positive coprime integers s and q have product c^n. For each prime ell, the exponent in this product is n times its exponent in c. The prime occurs in at most one factor, so its exponent in that factor is a multiple of n. Unique factorization in the positive integers gives s=u^n and q=v^n with gcd(u,v)=1. Positivity and c^n=(uv)^n give c=uv. The gcd identity and q congruent to s^2 modulo 3 give 3 not dividing uv.

When 3 divides s, put k=v_3(c). From sq=c^n and v_3(q)=1 we get v_3(s)=nk-1. Since v_3(s)>=1, k>=1. Every prime ell other than 3 occurs in at most one factor and with exponent divisible by n. Thus q=3v^n with 3 not dividing v, and

\[
s=3^{nk-1}w^n=3^{n-1}(3^{k-1}w)^n
\]

for an integer w coprime to 3. Set u=3^{k-1}w. No prime can divide both u and v, because their non-3 primes occur in separate factors and v is prime to 3. Then sq=(3uv)^n, so c=3uv. This also proves the asserted valuation formula. Prime factorization, or uniqueness of positive nth roots, proves uniqueness of u and v in both branches.

**The square condition and the converse.** Direct expansion gives

\[
4q=s^2+3d^2.
\]

Positive a,b imply |d|<s. Substituting the first factor conditions gives I. Substituting the second and dividing by 3 gives II; the exponent 2n-3 is nonnegative because n>=2.

Conversely, suppose I or II holds. Define s,c as in the conclusion, and put q=v^n in I or q=3v^n in II. Both systems imply 4q=s^2+3d^2. Modulo 4 this forces s and d to have the same parity: a square is 0 or 1, and the mixed-parity possibilities give a residue 1 or 3 rather than 0. Thus (s+d)/2 and (s-d)/2 are integers. The strict inequality |d|<s makes them positive. Their sum is s and their difference is d, so the same identity shows that their quadratic factor a^2-ab+b^2 is q.

It remains to verify coprimality instead of assuming it in the converse. In I, gcd(s,q)=gcd(u^n,v^n)=1. Any prime common to a and b would divide s and q, which is impossible. In II, the restrictions on u,v give gcd(s,q)=3 and v_3(q)=1. A prime common to a and b would therefore have to be 3; but then each term in a^2-ab+b^2 would be divisible by 9, contradicting v_3(q)=1. Hence gcd(a,b)=1 in both cases. Finally,

\[
a^3+b^3=sq=(uv)^n\quad\text{or}\quad sq=(3uv)^n,
\]

as appropriate. This proves the equation and gcd(a,b,c)=1. The earlier prime-divisor argument also gives pairwise coprimality with c.

**Prime support of the quadratic factor.** Let ell be a prime dividing q, with ell different from 3. Coprimality of a,b shows that ell does not divide b: otherwise q congruent to a^2 modulo ell would force ell to divide a. In the nonzero residues modulo ell put t=-a/b. Then

\[
t^2+t+1=0,\qquad t^3=1.
\]

If t=1, the first equation would give ell=3, excluded here. Thus t has multiplicative order exactly 3. Lagrange's theorem in the group of ell-1 nonzero residues gives 3 dividing ell-1. Every prime divisor of v divides q and is different from 3, so it satisfies the claimed condition. In particular v is odd and v is congruent to 1 modulo 3, with v=1 permitted by this assertion alone.

**Size and feasibility checks.** The positive numbers a,b satisfy 0<ab<=s^2/4, whence

\[
s^2/4\le q=s^2-3ab<s^2.
\]

Substitution of either factor split and taking positive nth roots proves the stated intervals. Their respective widths are (1-4^(-1/n))u^2 and 3^(2-3/n)(1-4^(-1/n))u^2. Thus this estimate does not tend to a subunit interval as u grows for a fixed n. It does not claim that every interval contains a v meeting the other constraints.

The individual quadratic-factor conditions have positive coprime witnesses already at n=5:

\[
62^2-62\cdot149+149^2=16807=7^5,
\]

while 62+149=211 lies strictly between 2^5 and 3^5 and is not a fifth power. Also

\[
211^2-211\cdot236+236^2=50421=3\cdot7^5,
\]

while 211+236=447=3\cdot149 has 3-adic valuation one, not 4 modulo 5. The gcds of these two pairs are one, as the Euclidean algorithm verifies. They show that neither q=v^p nor q=3v^p is itself contradictory under positivity and coprimality. Neither pair is a Beal solution because its sum fails the other required factor condition.

Conversely, the factor-power shapes and the size and prime-support constraints do not automatically make the discriminant a square. In I, n=5,u=4,v=13 gives s=1024, q=371293 and

\[
(4q-s^2)/3=145532,\qquad 381^2<145532<382^2.
\]

In II, n=5,u=3,v=37 gives s=19683, q=208031871 and

\[
(4q-s^2)/3=148235665,\qquad 12175^2<148235665<12176^2.
\]

Both have 0<(4q-s^2)/3<s^2; both have coprime u,v and allowed prime support for v. The second explicitly allows 3 to divide u. They are candidate factor data rejected by the remaining square condition, not integer solutions a,b. These controls locate the missing simultaneous constraint; they are not evidence of its uniform unsolvability.

At n=2 the converse has genuine positive controls: (a,b,c)=(56,65,671) gives s=11^2, q=61^2 in I, and (a,b,c)=(1,2,3) gives s=3, q=3 in II with u=v=1. These lie outside Beal's exponent range. They check that the second branch cannot be discarded just from its exceptional-prime valuation, and that the reduction retains base-one cases.

The desired family exclusion still requires proving that I and II have no solutions for every prime n>=5. No such exclusion or decreasing-height construction is proved here. Other residual Beal signatures remain outside this lemma's scope.

## Mathlib

Coverage of the full statement: **not checked**. Supporting results on prime valuations, coprime factors of perfect powers, finite-field multiplicative order, and parity were not looked up; no matching theorem name or absence claim is asserted. The integer-factorization and converse arguments are proved above. The familiar gcd-of-factors observation also appears in Bennett–Mihailescu–Siksek, [The Generalized Fermat Equation, section 2, PDF pages 3–4](https://samirsiksek.github.io/siksek.github.io/papers/bealconj.pdf#page=3); that source is supporting mathematical context, not a Mathlib match or an exclusion of this entire family.

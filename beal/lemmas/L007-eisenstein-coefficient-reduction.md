# L007 — An exact coefficient condition for the ramified cube branch

## Hypotheses

Let p >= 5 be prime, and let u,v be positive coprime integers with u odd and v congruent to 1 modulo 12. Suppose d is an integer satisfying the constrained system II of L003:

\[
d^2+3^{2p-3}u^{2p}=4v^p,\qquad |d|<3^{p-1}u^p.
\]

These explicit hypotheses include the surviving branch singled out by L005 at primes p >= 19 congruent to 1 modulo 3. No theorem about integer cube solutions is applied to local points here. Write delta=sqrt(-3), zeta=(1+delta)/2, and R=Z[zeta]. Put W=3^(p-2)u^p, so the displayed equation is d^2+3W^2=4v^p. Valuations of signed nonzero integers mean valuations of their absolute values.

## Conclusion

There are odd integers r,t with t nonzero such that

\[
\gcd(r,t)=\gcd(r,v)=\gcd(t,v)=1,\qquad 3\nmid r,
\qquad r^2+3t^2=4v,
\]

and

\[
\frac{d+W\delta}{2}=\left(\frac{r+t\delta}{2}\right)^p.
\]

Define integer sequences by

\[
U_0=0,\quad U_1=1,\qquad T_0=2,\quad T_1=r,
\qquad X_{n+2}=rX_{n+1}-vX_n
\]

for either X=U or X=T. Then the retained simultaneous coefficient condition is

\[
d=T_p,\qquad tU_p=3^{p-2}u^p,
\tag{1}
\]

with the explicit formula

\[
2^{p-1}U_p=
\sum_{j=0}^{(p-1)/2}\binom{p}{2j+1}
r^{p-2j-1}(-3t^2)^j.
\tag{2}
\]

In particular 3 does not divide U_p and

\[
v_3(t)=p-2+p\,v_3(u).
\tag{3}
\]

The possible common factor in (1) is exact:

\[
\gcd(|t|,|U_p|)=
\begin{cases}1,&p\nmid t,\\p,&p\mid t,\end{cases}
\qquad
p\mid U_p\ \Longleftrightarrow\ p\mid t,
\qquad p\mid t\ \Longrightarrow\ v_p(U_p)=1.
\tag{4}
\]

Consequently, for positive coprime odd integers h,k and sigma=sgn(t), exactly one of these shapes holds:

| Case | t | U_p | u | Further restrictions |
| --- | --- | --- | --- | --- |
| p does not divide t | sigma 3^(p-2) h^p | sigma k^p | hk | 3 does not divide k; p does not divide hk |
| p divides t | sigma 3^(p-2) p^(p-1) h^p | sigma p k^p | phk | gcd(k,3p)=1 |

In the second case p may divide h. In both cases 3 may divide h. The sign sigma is retained: positivity of W does not imply that t or U_p is individually positive.

There is an exact converse. Take odd coprime r,t with t nonzero, set v=(r^2+3t^2)/4, and require v congruent to 1 modulo 12. Define U,T by the recurrence above. If a positive integer u satisfies (1)'s coefficient equality and

\[
|T_p|<3^{p-1}u^p,
\tag{5}
\]

then u is automatically odd and coprime to v. With d=T_p, these data satisfy the stated system II. In particular

\[
a=(3^{p-1}u^p+T_p)/2,\qquad
b=(3^{p-1}u^p-T_p)/2,\qquad c=3uv
\]

are positive primitive integers satisfying a^3+b^3=c^p. Thus neither the coefficient equality nor the positivity bound can be dropped from this parameterization. No solution or exclusion of this complete system is asserted.

## Proof

**The ring and its units.** The relation zeta^2=zeta-1 shows that R is closed under multiplication and conjugation. Its elements are precisely (r+t delta)/2 for integers r,t of the same parity. Its norm is

\[
N(a+b\zeta)=a^2+ab+b^2=(a+b/2)^2+3b^2/4.
\]

It is a nonnegative integer, is positive on nonzero elements, and is multiplicative by complex conjugation. For any complex number written x+y zeta with real x,y, choose integers a,b with |x-a|,|y-b| <= 1/2. Then N((x-a)+(y-b)zeta) <= 3/4 < 1. Applying this to a quotient of two elements of R proves Euclidean division with the norm. The Euclidean algorithm gives Bezout identities. An irreducible is prime by Bezout; every nonunit factors into irreducibles because any nontrivial factorization strictly decreases its positive integer norm. Hence R has unique factorization, with no class-number assumption left unstated.

Units have norm one, and solving (2a+b)^2+3b^2=4 gives exactly the six powers of zeta. They form a group of order six. Since gcd(p,6)=1, raising a unit to the pth power permutes this group.

**Coprime conjugates and power extraction.** Since u is odd, W is odd; the equation modulo 4 makes d odd. Therefore alpha=(d+W delta)/2 belongs to R, with N(alpha)=v^p. Suppose an irreducible pi of R divided both alpha and its conjugate. Then pi divides v, since pi divides v^p and is prime. It also divides their difference W delta. Because W=3^(p-2)u^p and delta^2=-3, this forces pi to divide 3 or u. Either possibility contradicts gcd(v,3u)=1: a rational integer Bezout identity would make pi divide 1. Thus alpha and its conjugate are coprime in R. This also checks the primes above 2 and 3 without assuming that rational primes remain prime in R.

Every irreducible factor of alpha has exponent divisible by p, because alpha times its coprime conjugate is the pth power v^p. Unique factorization gives alpha=epsilon eta^p for a unit epsilon. Absorb epsilon using the unit-group fact just proved to obtain alpha=gamma^p. Write gamma=(r+t delta)/2, with r,t integers of the same parity. Taking norms gives N(gamma)=v and r^2+3t^2=4v.

If r,t were both even, gamma would belong to Z[delta], and so would gamma^p. But alpha has odd half-integer coefficients in the linearly independent basis 1,delta. This is impossible. Hence r,t are odd; in particular t is nonzero. The elements gamma and its conjugate are coprime, since any common divisor would divide alpha and its conjugate. If an odd rational prime ell divided both r and t, then gamma/ell and its conjugate would still belong to R, contradicting that coprimality. The prime 2 divides neither r nor t. Thus gcd(r,t)=1.

The norm equality modulo 3 and 3 not dividing v give 3 not dividing r. A prime common to r and v would divide 3t^2 by the norm equality; neither 3 nor a prime factor of t is possible. This gives gcd(r,v)=1. A prime common to t and v would divide r^2, so gcd(t,v)=1 as well. There is no prime-2 exception since r,t are odd.

**The coefficient and its recurrence.** The two numbers gamma and its conjugate are roots of X^2-rX+v. Their powers therefore obey the stated recurrence. The initial values show that

\[
T_n=\gamma^n+\bar\gamma^n,\qquad
U_n=\frac{\gamma^n-\bar\gamma^n}{\gamma-\bar\gamma}.
\]

The denominator t delta is nonzero. These quantities are ordinary integers by the recurrence. Comparing alpha=gamma^p and its conjugate gives d=T_p and W=tU_p. Expanding the difference of the pth powers of (r+t delta)/2 proves (2), including its denominator 2^(p-1). This denominator is not an omitted integrality condition: integrality has already been proved by the recurrence.

**Valuations at 3 and the common factors.** Reducing (2) modulo 3 leaves only p r^(p-1). It is nonzero there, since p >= 5 is prime and 3 does not divide r. The denominator is invertible modulo 3, so 3 does not divide U_p. Taking the 3-adic valuation of (1) proves (3).

If an odd prime ell divides t, reduce (2) modulo ell. All but the first summand vanish, giving

\[
2^{p-1}U_p\equiv p r^{p-1}\pmod\ell.
\]

Since gcd(r,t)=1, a common prime divisor of t and U_p can only be p. There is no common factor at 2 because t is odd.

If p does not divide t, all the binomial coefficients in (2) except the final one are divisible by p. Therefore

\[
2^{p-1}U_p\equiv(-3t^2)^{(p-1)/2}\not\equiv0\pmod p.
\]

If p divides t, then p does not divide r. The j=0 summand of (2) is p r^(p-1) and has valuation one. For 1 <= j < (p-1)/2 the binomial coefficient is divisible by p and t^(2j) by p^2; these terms have valuation at least three. The final term has valuation at least p-1 >= 4. Hence the sum has valuation exactly one at p; division by 2^(p-1) preserves it. This proves all of (4).

**Exact allocation into the two shapes.** Since W>0, the nonzero factors t and U_p have the same sign sigma. Their absolute-value product is 3^(p-2)u^p. All its prime valuations away from 3 are multiples of p, and the 3-adic valuation is p-2+p v_3(u).

If p does not divide t, (4) makes the two absolute values coprime. Each prime therefore belongs to only one factor. All the 3-adic contribution belongs to t, by (3). Taking the resulting positive pth roots gives |t|=3^(p-2)h^p, |U_p|=k^p, and u=hk. The claimed coprimality and restrictions on h,k follow from those prime allocations.

If p divides t, put e=v_p(t). Equation (1) and v_p(U_p)=1 give e+1=p v_p(u). Thus e=p-1+p(v_p(u)-1), with v_p(u)>=1. Remove 3^(p-2)p^(p-1) from |t| and p from |U_p|. Each remaining prime valuation is a multiple of p, so the remaining factors are h^p and k^p. Their only possible common prime was p, and the second remaining factor is prime to p. This proves the second shape, gcd(h,k)=1, and gcd(k,3p)=1. All h,k are odd because t and W are odd. None of these allocations excludes either shape.

**Converse, including the omitted-looking conditions.** Start with r,t,v,u as in the converse. In R set gamma=(r+t delta)/2. The same recurrence identities give gamma^p=(T_p+tU_p delta)/2. Taking norms and using the coefficient equality yields

\[
T_p^2+3^{2p-3}u^{2p}=4v^p.
\]

Because v is 1 modulo 12, it is odd and prime to 3. The norm identity and gcd(r,t)=1 again give gcd(r,v)=gcd(t,v)=1. Modulo v the recurrence gives U_n congruent to r^(n-1) for n>=1, so gcd(U_p,v)=1. Consequently gcd(tU_p,v)=1; the coefficient equality forces gcd(u,v)=1.

Modulo 2, the recurrence for U, with r,v odd, cycles through 0,1,1. Since the prime p>=5 is not divisible by 3, U_p is odd. The coefficient equality then makes u odd. With d=T_p, the displayed norm identity and (5) are precisely system II of L003. Its converse proves integral positive primitive a,b,c as stated. In particular the strict bound (5) is still needed; a norm representation alone is insufficient.

**Scope, test, and achieved threshold.** The intermediate target is met: the global square condition has an exact power extraction, the sum-power condition becomes (1), and its factor allocations retain both the ramified factor 3 and the possible common factor p. Equations (3) and (4) are necessary constraints beyond merely writing a norm as v^p. This is not a decreasing-height argument. Although v=(r^2+3t^2)/4 fixes a norm, r and t remain unbounded. In particular (3) forces |t| >= 3^(p-2), a lower bound, not the upper bound that would enable a finite exhaustion.

The required family threshold is zero solutions satisfying the coefficient equality, the norm relation, and (5). No such exclusion is proved. A theorem that supplies a prime divisor of U_p alone would be compatible with U_p=sigma k^p or sigma p k^p; it would need an additional restriction on multiplicities or on the full simultaneous system. The smaller repeated-cube cases and other residual Beal signatures are not resolved here.

As a sign and normalization control, p=5,r=5,t=1 gives v=7, U_5=149, T_5=-25. Thus the isolated norm representation recovers the quadratic-factor witness (a,b)=(211,236) from L003 by setting s=3tU_5. It fails (1), since 149 is not 3^3 times a positive fifth power. This is not an instance of the present hypotheses or a Beal solution. The control confirms that the retained coefficient condition distinguishes the previously failed single-factor test.

The bounded exact-arithmetic checks in scripts/eisenstein-coefficient/check_coefficients.py compare ring multiplication, both recurrence sequences, and the binomial formula independently; exercise both p-divisibility cases and signed t; and check the existing isolated-factor control. They supplement the proofs, without a bounded search being used to infer emptiness.

## Mathlib

Coverage of the full statement: **not checked**. Supporting declarations for Eisenstein-integer Euclidean division, unit groups, coprime perfect-power extraction, Lucas recurrences, and valuations: **not checked**. No matching declaration or absence claim is asserted. The ring arithmetic, unit absorption, coefficient formula, and valuation arguments are proved here; L003 supplies the integer reconstruction. No primitive-divisor theorem is an input to this result.
